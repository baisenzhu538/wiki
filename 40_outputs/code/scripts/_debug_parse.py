import re, json
from pathlib import Path

target = Path(r"C:\Users\Administrator\Desktop\wiki\00_inbox\战略专题\冉鹏PPT截图")

for f in sorted(target.glob("*_vlm_desc.md")):
    if "_111_" not in f.name:
        continue
    content = f.read_text(encoding="utf-8")
    idx = content.find("## 原始 JSON")
    after = content[idx:]

    FENCE_OPEN = "```"
    # Build regex: ## 原始 JSON \s* \n \s* ```json \s* \n (.*?) \n ```
    pattern = (
        r"## 原始 JSON\s*\n\s*"
        + re.escape(FENCE_OPEN) + r"json\s*\n"
        r"((?s:.*?))"
        r"\n" + re.escape(FENCE_OPEN)
    )
    print("Pattern:", repr(pattern))
    m = re.search(pattern, after)
    print("Match:", "YES" if m else "NO")
    if m:
        raw = m.group(1)
        print("Length:", len(raw))
        try:
            outer = json.loads(raw)
            print("json.loads OK, _parse_error:", outer.get("_parse_error"))
        except json.JSONDecodeError as e:
            print(f"json.loads FAILED: {e}")
    else:
        # Show what comes after 原始 JSON
        print("Content after 原始 JSON:", repr(after[:200]))
    break
