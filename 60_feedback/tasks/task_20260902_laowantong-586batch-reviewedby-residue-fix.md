---
id: task_20260902_laowantong-586batch-reviewedby-residue-fix
title: null
seq: 613
status: in_progress
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 欧阳锋建议书 prop_20260902_ouyangfeng-muse-reviewed-by-pending-residue（#611
  终审发现）09-02 王语嫣裁定立项
reviewer: 欧阳锋
instance: laowantong-kimi
updated_at: '2026-09-02T01:12:22.905698+00:00'
---

# #613 #586 批元数据残留排查补齐（老顽童）

## 背景

#611 终审发现 `framework-muse-ai-full-map-v1` frontmatter `status: reviewed` 但 `reviewed_by: pending`（#586 返工重提批遗留）。E018 家族：status=reviewed 必须有真实终审记录。这些卡确实过了终审（#586 PASS A- 在案），是元数据没跟上。

## 任务

1. **排查**（只读）：扫 30_wiki 全库 `status: reviewed` 且 `reviewed_by: pending`（或缺 reviewed_by/review_date）的卡，输出清单（yaml.safe_load 解析，禁正则扫 frontmatter——E017）
2. **补齐**：对能对应到真实终审记录的卡（#586 批及他批有 commit/任务单佐证的），补 reviewed_by: 欧阳锋 + review_date=实际终审日期（git log 取证）；对找不到终审佐证的卡，**不改状态**，单列清单报王语嫣
3. 只动 frontmatter 三字段（reviewed_by/review_date/grade 若有实证），不动正文

## 交付

- 排查清单 + 补齐 diff（每卡附终审佐证 commit）+ 无佐证卡单列清单
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 613 附清单路径）
