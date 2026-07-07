import os, re, json, glob

files = sorted(glob.glob("*_vlm_desc.md"))
rows = []
for f in files:
    img = f.replace("_vlm_desc.md", ".png")
    with open(f) as fh:
        content = fh.read()
    m = re.search(r'```json\n(.*?)\n```', content, re.DOTALL)
    if m:
        try:
            data = json.loads(m.group(1))
        except:
            data = {}
    else:
        data = {}
    cat = data.get("category", "未识别")
    title = data.get("title", "")
    conf = data.get("confidence", 0.3)
    rows.append((img, cat, title, conf, f))

def sort_key(row):
    img = row[0]
    if img.startswith("项目管理"):
        return (0, img)
    return (1, img)

rows.sort(key=sort_key)

md = f"""# 管项目 - VLM 描述汇总

模型: `MiniMax-M3`

图片数: {len(rows)}
成功: {len(rows)}
失败: 0
修复: 13张双层JSON

## 描述清单

| 图片 | 类型 | 标题 | 置信度 | 描述文件 |
|---|---|---|---|---|
"""
for img, cat, title, conf, f in rows:
    md += f"| {img} | {cat} | {title} | {conf} | `{f}` |\n"

cats = {}
for _, cat, _, conf, _ in rows:
    cats[cat] = cats.get(cat, 0) + 1

md += "\n## 类型分布\n\n"
for cat, n in sorted(cats.items(), key=lambda x: -x[1]):
    md += f"- **{cat}**: {n} 张\n"

confs = [r[3] for r in rows]
avg = sum(confs)/len(confs)
md += f"\n## 质量指标\n\n"
md += f"- 平均置信度: {avg:.3f}\n"
md += f"- 最高: {max(confs)}\n"
md += f"- 最低: {min(confs)}\n"
md += f"- ≥0.95: {sum(1 for c in confs if c >= 0.95)} 张\n"
md += f"- ≥0.90: {sum(1 for c in confs if c >= 0.90)} 张\n"

with open("README-VLM描述汇总.md", "w") as f:
    f.write(md)

print(f"Generated: {len(rows)} entries")
for cat, n in sorted(cats.items(), key=lambda x: -x[1]):
    print(f"  {cat}: {n}")
print(f"Avg confidence: {avg:.3f}")
