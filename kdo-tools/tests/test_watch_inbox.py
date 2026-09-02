"""#530 回归：watch_inbox 新素材通知通道（检测到→推王语嫣收件箱）。

三类用例（任务书第 4 条）：新文件推收件箱/重跑不重复推/夜间静默落盘带🔕。

运行：python -m pytest kdo-tools/tests/test_watch_inbox.py -q
沙盒：monkeypatch 注入临时 ROOT/INBOX/STATE_FILE/QUEUE_DIR/PROD_QUEUE/TODOS，不碰真实 vault。
"""
import importlib.util
import json
from datetime import datetime
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "watch_inbox", Path(__file__).resolve().parent.parent / "watch_inbox.py"
)
wi = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(wi)


def _sandbox(tmp_path, monkeypatch):
    inbox = tmp_path / "00_inbox"
    inbox.mkdir()
    todos = tmp_path / "90_control" / "todos" / "wangyuyan.md"
    monkeypatch.setattr(wi, "ROOT", tmp_path)
    monkeypatch.setattr(wi, "INBOX", inbox)
    monkeypatch.setattr(wi, "STATE_FILE", tmp_path / ".kdo" / "inbox_state.json")
    monkeypatch.setattr(wi, "QUEUE_DIR", tmp_path / "inbox-queue")
    monkeypatch.setattr(wi, "PROD_QUEUE", tmp_path / "production-queue.md")
    monkeypatch.setattr(wi, "TODOS_WANGYUYAN", todos)
    return inbox, todos


def test_new_file_notifies_wangyuyan(tmp_path, monkeypatch):
    inbox, todos = _sandbox(tmp_path, monkeypatch)
    (inbox / "素材-口述.txt").write_text("内容" * 100, encoding="utf-8")
    wi.dispatch(wi.scan())
    text = todos.read_text(encoding="utf-8")
    assert "新素材 1 项" in text and "素材-口述.txt" in text and "请诊断编排" in text


def test_rerun_no_duplicate(tmp_path, monkeypatch):
    """幂等：state 判重同键——重跑零 discoveries 零新通知。"""
    inbox, todos = _sandbox(tmp_path, monkeypatch)
    (inbox / "a.md").write_text("x" * 300, encoding="utf-8")
    wi.dispatch(wi.scan())
    first = todos.read_text(encoding="utf-8")
    assert wi.scan() == []  # 重跑无新发现
    assert todos.read_text(encoding="utf-8") == first  # 不重复推


def test_night_silent_marker(tmp_path, monkeypatch):
    """无 agent 在岗=静默落盘带 🔕；有 agent 在岗=正常 📥（#550 在岗判定口径，时段制已废）。"""
    inbox, todos = _sandbox(tmp_path, monkeypatch)
    (inbox / "口述-课程.txt").write_text("y" * 300, encoding="utf-8")  # P0 关键词命中
    monkeypatch.setattr(wi.on_duty, "any_agent_on_duty", lambda **k: (False, "测试静默"))
    wi._notify_inbox([{"file": "00_inbox/口述-课程.txt", "priority": "P0"}])
    text = todos.read_text(encoding="utf-8")
    assert "🔕" in text and "P0 1" in text
    # 在岗 → 不静默
    monkeypatch.setattr(wi.on_duty, "any_agent_on_duty", lambda **k: (True, "测试在岗"))
    todos.write_text("", encoding="utf-8")
    wi._notify_inbox([{"file": "00_inbox/口述-课程2.txt", "priority": "P0"}])
    assert "📥" in todos.read_text(encoding="utf-8")


def test_scan_whitelist_subdirs(tmp_path, monkeypatch):
    """#619 回归：白名单子目录（管线落点）回扫描面；内部子目录与大目录树不扫。"""
    inbox, _ = _sandbox(tmp_path, monkeypatch)
    (inbox / "wechat-collect").mkdir()
    (inbox / "wechat-collect" / "src_wechat_abc.md").write_text("x" * 100, encoding="utf-8")
    (inbox / "wechat-collect" / "knowledge").mkdir()
    (inbox / "wechat-collect" / "knowledge" / "case-wechat-abc.md").write_text("x" * 100, encoding="utf-8")
    (inbox / "wechat-collect" / "_needs_rerun").mkdir()
    (inbox / "wechat-collect" / "_needs_rerun" / "case-wechat-def.md").write_text("x" * 100, encoding="utf-8")
    (inbox / "video_transcripts").mkdir()
    (inbox / "video_transcripts" / "BV1xx-逐字稿.md").write_text("x" * 100, encoding="utf-8")
    (inbox / "Handle").mkdir()
    (inbox / "Handle" / "big.md").write_text("x" * 100, encoding="utf-8")
    found = {d["file"].replace("\\", "/") for d in wi.scan()}
    assert "00_inbox/wechat-collect/src_wechat_abc.md" in found
    assert "00_inbox/video_transcripts/BV1xx-逐字稿.md" in found
    assert not any("knowledge" in f or "_needs_rerun" in f or "Handle" in f for f in found)
