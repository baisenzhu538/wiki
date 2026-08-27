---
id: 563
assignee: huangyaoshi
status: queued
updated_at: '2026-08-27T19:32:28.324890+00:00'
version: v0.1
instance: huangyaoshi-kimi
code_files: []
---

# #563 hermes 飞书四实例时钟配置（ouyangfeng/huangyaoshi/wangyuyan 裸奔补齐）

- **任务号**：#563
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P1（飞书侧四实例只有一个有时钟且卡死，其余三个裸奔——飞书产线“被@才动”的根因）
- **立项**：2026-08-27 老朱直令「飞书的四个角色都需要配置时钟」，王语嫣诊断实证随附

## 背景（实证链）

- hermes profiles cron 目录实测（08-27 20:30）：
  - `ouyangfeng` / `huangyaoshi` / `wangyuyan`：**连 cron/jobs.json 都不存在**——从未配过任务时钟
  - `laowantong`：唯一有 job（clock-v3，*/15min），但 next_run 卡死 08-26 22:30（#560 重启不恢复 bug）
- 对照本地：role_clock（#553）对四角色的唤醒调度正常（08-27 全天日志连续），
  欧阳锋 CLI 被判「全实例疑似死亡」实为**心跳语义误报**（活着但 idle 无蹭拍，#562 任务2）——
  飞书侧则是**真的没有时钟**，两回事别混淆
- 节奏口径（与 #555 本地一致）：老顽童 15min / 王语嫣 30min / 欧阳锋事件驱动+30min 兜底 / 黄药师 15min

## 任务

1. 为 ouyangfeng / huangyaoshi / wangyuyan 三个 hermes profile 各建时钟 cron job
   （复用 laowantong clock-v3 的 prompt 模板，节奏按上行口径）
2. laowantong clock-v3 卡死恢复（依赖 #560 修复；若 #560 未落地则本单先手动重建 job 止血）
3. 四个 job 心跳写入 role-registry.json（kind=platform, profile=<role>）——飞书实例活性从此可见，
   check-liveness 才能区分「本地死」和「全死」
4. 验收回归：构造一次 pending_review → 飞书欧阳锋在兜底节奏内自起响应

## 边界

- 只配时钟和心跳，不动 SOUL/profile 内容（#561 的活）、不改审批模式（#559 的活）
- hermes cron 恢复逻辑 bug 归 #560，本单不重复修；两单同批施工分开 commit
- 频率不得高于本地节奏口径，防双源唤醒风暴

## 验收

- 四 profile jobs.json 齐 + role-registry 出现四条 kind=platform 心跳 + 欧阳锋兜底唤醒实测；
- 欧阳锋终审
