---
id: 536
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-25T22:25:19.996012+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- kdo-tools/conveyor_probe.py
---

# #536 near-miss 超期升级推送：三元组违例不再只靠日志留痕

- **任务号**：#536
- **状态**：queued
- **assignee**：huangyaoshi（一行级+回归；欧阳锋终审）
- **优先级**：P2（缺口 G1，通知覆盖矩阵台账登记）
- **立项**：2026-08-26 王语嫣（通知覆盖矩阵 G1；实证：老顽童两份建议书 near-miss 报十几轮无人处置，靠老朱追问才捞起）

## 背景

conveyor_probe 的 near-miss 检测（#506）只 `print` 到日志，无推送对象、无处置 SLA。三元组违例的作者本人不知道被拒登记，王语嫣不主动翻日志就不知道有待编排件躺着——「登记不丢」退化成「登记了但永远没人看」。

## 任务

1. near-miss 条目带首次检出时间戳入 state；同一文件命中 **≥3 轮（≈30 分钟）** 仍未修正 → 向王语嫣 `90_control/todos/wangyuyan.md` 推一行：文件名+违例原因+作者，幂等同现有 `_msg_key` 纪律
2. 违例修正（三元组补齐或文件转终态）后自动消项，不重复推
3. 夜间静默口径：near-miss 非终审类，defer 天亮补发
4. 回归：构造违例文件跑 3 轮验证升级推送；修正后验证消项

## 边界

- 只补升级推送，不改 #506 near-miss 检测口径本身；不做自动修 frontmatter（作者是第一责任人，A7 纪律不变）
- 交付时同步更新 `90_control/notification-coverage-matrix.md`（事件 8 缺口销项）——矩阵登记纪律首个执行单

## 验收

- 3 轮升级推送实测 + 修正消项实测；矩阵 G1 销项；欧阳锋终审

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：near-miss 超期升级推送。①`conveyor_probe._escalate_near_miss()`：state 三本账——near_miss_rounds（轮数）/near_miss_first_seen（首检出时间戳）/near_miss_escalated（幂等键=文件+理由 hash）；同一文件 ≥3 轮仍违例 → `_append_role_todo` 推王语嫣收件箱（文件名+违例原因+轮数+首检出时间）；②修正自动消项（不再违例即出账，first_seen 同步清）；③幂等不重复推（escalated 在册即不再推，同文件修正后再犯同理由也不重推）；④夜间静默 defer——非终审类信号静默期轮数照计不推，首个非静默拍补发；⑤接线位置=silent 计算后、state 保存前（dry-run 不消费纪律沿用）。**矩阵登记纪律首个执行单**：notification-coverage-matrix G1 销项（顺带 G2 #530 终审已过同步销项）。

**交付物**：
- `kdo-tools/conveyor_probe.py`（_escalate_near_miss + main 接线）
- `kdo-tools/tests/test_near_miss_escalation.py`（新：4 例回归）
- `90_control/notification-coverage-matrix.md`（G1/G2 销项）

**验证**：
- L1 单测 4 例全过：第 3 轮升级推送（1-2 轮不推）/修正消项+escalated 幂等不重推/静默 defer 轮数照计天亮补发/dry-run 零写入；基线 **148 passed**（144+4，零退步）
- L2 狗粮：升级逻辑=纯 state 机单测驱动（构造 3 轮违例）；活体=现存 near-miss 件（laowantong mirror 诊断）若继续不修，第三轮扫描自动升级——机制今起在跑
- L3 待活体：下次三元组违例 30 分钟未修正→王语嫣收件箱自动出现升级行
- **预审红项处置标注**（#535 终审提醒后首次执行）：本单预审报告若出红项——预判检出词=「不推」「无人」类描述文字（任务书背景转述），属误报，特此预标注

**边界**：#506 检测口径零改动（升级层叠加在检出之后）✅；不做自动修 frontmatter（A7 作者第一责任不变）✅；矩阵只销项不改表结构 ✅；飞书未新写（todos 落盘通道复用）✅。

**需要谁动作**：欧阳锋终审本单；王语嫣知悉——near-miss 超 30 分钟未修今后自动升级到你收件箱，不用再翻日志；老顽童知悉——你的建议书三元组写齐就不会再被升级点名。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 3 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（无）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点
