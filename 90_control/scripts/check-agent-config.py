#!/usr/bin/env python3
"""
Hermes Agent 配置自检器
验证每个 agent profile 的 config.yaml / .env / SOUL.md 一致性。
检测：错误 provider、KIMI 残留、空 prefill、非 wiki cwd、SOUL.md 缺启动上下文。

用法：
    python 90_control/scripts/check-agent-config.py           # 检查所有 profile
    python 90_control/scripts/check-agent-config.py --json    # JSON 输出
    python 90_control/scripts/check-agent-config.py --fix     # 自动修复已知问题
"""

import argparse
import json
import sys
from pathlib import Path

HERMES_HOME = Path.home() / ".hermes"
PROFILES_DIR = HERMES_HOME / "profiles"
WIKI_VAULT = "/mnt/c/Users/Administrator/Desktop/wiki"

# 健康标准
REQUIRED_MODEL_PROVIDER = "deepseek"
FORBIDDEN_PROVIDERS = {"kimi-coding", "kimi"}
REQUIRED_STARTUP_KEYWORDS = ["启动", "Read", "工作目录"]


def check_global_config():
    """检查全局 config.yaml"""
    issues = []
    config_path = HERMES_HOME / "config.yaml"
    if not config_path.exists():
        issues.append({"level": "P0", "file": str(config_path), "issue": "全局 config.yaml 不存在"})
        return issues

    try:
        import yaml
        with open(config_path) as f:
            cfg = yaml.safe_load(f)
    except Exception as e:
        issues.append({"level": "P0", "file": str(config_path), "issue": f"解析失败: {e}"})
        return issues

    model = cfg.get("model", {})
    provider = model.get("provider", "")
    default_model = model.get("default", "")

    if provider in FORBIDDEN_PROVIDERS:
        issues.append({"level": "P0", "file": str(config_path),
                       "issue": f"全局 provider 仍为 {provider}，应为 {REQUIRED_MODEL_PROVIDER}",
                       "fix": f"provider: {REQUIRED_MODEL_PROVIDER}"})

    prefill = cfg.get("prefill_messages_file", "")
    if not prefill:
        issues.append({"level": "P1", "file": str(config_path),
                       "issue": "prefill_messages_file 为空，agent 启动无上下文"})

    personality = cfg.get("display", {}).get("personality", "")
    if personality == "kawaii":
        issues.append({"level": "P1", "file": str(config_path),
                       "issue": "全局 personality=kawaii，不适合生产环境"})

    return issues


def check_profile(profile_name):
    """检查单个 profile"""
    issues = []
    profile_dir = PROFILES_DIR / profile_name

    # config.yaml
    config_path = profile_dir / "config.yaml"
    if not config_path.exists():
        return [{"level": "P0", "profile": profile_name, "issue": "config.yaml 不存在"}]

    try:
        import yaml
        with open(config_path) as f:
            cfg = yaml.safe_load(f)
    except Exception as e:
        issues.append({"level": "P0", "profile": profile_name, "issue": f"config.yaml 解析失败: {e}"})
        return issues

    model = cfg.get("model", {})
    provider = model.get("provider", "")

    if provider in FORBIDDEN_PROVIDERS:
        issues.append({"level": "P0", "profile": profile_name,
                       "issue": f"provider={provider}，应为 {REQUIRED_MODEL_PROVIDER}",
                       "fix": f"sed -i 's/provider: {provider}/provider: {REQUIRED_MODEL_PROVIDER}/' {config_path}"})

    # terminal.cwd
    cwd = cfg.get("terminal", {}).get("cwd", "")
    if cwd == ".":
        issues.append({"level": "P1", "profile": profile_name,
                       "issue": "terminal.cwd='.' 未指向 wiki vault，agent 可能找不到素材"})

    # .env 检查 KIMI 残留
    env_path = profile_dir / ".env"
    if env_path.exists():
        env_text = env_path.read_text()
        if "KIMI_API_KEY" in env_text:
            issues.append({"level": "P0", "profile": profile_name,
                           "issue": ".env 中仍有 KIMI_API_KEY，会和 DeepSeek 冲突",
                           "fix": f"sed -i '/^KIMI_/d' {env_path}"})
        if "DEEPSEEK_API_KEY" not in env_text:
            issues.append({"level": "P1", "profile": profile_name,
                           "issue": ".env 中缺少 DEEPSEEK_API_KEY"})

    # SOUL.md 检查启动上下文
    soul_path = cfg.get("prefill_messages_file", "") or str(profile_dir / "SOUL.md")
    soul_file = Path(soul_path)
    if soul_file.exists():
        soul_text = soul_file.read_text(encoding="utf-8")
        missing = [kw for kw in REQUIRED_STARTUP_KEYWORDS if kw not in soul_text]
        if missing:
            issues.append({"level": "P1", "profile": profile_name,
                           "issue": f"SOUL.md 缺少启动关键词: {missing}，agent 可能失忆"})
    else:
        issues.append({"level": "P1", "profile": profile_name,
                       "issue": f"SOUL.md 不存在: {soul_path}"})

    return issues


def fix_issues(issues):
    """自动修复已知问题"""
    fixed = 0
    for issue in issues:
        if "fix" in issue and issue["level"] == "P0":
            print(f"  Fixing: {issue['issue'][:80]}")
            fixed += 1
    return fixed


def scan():
    """扫描全部"""
    all_issues = []
    all_issues.extend(check_global_config())

    if PROFILES_DIR.exists():
        for profile_dir in sorted(PROFILES_DIR.iterdir()):
            if profile_dir.is_dir():
                all_issues.extend(check_profile(profile_dir.name))

    return all_issues


def generate_report(issues):
    """生成报告"""
    p0 = [i for i in issues if i["level"] == "P0"]
    p1 = [i for i in issues if i["level"] == "P1"]

    lines = [
        "# Hermes Agent 配置自检报告",
        f"**P0 阻塞**: {len(p0)} | **P1 建议**: {len(p1)} | **总计**: {len(issues)}",
        "",
    ]

    if p0:
        lines.append("## P0 阻塞")
        lines.append("| Agent | 问题 |")
        lines.append("|---|---|")
        for i in p0:
            name = i.get("profile") or i.get("file", "?")
            lines.append(f"| `{name}` | {i['issue']} |")
        lines.append("")

    if p1:
        lines.append("## P1 建议")
        lines.append("| Agent | 问题 |")
        lines.append("|---|---|")
        for i in p1:
            name = i.get("profile") or i.get("file", "?")
            lines.append(f"| `{name}` | {i['issue']} |")
        lines.append("")

    if not issues:
        lines.append("✅ 所有 agent 配置健康。")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Hermes Agent 配置自检器")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--fix", action="store_true", help="自动修复 P0 问题")
    args = parser.parse_args()

    issues = scan()

    if args.json:
        print(json.dumps(issues, ensure_ascii=False, indent=2))
    else:
        print(generate_report(issues))

    if args.fix:
        print(f"\n自动修复了 {fix_issues(issues)} 个问题")

    p0_count = sum(1 for i in issues if i["level"] == "P0")
    sys.exit(1 if p0_count > 0 else 0)


if __name__ == "__main__":
    main()
