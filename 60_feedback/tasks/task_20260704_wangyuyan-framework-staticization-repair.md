---
id: task_20260704_wangyuyan-framework-staticization-repair
type: task
status: reviewed
assignee: 老顽童
reviewer: 欧阳锋
reviewed_by: 欧阳锋
review_date: 2026-07-04
priority: P2
created_at: 2026-07-04
updated_at: 2026-07-04
source_task: task_20260704_laowantong-cross-domain-framework-iteration-audit
related:
- '[[yt-decision-y-model]]'
- '[[framework-yitang-jiefang-sixiang]]'
- '[[framework-yitang-shishi-qiushi]]'
- '[[framework-demand-iceberg]]'
- '[[framework-strategy-brm]]'
- '[[audit-framework-staticization-20260704]]'
- '[[method-yitang-y-model-engine-cycle]]'
---

# 任务 #79：框架卡静态化修复（5 张卡，分三级优先级）

## 审计来源

#68 跨域审计报告 `60_feedback/audits/audit-framework-staticization-20260704.md`

## 核心原则

**不重写，只加边界声明。** 静态工具就标明"这是静态工具，用完后用引擎循环收集反馈"。已通过终审的卡片不改已有内容，只追加新段落。

## 修复内容

### P0：yt-decision-y-model（4/12 · 全库根节点）

> 详细修复方案见老顽童已建任务单：`task_20260704_laowantong-fix-staticization-yt-decision-y-model.md`
>
> 摘要：
> 1. 新增"引擎层 vs 工具层"小节
> 2. 五步法改为循环图
> 3. 跨域迁移示例加引擎标注
> 4. Critique 加"作为静态工具的正确用法"
>
> 验收：`kdo pre-submit` PASS，`kdo lint` 0 新增 ERROR，欧阳锋终审

### P1：实事求是 + 解放思想（2/12 + 3/12 · Y模型子组件）

每张卡追加一个独立小节（3-5 行），不超 100 字：

**framework-yitang-shishi-qiushi：**

```
## 在 Y模型 引擎中的位置

实事求是是引擎循环的"校准"环节——每轮迭代中，用事实和数据检验假设是否成立。
它不是一次性做完的静态动作，而是每轮循环都会触发的检查点。
作为独立工具使用时，结论应进入 Y模型 引擎循环进行验证迭代。
```

**framework-yitang-jiefang-sixiang：**

```
## 在 Y模型 引擎中的位置

解放思想是引擎循环的"突破"环节——当实事求是暴露了假设不成立，解放思想负责提出新假设。
它不是凭空创新，而是在事实校准后跳出原有框架寻找新可能性。
作为独立工具使用时，产生的假设应进入 Y模型 引擎循环进行验证。
```

### P2：冰山 + BRM（1/12 + 1/12 · 非一堂域静态工具）

每张卡在 Critique 或边界小节追加一句话：

**framework-demand-iceberg：**

在 Critique 末尾追加一行：
> **引擎兼容性**：本框架为一次性诊断工具，诊断结论应作为 Y模型 引擎循环中"基础框架认知"的输入，通过假设验证迭代升级。单独使用不构成完整决策闭环。

**framework-strategy-brm：**

同上格式。

## 验收标准

- 5 张卡全部 `kdo pre-submit` PASS
- `kdo lint` 0 新增 ERROR
- P0：按老顽童已有任务单验收
- P1：两张卡各新增 1 个小节，含 Y模型 引擎位置声明
- P2：两张卡各追加 1 行 Critique
- related 互链完整（5 张卡之间 + 与 `method-yitang-y-model-engine-cycle` 的双向链接）
- 欧阳锋终审通过（只审新增段落，不重审全文）

## 依赖

- 依赖 #68 reviewed（审计报告为修复依据）
- P0 可与 P1/P2 并行提交
- P2 不阻塞 P0/P1 的终审

## 边界说明

- **不重写卡片**。已有内容质量没问题，只是缺少引擎模式定位声明。
- **不强改非一堂域卡**。冰山和 BRM 本身就适合静态工具形态，只需要声明边界。
- **不引入新 schema**。不新增 frontmatter 字段。
