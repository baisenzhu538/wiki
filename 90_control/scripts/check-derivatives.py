#!/usr/bin/env python3
"""派生副本手改检测（#369）——派生物必须由脚本生成，手改即报警。

检测逻辑：生成器在写入后把输出 hash 记录到 .derived-hashes.json；
本脚本计算当前文件 hash 与基线比对——不匹配 = 手改（或生成器未跑）。

用法：
    python 90_control/scripts/check-derivatives.py            # 人类可读
    python 90_control/scripts/check-derivatives.py --json     # JSON 输出

退出码：0 = 全部一致；1 = 检测到手改/基线缺失
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SCRIPT_DIR = Path(__file__).resolve().parent
HASH_FILE = SCRIPT_DIR / ".derived-hashes.json"

# 受检派生物（生成器写入 .derived-hashes.json 的 key 与这里一致）
DERIVATIVES = [
    "70_product/tasks/dashboard.html",
    ".agent/agent-contexts-summary.md",
    "90_control/vault-status.md",
]


def main():
    parser = argparse.ArgumentParser(description="派生副本手改检测（#369）")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    root = SCRIPT_DIR.parent.parent
    if not HASH_FILE.exists():
        if args.json:
            print(json.dumps({"error": "基线文件缺失——先跑一次各生成器建立基线"}, ensure_ascii=False))
        else:
            print("[WARN] .derived-hashes.json 基线缺失——请先运行三个生成器建立基线：")
            print("  python kdo-tools/generate-dashboard.py")
            print("  python 90_control/scripts/summarize-agent-contexts.py")
            print("  python 90_control/scripts/vault-snapshot.py")
        sys.exit(1)

    baseline = json.loads(HASH_FILE.read_text(encoding="utf-8"))
    findings = []
    for rel in DERIVATIVES:
        path = root / rel
        key = str(path)
        if key not in baseline:
            findings.append({"file": rel, "level": "NO_BASELINE",
                             "detail": "生成器未跑过或路径变更"})
            continue
        if not path.exists():
            findings.append({"file": rel, "level": "MISSING",
                             "detail": "文件不存在"})
            continue
        cur = hashlib.sha256(path.read_bytes()).hexdigest()
        if cur != baseline[key]:
            findings.append({"file": rel, "level": "HAND_EDITED",
                             "detail": "hash 与基线不一致——派生物被手改或生成器输出已变化，请重新生成"})
        else:
            findings.append({"file": rel, "level": "OK", "detail": "与基线一致（脚本生成）"})

    bad = [f for f in findings if f["level"] != "OK"]
    if args.json:
        print(json.dumps({"derivatives": findings, "exit": 1 if bad else 0},
                         ensure_ascii=False, indent=2))
    else:
        print("=" * 60)
        print(f"  KDO 派生副本手改检测 (#369)  |  {'HAND-EDIT DETECTED' if bad else 'CLEAN'}")
        print("=" * 60)
        for f in findings:
            print(f"  [{f['level']}] {f['file']}: {f['detail']}")
        print()
        if bad:
            print("[FAIL] 派生物与基线不一致——重新生成（勿手改派生物）。")
        else:
            print("[PASS] 全部派生物为脚本生成。")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
