#!/usr/bin/env python3
"""
diatonic_enclosures.py — Diatonic above + chromatic below enclosures.

Enclosure pattern: [diatonic step above target] [chromatic half step below target] → TARGET
More common in bebop lines than purely chromatic enclosures.
"""
import os
from mscz_utils import (open_mscz, save_mscz, get_measures, iter_phrases,
                         get_first_note_pitch, make_chord, make_rest)

# Major scale intervals (semitones from root)
_MAJOR_INTERVALS = [0, 2, 4, 5, 7, 9, 11]


def build_scale(root_pitch):
    """Return list of concert MIDI pitches for one octave of major scale from root."""
    return [root_pitch + i for i in _MAJOR_INTERVALS]


def diatonic_step_above(pitch, scale):
    """Return the next scale degree above pitch (wraps at octave if needed)."""
    pc = pitch % 12
    scale_pcs = [p % 12 for p in scale]
    if pc in scale_pcs:
        idx = scale_pcs.index(pc)
        next_pc = scale_pcs[(idx + 1) % len(scale_pcs)]
    else:
        # Not in scale — find nearest scale tone above
        above = [sp for sp in scale_pcs if sp > pc]
        next_pc = min(above) if above else scale_pcs[0]
    # Return at same octave or one above
    candidate = (pitch // 12) * 12 + next_pc
    if candidate <= pitch:
        candidate += 12
    return candidate


def add_diatonic_enclosure_to_ii_measure(measure, v_target, scale):
    voice = measure.find('voice')
    if voice is None:
        return
    chords = voice.findall('Chord')
    if not chords:
        return
    voice.remove(chords[-1])
    enc_above = diatonic_step_above(v_target, scale)
    enc_below = v_target - 1  # chromatic half step below
    voice.append(make_chord(enc_above, 'eighth'))
    voice.append(make_chord(enc_below, 'eighth'))


def add_diatonic_enclosure_to_rest_measure(measure, next_ii_target, scale):
    voice = measure.find('voice')
    if voice is None:
        return
    for rest in list(voice.findall('Rest')):
        voice.remove(rest)
    enc_above = diatonic_step_above(next_ii_target, scale)
    enc_below = next_ii_target - 1
    voice.append(make_rest('half', dotted=True))
    voice.append(make_chord(enc_above, 'eighth'))
    voice.append(make_chord(enc_below, 'eighth'))


def process(input_mscz, output_mscz):
    tree, mscx_path, names = open_mscz(input_mscz, '/tmp/denc_build')
    root = tree.getroot()
    measures = get_measures(root)

    # Detect key from first ii chord root (ii root - minor 3rd = key root)
    first_pitch = get_first_note_pitch(measures[0])
    key_root = (first_pitch - 3) if first_pitch else 70
    # Normalize to a usable octave (around concert pitch range)
    while key_root < 60:
        key_root += 12
    while key_root > 71:
        key_root -= 12
    scale = build_scale(key_root)

    for phrase_idx, m_ii, m_v, m_i, m_rest in iter_phrases(measures):
        v_target = get_first_note_pitch(m_v)
        if v_target:
            add_diatonic_enclosure_to_ii_measure(m_ii, v_target, scale)
        next_base = (phrase_idx + 1) * 4
        if next_base < len(measures):
            next_target = get_first_note_pitch(measures[next_base])
            if next_target:
                add_diatonic_enclosure_to_rest_measure(m_rest, next_target, scale)

    # Update title
    for text_el in root.findall('.//Text'):
        s = text_el.find('style')
        t = text_el.find('text')
        if s is not None and s.text == 'title' and t is not None:
            t.text = t.text + ' (Diatonic Enclosures)'
            break

    save_mscz(tree, mscx_path, names, '/tmp/denc_build', output_mscz)
    print(f"Saved: {output_mscz}")


if __name__ == '__main__':
    INPUT  = os.path.expanduser('~/Documents/MuseScore4/Scores/Bert Ligon Outlines.mscz')
    OUTPUT = os.path.expanduser('~/Documents/MuseScore4/Scores/Bert Ligon Outlines - Diatonic Enclosures.mscz')
    process(INPUT, OUTPUT)
