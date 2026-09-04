"""#636 回归：conveyor 陈旧事件去重键改按事件身份（_event_id）。

背景：#635 的去重是段内行文本匹配，王语嫣划销改写行文本（加 ~~ 和处置后缀）后
匹配落空，09-04 14:47/15:17 陈旧 liveness 事件重登记实证。修法：去重键=事件身份
（原始时间戳+源类型+主体），划销行内嵌的原始时间戳仍可提取，与行文本死活无关。

运行：python -m pytest kdo-tools/tests/test_probe_dedup_event_identity_636.py -q
"""
import importlib.util
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "conveyor_probe", Path(__file__).resolve().parent.parent / "conveyor_probe.py"
)
probe = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(probe)

# 09-04 真实划销行（production-queue.md L1074，15:08 王语嫣划销）
STRUCK_LINE = ("- ~~[gate-blocked] role-liveness｜09-04 14:47｜待王语嫣复核处置｜"
               "2026-08-27 14:57:00｜role-liveness｜huangyaoshi 全实例疑似死亡"
               "（stale: [('kimi-cli', 568.5), ('cli', 344.5)]）｜role_registry check-liveness｜role_registry~~"
               " → 划销（09-04 15:08 王语嫣）：#635 落地窗口期残留")


def _queue(tmp_path, monkeypatch, block_lines):
    queue = tmp_path / "production-queue.md"
    queue.write_text("# 队列\n\n" + probe.PROPOSAL_BEGIN + "\n" + "\n".join(block_lines)
                     + "\n" + probe.PROPOSAL_END + "\n", encoding="utf-8")
    monkeypatch.setattr(probe, "QUEUE_FILE", queue)
    return queue


def test_event_id_extraction():
    """身份三元组：记录行与划销行提取出同一身份（划销包装不影响提取）。"""
    rec = ("2026-08-27 14:57:00｜role-liveness｜huangyaoshi 全实例疑似死亡（stale: x）"
           "｜role_registry check-liveness｜role_registry")
    assert probe._event_id(rec) == "2026-08-27 14:57:00｜role-liveness｜huangyaoshi"
    assert probe._event_id(STRUCK_LINE) == "2026-08-27 14:57:00｜role-liveness｜huangyaoshi"
    assert probe._event_id("无时间戳的行") is None


def test_struck_same_identity_blocked(tmp_path, monkeypatch):
    """#636 场景回放：已划销行含同事件身份 → 同身份新记录（stale 值漂移）不再上段。"""
    queue = _queue(tmp_path, monkeypatch, [STRUCK_LINE])
    # 同一事件再触发：时间戳/类型/主体相同，仅 stale 数值不同（文本匹配必落空）
    rec = ("2026-08-27 14:57:00｜role-liveness｜huangyaoshi 全实例疑似死亡"
           "（stale: [('kimi-cli', 1299.9)]）｜role_registry check-liveness｜role_registry")
    assert rec not in STRUCK_LINE  # 前提：纯文本匹配确实落空（#635 失效实证形态）
    probe._update_proposal_board_gate([rec])
    text = queue.read_text(encoding="utf-8")
    assert text.count("2026-08-27 14:57:00") == 1  # 只有原划销行，无新增


def test_different_identity_still_registered(tmp_path, monkeypatch):
    """不同身份（主体不同）→ 不误拦，正常登记。"""
    queue = _queue(tmp_path, monkeypatch, [STRUCK_LINE])
    rec = ("2026-08-27 14:57:00｜role-liveness｜ouyangfeng 全实例疑似死亡"
           "（stale: [('cli', 1.0)]）｜role_registry check-liveness｜role_registry")
    probe._update_proposal_board_gate([rec])
    assert "ouyangfeng 全实例疑似死亡" in queue.read_text(encoding="utf-8").split("~~")[0] + \
        queue.read_text(encoding="utf-8")


def test_unparseable_record_falls_back(tmp_path, monkeypatch):
    """身份提取不出（无 ISO 时间戳）→ 回退 #635 文本匹配语义，不误伤正常登记。"""
    queue = _queue(tmp_path, monkeypatch, [STRUCK_LINE])
    rec = "task_x｜F-034-五字段｜执行报告缺字段｜huangyaoshi"
    probe._update_proposal_board_gate([rec])
    assert "F-034-五字段" in queue.read_text(encoding="utf-8")


def test_same_batch_identity_dedup(tmp_path, monkeypatch):
    """同批重复记录（log 里同文双写族）→ 只登记一次。"""
    queue = _queue(tmp_path, monkeypatch, [])
    rec = ("2026-08-27 18:12:00｜role-liveness｜wangyuyan 全实例疑似死亡（stale: x）"
           "｜role_registry check-liveness｜role_registry")
    probe._update_proposal_board_gate([rec, rec])
    assert queue.read_text(encoding="utf-8").count("18:12:00") == 1
