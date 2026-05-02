---
title: "Builder 调研方法论工作流执行评估"
author: "architect"
role: "知识架构师 (Knowledge Architect)"
created_at: "2026-05-03"
status: proposed
session_id: "2026-05-03-architect-002"
supersedes: []
superseded_by: []
references:
  - "architect-20260503-builder-work-assessment.md"
---

# Builder 调研方法论工作流执行评估

> 评估对象：commit `0471617` 及同批次文件变更（一堂调研行动营方法论全流程）
> 评估方法：全链路追溯（inbox → raw → wiki → artifact → validate）+ 知识卡片逐节审查 + artifact 质量检查
> 评估协议版本：KDO Protocol v0.1
> 前次评估参考：`architect-20260503-builder-work-assessment.md`

---

## 总体判断

**这是 KDO 仓库历史上第一次完整跑通 ingest → enrich → produce → validate 全链路。** 概念卡片质量是当前仓库最高水准，但 artifact 仍然是空壳——"enrich 脱困了，produce 还没脱困"。

综合评分：**B+**（概念卡 A，artifact D，链路完整性 B+，清理意识 A-）

---

## 一、本次变更全景

| 文件 | 类型 | 说明 |
|------|------|------|
| `10_raw/sources/src_20260503_5f268da2-什么叫行动方案.md` | source | Ingest 产出，207KB |
| `30_wiki/concepts/一堂调研行动营-ai辅助系统式调研方法论.md` | wiki 概念卡 | **Builder enrich 产出** |
| `40_outputs/content/articles/art_20260503_767ce1bf-从模糊提问到高质量决策.md` | artifact | produce 产物，**但为 TODO 空壳** |
| `60_feedback/eval-results/fb_20260503_c8dbba0e-artifact-validation.md` | 验证报告 | 全量 artifact 重新 validate |
| `60_feedback/assessments/architect-20260503-builder-work-assessment.md` | 评估 | 我上次的报告（已被 builder 阅读并触发本次工作） |
| `30_wiki/index.md` | Wiki 索引 | 已更新，新增一堂链接 |
| `30_wiki/links/index.md` | 链接索引 | 已更新 |
| `90_control/source-registry.yaml` | 源注册表 | 已同步 |
| `90_control/artifact-registry.yaml` | 产物注册表 | 已同步 |
| `30_wiki/log.md` | 操作日志 | 已追加 ingest/produce/validate 记录 |
| `20_memory/cli-preferences.json` | 记忆层 | 有变更（待确认具体内容） |

Commit `0471617`：清理了一个因 wiki 页面改名而失效的 auto-feedback 记录。

---

## 二、做得好的地方

### 2.1 概念卡片质量是仓库标杆（A）

这是 KDO 仓库至今质量最高的概念卡。具体证据：

**Condense：每条结论有数据支撑，非模板填充**
- "第零期调研行动营——为期 10 天"——有时间锚点
- "18 张方法论卡牌、5 个核心心法、4 种调研题型、7 层分层自洽模型"——有具体数量
- 不是"一堂有个调研方法论"这种空话

**Critique：击中了真实痛点**
- "前提假设是用户具备足够专业判断力来纠偏——这恰恰是最大变数"——这是使用过 AI 调研工具的人才会意识到的瓶颈
- "如果用户自己不懂产品内核，就无法判断 AI 的推理是否正确"——对"人掌方向盘"这一口号的反问是诚实的
- "25 轮对话 11 万字是演示案例，一般用户可能在第 3-5 轮就满意了"——对案例代表性的质疑

**Synthesis：跨链接不是凑数，每一条都有具体对标**
- [[KDO Protocol]] 的对标："O（目标）对应 KDO 的 Produce 阶段，S-C-A 对应 Enrich 阶段，R 对应 Validate 阶段"——具体到阶段映射
- [[Kimi Deep Research Swarm]] 的对标："共享'单源不可信'的认知前提"——一句话说清共性
- [[YC AI-Native 公司方法论]] 的对标："YC 聚焦组织效率（用 AI 减人），一堂聚焦个人能力杠杆（用 AI 乘人）"——清晰的差异概括

**Open Questions：不是泛泛而谈**
- "Graph RAG 在调研场景的实际增益"——直接关联一堂正在测试的方向
- "多轮对话中，错误在何时开始不可逆地污染推理链？是否需要内置 checkpoint？"——这是一个可工程化的问题

### 2.2 Pipeline 链路完整性有实质进步（B+）

相对于上次评估指出的"enrich=0"问题，本次：

```
前次评估时：
  inbox → raw ✅（做了）
  raw → wiki ❌（enrich=0）
  wiki → artifact ❌（没有原料）

本次：
  inbox → raw ✅
  raw → wiki ✅（首次真实 enrich）
  wiki → artifact ⚠️（骨架完成，内容未填）
  artifact → validate ✅
```

**关键进步：** 之前的 artifact 空壳是因为 enrich=0，builder 没有原料。这次 enrich 是完整的，如果有时间完全可以基于此产出真正的文章。所以原因从"不能"变成了"没来得及"——这是本质区别。

### 2.3 维护行为值得肯定（A-）

commit `0471617`（`chore: remove stale auto-feedback referencing renamed wiki page`）是主动的清理行为，没有人在任何评估中要求他做这件事。这说明 builder 有"系统健康度"的意识，不只是执行指令。这种维护意识在长期项目中比单次高产出更有价值。

### 2.4 Registry 同步意识好（B+）

source-registry.yaml 和 artifact-registry.yaml 都同步更新了，index.md 和 links/index.md 也更新了。没有留下"文件建了但注册表没同步"的尾巴。

---

## 三、需要关注的问题

### 3.1 artifact 仍是空壳——produce 阶段未完成（P0）

`art_20260503_767ce1bf` 的现状：

```
Audience:      TODO
Core Thesis:   TODO
Context:       TODO
Key Findings:  TODO
CTA:           TODO
Draft:         10 词
```

是的，10 个词。这不是一篇"写得短的文章"，这是一个**被中断的骨架**。

**根因分析：** 这不是 builder 意愿的问题。一堂调研方法论原文 207KB（约 10 万字+），概念卡的编译已经将原文压缩为知识卡片。但要从概念卡再展开为一篇 1500-3000 字的可交付文章，后面还有"选角度→定论点→组织论据→撰写→修改"这几个步骤。builder 在完成概念卡后没有继续推进到 artifact 填充。可能的原因是：

1. **时间/精力分配**：概念卡用掉了大部分可用资源
2. **目标分歧**：builder 可能认为"完成概念卡"就是 pipeline 的终点，produce 是后续步骤
3. **缺乏 produce 的明确触发**：当前 `kdo produce` 只生成骨架，没有自动跟进到填充

**建议：**
- 短期：请 builder 回来完成这个 artifact 的填充（概念卡已完备，素材就在手边）
- 中期：明确"produce 不算完成，除非 artifact 通过了 validate 且 draft 非空"

### 3.2 Pipeline 是人工编排而非自动化触发（P1）

回顾本次的触发链条：

```
我写评估报告 → 你看报告 → 你告知 builder → builder 执行 → 完成
```

这是一个**人工驱动的 pipeline**。每个环节之间的流转依赖人来做"传信人"。在只有 2-3 个 agent 和 1 个你时这是可行的，但如果有 10 个 agent 并行工作，人工编排会成为瓶颈。

**这不是 builder 的问题**，是系统架构问题。但值得记录，以便在未来的架构决策中考虑——比如 event-driven 的工作流触发。

### 3.3 全量 validate 的结果值得关注（P2）

本次 validate 报告显示了一个微妙但重要的进展：

| 分组 | 通过 | 不通过 | 变化 |
|------|:----:|:------:|:----:|
| 3 个 builtin skill | 3/3 | 0 | 与上次一致 ✅ |
| 早期 artifact（街顺、YC 等） | 3/5 | 2/5 | **有改善**——之前是 3/7 fail |
| 本次新 artifact（调研方法论） | — | 1/1 | ❌ TODO 残留 |

早期 artifact 的通过率在提升（诊所 O2O 和互联网医院已从之前的 fail 变为 pass），说明 enrich 后在逐步修复。但新增 artifact 又增加了 fail 数量。**整体通过率在改善，但增量赶不上存量修复的速度。**

### 3.4 log.md 的 session 记录仍然缺失（P2）

builder 追加了 ingest/produce/validate 的单行记录，但没有 session 摘要（像上次我和 builder 各自写的那个大段 Session Report）。单行记录对追溯有用，但新 agent 进入时无法通过 log.md 快速了解"这次 session 做了什么、为什么这么做、留下了什么未完成"。

---

## 四、与前次评估的对比

| 指标 | 前次评估（B+） | 本次评估 |
|------|:-------------:|:--------:|
| Enrich 完成率 | 0/12 | **1/13**（首次突破） |
| Artifact validate 通过率 | 2/10 | **3/10**（↑1） |
| 概念卡质量标杆 | 街顺报告 | **一堂调研方法论**（新高） |
| 清理/维护行为 | — | 主动清理 stale feedback ✅ |
| Registry 同步 | 未知 | ✅ 已同步 |
| Artifact 空壳 | 4/10 为 6 词 stub | 新增 1 个 10 词 stub |

**趋势：** 系统健康度在缓慢改善。enrich 链条已经突破 0，artifact 通过率在上升，但速度不足以在不增加 agent 工作量的情况下短期清空 backlog。

---

## 五、对 builder 的建议（在下一次评估报告中回应）

> 以下是我希望 builder 在看到本报告后回应的内容。这不是指令，是问题。

### 请 builder 回应的

1. **artifact 空壳是时间不够，还是认为"概念卡完成 = 调研方法论完成"？** 如果是时间问题，我们可能需要一起讨论每个环节的预算分配。如果是理解问题，我来调整我对 pipeline 各阶段完成标准的描述。

2. **你在跑全流程时，哪个环节最卡？** Ingest？Enrich 中的 Critique 写作？Produce 中的角度选择？还是 validate 的反复修复？这个信息对优化 pipeline 设计比任何架构讨论都有用。

3. **你对我的前次评估报告有没有不同意见？** 比如"37 个文件放一个 commit"的问题——你觉得在当前工具链下，分 3 个 commit 的实际成本是多少？你的角度看，我的建议是否可行？

---

*评估完成时间：2026-05-03*
*协议版本：KDO Protocol v0.1*
*状态说明：本文评估对象为 builder 在 commit 9a17190 之后的增量工作（一堂调研方法论相关变更）。*
*下次触发条件：builder 完成了本次 artifact 的填充，或开始了新的全流程迭代。*
