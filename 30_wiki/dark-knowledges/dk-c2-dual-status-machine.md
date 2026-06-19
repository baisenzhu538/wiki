---
id: dk-c2-dual-status-machine
title: C-2：Schema status 字段混用两个状态机→字段值互相污染
type: dark-knowledge
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: Builder
source_context: 2026-05-03
source_refs:
- 10_raw/sources/src_20260619_f35cd8b6_20_memory_corrections.md#C-2
created_at: 2026-05-31
updated_at: '2026-06-16'
related:
- '[[dk-c10-batch-tool-no-dry-run]]'
- '[[dk-p18-yaml-parser]]'
- '[[kdo-yaml-frontmatter-safety]]'
- '[[master-systems-thinking]]'
pipeline:
- confidence-draft
- confidence-source-cited
author: unknown
reviewed_by: 欧阳锋
confidence: 0.7
trust_level: low
diagnostic_signals:
- signal: "在 wiki 卡片 frontmatter 里看到 `status: enriched` 或 `status: superseded`，但 schema 枚举里没有这两个值"
  framework_lens: 同一个 `status` 字段名被两个独立状态机共用：wiki 页面用编译进度状态机，decision.yaml 用审批流程状态机
  follow_up_question: 先确认文件类型：若是 `.md` 则 `enriched/superseded` 合法；若是 `decision.yaml` 则属违规。是否在 schema 注释中显式声明了双状态机？
- signal: "自动化脚本用 `status == \"reviewed\"` 过滤卡片，结果漏掉 enriched 或把 decision 文件的 stable 误判"
  framework_lens: 脚本把单一状态语义硬编码到所有文件类型，没有区分 frontmatter 与 decision 文件的状态机
  follow_up_question: 把脚本改为按文件类型分支；为两种状态机分别定义枚举常量；为过滤逻辑补单元测试，覆盖 enriched、superseded、stable、needs-review 等边界值
- signal: "Schema 讨论中有人说'只要加 enforcement 就能避免 enriched 出现'"
  framework_lens: 这是归因偏差：把设计冲突（两个状态机共用字段名）误判为执行松懈（schema 写了但没严格执行）
  follow_up_question: 重新审视系统中是否真的只有一个状态机；若存在两条流水线，必须拆分字段名或在 schema 中显式保留双枚举并注明适用范围
- signal: "第三方工具/外部集成读取 KDO frontmatter 后报告 `status` 值异常"
  framework_lens: 外部集成未被告知 `status` 字段的双重语义，按单一枚举解析必然报错
  follow_up_question: 在对外接口文档中写明 `status` 的双重语义和两张取值表；考虑对外暴露拆分后的字段（如 `compile_status` / `approval_status`）
---
# C-2：Schema status 字段混用两个状态机→字段值互相污染

## 原始表述

> `status` 字段出现了 `enriched`（不在 schema 枚举 `draft/reviewed/stable/needs-review` 中），Architect 误判为"Schema 写了但没严格执行"。
> 
> 根因：两个独立状态机共用了同一个字段名：
> - 编译进度状态机：`draft → enriched → reviewed → superseded`（wiki 页面 frontmatter）
> - 审批流程状态机：`draft → reviewed → stable → needs-review`（decision.yaml）
> 
> 修正：当前不改代码，在 `schemas/concept.yaml` 加注释声明两个状态机的存在。下一轮 Schema 升级时考虑拆分字段名（如 `compile_status` vs `approval_status`）。

## 深度洞察

- **schema 违规可能不是执行问题，而是设计冲突。** `enriched` 出现在 decision.yaml 的 schema 枚举之外，但它在 wiki 页面的编译状态机里完全合法。把"设计冲突"诊断为"执行不严"会导向错误的修正方向。
- **最危险的是自动化脚本的硬编码判断。** 人看到 `enriched` 还能结合上下文猜测，脚本只会按字面匹配；一旦 `status == "reviewed"` 被写成全局过滤条件，就会系统性漏掉 enriched 卡片或误判 decision 文件。
- **"兼容不改字段名"是债务的种子。** 早期系统只有一个状态机，后期叠加第二个子系统时为了省事复用 `status`，结果产生语义污染。临时加注释不是根治，只是把隐性债务显性化，避免下一个人再踩。
- **双状态机问题对第三方集成是隐性陷阱。** 任何读取 KDO frontmatter 的外部工具，如果按单一枚举解析 `status`，都会在同步时出错——而 KDO 的接口文档此前并未声明这一歧义。

## 使用场景

- 你在设计或修改 wiki 卡片/决策文件的 frontmatter schema，需要新增或复用字段名
- 你在审查别人提交的卡片，看到 `status: enriched` 或 `status: superseded`，需要判断这是合法值还是 schema 违规
- 你在编写自动化脚本读取 `status` 字段做逻辑分支（如"只处理 reviewed 状态的卡片"）
- 你在做 schema 版本升级，需要评估字段名拆分的影响范围
- 你在对接第三方工具，需要对外暴露 KDO 卡片状态字段的语义

## 操作方法

1. **看到 status 字段，先问语义**：这个 status 描述的是"编译到哪个阶段了"还是"审批到哪个阶段了"？
2. **查文件类型定状态机**：
   - wiki 页面 frontmatter（`.md` 文件）→ 编译进度状态机：`draft → enriched → reviewed → superseded`
   - decision.yaml / 任务文件 → 审批流程状态机：`draft → reviewed → stable → needs-review`
3. **写 schema 时加注释**：如果在修改 `schemas/concept.yaml`，必须在 `status` 字段旁用注释声明两个状态机的共存，明确各自取值范围
4. **代码审查硬编码值**：检查所有读取 `status` 字段的脚本逻辑，确认它期望的是哪个状态机——一个脚本混用两个语义是灾难
5. **规划拆分**：下一轮 schema 升级时，将字段拆分为 `compile_status`（wiki 页面）和 `approval_status`（决策/任务文件），彻底消除歧义
6. **对外接口显式声明**：任何向外部暴露 `status` 的 API/文档，必须附两张状态机取值表或直接使用拆分后的字段名

## 适用边界

| 边界 | 说明 |
|:-----|:------|
| 适用于同时存在内容编译流与审批流程的项目 | 只有两条流水线共用字段名时才会触发此问题 |
| 适用于所有读取 frontmatter/decision.yaml 的自动化脚本 | 脚本硬编码 `status` 判断时风险最高，必须按文件类型分支 |
| 当前"加注释"方案是临时补丁，非根治 | 根治需要 schema 升级 + 全量数据迁移，成本较高 |
| 不适用于单一状态机系统 | 如果全项目只有一种进度状态，不会出现此问题 |
| 对外接口必须显式说明 | 第三方工具读取 KDO frontmatter 会受歧义影响，接口文档必须声明双状态机 |

## 常见失败模式

| 模式 | 症状 | 修复 |
|:-----|:------|:-----|
| 状态机 A 的值被状态机 B 判定为非法 | `kdo validate` 报告 `status: enriched` 不在 `draft/reviewed/stable/needs-review` 枚举中 | 在 schema 注释声明双状态机；校验脚本按文件类型使用不同枚举 |
| 脚本硬编码单一状态语义 | 过滤脚本只认 `reviewed`，漏掉 enriched 卡片或把 decision 的 stable 卡片当成已审 | 改为按文件类型分支；用显式枚举常量；添加覆盖 enriched/superseded/stable/needs-review 的单元测试 |
| 归因偏差：把设计冲突当执行问题 | 讨论结论变成"加强 schema enforcement"，准备删 enriched 值或强制改写 | 重新审视是否存在第二状态机；若存在，拆分字段或在 schema 中保留双枚举并注明适用范围 |
| 外部集成未被告知双语义 | 第三方工具同步 KDO 卡片后，`status` 字段解析报错或逻辑错误 | 在接口文档写明 `status` 的双重语义；提供映射表；考虑对外暴露拆分后的字段 |
| Schema 升级时未迁移历史数据 | 拆分字段后，旧 `.md` 文件的 `status` 值被误读为 `approval_status` | 升级脚本必须按原文件类型映射旧 `status` 到新字段；升级后全量校验 |

## 落地模板：双状态机排查 Checklist

**适用时机**：新增/修改 schema、写自动化脚本、做 schema 升级、对接外部系统前。

- [ ] 已列出项目里所有使用 `status` 字段的文件类型（`.md` / `decision.yaml` / `task.yaml` / 其他）
- [ ] 已确认每类文件的 `status` 对应哪条状态机，并画出状态转移图
- [ ] 已在 schema/代码注释中显式声明双状态机的存在和各自取值范围
- [ ] 已检查所有读取 `status` 的脚本，按文件类型分支或使用不同的枚举常量
- [ ] 已为过滤/统计逻辑补单元测试，覆盖 `enriched`、`superseded`、`stable`、`needs-review` 等边界值
- [ ] 已检查对外接口文档，说明 `status` 的双重语义或已改用拆分后的字段名
- [ ] （如做 schema 升级）已制定历史数据迁移脚本，并按文件类型映射旧 `status` 到新字段
- [ ] 升级后已运行全量 `kdo validate` 与 `yaml.safe_load()` 校验

## 为什么值钱

- 这是 KDO 特有的 schema 设计债务：**两个状态机共用同一个字段名**。任何外部 AI 训练语料都不会有这条具体知识
- 症状极具迷惑性：`enriched` 看起来像个合法的进度描述，Architect 会误判为"Schema 写了但没严格执行"，而不是"设计冲突"——这种归因偏差会导向错误的修正方向（加 enforcement 而不是拆分字段）
- 揭示了 schema 演进中的经典陷阱：早期系统只有一个状态机，后期叠加第二个子系统时为了"兼容"没有 rename，结果产生语义污染
- 通用软件工程原则（"命名要清晰"）谁都知道，但"什么时候必须把字段拆分"这条边界判断——特别是"共存方案的成本 vs 拆分方案的成本"——只有踩过坑才有体感

## 与其他知识的关联

- [[dk-c10-batch-tool-no-dry-run]] — 同一深层模式：系统设计中"一个组件承担两种语义"导致的级联故障。C-10 是工具（scaffold）同时兼容新旧格式失败，C-2 是字段（status）同时承载两种状态机失败
- [[dk-p18-yaml-parser]] — 同一领域：frontmatter/YAML 处理中的设计债务。P-18 暴露了手写解析器对嵌套结构的破坏；C-2 暴露了同一字段名承载两种语义的污染。两者共同说明"对 frontmatter 的轻率处理会级联放大"
- [[kdo-yaml-frontmatter-safety]] — 操作层面的防御指南：如何安全地读写 YAML frontmatter、如何做 round-trip 校验，避免在修复 C-2 的过程中引入新的数据损坏
- [[master-systems-thinking]] — 系统思维中的"边界清晰度"原则：两个独立子系统共用同一资源（字段名）时，边界模糊会导致涌现性故障。C-2 是这一原则在 schema 设计中的具体体现
- `20_memory/corrections.md` → C-2（原始记录）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
