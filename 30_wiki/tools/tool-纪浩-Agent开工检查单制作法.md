---
id: tool-纪浩-Agent开工检查单制作法
title: 技能：Agent开工检查单制作法
type: tool
status: reviewed
domain:
- src_unknown
- src_unknown
source_person: 纪浩
source_context: AI俱乐部-人和AI协作-纪浩-五层结构-图片01
source_refs:
- 10_raw/sources/src_20260609_8c00cb42-ocr-ai俱乐部-人和ai协作-纪浩-五层结构-图片01.md
author: 纪浩
reviewed_by: 欧阳锋
created_at: '2026-06-15'
updated_at: '2026-06-17'
confidence: 0.75
trust_level: medium
related:
- '[[yt-tool-peas-agent-analysis]]'
- '[[tool-agent-research-pipeline]]'
- '[[case-ai-agent-milestone-design]]'
- '[[tool-agent-crawl4ai]]'
- '[[agent-external-brain-design]]'
- '[[dk-demand-pitfall-travel-agent]]'
- '[[dk-skill-market-agent-self-install]]'
- '[[agent-ecosystem-design]]'
- '[[tool-demand-agent-signal-substitute]]'
- '[[tool-Truman-多Agent通信协作方案]]'
- '[[kdo_product_design_agent_final]]'
- '[[tool-agent-firecrawl]]'
- '[[tinyfish-agentic-web-infrastructure]]'
- '[[tool-纪浩-Agent技能市场设计法]]'
- '[[tool-纪浩-Problem与Question区分法]]'
diagnostic_signals:
- lens: 执行失控
  follow_up: 先和AI把任务做一遍，记录问题和决策点。把坑提前暴露，生成检查单
- lens: 重复交代
  follow_up: 把历史经验沉淀为检查单，开工前按单执行。隐性经验显性化
- lens: 审核遗漏
  follow_up: 检查单必须包含：输入验证、边界条件、异常处理、输出格式。逐项确认
- lens: 检查单臃肿
  follow_up: 检查单控制在10项以内，按优先级排序。关键项必须执行，次要项可选
- lens: 经验空白
  follow_up: 先用Do-first法跑一遍任务，记录问题。没有经验就创造经验，不能跳过第一步
tags:
- audience:executor
- scene:execution
- skill-level:intermediate
---

# 技能：Agent开工检查单制作法

- src_unknown

## 原始表述

Agent开工检查单制作法是纪浩在AI协作方法论分享中提出的具体方法，用于Agent开工检查单制作法。

## 操作步骤

1. 先和AI把任务做一遍
2. 记录过程中出现的问题、决策点和风险
3. 把问题清单丢给AI
4. 让AI生成一份开工前检查单
5. 人工审核检查单，补充自己的判断
6. 在真实任务启动前按检查单执行

## Constraints & Boundaries

### 适用边界

| 边界 | 说明 |
|:-----|:-----|
| ✅ 适合 | 准备让Agent协作完成真实任务，需要降低执行风险 |
| ✅ 适合 | Agent执行失控频繁出错，需要提升可控性 |
| ✅ 适合 | 需要把隐性经验显性化，沉淀为可复用检查单 |
| ✅ 适合 | 相似任务重复启动，需要标准化前置检查 |
| ❌ 不适合 | 任务过于简单无需检查 → 检查单成本超过收益 |
| ❌ 不适合 | 没有历史经验可参考 → 先用Do-first法跑一遍 |
| ❌ 不适合 | 完全探索性任务 → 检查单会限制探索空间 |
| ❌ 不适合 | 紧急任务时间不足 → 事后补检查单 |

#| 模式 | 症状 | 修复 |
|:-----|:-----|:-----|
| **执行失控** | Agent执行任务时频繁出错，执行失控 | 先和AI把任务做一遍，记录问题和决策点。把坑提前暴露，生成检查单 |
| **重复交代** | 每次启动相似任务都要重新交代注意事项，效率低下 | 把历史经验沉淀为检查单，开工前按单执行。隐性经验显性化 |
| **审核遗漏** | 人工审核检查单时遗漏关键风险点 | 检查单必须包含：输入验证、边界条件、异常处理、输出格式。逐项确认 |
| **检查单臃肿** | 检查单过于冗长，Agent执行时跳过或忽略 | 检查单控制在10项以内，按优先级排序。关键项必须执行，次要项可选 |
| **经验空白** | 没有历史经验可参考，无法制作检查单 | 先用Do-first法跑一遍任务，记录问题。没有经验就创造经验，不能跳过第一步 |
| **检查单僵化** | 检查单不更新，新出现的问题不在检查单中 | 每次任务后Review检查单，补充新发现的问题。检查单是活的文档 |
| **形式合规** | 按检查单执行但结果仍出错，检查单流于形式 | 检查单必须包含验证步骤，不是勾选就完。关键项执行后必须验证结果 |
| **过度依赖** | 有检查单就不思考，机械执行 | 检查单是辅助不是替代。保留人工判断空间，检查单无法覆盖所有场景 |

## 为什么有效

通过先跑一遍再沉淀检查单，把执行中的坑提前暴露，提升Agent协作的可控性。隐性经验显性化，降低每次启动的认知负担。

## 关联技能

- src_unknown
- src_unknown
- src_unknown

## 来源

- src_unknown

## Feedback Path

- src_unknown

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

- **具体假设**：该工具假设结构化方法论能提升效果，但方法论的有效性取决于执行者的判断力和场景适配——没有判断力的执行只是'走流程'，不等于'做好事'。
- **边界**：在全新领域或快速变化的环境中，已有数据和经验可能完全失效——工具的有效性高度依赖场景的稳定性。
- **前提**：该工具的前提是使用者能正确理解和执行工具的规则，但执行者的认知偏差和经验限制会影响工具的实际效果。

**Peter Drucker**（管理学大师）会质疑：工具的价值不在于"有没有"，而在于"用得好不好"。任何工具都是"能力放大器"——如果使用者的判断力不足，工具只会放大错误。真正的风险不是"缺少工具"，而是"有了工具后产生的虚假安全感"——让你以为自己已经覆盖了所有可能性，实际上只是走完了流程。
