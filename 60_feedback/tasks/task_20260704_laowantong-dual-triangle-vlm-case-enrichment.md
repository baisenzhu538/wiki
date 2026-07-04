---
id: task_20260704_laowantong-dual-triangle-vlm-case-enrichment
type: task
status: in_progress
assignee: claude
reviewer: 欧阳锋
priority: P1
created_at: 2026-07-04
updated_at: '2026-07-04T14:16:07.714052+00:00'
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
