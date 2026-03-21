#!/usr/bin/env python3
"""
mscz_utils.py — Shared utilities for MuseScore (.mscz) transformation scripts.

All transformation scripts in tools/ import from here.
"""

import xml.etree.ElementTree as ET
import zipfile, shutil, os, base64, subprocess

MUSESCORE_CLI = '/Applications/MuseScore 4.app/Contents/MacOS/mscore'

# ── TPC ──────────────────────────────────────────────────────────────────────

_CONCERT_TPC = {
    0: 14,   # C
    1:  9,   # Db
    2: 16,   # D
    3: 11,   # Eb
    4: 18,   # E
    5: 13,   # F
    6:  8,   # Gb
    7: 15,   # G
    8: 10,   # Ab
    9: 17,   # A
    10: 12,  # Bb
    11: 19,  # B
}

def pitch_to_tpc(midi_pitch):
    """Return (tpc_concert, tpc_written) for Bb trumpet.
    tpc_written = tpc_concert + 2 (major 2nd transposition).
    """
    tpc_c = _CONCERT_TPC[midi_pitch % 12]
    return tpc_c, tpc_c + 2

# ── EID ──────────────────────────────────────────────────────────────────────

def gen_eid():
    """Generate a 23-char EID in MuseScore's format: 11_11."""
    raw = os.urandom(16)
    b64 = base64.b64encode(raw).decode('ascii').rstrip('=')[:22].ljust(22, 'A')
    return b64[:11] + '_' + b64[11:22]

# ── XML builders ─────────────────────────────────────────────────────────────

def make_chord(pitch, duration):
    """<Chord> with one <Note>."""
    tpc_c, tpc_w = pitch_to_tpc(pitch)
    chord = ET.Element('Chord')
    ET.SubElement(chord, 'eid').text = gen_eid()
    ET.SubElement(chord, 'durationType').text = duration
    note = ET.SubElement(chord, 'Note')
    ET.SubElement(note, 'eid').text = gen_eid()
    ET.SubElement(note, 'pitch').text = str(pitch)
    ET.SubElement(note, 'tpc').text = str(tpc_c)
    ET.SubElement(note, 'tpc2').text = str(tpc_w)
    return chord

def make_rest(duration, dotted=False):
    """<Rest> element."""
    rest = ET.Element('Rest')
    ET.SubElement(rest, 'eid').text = gen_eid()
    if dotted:
        ET.SubElement(rest, 'dots').text = '1'
    ET.SubElement(rest, 'durationType').text = duration
    return rest

def get_first_note_pitch(measure):
    """MIDI pitch of the first note in a measure, or None."""
    chord = measure.find('.//Chord')
    if chord is None:
        return None
    note = chord.find('Note')
    if note is None:
        return None
    return int(note.find('pitch').text)

# ── File I/O ─────────────────────────────────────────────────────────────────

def open_mscz(mscz_path, work_dir):
    """Extract .mscz to work_dir. Returns (ET tree, mscx_path, zip namelist)."""
    shutil.rmtree(work_dir, ignore_errors=True)
    os.makedirs(work_dir)
    with zipfile.ZipFile(mscz_path, 'r') as z:
        names = z.namelist()
        z.extractall(work_dir)
    mscx_name = next(n for n in names if n.endswith('.mscx'))
    mscx_path = os.path.join(work_dir, mscx_name)
    tree = ET.parse(mscx_path)
    return tree, mscx_path, names

def save_mscz(tree, mscx_path, names, work_dir, output_mscz):
    """Write modified tree to mscx and repackage as .mscz."""
    ET.indent(tree, space='  ')
    tree.write(mscx_path, encoding='UTF-8', xml_declaration=True)
    with zipfile.ZipFile(output_mscz, 'w', zipfile.ZIP_DEFLATED) as z:
        for name in names:
            z.write(os.path.join(work_dir, name), name)

def export_pdf(mscz_path, pdf_path):
    """Export .mscz to PDF via MuseScore CLI. Returns True if file created."""
    subprocess.run([MUSESCORE_CLI, '-f', '-o', pdf_path, mscz_path],
                   capture_output=True)
    return os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0

# ── Phrase parsing ────────────────────────────────────────────────────────────

def get_measures(root):
    """Return list of Measure elements from Staff id=1."""
    staff = root.find('.//Staff[@id="1"]')
    return [c for c in staff if c.tag == 'Measure']

def iter_phrases(measures, phrase_size=4):
    """Yield (phrase_idx, m_ii, m_v, m_i, m_rest) for each phrase."""
    for i in range(len(measures) // phrase_size):
        base = i * phrase_size
        yield i, measures[base], measures[base+1], measures[base+2], measures[base+3]
