import json, re
from pathlib import Path

target = Path(r"C:\Users\Administrator\Desktop\wiki\00_inbox\战略专题\冉鹏PPT截图")
files = sorted(target.glob("*_vlm_desc.md"))

errors = []
low_conf = []
bad_structure = []

for f in files:
    content = f.read_text(encoding="utf-8")

    # 检查1：无 _parse_error
    if "_parse_error" in content:
        errors.append(f.name)
        continue

    # 检查2：置信度提取
    m = re.search(r'- \*\*置信度\*\*: ([0-9.]+)', content)
    conf = float(m.group(1)) if m else None
    if conf is None:
        bad_structure.append(f"{f.name}: no confidence field")
        continue
    if conf < 0.5:
        low_conf.append((f.name, conf))

    # 检查3：必要的结构化章节都存在
    required = ["## 结构化描述", "### 描述", "### 关键元素", "### 标签", "### 适用场景", "## 原始 JSON"]
    missing = [s for s in required if s not in content]
    if missing:
        bad_structure.append(f"{f.name}: missing {missing}")

    # 检查4：原始 JSON 段包含合法 JSON
    raw = re.search(r'## 原始 JSON\s*\n\s*```json\s*\n(.*?)\n```', content, re.DOTALL)
    if not raw:
        bad_structure.append(f"{f.name}: no 原始 JSON section")
        continue
    try:
        parsed = json.loads(raw.group(1))
        if parsed.get("_parse_error"):
            errors.append(f"{f.name}: _parse_error still true in raw JSON")
        if not parsed.get("category"):
            bad_structure.append(f"{f.name}: empty category")
    except json.JSONDecodeError as e:
        bad_structure.append(f"{f.name}: raw JSON parse failed: {e}")

print(f"总文件: {len(files)}")
print(f"含 _parse_error: {len(errors)}")
print(f"低置信度 (<0.5): {len(low_conf)}")
print(f"结构问题: {len(bad_structure)}")
print()

if errors:
    print("=== _parse_error 残留 ===")
    for e in errors[:10]:
        print(f"  {e}")

if low_conf:
    print("\n=== 低置信度 (<0.5) ===")
    for name, conf in sorted(low_conf, key=lambda x: x[1])[:15]:
        print(f"  {conf}: {name}")

if bad_structure:
    print("\n=== 结构问题 ===")
    for b in bad_structure[:10]:
        print(f"  {b}")

if not errors and not bad_structure:
    print("✅ 全部通过")
    if low_conf:
        print(f"⚠️  {len(low_conf)} 个文件置信度 <0.5（可能是过渡页/练习页/目录页，属正常现象）")
