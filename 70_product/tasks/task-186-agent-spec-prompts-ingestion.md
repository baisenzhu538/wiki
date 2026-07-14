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
#182 实勘发现：`.agent/prompts/` 有 **28 张** tool-agent-spec-yitang-* 卡，`30_wiki/tools/` 有 8 张正式卡——**20 张 agent-spec 卡只有运行时文件、未入知识层**（黑户）。分类：
- **销售域 6 张**：three-second-opening-scripts / payment-collection-risk / daily-weekly-meeting-host / sales-toolkit-gap / incentive-design / lead-funnel-health
- **kernel 系列 7 张**：kernel-yitang-Y-model / kernel-yitang-business-formula / kernel-yitang-five-step / kernel-yitang-decision-science / kernel-yitang-conversion-rate / kernel-yitang-product-kernel / kernel-yitang-personal-os
- **产品/设计/项目管理 7 张**：ability-migration-diagnosis / aesthetic-radar-modeling / beautiful-work-imagination / card-dealing-guide / project-background-analysis / scenario-walkthrough / user-perspective-training

王语嫣裁定（7-13 修正）：related 是知识层关系，不在 prompts 文件织网——20 张全部入库转正，一次清掉黑户。

## 工作清单
1. **入库**：20 张 prompts 文件→`30_wiki/tools/` 正式卡（内容不变，frontmatter 按知识层规范补全：id/domain/tags/related/source_refs）
2. **销售域 6 张**：入库时按 #182 映射表统一加 D 域回链
3. **kernel 系列 7 张**：related 按内核域接（五步法/业务公式/决策科学/转化率/产品内核/personal-os 等）
4. **产品/设计/项目管理 7 张**：related 按所属域接（产品内核/美商/项目管理等）；不确定的标 🟡 王语嫣裁定
5. **prompts 原件不动**（运行时文件保持原位，正式卡 source_refs 指向 prompts 路径建立溯源）
6. digest/index 登记

## 验收口径
- 20 张正式卡落地，pre-submit 全 PASS，lint 无新增
- 销售域 6 张 D 域回链与 #182 映射表一致
- 扫窗申报=20 新卡+digest/index 改动清单

## 流程
流程A 直通。门禁：`kdo pre-submit -f` 批量过。
