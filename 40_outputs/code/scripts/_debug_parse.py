import json, re, sys
from pathlib import Path

# Pick first parse error file
target = Path(r"C:\Users\Administrator\Desktop\wiki\00_inbox\战略专题\冉鹏PPT截图")
for f in sorted(target.glob("*_vlm_desc.md")):
    content = f.read_text(encoding="utf-8")
    if '"_parse_error": true' not in content:
        continue
    print(f"=== {f.name} ===")
    raw = re.search(r'## 原始 JSON\s*\n\s*```json\s*\n(.*?)\n```', content, re.DOTALL)
    if not raw:
        print("  FAIL: could not find raw JSON section")
        continue
    saved = json.loads(raw.group(1))
    desc = saved.get("description", "")
    print(f"  desc length: {len(desc)}")
    print(f"  desc starts with: {repr(desc[:100])}")

    # Try to extract inner JSON
    fence = re.search(r'```(?:json)?\s*\n?(.*?)```', desc, re.DOTALL)
    if fence:
        chunk = fence.group(1).strip()
        print(f"  fence extracted {len(chunk)} chars, starts: {repr(chunk[:100])}")
        try:
            inner = json.loads(chunk)
            print(f"  json.loads OK: title={inner.get('title','')}")
        except json.JSONDecodeError as e:
            print(f"  json.loads FAILED: {e}")
        try:
            import json5
            inner = json5.loads(chunk)
            print(f"  json5 OK: title={inner.get('title','')}")
        except Exception as e:
            print(f"  json5 FAILED: {e}")
    else:
        print("  no code fence found in description")
        # Try direct parse
        if desc.strip().startswith('{'):
            try:
                inner = json.loads(desc)
                print(f"  direct json.loads OK: {inner.get('title','')}")
            except Exception as e:
                print(f"  direct json.loads FAILED: {e}")
    break
