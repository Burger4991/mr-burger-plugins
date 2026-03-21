#!/usr/bin/env python3
"""
add_enclosures.py — Bert Ligon Outlines: chromatic enclosure generator

For each ii-V-I-rest phrase:
  - Modifies the REST measure to end with 2 eighth notes approaching
    beat 1 of the NEXT phrase's ii chord (chromatic: above → below → target)
  - Replaces the LAST beat of the ii chord measure with 2 eighth notes
    approaching beat 1 of the V chord measure (chromatic: above → below → target)

Enclosure pattern: [target+1 semitone] [target-1 semitone] → TARGET on beat 1

Usage: python3 add_enclosures.py
"""

import xml.etree.ElementTree as ET
import zipfile
import shutil
import os
import base64
import random

# ─── TPC helpers ─────────────────────────────────────────────────────────────

# Concert TPC values, preferring flat spellings for chromatic notes.
# MuseScore TPC: C=14, along circle of fifths ±1 per 5th.
# Flats: Bb=12, Eb=11, Ab=10, Db=9, Gb=8
# Sharps: F#=20, C#=21, G#=22, D#=23, A#=24
_CONCERT_TPC = {
    0:  14,  # C
    1:   9,  # Db  (prefer flat over C#=21)
    2:  16,  # D
    3:  11,  # Eb  (prefer flat over D#=23)
    4:  18,  # E
    5:  13,  # F
    6:   8,  # Gb  (prefer flat over F#=20)
    7:  15,  # G
    8:  10,  # Ab  (prefer flat over G#=22)
    9:  17,  # A
    10: 12,  # Bb  (prefer flat over A#=24)
    11: 19,  # B
}

def pitch_to_tpc(midi_pitch):
    """Return (tpc_concert, tpc_written) for a MIDI pitch on Bb trumpet.
    Bb trumpet: written = concert + major 2nd → tpc_written = tpc_concert + 2.
    """
    pc = midi_pitch % 12
    tpc_c = _CONCERT_TPC[pc]
    tpc_w = tpc_c + 2
    return tpc_c, tpc_w


# ─── EID generator ───────────────────────────────────────────────────────────

def gen_eid():
    """Generate a 23-char EID matching MuseScore's format: 11_11."""
    raw = os.urandom(16)
    b64 = base64.b64encode(raw).decode('ascii').rstrip('=')
    b64 = b64[:22].ljust(22, 'A')
    return b64[:11] + '_' + b64[11:22]


# ─── XML builders ────────────────────────────────────────────────────────────

def make_chord(pitch, duration):
    """Build a <Chord> element with one <Note>."""
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
    """Build a <Rest> element."""
    rest = ET.Element('Rest')
    ET.SubElement(rest, 'eid').text = gen_eid()
    if dotted:
        ET.SubElement(rest, 'dots').text = '1'
    ET.SubElement(rest, 'durationType').text = duration
    return rest


# ─── Measure queries ─────────────────────────────────────────────────────────

def get_first_note_pitch(measure):
    """Return MIDI pitch of the first note in a measure, or None."""
    chord = measure.find('.//Chord')
    if chord is None:
        return None
    note = chord.find('Note')
    if note is None:
        return None
    return int(note.find('pitch').text)


# ─── Measure modifiers ───────────────────────────────────────────────────────

def add_enclosure_to_rest_measure(measure, target_pitch):
    """
    Replace whole-measure rest with: dotted-half rest + enc_above(8th) + enc_below(8th).
    The target_pitch is beat 1 of the NEXT measure.
    Enclosure: [target+1] [target-1] → target
    """
    voice = measure.find('voice')
    if voice is None:
        return

    # Remove all Rest elements
    for rest in list(voice.findall('Rest')):
        voice.remove(rest)

    # Dotted half rest (3 beats)
    voice.append(make_rest('half', dotted=True))

    # Two eighth notes: above → below → target on beat 1 of next measure
    voice.append(make_chord(target_pitch + 1, 'eighth'))
    voice.append(make_chord(target_pitch - 1, 'eighth'))


def add_enclosure_to_ii_measure(measure, v_target_pitch):
    """
    Replace the last quarter note of the ii chord measure with 2 eighth notes
    approaching v_target_pitch: [v_target+1] [v_target-1] → v_target on beat 1 of V measure.
    """
    voice = measure.find('voice')
    if voice is None:
        return

    chords = voice.findall('Chord')
    if not chords:
        return

    # Remove last chord
    last_chord = chords[-1]
    # Find its index in voice's children and remove
    children = list(voice)
    idx = children.index(last_chord)
    voice.remove(last_chord)

    # Insert 2 eighth notes at the same position
    enc_above = make_chord(v_target_pitch + 1, 'eighth')
    enc_below = make_chord(v_target_pitch - 1, 'eighth')

    # ET doesn't have insert by index easily — rebuild voice children
    # (voice children are in order, so append works since we removed the last chord)
    voice.append(enc_above)
    voice.append(enc_below)


# ─── Main ────────────────────────────────────────────────────────────────────

def process(input_mscz, output_mscz):
    work_dir = '/tmp/enc_build'
    shutil.rmtree(work_dir, ignore_errors=True)
    os.makedirs(work_dir)

    # Extract
    with zipfile.ZipFile(input_mscz, 'r') as z:
        names = z.namelist()
        z.extractall(work_dir)

    # Find .mscx
    mscx_name = next(n for n in names if n.endswith('.mscx'))
    mscx_path = os.path.join(work_dir, mscx_name)

    tree = ET.parse(mscx_path)
    root = tree.getroot()

    # Update title
    for text_el in root.findall('.//Text'):
        style = text_el.find('style')
        txt = text_el.find('text')
        if style is not None and style.text == 'title' and txt is not None:
            txt.text = 'Bert Ligon Outlines (Enclosures)'
            break

    # Get measures from Staff id=1
    staff = root.find('.//Staff[@id="1"]')
    measures = [c for c in staff if c.tag == 'Measure']

    print(f"Total measures: {len(measures)}")

    # Each phrase = 4 measures: [ii, V, I, rest]
    phrase_size = 4
    n_phrases = len(measures) // phrase_size
    print(f"Total phrases: {n_phrases}")

    for phrase_idx in range(n_phrases):
        base = phrase_idx * phrase_size
        m_ii   = measures[base]
        m_v    = measures[base + 1]
        m_rest = measures[base + 3]

        # Target for the V chord enclosure = first note of V measure
        v_target = get_first_note_pitch(m_v)
        if v_target is not None:
            add_enclosure_to_ii_measure(m_ii, v_target)
            print(f"  Phrase {phrase_idx+1}: V enclosure → pitch {v_target} (±1: {v_target+1}/{v_target-1})")

        # Target for the ii chord of NEXT phrase = first note of next phrase's ii measure
        next_base = base + phrase_size
        if next_base < len(measures):
            next_ii_target = get_first_note_pitch(measures[next_base])
            if next_ii_target is not None:
                add_enclosure_to_rest_measure(m_rest, next_ii_target)
                print(f"  Phrase {phrase_idx+1}: ii enclosure → next phrase pitch {next_ii_target} (±1: {next_ii_target+1}/{next_ii_target-1})")

    # Write modified XML
    ET.indent(tree, space='  ')
    tree.write(mscx_path, encoding='UTF-8', xml_declaration=True)

    # Repackage as .mscz
    with zipfile.ZipFile(output_mscz, 'w', zipfile.ZIP_DEFLATED) as z:
        for name in names:
            z.write(os.path.join(work_dir, name), name)

    print(f"\nSaved: {output_mscz}")


if __name__ == '__main__':
    INPUT  = os.path.expanduser(
        '~/Documents/MuseScore4/Scores/Bert Ligon Outlines.mscz'
    )
    OUTPUT = os.path.expanduser(
        '~/Documents/MuseScore4/Scores/Bert Ligon Outlines - Enclosures.mscz'
    )
    process(INPUT, OUTPUT)
