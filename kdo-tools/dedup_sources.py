#!/usr/bin/env python3
"""Source registry dedup scanner. Run periodically to detect near-duplicates."""
import re, sys
from pathlib import Path
from collections import defaultdict

REGISTRY = Path(__file__).resolve().parent.parent / "90_control" / "source-registry.yaml"

def scan():
    if not REGISTRY.exists():
        print("Registry not found")
        return

    text = REGISTRY.read_text(encoding="utf-8")
    entries = re.split(r'\n(?=- src_)', text)

    # Group by possible duplicates: same itingnao ID, same source name
    by_itingnao = defaultdict(list)
    by_name = defaultdict(list)

    for entry in entries:
        entry = entry.strip()
        if not entry.startswith("- src_"):
            continue
        m_itingnao = re.search(r'itingnao_id:\s*"?(\d+)"?', entry)
        m_name = re.search(r'name:\s*"([^"]+)"', entry)
        m_src = re.search(r'(src_\d+_\w+)', entry)

        if m_itingnao and m_src:
            by_itingnao[m_itingnao.group(1)].append(m_src.group(1))
        if m_name and m_src:
            by_name[m_name.group(1)].append(m_src.group(1))

    dupes_found = 0
    for itingnao_id, srcs in by_itingnao.items():
        if len(srcs) > 1:
            print(f"⚠️  itingnao_id={itingnao_id} has {len(srcs)} sources: {', '.join(srcs)}")
            dupes_found += 1

    for name, srcs in by_name.items():
        if len(srcs) > 1:
            print(f"⚠️  name='{name}' has {len(srcs)} sources: {', '.join(srcs)}")
            dupes_found += 1

    if dupes_found == 0:
        print("✅ No duplicate sources found")
    else:
        print(f"\n{dupes_found} potential duplicates detected")

if __name__ == "__main__":
    scan()
