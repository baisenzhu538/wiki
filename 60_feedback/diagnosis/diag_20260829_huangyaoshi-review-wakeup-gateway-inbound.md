---
id: diag_20260829_huangyaoshi-review-wakeup-gateway-inbound
title: #574 R3 调研结论——待审提醒通道对齐（webhook 接收端可见性 + Hermes gateway 入站可行性）
type: finding
status: done
author: huangyaoshi
audience: 欧阳锋（终审）/ 王语嫣（编排）
date: 2026-08-29
task: 574
---

# #574 R3 调研结论：待审提醒通道对齐

> 依据建议书 `diag_20260828_ouyangfeng-review-wakeup-gap.md` R3，并入 #574 单。
> 调研对象：①webhook 群机器人接收端可见性 ②Hermes gateway 入站可行性（「提醒即唤醒」）
> ③「产线三角色 clock 配置规范」落地扩档——**因 08-29 老朱定调时钟停用，本节过时跳过，见 §三**。

## 一、webhook 群机器人接收端可见性

**结论：出站单向通道，接收端无元数据标注，可见性无法从代码侧证实，从 #573 实证推断非「常驻可见」。**

| 检查项 | 实证 | 判断 |
|:--|:--|:--|
| webhook 配置结构 | `kdo-tools/.feishu_webhooks.json` 四角色（ouyangfeng/laowantong/wangyuyan/huangyaoshi），每个 role 仅 `{url, key}` | **无 chat_id/群名/接收端标注**——建议书「无 chat_id 标注」属实 |
| 通道方向 | `conveyor_probe._send_hook` 走飞书群机器人 webhook（POST 出站） | **出站单向**，消息进群 ≠ 进任何 agent 输入流 |
| 可见性实证 | #573 21:50 提审 → 22:07/22:22/22:32 三拍推群 + todos，直到用户 22:3x 飞书追问才被看见 | 40min 无人响应 ⇒ 群推送**不是常驻可见**（至少不触发审查者会话） |
| 是否需要人工确认 | 群是否被用户/老朱常用，是**人的判断**，代码侧无法回答 | 建议欧阳锋/老朱口头确认一次群活跃度 |

**结论补一句**：即使群常驻可见，它仍是「人看群」通道，不是「提醒即唤醒」的自动化——要完全自动化，需 §二 的 gateway 入站。

## 二、Hermes gateway 入站可行性

**结论：支持，但本机当前未启用；「提醒即唤醒」完全自动化的正确实现路径 = Hermes 独立 webhook 入站平台，而非飞书群机器人 webhook。**

### 现状（本机 profile huangyaoshi）

| 项 | 实证 |
|:--|:--|
| gateway 平台 | `config.yaml` `platforms` 段仅 `feishu`（`ws_ping_interval: 30`），**未启用 webhook 平台** |
| 入站通道 | 飞书 gateway 通过飞书事件订阅接收**用户 DM** → 输入流 → 唤醒会话（已天然存在，即 #573「用户追问才叫醒」那条唯一可靠通道） |
| webhook 入站 | 无 `webhook_subscriptions.json`，`platforms.webhook` 未配置 ⇒ 独立 webhook 入站平台**未启用** |
| 防循环 | 飞书 gateway 对机器人自消息不触发会话（建议书断点 B 已指）——群机器人推的消息不会反过来唤醒自己 |

### 可行性判断（据 Hermes 官方能力）

Hermes 提供**独立 webhook 入站平台**（`platforms.webhook.enabled + port + HMAC secret`）：
- 外部服务 POST 到 webhook URL → 触发 agent run → 响应投递到配置的 target。
- 这正是「消息进输入流 = 提醒即唤醒」的**完全自动化通道**，技术上可行。

**关键区分（三个东西别混）**：

| 通道 | 方向 | 能否唤醒 agent 会话 |
|:--|:--|:--|
| 飞书群机器人 webhook（`.feishu_webhooks.json`） | 出站（Hermes→群） | ✗ 不能（群消息不进输入流） |
| 飞书 gateway 事件订阅（用户 DM） | 入站（用户→agent） | ✓ 能，但靠**人主动发消息** |
| Hermes webhook 入站平台（`platforms.webhook`，端口 8644） | 入站（外部服务→agent） | ✓ 能，**系统自动触发** = 提醒即唤醒 |

### 落地建议（后续立项，非本单范围）

若要做「提醒即唤醒」完全自动化，正确路径 = 让 `check-review-sla` / `conveyor_probe` 等探针在超时/检出时 **POST 到 Hermes webhook 入站平台**（而非只推飞书群机器人），由 webhook 触发审查者 agent run。
- 成本：需启用 `platforms.webhook` + 每角色一个 subscription + 探针侧加 POST 调用点 + 本机端口可达（跨机需隧道）。
- 风险/权衡：LLM 驱动的 webhook 触发有 token 成本；若只想「把提醒推到人眼前」而非「唤醒 agent」，R2 的 `cron deliver=feishu`（值守拍直达飞书 Home）更轻。**留待老朱/王语嫣裁定用哪档**。

## 三、产线三角色 clock 配置规范（过时跳过，标注原因）

> 原 R3 落地扩档（任务单「补充要求」段）：「产线三角色 clock 配置规范」= 各角色 clock ①deliver local→feishu ②prompt 加主动读收件箱执行待办。

**过时原因（08-29 老朱定调）**：各角色时钟**停用**，改「王语嫣 headless 拉起」模式（`hermes -z --profile <角色>`，唤醒链 = 老朱 DM 王语嫣 → 王语嫣 headless 拉起各角色）。

- clock deliver→feishu + 收件箱主动消费的**前提（角色时钟在跑）已消失**，规范整体过时，故跳过、不产出。
- 残留有效性：R2（欧阳锋自改 `ouyangfeng-clock-v1` deliver local→feishu）是**时钟停用前**的即时动作，若时钟已停，R2 本身也随之下线——此点交欧阳锋/王语嫣确认，不占本单。
- 「收件箱主动消费」的精神在 headless 拉起模式下由**拉起 prompt 自带**（王语嫣拉起时告知各角色读自己 todos），机制上不依赖 clock 规范。

## 四、给终审/编排的一句话

- **R3 调研落档完成**：webhook 接收端=出站单向、无元数据、非常驻可见（#573 实证）；gateway 入站=可行但需启用独立 webhook 平台（正确路径已厘清，落地待裁定档次）。
- **clock 规范跳过**：时钟停用（08-29 老朱），前提消失，规范过时。
- **待裁定**：①群活跃度口头确认 ②「提醒即唤醒」用 webhook 入站（重）还是 R2 值守拍（轻）——建议先 R2 轻量跑通，webhook 入站观察再立项。
