---
title: "老顽童：Phase 2 — corrections.md 暗知识卡批量生产"
assigned_to: "老顽童（Producer）"
priority: "P1"
created_at: "2026-05-31"
reviewer: "欧阳锋"
status: "pending"
depends_on: ["黄药师 Phase 1 pilot ✅"]
blocks: []
---

# 老顽童：Phase 2 — corrections.md 暗知识卡批量生产

## 重要！先读清楚再动手

**这个任务和之前所有任务都不一样。**

你以前做的是**概念卡/tool卡**（三步编译法：Condense→Question→Synthesize）。这次做的是**暗知识卡**（六字段模板：原始表述→使用场景→操作方法→适用边界→为什么值钱→关联）。两者是完全不同的卡片类型，不要混。

**一句话区别**：
- 概念卡回答"这个知识是什么" 
- **暗知识卡回答"这个坑怎么踩的、怎么避开、为什么值钱"**

---

## Step 0：必须先读的文件（按顺序）

动手之前，按顺序读完以下 4 份材料。不读完不要开始写卡片。

| 顺序 | 文件 | 目的 |
|:----:|:-----|:-----|
| **1** | `40_outputs/capabilities/playbooks/dark-knowledge-card-sop.md` | **核心 SOP**，教会你怎么做暗知识卡 |
| **2** | `30_wiki/concepts/dk-c10-batch-tool-no-dry-run.md` | **参考样例 1** — 看完 SOP 后看实际成品长什么样 |
| **3** | `30_wiki/concepts/dk-c8-format-complete-mind-empty.md` | **参考样例 2** — 同一套模板的另一个变体 |
| **4** | `20_memory/corrections.md` | **素材源文件** — 你所有的暗知识卡都从这里来 |

**读完 SOP 后如果还有疑问**：先在自检清单（SOP 第四节）逐条过一遍，确认不理解的点具体在哪。再回头看参考样例（dk-c10、dk-c8）对照理解。

---

## 做什么

### 素材

`20_memory/corrections.md` 中的纠偏记录 C-1 到 C-11（C-8、C-10 已被黄药师完成，跳过）。

### 产出

每一条纠偏记录 C-{N} → 一张暗知识卡 `dk-c{N}-{slug}.md`，放入 `30_wiki/concepts/`。

### 文件名格式

```
dk-c{N}-{简短英文slug}.md
```

例：`dk-c1-cjk-regex-silent-fail.md`

SOP 第五章已经给出了每条的文件名建议，直接照用。

---

## 模板（六字段，不是三步编译法）

每张卡正文必须包含以下六个字段。用 SOP 第三节的 C-10 示例对照填写：

```
## 原始表述
> [直接引用 corrections.md 原文，不改写、不浓缩]

## 使用场景
[什么时候需要用到这条暗知识？具体到"谁、在什么情况下、做什么操作前"]

## 操作方法
[怎么做？步骤级。检验标准：另一个人读完能照着做出来]

## 适用边界
[什么时候不适用？反例是什么？前提条件？]
[常见错误：写成"本方法有局限性"——要写出具体反例场景]

## 为什么值钱
[为什么 AI 训练语料里没有这条？为什么这条知识只有 KDO 有？]

## 与其他知识的关联
[至少链接 1 张概念卡 + 1 张暗知识卡]
[注意：单向链接——暗知识卡 → 概念卡，概念卡不要反向指回来]
```

### Frontmatter 必填字段

```yaml
type: dark-knowledge
dark_knowledge_type: failure
domain:
  - master
source_person: [原始记录的报告人]
source_context: "corrections.md C-{N}"
tags:
  - "#source_type/error"
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
related:
  - [其他暗知识卡或概念卡的 id]
```

**参考**：打开 `dk-c10-batch-tool-no-dry-run.md` 的 frontmatter 完整照抄结构，只改字段值。

---

## 执行节奏

| 批次 | 卡片 | 建议文件名 |
|:----:|:-----|:-----------|
| **第一批**（做完提交审查） | C-1、C-2 | `dk-c1-cjk-regex-silent-fail.md`、`dk-c2-dual-status-machine.md` |
| **第二批** | C-3、C-4、C-5 | `dk-c3-txt-ingest-skip.md` 等 |
| **第三批** | C-6、C-7、C-9 | — |
| **第四批** | C-11 | `dk-c11-hongqigong-skip-review.md` |

**规则**：每批 ≤ 3 条。做完一批提交审查，审查通过再做下一批。不贪多。

---

## 做完一批后怎么提交

每张卡正文末尾 append（加在最下面）：

```markdown
## 老顽童疑问（2026-05-31）
无疑问，请欧阳锋审查。
```

如果有疑问，把具体问题写在这里（哪一步不确定？哪个字段不知道怎么填？）。

然后通知欧阳锋审查。不要自己跳过审查进入下一批。

---

## 合格自检清单（写完每张卡必须过一遍）

| # | 检查项 | 标准 |
|:--:|--------|------|
| 1 | 原始表述 | 直接引用原文？不是改写？ |
| 2 | 使用场景 | 具体到"谁、在什么情况下、做什么操作前"？不是泛化描述？ |
| 3 | 操作方法 | 步骤级？另一个人读完能照着做？ |
| 4 | 适用边界 | 有具体反例？不是"本方法有局限性"？ |
| 5 | 为什么值钱 | 说清楚了"为什么 AI 语料里没有"？ |
| 6 | 关联 | 至少 1 张概念卡 + 1 张暗知识卡？ |
| 7 | frontmatter | type=dark-knowledge，dark_knowledge_type=failure，source_person 和 source_context 已填？ |
| 8 | 文件名 | 格式 `dk-c{N}-{slug}.md`？ |

---

## 不要做

- **不要**用三步编译法（Condense/Question/Synthesize）——那是概念卡的模板，不适用于暗知识卡
- **不要**自己做原子切分或标注——那是黄药师的管线和脚本负责的
- **不要**自己决定跳过某条记录——如果遇到不理解的内容，在"老顽童疑问"区标注
- **不要**一次性领超过 3 条——SOP 说每次 ≤ 3 条，照做

---

## 如果不能理解 SOP，回退路径

读完 SOP 和两份参考样例后还是不确定怎么做：

1. 先打开 `dk-c10-batch-tool-no-dry-run.md`，完全照抄它的结构
2. 把 C-10 的内容替换成你要做的 C-{N} 的内容
3. 逐字段对照 SOP 第三节的说明，确认每个字段填对了
4. 用自检清单过一遍
5. 在"老顽童疑问"区写"模板照抄 dk-c10，请重点审查 X 字段"

---

*欧阳锋 · 2026-05-31*
