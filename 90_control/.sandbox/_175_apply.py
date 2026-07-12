"""#175 apply all fixes"""
from pathlib import Path
VAULT = Path(__file__).resolve().parent.parent.parent

# 1. 6 orphans -> domain digest
digest = VAULT / "30_wiki/domains/business-formula-domain-digest.md"
d = digest.read_text(encoding="utf-8", errors="replace")
orphans = ["case-toc-ecommerce-formula-misjudgment","case-private-domain-ecommerce-formula",
    "case-saas-renewal-formula","case-dental-clinic-formula","case-gym-membership-formula",
    "case-offline-catering-formula"]
lines = d.splitlines()
fm_end = 0
for i,l in enumerate(lines):
    if l.strip() == "---" and i > 0: fm_end = i; break
last_rel = -1
for i in range(fm_end):
    if lines[i].strip().startswith("-") and "[[" in lines[i]: last_rel = i
added = 0
for o in orphans:
    if o in d: continue
    lines.insert(last_rel + 1, "  - '[[%s]]'" % o)
    last_rel += 1; added += 1
if added:
    digest.write_text("\n".join(lines), encoding="utf-8")
    print("Orphans -> digest: %d added" % added)

# 2. 6 orphans -> index.md (add links)
idx = VAULT / "30_wiki/index.md"
i = idx.read_text(encoding="utf-8", errors="replace")
for o in orphans:
    if o in i: continue
    i += "\n- [[cases/%s|%s]] — source pending_archive" % (o, o)
idx.write_text(i, encoding="utf-8")
print("Orphans -> index: done")

# 3. Coke-spill full body fix
coke = VAULT / "30_wiki/cases/case-yitang-coke-spill-compensation.md"
c = coke.read_text(encoding="utf-8", errors="replace")
c = c.replace("ROI/Y模型", "ROI模型（Y模型推导产物）").replace("ROI/Y 模型", "ROI模型（Y模型推导产物）")
coke.write_text(c, encoding="utf-8")

# Index files
for fname in ["30_wiki/index.md", "30_wiki/concept-card-index-latest.md"]:
    f = VAULT / fname
    c = f.read_text(encoding="utf-8", errors="replace")
    c = c.replace("ROI/Y模型", "ROI模型（Y模型推导产物）")
    f.write_text(c, encoding="utf-8")
print("ROI/Y fix: done")

# 4. Digest归属: check and fix双目标法/三类目标
d2 = digest.read_text(encoding="utf-8", errors="replace")
# Already in管理篇 row? Check
if "双目标法" in d2 and "三类目标" in d2:
    print("Digest归属: 双目标法/三类目标 found, need manual check")
else:
    print("Digest归属: 条目不存在, skip")

# 5. 马拉松双口径 - need to add note to marathon case card
marathon = VAULT / "30_wiki/cases/case-yitang-marathon-ten-seasons.md"
m = marathon.read_text(encoding="utf-8", errors="replace")
note = "\n> **裁定 #1（王语嫣·2026-07-12）**：马拉松切片维度存在双口径——核心6-7维（管理篇L2188）与扩展10维（参数篇L1756-1788）。两口径详略差异非矛盾，本卡以核心6-7维为主，扩展10维见参数篇。\n"
if "双口径" not in m:
    # Insert after first paragraph
    first_para_end = m.find("\n\n", m.find("# "))
    m = m[:first_para_end+2] + note + m[first_para_end+2:]
    marathon.write_text(m, encoding="utf-8")
    print("Marathon双口径: added")
else:
    print("Marathon双口径: already present")

# 6. dk伪因果卡补术语映射
dk_false = VAULT / "30_wiki/dark-knowledges/dk-yitang-business-formula-plus-times-trap.md"
try:
    dk = dk_false.read_text(encoding="utf-8", errors="replace")
    mapping = "\n> **术语映射（裁定 #3·王语嫣·2026-07-12）**：课程原话「因果倒置/共同因/筛选效应」≈ 学术界「自我选择偏差/中间变量」。另「因的因」为第三面具候选。\n"
    if "术语映射" not in dk:
        dk = dk.replace("> **一句话**", mapping + "> **一句话**")
        dk_false.write_text(dk, encoding="utf-8")
        print("DK伪因果术语映射: added")
    else:
        print("DK伪因果术语映射: already present")
except:
    print("DK伪因果: file not found - skip")

# 7. concept-一堂-相关不等于因果 补口径声明
try:
    related_card = VAULT / "30_wiki/concepts/concept-一堂-相关不等于因果.md"
    rc = related_card.read_text(encoding="utf-8", errors="replace")
    statement = "\n> **口径声明（裁定 #4·王语嫣·2026-07-12）**：课程口径——「因果=更强的单向相关，两者不互斥」（逻辑关系篇L2270-2280）。卡名「相关不等于因果」强调不可混淆，与课程口径的兼容性在于：相关是因果的必要条件，但仅凭相关不能断言因果。\n"
    if "口径声明" not in rc:
        rc = rc.replace("> **一句话**", statement + "> **一句话**")
        related_card.write_text(rc, encoding="utf-8")
        print("因果口径声明: added")
    else:
        print("因果口径声明: already present")
except:
    print("因果口径: file not found - skip")

print("\n#175 batch apply complete.")
