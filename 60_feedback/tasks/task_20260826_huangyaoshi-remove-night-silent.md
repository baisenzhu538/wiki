---
id: 550
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-26T20:52:31.486338+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- kdo-tools/conveyor_probe.py
- kdo-tools/watch_inbox.py
- kdo-tools/on_duty.py
- kdo-tools/tests/test_on_duty.py
- kdo-tools/tests/test_watch_inbox.py
- 90_control/infrastructure-inventory.md
- 90_control/todos/wangyuyan.md
---

# #550 取消夜间静默：时段静默→在岗判定（老朱直令）

- **任务号**：#550
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P1（老朱 08-26 直令，可插队；夜间 agent 协作链路静默断连实证=今晚 23:00+ 王语嫣裁定批期间通知面静默）
- **立项**：2026-08-26 王语嫣（老朱直令：「取消夜间探针和时钟静默，只要 kdo 的 agent 在岗，都必须激活，而且角色级别不能受到影响」）

## 背景

现有静默=**时段制**：`conveyor_probe.py:51` 与 `watch_inbox.py:31` 同口径 `SILENT_START_HOUR, SILENT_END_HOUR = 22, 8`——22:00-08:00 登记照常、通知不发（终审类经 `_split_silent_exempt` 豁免照推，其余天亮补发）。时段制的假设=「夜间无人在工作」，已被证伪：工厂夜间 agent 在岗协作是常态（08-25/08-26 两夜实证），通知接收方不只是老朱，更是在岗的 agent 同事——静默期=协作链路断连。

## 任务

1. **静默条件改写**：时段判定 → 在岗判定。**有 agent 在岗 = 全激活**（通知照发）；无 agent 在岗 = 可静默（登记照常+补发机制保留）
2. **在岗机器判定口径**（满足其一即在岗，窗口 30 分钟对齐 L1 节拍）：
   - 事件库最近 30 分钟有新事件（⚠️ 排除 conveyor_probe 自身写入的事件类型——否则探针每 10 分钟自证在岗=判定失效，循环依赖）
   - L1 采集层最近 30 分钟有新会话原文文件
3. **角色级别统一**：删除 `_split_silent_exempt` 的终审类豁免分级——激活/静默判定全角色全信号类型统一口径，不按角色或信号类型差异化。通知路由（按 assignee）不动
4. **覆盖两个脚本**：conveyor_probe.py + watch_inbox.py 同口径改造；`--force-notify` 人工豁免保留
5. **§3.19**：交付时通知王语嫣更新通知覆盖矩阵 defer 列口径（「非终审类静默」语义作废）

## 边界

- 只改通知层静默判定，不动各角色时钟频率、不动登记/补发/幂等机制
- 在岗判定宁可误激活不可误静默（误激活=多发通知，误静默=协作断连——不对称偏误拦方向）
- 判定信号都不可得时（事件库/L1 都读不到）→ 默认**激活**（静默是例外不是默认）

## 验收

- 单测：模拟「有事件流=激活」「无事件流=静默」「探针自身事件不计入」三用例
- 活体：今夜（静默时段内）王语嫣/黄药师在岗期间探针通知真实送达
- 回归：既有限流/幂等/补发机制不受影响；欧阳锋终审


## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：时段静默 → 在岗判定（双脚本同口径）。①**共享判定模块** `kdo-tools/on_duty.py`（单一判定源，禁双份实现）：事件库近 30 分钟非机器事件（排除 friction=探针镜像写入/token_usage=计量自写——防探针自证在岗循环依赖）OR L1 当日目录近 30 分钟新文件（首新鲜即短路）→ 在岗；双信号不可得 → **默认激活**（静默是例外不是默认）；②**conveyor_probe 改造**：silent 判定换 on_duty；**删除 `_split_silent_exempt` 终审豁免分级**——无在岗时全角色全信号统一 defer（pending_notify 补发机制不动，触发条件从「天亮」变「在岗」）；`--force-notify` 保留；③**watch_inbox 同口径**：通知 🔕/📥 判定同源切换，注释口径同步改写；④§3.19：矩阵 defer 列口径更新按任务书指派**通知王语嫣**（已落她收件箱，含新旧语义对照）；on_duty 登记 infrastructure-inventory。

**交付物**：
- `kdo-tools/on_duty.py`（新：共享判定模块）
- `kdo-tools/conveyor_probe.py`（静默判定换岗+豁免分级拆除）
- `kdo-tools/watch_inbox.py`（同口径）
- `kdo-tools/tests/test_on_duty.py`（新 6 例）+ `kdo-tools/tests/test_watch_inbox.py`（静默用例改写在岗口径）+ 删除 `test_conveyor_silent_exempt.py`（被测函数随 #550 废除）
- `90_control/infrastructure-inventory.md`（on_duty 登记）+ `90_control/todos/wangyuyan.md`（矩阵口径更新通知）

**验证**：
- L1 单测：on_duty 6 例全过（验收三用例：有事件流=激活/无事件流=静默/探针自身 friction 不计入；外加 L1 新文件=激活/双信号不可得=默认激活/probe 源码无分级残留断言）；基线：kdo-tools **187 passed**（旧豁免 4 例随函数废除删除，净 175+6+1 改写），90_control **177 passed** 零退步
- L2 狗粮：真机 `any_agent_on_duty()` 实测返回 `True — 事件库近 30 分钟有新事件`（本夜班真实在岗证据）；probe `--dry-run` 全链正常（05:0x 原静默时段内判定在岗不静默）
- L3 待活体：今夜再有通知事件时真实送达（补发队列若有存量将在本轮在岗判定下清空）
- **预审红项预标注**：预审若检「废除/删除/不」类词=任务书要求的拆除动作（删 `_split_silent_exempt` 是任务 3 明文要求），预标注在此；负向断言「无残留」**存在性核查**=grep `exempt_roles|_split_silent_exempt` conveyor_probe.py 零命中+测试断言锁死

**边界**：只改通知静默判定 ✅；时钟频率/登记/补发/幂等机制不动 ✅；通知路由（assignee）不动 ✅；矩阵 defer 列正文更新归王语嫣（任务书指派）✅。

**需要谁动作**：欧阳锋终审本单；王语嫣按收件箱说明更新矩阵 defer 列口径。
