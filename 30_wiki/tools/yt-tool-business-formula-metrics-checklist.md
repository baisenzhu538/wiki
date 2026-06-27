---



id: yt-tool-business-formula-metrics-checklist
title: 业务公式数据埋点设计清单
type: tool
status: enriched
domain:
  - src_unknown
  - src_unknown
  - src_unknown
source_refs:
- src_20260613_6b939d2b-yitang-business-formula-decomposition-transcript
- src_20260613_6edbf0af-yitang-business-formula-decomposition-notes
- src_20260613_a8bcfd38-yitang-business-formula-decomposition-oral
tags:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
created_at: '2026-06-16'
updated_at: '2026-06-16'
author: 孔阳
reviewed_by: 老顽童
review_date: '2026-06-16'
confidence: 0.88
trust_level: high
related:
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown

---# 业务公式数据埋点设计清单

> 业务公式拆到 L3-L4 后，每个定性参数都需要 3-5 个可定量的行为指标来佐证。本清单帮助你在提出假设的同时，把数据埋点一起设计好，避免“拆完公式却无从验证”。来源：一堂 2026-06-13 业务公式拆解培训（孔阳）。

---

## 核心原则

1. **假设与埋点同时出**：没有埋点的假设只是猜测。
2. **一个定性参数 → 3-5 个行为指标**：太少容易以偏概全，太多容易失去焦点。
3. **每个指标都能追溯到动作**：指标变了，必须知道该动哪个环节。
4. **先埋点再优化**：优化动作上线前，埋点必须先上线。

---

## 七步设计清单

### 1. 明确你要验证的假设

| 检查项 | 示例 |
|---|---|
| 假设是否可证伪？ | “优化落地页可提升转化率” vs “我们要把品牌做好” |
| 假设与哪个业务结果挂钩？ | 转化率、复购率、续费率、GMV |
| 假设属于哪一层参数？ | L3 抓手层 / L4 定性参数层 / L5 本质层 |

**不合格示例**：“提升用户信任度”（无法直接量化）  
**合格示例**：“详情页下滑完成率从 45% 提升到 80%，将带来支付转化率提升”

---

### 2. 识别定性参数

从公式拆解中找出无法直接测量的参数：

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

> 完整指标库参考：[[yt-business-formula-qualitative-metrics-library]]

---

### 3. 为每个定性参数选择 3-5 个行为指标

| 定性参数 | 行为指标 1 | 行为指标 2 | 行为指标 3 | 行为指标 4 |
|---|---|---|---|---|
| 信任度 | 详情页停留时长 | 详情页下滑完成率 | 评价区停留时长 | 试听课完课率 |
| 使用深度 | 月活账号率 | 核心功能使用率 | 周活跃天数 | 关键角色参与度 |
| 复购触发 | 7 天优惠券核销率 | 生日券核销率 | 新品 Push 打开率 | 消耗周期提醒触达率 |

选择标准：
- src_unknown
- src_unknown
- src_unknown

---

### 4. 设定基准值与目标值

| 指标 | 当前值 | 行业基准 / 历史基准 | 目标值 | 达成时间 |
|---|---|---|---|---|
| 详情页下滑完成率 | 45% | 80% | 70% | 4 周 |
| 核心功能使用率 | 30% | 50% | 50% | 8 周 |
| 7 天优惠券核销率 | 8% | 20% | 15% | 6 周 |

设定原则：
- src_unknown
- src_unknown
- src_unknown

---

### 5. 明确数据来源与埋点位置

| 指标 | 数据来源 | 埋点位置 | 事件定义 | 负责人 |
|---|---|---|---|---|
| 详情页下滑完成率 | 前端埋点 | 商品详情页 | 用户滑动到页面 80% 位置 | 产品 / 数据 |
| 核心功能使用率 | 后端埋点 | 功能模块调用日志 | 30 天内调用过核心功能 | 后端 / 数据 |
| 7 天优惠券核销率 | 交易数据 | 优惠券系统 | 领取后 7 天内使用 | 运营 / 数据 |

埋点设计注意：
- src_unknown
- src_unknown
- src_unknown

---

### 6. 建立监控与复盘机制

| 机制 | 频率 | 参与人 | 输出 |
|---|---|---|---|
| 指标看板 | 实时 / 每日 | 业务负责人 | 核心指标趋势 |
| 假设验证会 | 每周 | 产品 + 运营 + 数据 | 哪些假设被验证 / 证伪 |
| 公式复盘会 | 每月 / 每季度 | 管理层 | 公式是否需要更新 |

关键问题：
- src_unknown
- src_unknown
- src_unknown

---

### 7. 形成闭环：从埋点到公式迭代

```
拆解公式 → 提出假设 → 设计埋点 → 上线优化 → 验证假设 → 更新公式
     ↑___________________________________________________________↓
```

如果假设被验证，把该参数和关系固化进业务公式；  
如果假设被证伪，回到公式拆解层，检查是否选错了范式、拆错了参数或写错了运算符号。

---

## 快速检查表

在启动任何业务公式优化项目前，对照以下问题自查：

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

全部勾选后，再动手改业务。

---

## 常见错误

1. **只优化不埋点**：上线后无法判断效果。
2. **指标与动作脱节**：指标变了但不知道下一步做什么。
3. **只盯结果指标**：GMV 涨了不知道原因，跌了找不到抓手。
4. **忽视对照组**：无法区分是自然波动还是优化带来的效果。
5. **埋点命名混乱**：同一个行为在不同系统里叫不同名字，无法汇总分析。

---

## 与业务公式其他工具的协作关系

| 工具 | 作用 | 与本清单的关系 |
|---|---|---|
| [[yt-business-formula-business-pattern-selector]] | 判断业务类型 | 决定先拆哪类公式、先埋哪些指标 |
| [[yt-business-formula-qualitative-metrics-library]] | 提供行为指标库 | 本清单的“指标素材库” |
| [[yt-business-formula-abc-model]] | 定义目标/参数/关系 | 确定要验证的假设和参数关系 |
| [[dk-yitang-business-formula-plus-times-trap]] | 避免 +/× 写错 | 确保指标关系与公式关系一致 |

---

## 置信度说明

- src_unknown
- src_unknown
- src_unknown
