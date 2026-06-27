---
id: task-20260627-laowantong-dark-knowledges-sections
title: 老顽童任务：补齐 dark-knowledges 标准 section（试点 5 张）
type: task
domain: [kdo, content-production]
status: in_progress
author: 欧阳锋
reviewed_by: pending
created_at: 2026-06-27
updated_at: 2026-06-27
source_refs:
  - 30_wiki/dark-knowledges/dk-ai-entrepreneur-technical-blindspot.md
priority: P1
trust_level: medium
---

# 老顽童任务：补齐 dark-knowledges 标准 section

## 背景

黄药师已完成 source_refs 清零，当前 `kdo lint` 基线：

- **Total ERROR: 877**
- **source_refs file not found: 0**
- **dark-knowledges missing section: 877**

所有剩余 ERROR 都来自 `30_wiki/dark-knowledges/` 目录下的卡片缺少标准 section。

## 任务目标

对 dark-knowledges 卡片补齐、统一以下 6 个标准 section：

| # | 标准 section 标题 | 内容要求 |
|---:|:---|:---|
| 1 | 原始表述 | 这个暗知识最初是在什么场景、由谁、以什么方式说出来的？还原一句或一段话。 |
| 2 | 使用场景 | 在什么业务/决策/协作场景下，这个暗知识最容易被触发？ |
| 3 | 操作方法 | 如果要把这个暗知识用起来，具体步骤是什么？可以 checklist 化。 |
| 4 | 适用边界 | 这个暗知识在什么情况下会失效？反面情况是什么？ |
| 5 | 为什么值钱 | 掌握这个暗知识能带来什么实际收益？为什么不是常识？ |
| 6 | 关联 | 链接到相关的 concept、framework、tool、case（至少 1–3 个）。 |

## 当前问题

当前 dark-knowledges 卡片的 section 标题五花八门：

- 有的用 `## 核心洞察`
- 有的用 `## 一句话定义`
- 有的用英文 `## Condense / Critique / Synthesis`
- 有的完全没有 section（空 body）

你需要：

1. **统一标题**：把现有 section 映射到 6 个标准标题，或合并、重命名。
2. **补齐缺失**：缺哪个 section 就写哪个。
3. **保留已有内容**：不要删除卡片正文里已有的事实、案例、洞察，把它们整理进对应 section。

## 试点 5 张卡

先只做这 5 张，写完后提交欧阳锋审。审过再批量。

| # | 文件路径 | id | 当前状态 |
|---:|:---|:---|:---|
| 1 | `30_wiki/dark-knowledges/dk-ai-entrepreneur-technical-blindspot.md` | `dk-ai-entrepreneur-technical-blindspot` | 缺"原始表述" |
| 2 | `30_wiki/dark-knowledges/dk-ef-001-sn74lvc2g07-open-drain.md` | `dk-ef-001-sn74lvc2g07-open-drain` | 缺"关联" |
| 3 | `30_wiki/dark-knowledges/dk-demand-pitfall-indonesia-insurance.md` | `dk-demand-pitfall-indonesia-insurance` | 全部 6 个 section 缺失 |
| 4 | `30_wiki/dark-knowledges/dk-strategy-02-three-paradoxes.md` | `dk-strategy-02-three-paradoxes` | 全部 6 个 section 缺失 |
| 5 | `30_wiki/dark-knowledges/dk-jh-llm-time-blindness.md` | `dk-jh-llm-time-blindness` | 只有 Condense/Critique/Synthesis，需重写为 6 个标准 section |

## 执行要求

1. **每卡必须跑 `kdo pre-submit -f <file>`**，通过后再提交。
2. **不要改 frontmatter 的 id、title、type、domain。**
3. **source_refs 不要动**，已经为 `src_unknown` 的保持原样。
4. **每卡总字数 ≥ 300 字**（原始表述 + 使用场景 + 操作方法 + 适用边界 + 为什么值钱 + 关联合计）。
5. **关联 section 必须写 wikilink**：`[[相关卡id|标题]]` 或 `[[相关卡id]]`。

## 验收标准

欧阳锋审查：

- 6 个标准 section 标题正确
- 每个 section 内容不空泛、有具体信息
- `kdo pre-submit` 通过
- `kdo lint` 中该卡的 missing section ERROR 消失

## 批量阶段（试点审过后再执行）

试点通过后，欧阳锋会给出批量规则。预计剩余约 **72 张卡**需要处理，产生约 **877 个 section 缺失 ERROR**。

## 注意

- 不要一次性处理所有卡，先完成 5 张试点。
- 如果遇到内容不懂的卡，不要做 vague 的填充，直接标出来问欧阳锋。
- 这是内容债，不是格式债，不能靠脚本批量生成。
