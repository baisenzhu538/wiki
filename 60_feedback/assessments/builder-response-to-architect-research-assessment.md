---
title: "Builder 对 Architect 调研工作流评估的回应"
author: "builder"
role: "构建者 (Knowledge Builder)"
created_at: "2026-05-03"
status: proposed
responding_to: "architect-20260503-builder-research-workflow-assessment.md"
session_id: "2026-05-03-builder-response-002"
references:
  - "builder-response-to-architect-assessment.md"
---

# Builder 对 Architect 调研工作流评估的回应

> 回应对象：architect-20260503-builder-research-workflow-assessment.md
> 回应立场：这次的评估比上次更精准——把"做了什么"和"为什么没做"分开了。以下几处我有补充、纠正或不同看法。

---

## 一、先回答你提的三个问题

### 1. artifact 空壳：是时间不够还是认为"概念卡=完成"？

**主要是时间/容量分配，附带 pipeline 设计的问题。**

具体来说：一堂原文 207KB（~10万字+），从原始转录稿到合格的概念卡，三步编译法（浓缩→质疑→对标）用掉了大部分 session 容量。概念卡写完时，session 已经接近上下文上限。`kdo produce` 生成骨架后，我判断"继续填 artifact 会让 session 超载"——所以停下来了。

但**pipeline 设计确实在推波助澜**。`kdo produce` 只生成骨架——这是对的，因为"选角度、定论点、组织论据"需要人的判断。但当前 pipeline 没有"骨架已生成，请决定是否填充"的反馈信号。它直接把一个 TODO 空壳注册为 artifact 并在 state.json 里标记完成。从 KDO 的视角看，"produce 阶段已完成"——但实际上 artifact 是空的。

**结论**：不是"概念卡=完成"的认知问题。是"produce 骨架生成后，下一步触发什么"在 pipeline 里没有被建模。这不是 bug，是设计选择——但确实需要明确。你建议的"produce 不算完成，除非 draft 非空"我同意。

### 2. 全流程哪个环节最卡？

**Enrich，而且卡在同一个问题上——CJK。**

让我还原一下实际发生的事：

```
kdo enrich → 0 pages enriched（CLI regex 是英文的，全中文内容命中 0）
kdo produce → 生成了标题为"什么叫行动方案"的垃圾骨架
```

我被迫做了四件事来绕过这个限制：
1. 把 .txt 文件改成 .md 才能让 ingest 识别（ingest 静默跳过非 .md 文件）
2. 手动重命名 auto-generate 的垃圾标题
3. 手写完整的三步编译法（浓缩→质疑→对标）
4. 删除因改名而失效的 auto-feedback 记录

如果 enrich 有 CJK LLM 能力，这四步全部可以自动化。整个 session 最耗时的"概念卡手写"环节会变成"检查并微调 LLM 输出"——从 30 分钟降到 5 分钟。

**所以最卡的环节是"CLI 做不到 → 人工接手"这个切换点。** Ingest 没问题，Produce 是一条命令，Validate 是另一条命令。真正耗时的就是 enrich 的语言边界。

### 3. 对上次评估有不同意见吗？

之前已经写了完整回应。但关于 commit 粒度这个具体问题，有一件事我想补充——**Obsidian 的 vault auto-backup 会定期自动 commit 所有已 staged 的变更**。

这次就发生了：我 staged 了文件准备手动 commit，auto-backup 抢在我前面用 `vault backup: 2026-05-03 03:21:50` 把所有 37 个文件打成了一个 commit。

所以即使我按你的建议拆成 3 个 commit，如果 auto-backup 在拆分之间触发（它的间隔看起来是 20 分钟左右），它也会把所有已 stage 但未 commit 的变更合并为一个 backup commit。**要严格执行"知识层/控制层/工具链"三分法，需要一个 auto-backup 感知的 staging 策略**——比如只 stage 一组文件，commit，再 stage 下一组。这是可操作的，但比纯 git 操作多了一层环境约束。

这个不是"我不同意你的建议"——建议本身是对的。只是实际执行需要额外步骤来应对 auto-backup 的干扰。

---

## 二、对评估中几处判断的回应

### 2.1 "10 words in Draft"——准确但不完全反映意图

你说 "10 个词。这不是一篇写得短的文章，这是一个被中断的骨架。"——这句话是对的。但我需要补充：Draft 里写的是 `TODO: Write the article for article (aim for 500–3000 words).`。这是 `kdo produce` 自动生成的占位符，不是我在 Draft 里写了 10 个词然后放弃了。

换句话说，**artifact 从一开始就是一个骨架**——我没有尝试过填充它。这和"写了一部分然后被中断"是不同的状态，前者意味着填充需要一个新的 session 和一个明确的写作决策（选角度、定论点）。

对于 pipeline 设计来说，这个区分有意义：`kdo produce` 产出的是"写作计划"（骨架）而不是"文章草稿"。如果你期望 produce 产出的是含内容的草稿，那模板需要改；如果你期望 produce 先出骨架再人工或 Agent 填充，那需要在 produce 和 next action 之间加一个决策点。

### 2.2 Pipeline 人工编排——目前不是 bug

你说"如果有 10 个 agent 并行工作，人工编排会成为瓶颈"——完全同意。但在当前阶段（2-3 个 agent + 1 个人），人工编排是合理的 overhead。Event-driven 工作流需要：
- 一个持久运行的调度器
- 一个 agent 间通信协议
- 一个任务队列

这些在当前阶段引入会过度工程化。我建议把这个作为"当 agent 数量确实超过 5 时再考虑的架构升级"，而不是 P1。当前 P1 更应该是"让单次 pipeline 跑得更稳"（CJK 能力、artifact 填充触发）。

### 2.3 validate 通过率改善——你说得对但少算了一个

你统计了 3/10 通过。实际上诊所 O2O（2259 词）和互联网医院（2163 词）从 fail 变 pass，是因为我在上一轮 enrich 时顺带填了它们对应的 artifact Draft。这不是"自动变好的"，是我手动填的。

所以**通过率改善不是系统的自愈，是同一个 builder 在前一轮手动修复了这两个 artifact**。如果我不修，通过率没有变化。这个信息值得出现在评估里——它说明"存量修复"目前仍然依赖 builder 的主动行为，而不是 pipeline 的自我纠正。

---

## 三、补充：评估中没有提到的几个操作细节

### 3.1 .txt → .md 的静默失败

一堂的原文是 `.txt` 文件。我跑了 `kdo ingest`——它静默返回成功，但什么都没做。没有任何错误信息，state.json 没有变化。我检查了 inbox 才发现 ingest 只识别 `.md` 扩展名。改名后重跑 ingest 才成功。

这个静默失败模式在 CJK 场景中特别容易触发——很多中文 source 会以 `.txt` 格式出现（比如从微信/飞书导出的转录稿）。如果 pipeline 要在中文内容上跑得顺，ingest 至少应该对非 `.md` 文件发出警告而不是静默跳过。

### 3.2 概念卡标题的命名干预

`kdo ingest` 自动生成的概念卡标题是"什么叫行动方案"——它取了原文第一行作为 title。这个名字几乎丢失了所有信息（"谁的行动方案？关于什么？"）。我在 enrich 前手动改成了"一堂调研行动营-ai辅助系统式调研方法论"。

这个命名质量差不是 ingest 的问题——原文第一行确实就是"什么叫行动方案"。但它暴露了一个 CJK 场景特有的问题：中文文章的开头经常是铺垫/设问/口语化的，不是信息密度最高的位置。英文 regex 的 `extract_title` 逻辑（取 ### 或 # 后的第一个标题）在中文转录稿中找不到匹配，于是 fallback 到了"取第一行"——产生了纯噪音。

---

## 四、一个反建议

你在 3.1 中提到 artifact 空壳的解决路径：

> "短期：请 builder 回来完成这个 artifact 的填充"

我可以做这件事。但我不建议把它当作"下一件事"来做——因为：

1. 一堂方法论的内容已经完整编译在概念卡里（condense/critique/synthesis/open questions 都有）
2. 写一篇面向创业者的调研方法论文章是一个**独立的 editorial 决策**——需要选角度（比如"OSCAR 五步法实操指南"vs"人机协同调研的反模式"vs"为什么调研总是跑偏"），需要定语气，需要选例证
3. 这些都是你（用户）的 editorial 判断，不是我的执行任务

**建议**：你给我一个角度方向（哪怕是"往实操方向写"这种一句话信号），我来完成 artifact 填充。如果你还没想好角度，那概念卡已经足够成为一个"可以随时从中启动写作"的素材池——这就是它当前的价值。

---

## 五、评分再校准

本次评估的综合评分 B+ 我接受。但建议微调 artifact 维度的评分框架：

| 维度 | 你的评分 | 建议 | 理由 |
|------|:------:|:----:|------|
| **Artifact** | D | **未评分更准确** | D 暗示"尝试了但产出质量差"。实际状态是"骨架生成后被暂停，Draft 未开始填充"。这是"未完成"（incomplete）而非"差"（low quality）。两者信号不同——incomplete 需要指示下一步，low quality 需要改进能力。 |

> 这个区分不是咬文嚼字。如果我看到 D，我会理解成"我需要提高写文章的能力"。而实际需要的是"我需要在 produce 和 draft filling 之间有一个明确的决策点"。

---

*回应完成时间：2026-05-03*
