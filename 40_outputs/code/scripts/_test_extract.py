import re, json
from pathlib import Path

target = Path(r"C:\Users\Administrator\Desktop\wiki\00_inbox\战略专题\冉鹏PPT截图")

for f in sorted(target.glob("*_vlm_desc.md")):
    if "_111_" not in f.name and "_114_" not in f.name:
        continue
    content = f.read_text(encoding="utf-8")
    print(f"=== {f.name} ===")

    # Simple manual test of the regex
    # Find ## 原始 JSON position
    idx = content.find("## 原始 JSON")
    print(f"  Found 原始 JSON at idx {idx}")

    # Extract from that point
    from_idx = content[idx:]

    # Use re.DOTALL
    m = re.search(r"## 原始 JSON\s*\n\s*" + re.escape("```") + r"json\s*\n(.*?)\n" + re.escape("```"), from_idx, re.DOTALL)
    print(f"  regex match in slice: {'YES' if m else 'NO'}")

    # Try same regex on FULL content
    m2 = re.search(r"## 原始 JSON\s*\n\s*" + re.escape("```") + r"json\s*\n(.*?)\n" + re.escape("```"), content, re.DOTALL)
    print(f"  regex match in full: {'YES' if m2 else 'NO'}")

    if m2:
        raw = m2.group(1)
        print(f"  group(1) length: {len(raw)}")
        print(f"  first 100: {repr(raw[:100])}")
        try:
            outer = json.loads(raw)
            print(f"  json.loads OK: _parse_error={outer.get('_parse_error')}, desc_len={len(outer.get('description',''))}")
        except json.JSONDecodeError as e:
            print(f"  json.loads FAILED at line {e.lineno}: {e}")
            # Show problem area
            lines = raw.split('\n')
            if e.lineno <= len(lines):
                print(f"  line: {repr(lines[e.lineno-1][:150])}")
    break
