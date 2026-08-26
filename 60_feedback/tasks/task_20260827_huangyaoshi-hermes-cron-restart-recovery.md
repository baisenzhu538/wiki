---
id: 560
assignee: huangyaoshi
status: queued
updated_at: '2026-08-27T02:20:00+00:00'
version: v0.1
instance: huangyaoshi
code_files: []
---

# #560 hermes cron 调度器重启不恢复排查（job 错过 fire 点后卡死）

- **任务号**：#560
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P1（飞书侧唯一任务时钟卡死实证——laowantong-clock-v3 昨晚 22:56 后不再执行）
- **立项**：2026-08-27 王语嫣（诊断 diag_20260827_wangyuyan-feishu-instances-shared-audit 发现 1）

## 背景（实证链）

- `laowantong-clock-v3`（jobs.json，*/15min，enabled，state=scheduled，workdir 正确）：last_run 08-26 22:23:58 ok
- hermes 进程 22:56:43 重启（5 个 hermes.exe，Services 会话）
- 重启后 **next_run_at 永远停在 22:30**——错过 fire 点的 job 不再被调度推进
- 对照：同机三 profile 的 ticker 心跳 08-27 01:46 正常——**心跳活着、任务死了**，jobs.json 与 ticker 的重启恢复逻辑不对称

## 任务

1. 定位 hermes cron 调度器的启动恢复逻辑：重启时是否重载 jobs.json / 是否重算 next_run_at / 错过 fire 点的 job 是跳过还是补跑
2. 修复：重启后 scheduled job 的 next_run 重算到未来（补跑策略：错过即下一周期，不追补——防风暴）
3. 回归：注册 */1min 测试 job → 重启 hermes → 验证恢复执行；laowantong-clock-v3 恢复实跑
4. §3.19：若新增/变更信号→矩阵登记

## 边界

- 只修调度器恢复逻辑，不动 job 定义/prompt
- hermes 源码位置自定位；与 #558 同属 hermes 工具层，可同批施工分开 commit

## 验收

- 重启恢复回归用例过 + laowantong-clock-v3 恢复执行实证；欧阳锋终审
