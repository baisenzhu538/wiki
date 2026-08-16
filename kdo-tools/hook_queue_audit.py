#!/usr/bin/env python3
"""UserPromptSubmit hook: 用户消息含队列/看板/入队/对账关键词时，运行 queue_audit 并把结果注入上下文（E021 环境强制）。

配合 .claude/settings.json 的 UserPromptSubmit hook 使用。
"""
import sys
import json
import subprocess
import os

WIKI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEYWORDS = ["队列", "看板", "入队", "全部完成", "队列状态", "队列健康", "对账", "queue"]


def main():
    # Windows 上 stdin/stdout 默认 GBK——强制 UTF-8 字节流（Claude Code 传 UTF-8 JSON）
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    try:
        raw = sys.stdin.buffer.read()
        data = json.loads(raw.decode("utf-8", errors="replace"))
        prompt = data.get("prompt", "")
    except Exception:
        prompt = ""
    if not any(k in prompt for k in KEYWORDS):
        print(json.dumps({"suppressOutput": True}))
        return
    r = subprocess.run(
        [sys.executable, os.path.join(WIKI, "kdo-tools", "queue_audit.py"), "--brief"],
        capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=WIKI, timeout=30,
    )
    out = (r.stdout or r.stderr or "QUEUE_AUDIT: 运行失败").strip()
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": "[队列对账-E021环境强制] " + out,
        }
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
