#!/usr/bin/env python3
"""src_ID → 10_raw/sources/ 映射索引。每个 src_* ID 对应唯一的源文件路径。

Usage:
  python 90_control/scripts/source-id-registry.py              # 打印映射表
  python 90_control/scripts/source-id-registry.py --missing    # 检查卡片引用的 src 是否存在
  python 90_control/scripts/source-id-registry.py --rebuild    # 重建完整映射
"""

import re, json, sys
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent.parent
SOURCES_DIR = ROOT / "10_raw" / "sources"
MAPPING_FILE = ROOT / ".kdo" / "source_id_map.json"

def scan_sources() -> dict[str, str]:
    """Scan 10_raw/sources/ and build src_ID → filename mapping."""
    mapping = {}
    if not SOURCES_DIR.is_dir():
        return mapping
    for f in sorted(SOURCES_DIR.glob("*.md")):
        name = f.stem
        m = re.match(r'(src_\d+_\w{8})', name)
        if m:
            src_id = m.group(1)
            mapping[src_id] = f.relative_to(ROOT).as_posix()
    return mapping

def scan_cards() -> list[dict]:
    """Scan 30_wiki/ for all source_refs references."""
    refs = []
    wiki = ROOT / "30_wiki"
    card_dirs = ["concepts", "frameworks", "tools", "cases", "dark-knowledges", "entities", "decisions", "systems", "projects"]
    for sub in card_dirs:
        d = wiki / sub
        if not d.is_dir():
            continue
        for f in sorted(d.glob("*.md")):
            if f.name in ("index.md", "log.md", "contradictions.md"):
                continue
            try:
                content = f.read_text(encoding="utf-8")
            except Exception:
                continue
            found = re.findall(r'(src_\d+_\w{8})', content)
            for src_id in set(found):
                refs.append({"card": f.relative_to(ROOT).as_posix(), "src": src_id})
    return refs

def rebuild():
    mapping = scan_sources()
    MAPPING_FILE.parent.mkdir(parents=True, exist_ok=True)
    MAPPING_FILE.write_text(json.dumps(mapping, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Indexed {len(mapping)} sources → {MAPPING_FILE}")

def report_missing():
    mapping = scan_sources()
    refs = scan_cards()
    missing = defaultdict(list)
    for r in refs:
        if r["src"] not in mapping:
            missing[r["src"]].append(r["card"])
    if missing:
        print(f"⚠️  {len(missing)} source IDs referenced by cards but NOT found in 10_raw/sources/:")
        for src_id, cards in sorted(missing.items())[:20]:
            print(f"  {src_id}: {len(cards)} card(s)")
            for c in cards[:3]:
                print(f"    ← {c}")
            if len(cards) > 3:
                print(f"    ... and {len(cards)-3} more")
    else:
        print("✅ All source IDs found in 10_raw/sources/")

if __name__ == "__main__":
    if "--rebuild" in sys.argv:
        rebuild()
    elif "--missing" in sys.argv:
        report_missing()
    else:
        mapping = scan_sources()
        print(f"Sources indexed: {len(mapping)}")
        for src_id, path in sorted(mapping.items())[:10]:
            print(f"  {src_id} → {path}")
        if len(mapping) > 10:
            print(f"  ... and {len(mapping)-10} more")
