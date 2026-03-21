#!/usr/bin/env python3
"""
transpose_pattern.py — Generate a 12-key worksheet from a single-key pattern.

Takes any .mscz with phrase_size measures, transposes it through the
cycle of fifths, and outputs a new .mscz with all 12 keys concatenated.

Cycle of fifths (ascending P5): C G D A E B Gb Db Ab Eb Bb F
Each successive key is 7 semitones above the previous.
"""
import os, copy
import xml.etree.ElementTree as ET
from mscz_utils import (open_mscz, save_mscz, get_measures, pitch_to_tpc)

# Semitone offsets for each key in cycle-of-fifths order (starting from key 0)
# Key 0: 0, Key 1: +7, Key 2: +14→+2, Key 3: +21→+9 ... wrapping at octave
_CYCLE_OFFSETS = [(i * 7) % 12 for i in range(12)]
# = [0, 7, 2, 9, 4, 11, 6, 1, 8, 3, 10, 5]


def transpose_pitch(midi_pitch, semitones):
    """Return midi_pitch + semitones."""
    return midi_pitch + semitones


def _keep_in_range(pitch, low=60, high=84):
    """Shift by octaves to keep pitch in [low, high] (trumpet range C4–C6)."""
    while pitch < low:
        pitch += 12
    while pitch > high:
        pitch -= 12
    return pitch


def transpose_measure(measure, semitones):
    """Return a deep copy of measure with all pitches transposed and TPCs updated."""
    m = copy.deepcopy(measure)
    for note_el in m.findall('.//Note'):
        p_el = note_el.find('pitch')
        if p_el is None:
            continue
        old_pitch = int(p_el.text)
        new_pitch = old_pitch + semitones
        p_el.text = str(new_pitch)
        tpc_c, tpc_w = pitch_to_tpc(new_pitch)
        tpc_el = note_el.find('tpc')
        tpc2_el = note_el.find('tpc2')
        if tpc_el is not None:
            tpc_el.text = str(tpc_c)
        if tpc2_el is not None:
            tpc2_el.text = str(tpc_w)
    return m


def process(input_mscz, output_mscz, phrase_size=4):
    tree, mscx_path, names = open_mscz(input_mscz, '/tmp/tp_build')
    root = tree.getroot()
    measures = get_measures(root)
    staff = root.find('.//Staff[@id="1"]')

    # Capture source phrase (first phrase_size measures)
    source_measures = measures[:phrase_size]

    # Detect base pitch for range normalization
    base_pitch = None
    for m in source_measures:
        for p in m.findall('.//pitch'):
            base_pitch = int(p.text)
            break
        if base_pitch:
            break

    # Remove all existing measures from staff
    for m in list(staff.findall('Measure')):
        staff.remove(m)

    # Generate all 12 keys in cycle-of-fifths order
    for key_idx in range(12):
        raw_offset = _CYCLE_OFFSETS[key_idx]
        # Calculate octave-aware offset: keep notes near base_pitch
        if base_pitch:
            test_pitch = base_pitch + raw_offset
            adjusted = _keep_in_range(test_pitch)
            semitones = adjusted - base_pitch
        else:
            semitones = raw_offset

        for src_m in source_measures:
            staff.append(transpose_measure(src_m, semitones))

    save_mscz(tree, mscx_path, names, '/tmp/tp_build', output_mscz)
    print(f"Saved: {output_mscz} (12 keys)")


if __name__ == '__main__':
    INPUT  = os.path.expanduser('~/Documents/MuseScore4/Scores/Pattern-OneKey.mscz')
    OUTPUT = os.path.expanduser('~/Documents/MuseScore4/Scores/Pattern-12Keys.mscz')
    if not os.path.exists(INPUT):
        print(f"Source not found: {INPUT}")
    else:
        process(INPUT, OUTPUT)
