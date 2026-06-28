---

id: dk-f1-regex-on-cjk
title: F-KDO-001：CJK regex 静默零返回→kdo enrich 对中文页面永远返回 0 pages enriched
type: dk
dark_knowledge_type: failure
status: reviewed
domain:
- master
source_person: system
source_context: failure-modes.md F-KDO-001
source_refs:
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-28'
related:
  - [[kdo-input-channel-strategy-2026-06-16]]
  - [[kdo-protocol]]
  - [[modeling-to-kdo-toolchain]]
  - [[kdo-batch-produce-req014]]
  - [[kdo-15-dimension-label-spec]]
  - [[obsidian-kdo-内容产出工作流-产品设计大纲]]
  - [[tool-ban-fei-mao-qing-xi-zi-liao-wei-markdown-ge-shi-wei-gei-ai]]
  - [[kdo-watch-health-check-layer]]
  - [[framework-kdo-self-attack]]
  - [[kdo-yaml-frontmatter-safety]]
  - [[kdo-priority-checklist]]
  - [[dk-f6-cjk-skeleton-corruption]]
  - [[kdo_product_design_agent_final]]
  - [[proposal-kdo-flywheel-infrastructure]]
  - [[yc-放出一套ai-native-公司组织方法论直接把公司当操作系统来设计中层管理变成了-markdown]]
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.7
trust_level: low
diagnostic_signals:
- signal: src_unknown
  framework_lens: regex 的 `\\b` 词边界对 CJK 字符不生效，enrich 提取器在中文内容上空匹配，系统把“无结果”当“无工作”
  follow_up_question: 立即抽检 3-5 个未 enrich 页面的语言；若含中文字符，改用 LLM 路径或 Agent 三步编译，不要再重试
    enrich
- signal: src_unknown
  framework_lens: 同一根因在 ingest/enrich 两阶段的表现：`\\b` 随机切分 CJK 文本，导致摘要截断或关键词为空
  follow_up_question: 不要尝试修复自动骨架，直接对中文页面执行三步 CJK 编译（浓缩→质疑→对标），并人工校验可读性
- signal: src_unknown
  framework_lens: 缺陷会通过“复制代码”传播到任何继承 `\\b` 或英文关键词假设的正则逻辑
  follow_up_question: 审计所有基于 regex 的提取器，把 `\\b` 替换为 CJK-aware 模式或改用分词库，并在中文样本上回归测试
review_date: '2026-06-28'

---

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

## 深度洞察

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **识别内容语言**：运行 enrich 前，确认待处理页面是否含有 CJK 字符
2. **若含中文，禁止走 regex enrich**：`kdo enrich` 的 regex 模式对中文内容必然返回 0，不要浪费时间试验
3. **走 Agent 三步编译法**：浓缩 → 质疑 → 对标，手动编辑 wiki 页面文件
4. **配置 LLM 路径（可选）**：设置 `KDO_LLM_ENDPOINT` 环境变量，启用 LLM-based CJK enrich 自动化路径
5. **手动更新 status**：三步编译完成后，手动将 frontmatter 的 `status` 改为 `enriched`，并验证 `kdo self-check` 通过
6. **审计自定义 extractor**：如果复制了 `extractors.py` 的 regex 逻辑，替换 `\b` 为 CJK-aware 边界或改用分词器

## 适用边界

| 边界 | 说明 |
|:
--|:------|
| ✅ 适用 | 所有含中文、日文、韩文（CJK）内容的 wiki 页面——regex 的 `\b` 对它们全部失效 |
| ❌ 不适用 | 纯英文内容：regex 模式对英文有效，可以正常使用 `kdo enrich` |
| 设计约束 | 当前 KDO 没有 CJK-aware extractor，这是设计约束而非临时 bug，短期内不会自动消失 |
| 传播约束 | 自定义 extractor 脚本如果复制了 `extractors.py` 的 regex 逻辑，会继承这个缺陷 |
| 质量约束 | 即使配置了 LLM 路径，enrich 后仍需人工抽检输出质量——自动化不等于无需验证 |

### 常见失败模式

| 模式 | 症状 | 修复 |
|:-----|:------|:-----|
| 静默零返回 | `kdo enrich --all` 输出 "0 pages enriched"，exit code 为 0，未 enrich 的中文页面被跳过 | 含中文页面不走 regex，改用 LLM 路径或 Agent 三步编译；事后用 `kdo self-check` 兜底 |
| 中文摘要碎化 | ingest/enrich 后 Summary 变成无意义汉字碎片，如"的概和心结提取课特有" | 不修复骨架，直接重写页面；完成后 `status=enriched` 并人工读一遍 |
| 关键词/问题漏提 | 页面被 enrich 但生成的 open questions、tags 为空或与主题无关 | 手动补充三步编译中的“质疑”和“对标”输出，不要依赖 regex 提取 |
| 缺陷跨脚本传染 | 自己写的 extractor/脚本复制 `extractors.py` 逻辑后，对中文文档同样返回空 | 审计 regex：`\b` 替换为 `(?=[\x{4e00}-\x{9fff}])` 等 CJK-aware 模式，或用 jieba/mecab 分词 |

## 真实案例：中文产品需求文档 enrich 后关键词全丢

**背景**：某张中文产品需求卡 `concept-prd-smart-cabinet.md` 全文约 1200 字，标题与正文均为中文。

**触发**：执行 `kdo enrich --all` 后，该卡状态仍为 `draft`，输出显示 `0 pages enriched`。

**根因定位**：

- src_unknown
- src_unknown
- src_unknown

**修复动作**：

1. 不重新跑 enrich。
2. Agent 按三步 CJK 编译重写页面：
   - src_unknown
   - src_unknown
   - src_unknown
3. 手动设置 `status: enriched`。
4. 在 `kdo self-check` 中确认该卡不再出现在 unenriched 列表。

## 落地模板：CJK 内容处理 30 秒自检清单

```markdown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
```

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
- src_unknown

## 老顽童疑问（2026-06-16）

无疑问，请欧阳锋审查。
