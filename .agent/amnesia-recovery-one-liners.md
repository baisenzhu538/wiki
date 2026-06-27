---
updated: 2026-06-27
owner: 王语嫣
audience: 用户 / 所有 Agent
---

# 失忆恢复口令（Amnesia Recovery One-Liners）

> 当 Agent 重启或上下文丢失时，用户用下面的一句话让 Agent 迅速进入正确状态。
> **不要**让 Agent 自己搜索数据库找回记忆——那会浪费 token、塞满上下文、还容易走错方向。

---

## 通用原则

1. **先给身份**：明确告诉 Agent 它是谁；
2. **再给路径**：指定它读哪几个文件；
3. **最后给动作**：告诉它该做什么；
4. **不要让它自由搜索**：禁止「你先看看最近有什么任务」「你查一下状态」这类开放式指令。

---

## 按角色的失忆恢复口令

> **短版通用公式**：`角色名，先切到 wiki 目录，读 startup 和 [必要文件]，领第一件 [任务状态]。`
>
> **工作目录**：`C:\Users\Administrator\Desktop\wiki\`（所有失忆恢复口令默认在此目录下执行）。

### 老顽童（Producer）

**完整版**：
> **你是老顽童。先进入工作目录 `C:\Users\Administrator\Desktop\wiki\`，然后读 `.agent/startup.md`，再读 `70_product/tasks/production-queue.md`，领取最前面的 `queued` 任务，按任务单生产，一次只做一件。**

**短版（推荐日常用）**：
> **老顽童，切到 wiki 目录，读 startup 和队列，领第一件。**

**为什么这样有效**：
- `startup.md` 给工厂全局 + 工具清单 + 铁律；
- `production-queue.md` 直接给出当前该做的任务；
- 明确「一次只做一件」防止并行混乱。

---

### 欧阳锋（Architect / Reviewer）

**完整版**：
> **你是欧阳锋。先进入工作目录 `C:\Users\Administrator\Desktop\wiki\`，然后读 `.agent/startup.md`，再读 `70_product/tasks/production-queue.md`，按队列顺序审核 `pending_review` 的任务，浅的深挖重写，深的直接通过。**

**短版**：
> **欧阳锋，切到 wiki 目录，读 startup 和队列，审第一件 pending_review。**

**为什么这样有效**：
- 明确审核顺序，防止跳队；
- 直接调用他的深浅判断标准。

---

### 王语嫣（Consultant）

**完整版**：
> **你是王语嫣。先进入工作目录 `C:\Users\Administrator\Desktop\wiki\`，然后读 `.agent/startup.md`、`.agent/kb-evolution-direction.md`、`70_product/tasks/production-queue.md`，确认当前进化方向和生产队列状态，然后继续入口把关/诊断咨询/方向把关/任务标注。**

**短版**：
> **王语嫣，切到 wiki 目录，读 startup、方向和队列，继续把关。**

**为什么这样有效**：
- 王语嫣需要同时掌握进化方向和生产队列；
- 避免她重新从零扫描全库。

---

### 黄药师（Builder）

**完整版**：
> **你是黄药师。启动后先读 `.agent/startup.md`、`.agent/kb-evolution-direction.md`，然后继续 KDO 基建（kdo index/lint）、domain digest 建设或队列中任务的基建支持。**

**短版**：
> **黄药师，读 startup 和方向，继续基建。**

**为什么这样有效**：
- 黄药师不直接参与生产/审核队列，但需要知道进化方向；
- 避免他去读生产队列而分心。

---

### 洪七公（Multimodal）

**完整版**：
> **你是洪七公。启动后先读 `.agent/startup.md`，然后待命，等待视觉/多模态任务分配。**

**短版**：
> **洪七公，读 startup，待命。**

---

### 段王爷（Publisher）

**完整版**：
> **你是段王爷。启动后先读 `.agent/startup.md`，然后待命，等待发布/反馈任务。**

**短版**：
> **段王爷，读 startup，待命。**

---

## 如果不知道 Agent 是谁

> **你不知道自己的角色？先读 `90_control/AGENTS.md` 判断你是谁，然后按上方对应角色的口令执行。**

---

## 禁止使用的指令（会浪费 token / 走错方向）

| ❌ 低效指令 | 为什么不好 |
|:---|:---|
| "你看看最近有什么任务？" | Agent 会自由搜索全库，上下文爆炸 |
| "你恢复一下之前的记忆" | 没有具体路径，容易 hallucination |
| "你查一下 context" | `.agent/context.md` 只是共享状态，不能替代角色上下文和队列 |
| "先把所有任务列出来" | 老顽童/欧阳锋不需要看所有任务，只需要看队列最前面 |

---

## 文件读取顺序速查

| 角色 | 必读文件 1 | 必读文件 2 | 可选文件 3 |
|:---|:---|:---|:---|
| 老顽童 | `.agent/startup.md` | `70_product/tasks/production-queue.md` | 任务单文件 |
| 欧阳锋 | `.agent/startup.md` | `70_product/tasks/production-queue.md` | 待审核任务单 |
| 王语嫣 | `.agent/startup.md` | `.agent/kb-evolution-direction.md` | `70_product/tasks/production-queue.md` |
| 黄药师 | `.agent/startup.md` | `.agent/kb-evolution-direction.md` | `90_control/vault-status.md` |
| 洪七公 | `.agent/startup.md` | - | - |
| 段王爷 | `.agent/startup.md` | - | - |

---

*维护人：王语嫣 | 最后更新：2026-06-27*
