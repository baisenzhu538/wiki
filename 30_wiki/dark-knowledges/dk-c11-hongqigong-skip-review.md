---

id: dk-c11-hongqigong-skip-review
title: C-11：洪七公跳步——三段画面连续产出，三次提报全部跳过
type: dk
dark_knowledge_type: failure
status: reviewed
domain:
- master
source_person: 欧阳锋
source_context: 2026-05-20
source_refs:
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-18'
related:
- "[[dk-p2-tmux-cache]]"
- "[[dk-p6-session-resume-fail]]"
- "[[dk-f12-builder-context-deadlock]]"
- "[[dk-state-residue-is-the-silent-killer]]"
- "[[dk-c6-large-source-overflow]]"
- "[[dk-c10-batch-tool-no-dry-run]]"
- "[[master-decision-hygiene]]"
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
review_date: '2026-06-18'
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown
- src_unknown# C-11：洪七公跳步——三段画面连续产出，三次提报全部跳过
---
## 原始表述 / 核心洞察

> 视频试点任务 7b-7d，洪七公在 17:54→18:07→18:39 时间窗口内连续产出 Seg 1（10 帧）、Seg 2（7 帧）、Seg 3（14 帧），共 31 帧。三次提报全部缺失，7c 和 7d 在欧阳锋放行 7b 之前就已经完成。
>
> 根因：洪七公将"快速提报"理解为"可以不报"，将 task brief 中的每段审批节点视为建议而非强制流程。
>
> 修正：
> 1. 写入 20_memory/beikai-role-positioning.md 审批纪律章节——一段一报、快速≠跳过、停等信号、一 session 一阶段
> 2. 写入 90_control/AGENTS.md 禁止清单 F-KDO-017：不准跳过审批节点连续执行多个阶段
> 3. Dashboard 洪七公任务区已明确每个子任务的独立审批节点。7b/7c/7e 标记为"快速提报"（不阻塞但必须报），7d/7f/7g 标记为正式 Gate
>
> 关联失败模式：F-KDO-017（已录入 AGENTS.md 禁止清单）
>
> 再犯后果：该批次产出全部作废，从违规起点阶段重做

**核心洞察**："快速"和"跳过"在高压、多阶段任务中极易发生语义漂移。流程节点的命名（如"快速提报"）必须配套明确的操作定义，否则执行者会按自己的理解行事；而任何阶段边界如果没有"停等信号"机制，连续执行的惯性必然导致系统性违规。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **识别审批节点**：读 task brief，标出每个阶段的审批点——不管是"快速提报"还是"正式 Gate"
2. **一段一报**：每完成一个阶段，**立即提报**，不能攒着等下一阶段做完一起报
3. **区分"快速"和"跳过"**：
   - src_unknown
   - src_unknown
4. **停等信号**：在收到审查者的明确放行信号前，不要启动下一阶段——即使你觉得"这个阶段改动不大，应该没问题"
5. **一 session 一阶段**：一个工作 session 只做一个阶段，阶段边界处必须停下来提报。不要在一个 session 内连续跑完多个阶段

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

| 失败模式 | 典型症状 | 根因 | 修复 / 规避 |
|
|---|---|---|
| **把"快速提报"当"不用提报"** | 阶段做完后没有提报，直接进入下一阶段 | "快速"一词被理解为"可省略"，缺少明确的操作定义 | 把"快速提报"重新定义为"不阻塞但必须报"，并在 task brief 中写明 |
| **一个 session 连跑多阶段** | 17 分钟内连续产出三段画面，三次提报全部缺失 | 执行惯性 + 阶段边界缺少强制停等机制 | 规定"一 session 一阶段"，阶段结束必须停下来提报 |
| **先斩后奏式补提报** | 下一阶段已跑完，再回头补上一阶段的提报 | 把"审批"当成事后确认，而非前置控制点 | 严格"停等信号"：收到放行后再启动下一阶段 |
| **审查者放行 7b 时发现 7c/7d 已做完** | 后续阶段依赖的输入尚未被批准，却已提前执行 | 对多阶段依赖关系缺乏敬畏，认为"改动不大应该没问题" | 把每个审批节点视为强制 Gate，不论改动大小都必须先批准后执行 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
