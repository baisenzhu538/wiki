"""#656 回归：拉起器通道健康预检 + fallback（F-073 落地）。

验收（任务单 60_feedback/tasks/task_20260906_huangyaoshi-channel-health-fallback.md）：
  1. 模拟死通道（坏 key / --force-dead）launch → 自动 fallback 成功 + 通知出现
  2. 全通道死 → 明确报错不假跑（exit 2，不 spawn 进程）
  3. 现有回归不红（test_headless_launch_650.py 继续过）

运行：python -m pytest 90_control/scripts/tests/test_channel_health_656.py -q
网络类用例只有 test_bad_key_real_endpoint 打真端点（401 免费且断网时仍判不健康，不脆）。
"""
import importlib.util
import json
import urllib.error
import urllib.request
from pathlib import Path

import pytest

_SCRIPTS = Path(__file__).resolve().parent.parent
_SPEC = importlib.util.spec_from_file_location("kimi_headless_launch", _SCRIPTS / "kimi-headless-launch.py")
launcher = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(launcher)

# 必须=launcher 持有的同一模块实例——patch 才打得到 launcher 的调用面
ch = launcher.channel_health


def pr(tool, healthy, scope="upstream", reason=""):
    return ch.ProbeResult(tool, healthy, scope, reason)


class FakePopen:
    """拦下真实 spawn，记录 cmd。"""
    called = []

    def __init__(self, cmd, **kw):
        self.cmd = cmd
        self.pid = 0
        FakePopen.called.append(cmd)


@pytest.fixture(autouse=True)
def isolated(monkeypatch, tmp_path):
    """测试隔离：todos/log 全部落 tmp，Popen 拦截，不产生真实进程和真实留痕。"""
    FakePopen.called = []
    monkeypatch.setattr(launcher.subprocess, "Popen", FakePopen)
    monkeypatch.setattr(launcher, "WIKI", tmp_path)
    monkeypatch.setattr(launcher, "TODOS_DIR", tmp_path / "90_control" / "todos")
    monkeypatch.setattr(ch, "HEALTH_LOG", tmp_path / "logs" / "channel-health.log")
    (tmp_path / "90_control" / "todos").mkdir(parents=True)
    (tmp_path / "90_control" / "todos" / "huangyaoshi.md").write_text("# huangyaoshi\n", encoding="utf-8")
    (tmp_path / "logs").mkdir()
    yield tmp_path


def todos_text(tmp):
    return (tmp / "90_control" / "todos" / "huangyaoshi.md").read_text(encoding="utf-8")


# ---------- 验收1：死通道 → fallback + 通知 ----------

def test_primary_dead_auto_fallback_with_notification(monkeypatch, capsys, isolated):
    fake = {
        "kimi": pr("kimi", False, "upstream", "CLI exit 1: 403 You've reached your weekly (7-day) usage limit"),
        "claude": pr("claude", True, "upstream", "200 OK"),
        "codex": pr("codex", True, "upstream", "200 OK"),
        "hermes": pr("hermes", False, "upstream", "同上游 kimi 已判定，未重复探测"),
    }
    monkeypatch.setattr(ch, "probe_chain", lambda tools, **kw: [fake[t] for t in tools])
    rc = launcher.main(["huangyaoshi", "做点事", "--force-dead", "kimi"])
    assert rc == 0
    out = capsys.readouterr().out
    assert "【通道fallback】kimi 不健康" in out and "已切 claude" in out
    assert "tool=claude" in out                       # 实际拉起走的是 fallback 通道
    assert FakePopen.called and FakePopen.called[0][0] == launcher.TOOLS["claude"][0]
    text = todos_text(isolated)
    assert "403" in text and "【通道预检 #656】" in text


def test_force_dead_simulates_dead_channel_end_to_end(monkeypatch, capsys):
    """坏 key 模拟的等价钩子：--force-dead 主通道 → 不动真实配置即触发 fallback。"""
    monkeypatch.setattr(
        ch, "probe_channel",
        lambda tool, **kw: pr(tool, not kw.get("force_dead"), "upstream", "200 OK" if not kw.get("force_dead") else "force_dead（模拟死通道）"))
    monkeypatch.setattr(
        ch, "probe_chain",
        lambda tools, **kw: [ch.probe_channel(t, force_dead=(t in kw.get("force_dead", ()))) for t in tools])
    rc = launcher.main(["huangyaoshi", "做点事", "--force-dead", "kimi"])
    assert rc == 0
    out = capsys.readouterr().out
    assert "已切 claude" in out and "force_dead（模拟死通道）" in out


def test_bad_key_real_endpoint_classified_unhealthy():
    """坏 key 实弹：GLM 端点 + 假 key → 401 判死（免费）；断网时判「不可达」同样不健康。"""
    r = ch.probe_claude(key_override="sk-dead0000dead0000dead0000dead0000dead0000")
    assert r.healthy is False
    assert ("401" in r.reason) or ("不可达" in r.reason)


# ---------- 验收2：全死 → 明确报错不假跑 ----------

def test_all_channels_dead_refuses_to_launch(monkeypatch, capsys, isolated):
    rc = launcher.main(["huangyaoshi", "做点事", "--force-dead", "claude,codex,kimi,hermes"])
    assert rc == 2
    assert FakePopen.called == []                      # 不假跑：一个进程都没起
    out = capsys.readouterr().out
    assert "【通道全死】" in out and "不硬派" in out and "王语嫣" in out
    text = todos_text(isolated)
    assert "【通道全死】" in text and "--no-probe" in text   # 应急出口写进通知


# ---------- 预检跳过 / 链序 / 上游去重 ----------

def test_no_probe_skips_precheck(monkeypatch, capsys):
    def boom(*a, **kw):
        raise AssertionError("--no-probe 不该触发任何探测")
    monkeypatch.setattr(ch, "probe_chain", boom)
    rc = launcher.main(["huangyaoshi", "做点事", "--no-probe"])
    assert rc == 0
    assert FakePopen.called[0][0] == launcher.TOOLS["kimi"][0]
    assert "【通道" not in capsys.readouterr().out      # 静默直通，无预检通知


def test_chain_primary_first_then_fallback_order():
    assert launcher.chain_for("huangyaoshi") == ["kimi", "claude", "codex", "hermes"]
    assert launcher.chain_for("ouyangfeng") == ["codex", "claude", "kimi", "hermes"]
    assert launcher.chain_for("huangyaoshi", "codex") == ["codex", "claude", "kimi", "hermes"]
    assert launcher.chain_for("未登记角色")[0] == "kimi"


def test_probe_chain_dedups_same_upstream():
    calls = []

    def prober(tool, **kw):
        calls.append(tool)
        if tool == "kimi":
            return pr("kimi", False, "upstream", "403 weekly limit")
        return pr(tool, True, "upstream", "200 OK")

    results = ch.probe_chain(["kimi", "claude", "codex", "hermes"], prober=prober)
    assert calls == ["kimi", "claude", "codex"]        # hermes(kimi 同上游) 未重复探测
    assert [r.healthy for r in results] == [False, True, True, False]
    assert "未重复探测" in results[3].reason


def test_tool_level_failure_does_not_condemn_same_upstream():
    """relay 挂（工具级）≠ deepseek 死——不得连坐同上游通道。"""
    calls = []

    def prober(tool, **kw):
        calls.append(tool)
        if tool == "codex":
            return pr("codex", False, "tool", "不可达：URLError 连接拒绝")
        return pr(tool, True, "upstream", "200 OK")

    results = ch.probe_chain(["codex", "kimi"], prober=prober)
    assert calls == ["codex", "kimi"]                  # 工具级死亡不写上游黑名单
    assert results[1].healthy is True


# ---------- 分类矩阵 ----------

def test_classify_matrix():
    assert ch.classify_status(200, "{}") == (True, "upstream", "200 OK")
    healthy, scope, _ = ch.classify_status(200, '{"error":{"message":"Insufficient Balance"}}')
    assert (healthy, scope) == (False, "upstream")
    for code in (401, 402, 403, 429):
        healthy, scope, reason = ch.classify_status(code)
        assert healthy is False and scope == "upstream"
    healthy, scope, _ = ch.classify_status(503)
    assert (healthy, scope) == (False, "tool")
    healthy, scope, _ = ch.classify_status(302)
    assert (healthy, scope) == (False, "tool")


def test_probe_result_json_shape():
    r = ch.probe_channel("kimi", force_dead=True)
    j = r.to_json()
    assert j["upstream"] == "kimi" and j["healthy"] is False


def test_regression_tools_and_role_tables_untouched():
    # 650 回归锚 + 09-03 异构防线：本任务只加预检，不动工具路由表
    assert launcher.ROLE_TOOL == {"huangyaoshi": "kimi", "laowantong": "kimi", "ouyangfeng": "codex"}
    assert launcher.TOOLS["hermes"][launcher.TOOLS["hermes"].index("-p") + 1] == "{role}"
    assert launcher.TOOL_ENV == {}
