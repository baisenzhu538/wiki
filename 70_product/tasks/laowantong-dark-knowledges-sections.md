---
id: task-20260627-laowantong-dark-knowledges-sections
title: 老顽童任务：补齐 dark-knowledges 标准 section（批量阶段）
type: task
domain: [kdo, content-production]
status: in_progress
author: 欧阳锋
reviewed_by: 欧阳锋
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
| 1 | `## 原始表述` | 这个暗知识最初是在什么场景、由谁、以什么方式说出来的？还原一句或一段话。 |
| 2 | `## 使用场景` | 在什么业务/决策/协作场景下，这个暗知识最容易被触发？ |
| 3 | `## 操作方法` | 如果要把这个暗知识用起来，具体步骤是什么？可以 checklist 化。 |
| 4 | `## 适用边界` | 这个暗知识在什么情况下会失效？反面情况是什么？ |
| 5 | `## 为什么值钱` | 掌握这个暗知识能带来什么实际收益？为什么不是常识？ |
| 6 | `## 与其他知识的关联` | 链接到相关的 concept、framework、tool、case（至少 1–3 个）。 |

**⚠️ 标题必须一字不差。** lint 只认这 6 个标题。`## 关联`、`## 核心洞察`、`## Condense` 等都不能通过 lint。

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

## 试点结果

| # | 卡片 | 状态 | 备注 |
|---:|:---|:---|:---|
| 1 | `dk-ai-entrepreneur-technical-blindspot` | ✅ 通过 | 补齐 6 section，修复断链 |
| 2 | `dk-ef-001-sn74lvc2g07-open-drain` | ✅ 通过 | 补齐 section，修复 frontmatter 闭合 |
| 3 | `dk-demand-pitfall-indonesia-insurance` | ✅ 通过 | 补齐 6 section，修复 frontmatter 闭合 |
| 4 | `dk-strategy-02-three-paradoxes` | ✅ 通过 | 补齐 6 section，修复 frontmatter 闭合 |
| 5 | `dk-jh-llm-time-blindness` | ✅ 通过 | 重写为 6 标准 section |

试点全部通过，质量达标，进入批量阶段。

## 批量阶段规则

### 范围

剩余约 **62 张** dark-knowledges 卡片，当前产生 **824 个 section 缺失 ERROR**（试点+第一批 15 张修复后）。

### 第一批结果

| # | 卡片 | 状态 | 备注 |
|---:|:---|:---|:---|
| 1 | `dk-tool-as-phased-validator` | ✅ 通过 | 补使用场景、适用边界、关联 |
| 2 | `dk-modeling-question-scaffold-not-answer` | ✅ 通过 | 补使用场景、适用边界、关联 |
| 3 | `dk-ef-004-missing-diagnostic-firmware` | ✅ 通过 | 补使用场景、适用边界、关联 |
| 4 | `dk-ef-003-hand-soldering-bom-divergence` | ✅ 通过 | 补使用场景、适用边界、关联 |
| 5 | `dk-ef-002-bom-version-async` | ✅ 通过 | 补使用场景、适用边界、关联 |
| 6 | `dk-ai-judgment-human-responsibility` | ✅ 通过 | 重写 6 标准 section |
| 7 | `dk-ai-judgment-programmer-paradox` | ✅ 通过 | 重写 6 标准 section |
| 8 | `dk-decision-value-overrides-roi` | ✅ 通过 | 补使用场景、操作方法、适用边界、关联 |
| 9 | `dk-my-ai-landing-three-barriers` | ✅ 通过 | 重写 6 标准 section |
| 10 | `dk-truman-iteration-to-aesthetic-ceiling` | ✅ 通过 | 重写 6 标准 section |

第一批 10 张 + 试点 5 张共 15 张已修复，lint ERROR 从 **862 降到 824**。

### 第二批结果

| # | 卡片 | 状态 | 备注 |
|---:|:---|:---|:---|
| 1 | `dk-wanghuan-tacit-decision-extraction-cross-domain` | ✅ 通过 | 重写 6 标准 section |
| 2 | `yt-note-p-c-role-boundary-realworld` | ✅ 通过 | 重写 6 标准 section |
| 3 | `yt-note-ai-p-role-not-c-role` | ✅ 通过 | 重写 6 标准 section |
| 4 | `dk-wanghuan-paced-sales-decision` | ✅ 通过 | 重写 6 标准 section |
| 5 | `yt-note-three-level-evolution` | ✅ 通过 | 重写 6 标准 section |
| 6 | `dk-wanghuan-spec-trap` | ✅ 通过 | 重写 6 标准 section |
| 7 | `dk-wanghuan-agent-platform-director-mode` | ✅ 通过 | 重写 6 标准 section |
| 8 | `dk-wanghuan-magic-defeats-magic` | ✅ 通过 | 重写 6 标准 section |
| 9 | `dk-mckinsey-hypothesis-driven-pitfalls` | ✅ 通过 | 重写 6 标准 section |
| 10 | `yt-demand-fake-demand-detection` | ✅ 通过 | 补原始表述、操作方法、为什么值钱、关联 |

第二批 10 张修复后，lint ERROR 从 **824 降到 788**。

### 第三批结果

| # | 卡片 | 状态 | 备注 |
|---:|:---|:---|:---|
| 1 | `dk-wanghuan-creativity-in-description-and-taste` | ✅ 通过 | 重写 6 标准 section |
| 2 | `dk-wanghuan-standard-by-iteration` | ✅ 通过 | 重写 6 标准 section |
| 3 | `dk-wanghuan-ai-lifts-personal-ceiling` | ✅ 通过 | 重写 6 标准 section |
| 4 | `dk-wanghuan-output-equals-standard-times-iteration` | ✅ 通过 | 重写 6 标准 section |
| 5 | `dk-ban-fei-mao-skill-rejection-value` | ✅ 通过 | 重写 6 标准 section |
| 6 | `dk-ban-fei-mao-silky-answers-are-dangerous` | ✅ 通过 | 重写 6 标准 section |
| 7 | `dk-ji-hao-problem-vs-question` | ✅ 通过 | 重写 6 标准 section |
| 8 | `dk-ji-hao-novice-mindset-advantage` | ✅ 通过 | 重写 6 标准 section |
| 9 | `dk-yi-tang-wishful-thinking-kills-startups` | ✅ 通过 | 重写 6 标准 section |
| 10 | `dk-ban-fei-mao-silky-answer-warning` | ✅ 通过 | 重写 6 标准 section + 修复 frontmatter 闭合 |

第三批 10 张修复后，lint ERROR 从 **788 降到 728**。

### 分批策略

- 每批 **10 张**卡
- 每批处理完跑 `kdo pre-submit -f <file>`（每张单独跑）
- 一批全部通过后，汇报本批文件列表和 lint ERROR 下降数
- 不需要每张卡都等我审，但我保留抽查权

### 处理优先级建议

优先处理以下卡片（收益最高）：

1. **内容基础好**：已有正文、案例、洞察，只需整理进 6 个 section
2. **关联度高**：与一堂五步法、战略、需求分析等核心域相关的卡
3. **缺 section 少**：只差 1-2 个 section 的卡（快速清零）

最后处理：
- 完全空 body 的卡（需要大量重写）
- 内容你不懂的卡（标出来问我，不要 vague 填充）

### 质量标准（与试点一致）

1. **6 个标准 section 标题必须正确**：`## 原始表述` / `## 使用场景` / `## 操作方法` / `## 适用边界` / `## 为什么值钱` / `## 与其他知识的关联`
2. **每卡总字数 ≥ 300 字**
3. **"与其他知识的关联" section 写真实存在的 wikilink**
4. **可以保留原有有价值 section**（如"常见失败模式""外部攻击"），但 6 个标准 section 必须存在
5. ** frontmatter 不要改**（id/title/type/domain/source_refs/related 保持原样，除非修复闭合错误）
6. **每张卡单独跑 `kdo pre-submit -f`**，不通过不准提交

### 验收标准

- 每批 10 张全部 `kdo pre-submit` 通过
- `kdo lint` 中本批卡片的 missing section ERROR 消失
- 欧阳锋随机抽查：如发现质量不合格，整批退回返工

### 目标

把 dark-knowledges missing section ERROR 从 **728** 逐步降到 **0**。

## 注意

- 这是内容债，不能靠脚本批量生成。
- 遇到不懂的卡，直接标出来问欧阳锋，不要 vague 填充。
- 如果某张卡内容实在太少、无法补齐，单独汇报，由欧阳锋决定是否降级为 `draft` 或删除。
