import json, re, sys
from pathlib import Path

target = Path(r"C:\Users\Administrator\Desktop\wiki\00_inbox\战略专题\冉鹏PPT截图")

UNFIXABLE = [
    "111", "114", "125", "129", "134", "139", "149", "14", "158",
    "166", "167", "16", "184", "188", "190", "193", "195", "199",
    "208", "218", "222", "247", "249", "256", "25", "260", "264",
    "266", "290", "29", "30", "33", "39", "41", "45", "51", "53",
    "54", "58", "61", "63", "78", "86", "93", "98",
]

def _clean_chinese_quotes(text):
    result = re.sub(r'([一-鿿　-〿＀-￯])"'
                    r'(?=[一-鿿　-〿＀-￯])', r'\1\\"', text)
    result = re.sub(r'([：:])"'
                    r'(?=[一-鿿])', r'\1\\"', result)
    result = re.sub(r'([。，、；！？）\)】\]、])"'
                    r'(?=[一-鿿])', r'\1\\"', result)
    return result

for num in UNFIXABLE[:3]:
    for f in sorted(target.glob("*_vlm_desc.md")):
        if f"_{num}_" not in f.name:
            continue
        print(f"=== {f.name} ===")
        content = f.read_text(encoding="utf-8")
        raw = re.search(r'## 原始 JSON\s*\n\s*```json\s*\n(.*?)\n```', content, re.DOTALL)
        if not raw:
            print("  FAIL: no raw JSON section found")
            # Try to find what's around "原始 JSON"
            idx = content.find("原始 JSON")
            if idx > 0:
                print(f"  Content around 原始 JSON: {repr(content[idx:idx+300])}")
            break
        try:
            saved = json.loads(raw.group(1))
        except json.JSONDecodeError as e:
            print(f"  FAIL: outer json.loads failed: {e}")
            # Examine the raw text
            raw_text = raw.group(1)
            print(f"  raw text first 200: {repr(raw_text[:200])}")
            # Try to find the error location
            lno = e.lineno
            lines = raw_text.split('\n')
            if lno <= len(lines):
                print(f"  error line {lno}: {repr(lines[lno-1][:120])}")
            break
        if not saved.get("_parse_error"):
            print("  Not a parse error file (no _parse_error flag)")
            break
        desc = saved.get("description", "")
        if not desc:
            print("  FAIL: empty description")
            print(f"  saved keys: {list(saved.keys())}")
            print(f"  saved: {json.dumps(saved, ensure_ascii=False)[:300]}")
            break
        print(f"  desc length: {len(desc)}")
        print(f"  desc first 100: {repr(desc[:100])}")

        # Check for fence
        fence_match = re.search(r'```(?:json)?\s*\n?(.*?)```', desc, re.DOTALL)
        if not fence_match:
            print("  FAIL: no fence in desc")
            # Check if desc is just JSON without fence
            if desc.strip().startswith('{'):
                print("  desc IS JSON without fence, trying to parse...")
                cleaned = _clean_chinese_quotes(desc)
                import json5
                try:
                    parsed = json5.loads(cleaned)
                    print(f"  OK json5 → {parsed.get('title','')}")
                except Exception as e2:
                    print(f"  json5 failed: {e2}")
            else:
                print(f"  desc is not JSON either")
            break
        chunk = fence_match.group(1).strip()
        cleaned = _clean_chinese_quotes(chunk)
        print(f"  chunk first 100: {repr(chunk[:100])}")
        print(f"  cleaned first 100: {repr(cleaned[:100])}")

        import json5
        try:
            parsed = json5.loads(cleaned)
            print(f"  JSON5 OK → {parsed.get('title','')}")
        except Exception as e2:
            print(f"  JSON5 failed: {e2}")
        try:
            parsed = json.loads(cleaned)
            print(f"  JSON OK → {parsed.get('title','')}")
        except json.JSONDecodeError as e2:
            lno = e2.lineno
            lines_list = cleaned.split('\n')
            if lno <= len(lines_list):
                print(f"  JSON fail line {lno}: {repr(lines_list[lno-1][:120])}")
        break
