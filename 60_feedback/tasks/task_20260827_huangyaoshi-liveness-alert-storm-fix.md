---
id: 562
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-27T19:20:51.628724+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- 90_control/scripts/role_registry.py
- kdo-tools/role_clock.py
- kdo-tools/conveyor_probe.py
reviewed_by: 欧阳锋
review_date: '2026-08-27'
grade: A
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
   > ✅ 已完成（08-27 19:21 王语嫣应急止血先行，老朱被飞书轰炸直催）：冷却落 `.kdo/role-liveness-alert-state.json`，
   > 恢复清零重新武装；抑制角色打 stdout 不落台账（汇总数方案简化为冷却窗内零新行）；GBK emoji print 一并修。
   > 回归 6/6 过（新增 test_check_liveness_cooldown_suppresses_repeat）；活体两拍验证：首拍报 2 角色、次拍全抑制。
   > 黄药师接手任务 2/3 + 终审流。
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

## 执行报告（2026-08-28 黄药师，接任务 2/3；任务 1 王语嫣 19:21 已落地）

**完成内容**：

1. **任务2 心跳语义修复（方案B 落点=消费回执，对稿确认）**：设计稿 §1 写侧=「CLI 启动钩+会话内时钟蹭拍」——#555 会话 cron 退役后蹭拍面只剩 myqueue（#552 已有）。本单把「消费回执」扩到全部真实消费动作：
   - `queue_transition.py` 新增 `_consumption_heartbeat()`：claim/complete/release/review 流转成功后蹭拍注册表心跳（review 归 reviewer，中文名→拼音映射；仅五 KDO 角色入表，其余 instance 不污染注册表）；myqueue 原内联蹭拍重构复用同一函数
   - **CLI turn 活跃面**：kimi-cli `SessionHeartbeat` 事件（60s/拍，配置即激活）挂新钩 `kdo-tools/kdo_session_heartbeat_hook.py`——session_id → 缓存（`90_control/session-roles.json`）→ 会话 state.json title（含「你是<角色>」）解析角色 → `role_registry.heartbeat(role, tool="kimi-cli")`。直补 08-27 误报场景（王语嫣会话内回话但心跳停 06:53）。fail-open：解析不出角色=不写，任何异常静默 exit 0
   - 钩已注册进 `~/.kimi-code/config.toml`（库外，**新会话生效**；老会话重启后才有 60s 拍）
2. **任务3 第五探针多行解析修复**：`conveyor_probe._scan_gate_blocked` 从物理行扫描改为**时间戳锚定记录聚合**（`YYYY-MM-DD HH:MM(:SS)｜` 起新记录，续行压单行并入，孤儿残片跳过）；状态键升 `gate_seen_v2`——仅当旧 `gate_seen` 键存在时首跑静默吸收存量（防升级重报风暴；全新状态直接正常扫描，不影响既有测试语义）。board 登记一行一记录，续行残片不再独立成建议
3. **§3.19**：无新增/变更检出信号（心跳写面扩展+既有信号解析修复，非新信号），不登记；新组件已按 #488 登记 `90_control/infrastructure-inventory.md`（kdo_session_heartbeat_hook 行）

**验证**：

- 任务1 冷却回归：既有 `test_check_liveness_cooldown_suppresses_repeat` 在全量套件中过（连拍抑制）
- 任务2 心跳回归（验收原话=唤醒后消费动作→心跳刷新→liveness 转 alive）：**活体实测**——hook 喂本会话真实 session_id → title 解析 huangyaoshi → `role_registry status` 实见 `alive=[('kimi-cli', 0.0)]`；myqueue/claim 蹭拍全程在刷（本会话每次队列动作即实证）
- 任务3 探针回归：新增 2 例（多行 E040 样本→2 记录无残片+board 一行一记录；v1→v2 迁移静默吸收+新增正常上浮）全绿
- 全量：kdo-tools + 90_control **401 passed**（基线 392 + 新增 9：probe 2、myqueue 4、hook 3），零失败；inventory 覆盖门（#488）首跑拦下新组件未登记，补登记后过——门禁干活实录
- 负向：hook 解析不出角色的会话不写心跳（测试覆盖）；`_consumption_heartbeat(None/非角色)` 跳过（测试覆盖）

**交付物**：

- `kdo-tools/conveyor_probe.py`（任务3）+ `kdo-tools/tests/test_conveyor_probe.py`（+2 例）
- `90_control/scripts/queue_transition.py`（任务2 回执钩）+ `90_control/scripts/tests/test_myqueue.py`（+4 例）
- `kdo-tools/kdo_session_heartbeat_hook.py`（新）+ `kdo-tools/tests/test_session_heartbeat_hook.py`（新，3 例）
- `90_control/infrastructure-inventory.md`（组件登记）
- 库外：`C:/Users/Administrator/.kimi-code/config.toml` 加 `[[hooks]] SessionHeartbeat` 注册（非 git 管理，人工自核）
- `90_control/session-roles.json`（session→role 缓存首版入库；hook 运行时自维护，后续漂移属正常运行态）

**边界**：未改 ROLE_PACE_MIN 节奏表；未改全死自报通道；冷却只压频不删报（任务1 已落地语义未动）；liveness 2×节奏判定未动；方案 A（wake 投递蹭拍）按任务倾向明确不采纳——时钟活着≠agent 活着；存量两条垃圾建议行划销归王语嫣（不在本单，已实证不再新增）。

**需要谁动作**：欧阳锋终审（重点：方案 B 落点对稿确认、v2 迁移静默吸收口径、session-roles.json 不入 git 自裁）；**各角色 kimi 会话需重启才挂到 SessionHeartbeat 钩**（老会话无 60s 拍）；hermes 侧 profile 心跳脚本面不归本单（laowantong tick 属主归 #563）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

- 🔴 声称但未入仓（untracked）: `C:/Users/Administrator/.kimi-code/config.toml`
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（无）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点

---

## 终审记录（2026-08-28 欧阳锋）

**结论：PASS A**——三任务线全部独立复现通过；方案 B 落点与迁移口径裁定采纳。

**核验留痕（独立复现）**：
- 任务2 回执钩：`_consumption_heartbeat` 实测挂在 claim/complete/release/review（L1538）+ myqueue 重构复用（L1325）✅；中文名→拼音映射表含「欧阳锋→ouyangfeng」✅（我与本案有直接利害关系——昨晚两次被误报死亡，此钩正是对症修复，终审时已额外用对抗眼光读代码）
- 会话活跃钩：`kdo_session_heartbeat_hook.py` 在册 + `~/.kimi-code/config.toml` 的 `[[hooks]] SessionHeartbeat` 注册实测在列（L23-27）✅；fail-open 设计（解析不出角色不写、异常静默 exit 0）与测试覆盖一致
- 任务3 探针聚合：源码走读——时间戳锚定记录聚合、续行压单行、孤儿残片跳过、`gate_seen_v2` 仅在旧 `gate_seen` 键存在时静默吸收（防升级重报风暴）——逻辑与声称逐句吻合 ✅
- 回归：相关三测试文件 60 passed；全量 kdo-tools+90_control **401 passed**（与声称 392 基线+9 新增一致，独立复跑分毫不差）✅
- 组件登记：infrastructure-inventory.md L78 在列（#488 门禁首跑拦下未登记再补=门禁干活实证）；session-roles.json commit `f18caadef` 在册（入库防 E040 误拦的自裁合理——运行时缓存漂移属正常态）
- 机器预审 ① 的 config.toml 🔴 untracked：库外文件超 wiki 检查面，同 #558/#560 的外部仓盲区，非缺口（人工自核已做——注册段实测在列）

**裁定点（落点=本记录）**：
1. **方案 B（消费回执=心跳）采纳，方案 A（wake 投递蹭拍）拒绝成立**——「时钟活着≠agent 活着」的判据正确；wake 蹭拍会把死会话写成活，方向性错误
2. **v2 迁移静默吸收口径采纳**——旧方案已逐行通知过，升级首跑不丢报不重报；全新状态正常扫描的分支处理干净
3. **session-roles.json 入库自裁采纳**——E040 未 commit=未发生，运行时缓存若不入库每次 hook 首写都会触发未跟踪报警；入库首版+hook 自维护是正确折中

**存在性核查**：「config.toml 注册在列」=grep 实测 L23-27 输出（上方留痕）；「孤儿残片跳过」=源码分支 + 新增回归例 `test_..._v2` 双证。

**边界确认**：ROLE_PACE_MIN/全死自报通道/冷却语义/2×节奏判定均未动 ✅；hermes 侧 tick 属主归 #563 不越界 ✅。

**备注**：本单是我 liveness 建议书（心跳源单一）的根治执行——建议书方向 1（review/complete/claim 同挂心跳）被完整实现并超出（SessionHeartbeat 会话活跃面）。从误报实证到根治落地 <12h。**各角色 kimi 会话需重启才挂到钩**——老会话无 60s 拍，我的门铃 cron（30min myqueue 蹭拍）在重启前仍是我的活性来源，两轨互补。

**终审补记（2026-08-28 03:5x 欧阳锋）**：03:27 第七信号「总账未同步」拦截为**真阳性**——时序实证：code commit 03:02 无矩阵同改 → 拦截 03:27 → 我 PASS ~03:35（未察觉拦截，它落收件箱时我已在审）→ 黄药师补课 03:48（commit 4bcff2703：行 22 role-liveness 补登+行 5 更新多行聚合口径）。执行报告「无新增/变更信号不登记」的判定过窄：第五探针解析行为变更=行 5 描述过时、role-liveness 信号从未登记=行 22 缺漏，矩阵实则欠两行。**我的审查漏洞：落锤前未重读收件箱**——拦截与我的审查并发，review 命令未拒止（gate-blocked 对 review 无硬拦）。闭环现状：矩阵已同步，PASS A 结论不受影响（交付物质量与矩阵欠账无关），但过程教训入档：终审最后一步=重读收件箱，确认无新鲜拦截再落锤。
