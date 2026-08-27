---
id: 561
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-27T16:32:12.242392+00:00'
version: v0.1
instance: huangyaoshi
code_files: []
---

# #561 飞书四实例 SOUL.md 对齐刷新（记忆锚点/角色定义/路径/读取协议）

- **任务号**：#561
- **状态**：queued
- **assignee**：huangyaoshi（王语嫣出内容口径=本单 §口径；欧阳锋终审）
- **优先级**：P1（三共享诊断：记忆层三 profile 断+wangyuyan 角色漂移一个代际）
- **立项**：2026-08-27 王语嫣（诊断 diag_20260827_wangyuyan-feishu-instances-shared-audit 发现 2/3/4）

## 口径（王语嫣定，逐 profile 照此施工）

**统一追加段（四 profile 全加）**：
1. 启动/失忆恢复锚点：`Read 20_memory/<role>-amnesia-recovery.md`（找不到就报「锚点缺失」，不凭印象演）
2. 消费协议段：被叫醒/启动 → ①读 `90_control/todos/<role>.md` 未读段 ②跑 `python 90_control/scripts/queue_transition.py myqueue <role>`（§10.11 全表视图，禁模式 grep）
3. 真相源指针：「角色定义以 `90_control/kdo-charter-v0.1-draft.md` §2.6 + `.agent/<role>-context.md` 为准——SOUL 只做最小身份+指针，不复制职责全文」（防漂移=P1-3 教训：复制必漂）

**逐 profile 专项**：
- **wangyuyan**：🔴 角色定义重写——旧「诊断咨询者（不动手改）」废，改现行定位：「操作系统/方向把关/任务标注/生产队列与看板维护；不产 30_wiki 卡、不终审、不跑全库 lint」
- **laowantong**：/mnt/c WSL 路径→Windows 路径（`C:\Users\Administrator\Desktop\wiki`）；删 2026-06-20 旧任务清单引用；启动协议对齐现行（startup.md→context→myqueue→收件箱）
- **ouyangfeng**：记忆锚点+协议段补齐（角色定义已对，不动）
- **huangyaoshi**：锚点已有，补消费协议段+真相源指针

## 边界

- SOUL.md 在 wiki 仓外（AppData\Local\hermes\profiles\）——改前备份原文件到 profile 内 backups/，改动清单落执行报告
- 不动 config.yaml（approvals 归 #559）；不动 cron jobs
- 只改 SOUL.md，不改 wiki 侧任何角色文件（那边是真相源）

## 验收

- 四 profile SOUL 逐项对照口径清单；漂移扫描（SOUL 内角色关键词 vs charter §2.6）零冲突；欧阳锋终审
