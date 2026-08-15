---
title: Codex 观察者 · 系统记忆基线
created_at: 2026-08-15
updated_at: 2026-08-15
type: memory/system-baseline
owner: codex
---

# Codex 观察者 · 系统记忆基线

> 我是 **Codex，系统观察者**，不是任何一个业务 Agent。
> 职责：保证整个系统和 Agent 正常运行、帮助各 Agent 记住自己、建立并维护长久化的记忆基线。
> 本文件是记忆基线（baseline）——恢复、巡检、漂移检测都以本文件为参照。

## 0. 观察者身份

- 名字：Codex（观察者 / 运维）
- 不是：黄药师、老顽童、王语嫣、欧阳锋、洪七公、段王爷，也不替代他们做业务判断
- 职责：
  1. 保证系统与 Agent 正常运行（巡检、诊断、修复）
  2. 帮助 Agent 记忆（失忆恢复、context / 复盘 / 锚点维护）
  3. 建立长久化记忆基线（本文件 + `agent复盘/codex/`）
- 工作目录：`C:\Users\Administrator\Desktop\wiki\`
- 自己的记忆：`agent复盘/codex/`（复盘）+ 本文件（基线）

## 1. 系统 Agent 地图（2026-08-15）

### 五绝（核心六角色）

| 角色 | 英文 id | 职责 | context | amnesia 恢复 | agent复盘 |
|:--|:--|:--|:--|:--|:--|
| 欧阳锋 | ouyangfeng | Architect + 终审 | `.agent/ouyangfeng-context.md` | `20_memory/ouyangfeng-amnesia-recovery.md` | `ouyangfeng/` + `欧阳锋/` |
| 黄药师 | huangyaoshi | Builder / 基建 | `.agent/huangyaoshi-context.md` | `20_memory/huangyaoshi-amnesia-recovery.md` | `huangyaoshi/` + `黄药师/` |
| 王语嫣 | wangyuyan | Consultant / 编排 | `.agent/wangyuyan-context.md` | `20_memory/wangyuyan-amnesia-recovery.md` | `wangyuyan/` + `王语嫣/` |
| 老顽童 | laowantong | Producer / 卡片产能 | `.agent/laowantong-context.md` | `20_memory/laowantong-amnesia-recovery.md` | `laowantong/` + `老顽童/` |
| 洪七公 | hongqigong | Multimodal / 视觉 | `.agent/hongqigong-context.md` | `20_memory/hongqigong-amnesia-recovery-20260613.md` | `hongqigong/` + `洪七公/` |
| 段王爷 | duanwangye | Publisher / 发布反馈 | `.agent/duanwangye-context.md` | `20_memory/duanwangye-amnesia-recovery-2026-07-21.md` | `duanwangye/` + `段王爷/` |

### 其他 / 辅助 Agent

| 名称 | 运行位置 | 记忆位置 |
|:--|:--|:--|
| Codex（观察者 / 运维） | Windows | `agent复盘/codex/` + 本文件 |
| CodeBuddy | Windows | `agent复盘/codebuddy/` |
| Kimi / Kimi Code | Windows / CLI | `agent复盘/Kimi/`、`agent复盘/kimi-code/` |
| AI基本功教练 | 飞书 | `agent复盘/AI基本功教练/` |
| 销售对话参谋 | 飞书 | `agent复盘/sales-dialogue-assistant/daily-context/`（daily-context 人读）；`agent复盘/销售对话参谋/` 为空壳目录待裁定 |
| 教练式领导力助理 / 会议助理 | 飞书 | `wiki/agents/` spec（暂无独立 agent复盘 目录） |

## 2. 当前状态基线（2026-08-15）

### 硬件 / 环境
- 物理内存：**16GB → 32GB**（实测 31.87GB，当前可用 18.17GB）
- `.wslconfig`：`memory=6GB`、`vmIdleTimeout=-1`（已从 4GB 上调）
- WSL Ubuntu-22.04：running；实测 swap 使用 **0B**（原 540Mi）、内存使用 2.9/6GB
- CPU：i7-10750H，6 核 12 线程；WSL 可用 12 线程
- 8 个 Hermes gateway 服务全部 active running

### 生产队列
- 297 任务：queued=0 / claimed=0 / pending_review=0（看板全清）
- active_task：Live258 内容域三连批全闭环（#312/#313/#314 全部 reviewed）
- 遗留：#304/#298 待欧阳锋终审

### 停车场关键项
- **P-31 WSL Hermes 性能：✅ 已解决（2026-08-15）**——16→32GB + .wslconfig 6GB + 老顽童 CLI 迁 Windows 原生后，swap 归零、8 gateway 正常
- P-3 事实核对门（待设计）、P-30 GBK 修复（排期优先）、O-12/O-13（Hermes WSL→Windows 迁移专项，决策待用户）

### 记忆基线刷新
- **洪七公**：`hongqigong-amnesia-recovery-20260613.md` 已刷新至 2026-08-15；最新业务锚点 2026-08-09（long-image-ocr v2.0、E001-E024、M3-only 铁律、三专题收官）
- **段王爷**：`duanwangye-amnesia-recovery-2026-07-21.md` 已刷新至 2026-08-15；最新业务锚点 2026-08-11（周一 cron 巡检闭环、E001-E009、Bitable 补录 3 条）

### 已知阻塞
- production-queue.md 中文 mojibake（UTF-8-SIG 混合编码）——历史遗留
- queue_transition.py review 路径被 auto mode 拦截 + O-3 bug（complete --force 对 queued 必失败）

## 3. 记忆地图（每个 Agent 的记忆在哪里）

- **角色身份**：`wiki/.agent/<role>-context.md`
- **失忆恢复锚点**：`wiki/20_memory/<role>-amnesia-recovery*.md`
- **每日 Truman 复盘**：`agent复盘/<role>/daily-context/YYYY-MM-DD.md`
- **认知复盘（中文旧体系）**：`agent复盘/<中文名>/daily_cognitive_review/`
- **共享状态**：`wiki/.agent/context.md`
- **恢复口令**：`wiki/.agent/amnesia-recovery-one-liners.md`
- **一页纸摘要**：`wiki/.agent/agent-contexts-summary.md`

## 4. 失忆恢复口令速查

| 角色 | 最短口令 |
|:--|:--|
| 老顽童 | 老顽童，切到 wiki 目录，读 startup 和队列，领第一件 |
| 欧阳锋 | 欧阳锋，切到 wiki 目录，读 startup 和队列，审第一件 pending_review |
| 王语嫣 | 王语嫣，切到 wiki 目录，读 startup、方向和队列，继续把关 |
| 黄药师 | 黄药师，切到 wiki 目录，读 startup 和方向，继续基建 |
| 洪七公 | 洪七公，切到 wiki 目录，读 startup，待命 |
| 段王爷 | 段王爷，切到 wiki 目录，读 startup，待命 |
| Codex | Codex，观察者身份，读 `20_memory/codex-observer-memory-baseline.md` + `agent复盘/codex/` |

## 5. 基线维护规则

1. 每次观察者会话结束后，更新本文件 `updated_at` 和「当前状态基线」节。
2. 系统 / Agent 发生重大变更（新增 Agent、迁移、硬件/角色调整）时，更新地图与状态节。
3. 漂移检测：对比 `agent复盘/<agent>/` 最新 daily-context 与 amnesia-recovery 锚点日期；发现写死日期过期，改为「以目录内最新为准」。
4. 所有 Agent 的「已更新 XX」声明，落盘前 grep 验证（对己验证纪律）。

## 6. 已知记忆债（待观察者跟踪）

1. 双目录记忆同步方向未裁定：`agent复盘/<英文>` 与 `agent复盘/<中文>`、`wiki/.agent/<role>/daily_cognitive_review/` 三处副本不一致。
2. context 路径漂移已完成第一轮修复：六份 `*-context.md` 的 `技能进化日志.md` 路径已对齐实际中文目录；`sales-dialogue-assistant` 的 `daily-context/` 目录已按规范创建。剩余：`agent复盘/销售对话参谋/` 空壳目录用途未裁定。
3. 失忆恢复指引写死日期已陆续改为「以目录内最新为准」；洪七公 / 段王爷本次已改，黄药师 / 王语嫣 / 老顽童 / 欧阳锋仍需继续清查剩余写死路径。
4. git 工作区曾存在 command-as-filename 损坏文件名（`&& cp ...`），已于 2026-08-15 从索引清理并提交 `d65098bd4`。