---

id: dk-c3-txt-ingest-skip
title: C-3：.txt 文件被 kdo ingest 静默跳过→state.json 无变化但返回成功
type: dk
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: Builder
source_context: 2026-05-03
source_refs:
- 10_raw/sources/src_20260619_f35cd8b6_20_memory_corrections.md
created_at: 2026-05-31
updated_at: '2026-06-16'
related:
  - '[[dk-f2-txt-ingest-skip]]'
  - '[[存储策略]]'
  - '[[dk-f5-stale-feedback-ref]]'
  - '[[dk-f3-state-json-race-condition]]'
  - '[[dk-p16-validate-reads-state-json]]'
  - '[[dk-c1-cjk-regex-silent-fail]]'
  - '[[dk-f2-txt-ingest-skip]]'
  - '[[dk-p16-validate-reads-state-json]]'
  - '[[master-ai-info-literacy]]'
pipeline:
- confidence-draft
- confidence-source-cited
author: unknown
reviewed_by: 欧阳锋
confidence: 0.7
trust_level: low
diagnostic_signals:
- signal: "`kdo ingest` 执行后 exit code 为 0，但 `state.json` 的 `ingested_inbox_files` 列表无新增"
  framework_lens: 这是 KDO ingest 的"静默跳过"模式：扩展名白名单只包含 `.md`，非 `.md` 文件被设计为不报错、不处理
  follow_up_question: 立即执行 `find 00_inbox -type f ! -name '*.md'` 列出所有非 .md 文件；对 .txt 执行 `cp file.txt file.md` 后重跑 ingest，并再次检查 state.json 计数
- signal: "自动化脚本跑完后，vault/源文件目录里找不到预期的 wiki 页面或源文件"
  framework_lens: 批量管线中"返回成功"被脚本视为完成信号，但扩展名白名单过滤导致实质数据未进入处理流程
  follow_up_question: 在脚本里加入"ingest 前后 state.json 计数校验"，若 inbox 中仍有非 .md 文件但 state 计数未增加，则判定为静默跳过并告警
- signal: ".txt 文件转换后的同名 .md 已存在，但内容缺少 frontmatter 或 validate 报错"
  framework_lens: 简单改扩展名只是绕过白名单，ingest 后系统仍按 Markdown 规范要求结构化元数据
  follow_up_question: 转换后是否为文件注入了最小 frontmatter（id/type/title/created_at/updated_at/source_refs）？运行 `kdo validate` 是否通过？
- signal: "团队新成员/外部协作者把 `.txt` 素材丢进 inbox，几天后仍无对应 wiki 页面"
  framework_lens: 这是组织知识沉淀流程中的"格式盲区"：贡献者不知道 KDO ingest 的扩展名白名单，系统也不会主动反馈
  follow_up_question: 是否在 inbox 入口有 CONTRIBUTING/README 说明？是否在 CI/预提交钩子中跑 `find 00_inbox -type f ! -name '*.md'` 并阻塞合并？
---
# C-3：.txt 文件被 kdo ingest 静默跳过→state.json 无变化但返回成功

## 原始表述

> `kdo ingest` 对 `.txt` 文件静默返回成功，但什么都不做。无错误信息，state.json 无变化。
>
> 根因：ingest 只识别 `.md` 扩展名，非 `.md` 文件直接跳过。
>
> 修正：ingest 前检查扩展名，如果是 `.txt` 先 `cp file.txt file.md` 再 ingest。
>
> 关联失败模式：F-KDO-002（已录入 AGENTS.md 禁止清单）

## 深度洞察

`.txt` 被跳过不是简单的"漏处理"，而是 KDO CLI 中一个典型的 **fail-silent（静默失败）设计**：扩展名白名单把不支持的文件直接过滤掉，同时上层命令仍返回成功状态。问题的核心不在"跳过"本身，而在于 **"成功"信号与"零产出"同时出现**——这会让所有依赖 exit code 的自动化脚本、CI 流程、夜间定时任务都误判为正常完成。

更隐蔽的是数据丢失风险。假设某次批量导入有 50 个 `.txt` 口述稿，运行 `kdo ingest` 后 state.json 一条没增加，但命令返回 0。如果操作者没有养成"ingest 后校验 state.json"的习惯，这些素材可能在几天甚至几周后才被发现遗漏，期间团队已经默认"素材已入库"并继续 downstream 工作（标注、建模、出卡）。此时修复成本不再是"重新跑一遍 ingest"，而是**回溯哪些素材缺失、补 frontmatter、重跑下游流程、检查是否已产生错误卡片**。

一个反常识点是：**单纯把 `.txt` 重命名为 `.md` 只是绕过白名单，不等于正确入库**。ingest 后系统会按 Markdown 卡片规范处理文件，没有 frontmatter 的纯文本会被生成 wiki 页面，但后续 `validate` 可能报缺少 `id`/`type`/`source_refs`，`enrich` 也可能因缺少元数据而跳过。因此".txt → .md"只是第一步，后处理（补 frontmatter、校验、编码检查）才是避免二次沉默失败的关键。

## 使用场景

- 你有一批 `.txt` 格式的口述稿/素材文件要导入 KDO vault，运行 `kdo ingest` 后看到 "success" 但 vault 里找不到新文件
- 你写自动化脚本批量处理 `00_inbox/` 中的原始素材，脚本跑完但输出目录为空
- 你检查 `state.json` 确认 ingest 状态，发现文件数量没有增加，需要判断是重复文件还是被静默跳过
- 你在设计 KDO 的 ingest 管线，需要确认支持哪些输入格式
- 你在做团队 onboarding，需要给新成员写"素材入库前的格式检查"规范

## 诊断信号

| 信号 Signal | 透镜 Lens | 跟进 Follow-up |
|:---|:---|:---|
| `kdo ingest` 执行后 exit code 为 0，但 `state.json` 的 `ingested_inbox_files` 列表无新增 | 这是 KDO ingest 的"静默跳过"模式：扩展名白名单只包含 `.md`，非 `.md` 文件被设计为不报错、不处理 | 立即执行 `find 00_inbox -type f ! -name '*.md'` 列出所有非 .md 文件；对 .txt 执行 `cp file.txt file.md` 后重跑 ingest，并再次检查 state.json 计数 |
| 自动化脚本跑完后，vault/源文件目录里找不到预期的 wiki 页面或源文件 | 批量管线中"返回成功"被脚本视为完成信号，但扩展名白名单过滤导致实质数据未进入处理流程 | 在脚本里加入"ingest 前后 state.json 计数校验"，若 inbox 中仍有非 .md 文件但 state 计数未增加，则判定为静默跳过并告警 |
| .txt 文件转换后的同名 .md 已存在，但内容缺少 frontmatter 或 validate 报错 | 简单改扩展名只是绕过白名单，ingest 后系统仍按 Markdown 规范要求结构化元数据 | 转换后是否为文件注入了最小 frontmatter（id/type/title/created_at/updated_at/source_refs）？运行 `kdo validate` 是否通过？ |
| 团队新成员/外部协作者把 `.txt` 素材丢进 inbox，几天后仍无对应 wiki 页面 | 这是组织知识沉淀流程中的"格式盲区"：贡献者不知道 KDO ingest 的扩展名白名单，系统也不会主动反馈 | 是否在 inbox 入口有 CONTRIBUTING/README 说明？是否在 CI/预提交钩子中跑 `find 00_inbox -type f ! -name '*.md'` 并阻塞合并？ |

## 操作方法

1. **检查文件扩展名**：运行 ingest 前，先 `find 00_inbox -type f` 确认待处理文件的扩展名——`.txt` 会被跳过
2. **手动转换**：对 `.txt` 文件执行 `cp file.txt file.md`，再运行 `kdo ingest file.md`
3. **批量处理脚本**：如果文件量大，用循环自动转换——`for f in 00_inbox/*.txt; do cp "$f" "${f%.txt}.md"; done`
4. **注入最小 frontmatter**：转换后，给每个 `.md` 补上前言元数据，至少包含 `id`/`type`/`title`/`created_at`/`updated_at`/`source_refs`
5. **验证 state.json**：ingest 后检查 `state.json`，确认 `ingested_inbox_files` 计数确实增加了
6. **运行 validate**：对新生成的 wiki 页面跑 `kdo validate`，确认无 missing frontmatter 或格式错误
7. **内容清理（可选）**：如果 `.txt` 内容不是标准 Markdown，转换后可能需要调整标题层级、列表符号或补充结构化标记

## 适用边界

| 边界 | 说明 |
|:---|:---|
| **适合** | 需要把 `.txt` 口述稿/素材导入 KDO vault，且内容可整理为 Markdown 卡片的场景 |
| **不适合** | `.docx`、`.pdf`、`.html` 等富格式——需要先用专用工具/脚本转为 Markdown，不能简单改扩展名 |
| **不适合** | 已经配置自定义 extractor 白名单覆盖 `.txt` 的 KDO 版本/分支——此时 ingest 行为已被改写 |
| **不适合** | `.txt` 只是临时草稿、不期望进入 vault 的场景——此时跳过是正确的行为，不应转换 |
| **边界条件** | 即使改了 `.md` 扩展名，完全无结构的纯文本仍需人工补充 frontmatter 和结构化标记 |
| **边界条件** | 批量转换前需确认 `.txt` 编码为 UTF-8，否则改扩展名后可能出现 CJK 乱码 |

## 常见失败模式

| 失败模式 | 真实症状 | 可执行修复 |
|:---|:---|:---|
| **静默跳过导致数据"假入库"** | `kdo ingest` 成功，state.json 无新增，几天后找素材找不到 | ingest 前 `find 00_inbox -type f ! -name '*.md'`；非 .md 先转换再 ingest；ingest 后校验 state.json 计数是否增加 |
| **改扩展名后 frontmatter 缺失** | `.txt` → `.md` 后 ingest 成功，但 `validate` 报 missing frontmatter / id / type | 转换脚本自动注入最小 frontmatter 模板；人工补 id/type/title/created_at/updated_at/source_refs |
| **批量脚本误删原始 .txt** | `cp file.txt file.md && rm file.txt` 后，原始素材丢失，.md 若被误改无法回溯 | 转换时不删除原 .txt，或先移动到 `10_raw/archive/`；保留原始素材直到 .md 通过 validate |
| **编码问题导致 CJK 乱码** | `.txt` 是 GBK/ANSI 编码，改扩展名后 ingest，中文显示为 � 或乱码 | 转换前用 `file -i` 或 Python 检测编码；非 UTF-8 先转码 `iconv -f GBK -t UTF-8` |
| **重复 ingest 产生重复页面** | 同一素材先以 .txt 跳过，后转成 .md 再次 ingest，因 id 不同生成两个 wiki 页面 | 转换时指定稳定 id（如基于文件名哈希）；ingest 前检查是否已存在同名/id 页面 |

## 落地模板：txt 素材入库前检查清单

在批量把 `.txt` 素材导入 KDO 前，逐条勾选：

| 步骤 | 检查项 | 通过标准 | 修复动作 |
|:---|:---|:---|:---|
| 1. 扩展名扫描 | `find 00_inbox -type f ! -name '*.md'` | 输出为空，或所有非 .md 文件都是已知可跳过类型 | 对 .txt 执行 `cp file.txt file.md` |
| 2. 编码检查 | `file -i 00_inbox/*.txt` | 全部为 UTF-8 或 ASCII | 非 UTF-8 用 `iconv` 转码后再转换 |
| 3. 原始备份 | 检查 `10_raw/archive/` 或 `.git` | 原始 .txt 未被删除，或已版本控制 | 转换脚本禁止 `rm` 原文件 |
| 4. frontmatter 注入 | 每个新 .md 文件头部 | 包含 id / type / title / created_at / updated_at / source_refs | 用脚本模板批量注入，缺失则补全 |
| 5. ingest 后计数校验 | `state.json` 的 `ingested_inbox_files` | 计数增加量 = 本次处理的 .md 文件数 | 若未增加，立即回查日志和文件列表 |
| 6. validate 校验 | `kdo validate` | 无 P0/P1 错误 | 修复 frontmatter/格式问题 |
| 7. 内容抽样人读 | 随机打开 1-2 张新卡 | 无乱码、无碎片化、标题层级正确 | 对问题文件重新整理 |

**风险量化速算**：
- 假设本次有 `N` 个 `.txt` 文件未被发现跳过
- 每个文件平均下游工作量为 `W` 小时（标注/建模/出卡）
- 发现延迟为 `D` 天
- **隐性损失 ≈ N × W × (1 + 0.1D)**（延迟越久，回溯和重跑成本越高）

> 例：20 个口述稿被跳过，每个后续建模需 2 小时，7 天后才发现 → 损失 ≈ 20 × 2 × (1 + 0.7) = 68 小时。

## 为什么值钱

- 这是 KDO CLI 特有的行为：`kdo ingest` 的扩展名白名单只包含 `.md`，`.txt` 被设计为"静默跳过"而非报错——这个设计决策本身不在任何文档中明确说明
- **"返回成功但什么都不做"是最危险的失败模式**：exit code 为 0，日志里没有 error，你唯一发现的方式是事后检查 `state.json` 或 vault 目录
- 暴露了 CLI 工具中"静默跳过"这一反模式：对不支持的输入格式，应该选择报错（fail fast）还是静默跳过？KDO 选择了后者，代价是用户需要靠经验才能发现
- 任何 AI 训练语料中都不会有"kdo ingest 跳过 .txt 但返回成功"这条知识——这是具体工具实现层面的暗知识
- 在团队协作中，这个问题会从"个人踩坑"升级为"流程级数据丢失"：新成员、外部贡献者、自动化脚本都可能把 `.txt` 当成合法输入，而系统不会给出任何反馈

## 与其他知识的关联

- [[dk-c1-cjk-regex-silent-fail]] — 同一模式：KDO CLI 工具的"静默失败"。C-1 是 enrich 对中文返回 0，C-3 是 ingest 对 .txt 跳过——两者都是"exit code 为 0 + 无实质输出"
- [[dk-f2-txt-ingest-skip]] — F-KDO-002 的系统级抽象：非 .md 文件 ingest 静默跳过。dk-c3 是 Builder 在 2026-05-03 报告的具体事故，dk-f2 是这个事故的模式化、防御措施化版本
- [[dk-p16-validate-reads-state-json]] — 诊断 C-3 时必须读取 `state.json`，但 P-16 提醒我们：validate 优先读 state.json 而非文件 frontmatter，多处数据拷贝可能不一致，校验时要确认自己看的是正确的那份数据
- [[master-ai-info-literacy]] — AI 信息素养要求使用者了解工具的输入格式白名单和盲区。C-3 是"ingest 工具扩展名白名单盲区"的具体案例
- `90_control/failure-modes.md` → F-KDO-002（已录入 AGENTS.md 禁止清单：不准直接将 .txt 丢给 kdo ingest）
- `20_memory/corrections.md` → C-3（原始记录）

## 老顽童疑问（2026-06-16）

无疑问，请欧阳锋审查。
