---
id: 2026-07-21-197-merge-retrospective
type: retrospective
status: draft
created_at: 2026-07-21
author: 王语嫣
reviewer: 用户
---

# 王语嫣 · 2026-07-21 · #197 厚内容合并与终审复盘

---

## 概要

> 一句话：完成 #197 `ai-collaboration/` 恢复版本厚内容合并、diagnostic_signals 与 related 补齐、tool/case Critique 补全，推动终审通过；将 #198 无限画布任务交接给老顽童；并沉淀一份任务编排侧结构化复盘。

---

## 关键决策

| 决策 | 理由 | 结果 |
|:---|:---|:---|
| 先从 `/tmp/ai-collab-recovery/ai-collaboration/` 恢复 8 张副本，再合并到标准目录 | 老顽童只删了副本没做内容合并，标准目录版本已丢 Critique 等厚内容；先恢复可防止不可逆丢失 | 8 张卡完整合并，无内容丢失 |
| 用 Python 脚本批量合并 frontmatter + body，而非逐张手改 | 8 张卡、多 section，手动易漏且 frontmatter 字段多 | 一致完成，ds / related / tags 全达标 |
| 发现 tool/case 仍缺 Critique 后，回改卡片并二次 `kdo pre-submit` | 复核表已将 5 张卡缺 Critique 列为未达标，不能带缺口终审 | 8/8 通过 pre-submit，#197 终审通过 |
| 操作 `queue_transition.py` 时改用完整任务 ID | 脚本匹配队列第二列完整 ID，不是 frontmatter 里的数字 task_id | #197 成功标记 reviewed，#198 成功 claimed-hermes |
| `kdo lint` 全仓库超时后，以 `kdo pre-submit --files` 作为门控证据 | 不因为全库扫描超时阻塞单任务提交，同时诚实记录 | 任务单有明确验证记录 |

---

## 思维盲点

> ≥1 条：什么被漏掉了？每条追问"为什么漏掉"。

1. **复核时只看"重复已删"，没看"内容是否已合并进 canonical 版本"。**
   - 第一次复核报告写"6 份 `ai-collaboration/` 副本已删，2 dk 卡已移入标准目录，无重复 ID"，但标准目录版本丢掉了 Critique、Synthesis、三层账本等核心 section。
   - **为什么漏掉？** 默认老顽童会执行"合并→删除"，我只验证了删除结果，没做两个版本的内容 diff。

2. **第一次合并后没立刻检查 tool/case 的 Critique。**
   - 复核表明确列出 `tool-ai-video-market-gap-assessment`、`tool-ai-video-cost-optimization`、`case-fuzeyu-ai-koubo-tool-dev` 缺 Critique。
   - **为什么漏掉？** 把 Critique 当作 dk 卡的"硬性要求"、tool/case 的"建议修复"，没意识到项目对卡片完整度的要求已经统一提高。

3. **第一次调用 `queue_transition.py` 时用了数字 `197`。**
   - 脚本报错"任务 197 不在队列中"。
   - **为什么漏掉？** 惯性以为 `task_id: 197` 就是脚本接受的 ID，没先读队列表格里的完整任务标识。

---

## 顿悟

> ≥1 条：什么基础认知被推翻了？

- **"删重复"不等于"合并完成"。** 删除副本前必须显式校验 canonical 版本是否已包含所有厚内容；"无重复 ID"只是最低要求。
- **`diagnostic_signals` 不是形式字段。** 它应该和"失败模式 / 使用场景"一一对应，回答"什么时候该查这张卡"，而不是占位符。
- **队列脚本的 ID 是"完整文件名"。** `task_id: 197` 只存在于 frontmatter，队列操作必须用工单在队列里的完整 ID。
- **`kdo pre-submit --files` 是 `kdo lint` 超时后的可靠 fallback。** 但要在任务单里诚实记录 lint 超时和尝试过程，不能假装跑过全库 lint。
- **工具卡和案例卡也需要 Critique / When NOT to Use。** 这是完整度要求，不再只是 dk 卡的特权。

---

## 过程资产

| 新增/更新 | 路径 |
|:---|:---|
| 合并 8 张 canonical 卡 | `30_wiki/frameworks/framework-ai-video-production-aesthetics-first.md` 等 |
| 更新 #197 任务单修复报告 | `60_feedback/tasks/task_20260720_wangyuyan-ai-video-tool-dev.md` |
| 新增任务编排侧复盘（audit 格式） | `60_feedback/audit/2026-07-21-197-merge-retrospective.md` |
| 队列状态更新 | `70_product/tasks/production-queue.md`、dashboard.html |
| #198 已交接老顽童 | `task_20260721_wangyuyan-infinite-canvas` 状态 `claimed-hermes` |

---

## 元反思

> 下次怎么做才能不一样？

1. **清理重复前先恢复副本**，删除前做标准目录 vs 副本的内容 diff，确认 Critique/Synthesis/Evidence/Claims/Action Triggers/When NOT/失败模式全部合并。
2. **提交 `pending_review` 前跑 section 完整度检查清单**，不再区分"dk 才需要 Critique"。
3. **操作队列前先看队列表格里的完整任务 ID**，不再用数字 task_id 直接调用 `queue_transition.py`。
4. **`kdo lint` 超时则尝试 domain-level 分批跑**，并记录尝试过程；以 `pre-submit --files` 作为 fallback 证据。
5. **发现他人卡片口径不一致**（如 skill 卡"待迁移"与实际决策不符），走"报告东家/写纠偏"通道，不直接改别人卡片主体。

---

## Truman 复盘

### 逐轮映射

| 轮次 | 人做了什么 | 双三角 | AI 做了什么 | 双三角 |
|:---|:---|:---|:---|:---|
| 1 | 派发 #197 厚内容合并修复任务 | 体系（任务编排） | 读取 `/tmp` 恢复版本与标准目录版本，定位内容缺口 | 基本功（读取+对比） |
| 2 | 给出"按格式写复盘"指令 | 体系（方法要求） | 用 Python 脚本合并 8 张卡 frontmatter 与 body，补 ds 和 related | 基本功（执行）+ 体系（脚本化） |
| 3 | 告知 #197 终审通过，#198 交给老顽童 | 审美（决策确认） | 校验队列状态，确认 #197 reviewed、#198 claimed-hermes | 基本功（验证） |
| 4 | 要求"按照格式来"写复盘 | 体系（复盘方法） | 先写 audit 格式复盘 | 体系（结构化输出） |
| 5 | 要求学习洪七公复盘 | 审美（标准升级） | 读洪七公 session archive，重写为每日复盘格式 | 体系（方法论自省）+ 基本功（重写） |

### 飞轮效应

- **重复合并检查飞轮**：从"丢 Critique"事件中沉淀出"恢复→diff→合并→删除"四步清单，下次清理重复目录不再丢内容。
- **队列状态校验飞轮**：完整任务 ID + `queue_transition.py` 原子操作，状态同步从"手动对表"变为"脚本强制一致"。
- **复盘格式飞轮**：采用洪七公"概要→关键决策→思维盲点→顿悟→过程资产→元反思→Truman"结构，认知沉淀从"总结"升级为"可复用模板"。

### 对照实验

| 场景 | 结果 |
|:---|:---|
| **无 AI（纯人做）** | 8 张卡内容 diff / frontmatter 合并 / ds 设计，手动易漏；队列状态手动改易冲突；复盘格式各人各样 |
| **无 人（纯 AI 自治）** | 可能凭默认假设直接删副本不合并；可能用数字 ID 操作队列失败；可能漏 tool/case Critique；复盘易流于表面 |
| **人机合一（实际）** | 人定验收标准和方向，AI 执行合并/校验/状态更新/复盘结构化，最终人工确认 |

### 下次改进

- **Agent 自身**：① 清理重复前强制恢复+diff；② 操作队列前读队列表格完整 ID；③ lint 超时尝试 domain-level 并记录；④ 他人卡片口径不一致走报告通道。
- **任务单更新建议**：把"section 完整度检查清单"写入 #198 任务单，老顽童修复前必须逐项过检；并在 #198 仍阻塞项中补充 `tool-presentation-quality-gate-pipeline` 缺 When NOT to Use。

---

*任务编排复盘 · 2026-07-21*
