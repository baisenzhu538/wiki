# -*- coding: utf-8 -*-
"""欧阳锋终审交叉印证：mnemo_store 库清洁度复检（审而不改——只读）"""
import sqlite3, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
db = sqlite3.connect("60_feedback/diagnosis/assets_20260831_mnemosyne-dogfood/mnemo_store/memory.db")
rows = db.execute("SELECT content FROM memories").fetchall()
print("总记录数:", len(rows))
ids = []
for (c,) in rows:
    fm = c.split("---")[1] if c.startswith("---") else ""
    m = re.search(r"^id:\s*(.+?)\s*$", fm, re.M)
    if m:
        ids.append(m.group(1))
print("可提取id:", len(ids), "| 唯一:", len(set(ids)), "| 重复:", len(ids) - len(set(ids)))
print("projects:", db.execute("SELECT DISTINCT project FROM memories").fetchall())
