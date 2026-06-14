---
id: dk-c1-cjk-regex-silent-fail
title: "C-1：enrich 中文内容不能用 CLI regex→0 pages enriched 静默失败"
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
  - master
source_person: Builder
source_context: 2026-05-03
source_refs:
  - 20_memory/corrections.md#C-1
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - dk-c10-batch-tool-no-dry-run
  - master-ai-info-literacy
pipeline:
  - confidence-draft
  - confidence-source-cited
author: legacy
reviewed_by: pending
confidence: 0.7
trust_level: low
---

# C-1：enrich 中文内容不能用 CLI regex→0 pages enriched 静默失败

## 原始表述

> `kdo enrich` 对中文页面返回 0 pages enriched，但静默成功，无错误信息。
> 
> 根因：`kdo/extractors.py` 的 regex 提取器三个缺陷：
> 1. `\b` 单词边界不识别中文字符
> 2. keywords（tutorial/article/script）纯英文
> 3. 长度阈值不适合 CJK 内容
> 
> 修正：中文内容不调 `kdo enrich`，走 Agent 三步编译法（浓缩→质疑→对标）。
> 
> ✅ 已修复 (2026-05-05)：kdo enrich 现自动检测 LLMConfig，配置后自动走三步编译（浓缩→质疑→对标），无需手动 --llm flag。中文内容直接受益。

## 使用场景

- 你准备用 `kdo enrich` 对一批 wiki 页面做自动内容增强，但其中包含中文内容
- 你刚写完一张中文概念卡，准备跑 `kdo enrich --all` 批量提升卡片质量
- 你审查 `kdo enrich` 的输出日志，看到 "0 pages enriched" 但 exit code 为 0，需要判断这是真无事还是假成功
- 你在为 KDO CLI 编写新的提取器/正则规则，需要确认它是否对 CJK 字符友好

## 操作方法

1. **识别内容语言**：运行 enrich 前，先抽检待处理页面，确认是否包含中文字符（CJK）
2. **若含中文，禁止走 CLI regex 模式**：
   - 未配置 LLMConfig 时，`kdo enrich` 默认走 regex 模式——对中文内容必然静默失败
   - 必须确保 `~/.kdo/config.yaml` 中已配置有效的 LLM API key（LLMConfig）
3. **验证自动切换**：配置 LLMConfig 后运行 `kdo enrich` 单卡，确认日志显示的是三步编译法（浓缩→质疑→对标）而非 regex 提取
4. **人工抽检输出**：enrich 完成后，人读一遍输出内容，确认有实质的质疑和合成加工，不是空壳或格式填充
5. **如果没配置 LLMConfig**：中文内容直接走手动 Agent 三步编译法，不要试图用 CLI 工具自动化

## 适用边界

- 适用于所有含中文、日文、韩文（CJK）内容的 wiki 页面——regex 的 `\b` 对它们全部失效
- 不适用于纯英文内容：regex 模式对英文有效，可以正常使用
- **已修复版本（2026-05-05 后）自动受益，但前提是有 LLMConfig**——如果没有配置 API key，仍然会静默失败
- 即使 LLMConfig 已配置，enrich 后的输出仍需人工抽检——三步编译法的质量取决于 LLM 能力，不能 100% 信任
- 自定义提取器脚本如果复制了 `extractors.py` 的 regex 逻辑，同样会继承这个缺陷

## 为什么值钱

- 这是 KDO 特有的坑：`kdo/extractors.py` 的 regex 提取器专门为英文语料设计，对中文有系统性排斥
- 最致命的是**静默失败**——返回 "0 pages enriched" 但 exit code 为 0，不会触发任何告警。在批量流水线中，这个信号会被直接忽略
- 暴露了 CLI 工具本地化盲区的一个典型模式：**regex + 英文关键词 + 长度阈值 = 非拉丁语系内容的系统性排斥**。这个模式在任何通用软件工程教材或 AI 训练语料中都不会被具体提及
- 任何 AI 训练语料中都不存在"kdo enrich 对中文页面返回 0 pages enriched 是因为 `\b` 不识别 CJK"这条知识——这是具体工具实现层面的暗知识

## 与其他知识的关联

- [[dk-c10-batch-tool-no-dry-run]] — 同一模式：KDO CLI 工具缺陷导致内容处理事故。C-10 是"批量覆盖破坏内容"，C-1 是"静默失败不处理内容"，两者都是"信任 CLI 工具 + 未人工验证"的变体
- [[master-ai-info-literacy]] — AI 信息素养的核心能力之一是识别工具的盲区和系统性偏差。C-1 是"工具对非英文内容的盲区"的典型案例
- `90_control/failure-modes.md` → F-KDO-001（已录入 AGENTS.md 禁止清单：不准对中文内容使用 regex 提取器）
- `20_memory/corrections.md` → C-1（原始记录）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
