---
id: tool-demand-report-template
title: 需求分析报告模板——TAM/SAM/CR1 + 策略 + 假设 + 元认知提醒
type: tool
status: enriched
confidence: 0.92
trust_level: high
domain: yitang
source_refs:
- src_unknown
- 30_wiki/tools/tool-demand-iceberg-l6-hypothesis.md
- 30_wiki/frameworks/framework-demand-opportunity-spectrum.md
created_at: '2026-06-21'
updated_at: '2026-06-21'
author: 黄药师（从 Coze 报告结构提取 + KDO 框架映射）
reviewed_by: 欧阳锋
related:
- [[tool-demand-iceberg-l6-hypothesis]]
- [[framework-demand-opportunity-spectrum]]
- [[yt-market-size-estimation]]

---

# 需求分析报告模板

> 端到端报告结构。Agent 跑完需求分析后，按此模板输出——不只是"分析结论"，是可投递给用户的完整报告。

## 报告结构总览

```
一、项目简介           → 一句话+商业模式+当前困惑
二、市场规模总览        → TAM/SAM/CR1 速览表
三、TAM 分析           → 双路径交叉验证
四、SAM 分析           → 四把砍刀 + 测算
五、CR1 头部天花板     → 规模经济性/壁垒/集中度/演化阶段
六、经营策略建议       → 天花板定位/核心能力/团队/节奏
七、关键假设清单        → 最危险假设 + 验证方式
八、后续步骤建议        → 优先验证/数据更新/应用场景
九、最重要提醒 🆕       → 跳出框架的元认知
```

## 逐节模板

### 一、项目简介

```markdown
## 一、项目简介

提供 [一句话说清做什么]，主要面向 [客户类型]。业务已运营 [X]年，采用 [商业模式]。当前面临 [战略困惑/核心问题]。

> **📌 阅读须知**：本报告是一次结构化的思考过程，而非定论。数字标注了置信度（✅已知/⚠️行业经验/🔮推测），仅供参考。重大决策请结合一手调研和实时数据验证。市场动态变化，建议定期回顾、修正、迭代。
```

### 二、市场规模总览

```markdown
## 二、市场规模分析总览

| 层级 | 名称 | 数值（中位估算） | 合理区间 | 置信度 |
|------|------|--------------|---------|--------|
| TAM | 总可寻址市场 | [X] 亿元/年 | [Y]～[Z] 亿 | ⚠️ |
| SAM | 可服务市场 | [X] 亿元/年 | [Y]～[Z] 亿 | ⚠️ |
| CR1 | 头部天花板 | [X] 万元/年 | [Y]～[Z] 万 | 🔮 |
```

**置信度标注体系**：

| 标记 | 含义 | 何时用 |
|:--|:--|:--|
| ✅ | 已知数据——有公开可查的官方来源 | 引用统计局/上市公司年报/权威报告时 |
| ⚠️ | 行业经验——基于行业常识和逻辑推演 | 引用行业报告/专家访谈/类比推断时 |
| 🔮 | 合理推测——缺少直接数据，基于间接信号推断 | 前提假设多、数据稀疏时 |

> KDO 原有 `confidence` 0-1 字段保留（机器可读）。✅⚠️🔮 是人读的快速标注。

### 三、TAM 分析

```markdown
## 三、TAM 分析

### 3.1 问题品类定义
[用一句话定义用户"雇佣"这个产品要完成的任务——方案中立]

### 3.2 测算过程
**路径A：自上而下（Top-Down）**
- src_unknown
- src_unknown
- src_unknown

**路径B：自下而上（Bottom-Up）**
- src_unknown
- src_unknown
- src_unknown
- src_unknown

### 3.3 结论
TAM 合理区间为 [X]～[Y]。两条路径结果[吻合/偏差大——为什么]。关键不确定性：[列出最影响数字的2-3个假设]。
```

> 映射：`yt-market-size-estimation`（市场规模估算四种方法）

### 四、SAM 分析

```markdown
## 四、SAM 分析

### 4.1 切割逻辑
从 TAM 切割到 SAM 的限制维度：

| 限制维度 | 切割逻辑 | 保留比例 | 置信度 |
|---------|---------|---------|--------|
| [限制1] | [为什么这一刀砍掉多少] | [X]% | |
| [限制2] | ... | ... | |
| [至少列3-4个维度] | | | |

### 4.2 测算过程
TAM（[X]）× 综合保留比例（[Y]%）= SAM：[数字]

### 4.3 结论
在当前商业模式和约束下，实际可触达市场约为 [X]～[Y]。[主要限制因素]。
```

### 五、CR1 头部天花板分析

```markdown
## 五、CR1 头部天花板分析

### 5.1 规模经济性评估
**正向因素**：[列出]（评分：强/中/弱）
**负向因素**：[列出]（评分：强/中/弱）
**净判断**：规模经济性 **[强/中等/弱]**

### 5.2 壁垒分析
| 壁垒类型 | 强度 | 说明 |
|:--|:--|:--|
| 技术壁垒 | [强/中/弱] | |
| 转化成本 | | |
| 无形资产 | | |
| 网络效应 | | |

### 5.3 集中度判断
**[集中/相对分散/百花齐放]型**
- src_unknown
- src_unknown
- src_unknown

### 5.4 市场演化阶段
**[赢家通吃/寡头稳定/百花齐放/...]型**
- src_unknown
- src_unknown

### 5.5 CR1 估算
SAM（[X]）× CR1比例（[Y]%）= **头部天花板：[X]～[Y]/年**
```

> 映射：`five-step-barrier`（壁垒）+ `framework-demand-opportunity-spectrum`（终局光谱）

### 六、经营策略建议

```markdown
## 六、经营策略建议

### 6.1 天花板定位
基于 CR1 测算，头部天花板约为 [X]～[Y]/年。意味着：
1. 赛道定性：[独角兽赛道 / 现金流业务 / 小而美]
2. 天花板判断：[能/不能]支撑大规模融资
3. 战略启示：[一句话]

### 6.2 核心资源与能力要求
**要做到头部需要构建：**
1. [能力1]
2. [能力2]

**瓶颈所在：**
1. [瓶颈1]
2. [瓶颈2]

### 6.3 团队与发展节奏
**团队配置建议**：[关键角色 + 为什么]
**发展节奏**：
1. **阶段一（0-1年）：聚焦验证** — [做什么]
2. **阶段二（1-3年）：区域复制** — [做什么]
3. **阶段三（3-5年）：生态构建** — [做什么]

### 6.4 关键决策点
**成败关键节点**：[2-3 个最重要的战略选择]
**盈亏平衡线方向性判断**：[基于当前价格，估计盈亏平衡点]
```

### 七、关键假设清单

```markdown
## 七、关键假设清单

以下假设对最终结果影响最大，建议优先验证：

| 假设项 | 当前取值 | 影响程度 | 建议验证方式 |
|--------|---------|---------|------------|
| [假设1] | [值] | 🔴高 | [具体验证方法] |
| [假设2] | [值] | 🟡中 | |
| [假设3] | [值] | 🟢低 | |
```

> 映射：`tool-demand-iceberg-l6-hypothesis`（RAT——最危险假设必须优先验证）+ `/demand-analysis-synthetic` Step 5 对抗检验

### 八、后续步骤建议

```markdown
## 八、后续步骤建议

1. **优先验证**：标注为 🔮 的核心假设，通过 [具体方法] 验证
2. **数据更新**：市场数据以 [年份] 为基准，建议 [频率] 更新
3. **报告应用场景**：
   - src_unknown
   - src_unknown
   - src_unknown
   - src_unknown
```

### 九、最重要提醒 🆕

```markdown
## 九、最重要提醒

> ⚠️ 这不是框架自动生成的——是 Agent 跑完所有分析后，跳出框架的元认知。

[在此回答：这份报告的结论基于什么关键前提？如果用户改变某个核心假设（如商业模式/目标客户/定价策略），哪些数字会彻底改变？框架的边界在哪里？]

示例：
- src_unknown
- src_unknown
```

## Agent 执行指令

```python
def generate_demand_report(analysis_result):
    """按模板生成需求分析报告"""
    sections = []
    
    # 1. 项目简介
    sections.append(fill_template("一、项目简介", project_brief))
    
    # 2. 市场规模总览
    sections.append(fill_tam_sam_cr1_table(analysis_result))
    
    # 3-5. TAM/SAM/CR1（调用 yt-market-size-estimation + five-step-barrier）
    sections.append(fill_tam(analysis_result.market_size))
    sections.append(fill_sam(analysis_result.market_size))
    sections.append(fill_cr1(analysis_result.barrier, analysis_result.spectrum))
    
    # 6. 经营策略（调用冰山 L6 RAT + 增长周期模型）
    sections.append(fill_strategy(analysis_result))
    
    # 7. 关键假设（调用 iceberg L6 RAT）
    sections.append(fill_assumptions(analysis_result.rat_list))
    
    # 8. 后续步骤
    sections.append(fill_next_steps(analysis_result))
    
    # 9. 最重要提醒——元认知：框架的边界在哪？
    sections.append(fill_meta_reminder(analysis_result))
    
    return "\n\n".join(sections)
```

## 与 `/demand-analysis-synthetic` 的关系

| 合成调研 | 报告模板 |
|:--|:--|
| 生成假设 + 对抗验证 | 把验证后的假设格式化为用户可读的报告 |
| Pipeline 的前 7 步 | Pipeline 的第 8 步——最终输出 |
| Agent 内部流程 | 面向用户的交付物 |

## 适用边界

- src_unknown
- src_unknown

---

*黄药师 · 2026-06-21 · 从 Coze 一堂Agent 报告提炼 + KDO 框架映射*

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 操作步骤

1. **步骤一**：待补充
2. **步骤二**：待补充
3. **步骤三**：待补充

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

> 待补充：这个工具的内在局限是什么？外部反对者会怎么批评？
