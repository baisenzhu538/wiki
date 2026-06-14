---
id: "dk-f1-regex-on-cjk"
title: "F-KDO-001：CJK regex 静默零返回→kdo enrich 对中文页面永远返回 0 pages enriched"
type: "dark-knowledge"
dark_knowledge_type: "failure"
status: draft
domain:
  - "master"
source_person: "system"
source_context: "failure-modes.md F-KDO-001"
source_refs:
  - "90_control/failure-modes.md#F-KDO-001"
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - "dk-c1-cjk-regex-silent-fail"
  - "master-ai-info-literacy"
contradicts:
  - "dk-c1-cjk-regex-silent-fail"
  - "master-ai-info-literacy"
tags:
  - #domain/knowledge-management
  - #method/evaluation-method
  - #scene/ai-collaboration
  - #scene/learning-methodology
  - #scene/note-taking
  - #scene/skill-engineering
pipeline:
  - #boundary/requires-human-judgment
  - #source_type/error
  - confidence-draft
  - confidence-source-cited
author: legacy
reviewed_by: pending
---

# F-KDO-001：CJK regex 静默零返回→kdo enrich 对中文页面永远返回 0 pages enriched

## 原始表述

> **触发命令**：`kdo enrich --all`
>
> **表现**：输出 "0 pages enriched"，无报错，无任何页面被更新
>
> **根因**：`extractors.py` 中的 `extract_open_questions()` 使用 `\b` 词边界匹配——`\b` 不识别中文字符边界，对全中文页面永远返回空列表
>
> **触发信号**：`kdo enrich --all` 输出 "0 pages enriched" 但 wiki 目录下有未 enrich 的中文页面
>
> **防御措施**：① `kdo self-check` 的 unenriched-wiki-page 检查会在事后发现（已生效）② 事前防御：ingest 时检测内容语言，CJK 内容跳过 regex enrich 并提示走 Agent 三步编译
>
> **临时绕过**：Agent 直接编辑 wiki 页面文件，执行三步 CJK 编译（浓缩→质疑→对标），手动更新 frontmatter status=enriched
>
> **永久修复**：配置 `KDO_LLM_ENDPOINT` 环境变量启用 LLM-based CJK enrich 路径（`curation.py:enrich_wiki_page_llm`），或等待 `extractors.py` 增加 CJK-aware 分词器
>
> **关联文件**：`kdo/extractors.py`, `kdo/commands/curation.py` lines 142-336

## 使用场景

- 你准备用 `kdo enrich --all` 对 vault 中的中文页面做自动内容增强
- 你运行 enrich 后看到 "0 pages enriched"，需要判断是真的没有需要处理的页面，还是 regex 对 CJK 失效了
- 你在设计新的 extractor 或编写正则规则时，需要确认规则是否对 CJK 字符友好
- 你审查 `kdo self-check` 报告中的 unenriched wiki pages 列表，发现全是中文页面

## 操作方法

1. **识别内容语言**：运行 enrich 前，确认待处理页面是否含有 CJK 字符
2. **若含中文，禁止走 regex enrich**：`kdo enrich` 的 regex 模式对中文内容必然返回 0，不要浪费时间试验
3. **走 Agent 三步编译法**：浓缩 → 质疑 → 对标，手动编辑 wiki 页面文件
4. **配置 LLM 路径（可选）**：设置 `KDO_LLM_ENDPOINT` 环境变量，启用 LLM-based CJK enrich 自动化路径
5. **手动更新 status**：三步编译完成后，手动将 frontmatter 的 `status` 改为 `enriched`，并验证 `kdo self-check` 通过

## 适用边界

- 适用于所有含中文、日文、韩文（CJK）内容的 wiki 页面——regex 的 `\b` 对它们全部失效
- 不适用于纯英文内容：regex 模式对英文有效，可以正常使用 `kdo enrich`
- **与 F-KDO-006 共享同一根因**：F-KDO-001 是 enrich 阶段的失败，F-KDO-006 是 ingest 阶段的失败——两者都是 `\b` 不识别 CJK 导致的
- 即使配置了 LLM 路径，enrich 后仍需人工抽检输出质量——自动化不等于无需验证
- 自定义 extractor 脚本如果复制了 `extractors.py` 的 regex 逻辑，会继承这个缺陷

## 为什么值钱

- 这是 KDO CLI 特有的工具层面缺陷：`extractors.py` 专门为英文语料设计，对中文有系统性排斥
- **静默失败是最危险的失败模式**：exit code 为 0，日志里没有 error，你唯一发现的方式是事后检查 `kdo self-check`
- 暴露了 CLI 工具本地化盲区的典型模式：regex + 单词边界 + 英文关键词 = 非拉丁语系内容的系统性排斢
- 任何 AI 训练语料中都不会有"kdo enrich 的 `\b` 不识别 CJK 导致静默零返回"这条知识——这是具体工具实现层面的暗知识

## 与其他知识的关联

- dk-c1-cjk-regex-silent-fail — corrections 层面的具体事故记录：2026-05-03 Builder 报告 enrich 对中文页面返回 0。F-KDO-001 是这个具体事故的模式化抽象
- master-ai-info-literacy — AI 信息素养的核心能力：识别工具的盲区和系统性偏差。F-KDO-001 是"工具对非英文内容的盲区"的典型案例
- `90_control/failure-modes.md` → F-KDO-001（原始记录）
- `90_control/AGENTS.md` → 禁止清单 #1（不准对中文内容执行 `kdo enrich`）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
