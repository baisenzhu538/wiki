---
id: task_20260713_wangyuyan-agent-spec-prompts-ingestion
assignee: kimi
status: in_progress
updated_at: '2026-07-14T18:36:52.298406+00:00'
---

# Task #186 · agent-spec 卡入知识层（.agent/prompts → 30_wiki/tools）

- **状态**：queued
- **负责人**：老顽童
- **优先级**：P2
- **依赖**：#182 reviewed 后顺领（回链在入库时统一加）

## 背景
#182 实勘发现：`.agent/prompts/` 有 22 张 tool-agent-spec-yitang-* 卡，`30_wiki/tools/` 只有 8 张正式卡——**14 张 agent-spec 卡只有运行时文件、未入知识层**（黑户）。其中销售域 6 张（three-second-opening-scripts / payment-collection-risk / daily-weekly-meeting-host / sales-toolkit-gap / incentive-design / lead-funnel-health），其余 8 张属其他域（kernel-* 系列 / Y-model-coach / card-dealing-guide / aesthetic-radar-modeling / beautiful-work-imagination / project-background-analysis / scenario-walkthrough / user-perspective-training / ability-migration-diagnosis 等，以实勘为准）。

王语嫣裁定（7-13）：related 是知识层关系，不在 prompts 文件织网——先入库再回链。

## 工作清单
1. **入库**：14 张 prompts 文件→`30_wiki/tools/` 正式卡（内容不变，frontmatter 按知识层规范补全：id/domain/tags/related/source_refs）
2. **销售域 6 张**：入库时按 #182 映射表统一加 D 域回链（与 #182 同标准）
3. **其他域 8 张**：related 按所属域接（kernel 系列→五步法/产品内核域，Y-model-coach→Y 模型域等），不确定的标 🟡 王语嫣裁定
4. **prompts 原件不动**（运行时文件保持原位，正式卡 source_refs 指向 prompts 路径建立溯源）
5. digest/index 登记

## 验收口径
- 14 张正式卡落地，pre-submit 全 PASS，lint 无新增
- 销售域 6 张 D 域回链与 #182 映射表一致
- 扫窗申报=14 新卡+digest/index 改动清单

## 流程
流程A 直通。门禁：`kdo pre-submit -f` 批量过。
