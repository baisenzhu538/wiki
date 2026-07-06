#!/usr/bin/env python3
"""
Agent 每日上下文自动存储——双写管线 + Truman 模板 + 自动自检。

每次保存同时写入两个位置：
  1. 桌面 agent复盘/<agent>/daily-context/YYYY-MM-DD.md  （人看）
  2. 60_feedback/session-archives/YYYY-MM-DD/{agent-id}.md （Agent检索+kdo query可查）

Usage:
  python kdo-tools/daily-context-save.py save --agent <id> --truman --stdin  # 从 stdin 读复盘（推荐）
  python kdo-tools/daily-context-save.py save --agent <id> --text "<摘要>" [--truman]
  python kdo-tools/daily-context-save.py list --agent <id>
"""

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent
REVIEW_DIR = Path.home() / "Desktop" / "agent复盘"
ARCHIVE_DIR = WIKI / "60_feedback" / "session-archives"

TRUMAN_TEMPLATE = """## 概要
> 一句话：今天做了什么？



## 关键决策

| 决策 | 理由 | 结果 |
|:---|:---|:---|
| | | |

## 思维盲点
> ≥1条：什么被漏掉了？每条追问"为什么漏掉"。

1.

## 顿悟
> ≥1条：什么基础认知被推翻了？

1.

## 过程资产

| 新增/更新 | 路径 |
|:---|:---|
| | |

## 元反思
> 下次怎么做才能不一样？

1.

---

## Truman复盘

### 逐轮映射

| 轮次 | 人做了什么 | 双三角 | AI做了什么 | 双三角 |
|:---|:---|:---|:---|:---|
| 1 | | | | |

### 飞轮效应
> 本轮加速了哪个回路？



### 对照实验
- 无人协作：人需要____小时
- 无AI协作：AI只能产出____分
- 合在一起：____分钟，质量____

### 下次改进
- Agent自身：____
- 方法论卡更新：____
"""

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def _run_review_check(agent: str) -> str:
    """运行 review-check.py 并返回等级字符串。"""
    try:
        import importlib.util
        rc_path = Path(__file__).parent / "review-check.py"
        spec = importlib.util.spec_from_file_location("review_check", str(rc_path))
        rc = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(rc)
        today = datetime.now().strftime("%Y-%m-%d")
        result = rc.check_agent(agent, today)
        if result["status"] != "ok":
            return "❌ 未复盘"
        g = result.get("grade", "?")
        e = result.get("emoji", "")
        if result.get("retrieval", {}).get("has_discovery"):
            return f"{e} {g}级 📚检索有发现"
        elif result.get("retrieval", {}).get("has_retrieval"):
            return f"{e} {g}级 ✅已检索"
        return f"{e} {g}级 ⚠️未检索wiki"
    except Exception as ex:
        return f"⚠️ {ex}"


def cmd_save(args):
    agent = args.agent
    today = datetime.now().strftime("%Y-%m-%d")
    ts = now_iso()
    session_id = f"{agent}-{today}"

    # 读取复盘内容：优先级 --file > --stdin > --text
    body = ""
    if getattr(args, "file", ""):
        fp = Path(args.file)
        if fp.exists():
            body = fp.read_text(encoding="utf-8")
        else:
            print(f"❌ 文件不存在：{args.file}", file=sys.stderr)
            return 1
    elif getattr(args, "stdin", False):
        body = sys.stdin.read()
    else:
        body = args.text or ""

    fm_lines = [
        "---",
        f"session_id: {session_id}",
        f"agent_id: {agent}",
        f"date: {today}",
        f"created_at: {ts}",
        f"updated_at: {ts}",
    ]
    fm_lines.append("---")
    fm = "\n".join(fm_lines)

    # Truman 模板模式：内容直接作为正文（不再套 Agent 输入壳）
    if getattr(args, "truman", False):
        if body.strip():
            full_body = body.strip()
        else:
            full_body = TRUMAN_TEMPLATE
    else:
        full_body = body.strip() if body.strip() else "(无内容)"

    content = f"{fm}\n\n# {agent} · {today}\n\n{full_body}\n"

    # Write 1: Desktop (human-readable)
    desktop_dir = REVIEW_DIR / agent / "daily-context"
    desktop_dir.mkdir(parents=True, exist_ok=True)
    desktop_path = desktop_dir / f"{today}.md"
    desktop_path.write_text(content, encoding="utf-8")

    # Write 2: Archive (agent-searchable, kdo query can find)
    archive_dir = ARCHIVE_DIR / today
    archive_dir.mkdir(parents=True, exist_ok=True)
    archive_path = archive_dir / f"{agent}.md"
    archive_path.write_text(content, encoding="utf-8")

    print(f"已保存：{desktop_path}")
    print(f"已存档：{archive_path.relative_to(WIKI)}")

    # 自动跑 review-check 并显示等级
    grade = _run_review_check(agent)
    print(f"自检：{grade}")

    return 0


def cmd_list(args):
    agent = args.agent
    d = REVIEW_DIR / agent / "daily-context"
    if not d.exists():
        print("暂无上下文记录")
        return 0
    files = sorted(d.glob("*.md"), reverse=True)
    print(f"{agent} 每日上下文（{len(files)} 条）")
    for f in files[:10]:
        size = f.stat().st_size
        fname = f.stem
        # Quick quality check
        content = f.read_text(encoding="utf-8", errors="ignore")
        ch_count = sum(1 for ch in ["概要", "关键决策", "思维盲点", "顿悟", "逐轮映射"] if ch in content)
        flag = "✅" if ch_count >= 5 else "⚠️" if ch_count >= 3 else "❌"
        print(f"  {fname} — {size}B {flag} ({ch_count}/5 关键章)")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Agent 每日上下文存储")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_save = sub.add_parser("save", help="保存今日上下文")
    p_save.add_argument("--agent", required=True)
    p_save.add_argument("--text", default="", help="上下文摘要（短内容用；长内容用 --stdin 或 --file）")
    p_save.add_argument("--stdin", action="store_true", help="从标准输入读取复盘内容（管道输入）")
    p_save.add_argument("--file", default="", help="从指定文件读取复盘内容（Agent 先 Write 到此路径）")
    p_save.add_argument("--truman", action="store_true", help="Truman 10章模式：纯模板 / 配合 --stdin/--file 保存复盘")

    p_list = sub.add_parser("list", help="列出历史上下文")
    p_list.add_argument("--agent", required=True)

    args = parser.parse_args()
    if args.cmd == "save":
        return cmd_save(args)
    elif args.cmd == "list":
        return cmd_list(args)


if __name__ == "__main__":
    sys.exit(main())
