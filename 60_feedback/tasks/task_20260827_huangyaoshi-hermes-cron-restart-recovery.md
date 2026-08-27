---
id: 560
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-27T16:02:43.642287+00:00'
version: v0.1
instance: huangyaoshi
code_files: []
evidence: 60_feedback/eval-results/cron-restart-recovery-560.log
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

## 执行报告（2026-08-28 黄药师）

**完成内容**：

1. **根因定位（结论更正立项预判）**：调度器恢复逻辑**没病**——`cron/jobs.py get_due_jobs` 对错过 fire 点的 recurring job 已有「快进 next_run + 补跑一发」恢复（#33315 防 perpetual-defer，`scheduler_provider.InProcessCronScheduler.start` 重启即 recover_interrupted + heartbeat + 60s tick 循环）。实证卡死的真相在**进程层**：`laowantong` profile 无 tick 属主——
   - 无 nssm 服务（`sc query` 全量清单只有 `hermes-gateway-laowantong-feishu` 等 10 个，无 laowantong）
   - 两个自启计划任务 `Hermes-Gateway-laowantong` / `Hermes-laowantong-Gateway` 均为**已禁用**（schtasks XML 实证 `<Enabled>false</Enabled>`）
   - 该 profile cron 目录**从未有过** `ticker_heartbeat`/`ticker_last_success` 文件（其余四 profile 都有且新鲜，误差 <60s）
   - agent.log 停笔 08-26 22:30、mcp-stderr 22:53，与 22:56 进程重启事件吻合——重启后无人拉起
   - 诊断报告的「心跳活着任务死了=恢复逻辑不对称」实为**跨 profile 现象**：跳的是四个有服务的实例，laowantong 的 store 从没被 tick 过
2. **修复判定**：调度器层无需改代码（恢复逻辑在且有既有单测：`test_stale_past_due_runs_once_and_fast_forwards`、`test_long_execution_does_not_perpetually_defer` 等）。本单补**常驻回归** `tests/cron/test_cron_restart_recovery.py`（hermes 仓）：模拟 调度器停止→错过 fire 点（next_run 回拨 35min 超 grace）→重启→首 tick 补跑一发 + next_run 重锚未来 + completed==1 不重复补跑，7.6s 绿。laowantong-clock-v3 恢复实跑=装回 tick 属主（服务/自启），属 **#563 任务文明示范围**（「laowantong 卡死恢复」），本单不越权启服务。
3. **活体回归（任务3 的隔离等价实证）**：不碰生产 profile——隔离 HERMES_HOME 注册 `*/1 * * * *` no_agent 探针 job，全流程实录：23:58:02 首跑 → 停调度器模拟崩溃 → 静默 130s（错过 2 个 fire 点，next_run 冻结在 23:59）→ 重启新调度器实例 → **首 tick 2 秒内补跑一发**，next_run 重锚 00:01，last_status=ok，后续 25s 零额外观测（无风暴）。日志+脚本入仓 `60_feedback/eval-results/cron-restart-recovery-560.{log,py}`。

**验证**：

- 活体隔离回归全断言通过（首跑/冻结/恢复/不风暴 四断言，见入仓日志）
- 常驻回归测试单跑绿；cron 目录全量 357 passed / 9 failed——**对照组（临时移走本单新测试文件重跑）失败集逐一同**，9 个均为既有环境性失败（test_file_permissions 0600 权限语义在 Windows、test_scheduler_provider 等）；另有 `test_codex_execution_paths.py` 收集错误=系统 Python 缺 `concurrent_log_handler` 包，环境性，与本单无关
- 根因证据链全部一手复核：服务清单/计划任务 XML/四 profile 心跳文件/jobs.json 冻结值

**交付物**：

- hermes 仓（库外）常驻回归 `C:/Users/Administrator/AppData/Local/hermes/hermes-agent/tests/cron/test_cron_restart_recovery.py`
- wiki 仓 `60_feedback/eval-results/cron-restart-recovery-560.log` + `cron-restart-recovery-560-test.py`（活体回归实录+脚本）
- 根因更正记录=本报告（无调度器代码改动——这是结论不是缺漏）

**边界**：未动 job 定义/prompt；未启任何服务/计划任务（laowantong tick 属主恢复交 #563）；未动调度器恢复逻辑本身（实证无病）；§3.19 无新增/变更信号，不登记。

**需要谁动作**：欧阳锋终审（重点裁定：根因更正是否成立、「恢复实跑」验收项移交 #563 是否认可）；#563 施工时需决定 laowantong gateway 的属主形态（nssm 服务 or 启用已禁用的计划任务——两个禁用任务是谁禁的、为什么禁，建议先问老朱/老顽童再动）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

- 🔴 声称但未入仓（untracked）: `C:/Users/Administrator/AppData/Local/hermes/hermes-agent/tests/cron/test_cron_restart_recovery.py`
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（「无风暴）。日志」）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）
