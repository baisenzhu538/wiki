import re, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from repair_vlm_parse_errors import _extract_inner_from_raw_json, _robust_json_parse

target = Path(r"C:\Users\Administrator\Desktop\wiki\00_inbox\战略专题\冉鹏PPT截图")

for f in sorted(target.glob("*_vlm_desc.md")):
    if "_111_" not in f.name and "_114_" not in f.name:
        continue
    content = f.read_text(encoding="utf-8")
    print(f"=== {f.name} ===")
    inner = _extract_inner_from_raw_json(content)
    print(f"  _extract_inner: {'OK' if inner else 'NULL'}")
    if not inner:
        # Step through manually
        raw_match = re.search(
            r'## 原始 JSON\s*\n\s*```json\s*\n(.*?)\n```',
            content, re.DOTALL
        )
        print(f"  raw_match: {'YES' if raw_match else 'NO'}")
        if raw_match:
            try:
                outer = json.loads(raw_match.group(1))
                print(f"  json.loads: OK, _parse_error={outer.get('_parse_error')}")
                print(f"  desc length: {len(outer.get('description',''))}")
            except json.JSONDecodeError as e:
                print(f"  json.loads FAILED: {e}")
    break
