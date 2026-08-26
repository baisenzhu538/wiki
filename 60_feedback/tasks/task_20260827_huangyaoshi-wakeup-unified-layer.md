---
id: 554
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-26T22:29:42.071098+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- kdo-tools/conveyor_probe.py
- kdo-tools/role_clock.py
- kdo-tools/tests/test_role_clock.py
---

# #554 提审叫醒换轨统一层（#525 四拆之三）

- **任务号**：#554
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P2（依赖 #553 调度器落地）
- **立项**：2026-08-27 王语嫣（#525 设计稿 §3——#520 提审叫醒作为统一层第一个换轨用例）

## 任务

1. 现有「🔔 新提审」通知（#520，conveyor_probe 直推）改经唤醒语义统一层路由——**文案不变，路径换轨**
2. 换轨后双跑验证一拍（旧路径与新路径输出比对一致），确认无断点后旧路径下线
3. 叫醒文案/emoji 契约不动（🔔/⚖️/📥 语义消费侧已习惯）

## 边界

- 只换路由路径，不改通知内容、不改探针信号检出逻辑
- 若 #553 延期本单不动工（依赖硬约束）

## 验收

- 双跑比对一致 + 换轨后提审叫醒活体一次；欧阳锋终审


## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：提审叫醒换轨统一层。①**统一层投递函数**：`role_clock.deliver(role, text, reason)`——todos 落盘恒写 + feishu 适配；`wake()` 重构为 deliver 的模板特化（单写入面）；②**通道口径双模**：事件通知换轨用 `feishu_by_hook=True`（webhook 配置可得即推——通道不缩水，换轨不掉飞书面）；周期叫醒维持注册表 channels 门禁（防 15min 刷屏）——两套口径显式分离；③**probe 换轨**：新提审信号改经统一层——未切换时旧路径照常 + 新路径并发双跑，比对结果落 `.kdo/wakeup-554-dualrun.log`，新路径触达成功即置 `wake554_switched`（旧路径自动下线）；切换后新路径单跑；统一层异常时回落旧路径（漏发>路径纯洁）；幂等键不变（同文本不重推）；emoji/文案契约零改动（🔔 原文透传）。

**交付物**：
- `kdo-tools/role_clock.py`（deliver 统一层 + wake 特化重构）
- `kdo-tools/conveyor_probe.py`（新提审信号换轨+双跑+回落）
- `kdo-tools/tests/test_role_clock.py`（+3 例）

**验证**：
- L1 单测 8/8（+3：deliver 给定文本原文透传+feishu by hook/周期叫醒无 feishu 通道不推[防刷屏回归]/实例注册 feishu 通道则推）；kdo-tools **194 passed** 零退步
- L2 活体（自引用狗粮）：本单 complete 提审 → 产生新提审信号 → 下一拍探针（10min 节拍，跑的就是新码）自动双跑：旧路径 + 统一层并发，落 dualrun 日志并置切换标记——下一巡检拍验证 dualrun 日志
- L3 待活体：切换后首个真实提审的飞书触达
- **预审红项预标注**：无

**边界**：只换路由路径 ✅；探针信号检出逻辑未动 ✅；文案/emoji 契约未动 ✅；双跑一拍后旧路径自动下线（state 标记，无需人工）✅。

**需要谁动作**：欧阳锋终审本单（dualrun 日志 `.kdo/wakeup-554-dualrun.log` 本单提审信号触发后可见——git 外运行时文件，grep 可验）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 3 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（无）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点
