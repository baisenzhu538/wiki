---
id: task_20260704_laowantong-dual-triangle-vlm-case-enrichment
type: task
status: reviewed
assignee: claude
reviewer: 欧阳锋
priority: P1
estimated_cards: 10
created_at: 2026-07-04
updated_at: '2026-07-04T15:01:23.718599+00:00'
reviewed_by: 欧阳锋
review_date: '2026-07-04'
source_refs:
  - 00_inbox/人机协作双三角/_processed/vlm_summary.json
  - 00_inbox/人机协作双三角/_processed/一堂双三角-数字化营销提效十倍_vlm.md
  - 00_inbox/人机协作双三角/_processed/一堂双三角-IP选题智能体挑战交付上限_vlm.md
  - 00_inbox/人机协作双三角/_processed/一堂双三角-图书分析AI工具_vlm.md
  - 00_inbox/人机协作双三角/_processed/一堂双三角-AI企业经营数据分析_vlm.md
  - 00_inbox/人机协作双三角/_processed/一堂双三角-人生红点教练parther探索_vlm.md
  - 00_inbox/人机协作双三角/_processed/一堂双三角-龙虾训练实验_vlm.md
  - 00_inbox/人机协作双三角/_processed/一堂双三角-教育新官网制作_vlm.md
related:
  - '[[concept-yihang-dual-triangle-core]]'
  - '[[framework-yihang-dual-triangle-ai-landing-five-steps]]'
  - '[[framework-yihang-dual-triangle-weapon-library]]'
  - '[[tool-yihang-dual-triangle-canvas]]'
---
# 双三角 VLM 案例批量 enrichment

## 背景

洪七公已完成 115 个双三角域案例的 VLM 提取（OCR + 六要素映射），但之前全部停在 `00_inbox/_processed/`，未入库。黄药师已批量 ingest 37 张 draft case 卡到 `30_wiki/cases/case-yihang-dual-triangle-*.md`，索引已更新，Agent 现在可以搜到。

## 任务

从 37 张 draft 卡中挑选 VLM 分析质量最高的 **10 张**，enrich 为正式 case 卡：

1. 补充 frontmatter 缺失字段（confidence、trust_level、source_person、reviewed_by）
2. 补充双三角六要素标注（VLM 已有初步映射，老顽童深挖确认）
3. 补 Critique（至少 1 个外部攻击者）
4. 补 Action Triggers
5. `kdo pre-submit` 通过

## 验收

- 10 张卡 status: enriched，pre-submit PASS
- 每张卡六要素标注完整
- 欧阳锋抽检 3 张

## 备注

- 其余 27 张保持 draft，后续按需精修
- 来源：洪七公 VLM 提取，已在 `30_wiki/cases/case-yihang-dual-triangle-*`
