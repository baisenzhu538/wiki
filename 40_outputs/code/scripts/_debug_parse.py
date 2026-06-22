import json, re, sys
from pathlib import Path

# Test Chinese quote cleaning on first parse error file
target = Path(r"C:\Users\Administrator\Desktop\wiki\00_inbox\战略专题\冉鹏PPT截图")

def _clean_chinese_quotes(text):
    result = re.sub(r'([一-鿿　-〿＀-￯])"'
                    r'(?=[一-鿿　-〿＀-￯])', r'\1\\"', text)
    result = re.sub(r'([：:])"'
                    r'(?=[一-鿿])', r'\1\\"', result)
    result = re.sub(r'([。，、；！？）\)】\]、])"'
                    r'(?=[一-鿿])', r'\1\\"', result)
    return result

for f in sorted(target.glob("*_vlm_desc.md")):
    content = f.read_text(encoding="utf-8")
    if '"_parse_error": true' not in content:
        continue
    print(f"=== {f.name} ===")
    raw = re.search(r'## 原始 JSON\s*\n\s*```json\s*\n(.*?)\n```', content, re.DOTALL)
    if not raw:
        print("  FAIL: no raw JSON")
        continue
    saved = json.loads(raw.group(1))
    desc = saved.get("description", "")

    fence = re.search(r'```(?:json)?\s*\n?(.*?)```', desc, re.DOTALL)
    if not fence:
        print("  FAIL: no fence in desc")
        continue
    chunk = fence.group(1).strip()

    cleaned = _clean_chinese_quotes(chunk)
    print(f"  Original first 150: {repr(chunk[:150])}")
    print(f"  Cleaned first 150: {repr(cleaned[:150])}")

    # Try parsing
    import json5
    try:
        parsed = json5.loads(cleaned)
        print(f"  OK json5 → title={parsed.get('title','')} confidence={parsed.get('confidence','')}")
    except Exception as e:
        print(f"  json5 FAILED: {e}")
    try:
        parsed = json.loads(cleaned)
        print(f"  OK json → title={parsed.get('title','')} confidence={parsed.get('confidence','')}")
    except json.JSONDecodeError as e:
        lno = e.lineno
        col = e.colno
        line_text = cleaned.split('\n')[lno-1] if lno <= len(cleaned.split('\n')) else '?'
        print(f"  json FAILED line {lno} col {col}: {e}")
        print(f"  problem line: {repr(line_text[:120])}")
        # Show the problematic character
        start = max(0, col - 5)
        end = min(len(line_text), col + 5)
        print(f"  around col {col}: {repr(line_text[start:end])}")
    break
