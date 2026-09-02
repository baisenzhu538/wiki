# -*- coding: utf-8 -*-
"""#613 排查：30_wiki 全库 status=reviewed 但 reviewed_by ∈ {pending, 待审, 缺失} 或 review_date 缺失的卡。
yaml.safe_load 解析 frontmatter，禁正则提取字段值（E017）。
口径与排查补齐报告-613.md §0 文字口径逐字对齐（#613 终审 P1-1 返工点）。"""
import os, sys, json, io
import yaml

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = r"C:\Users\Administrator\Desktop\wiki\30_wiki"

def split_frontmatter(text):
    # 只按行切分定位 frontmatter 边界，字段解析交给 yaml.safe_load
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i])
    return None

hits = []
errors = []
n_files = 0
for dirpath, _dirs, files in os.walk(ROOT):
    for fn in files:
        if not fn.endswith(".md"):
            continue
        n_files += 1
        path = os.path.join(dirpath, fn)
        try:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
        except Exception as e:
            errors.append((path, f"read: {e}"))
            continue
        fm_text = split_frontmatter(text)
        if fm_text is None:
            continue
        try:
            fm = yaml.safe_load(fm_text)
        except Exception as e:
            errors.append((path, f"yaml: {e}"))
            continue
        if not isinstance(fm, dict):
            continue
        status = fm.get("status")
        if status != "reviewed":
            continue
        reviewed_by = fm.get("reviewed_by")
        review_date = fm.get("review_date")
        rb_pending = reviewed_by is None or (isinstance(reviewed_by, str) and (reviewed_by.strip().lower() in ("pending", "") or reviewed_by.strip() == "待审"))
        rd_missing = review_date is None or (isinstance(review_date, str) and review_date.strip().lower() in ("pending", ""))
        if rb_pending or rd_missing:
            hits.append({
                "path": os.path.relpath(path, r"C:\Users\Administrator\Desktop\wiki"),
                "id": fm.get("id"),
                "type": fm.get("type"),
                "author": fm.get("author"),
                "status": status,
                "reviewed_by": reviewed_by if reviewed_by is not None else "<missing>",
                "review_date": str(review_date) if review_date is not None else "<missing>",
                "updated_at": str(fm.get("updated_at")),
            })

print(f"扫描文件数: {n_files}")
print(f"YAML/读取错误数: {len(errors)}")
for p, e in errors[:20]:
    print(f"  ERROR {p}: {e}")
print(f"命中卡数: {len(hits)}")
for h in hits:
    print(f"- {h['path']} | id={h['id']} | type={h['type']} | author={h['author']} | reviewed_by={h['reviewed_by']} | review_date={h['review_date']} | updated_at={h['updated_at']}")

OUT = r"C:\Users\Administrator\Desktop\wiki\60_feedback\tasks\task_20260902_laowantong-586batch-reviewedby-residue-fix\scan-result.json"
with open(OUT, "w", encoding="utf-8") as f:
    json.dump({"scanned": n_files, "errors": errors, "hits": hits}, f, ensure_ascii=False, indent=2)
print("JSON 落盘: 60_feedback/tasks/task_20260902_laowantong-586batch-reviewedby-residue-fix/scan-result.json")
