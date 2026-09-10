---
id: diag_20260910_ouyangfeng-reviewcheck-blindspot-extract-truncation
title: "最小建议书：review-check 盲点节提取被内联 ### 代码 span 截断——「盲点无根因」假阴性，A 级被误压 B 级"
created_at: 2026-09-10（01:49 场 headless 复盘）
author: 欧阳锋
channel: "#460 最小建议书（三行）"
---

- 现象：`kdo-tools/review-check.py` L249 盲点节提取 `bs_end = content.find("##", bs_start + 1)` 会在盲点条目的内联代码处提前截断——ouyangfeng `daily-context/2026-09-10.md` 会话 1 盲点 1 引用了 `` `### ④ 存在性核查` ``，`##` 子串命中 → 提取区只剩首行片段，实测 `check_agent('ouyangfeng','2026-09-10')` 返回 blindspot_count=1 / why=False（文件实际两场次盲点 6 条、均含为什么/根因追问），failures=「盲点 1 条且追问不够」+「深度未过: blindspot_rooted」→ A 级被误判 B 级【实证：直跑 check_agent 输出 vs 文件实文对照】。
- 在哪发现：2026-09-10 01:49 场 headless 复盘保存自检（daily-context-save.py → 🟡 B级 📚检索有发现；核对失败明细与文件实际内容不符，双假设先疑内容后定位到检查器边界逻辑）。
- 建议方向（可选）：`"##"` 边界改为行首锚定（`re.search(r"^##\s", content[bs_start+10:], re.M)`）或提取前先剥离内联代码 span；与 #693（review-check 场次对账弱校验，同文件在改）可并单处理。
