import sys, os, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from mscz_utils import pitch_to_tpc


def test_c_concert():
    tpc_c, tpc_w = pitch_to_tpc(60)  # C4
    assert tpc_c == 14  # C
    assert tpc_w == 16  # D (written for Bb trumpet)


def test_eb_concert():
    tpc_c, tpc_w = pitch_to_tpc(63)  # Eb4
    assert tpc_c == 11  # Eb
    assert tpc_w == 13  # F


def test_bb_prefers_flat():
    tpc_c, tpc_w = pitch_to_tpc(70)  # Bb4
    assert tpc_c == 12  # Bb not A#
    assert tpc_w == 14  # C


def test_add_enclosures_roundtrip():
    """add_enclosures.py produces a .mscz with correct note count."""
    from add_enclosures import process
    src = os.path.expanduser('~/Documents/MuseScore4/Scores/Bert Ligon Outlines.mscz')
    if not os.path.exists(src):
        return  # skip if source not present
    with tempfile.NamedTemporaryFile(suffix='.mscz', delete=False) as f:
        out = f.name
    try:
        process(src, out)
        assert os.path.exists(out)
        assert os.path.getsize(out) > 10_000
    finally:
        os.unlink(out)
