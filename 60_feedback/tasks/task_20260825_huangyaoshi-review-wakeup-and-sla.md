---
id: 520
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-25T04:16:07.064572+00:00'
version: v0.1
instance: huangyaoshi
---

# #520 审查供给端三件套：提审叫醒审查者 + 阻塞链标记 + 审查 SLA 观测

- **任务号**：#520
- **状态**：queued
- **assignee**：huangyaoshi（探针/看板/健康检查扩展；欧阳锋终审）
- **优先级**：P1（#505 实证：提审后审查供给靠"老朱发现卡点手动叫人"——锁修得越好审查卡点越硬）
- **立项**：2026-08-25 王语嫣（欧阳锋建议书 `diag_20260825_ouyangfeng-review-bottleneck-wakeup.md` R1+R2+R3 裁定采纳同批；R4 挂停车场待老朱拍板）

## 背景

08-25 00:51 #505 提审 → 黄药师 #506-#511 依赖链被 can_claim 全线阻塞（#503/#504 修好的锁在正常工作）→ 直到老朱发现卡点手动唤起欧阳锋才解封。**审查供给的触发器=用户想起**——门禁完善的副作用是审查供给成为唯一瓶颈，必须配套供给端机制。三个缺口：①叫醒方向缺失（有"审完→通知生产者"，无"提审→叫醒审查者"）②阻塞链无优先级（REVIEW-PENDING 段内同权，#505 这类挂着 6 个依赖单的关键单看不出）③降级机制错配（分级审查触发器是"积压量"，对"单点阻塞关键链"无机制）。

## 任务

1. **R1 提审叫醒通道**：conveyor_probe 增加 REVIEW-PENDING 段新行检测 → 通知审查端（复用 #462 双通道 + #501 收件箱落盘，飞书推 ouyangfeng + CLI 落 todos/ouyangfeng.md）；最小实现=探针比对 REVIEW-PENDING 最新行 task_id，变化即推；**终审完成类信号豁免夜间静默**（老朱 08-25 已拍板豁免范围，与 #521 同口径）
2. **R2 阻塞链标记**：看板生成（generate-dashboard）对「后方有同角色 queued 单」的 pending_review 行加 🔴阻塞链 标记——审查者进队列先审阻塞单
3. **R3 审查 SLA 观测**：health-check 增「pending_review 最大年龄」指标，超阈值（2h）入巡检报告——卡点从被发现变被预测

## 验证（验证分层）

- L1：单测——REVIEW-PENDING 新增行触发通知（幂等，重跑不重复推）；阻塞链标记逻辑对样例队列正确
- L2 狗粮：制造一次提审 → 欧阳锋收件箱/飞书收到叫醒（夜间也到，豁免生效）
- L3 待活体：下一次提审→终审时延不再=老朱发现时延

## 边界

- **依赖 #519**（探针计划任务空转修复——叫醒通道建在探针上，探针不稳则本单白建；同文件区防冲突）
- R4（阻塞链超时 force 应急通道）**不在本单**——涉审查权下放边界，挂 F-056 待老朱拍板
- 不改审查标准本身（分级审查协议不动）；只补供给端叫醒与优先级
- 审查者侧自律已同步生效（欧阳锋会话启动即查 REVIEW-PENDING），机制归机制不替代自律

## 关联

- 欧阳锋建议书 R1-R3（实证表完整：#505 提审→解封时延=用户发现时延）
- #519（探针空转修复，先行依赖）/ #462（审查完成通知通道）/ #501（收件箱机制）/ #504（审查等待期阻塞策略——本单是其供给端配套）
- F-056（R4 应急通道，待拍板）

## 需要谁动作

- **黄药师**：三件套施工（#519 后）
- **欧阳锋**：终审本单；自律侧已生效

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：审查供给端三件套。①**R1 提审叫醒通道**：实测探针已有 `new_review → messages["ouyangfeng"] 🔔新提审`（#519 终审活体实证：通知链复活后欧阳锋收到的第一条就是叫醒）——本单补的是**夜间静默豁免**：新增 `_split_silent_exempt()`（终审类信号 exempt_roles 照常推，其余进 pending 天亮补发；失败留 pending 重试不丢），F-036 提醒覆盖叫醒文本时摘除豁免（豁免跟随最终文本类别）；②**R2 阻塞链标记**：`generate-dashboard.py` 新增 `_mark_blocking_chains()`——pending_review 且后方（seq 更大）有同角色 queued 单 → 看板卡片打 🔴阻塞链 红色徽章（新 CSS g-BLOCK）；③**R3 审查 SLA 观测**：新 `check-review-sla.py`——解析 REVIEW-PENDING 段活跃行（划掉行跳过、跨年回退、无年份按今年），最大年龄 >2h → exit 1，挂入 health-check 每日 02:07。

**交付物**：
- `kdo-tools/conveyor_probe.py`（_split_silent_exempt + 静默期分级 + F-036 覆盖摘豁免）
- `kdo-tools/generate-dashboard.py`（_mark_blocking_chains + 🔴阻塞链 徽章 + g-BLOCK CSS）
- `90_control/scripts/check-review-sla.py`（新）+ `90_control/scripts/tests/test_check_review_sla.py`（5 例）
- `kdo-tools/tests/test_conveyor_silent_exempt.py`（4 例）+ `kdo-tools/tests/test_dashboard_blocking.py`（5 例）
- `90_control/scripts/health-check.py`（挂 check-review-sla）+ `90_control/infrastructure-inventory.md`（登记）

**验证**：
- L1 单测 14 例全过：静默分级 4 例（豁免通过/非豁免 defer/混合拆分/空豁免集）；阻塞链 5 例（后方同角色标记/前方不算/他人角色不算/queued 永不标/徽章入 HTML）；SLA 5 例（新鲜 0/超龄 1/划掉行跳过/零积压/段标记缺失）。基线零退步：kdo-tools **107 passed**（98+9）、90_control/scripts **126 passed**（121+5）
- L2 狗粮：R2 探针队列（505 审查中+506 同角色后方+507 他人）→ 仅 505 标记、HTML 恰 1 个徽章 ✅；R3 活体直跑「零积压」exit 0 ✅；R1 夜间豁免分支=单测覆盖+本单提审即真实叫醒（白天非静默期）；本单 complete 后 #520 自身成 pending_review 且后方 #521-523 同角色 queued → 看板将自证阻塞链标记（有机活体）
- L3 待活体：夜间（22-08）真实提审叫醒即时到达（豁免分支活体验证）；下次提审→终审时延≠老朱发现时延

**边界**：叫醒复用既有 #462/#501 双通道未新造 ✅；R4 应急通道未动（F-056 待拍板）✅；审查标准/分级协议未动 ✅；FAIL 通知（failback）路由未动；#521 的 PASS 按 assignee 路由生产者**不在本单**（队列顺序 #521 下一单，豁免机制已留 exempt_roles 可直接复用）。

**需要谁动作**：欧阳锋终审本单；老朱知悉——今晚起夜间提审叫醒不再被静默压住（拍板口径已落地）；各角色知悉——看板 🔴阻塞链 标记上线，pending_review 超 2h 会在每日健康检查显形。
