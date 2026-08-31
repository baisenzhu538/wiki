#!/usr/bin/env python3
"""注册副本转发桩（#584，2026-08-31，黄药师）。

本文件不再是代码副本——是转发到真身的桩：
    真身 = kdo-tools/wechat_promote.py（唯一活代码，含 #380 编排门禁 /
           #395 updated_at 归一化 / #516 _processed 隔离区三代修复）
    本桩 = 40_outputs/code/scripts/ 注册位（可发现性保留，调用即转发）

为什么是桩不是副本：双副本手工同步已实证漂移 3 代——旧副本缺 #380 门禁，
谁跑它就会绕过王语嫣编排门禁直写 30_wiki/cases/（08-31 #584 评估实证）。
桩让漂移结构性不可能。改代码 → 只改 kdo-tools/ 真身，本桩永不修改。
"""
import runpy
import sys
from pathlib import Path

_HERE = Path(__file__).resolve()
_CANON = _HERE.parent.parent.parent.parent / "kdo-tools" / "wechat_promote.py"

if __name__ == "__main__":
    if not _CANON.exists():
        sys.exit(f"[stub] 真身不存在: {_CANON}")
    sys.argv[0] = str(_CANON)
    runpy.run_path(str(_CANON), run_name="__main__")
