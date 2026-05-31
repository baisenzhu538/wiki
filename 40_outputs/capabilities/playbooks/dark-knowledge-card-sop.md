---
id: dark-knowledge-card-sop
title: "SOP：暗知识卡生产工作流（老顽童用）"
type: capability
subtype: playbook
status: draft
domain:
  - master
tags:
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
created_at: 2026-05-31
updated_at: 2026-05-31
target_user: 老顽童（Producer）
source_refs:
  - plan_20260531_data-curator-v1.3
  - data-curator-role-division
  - dark-knowledge
---

# SOP：暗知识卡生产工作流

> **写给老顽童**：这份 SOP 教你从一条原始纠偏记录，一步步生产出一张合格的暗知识卡。
> **前置阅读**：`30_wiki/decisions/three-party-data-alignment.md`（了解为什么暗知识 ≠ 三步编译法）
> **参考样例**：`30_wiki/concepts/dk-c10-batch-tool-no-dry-run.md` 和 `dk-c8-format-complete-mind-empty.md`

---

## 一、核心区别：暗知识卡 ≠ 概念卡

| | 概念卡（你以前做的） | 暗知识卡（现在新加的） |
|------|-------------------|---------------------|
| **模板** | 三步编译法（Condense→Question→Synthesize） | **六字段模板**（原始表述→使用场景→操作方法→适用边界→为什么值钱→关联） |
| **目标** | 提取稳定知识（结论、边界、关联） | **捕获暗知识**（过程、工具用法、失败记录、体悟） |
| **type** | concept / tool / framework | **dark-knowledge** |
| **特殊字段** | domain, related, reviewed_by | **+ source_person, source_context, dark_knowledge_type** |

**记住一句话**：概念卡回答"这个知识是什么"。暗知识卡回答"这个坑怎么踩的、怎么避开、为什么值钱"。

---

## 二、素材来源（一期全部来自现有文件）

所有素材都在 vault 里，不需要翻 inbox 找新东西：

| 素材 | 位置 | 数量 | 产出类型 |
|------|------|:--:|---------|
| corrections.md | `20_memory/corrections.md` | 12 条 | `dark_knowledge_type: failure` |
| failure-modes.md | `90_control/failure-modes.md` | 22 种 | `dark_knowledge_type: failure` |
| pitfalls.md | `.agent/pitfalls.md` | 15 条 | `dark_knowledge_type: failure` |

---

## 三、操作步骤（以 C-10 为示例）

### Step 1：读原始素材

打开 `20_memory/corrections.md`，找到 C-10 条目。确认它包含六个关键信息：
- 时间、报告人
- 症状（发生了什么）
- 根因（为什么发生）
- 修正（怎么修的）
- 关联失败模式
- 再犯后果

**如果原始条目缺少关键信息**（比如缺少"再犯后果"），不要编。在卡片里标 `[原始记录未提供]`。

### Step 2：拆解为六字段

对照原始条文，逐字段填充：

#### 字段 1：原始表述
> 直接引用原文。不要改写、不要浓缩。这是"证据"。

**C-10 示例**：
```
黄药师交付了 kdo scaffold，老顽童直接跑 kdo scaffold --batch B --write 对 71 张卡批量操作。
结果：scaffold 的 _count_external_attacks 只认 ## Critique H2 节，不认旧格式...
~140 个精心研究的攻击段落全部丢失。但更可怕的是：kdo validate --v15 给空壳卡打了 PASS。
```

**检验标准**：读者读完这段话，能不能感受到事故的严重性？

#### 字段 2：使用场景
> 什么时候需要用到这条暗知识？不要泛化，要具体场景。

**C-10 示例**：
```
- 你刚修改了 KDO CLI 的某个批量写入工具，准备对多张卡运行
- 你正在设计一个新的自动化管线脚本，它会对卡片内容做修改
- 你审查别人的批量操作提案时，需要快速判断它是否会重蹈 C-10
```

**常见错误**：写成"做批量操作时"——太泛了。要具体到"谁、在什么情况下、做什么操作前"。

#### 字段 3：操作方法
> 步骤级。**检验标准：另一个人读完能照着做出来。** 不要抽象成"原则"。

**C-10 示例（✅ 合格）**：
```
1. dry-run 单卡：新工具先在 1 张卡上 --dry-run，确认 diff 符合预期
2. write 单卡：--write 写入 1 张卡，逐字段检查内容是否被破坏
3. validator 验证：跑 kdo validate 确认通过
4. 人工审查内容：人读一遍卡片正文，确认内容未被破坏
5. 再考虑批量：以上四步全部通过后，才允许 --batch N --write
```

**C-10 示例（❌ 不合格——太抽象了）**：
```
先单卡验证再批量。
```
——"怎么验证？验证什么？多少张算单卡？"全是问号。

#### 字段 4：适用边界
> 什么时候不适用？反例是什么？前提条件是什么？

**C-10 示例**：
```
- 适用于所有会修改卡片正文内容的工具
- 不适用于只读操作（audit、lint、validate、query）
- 即使工具"只是加字段""只是修格式"，也必须走流程——C-10 的 scaffold 也只是"加 Critique section"，结果覆盖了已有内容
```

**常见错误**：写成"本方法有局限性"。这是废话。要写出具体的反例场景。

#### 字段 5：为什么值钱
> 为什么 AI 训练语料里没有这条？为什么有了它能给 AI 产出带来质的提升？

**C-10 示例**：
```
- 这是 KDO 历史上最严重的内容破坏事故——71 张卡、~140 个攻击段落、一次操作全部丢失
- 根因链条揭示了三个叠加漏洞：工具缺陷 + 流程缺陷 + 校验缺陷
- 任何 AI 训练语料中都不存在"KDO 的 scaffold 因为不认旧格式而覆盖了 Taleb 的攻击段落"
- C-10 的教训具有强迁移性：任何自动化内容修改工具，必须先单卡验证再批量。无一例外。
```

**关键问题**：这条知识在互联网上搜得到吗？如果搜不到，它就是暗知识。如果搜得到（比如通用项目管理原则），它就不值钱。

#### 字段 6：与其他知识的关联
> 链接到概念卡和其他暗知识卡。**单向**：暗知识卡 → 概念卡。概念卡不需要反向链接。

**C-10 示例**：
```
- [[dk-c8-format-complete-mind-empty]] — 同一模式
- [[master-decision-hygiene]] — C-10 的"先单卡后批量"类比 Step 3（独立评估）
```

### Step 3：写 frontmatter

参考样例卡 `dk-c10-batch-tool-no-dry-run.md` 的 frontmatter。必填字段：
- `type: dark-knowledge`
- `dark_knowledge_type: failure`（纠偏类统一用这个）
- `source_person`（原报告人）
- `source_context`（原始记录的时间+场景）
- `source_refs`（指向 corrections.md 原文）
- `tags`：至少包含 `#source_type/error` + domain tag + method tag

### Step 4：保存文件

文件命名：`dk-c{N}-{简短英文slug}.md`
保存位置：`30_wiki/concepts/`

例：`dk-c10-batch-tool-no-dry-run.md`

### Step 5：提交审查

完成后在卡片末尾 append：
```
## 老顽童疑问（日期）
[如有疑问写在这里，如无则写"无疑问，请欧阳锋审查"]
```

欧阳锋审查后会在此 append 回应。

---

## 四、合格自检清单

写完后自己先过一遍，全部打勾再提交：

| # | 检查项 | 标准 |
|:--:|--------|------|
| 1 | 原始表述 | 是否直接引用了原文？（不是改写） |
| 2 | 使用场景 | 是否具体到"谁、在什么情况下、做什么操作前"？（不是泛化描述） |
| 3 | 操作方法 | 是否步骤级？（另一个人读完能照着做） |
| 4 | 适用边界 | 是否有具体反例？（不是"本方法有局限性"） |
| 5 | 为什么值钱 | 是否说清楚了"互联网上搜不到"的原因？ |
| 6 | 关联 | 是否至少链接了 1 张概念卡 + 1 张暗知识卡？ |
| 7 | frontmatter | type=dark-knowledge, dark_knowledge_type=failure, source_person 和 source_context 已填 |
| 8 | 文件名 | 格式：`dk-c{N}-{slug}.md` |

---

## 五、参考：第一批任务清单

| 素材 | 产出 | 预估工作量 |
|------|------|:--:|
| C-1（enrich 中文 regex 静默失败） | `dk-c1-cjk-regex-silent-fail.md` | 15min |
| C-2（Schema status 混用两个状态机） | `dk-c2-dual-status-machine.md` | 15min |
| C-3（.txt 被 ingest 静默跳过） | `dk-c3-txt-ingest-skip.md` | 10min |
| C-4（自检误报 superseded） | `dk-c4-selfcheck-superseded.md` | 10min |
| C-5（TODO 字符串匹配过宽） | `dk-c5-todo-false-positive.md` | 10min |
| C-6（大源文件 session 超载） | `dk-c6-large-source-overflow.md` | 15min |
| C-7（Obsidian auto-backup 干扰 commit） | `dk-c7-auto-backup-conflict.md` | 10min |
| C-8 | ✅ 已完成（黄药师） | — |
| C-9（批处理 query_triggers 垃圾） | `dk-c9-batch-trigger-garbage.md` | 15min |
| C-10 | ✅ 已完成（黄药师） | — |
| C-11（洪七公跳步三次提报跳过） | `dk-c11-hongqigong-skip-review.md` | 15min |

**节奏**：每次领 ≤ 3 条，做完一批提交审查。不贪多。

---

*黄药师 · 2026-05-31*
