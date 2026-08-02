---
id: dk-c1-cjk-regex-silent-fail
title: C-1：enrich 中文内容不能用 CLI regex→0 pages enriched 静默失败
type: dk
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: Builder
source_context: 2026-05-03
aliases:
  - Builder
  - 中文内容不能用
  - 内容不能用
  - 静默失败
source_refs:
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-16'
related:
- '[[dk-f6-cjk-skeleton-corruption]]'
- '[[yt-model-pan-product-climbing-map]]'
- '[[tool-clinic-medical-shortvideo-compliance]]'
- '[[concept-smart-medicine-cabinet-giants-why-not-clinic-cabinet]]'
- '[[sprint-2-gate-enrich-evidence]]'
- '[[dk-p11-regex-cutoff]]'
- '[[sprint-6-cli-gap-proposal]]'
- '[[case-dental-clinic-formula]]'
pipeline:
- src_unknown
- src_unknown
author: unknown
reviewed_by: 王语嫣
confidence: 0.7
trust_level: low
diagnostic_signals:
- signal: src_unknown
  framework_lens: 这是 regex 模式对 CJK 内容静默失败的典型症状：\b 词边界、英文关键词、长度阈值三重排斥同时触发
  follow_up_question: 检查 ~/.kdo/config.yaml 是否配置了有效 LLM API key；若无，禁止对中文页面使用 enrich，改走
    Agent 三步编译（浓缩→质疑→对标）
- signal: src_unknown
  framework_lens: 可能 LLM 路径未真正启用，或 regex 路径返回空导致 enrich 只更新了 frontmatter/status
  follow_up_question: 人读输出，确认是否出现“浓缩→质疑→对标”三段加工；如没有，手动重跑 Agent 三步编译并检查日志中的处理路径
- signal: src_unknown
  framework_lens: 流水线把 exit code 0 当成功信号，静默失败被淹没；CJK 内容在自动化管线中被系统性遗漏
  follow_up_question: 在脚本中加入 enrich 前后未 enrich 中文页面计数校验，或改用 LLM-based 路径，并将告警接入通知渠道
- signal: src_unknown
  framework_lens: 脚本复制了 extractors.py 的 \b / 英文 keyword / 长度阈值逻辑，继承了同样的 CJK 盲区
  follow_up_question: 审查脚本 regex，将 \b 替换为 CJK-aware 分词或改用 LLM/NLP 库；参考 F-KDO-001 防御模式
tags:
- audience:executor
- scene:reference
- skill-level:beginner
---

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

## 深度洞察

CJK 正则静默失败不是单纯的“中文 bug”，而是一类**以英文为中心设计的 CLI 工具对非拉丁语系内容的系统性排斥**。它的危险性在于三重叠加：

1. **失败是静默的**：exit code 为 0、日志无 error，唯一症状是“0 pages enriched”，在批量流水线中会被直接忽略。
2. **修复是设计层面的转向**：不是修 regex 就能解决，而是必须将 CJK 内容从“自动化 enrich”转向“人在环中的 Agent 三步编译”——这意味着中文内容在 KDO 中永久是**人智协作工作流**，不是全自动管线。
3. **影响会跨阶段扩散**：同样的 `\b` 词边界缺陷在 ingest 阶段表现为骨架页面中文摘要碎裂（参见 [[dk-f6-cjk-skeleton-corruption]]），在 enrich 阶段表现为零返回。两者共享根因，却呈现不同症状，需要跨阶段联合诊断。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **识别内容语言**：运行 enrich 前，先抽检待处理页面，确认是否包含中文字符（CJK）
2. **若含中文，禁止走 CLI regex 模式**：
   - src_unknown
   - src_unknown
3. **验证自动切换**：配置 LLMConfig 后运行 `kdo enrich` 单卡，确认日志显示的是三步编译法（浓缩→质疑→对标）而非 regex 提取
4. **人工抽检输出**：enrich 完成后，人读一遍输出内容，确认有实质的质疑和合成加工，不是空壳或格式填充
5. **如果没配置 LLMConfig**：中文内容直接走手动 Agent 三步编译法，不要试图用 CLI 工具自动化
6. **跨阶段校验**：若 enrich 静默失败，同时检查 ingest 产出的中文骨架是否也被 `\b` 损毁（参见 [[dk-f6-cjk-skeleton-corruption]]）

## 适用边界

| 边界 | 说明 |
|:
--|:------|
| ✅ 适合 | 识别和预防 KDO CLI regex 模式对 CJK 内容的系统性排斥 |
| ✅ 适合 | 批量流水线中需要检测 "0 pages enriched" 是否为静默失败 |
| ❌ 不适合 | 纯英文内容可正常使用 regex enrich，不需要本卡防御 |
| ❌ 不适合 | 未配置 LLMConfig 时，本卡不能替代 Agent 人工三步编译 |
| ⚠️ 注意 | 2026-05-05 后的自动切换依赖 LLMConfig；无 API key 仍会静默失败 |
| ⚠️ 注意 | 自定义提取器若复制 `extractors.py` 逻辑，会继承同样缺陷 |

| 失败模式 | 真实症状 | 可执行修复 |
|:-----|:------|:------|
| regex 词边界对 CJK 失效 | `kdo enrich --all` 对中文页面返回 0 pages enriched，exit code 0 | 配置 LLMConfig 启用自动三步编译；或手动执行 Agent 浓缩→质疑→对标 |
| 英文关键词过滤 CJK 内容 | 中文页面即使含“教程/文章/脚本”等主题，也被排除 | 不使用 regex keyword 过滤；改用 LLM 判断内容类型 |
| 长度阈值误伤中文 | 中文高密度短段落被判定为“过短无价值” | 调整阈值或改用基于语义密度的 LLM 评估 |
| 静默失败被流水线忽略 | CI/nightly 脚本运行正常，但中文卡片长期未 enrich | 在脚本中加入“未 enrich 中文页面计数”告警；人工抽检 |
| LLM 路径配置错误仍走 regex | 配置了 API key 但 enrich 输出仍是模板化空壳 | 检查 `~/.kdo/config.yaml` 中 LLM endpoint 是否有效；确认日志出现“浓缩→质疑→对标” |

## 修复 checklist：CJK 内容 enrich 前 5 问

在运行任何 `kdo enrich` 命令前，按以下顺序检查：

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

若 Q2-Q4 任一答案为“否”，立即切换到手动 Agent 三步编译，不要依赖 CLI enrich。

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
