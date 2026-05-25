import os, re, sys

# Force UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

print("=== y-model ===")
path = "30_wiki/concepts/yt-decision-y-model.md"
content = open(path, "r", encoding="utf-8").read()
body = content.split("---", 2)[2] if content.startswith("---") else content

print("Has ## Constraints & Boundaries:", "## Constraints & Boundaries" in body)
print("Has ## Critique:", "## Critique" in body)
print("Has ### 外部攻击:", "### 外部攻击" in body)
print("Has ### 内部局限:", "### 内部局限" in body)
attacks = re.findall(r"#### (.+)", body)
for a in attacks:
    print("  Attack:", a)

print()
print("=== Batch 4 - 8 cards ===")

batch8 = [
    "ocr-一堂-地图-个人地图", "ocr-一堂-地图-创业地图", "ocr-一堂-地图-管理地图",
    "ocr-一堂进步大地图", "ocr-一堂个人地图高潜力成长者修炼全景图",
    "ocr-一堂泛产品设计-十年修炼爬山地图", "ocr-一堂泛产品设计36计-全套地图",
    "ocr-萃取总结",
]

kw_critique = ["阅读路径", "空间层级", "视觉", "F形", "Z形", "箭头", "模块", "象限", "布局", "并列", "递进"]
kw_oq = ["阅读路径", "空间层级", "视觉", "F形", "Z形", "箭头", "模块", "象限", "布局", "并列", "递进"]

for name in batch8:
    path = "30_wiki/concepts/" + name + ".md"
    if not os.path.exists(path):
        print("\n" + name + ": NOT FOUND")
        continue
    content = open(path, "r", encoding="utf-8", errors="replace").read()
    body = content.split("---", 2)[2] if content.startswith("---") else content
    attacks = re.findall(r"#### (.+)", body)
    short_atk = [a.split("—")[0].split(" -")[0].split("—")[0][:30] for a in attacks]
    has_va = "## Visual Analysis" in body
    has_crit = "## Critique" in body
    has_syn = "## Synthesis" in body
    has_oq = "## Open Questions" in body
    has_new = any(x in content for x in ["Bowker", "Langlois", "Dewey", "Schön", "Sontag", "Schon"])

    print()
    print(name)
    print("  VA={} Crit={} Syn={} OQ={} HasNewAttacker={}".format(has_va, has_crit, has_syn, has_oq, has_new))
    print("  Attackers:", short_atk)

    # Check VA refs in Critique
    crit_sec = re.search(r"## Critique(.*?)(?=^## |\Z)", body, re.DOTALL | re.MULTILINE)
    if crit_sec:
        ct = crit_sec.group(1)
        refs = [kw for kw in kw_critique if kw in ct]
        print("  VA-refs in Critique:", refs)

    # Check VA refs in Open Questions
    oq_sec = re.search(r"## Open Questions(.*?)(?=^## |\Z)", body, re.DOTALL | re.MULTILINE)
    if oq_sec:
        refs = [kw for kw in kw_oq if kw in oq_sec.group(1)]
        print("  VA-refs in Open Questions:", refs)

    # Print the full Open Questions
    if oq_sec:
        text = oq_sec.group(1).strip()
        lines = [l.strip() for l in text.split("\n") if l.strip()]
        for l in lines[:5]:
            print("    OQ:", l[:80])
