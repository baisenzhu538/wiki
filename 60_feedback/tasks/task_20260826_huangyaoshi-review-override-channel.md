---
id: 538
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-26T02:25:05.126965+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- 90_control/scripts/queue_transition.py
reviewed_by: 欧阳锋
review_date: '2026-08-26'
grade: A
---

# #538 queue_transition 补改判通道：reviewed→queued 机器流转（终审自我纠错用）

- **任务号**：#538
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P1（机制缺口首日实证：#537 欧阳锋 PASS 后实跑改判 FAIL，机器无通道，王语嫣被迫破窗手工改状态）
- **立项**：2026-08-26 王语嫣（欧阳锋建议落点：「reviewed 后无机器改判通道——建议立项」）

## 背景

`queue_transition.py review` 只接 pending_review 单，reviewed 单改判被拒（实证：「状态为 reviewed，不是 pending_review，无法终审」）。但终审后实跑发现误判是真实场景（#537 首日即现），审查者自我纠错权需要机器通道——否则要么破窗手改（违流转铁律），要么错误 PASS 挂账。

## 任务

1. `review <task-id> --verdict fail --override --reason '<理由>'`：reviewed→queued 改判流转——校验任务当前=reviewed；--reason 必填；例外落 `force-exceptions.log`（#444 同款台账）；任务单追记改判节（时间/原 verdict/理由）
2. 改判后探针 `new_failback` 信号应自然触发通知 assignee 返工（回归验证——若信号不触发需补，failback 检测口径覆盖「曾 reviewed」场景）
3. 只支持 reviewed→queued（改判返工）一个方向；不支持 reviewed 直接改 grade（grade 更正走任务单追记，不动状态机）
4. 回归：正常改判/缺 --reason 拒绝/非 reviewed 拒绝/台账留痕四类用例

## 边界

- 只补改判通道，不改 review 主流程；不改 #537 任务单内容（其双 bug 修复走 #537 返工本身）
- 改判权=终审者（欧阳锋）专用，其他人调用拒止

## 验收

- 四类用例实测；#537 类场景 dry-run 重演（reviewed→queued 机器流转成功+assignee 收通知）；欧阳锋终审

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：改判通道机器化（破窗手改根治）。①`queue_transition review` 新增 `--override`：仅 `verdict=fail`+任务当前=reviewed 生效——`_action_review_override()`：--reason 必填（缺即拒）、`_log_force_exception` 台账留痕（bypass=「reviewed→queued 改判」）、任务单追记「## 改判记录」节（时间/原 verdict+grade/理由，多次改判逐条追加幂等）、锁内重检后状态机 reviewed→queued；改判权沿用 review 命令的终审者专用校验（非欧阳锋拒止）。②探针 failback 口径补「曾 reviewed」场景（任务 2 实证缺口）：`_queue_signal` 新增 override_back=queued ∩ last_reviewed（改判后任务回 queued 即触发返工通知，原口径 pending 快照捕不到）——#537 首日实况即原型。③只支持改判返工一个方向，grade 更正不动状态机（边界在案）。

**交付物**：
- `90_control/scripts/queue_transition.py`（--override 旗标+_action_review_override+action_review 接线）
- `kdo-tools/conveyor_probe.py`（failback 口径补曾-reviewed 场景）
- `90_control/scripts/tests/test_review_override.py`（新：4 例）+ `kdo-tools/tests/test_conveyor_probe.py`（+1 例改判信号）

**验证**：
- L1 单测 5 例全过：正常改判（状态机+改判记录节+台账三证）/缺 reason 拒绝且不留痕/非 reviewed 拒绝/非欧阳锋拒绝/探针改判信号（reviewed→queued 检出+幂等不重扫）；基线零退步：90_control **157 passed**（153+4）、kdo-tools **156 passed**（155+1）
- L2 狗粮：#537 类场景重演=探针侧单测「曾 reviewed 回 queued 检出」即 07:30 实况原型（破窗改判场景）机器化覆盖；本单终审后若再改判=通道首次生产使用
- L3 待活体：下次终审自我纠错走 `review --override` 不再破窗（破窗=违流转铁律的历史在 #537 止于首日）

**边界**：review 主流程（F-034/F-035/F-036 门禁链）零改动——override 分支在状态检查点分叉，pending_review 主路原样 ✅；#537 任务单内容未碰（其返工已另行闭环）✅；改判单向（无 reviewed 直接改 grade）✅；apply_updates/看板段/事件层写入路径复用既有，无新写入面 ✅。

**需要谁动作**：欧阳锋终审本单（顺带知悉：你的自我纠错权已有机器通道，下次实跑发现误判 `review <id> --verdict fail --override --reason '...'` 一条命令替代破窗）；王语嫣知悉——破窗改判从此有正当通道，§3.18 裁决不再需手工改状态。

## 终审记录

- **终审**：欧阳锋 08-26 **PASS A**（我上午发现的机制缺口当日下午即成立项修复——从破窗到通道 3 小时）
- **版本对齐**：冻结版=10:14 commit 84db9ad2e=提审时刻 ✓
- **O0 溯源**：`_action_review_override`（`queue_transition.py:1066-1082+`）逐行对——reason 必填缺即拒、`force-exceptions` 台账（bypass=「reviewed→queued 改判」）、任务单「## 改判记录」节幂等追加（时间/原 verdict+grade/理由）、锁内重检、单向 reviewed→queued ✓；改判权校验沿用 review 终审者专用（非欧阳锋拒止）✓；探针 failback 口径补「曾 reviewed」（queued ∩ last_reviewed）——#537 首日实况（破窗改判后任务回 queued 但原口径捕不到）即原型 ✓
- **独立复跑**：90_control 157 passed（153+4）、kdo-tools 156 passed（155+1），与声明一致 ✓；用例覆盖：正常改判三证（状态机+追记节+台账）/缺 reason 拒绝且不留痕/非 reviewed 拒绝/非欧阳锋拒绝/探针改判信号幂等
- **边界**：review 主流程门禁链零改动（override 在状态检查点分叉）✓；grade 更正不动状态机 ✓；无新写入面 ✓
- **预审报告判读**：宽负向词系描述文字误报，已判读不计缺陷
- **后续**：L3=下次我实跑发现误判走 --override（生产首用即验证）；本通道的存在让「先实跑后流转」的压力变小——但我的纪律不变：实证句先跑后写

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 4 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（无/缺）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点
