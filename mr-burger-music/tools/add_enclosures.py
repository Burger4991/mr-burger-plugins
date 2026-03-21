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

import os
from mscz_utils import (open_mscz, save_mscz, get_measures, iter_phrases,
                         get_first_note_pitch, make_chord, make_rest)


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

    for rest in list(voice.findall('Rest')):
        voice.remove(rest)

    voice.append(make_rest('half', dotted=True))
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

    voice.remove(chords[-1])
    voice.append(make_chord(v_target_pitch + 1, 'eighth'))
    voice.append(make_chord(v_target_pitch - 1, 'eighth'))


# ─── Main ────────────────────────────────────────────────────────────────────

def process(input_mscz, output_mscz):
    tree, mscx_path, names = open_mscz(input_mscz, '/tmp/enc_build')
    root = tree.getroot()

    # Update title
    for text_el in root.findall('.//Text'):
        style = text_el.find('style')
        txt = text_el.find('text')
        if style is not None and style.text == 'title' and txt is not None:
            txt.text = 'Bert Ligon Outlines (Enclosures)'
            break

    measures = get_measures(root)
    print(f"Total measures: {len(measures)}, phrases: {len(measures) // 4}")

    for phrase_idx, m_ii, m_v, m_i, m_rest in iter_phrases(measures):
        v_target = get_first_note_pitch(m_v)
        if v_target is not None:
            add_enclosure_to_ii_measure(m_ii, v_target)

        next_base = (phrase_idx + 1) * 4
        if next_base < len(measures):
            next_target = get_first_note_pitch(measures[next_base])
            if next_target is not None:
                add_enclosure_to_rest_measure(m_rest, next_target)

    save_mscz(tree, mscx_path, names, '/tmp/enc_build', output_mscz)
    print(f"Saved: {output_mscz}")


if __name__ == '__main__':
    INPUT  = os.path.expanduser('~/Documents/MuseScore4/Scores/Bert Ligon Outlines.mscz')
    OUTPUT = os.path.expanduser('~/Documents/MuseScore4/Scores/Bert Ligon Outlines - Enclosures.mscz')
    process(INPUT, OUTPUT)
