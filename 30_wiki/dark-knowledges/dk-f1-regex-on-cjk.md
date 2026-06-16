---
id: dk-f1-regex-on-cjk
title: F-KDO-001：CJK regex 静默零返回→kdo enrich 对中文页面永远返回 0 pages enriched
type: dark-knowledge
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: system
source_context: failure-modes.md F-KDO-001
source_refs:
- 90_control/failure-modes.md#F-KDO-001
created_at: 2026-05-31
updated_at: '2026-06-16'
related:
- '[[dk-c1-cjk-regex-silent-fail]]'
- '[[dk-f2-txt-ingest-skip]]'
- '[[dk-f6-cjk-skeleton-corruption]]'
- '[[dk-p11-regex-cutoff]]'
- '[[master-ai-info-literacy]]'
pipeline:
- confidence-draft
- confidence-source-cited
- confidence-verified-by-case
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.7
trust_level: low
diagnostic_signals:
- signal: "运行 `kdo enrich --all` 后输出 `0 pages enriched`，exit code 为 0，且 vault 中存在未 enrich 的中文页面"
  framework_lens: regex 的 `\\b` 词边界对 CJK 字符不生效，enrich 提取器在中文内容上空匹配，系统把“无结果”当“无工作”
  follow_up_question: 立即抽检 3-5 个未 enrich 页面的语言；若含中文字符，改用 LLM 路径或 Agent 三步编译，不要再重试 enrich
- signal: "自动生成或 enrich 后的中文页面 Summary 出现无意义碎片，如'的概和心结提取课特有'"
  framework_lens: 同一根因在 ingest/enrich 两阶段的表现：`\\b` 随机切分 CJK 文本，导致摘要截断或关键词为空
  follow_up_question: 不要尝试修复自动骨架，直接对中文页面执行三步 CJK 编译（浓缩→质疑→对标），并人工校验可读性
- signal: "自定义 extractor 或脚本复制了 `extractors.py` 的 regex 逻辑，对中文文档返回空列表或错误关键词"
  framework_lens: 缺陷会通过“复制代码”传播到任何继承 `\\b` 或英文关键词假设的正则逻辑
  follow_up_question: 审计所有基于 regex 的提取器，把 `\\b` 替换为 CJK-aware 模式或改用分词库，并在中文样本上回归测试
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

## 深度洞察

- **这不是“中文没写好”，而是“工具对非拉丁语系有系统性排斥”**：exit code 为 0 让失败看起来像是“没有需要处理的内容”，真正的信号被静默吞掉。
- **`\b` 的问题只是表象，底层假设是“单词=字母+空格”**：只要 extractor 用英文关键词、长度阈值、单词边界中的任意一个，就会在不同程度上对 CJK 失效。
- **同一根因跨阶段复现**：enrich 阶段是“零返回”，ingest 阶段是“中文摘要碎化”（F-KDO-006），自定义脚本复制逻辑后会再次复现——它是会传染的缺陷模式。
- **最值钱的不是修复代码，而是修复“对 CLI 自动化默认信任”的认知**：批量管线中越“干净”的日志，越容易掩盖这种失败。

## 使用场景

- 你准备用 `kdo enrich --all` 对 vault 中的中文页面做自动内容增强
- 你运行 enrich 后看到 "0 pages enriched"，需要判断是真的没有需要处理的页面，还是 regex 对 CJK 失效了
- 你在设计新的 extractor 或编写正则规则时，需要确认规则是否对 CJK 字符友好
- 你审查 `kdo self-check` 报告中的 unenriched wiki pages 列表，发现全是中文页面
- 你维护自定义脚本，发现中文文档返回空列表或错误关键词

## 操作方法

1. **识别内容语言**：运行 enrich 前，确认待处理页面是否含有 CJK 字符
2. **若含中文，禁止走 regex enrich**：`kdo enrich` 的 regex 模式对中文内容必然返回 0，不要浪费时间试验
3. **走 Agent 三步编译法**：浓缩 → 质疑 → 对标，手动编辑 wiki 页面文件
4. **配置 LLM 路径（可选）**：设置 `KDO_LLM_ENDPOINT` 环境变量，启用 LLM-based CJK enrich 自动化路径
5. **手动更新 status**：三步编译完成后，手动将 frontmatter 的 `status` 改为 `enriched`，并验证 `kdo self-check` 通过
6. **审计自定义 extractor**：如果复制了 `extractors.py` 的 regex 逻辑，替换 `\b` 为 CJK-aware 边界或改用分词器

## Constraints & Boundaries

### 适用边界

| 边界 | 说明 |
|:-----|:------|
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

- `extractors.py` 的 regex 类似 `(?i)\b(open questions|gaps|assumptions)\b`。
- 中文段落 `"我们需要明确用户取药时的开柜权限问题"` 中，`\b` 找不到“字母-非字母”边界，匹配不到任何候选片段。
- 结果：关键词列表为空，enrich 流程认为“无需更新”。

**修复动作**：

1. 不重新跑 enrich。
2. Agent 按三步 CJK 编译重写页面：
   - 浓缩：提取“取药权限”“离线场景”“异常开柜”三个核心问题。
   - 质疑：追问“如果用户手机没电怎么办？”“如果柜门被暴力打开如何告警？”
   - 对标：补充 `case-smart-medicine-cabinet-failure-patterns-library` 中的真实失败模式作为参考。
3. 手动设置 `status: enriched`。
4. 在 `kdo self-check` 中确认该卡不再出现在 unenriched 列表。

## 落地模板：CJK 内容处理 30 秒自检清单

```markdown
- [ ] 运行 enrich 前，先用 `grep -P '[\x{4e00}-\x{9fff}]' <file>` 检查页面是否含中文
- [ ] 若含中文 → 禁止走 regex enrich，改用 LLM 路径或 Agent 三步编译
- [ ] 若含中文且已自动生成骨架 → 直接重写，不尝试局部修复
- [ ] enrich/重写后，人工抽检 1 个中文页面，确认 Summary 可读、open questions 不离题
- [ ] 更新 frontmatter `status: enriched` 后，运行 `kdo self-check` 确认无未处理中文页面
- [ ] 若维护自定义 extractor → 在中文样本上回归测试，确保没有 `\b` 依赖
```

## 为什么值钱

- 这是 KDO CLI 特有的工具层面缺陷：`extractors.py` 专门为英文语料设计，对中文有系统性排斥
- **静默失败是最危险的失败模式**：exit code 为 0，日志里没有 error，你唯一发现的方式是事后检查 `kdo self-check`
- 暴露了 CLI 工具本地化盲区的典型模式：regex + 单词边界 + 英文关键词 = 非拉丁语系内容的系统性排斥
- 任何 AI 训练语料中都不会有"kdo enrich 的 `\b` 不识别 CJK 导致静默零返回"这条知识——这是具体工具实现层面的暗知识
- 该模式会跨阶段（ingest/enrich）和跨脚本（自定义 extractor）复现，识别一次就能规避一类事故

## 与其他知识的关联

- [[dk-c1-cjk-regex-silent-fail]] — corrections 层面的具体事故记录：2026-05-03 Builder 报告 enrich 对中文页面返回 0。F-KDO-001 是这个具体事故的模式化抽象
- [[dk-f6-cjk-skeleton-corruption]] — 同一根因在不同阶段的表现：F-KDO-006 是 ingest 阶段中文骨架碎化，与 F-KDO-001 共同构成 CJK 内容的系统性盲区
- [[dk-p11-regex-cutoff]] — 同类“手写正则解析内容”陷阱：P-11 是 `^##` 误匹配 `###` 导致 section 截断，提醒我们任何 regex 解析 Markdown 都需边界检查
- [[dk-f2-txt-ingest-skip]] — 另一个 KDO CLI 静默失败模式：扩展名白名单导致 .txt 被跳过，与 F-KDO-001 共同说明“exit 0 ≠ 成功”
- [[master-ai-info-literacy]] — AI 信息素养的核心能力：识别工具的盲区和系统性偏差。F-KDO-001 是"工具对非英文内容的盲区"的典型案例
- `90_control/failure-modes.md` → F-KDO-001（原始记录）
- `90_control/AGENTS.md` → 禁止清单 #1（不准对中文内容执行 `kdo enrich`）

## 老顽童疑问（2026-06-16）

无疑问，请欧阳锋审查。
