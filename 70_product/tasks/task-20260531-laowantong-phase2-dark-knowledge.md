---
title: "老顽童：Phase 2.2 — failure-modes.md 暗知识卡批量生产"
assigned_to: "老顽童（Producer）"
priority: "P1"
created_at: "2026-05-31"
reviewer: "欧阳锋"
status: "pending"
depends_on: ["Phase 2.1 — corrections.md ✅ 审查通过"]
blocks: []
---

# 老顽童：Phase 2.2 — failure-modes.md 暗知识卡批量生产

## Phase 2.1 完成状态

corrections.md 全部 11 张暗知识卡（C-1 到 C-11）已全部通过审查。SOP 已跑通。

**模板和方法你已经完全掌握。** 接下来换素材源，做法一模一样。

---

## 素材源

`90_control/failure-modes.md` → 22 种 KDO 失败模式。

**位置**：`C:\Users\Administrator\Desktop\wiki\90_control\failure-modes.md`

**与 corrections.md 的区别**：

| 维度 | corrections.md | failure-modes.md |
|:----|:---------------|:-----------------|
| 内容 | 具体事故记录（何时、何地、发生了什么） | 抽象失败模式（什么条件下、什么类型的问题会反复出现） |
| 编号 | C-1 到 C-11 | F-KDO-001 到 F-KDO-022 |
| 每条结构 | 时间→报告人→症状→根因→修正→关联→再犯后果 | 触发条件→表现→根因→防御→关联→严重度 |
| 产出文件名 | `dk-c{N}-{slug}.md` | `dk-f{N}-{slug}.md` |
| 产出 dark_knowledge_type | `failure` | `failure`（不变） |
| source_person | 原始报告人 | **system**（失败模式是系统级归纳，非个人） |
| source_context | "corrections.md C-{N}" | **"failure-modes.md F-KDO-{N}"** |

**核心差异**：corrections 是"某个人某天踩了一个具体的坑"，failure-modes 是"这类坑反复出现，归纳成了一种模式"。写卡时，"原始表述"字段需要包含触发条件和具体表现，比 corrections 多一层概括。

---

## 参考样例

SOP 和之前的 dk-c* 卡仍然是参考，但最直接的参考是这一条已有卡片：

- `dk-c10-batch-tool-no-dry-run.md` — C-10 在 corrections 中就有对应的失败模式：`F-KDO-014`（不准擅自运行批量写入命令）。**注意：failure-modes 卡和 corrections 卡是互相补充的，不是互相替代**。C-10 仍然存在，F-KDO-014 是它的模式化版本。

**做法**：打开 failure-modes.md，阅读每条失败模式的完整内容。每条 F-KDO-{N} 产出一张 `dk-f{N}-{slug}.md`。

---

## 文件名格式

```
dk-f{N}-{简短英文slug}.md
```

其中 {N} 是 failure-modes.md 中的编号。例：
- F-KDO-001 → `dk-f1-regex-on-cjk.md`
- F-KDO-002 → `dk-f2-txt-ingest-skip.md`

---

## Frontmatter（对照 corrections 版的差异）

```yaml
type: dark-knowledge
dark_knowledge_type: failure
domain:
  - master
source_person: system          # ← 不同：模式归纳，非个人
source_context: "failure-modes.md F-KDO-{N}"  # ← 不同：指向 failure-modes
tags:
  - "#source_type/error"
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
related:
  - [对应的 dk-c* 卡或其他概念卡]
```

**related 字段**：很多 F-KDO 条目文末有关联的 corrections 编号（如 `关联：C-10`），直接链到对应的 `dk-c{N}-{slug}` 卡。

---

## 六字段模板（不变，和 corrections 版一样）

```
## 原始表述
> [直接引用 failure-modes.md 原文，含触发条件和表现]

## 使用场景
[什么时候需要用到这条失败模式？具体到"谁、在什么情况下"]


## 操作方法
[怎么预防/怎么修复？步骤级]

## 适用边界
[什么情况下这条模式不适用？和哪些其他模式容易混淆？]

## 为什么值钱
[为什么 AI 训练语料里没有这条？为什么只有 KDO 有？]

## 与其他知识的关联
[至少链接 1 张概念卡 + 1 张关联的 dk-c* 卡]
```

---

## 执行节奏

22 种失败模式，分 7-8 批，每批 ≤ 3 条。

| 批次 | 条目 | 建议文件名 |
|:----:|:-----|:-----------|
| **第一批** | F-KDO-001、F-KDO-002、F-KDO-003 | `dk-f1-regex-on-cjk.md`、`dk-f2-txt-ingest-skip.md`、`dk-f3-protected-branch-forbidden.md` |
| **第二批** | F-KDO-004、F-KDO-005、F-KDO-006 | 依此类推 |
| **第三批** | F-KDO-007、F-KDO-008、F-KDO-009 | |
| **第四批** | F-KDO-010、F-KDO-011、F-KDO-012 | |
| **第五批** | F-KDO-013、F-KDO-014、F-KDO-015 | |
| **第六批** | F-KDO-016、F-KDO-017、F-KDO-018 | |
| **第七批** | F-KDO-019、F-KDO-020、F-KDO-021、F-KDO-022 | 最后一批 4 条 |

**规则不变**：每批做完 append "老顽童疑问" 区 → 通知欧阳锋审查 → 通过后做下一批。不贪多。

---

## 自检清单（和之前一样）

| # | 检查项 | 标准 |
|:--:|--------|------|
| 1 | 原始表述 | 直接引用原文？含触发条件和表现？ |
| 2 | 使用场景 | 具体到"谁、在什么情况下"？ |
| 3 | 操作方法 | 步骤级？另一个人读完能照着做？ |
| 4 | 适用边界 | 有具体反例或易混淆模式？ |
| 5 | 为什么值钱 | 说清楚了"为什么 AI 语料里没有"？ |
| 6 | 关联 | 至少 1 张概念卡 + 1 张关联的 dk-c* 卡（如有）？ |
| 7 | frontmatter | source_person=system, source_context="failure-modes.md F-KDO-{N}" |
| 8 | 文件名 | 格式 `dk-f{N}-{slug}.md`？ |

---

## 完成状态

| 阶段 | 素材 | 预估产出 | 状态 |
|:----:|:-----|:--------:|:----:|
| Phase 2.1 | corrections.md | 11 张 dk-c | ✅ 全部通过 |
| Phase 2.2 | failure-modes.md | 22 张 dk-f | 🔨 进行中 |
| Phase 2.3 | pitfalls.md | 15 张 dk-p | ⏳ 下一站 |

Phase 2.2 完成后不做三期的乱七八糟扫描。直接进 **Phase 2.3 — pitfalls.md**（15 条踩坑记录，`。agent/pitfalls.md`）。

**和 failure-modes 的区别**：
- source_person = `system`（不变）
- source_context = `"pitfalls.md P-{N}"`
- dark_knowledge_type = `failure`（不变）
- 文件名前缀 = `dk-p{N}-{slug}.md`
- 其他六字段模板完全一样

做完 Phase 2.3，一期结构化源全部入库（corrections 12 + failure-modes 22 + pitfalls 15 = **49 张暗知识卡**）。二期待黄药师萃取器就绪后再安排。

---

*欧阳锋 · 2026-05-31*
