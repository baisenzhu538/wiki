---
id: 537
assignee: huangyaoshi
status: queued
updated_at: '2026-08-26T03:30:00+00:00'
version: v0.1
instance: huangyaoshi
code_files:
  - kdo-tools/conveyor_probe.py
  - 90_control/notification-coverage-matrix.md
---

# #537 总账登记机器核查：基础设施单 reviewed 时矩阵未同步→拦截提醒

- **任务号**：#537
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P1（charter §3.19 目前纯文档纪律，无机器兜底=今日同款结构性风险，老朱追问「是不是有基础设施来保障」立项）
- **立项**：2026-08-26 王语嫣

## 背景

§3.19 矩阵强制登记已入宪，但执行保障是人脑两级（王语嫣立项记得写验收项/欧阳锋终审记得查）。本库全部教训指向同一结论：**文档纪律必须配机器信号**（#460 门禁自报/#506 near-miss 同款逻辑）。conveyor_probe 补第七信号，让「登记被遗忘」在 10 分钟内显形。

## 任务

1. **第七信号：总账登记核查**——conveyor_probe 检测新 reviewed 任务单，若其 `code_files` 触及基础设施面（初版清单：`kdo-tools/conveyor_probe.py`、`kdo-tools/watch_inbox.py`、`90_control/scripts/queue_transition.py`、`kdo-tools/generate-dashboard.py`，清单集中定义便于扩）→ 核查该 reviewed commit（或相邻 3 笔内）是否同改 `90_control/notification-coverage-matrix.md`
2. **未同步 → 双推**：欧阳锋「⛔ 总账未同步：#N 触碰基础设施但矩阵未更新，终审暂缓闭环」+ 抄送王语嫣；同步了 → 静默通过
3. **豁免口径**：任务单 frontmatter 标 `matrix_exempt: true`（注明理由，如不涉及事件/通道变更的纯重构）→ 跳过核查，豁免本身落 force-exceptions 台账留痕（#444 同款）
4. WARNING 起步、只向前生效，不回扫历史单；幂等+夜间静默口径同现有纪律
5. 回归：构造触发/豁免/已同步三类用例

## 边界

- 只核查「登没登」，不判「登得对不对」（内容质量仍欧阳锋人审——机器做存在性，人做正确性，#433 同哲学）
- 基础设施面清单初版宁窄勿宽，误报比漏报贵；扩充走后续单
- 本单交付时自身即首个被核查对象：矩阵事件表需同步补第七信号行（元狗粮）

## 验收

- 三类用例实测输出；矩阵补第七信号行+G 台账口径更新；欧阳锋终审
