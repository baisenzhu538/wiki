---
id: task_20260704_laowantong-fix-staticization-consolidated
type: task
status: queued
assignee: 老顽童
reviewer: 欧阳锋
priority: P0
created_at: 2026-07-04
updated_at: 2026-07-04
source_task: task_20260704_laowantong-cross-domain-framework-iteration-audit
related:
- "[[audit-framework-staticization-20260704]]"
- "[[task_20260704_laowantong-fix-staticization-yt-decision-y-model]]"
---

# 任务 #79：跨域静态化修复（合并 P0+P1+P2）

## 来源

审计报告 `audit-framework-staticization-20260704` 发现 5 张高风险卡 + 1 张中风险卡需修复。本任务合并所有修复，按优先级分批执行。

## P0：yt-decision-y-model 引擎化升级（1 张）

详细方案见 `task_20260704_laowantong-fix-staticization-yt-decision-y-model.md`（参考资料，不入队）。

五项改动：
1. 新增"引擎层 vs 工具层"小节
2. 五步法改为循环图
3. 跨域迁移示例加迭代标注
4. 新增"朴素起点"小节
5. Critique 内部局限增加"引擎层被忽略"

## P1：实事求是 + 解放思想引擎化（2 张）

### framework-yitang-shishi-qiushi（2/12 → 目标 8/12）
- 增强"在 Y模型 引擎循环中的位置"节
- 增加触发条件："什么时候需要跑实事求是校准？"
- 展开验证成本阶梯
- 增加"校准后下一步"指引

### framework-yitang-jiefang-sixiang（3/12 → 目标 8/12）
- 增强"在 Y模型 引擎循环中的位置"节
- 增加"从 L0 到 L4 的修炼路径"
- 增加触发信号和"解放后下一步"指引

## P2：冰山 + BRM 边界声明（2 张）

### framework-demand-iceberg（1/12 → 目标 5/12）
- 增加"冰山模型的迭代使用"节
- L6 之后增加循环箭头（假设被推翻→回到 L3）
- 增加"什么时候不需要走完六层"的边界声明

### framework-strategy-brm（1/12 → 目标 5/12）
- 增加"BRM 的适用边界"：它是规划工具，不是迭代引擎
- 增加"BRM 与 Y模型 的关系"

## 验收标准

- 每张修改卡 `kdo pre-submit` 通过
- 每张卡审计得分提升到目标值以上
- P0 优先，P1/P2 可分批提交
- 欧阳锋终审通过
