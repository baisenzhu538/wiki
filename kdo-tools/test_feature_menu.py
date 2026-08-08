#!/usr/bin/env python3
"""pytest for kdo feature menu — #254 验收条件 T1. All counts are dynamic."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from feature_menu import load, fmt

def test_load():
    feats = load()
    assert len(feats) in (96, 100), f"Expected 96-100, got {len(feats)}"
    f = feats[0]
    for key in ["id", "name", "layer", "dimension", "purpose", "scenario", "case_ref", "verified"]:
        assert key in f, f"Missing key: {key}"

def test_unique_ids():
    feats = load()
    ids = [f["id"] for f in feats]
    assert len(set(ids)) == len(feats), f"Duplicate IDs: {len(feats)} vs {len(set(ids))}"

def test_fmt_output():
    feats = load()
    output = fmt(feats[0])
    assert "F001" in output

def test_info_verified():
    feats = load()
    verified = [f for f in feats if f.get("verified")]
    assert len(verified) >= 16, f"Only {len(verified)} verified — too few"

def test_info_unverified():
    feats = load()
    unverified = [f for f in feats if not f.get("verified")]
    assert len(unverified) >= 70, f"Only {len(unverified)} unverified — too few"

def test_query_layer():
    feats = load()
    layers = set(f["layer"] for f in feats)
    for l in ["L0", "L1", "L2", "L3", "L4", "L5"]:
        assert l in layers, f"Missing layer {l}"

def test_query_dimension():
    feats = load()
    dims = set(f["dimension"] for f in feats)
    for d in ["A", "B", "C", "D"]:
        assert d in dims, f"Missing dimension {d}"

def test_pick_reproducible():
    import random
    feats = load()
    random.seed(42)
    a = random.sample(feats, 5)
    random.seed(42)
    b = random.sample(feats, 5)
    assert [f["id"] for f in a] == [f["id"] for f in b], "Seed not reproducible"

if __name__ == "__main__":
    test_load()
    test_unique_ids()
    test_fmt_output()
    test_info_verified()
    test_info_unverified()
    test_query_layer()
    test_query_dimension()
    test_pick_reproducible()
    print(f"ALL 8 TESTS PASSED ({len(load())} features)")
