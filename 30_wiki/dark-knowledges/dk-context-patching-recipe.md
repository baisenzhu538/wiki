---
id: dk-context-patching-recipe
title: 上下文补齐配方：内容质量不够时先补"价值观+方法论+素材"，不换模型
type: dk
status: pending_review
author: 老顽童
reviewed_by: pending
confidence: 0.88
trust_level: medium
language: zh-CN
created_at: 2026-08-19
updated_at: 2026-08-19
domain:
- knowledge-management
- ai-collaboration
aliases:
- 上下文补齐配方
- 内容不够先补上下文
- 价值观方法论素材三件套
- 楚门-AI知识管理探索营-口述
- 楚门-AI知识管理探索营-口述.txt
- AI知识库
tags:
- audience:manager
- scene:execution
- skill-level:advanced
source_person: 楚门
source_context: AI×知识管理探索营（2026-08-15 晚直播）——新年洞察救活 + 新手设计师补丁（L1918-1944、L2230-2238）
source_refs:
- 00_inbox/AI知识库/楚门-AI知识管理探索营-口述.txt
related:
- '[[dk-model-demystification]]'
- '[[case-new-year-insight-relay]]'
- '[[case-vibecoding-one-week-delivery]]'
- '[[framework-multi-agent-collab-chain-six]]'
- '[[dk-ai-builder-illusion]]'
- '[[framework-一堂-机会预判]]'
- '[[tool-agent-white-paper-five-elements]]'
- 'case-truman-ai-native-research-flow'
- 'tool-local-search-repo-datasource-engineering'
- 'framework-knowledge-naming-systems-comparison'
- '[[case-friend-circle-aigc-transformation]]'
- '[[concept-meta-skill-layering]]'
- '[[framework-ai-deliberate-practice-loop]]'
- '[[framework-fact-rule-insight]]'
- '[[tool-skill-packaging-eight-steps]]'
---
# 上下文补齐配方：内容质量不够时先补"价值观+方法论+素材"，不换模型

> **定位**：属于 [[dk-model-demystification]] 的操作篇——模型祛魅之后，质量不够时的第一反应是补上下文，不是换模型/换话术

## 原始表述

> 「因为我可能对业务相对稍微熟一点，可能审美稍微高了一点点……我又给他读了三个关键的关键文档。一个文档是关于一堂的价值观的介绍和审美愿景，因为这是魂儿。第二个我补了一轮，我对他没有想象，以及我这么多年我如果来作为洞察，我底层逻辑是什么？其实矛盾和自洽……我第三个我又让他去调研了几十个有流传度的金曲，然后我说无论如何你要塞一两个金句到所有洞察力。」（口述 L1918-1928）
> 「这个 session 是新的，但是我只要给他补两个上门，一个是这个项目的基本介绍，一个是设计开发。只要给他两个项目，他就能做出来专业的，相当于你可以用很短的时间，可以把一个新手设计师训练成一个能干这个活的设计师。」（L2236-2238）

## 使用场景

- AI 产出"浅、AI 味、没人味儿"（L1902）时——质量不够的第一反应
- 新开 session/新 Agent 加入项目，需要快速上手时
- 团队产出风格不统一，需要统一"魂"时

## 操作方法

1. **诊断缺什么**：产出没魂 → 缺价值观/愿景（魂）；产出不专业 → 缺方法论/底层逻辑；产出没味道 → 缺素材/金句
2. **补三件套**（楚门配方）：
   - ①价值观/审美愿景——"这是魂儿"（L1920）
   - ②方法论/底层逻辑——洞察=矛盾和自洽（L1924-1926）
   - ③素材库/金句——"塞一两个金句到所有洞察"（L1926-1928）
3. **轻量补丁**：新 Agent 只需两个上下文（项目介绍+设计规范）就能干活（L2236-2238）——不是每次都补全套
4. **补完再生成**：上下文补齐后再让 AI 重做（L1930-1934），补 3-4 个关键假设后"快看哭了"
5. **沉淀为文档**：价值观/方法论/素材都已在知识库——补上下文=指向文档，不是口述

## 适用边界

- 适用于**内容生成质量**问题；如果是事实错误/逻辑硬伤，先查方法（不是补上下文能救的）
- 三件套需要提前沉淀在知识库——没有"魂/方法论/素材"文档时，先补建
- 轻量补丁（2 个上下文）适合"会干活但不懂你"的新 Agent；深度补齐（三件套）适合"懂你"的长期 Agent

## 为什么值钱

- **质量瓶颈在上下文不在模型**：模型祛魅的实证——"Prompt 完备性优先级远高于模型"（L1764-1770）
- **可复用配方**：三件套不是玄学——价值观/方法论/素材是任何"有魂内容"的通用底盘
- **新手秒变专家**：两个上下文补丁=把新手设计师训练成能干活的（L2238）——能力复制成本趋零

## Critique

- **反驳**：上下文补得再多，模型笨还是不行？——模型差距真实存在但被高估；上下文的边际收益在大多数场景更高（L1752-1760）。
- **反驳**：三件套是从一堂角度总结的，别的领域适用吗？——结构通用（价值观/方法论/素材），内容按领域替换。
- **条件**：此 dk 前提=知识库已有沉淀；从零开始要先建"魂/方法论/素材"文档。
- **注意**：补上下文不是无限追加——补到"够用"就停（楚门补三个文档，不是三十个）。

## 与其他知识的关联

- `dk-model-demystification`：模型祛魅=本 dk 的理论前提（一刷 dk）
- `case-new-year-insight-relay`：三件套救活浅稿的完整案例
- `case-vibecoding-one-week-delivery`：五个核心文档=项目级上下文
- `framework-multi-agent-collab-chain-six`：补上下文=读写关系管理的核心动作
- `dk-ai-builder-illusion`：AI 基建≠内容质量（跨域）

- `framework-opportunity-foresight`：洞察=矛盾和自洽（跨域 yitang）
- `tool-agent-white-paper-five-elements`：白皮书五要素（#384 回链）
