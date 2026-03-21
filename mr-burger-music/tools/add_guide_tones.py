#!/usr/bin/env python3
"""
add_guide_tones.py — Adds guide tone voice above Ligon outlines.

Inserts Voice 2 into each phrase showing:
  ii measure:  ii_3rd (half) + ii_7th (half)
  V measure:   v_3rd  (half) + v_7th  (half)
  I measure:   i_3rd  (whole)

This makes the 7→3 voice leading visible alongside the outline.
"""
import os
import xml.etree.ElementTree as ET
from mscz_utils import (open_mscz, save_mscz, get_measures, iter_phrases,
                         get_first_note_pitch, make_chord, gen_eid)


def guide_tones_for_key(key_root):
    """Return guide tone MIDI pitches for ii-V-I in given major key.
    key_root: concert MIDI pitch of the tonic (e.g. 70 for Bb).

    Bb major example (key_root=70):
      ii = Cm7:    3rd = Eb (r+5),  7th = Bb (r+12)
      V  = F7:     3rd = A  (r+11), 7th = Eb (r+5)
      I  = Bbmaj7: 3rd = D  (r+4)
    """
    r = key_root
    return {
        'ii_3rd': r + 5,   # Eb in Bb: 3rd of Cm7 (r+5=75, 75%12=3 ✓)
        'ii_7th': r + 12,  # Bb in Bb: 7th of Cm7 = tonic (r+12=82, 82%12=10 ✓)
        'v_3rd':  r + 11,  # A in Bb:  3rd of F7 = leading tone (r+11=81, 81%12=9 ✓)
        'v_7th':  r + 5,   # Eb in Bb: 7th of F7 = 4th scale degree (r+5=75, 75%12=3 ✓)
        'i_3rd':  r + 4,   # D in Bb:  3rd of Bbmaj7 (r+4=74, 74%12=2 ✓)
    }


def _normalize(pitch, ref_pitch, tolerance=6):
    """Shift pitch by octaves to be within tolerance semitones of ref_pitch."""
    while pitch < ref_pitch - tolerance:
        pitch += 12
    while pitch > ref_pitch + tolerance:
        pitch -= 12
    return pitch


def make_voice2(notes_durations):
    """Build a <voice> element (voice 2) with given (pitch, duration) pairs."""
    voice = ET.Element('voice')
    ET.SubElement(voice, 'eid').text = gen_eid()
    from mscz_utils import make_chord as _make_chord
    for pitch, dur in notes_durations:
        voice.append(_make_chord(pitch, dur))
    return voice


def add_guide_tones_to_phrase(m_ii, m_v, m_i, key_root):
    gt = guide_tones_for_key(key_root)
    ref = get_first_note_pitch(m_ii) or key_root + 5

    ii_3 = _normalize(gt['ii_3rd'], ref)
    ii_7 = _normalize(gt['ii_7th'], ref)
    v_3  = _normalize(gt['v_3rd'],  ref)
    v_7  = _normalize(gt['v_7th'],  ref)
    i_3  = _normalize(gt['i_3rd'],  ref)

    m_ii.append(make_voice2([(ii_3, 'half'), (ii_7, 'half')]))
    m_v.append(make_voice2([(v_3, 'half'), (v_7, 'half')]))
    m_i.append(make_voice2([(i_3, 'whole')]))


def detect_key_root(measures):
    """Detect key from first ii chord: ii root - minor 3rd = key root."""
    first = get_first_note_pitch(measures[0])
    if first is None:
        return 70  # default Bb
    # ii chord root is first note; key root is minor 3rd below
    key_root = first - 3
    while key_root < 60:
        key_root += 12
    return key_root


def process(input_mscz, output_mscz):
    tree, mscx_path, names = open_mscz(input_mscz, '/tmp/gt_build')
    root = tree.getroot()
    measures = get_measures(root)
    key_root = detect_key_root(measures)

    for _, m_ii, m_v, m_i, m_rest in iter_phrases(measures):
        add_guide_tones_to_phrase(m_ii, m_v, m_i, key_root)

    for text_el in root.findall('.//Text'):
        s = text_el.find('style')
        t = text_el.find('text')
        if s is not None and s.text == 'title' and t is not None:
            t.text = t.text + ' (Guide Tones)'
            break

    save_mscz(tree, mscx_path, names, '/tmp/gt_build', output_mscz)
    print(f"Saved: {output_mscz}")


if __name__ == '__main__':
    INPUT  = os.path.expanduser('~/Documents/MuseScore4/Scores/Bert Ligon Outlines.mscz')
    OUTPUT = os.path.expanduser('~/Documents/MuseScore4/Scores/Bert Ligon Outlines - Guide Tones.mscz')
    process(INPUT, OUTPUT)
