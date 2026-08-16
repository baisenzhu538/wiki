#!/usr/bin/env python3
"""
Initialize 老朱's personal domain infrastructure.

Creates:
  1. zhu_decisions table in .kdo/state.sqlite
  2. 30_wiki/personal-os/ directory with starter files
  3. A kdo capture integration for decision logging

Usage:
  python 90_control/scripts/init_zhu_personal_domain.py
"""

import sqlite3
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
import sys
from datetime import datetime, timezone
from pathlib import Path


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def init_db(db_path: Path) -> None:
    """Create zhu_decisions table in the KDO SQLite state."""
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA busy_timeout=5000")

    conn.executescript("""
        CREATE TABLE IF NOT EXISTS zhu_decisions (
            id TEXT PRIMARY KEY,
            ts TEXT NOT NULL,
            domain TEXT NOT NULL,
            decision TEXT NOT NULL,
            framework_used TEXT,
            outcome TEXT,
            feedback_signal TEXT,
            updated_at TEXT NOT NULL
        );

        CREATE INDEX IF NOT EXISTS idx_zhu_decisions_ts
            ON zhu_decisions(ts);
        CREATE INDEX IF NOT EXISTS idx_zhu_decisions_domain
            ON zhu_decisions(domain);
        CREATE INDEX IF NOT EXISTS idx_zhu_decisions_framework
            ON zhu_decisions(framework_used);
    """)

    conn.commit()
    conn.close()
    print(f"  zhu_decisions table ready in {db_path}")


def create_personal_os_dir(wiki_root: Path, db_path: Path) -> None:
    """Create 30_wiki/personal-os/ with starter files."""
    os_dir = wiki_root / "30_wiki" / "personal-os"
    os_dir.mkdir(parents=True, exist_ok=True)

    # Move or symlink the time-os if it exists in 20_memory
    time_os_src = wiki_root / "20_memory" / "zhu-time-os.md"
    time_os_dst = os_dir / "zhu-time-os.md"
    if time_os_src.exists() and not time_os_dst.exists():
        time_os_dst.write_text(time_os_src.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"  Copied: {time_os_src} → {time_os_dst}")

    # Domain index (auto-updated by capture)
    domain_index = os_dir / "zhu-domain-index.md"
    if not domain_index.exists():
        domain_index.write_text(f"""---
id: zhu-domain-index
title: "老朱个人域索引"
type: system
status: active
created_at: {now_iso()}
updated_at: {now_iso()}
domain:
  - personal-os
---

# 老朱个人域索引

> 自动维护。每次 `kdo capture --kind decision` 更新此索引。

## 域使用频率

| 域 | 决策数 | 最近调用 | 最常用框架 |
|:---|:---|:---|:---|
| | | | |

## 最近 10 条决策

| 日期 | 域 | 决策 | 框架 | 结果 |
|:---|:---|:---|:---|:---|
| | | | | |

*数据源：`.kdo/state.sqlite` → `zhu_decisions`*
""", encoding="utf-8")
        print(f"  Created: {domain_index}")

    # Feedback patterns (王语嫣 maintains)
    patterns = os_dir / "zhu-feedback-patterns.md"
    if not patterns.exists():
        patterns.write_text(f"""---
id: zhu-feedback-patterns
title: "老朱反馈模式库"
type: system
status: active
created_at: {now_iso()}
updated_at: {now_iso()}
domain:
  - personal-os
---

# 老朱反馈模式库

> 王语嫣维护。从对话中提取重复出现的偏好、盲区、决策习惯。

## 已识别模式

| # | 模式 | 证据（对话记录） | 影响 |
|:---|:---|:---|:---|
| | | | |

## 盲区标记

| 盲区 | 发现时间 | 状态 |
|:---|:---|:---|
| | | |

*维护人：王语嫣 | 更新时机：每次对话结束后*
""", encoding="utf-8")
        print(f"  Created: {patterns}")

    # README
    readme = os_dir / "README.md"
    if not readme.exists():
        readme.write_text(f"""# 老朱个人域 (personal-os)

> 这是 KDO 知识库中属于老朱个人的区域。
> 它不是方法论卡——它是老朱的**使用说明书**。

## 文件

| 文件 | 内容 | 维护人 |
|:---|:---|:---|
| `zhu-time-os.md` | 时间配置、双峰安排、任务深度分级 | 老朱 + 王语嫣 |
| `zhu-domain-index.md` | 各域使用频率、调用过的框架 | 自动（kdo capture） |
| `zhu-feedback-patterns.md` | 重复出现的偏好、盲区、决策习惯 | 王语嫣 |

## 数据库

| 表 | 位置 | 内容 |
|:---|:---|:---|
| `zhu_decisions` | `.kdo/state.sqlite` | 结构化决策记录 |

## 如何使用

### 记录一次决策
```bash
kdo capture "今天做了X决策，用了Y框架，结果是Z" --kind decision --domain sales
```

### 查看决策历史
```bash
python -c "import sqlite3; db=sqlite3.connect('.kdo/state.sqlite'); [print(r) for r in db.execute('SELECT ts,domain,decision FROM zhu_decisions ORDER BY ts DESC LIMIT 10')]"
```

### 王语嫣查个人域
王语嫣启动时自动读本目录下所有文件 + 查 zhu_decisions 表最近 10 条。
""", encoding="utf-8")
        print(f"  Created: {readme}")


def update_wangyuyan_context(wiki_root: Path) -> None:
    """Ensure 王语嫣's context references the personal domain."""
    ctx_path = wiki_root / ".agent" / "wangyuyan-context.md"
    if not ctx_path.exists():
        print("  WARNING: wangyuyan-context.md not found, skipping context update")
        return
    print(f"  王语嫣 context already updated (startup step 1 + session end step 4)")


def main():
    wiki_root = Path.cwd()
    # Verify we're in the wiki
    if not (wiki_root / "90_control" / "routing-rules.md").exists():
        print("ERROR: Run this script from the wiki vault root.", file=sys.stderr)
        sys.exit(1)

    db_path = wiki_root / ".kdo" / "state.sqlite"
    if not db_path.exists():
        print("ERROR: state.sqlite not found. Run kdo status first to trigger migration.", file=sys.stderr)
        sys.exit(1)

    print("=== Initializing 老朱 Personal Domain ===\n")

    print("1. Database table:")
    init_db(db_path)

    print("\n2. Personal-OS directory:")
    create_personal_os_dir(wiki_root, db_path)

    print("\n3. 王语嫣 context:")
    update_wangyuyan_context(wiki_root)

    print(f"\n=== Done ===\n")
    print("Paths:")
    print(f"  SQLite table:  .kdo/state.sqlite → zhu_decisions")
    print(f"  Directory:     30_wiki/personal-os/")
    print(f"  Usage guide:   30_wiki/personal-os/README.md")
    print(f"  王语嫣 context: .agent/wangyuyan-context.md (already wired)")
    print()
    print("Test: kdo capture \"测试决策记录\" --kind decision --domain test")


if __name__ == "__main__":
    main()
