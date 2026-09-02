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


## 执行报告（2026-09-02 老顽童 kimi 实例）

**交付物**：`60_feedback/tasks/task_20260902_laowantong-586batch-reviewedby-residue-fix/` 五件——排查补齐报告-613.md（排查清单+补齐清单+无佐证清单）/ scan-result.json / fix-result.json / scan-script.py / fix-script.py（可独立复跑）；23 张卡 frontmatter 修复（同 commit 入仓）。

**完成内容**：扫 30_wiki 全库 2949 文件（yaml.safe_load 解析，禁正则——E017），命中 status=reviewed 且 reviewed_by 残留 30 张（pending 17 + 待审 13）。23 张有真实终审佐证已补齐：#586 批 12 张（reviewed_by→欧阳锋 + review_date=2026-09-01 + grade=A-，佐证=任务单返工复审 PASS A- 2026-09-01 07:45 + 逐卡 #586 commit）；06-28 批 3 张（仅补 reviewed_by，review_date 2026-06-28 已在卡，佐证=review_20260628_ouyangfeng-channel-growth §已执行动作 + task_20260627 终审 11 卡全过）；待审批 8 张（reviewed_by→欧阳锋 + review_date + grade=A-，佐证=task_20260815 spin/candy 两单 PASS A- 2026-08-16 + task_20260822 fengqingyang PASS/A- 2026-08-22）。只动 frontmatter 三字段，未动正文。

**验证**：复扫 pending 17→2 / 待审 13→5（余 7=无佐证清单）；git diff 23 文件每文件仅 +3/-1 或 +1/-1 行；23/23 写后 yaml.safe_load 复解析断言通过；pre-submit 23/23 PASS（两批，WARNING 19+17 条均 #542 提示制不拦截级）；kdo index --incremental +0 ~23 -0（total 4177）。

**边界**：7 张无终审佐证卡（dk-p15-unverified / high-density-composite-compilation-strategy / 4 张 07-08 产品内核 case / tool-kdo-wechat-serendipity-collect）不改状态，单列报王语嫣裁定；500 张历史缺 review_date（reviewed_by 已是真人）不在本单范围，需另立项；2 个 YAML 解析错误文件如实记录未修。

**需要谁动作**：欧阳锋终审本单（重点复核 23 卡佐证映射与 grade=A- 标注口径）；王语嫣裁定 7 张无佐证卡处置方向（补登记 or 降回 enriched 重审）。
