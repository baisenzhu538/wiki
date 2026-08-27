---
id: 562
assignee: huangyaoshi
status: queued
updated_at: '2026-08-27T09:05:00+00:00'
version: v0.1
instance: huangyaoshi
code_files:
  - 90_control/scripts/role_registry.py
  - kdo-tools/role_clock.py
  - kdo-tools/conveyor_probe.py
---

# #562 liveness 报警风暴止血：报警幂等冷却 + 心跳语义修复 + 探针多行解析

- **任务号**：#562
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P0（报警风暴进行中——07:42 起每 5 分钟 2-3 条，至 09:00 已 25+ 条，每条触发第五探针推送）
- **立项**：2026-08-27 王语嫣（老朱质询「KDO秘书推送多条门禁拦截异常提醒」诊断发现）

## 背景（实证链）

role_clock（schtasks 5min）每拍调 `rr.check_liveness(now=ts)`（role_clock.py:169），
`check_liveness` 对全死角色**无幂等无冷却**直接 append gate-blocked.log（role_registry.py:100-108）
→ conveyor_probe 第五探针增量拾取 → 登记 [gate-blocked] + 推送。
08-27 07:42-08:57 已 25 条 role-liveness 行，且**全是误报或半误报**：

- 王语嫣 08:55 正在会话中回话，心跳停在 06:53 被判「全实例疑似死亡」——**活跃≠心跳，idle 会话被误杀**
- 心跳写入点只有 CLI 启动/手工 register/蹭拍（设计稿 §1 写侧列了「时钟蹭拍」），
  但 role_clock wake 只投递 todos 不刷心跳（role_clock.py:146-148），**蹭拍未实现**
- laowantong 对照组：08:42 唤醒后 08:45 真实活动刷了心跳 → 从报警名单消失。
  证明链路本身能工作，缺的是「无任务时的心跳面」

附带发现：E040 拦截消息是多行（`未 commit=未发生\n  - untracked: ...`），
第五探针按物理行解析 → 续行残片被登记成独立垃圾建议
（队列 PROPOSAL-PENDING 区 `[gate-blocked] huangyaoshi｜- untrack`、`[gate-blocked] laowantong｜- untracked: kdo pre-submit -f...` 两条实证）。

附带发现 2：role_registry.py heartbeat 确认输出的 ✅ emoji 在 GBK 控制台直接抛
UnicodeEncodeError（08-27 19:17 王语嫣实测——写入成功但 exit 1，F-030 同族坑）；
同文件所有 print 需过一遍非 ASCII 输出。

## 任务

1. **止血（先行）**：`check_liveness` 加报警冷却——同角色报警后 2h 内不重报（state 记 last_alert_ts，
   恢复后清零重新武装）；台账行追加「(冷却中 N 次抑制)」汇总数，不丢信息
2. **心跳语义修复（设计选择，倾向后者）**：
   - 方案 A：wake 投递成功即蹭拍 heartbeat——实现一行，但时钟活着≠agent 活着，liveness 失真
   - 方案 B（倾向）：消费回执=心跳——agent 处理 todos/时钟拍后由 queue_transition 或 myqueue 消费点蹭拍；
     另 CLI 会话活跃（turn 活动）可挂 hook 蹭拍。设计稿 §1「时钟蹭拍」原意需黄药师对稿确认落点
3. **第五探针解析修复**：gate-blocked.log 按记录起始行（时间戳开头）聚合续行，不按物理行逐行登记；
   存量两条垃圾建议行由王语嫣批核划销（不在本单）
4. §3.19：若新增/变更信号 → 矩阵登记

## 边界

- 不改 ROLE_PACE_MIN 节奏表，不改「全死自报」通道（复用 gate-blocked 的设计不动）
- 报警冷却只压频不删报——首次必报、恢复必清零
- liveness 语义（>2×节奏=疑似死亡）不动，只修心跳来源真实性

## 验收

- 冷却回归：构造全死角色连跑 3 拍 check_liveness → 台账仅 1 条新行（含抑制计数）
- 心跳回归：唤醒后 agent 消费动作 → 注册表心跳刷新 → liveness 转 alive
- 探针回归：多行 E040 样本 → 仅 1 条登记无残片
- 欧阳锋终审
