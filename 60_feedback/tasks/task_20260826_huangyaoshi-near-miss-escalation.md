---
id: 536
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-25T22:22:12.850840+00:00'
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
