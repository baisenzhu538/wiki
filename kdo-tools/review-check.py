#!/usr/bin/env python3
"""Agent 复盘检查——一眼看出谁复盘了、谁没复盘。"""
import sys
from datetime import datetime
from pathlib import Path

REVIEW_DIR = Path.home() / "Desktop" / "agent复盘"

AGENTS = ["huangyaoshi", "wangyuyan", "laowantong", "ouyangfeng", "sales-dialogue-assistant"]

today = datetime.now().strftime("%Y-%m-%d")

print(f"Agent 复盘检查 — {today}\n")

for agent in AGENTS:
    d = REVIEW_DIR / agent / "daily-context"
    f = d / f"{today}.md"
    if f.exists():
        size = f.stat().st_size
        content = f.read_text(encoding="utf-8", errors="ignore")
        has_truman = "逐轮映射" in content or "对照实验" in content or "飞轮效应" in content
        status = "✅ Truman格式" if has_truman else "⚠️ 旧格式"
        print(f"  {agent:<30} {status} ({size}B)")
    else:
        print(f"  {agent:<30} ❌ 未复盘")
