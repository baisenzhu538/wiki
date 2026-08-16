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


# ---- #272 新鲜度 SLA：stale 判定三场景 ----

from datetime import datetime, timedelta
from unittest.mock import patch

def _mk_feat(verified, verify_date, reverify_by=None):
    return {"id": "T001", "name": "测试", "layer": "L0", "dimension": "A",
            "purpose": "p", "scenario": "s", "case_ref": "", "verified": verified,
            "verify_date": verify_date, "reverify_by": reverify_by}

def test_stale_overdue():
    """超期：verify_date 距今 > 6 个月 → stale"""
    import feature_menu
    old = (datetime.now() - timedelta(days=200)).strftime("%Y-%m-%d")
    assert feature_menu._is_stale(_mk_feat(True, old)) is True

def test_stale_fresh():
    """未超期：verify_date 距今 < 6 个月 → 非 stale"""
    import feature_menu
    recent = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    assert feature_menu._is_stale(_mk_feat(True, recent)) is False

def test_stale_missing_date_tolerated():
    """字段缺失容忍：verified 但无 verify_date → 非 stale（迁移中不误报）"""
    import feature_menu
    assert feature_menu._is_stale(_mk_feat(True, None)) is False

def test_stale_unverified_never():
    """未 verified 永不 stale"""
    import feature_menu
    old = (datetime.now() - timedelta(days=400)).strftime("%Y-%m-%d")
    assert feature_menu._is_stale(_mk_feat(False, old)) is False

def test_stale_uses_reverify_by_fallback():
    """reverify_by 作为 verify_date 的回退"""
    import feature_menu
    old = (datetime.now() - timedelta(days=200)).strftime("%Y-%m-%d")
    assert feature_menu._is_stale(_mk_feat(True, None, reverify_by=old)) is True

# ---- #315 aliases 别名增强 ----

def test_aliases_present():
    feats = load()
    with_alias = [f for f in feats if f.get("aliases")]
    assert len(with_alias) >= 30, f"Only {len(with_alias)} with aliases — expected >= 30"

def test_alias_fanxiang_jiaoxue_maps_to_F022():
    """学员命名'反向教学'→ F022 反向教我（#315 验收 1）"""
    feats = {f["id"]: f for f in load()}
    assert "反向教学" in feats["F022"].get("aliases", []), "F022 aliases 缺'反向教学'"

def test_alias_cankao_anli_maps_to_F026():
    """学员命名'参考案例'→ F026 Few-shot（#315 验收 1）"""
    feats = {f["id"]: f for f in load()}
    assert "参考案例" in feats["F026"].get("aliases", []), "F026 aliases 缺'参考案例'"

def test_alias_match_function():
    import feature_menu
    feats = load()
    f100 = next(f for f in feats if f["id"] == "F100")
    assert feature_menu._match(f100, "复述需求") is True, "_match 未命中 F100 别名"
    assert feature_menu._match(f100, "完全无关词xyz") is False, "_match 误命中"

def test_version_v10():
    import json as _json
    from pathlib import Path as _Path
    data = _json.loads(_Path(__file__).resolve().parent.parent.joinpath(
        "10_raw/sources/feature-periodic-table-v1.0.json").read_text(encoding="utf-8"))
    assert data["version"] == "V1.0"
    assert len(data["features"]) == 100

# ---- #316 combo 组合查询 ----

def test_combo_data_loadable():
    import feature_menu
    data = json.loads(feature_menu.COMBO_PATH.read_text(encoding="utf-8"))
    assert len(data["combos"]) == 4, f"Expected 4 combos, got {len(data['combos'])}"

def test_combo_feature_refs_exist():
    """组合引用的 Feature id 全部存在于周期表（验收 3 溯源链）"""
    import feature_menu
    feats = {f["id"] for f in load()}
    combos = json.loads(feature_menu.COMBO_PATH.read_text(encoding="utf-8"))["combos"]
    for c in combos:
        for f in c["features"]:
            assert f["id"] in feats, f"combo {c['id']} 引用 {f['id']} 不在周期表"

def test_combo_evidence_grade_valid():
    import feature_menu
    combos = json.loads(feature_menu.COMBO_PATH.read_text(encoding="utf-8"))["combos"]
    for c in combos:
        g = c["evidence"]["grade"]
        assert g in ("实测", "引用", "推演"), f"combo {c['id']} grade 非法: {g}"

def test_combo_scene_match():
    import feature_menu
    combos = json.loads(feature_menu.COMBO_PATH.read_text(encoding="utf-8"))["combos"]
    content = [c for c in combos if any("内容创作" in t for t in c.get("scene_tags", []))]
    assert len(content) == 1 and content[0]["id"] == "combo-content-3dim"

# ---- #317 evidence 证据分级 ----

def test_evidence_backfill_count():
    feats = load()
    ev = [f for f in feats if f.get("evidence")]
    assert len(ev) >= 10, f"evidence 回填仅 {len(ev)} 条 — 期望 >= 10"

def test_evidence_grade_valid():
    feats = load()
    for f in feats:
        if f.get("evidence"):
            assert f["evidence"]["grade"] in ("实测", "引用", "推演"), f"{f['id']} grade 非法"

def test_verified_count_preserved():
    """25 条 verified 全保留（验收 1 迁移无丢失）"""
    feats = load()
    assert sum(1 for f in feats if f.get("verified")) == 25, "verified 计数非 25"

def test_verified_never_inference():
    """约定：verified=true 的条目 evidence.grade 不得为'推演'"""
    feats = load()
    for f in feats:
        if f.get("verified") and f.get("evidence", {}).get("grade") == "推演":
            raise AssertionError(f"{f['id']} verified=true 但 evidence=推演（违反约定）")

# ---- #318 分层水位 ----

def test_by_layer_counts_match_json():
    """各层总数/verified 数与 JSON 一致（验收 1）"""
    feats = load()
    expect = {"L0": (3, 3), "L1": (14, 2), "L2": (38, 14), "L3": (14, 1), "L4": (18, 4), "L5": (13, 1)}
    for layer, (n, v) in expect.items():
        fs = [f for f in feats if f.get("layer") == layer]
        assert len(fs) == n, f"{layer} 总数 {len(fs)} != {n}"
        assert sum(1 for f in fs if f.get("verified")) == v, f"{layer} verified != {v}"

def test_by_layer_all_six_layers():
    feats = load()
    layers = set(f["layer"] for f in feats)
    assert {"L0", "L1", "L2", "L3", "L4", "L5"} <= layers


if __name__ == "__main__":
    test_load()
    test_unique_ids()
    test_fmt_output()
    test_info_verified()
    test_info_unverified()
    test_query_layer()
    test_query_dimension()
    test_pick_reproducible()
    test_stale_overdue()
    test_stale_fresh()
    test_stale_missing_date_tolerated()
    test_stale_unverified_never()
    test_stale_uses_reverify_by_fallback()
    test_aliases_present()
    test_alias_fanxiang_jiaoxue_maps_to_F022()
    test_alias_cankao_anli_maps_to_F026()
    test_alias_match_function()
    test_version_v10()
    test_combo_data_loadable()
    test_combo_feature_refs_exist()
    test_combo_evidence_grade_valid()
    test_combo_scene_match()
    test_evidence_backfill_count()
    test_evidence_grade_valid()
    test_verified_count_preserved()
    test_verified_never_inference()
    test_by_layer_counts_match_json()
    test_by_layer_all_six_layers()
    print(f"ALL {27} TESTS PASSED ({len(load())} features)")
