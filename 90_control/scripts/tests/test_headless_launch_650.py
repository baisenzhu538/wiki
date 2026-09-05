"""#650 回归：拉起器 hermes 通道角色切换必须走 -p flag（env 机制已证死）。

背景（段王爷 09-06 实测 + 黄药师今日双实测）：
- hermes 无头解析链只认 argv `-p` → `active_profile` 文件 → `HERMES_HOME` env，
  `HERMES_PROFILE` 环境变量根本不被读——env-only 拉起全部错载 active_profile
  （当时=huangyaoshi）：阴性对照 `HERMES_PROFILE=skills-assistant hermes -z 你是谁`
  → 自称 huangyaoshi；`-p skills-assistant` → 自称 skills-assistant。

运行：python -m pytest 90_control/scripts/tests/test_headless_launch_650.py -q
"""
import importlib.util
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "kimi_headless_launch",
    Path(__file__).resolve().parent.parent / "kimi-headless-launch.py",
)
launcher = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(launcher)


def test_hermes_template_uses_p_flag_for_role():
    cmd_tmpl = launcher.TOOLS["hermes"]
    assert "-p" in cmd_tmpl, "hermes 模板缺 -p flag——角色切换机制回退"
    assert cmd_tmpl[cmd_tmpl.index("-p") + 1] == "{role}", "-p 后必须紧跟 {role} 占位符"
    assert "HERMES_PROFILE" not in cmd_tmpl


def test_tool_env_no_dead_hermes_profile_entry():
    assert "hermes" not in launcher.TOOL_ENV, (
        "TOOL_ENV 的 HERMES_PROFILE 是死配置（hermes 从不读该 env）——#650 已移除，勿回填"
    )


def test_cmd_build_substitutes_role_into_flag():
    role = "laowantong"
    cmd = [part.replace("{prompt}", "P").replace("{role}", role) for part in launcher.TOOLS["hermes"]]
    i = cmd.index("-p")
    assert cmd[i + 1] == role
    assert "{role}" not in " ".join(cmd) and "{prompt}" not in " ".join(cmd)
