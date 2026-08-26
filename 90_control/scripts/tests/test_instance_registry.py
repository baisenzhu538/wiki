"""#546 回归：实例身份登记 + 终审权机器校验（一具两职事件根治轻量版）。

三类用例（任务书）：正常登记+终审放行 / 越权终审拒止 / force 逃生门留痕。
外加：一具两职场景重演（同 cwd 双角色登记→审计轨+口径行为）、probe 活性读取。

运行：python -m pytest 90_control/scripts/tests/test_instance_registry.py -q
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import queue_transition as qt


def _reg(tmp_path, monkeypatch, entries=None):
    reg = tmp_path / "active-instances.json"
    monkeypatch.setattr(qt, "INSTANCE_REGISTRY", reg)
    if entries is not None:
        reg.write_text(json.dumps({"instances": entries}, ensure_ascii=False), encoding="utf-8")
    return reg


def test_claim_registers_instance(tmp_path, monkeypatch):
    """claim 成功 → 登记表无感写入（角色/cwd/时间戳）。"""
    reg = _reg(tmp_path, monkeypatch)
    qt._register_instance("task_20260827_real-x", "huangyaoshi")
    e = json.loads(reg.read_text(encoding="utf-8"))["instances"]["huangyaoshi"]
    assert e["role"] == "huangyaoshi"
    assert e["cwd"] and e["ts"]


def test_claim_legacy_alias_maps_role(tmp_path, monkeypatch):
    """legacy 实例名映射：hermes → laowantong（INSTANCE_ROLE_MAP shim）。"""
    reg = _reg(tmp_path, monkeypatch)
    qt._register_instance("task_20260827_real-y", "hermes")
    e = json.loads(reg.read_text(encoding="utf-8"))["instances"]["hermes"]
    assert e["role"] == "laowantong"


def test_test_task_not_registered(tmp_path, monkeypatch):
    """task_9999_ 测试件不登记（#483 噪声分流纪律）。"""
    reg = _reg(tmp_path, monkeypatch)
    qt._register_instance("task_9999_smoke", "kimi")
    assert not reg.exists()


def test_register_action_roundtrip(tmp_path, monkeypatch):
    """register 命令：纯审查角色（不 claim）的上岗入口。"""
    reg = _reg(tmp_path, monkeypatch)
    ok, msg = qt.action_register("ouyangfeng")
    assert ok and "ouyangfeng" in msg
    e = json.loads(reg.read_text(encoding="utf-8"))["instances"]["ouyangfeng"]
    assert e["role"] == "ouyangfeng"


def test_review_authority_pass_with_registered_ouyangfeng(tmp_path, monkeypatch):
    """当前 cwd 有 ouyangfeng 登记 → 放行。"""
    import os
    _reg(tmp_path, monkeypatch, entries={
        "ouyangfeng": {"role": "ouyangfeng", "cwd": os.getcwd(), "ts": "2026-08-27T02:00"},
    })
    ok, msg = qt._check_review_authority("task_20260827_a", "欧阳锋")
    assert ok and msg == ""


def test_review_authority_reject_unregistered(tmp_path, monkeypatch):
    """未登记/角色不符 → 拒止 + 提示 register（一具两职裸奔封死）。"""
    _reg(tmp_path, monkeypatch, entries={
        "huangyaoshi": {"role": "huangyaoshi", "cwd": __import__("os").getcwd(), "ts": "2026-08-27T02:00"},
    })
    ok, msg = qt._check_review_authority("task_20260827_b", "欧阳锋")
    assert not ok and "register ouyangfeng" in msg


def test_review_authority_reject_wrong_cwd(tmp_path, monkeypatch):
    """ouyangfeng 登记在别的 cwd → 当前目录仍拒止。"""
    _reg(tmp_path, monkeypatch, entries={
        "ouyangfeng": {"role": "ouyangfeng", "cwd": "D:/tech-wiki", "ts": "2026-08-27T02:00"},
    })
    ok, _ = qt._check_review_authority("task_20260827_c", "欧阳锋")
    assert not ok


def test_review_authority_force_escape_with_ledger(tmp_path, monkeypatch):
    """force 逃生门：--reason 必填 + 落 force 台账。"""
    import os
    _reg(tmp_path, monkeypatch, entries={})
    ledger = tmp_path / "force.log"
    monkeypatch.setattr(qt, "FORCE_LEDGER", ledger)
    # 无 reason → 拒
    ok, msg = qt._check_review_authority("task_20260827_d", "欧阳锋", force=True, reason="")
    assert not ok and "--reason" in msg
    # 有 reason → 放行 + 台账留痕
    ok, msg = qt._check_review_authority("task_20260827_d", "欧阳锋", force=True, reason="登记机制上线首日应急")
    assert ok and "留痕" in msg
    assert "task_20260827_d" in ledger.read_text(encoding="utf-8")


def test_dual_role_scenario_audit_trail(tmp_path, monkeypatch):
    """一具两职重演：同 cwd 先登记 ouyangfeng 再以 huangyaoshi claim。
    口径行为：review 放行（该 cwd 有 ouyangfeng 登记）+ 双角色登记记录都在（审计轨）。
    会话级绑定防控属 #525 正单，本单轻量版的边界如实如此。"""
    import os
    reg = _reg(tmp_path, monkeypatch)
    qt.action_register("ouyangfeng")
    qt._register_instance("task_20260827_real-z", "huangyaoshi")
    instances = json.loads(reg.read_text(encoding="utf-8"))["instances"]
    assert set(instances) == {"ouyangfeng", "huangyaoshi"}  # 审计轨：两个角色都留痕
    assert instances["ouyangfeng"]["cwd"] == instances["huangyaoshi"]["cwd"] == os.getcwd()
    ok, _ = qt._check_review_authority("task_20260827_e", "欧阳锋")
    assert ok  # 口径：cwd 有 ouyangfeng 登记即放行


def test_probe_instance_activity(tmp_path, monkeypatch):
    """conveyor_probe 活性展示：读登记表计数+角色（只读 fail-open）。"""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "conveyor_probe", Path(__file__).resolve().parents[3] / "kdo-tools" / "conveyor_probe.py")
    probe = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(probe)
    monkeypatch.setattr(probe, "ROOT", tmp_path)
    (tmp_path / ".kdo").mkdir()
    (tmp_path / ".kdo" / "active-instances.json").write_text(json.dumps({
        "instances": {"a": {"role": "huangyaoshi", "ts": "2026-08-27T01:00"},
                      "b": {"role": "ouyangfeng", "ts": "2026-08-27T02:00"}}
    }), encoding="utf-8")
    act = probe._instance_activity()
    assert act["count"] == 2 and act["roles"] == ["huangyaoshi", "ouyangfeng"]
    # 读不到 → fail-open 空
    monkeypatch.setattr(probe, "ROOT", tmp_path / "nowhere")
    assert probe._instance_activity()["count"] == 0
