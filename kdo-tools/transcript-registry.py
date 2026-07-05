#!/usr/bin/env python3
"""
口述稿预处理注册表——王语嫣启动时先查这个，知道哪些口述稿已经预处理好了。

Usage:
  python kdo-tools/transcript-registry.py list
  python kdo-tools/transcript-registry.py check <口述稿路径>
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent
REGISTRY = WIKI / ".kdo" / "transcript-registry.json"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def load_registry() -> dict:
    if not REGISTRY.exists():
        return {"transcripts": {}}
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def save_registry(data: dict):
    REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    REGISTRY.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def register(transcript_path: Path):
    """Register a transcript and its preprocessed assets."""
    data = load_registry()
    rel = str(transcript_path.resolve().relative_to(WIKI.resolve()))
    processed_dir = transcript_path.parent / "_processed"
    stem = transcript_path.stem

    assets = []
    for suffix in ["_索引.json", "_主题索引.md", "_高价值段落汇编.md"]:
        f = processed_dir / f"{stem}{suffix}"
        if f.exists():
            assets.append(str(f.relative_to(WIKI)))

    data["transcripts"][rel] = {
        "registered_at": datetime.now(timezone.utc).isoformat(),
        "assets": assets,
    }
    save_registry(data)


def cmd_list():
    data = load_registry()
    if not data["transcripts"]:
        print("暂无已预处理的口述稿")
        return 0

    print(f"已预处理的口述稿（{len(data['transcripts'])} 份）\n")
    for path, info in data["transcripts"].items():
        print(f"  {path}")
        for a in info["assets"]:
            print(f"    → {a}")
        print()
    return 0


def cmd_check(path: Path):
    data = load_registry()
    rel = str(path.resolve().relative_to(WIKI.resolve()))
    if rel in data["transcripts"]:
        info = data["transcripts"][rel]
        print(f"✅ 已预处理：{rel}")
        for a in info["assets"]:
            print(f"   {a}")
    else:
        print(f"❌ 未预处理：{rel}")
        print(f"   先跑：python kdo-tools/transcript-index.py build <路径>")
    return 0


def main():
    import argparse
    parser = argparse.ArgumentParser(description="口述稿预处理注册表")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list", help="列出所有已预处理的口述稿")
    p_check = sub.add_parser("check", help="检查某个口述稿是否已预处理")
    p_check.add_argument("path")
    args = parser.parse_args()

    if args.cmd == "list":
        return cmd_list()
    elif args.cmd == "check":
        return cmd_check(Path(args.path))


if __name__ == "__main__":
    sys.exit(main())
