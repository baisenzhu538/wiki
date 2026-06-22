# 冉鹏 PPT 299 张 9 层深挖质量审计报告（CLI 王语嫣）

## 审计方法

9 层深挖维度：
1. 视觉层识别（OCR + VLM）
2. 框架类型判定（概念/框架/工具/模板/案例/练习/过渡页）
3. 与 PPT 讲义文字版交叉验证
4. 与已有 wiki 卡片对比
5. 外部知识交叉验证（待 WebSearch）
6. 操作可执行性评估
7. 失败模式与边界识别
8. 跨域桥接评估
9. 入库建议

## 统计摘要

- 总幻灯片：299
- Parse error：113
- 高潜独立成卡：180
- 中潜（可能并入已有卡）：44
- 低潜（跳过/过渡/练习）：75

### 框架域分布

- template_workshop: 159
- case_example: 108
- layout: 102
- capability: 92
- business_design: 55
- market_insight: 54
- strategy_intent: 44
- execution: 41

## 高潜独立成卡幻灯片（按幻灯片编号排序）

| 幻灯片 | 标题 | 类型 | 有效置信度 | 框架域 | 深度信号 | 入库建议 |
|:--|:--|:--|--:|:--|:--|:--|
| 00 | 战略破局营 | 幻灯片 | 0.95 | capability, template_workshop | has_template | 独立成卡 |
| 15 | 问题3：做生意，是可以写个战略然后照着执行的吗？ | 幻灯片 | 0.95 | business_design, market_insight, execution | has_steps, has_questions, has_examples | 独立成卡 |
| 16 | - **置信度**: 0.3 | 未识别 | 0.95 | capability, layout, template_workshop | has_template, has_cross_domain | 独立成卡 |
| 17 | 我对战略的定义： | 幻灯片 | 0.95 | capability, template_workshop | has_template | 独立成卡 |
| 20 | 企业战略金字塔：公司、业务与职能协同 | 框架图 | 0.95 | capability, layout, case_example | has_questions, has_examples | 独立成卡 |
| 21 | 案例：W&C战略金字塔对比 | 幻灯片 | 0.93 | capability, layout, case_example | has_template, has_examples | 独立成卡 |
| 22 | 战略的九个工作维度 | 框架图 | 0.95 | market_insight, layout, template_workshop | has_template, has_questions, has_failures | 独立成卡 |
| 23 | 战略工作的核心在于解决关键增长问题！ | 幻灯片 | 0.95 | capability, layout, template_workshop | has_template, has_questions, has_cross_domain | 独立成卡 |
| 24 | 战略怎么做？什么时候做？ | 幻灯片 | 0.95 | template_workshop | has_template, has_questions | 独立成卡 |
| 25 | - **置信度**: 0.3 | 未识别 | 0.95 | execution, capability | has_steps | 独立成卡 |
| 26 | 企业不同生命周期的战略怎么做？ | 信息图 | 0.96 | capability, layout, case_example | has_steps, has_template, has_examples | 独立成卡 |
| 30 | - **置信度**: 0.3 | 未识别 | 0.95 | capability, template_workshop | has_questions | 独立成卡 |
| 31 | 战略要练哪几个方面的基本功? | 幻灯片 | 0.95 | template_workshop | has_template, has_questions | 独立成卡 |
| 33 | - **置信度**: 0.3 | 未识别 | 0.95 | template_workshop | has_template | 独立成卡 |
| 34 | 以IBM "BLM业务领导力模型" 为例 | 框架图/幻灯片 | 0.95 | business_design, market_insight, strategy_intent | has_steps, has_template, has_questions | 独立成卡 |
| 35 | BLM的演化：华为五看三定 | 幻灯片 | 0.95 | business_design, market_insight, capability | has_steps, has_template | 独立成卡 |
| 39 | - **置信度**: 0.3 | 未识别 | 0.92 | strategy_intent, template_workshop | has_template | 独立成卡 |
| 40 | 业绩差距外部原因简析 | 幻灯片 | 0.92 | strategy_intent, template_workshop | has_template, has_questions | 独立成卡 |
| 41 | - **置信度**: 0.3 | 未识别 | 0.95 | strategy_intent, layout | has_steps | 独立成卡 |
| 42 | 鱼骨图详解1 - 销售 | 框架图 | 0.92 | strategy_intent, case_example | has_template, has_examples | 独立成卡 |
| 43 | - **置信度**: 0.3 | 未识别 | 0.92 | layout, case_example, template_workshop | has_steps, has_template, has_questions | 独立成卡 |
| 44 | 鱼骨图详解2 - EBIT | 教学示意图 | 0.93 | strategy_intent | has_template | 独立成卡 |
| 45 | - **置信度**: 0.3 | 未识别 | 0.95 | layout, template_workshop | has_template, has_questions | 独立成卡 |
| 46 | 鱼骨图详解3 - 库存 | 幻灯片 | 0.93 |  | has_template, has_questions | 独立成卡 |
| 48 | 根因分析4 – 管理问题 | 框架图 | 0.95 | layout, case_example | has_steps, has_questions, has_examples | 独立成卡 |
| 49 | - **置信度**: 0.3 | 未识别 | 0.95 | capability, case_example | has_steps, has_examples | 独立成卡 |
| 53 | - **置信度**: 0.3 | 未识别 | 0.92 | strategy_intent, case_example | has_template, has_examples, has_cross_domain | 独立成卡 |
| 56 | 价值链上的新生意机会 1 | 框架图 | 0.92 | market_insight, layout, case_example | has_steps, has_template, has_examples | 独立成卡 |
| 59 | 战略意图 | 幻灯片 | 0.92 | strategy_intent, case_example, template_workshop | has_steps, has_template, has_questions | 独立成卡 |
| 60 | - **置信度**: 0.3 | 未识别 | 0.92 | case_example | has_steps, has_examples, has_failures | 独立成卡 |
| 62 | - **置信度**: 0.3 | 未识别 | 0.95 | business_design, market_insight, capability | has_steps, has_failures, has_cross_domain | 独立成卡 |
| 64 | - **置信度**: 0.3 | 未识别 | 0.95 | market_insight, case_example, template_workshop | has_template, has_examples, has_cross_domain | 独立成卡 |
| 66 | 产业链机会和行动计划 | 框架图 | 0.95 | market_insight, execution, capability | has_steps, has_template, has_examples | 独立成卡 |
| 67 | - **置信度**: 0.3 | 未识别 | 0.92 | market_insight, capability, layout | has_steps, has_template, has_examples | 独立成卡 |
| 70 | 细分市场分析逻辑 | 幻灯片 | 0.95 | market_insight, capability, layout | has_steps, has_template, has_questions | 独立成卡 |
| 71 | - **置信度**: 0.3 | 未识别 | 0.96 | market_insight, template_workshop | has_template, has_cross_domain | 独立成卡 |
| 74 | 3.4 波特五力分析（1/5） | 幻灯片 | 0.95 | market_insight, case_example | has_template, has_examples, has_cross_domain | 独立成卡 |
| 78 | - **置信度**: 0.3 | 未识别 | 0.88 | market_insight, capability, template_workshop | has_template | 独立成卡 |
| 79 | 3.5 竞争格局分析-利润率 (2/3) | 幻灯片 | 0.88 | market_insight, capability, template_workshop | has_template | 独立成卡 |
| 80 | - **置信度**: 0.3 | 未识别 | 0.95 | market_insight, execution, case_example | has_steps, has_template, has_examples | 独立成卡 |
| 82 | 竞品B关键成功要素分析（2/4） | 幻灯片 | 0.92 | market_insight, case_example, template_workshop | has_template, has_examples | 独立成卡 |
| 84 | 我司与竞品关键成功因素-对比 (1/2) | 信息图 | 0.92 | market_insight, capability, case_example | has_template, has_examples | 独立成卡 |
| 85 | 关键成功因素-总结&策略（2/2） | 幻灯片 | 0.96 | market_insight, case_example, template_workshop | has_template, has_examples | 独立成卡 |
| 86 | - **置信度**: 0.3 | 未识别 | 0.95 | market_insight, strategy_intent, capability | has_template, has_cross_domain | 独立成卡 |
| 87 | 形成我们的SWOT分析 | 教学示意图 | 0.95 | market_insight, template_workshop | has_template | 独立成卡 |
| 91 | 通过安索夫矩阵探讨未来业务的发展方向 | 框架图 | 0.95 | layout, template_workshop | has_template, has_questions, has_cross_domain | 独立成卡 |
| 92 | 提供什么产品/服务(解决方案)? | 幻灯片 | 0.95 |  | has_steps, has_cross_domain | 独立成卡 |
| 93 | - **置信度**: 0.3 | 未识别 | 0.95 | case_example, template_workshop | has_template, has_examples | 独立成卡 |
| 94 | - **置信度**: 0.3 | 未识别 | 0.95 | template_workshop | has_template | 独立成卡 |
| 95 | 我们的渠道组合策略 | 幻灯片 | 0.92 | template_workshop | has_template | 独立成卡 |
| 96 | 创新焦点——总结 | 幻灯片 | 0.95 | business_design, strategy_intent, capability | has_template, has_questions | 独立成卡 |
| 97 | 业务设计 | 框架图 | 0.95 | business_design, market_insight, strategy_intent | has_template, has_cross_domain | 独立成卡 |
| 99 | 业务设计大定势：六要素*三步骤 | 教学示意图/幻灯片 | 0.95 | business_design, market_insight, strategy_intent | has_steps, has_template, has_questions | 独立成卡 |
| 101 | 为哪些目标用户服务？她们有何需求/痛点？ | 幻灯片 | 0.95 | capability | has_steps, has_questions, has_cross_domain | 独立成卡 |
| 102 | - **置信度**: 0.3 | 未识别 | 0.95 | capability, template_workshop | has_template | 独立成卡 |
| 103 | 示例：目标客群定位与描述 | 幻灯片 | 0.93 | capability, case_example, template_workshop | has_template, has_examples, has_cross_domain | 独立成卡 |
| 104 | - **置信度**: 0.3 | 未识别 | 0.92 | business_design, layout, case_example | has_template, has_examples, has_cross_domain | 独立成卡 |
| 105 | 示例：差异化的客群经营策略 | 幻灯片 | 0.92 | layout, case_example, template_workshop | has_template, has_examples, has_cross_domain | 独立成卡 |
| 107 | 二、价值主张 | 幻灯片 | 0.95 | business_design, template_workshop | has_template, has_questions, has_cross_domain | 独立成卡 |
| 108 | 顾客有何需求？需求有何变化？ | 框架图 | 0.92 | capability, template_workshop | has_cross_domain | 独立成卡 |
| 110 | 对价值主张排序，并用一段话进行描述 | 幻灯片 | 0.92 | business_design, case_example, template_workshop | has_template, has_examples, has_cross_domain | 独立成卡 |
| 111 | - **置信度**: 0.3 | 未识别 | 0.95 | capability, case_example, template_workshop | has_template, has_examples, has_cross_domain | 独立成卡 |
| 112 | 对比竞品，设定未来的价值主张与定位 | 框架图 | 0.95 | business_design, market_insight, case_example | has_template, has_examples, has_cross_domain | 独立成卡 |
| 113 | 得出我们的差异化核心价值主张 | 框架图 | 0.93 | business_design, case_example | has_template, has_examples, has_cross_domain | 独立成卡 |
| 114 | - **置信度**: 0.3 | 未识别 | 0.95 | business_design, template_workshop | has_template | 独立成卡 |
| 115 | 价值获取：如何实现我们的价值主张？ | 幻灯片 | 0.95 | business_design, template_workshop | has_template, has_questions, has_cross_domain | 独立成卡 |
| 116 | - **置信度**: 0.3 | 未识别 | 0.95 | capability, template_workshop | has_steps, has_template | 独立成卡 |
| 117 | 盈利模式示例 - M采用代理加盟的连锁加盟模式（1/4） | 信息图 | 0.95 | business_design, capability, case_example | has_template, has_examples, has_cross_domain | 独立成卡 |
| 118 | 如何实现持续的价值增值(经营壁垒)？ | 幻灯片 | 0.96 | execution, layout, case_example | has_template, has_examples, has_failures | 独立成卡 |
| 119 | 业务设计4：活动范围 | 幻灯片 | 0.93 | business_design, template_workshop | has_template | 独立成卡 |
| 121 | 活动范围 | 框架图 | 0.92 | business_design, execution, case_example | has_template, has_examples, has_cross_domain | 独立成卡 |
| 123 | - **置信度**: 0.3 | 未识别 | 0.95 | business_design, capability, template_workshop | has_template, has_questions, has_cross_domain | 独立成卡 |
| 124 | 价值定位模型 | 幻灯片 | 0.95 | business_design, layout, template_workshop | has_template, has_cross_domain | 独立成卡 |
| 125 | - **置信度**: 0.3 | 未识别 | 0.92 | business_design, case_example, template_workshop | has_template, has_questions, has_examples | 独立成卡 |
| 127 | 业务设计的风险识别与评估 | 幻灯片 | 0.92 | business_design, layout, template_workshop | has_steps, has_template | 独立成卡 |
| 129 | - **置信度**: 0.3 | 未识别 | 0.95 | business_design, template_workshop | has_steps, has_template | 独立成卡 |
| 130 | 业务设计7 总结 | 幻灯片 | 0.95 | business_design, template_workshop | has_template | 独立成卡 |
| 131 | 业务设计结果示例 | 框架图 | 0.95 | business_design, execution, case_example | has_steps, has_template, has_examples | 独立成卡 |
| 132 | 为公司各业态/业务单元制订不同的业务设计概要 | 框架图 | 0.95 | business_design, capability, template_workshop | has_steps, has_template, has_cross_domain | 独立成卡 |
| 133 | 关键任务 | 框架图 | 0.95 | business_design, market_insight, strategy_intent | has_steps, has_questions | 独立成卡 |
| 135 | 公司业务策略汇总 | 幻灯片 | 0.93 | template_workshop | has_steps, has_template | 独立成卡 |
| 136 | - **置信度**: 0.3 | 未识别 | 0.93 | business_design, strategy_intent, layout | has_template | 独立成卡 |
| 137 | - **置信度**: 0.3 | 未识别 | 0.95 | template_workshop | has_template | 独立成卡 |
| 138 | 公司级关键举措推进表 | 信息图 | 0.95 | template_workshop | has_template | 独立成卡 |
| 139 | - **置信度**: 0.3 | 未识别 | 0.95 | template_workshop | has_steps, has_template | 独立成卡 |
| 140 | 财务预测 | 幻灯片 | 0.92 | layout | has_template | 独立成卡 |
| 141 | 最终交付：战略蓝图（三年） | 框架图 | 0.93 | capability, case_example, template_workshop | has_steps, has_template, has_examples | 独立成卡 |
| 142 | 公司/各BU/业务单元/业态 的战略地图 | 框架图 | 0.95 | business_design, market_insight, strategy_intent | has_template | 独立成卡 |
| 144 | 支撑战略目标所需打造的全部核心能力 | 框架图 | 0.92 | execution, capability, layout | has_template, has_examples, has_cross_domain | 独立成卡 |
| 145 | 核心能力评估矩阵 | 框架图 | 0.95 | capability, layout, template_workshop | has_steps, has_template, has_cross_domain | 独立成卡 |
| 148 | 逐个检查与内外部合作伙伴的依赖关系 | 幻灯片 | 0.95 | template_workshop | has_template, has_questions, has_cross_domain | 独立成卡 |
| 151 | - **置信度**: 0.3 | 未识别 | 0.92 | layout, template_workshop | has_template | 独立成卡 |
| 152 | 财务资源分配 | 幻灯片 | 0.95 | layout, template_workshop | has_template, has_cross_domain | 独立成卡 |
| 153 | IT资源排布 | 幻灯片 | 0.95 | layout | has_steps, has_template | 独立成卡 |
| 155 | 公关资源：借助政策和政府公信力 | 幻灯片 | 0.95 | layout, template_workshop | has_template | 独立成卡 |
| 157 | - **置信度**: 0.3 | 未识别 | 0.95 | market_insight, capability, template_workshop | has_steps, has_template | 独立成卡 |
| 158 | - **置信度**: 0.3 | 未识别 | 0.93 | business_design, layout, template_workshop | has_template | 独立成卡 |
| 160 | - **置信度**: 0.3 | 未识别 | 0.95 | capability, case_example, template_workshop | has_steps, has_template, has_examples | 独立成卡 |
| 161 | - **置信度**: 0.3 | 未识别 | 0.95 | capability, template_workshop | has_template | 独立成卡 |
| 162 | - **置信度**: 0.3 | 未识别 | 0.92 | capability, layout, case_example | has_steps, has_template, has_examples | 独立成卡 |
| 163 | 关键任务卡片（将次年工作任务逐一细化） | 框架图 | 0.95 | execution, layout, case_example | has_steps, has_template, has_examples | 独立成卡 |
| 165 | - **置信度**: 0.3 | 未识别 | 0.95 | layout, case_example | has_steps, has_examples, has_cross_domain | 独立成卡 |
| 166 | - **置信度**: 0.3 | 未识别 | 0.92 | template_workshop | has_steps, has_template | 独立成卡 |
| 167 | - **置信度**: 0.3 | 未识别 | 0.95 |  | has_template | 独立成卡 |
| 168 | 最终交付：2、财务目标（渠道维度） | 幻灯片 | 0.92 | template_workshop | has_template | 独立成卡 |
| 169 | 最终交付：2、财务目标（区域维度） | 幻灯片 | 0.95 | template_workshop | has_template | 独立成卡 |
| 170 | - **置信度**: 0.3 | 未识别 | 0.95 | execution, capability, case_example | has_template, has_examples | 独立成卡 |
| 171 | - **置信度**: 0.3 | 未识别 | 0.92 | execution, layout, case_example | has_template, has_questions, has_examples | 独立成卡 |
| 172 | - **置信度**: 0.3 | 未识别 | 0.92 | capability, case_example | has_template, has_examples, has_cross_domain | 独立成卡 |
| 173 | 风险应对 | 幻灯片 | 0.92 | business_design, template_workshop | has_template | 独立成卡 |
| 175 | 三年计划财务结果 | 幻灯片 | 0.95 |  | has_template | 独立成卡 |
| 176 | - **置信度**: 0.3 | 未识别 | 0.95 | template_workshop | has_template | 独立成卡 |
| 178 | 三年挑战收入目标 | 幻灯片 | 0.95 | template_workshop | has_template | 独立成卡 |
| 179 | - **置信度**: 0.3 | 未识别 | 0.85 |  | has_template | 独立成卡 |
| 182 | 行销费用明细 | 幻灯片 | 0.92 | template_workshop | has_template | 独立成卡 |
| 183 | - **置信度**: 0.3 | 未识别 | 0.92 | template_workshop | has_template | 独立成卡 |
| 184 | - **置信度**: 0.3 | 未识别 | 0.92 | template_workshop | has_template | 独立成卡 |
| 185 | 各部门行政费用 | 框架图 | 0.95 | template_workshop | has_template | 独立成卡 |
| 186 | 组织架构调整及人工效能提升 | 幻灯片 | 0.92 | layout, template_workshop | has_template | 独立成卡 |
| 187 | 资本支出三年计划 | 幻灯片 | 0.95 | template_workshop | has_template | 独立成卡 |
| 188 | - **置信度**: 0.3 | 未识别 | 0.96 | template_workshop | has_template | 独立成卡 |
| 189 | - **置信度**: 0.3 | 未识别 | 0.95 | template_workshop | has_template | 独立成卡 |
| 191 | - **置信度**: 0.3 | 未识别 | 0.88 |  | has_template | 独立成卡 |
| 192 | - **置信度**: 0.3 | 未识别 | 0.92 | template_workshop | has_template | 独立成卡 |
| 195 | - **置信度**: 0.3 | 未识别 | 0.95 | market_insight, template_workshop | has_template, has_cross_domain | 独立成卡 |
| 198 | - **置信度**: 0.3 | 未识别 | 0.95 | case_example, template_workshop | has_steps, has_template, has_questions | 独立成卡 |
| 200 | 答案找不到，更上一层楼（注意：每次只上一层楼） | 框架图 | 0.95 | strategy_intent, template_workshop | has_questions, has_cross_domain | 独立成卡 |
| 201 | 另一种工作顺序（从上往下的假设验证） | 幻灯片 | 0.95 | layout, template_workshop | has_steps, has_template, has_questions | 独立成卡 |
| 205 | 2、角度引擎——配置你的"认知透镜组合" | 幻灯片 | 0.95 |  | has_steps, has_questions, has_cross_domain | 独立成卡 |
| 206 | - **置信度**: 0.3 | 未识别 | 0.95 | template_workshop | has_template, has_questions, has_failures | 独立成卡 |
| 217 | - **置信度**: 0.3 | 未识别 | 0.95 | template_workshop | has_template | 独立成卡 |
| 220 | - **置信度**: 0.3 | 未识别 | 0.92 | layout | has_steps, has_questions | 独立成卡 |
| 222 | - **置信度**: 0.3 | 未识别 | 0.92 | capability, layout, case_example | has_steps, has_template, has_questions | 独立成卡 |
| 223 | 第1阶段：现状→问题（模型与图表环节） | 幻灯片 | 0.95 | capability, case_example | has_steps, has_questions, has_examples | 独立成卡 |
| 224 | 第2阶段：问题→根因（假设循环环节） | 教学示意图 | 0.95 | template_workshop | has_steps, has_template, has_questions | 独立成卡 |
| 225 | 第3阶段：根因→改进方向（角度引擎环节） | 幻灯片 | 0.93 | case_example, template_workshop | has_steps, has_template, has_questions | 独立成卡 |
| 226 | - **置信度**: 0.3 | 未识别 | 0.95 | layout, template_workshop | has_steps, has_template, has_questions | 独立成卡 |
| 227 | 洞察力到底在修炼什么？ | 框架图 | 0.93 | market_insight, capability, template_workshop | has_steps, has_template, has_questions | 独立成卡 |
| 228 | - **置信度**: 0.3 | 未识别 | 0.95 | capability, layout, template_workshop | has_steps, has_template, has_questions | 独立成卡 |
| 230 | 2.3 战略基本功-战略布局 | 幻灯片 | 0.92 | template_workshop | has_template | 独立成卡 |
| 231 | 战略布局 | 幻灯片 | 0.95 | capability, layout, case_example | has_steps, has_examples | 独立成卡 |
| 232 | 当前企业战略布局的挑战与痛点 | 幻灯片 | 0.95 | market_insight, capability, layout | has_template, has_failures | 独立成卡 |
| 233 | 1、增长型战略布局 | 幻灯片 | 0.95 | layout, template_workshop | has_template | 独立成卡 |
| 235 | 碗里和锅里的生意：战不战？退不退？留不留？ | 幻灯片 | 0.95 | layout, template_workshop | has_steps, has_template, has_questions | 独立成卡 |
| 236 | 田里的生意：大不大？小不小？赌不赌？ | 框架图 | 0.95 | layout | has_template, has_cross_domain | 独立成卡 |
| 241 | - **置信度**: 0.3 | 未识别 | 0.96 | layout, case_example, template_workshop | has_template, has_examples, has_cross_domain | 独立成卡 |
| 245 | 不同业务类型，不同的关注重点 | 幻灯片 | 0.95 | business_design, layout, case_example | has_template, has_examples, has_cross_domain | 独立成卡 |
| 246 | 三个地平线：短中长期各项业务如何管理？ | 教学示意图/框架图 | 0.95 | strategy_intent, capability, layout | has_template | 独立成卡 |
| 248 | 1、全业务BCG矩阵分析 | 幻灯片 | 0.96 | layout, case_example, template_workshop | has_template, has_questions, has_examples | 独立成卡 |
| 249 | - **置信度**: 0.3 | 未识别 | 0.95 | template_workshop | has_template, has_cross_domain | 独立成卡 |
| 250 | 3、填写三个地平线图（时间3~5年） | 框架图 | 0.96 | strategy_intent, layout, template_workshop | has_steps, has_template, has_questions | 独立成卡 |
| 251 | 初步描绘三个地平线的目标与策略 | 幻灯片 | 0.96 | strategy_intent, template_workshop | has_template, has_questions | 独立成卡 |
| 252 | 撤退型战略布局 | 幻灯片 | 0.95 | layout | has_steps, has_cross_domain | 独立成卡 |
| 253 | - **置信度**: 0.3 | 未识别 | 0.95 | capability, layout, case_example | has_steps, has_questions, has_examples | 独立成卡 |
| 254 | 撤退型布局2 去除 | 幻灯片 | 0.95 | layout, case_example | has_steps, has_examples | 独立成卡 |
| 255 | - **置信度**: 0.3 | 未识别 | 0.95 | layout, case_example | has_steps, has_examples, has_cross_domain | 独立成卡 |
| 257 | 战略布局中的转型路径 | 幻灯片 | 0.95 | capability, layout, case_example | has_template, has_examples | 独立成卡 |
| 259 | 突破型布局1 重新想象 | 幻灯片 | 0.95 | market_insight, layout, case_example | has_template, has_questions, has_examples | 独立成卡 |
| 263 | 重要工具：平台商业模式地图 | 框架图 | 0.95 | business_design, layout, case_example | has_template, has_examples, has_cross_domain | 独立成卡 |
| 264 | - **置信度**: 0.3 | 未识别 | 0.95 | layout, case_example, template_workshop | has_template, has_examples, has_failures | 独立成卡 |
| 265 | 突破型布局3 后手布局2 | 幻灯片 | 0.95 | execution, capability, layout | has_steps, has_examples, has_cross_domain | 独立成卡 |
| 269 | 2.4 战略基本功-价值创造体系 | 幻灯片 | 0.92 | template_workshop | has_template | 独立成卡 |
| 271 | - **置信度**: 0.3 | 未识别 | 0.95 | layout, template_workshop | has_template, has_questions | 独立成卡 |
| 272 | 价值创造体系示例：某定位公司"万箭穿心"模型 | 框架图 | 0.95 | layout, case_example | has_steps, has_examples, has_cross_domain | 独立成卡 |
| 273 | 如何构建价值创造体系：三层架构+五大原则 | 幻灯片/框架图 | 0.93 | business_design, strategy_intent, execution | has_steps, has_failures | 独立成卡 |
| 275 | 诊断并优化你的价值创造体系 | 幻灯片 | 0.95 | business_design, execution, layout | has_steps, has_template, has_examples | 独立成卡 |
| 276 | - **置信度**: 0.3 | 未识别 | 0.95 | layout, template_workshop | has_template | 独立成卡 |
| 282 | - **置信度**: 0.3 | 未识别 | 0.95 | layout | has_template, has_cross_domain | 独立成卡 |
| 283 | 变革管理的基本功：维持四大平衡 | 框架图 | 0.95 | execution, template_workshop | has_template | 独立成卡 |
| 284 | 适配变革的组织结构：三大平衡特征 | 幻灯片 | 0.92 | execution, layout | has_steps | 独立成卡 |
| 285 | - **置信度**: 0.3 | 未识别 | 0.97 | template_workshop | has_steps, has_template, has_cross_domain | 独立成卡 |
| 286 | 小组任务 | 幻灯片 | 0.92 | template_workshop | has_template | 独立成卡 |
| 288 | 每组推出一个案例，为最终对决制订战略： | 幻灯片 | 0.95 | strategy_intent, layout, case_example | has_steps, has_template, has_questions | 独立成卡 |
| 289 | - **置信度**: 0.3 | 未识别 | 0.95 |  | has_steps, has_questions | 独立成卡 |
| 292 | 机会差距分析： | 幻灯片 | 0.88 | strategy_intent, template_workshop | has_template, has_cross_domain | 独立成卡 |
| 293 | - **置信度**: 0.3 | 未识别 | 0.93 | business_design, template_workshop | has_template, has_questions | 独立成卡 |
| 294 | 业务设计大定势：六要素*三步骤 | 框架图 | 0.95 | business_design, template_workshop | has_steps, has_template, has_questions | 独立成卡 |
| 295 | 战略主题-战略举措-行动任务（三年） | 框架图 | 0.95 | capability, template_workshop | has_template | 独立成卡 |
| 296 | 财务预测 | 信息图 | 0.92 | layout, template_workshop | has_template, has_cross_domain | 独立成卡 |
| 297 | "九层宝塔" 模型简介 | 框架图 | 0.95 | template_workshop | has_questions, has_cross_domain | 独立成卡 |

## 中潜幻灯片（可能并入已有卡或待进一步确认）

| 幻灯片 | 标题 | 类型 | 有效置信度 | 框架域 | 深度信号 | 入库建议 |
|:--|:--|:--|--:|:--|:--|:--|
| 06 | 不重视战略的后果： | 幻灯片 | 0.95 | business_design, layout | has_failures | 待定 |
| 08 | - **置信度**: 0.3 | 未识别 | 0.95 | execution, capability, layout | has_questions, has_examples, has_failures | 待定 |
| 28 | 一、统帅的战略角色不可替代 | 幻灯片 | 0.95 | capability, layout | has_questions, has_cross_domain | 待定 |
| 29 | - **置信度**: 0.3 | 未识别 | 0.96 | capability, layout |  | 待定 |
| 32 | 战略基本功 5C模型 | 幻灯片 | 0.95 | business_design, strategy_intent, execution | has_cross_domain | 待定 |
| 36 | 业绩差距与机会差距 | 框架图 | 0.95 | business_design, market_insight, strategy_intent |  | 待定 |
| 52 | 新品类机会差距 1 | 幻灯片 | 0.95 | strategy_intent, capability, case_example | has_examples, has_cross_domain | 待定 |
| 54 | - **置信度**: 0.3 | 未识别 | 0.88 | strategy_intent |  | 待定 |
| 55 | 新用户需求机会差距 1 | 幻灯片 | 0.88 | strategy_intent | has_cross_domain | 待定 |
| 58 | - **置信度**: 0.3 | 未识别 | 0.92 | business_design, market_insight, strategy_intent |  | 待定 |
| 61 | - **置信度**: 0.3 | 未识别 | 0.92 | business_design, market_insight, strategy_intent | has_cross_domain | 待定 |
| 69 | 3.3 细分市场分析-市场总量 | 幻灯片 | 0.95 | case_example | has_examples | 待定 |
| 73 | 3.4 波特五力分析 | 教学示意图 | 0.95 | market_insight |  | 待定 |
| 77 | 3.5 竞争对手定义 | 幻灯片 | 0.95 | market_insight | has_cross_domain | 待定 |
| 83 | - **置信度**: 0.3 | 未识别 | 0.95 | market_insight, case_example | has_examples | 待定 |
| 88 | 创新焦点 | 框架图 | 0.95 | business_design, market_insight, strategy_intent | has_questions, has_cross_domain | 待定 |
| 98 | - **置信度**: 0.3 | 未识别 | 0.92 | business_design, market_insight, strategy_intent | has_questions | 待定 |
| 100 | 业务设计1：客户选择 | 幻灯片 | 0.95 | business_design |  | 待定 |
| 106 | 业务设计2 - 价值主张 | 幻灯片 | 0.95 | business_design |  | 待定 |
| 120 | 活动范围 | 幻灯片 | 0.95 | business_design, market_insight | has_questions, has_cross_domain | 待定 |
| 122 | 业务设计5 战略控制点 | 幻灯片 | 0.95 | business_design |  | 待定 |
| 126 | 业务设计6 风险管理 | 幻灯片 | 0.95 | business_design |  | 待定 |
| 150 | 资源与支撑体系 | 信息图 | 0.93 | market_insight, execution, capability |  | 待定 |
| 154 | - **置信度**: 0.3 | 未识别 | 0.92 | market_insight, layout |  | 待定 |
| 193 | - **置信度**: 0.3 | 未识别 | 0.95 | capability | has_questions | 待定 |
| 194 | 战略洞察双引擎：从看到到看透 | 幻灯片 | 0.92 | capability, layout |  | 待定 |
| 197 | 案例背景 | 幻灯片 | 0.95 | capability, case_example | has_questions, has_examples | 待定 |
| 199 | - **置信度**: 0.3 | 未识别 | 0.95 | business_design, strategy_intent |  | 待定 |
| 204 | 模型选择的心智模式 | 幻灯片 | 0.95 | capability | has_questions, has_cross_domain | 待定 |
| 207 | - **置信度**: 0.3 | 未识别 | 0.95 | market_insight, capability, case_example | has_examples | 待定 |
| 213 | - **置信度**: 0.3 | 未识别 | 0.93 | capability, case_example | has_examples, has_cross_domain | 待定 |
| 238 | 小李飞刀：打"进化"时间差 | 幻灯片 | 0.92 | case_example | has_examples, has_cross_domain | 待定 |
| 239 | 2. 分筋错骨手：与市场常识反向而行 | 幻灯片 | 0.92 | market_insight, case_example | has_examples | 待定 |
| 240 | 葵花点穴手：聚焦细分客群 | 幻灯片 | 0.93 | market_insight, layout, case_example | has_examples | 待定 |
| 242 | 降龙十八掌：寻找价值链上其它环节的市场机会 | 幻灯片 | 0.95 | business_design, case_example | has_examples | 待定 |
| 243 | - **置信度**: 0.3 | 未识别 | 0.95 | business_design, execution, layout | has_examples, has_cross_domain | 待定 |
| 244 | 田里的生意：拆用户→拆场景→挖内核 | 幻灯片 | 0.95 | business_design, market_insight, execution | has_failures, has_cross_domain | 待定 |
| 258 | - **置信度**: 0.3 | 未识别 | 0.95 | execution, capability, layout |  | 待定 |
| 260 | - **置信度**: 0.3 | 未识别 | 0.95 | capability, layout, case_example | has_examples, has_cross_domain | 待定 |
| 261 | 突破型布局2 击破边界2 | 幻灯片 | 0.92 | capability, layout, case_example | has_examples, has_cross_domain | 待定 |
| 266 | - **置信度**: 0.3 | 未识别 | 0.95 | layout, case_example | has_examples, has_cross_domain | 待定 |
| 277 | 2.5 战略基本功-变革管理 | 幻灯片 | 0.95 | execution, capability, layout |  | 待定 |
| 279 | 内外部环境高速变化，绝不会依你意愿来行事 | 信息图 | 0.88 | execution, capability | has_cross_domain | 待定 |
| 290 | - **置信度**: 0.3 | 未识别 | 0.93 | layout, case_example | has_questions, has_examples | 待定 |

## Parse error 但内层高质量的可修复幻灯片

| 幻灯片 | 标题 | 外层置信度 | 内层置信度 | 框架域 | 备注 |
|:--|:--|--:|--:|:--|:--|
| 01 | - **置信度**: 0.3 | 0.30 | 0.95 | case_example, template_workshop | P-33 修复后可读 |
| 02 | - **置信度**: 0.3 | 0.30 | 0.95 | business_design | P-33 修复后可读 |
| 08 | - **置信度**: 0.3 | 0.30 | 0.95 | execution, capability, layout | P-33 修复后可读 |
| 14 | - **置信度**: 0.3 | 0.30 | 0.95 | case_example | P-33 修复后可读 |
| 16 | - **置信度**: 0.3 | 0.30 | 0.95 | capability, layout, template_workshop | P-33 修复后可读 |
| 25 | - **置信度**: 0.3 | 0.30 | 0.95 | execution, capability | P-33 修复后可读 |
| 29 | - **置信度**: 0.3 | 0.30 | 0.96 | capability, layout | P-33 修复后可读 |
| 30 | - **置信度**: 0.3 | 0.30 | 0.95 | capability, template_workshop | P-33 修复后可读 |
| 33 | - **置信度**: 0.3 | 0.30 | 0.95 | template_workshop | P-33 修复后可读 |
| 39 | - **置信度**: 0.3 | 0.30 | 0.92 | strategy_intent, template_workshop | P-33 修复后可读 |
| 41 | - **置信度**: 0.3 | 0.30 | 0.95 | strategy_intent, layout | P-33 修复后可读 |
| 43 | - **置信度**: 0.3 | 0.30 | 0.92 | layout, case_example, template_workshop | P-33 修复后可读 |
| 45 | - **置信度**: 0.3 | 0.30 | 0.95 | layout, template_workshop | P-33 修复后可读 |
| 49 | - **置信度**: 0.3 | 0.30 | 0.95 | capability, case_example | P-33 修复后可读 |
| 50 | - **置信度**: 0.3 | 0.30 | 0.92 | strategy_intent, case_example, template_workshop | P-33 修复后可读 |
| 51 | - **置信度**: 0.3 | 0.30 | 0.95 | strategy_intent, template_workshop | P-33 修复后可读 |
| 53 | - **置信度**: 0.3 | 0.30 | 0.92 | strategy_intent, case_example | P-33 修复后可读 |
| 54 | - **置信度**: 0.3 | 0.30 | 0.88 | strategy_intent | P-33 修复后可读 |
| 57 | - **置信度**: 0.3 | 0.30 | 0.92 | strategy_intent, layout, case_example | P-33 修复后可读 |
| 58 | - **置信度**: 0.3 | 0.30 | 0.92 | business_design, market_insight, strategy_intent | P-33 修复后可读 |
| 60 | - **置信度**: 0.3 | 0.30 | 0.92 | case_example | P-33 修复后可读 |
| 61 | - **置信度**: 0.3 | 0.30 | 0.92 | business_design, market_insight, strategy_intent | P-33 修复后可读 |
| 62 | - **置信度**: 0.3 | 0.30 | 0.95 | business_design, market_insight, capability | P-33 修复后可读 |
| 63 | - **置信度**: 0.3 | 0.30 | 0.95 | market_insight, strategy_intent, capability | P-33 修复后可读 |
| 64 | - **置信度**: 0.3 | 0.30 | 0.95 | market_insight, case_example, template_workshop | P-33 修复后可读 |
| 67 | - **置信度**: 0.3 | 0.30 | 0.92 | market_insight, capability, layout | P-33 修复后可读 |
| 68 | - **置信度**: 0.3 | 0.30 | 0.95 | market_insight, strategy_intent, capability | P-33 修复后可读 |
| 71 | - **置信度**: 0.3 | 0.30 | 0.96 | market_insight, template_workshop | P-33 修复后可读 |
| 75 | - **置信度**: 0.3 | 0.30 | 0.95 | market_insight, strategy_intent, capability | P-33 修复后可读 |
| 78 | - **置信度**: 0.3 | 0.30 | 0.88 | market_insight, capability, template_workshop | P-33 修复后可读 |
| 80 | - **置信度**: 0.3 | 0.30 | 0.95 | market_insight, execution, case_example | P-33 修复后可读 |
| 83 | - **置信度**: 0.3 | 0.30 | 0.95 | market_insight, case_example | P-33 修复后可读 |
| 86 | - **置信度**: 0.3 | 0.30 | 0.95 | market_insight, strategy_intent, capability | P-33 修复后可读 |
| 93 | - **置信度**: 0.3 | 0.30 | 0.95 | case_example, template_workshop | P-33 修复后可读 |
| 94 | - **置信度**: 0.3 | 0.30 | 0.95 | template_workshop | P-33 修复后可读 |
| 98 | - **置信度**: 0.3 | 0.30 | 0.92 | business_design, market_insight, strategy_intent | P-33 修复后可读 |
| 102 | - **置信度**: 0.3 | 0.30 | 0.95 | capability, template_workshop | P-33 修复后可读 |
| 104 | - **置信度**: 0.3 | 0.30 | 0.92 | business_design, layout, case_example | P-33 修复后可读 |
| 111 | - **置信度**: 0.3 | 0.30 | 0.95 | capability, case_example, template_workshop | P-33 修复后可读 |
| 114 | - **置信度**: 0.3 | 0.30 | 0.95 | business_design, template_workshop | P-33 修复后可读 |
| 116 | - **置信度**: 0.3 | 0.30 | 0.95 | capability, template_workshop | P-33 修复后可读 |
| 123 | - **置信度**: 0.3 | 0.30 | 0.95 | business_design, capability, template_workshop | P-33 修复后可读 |
| 125 | - **置信度**: 0.3 | 0.30 | 0.92 | business_design, case_example, template_workshop | P-33 修复后可读 |
| 129 | - **置信度**: 0.3 | 0.30 | 0.95 | business_design, template_workshop | P-33 修复后可读 |
| 134 | - **置信度**: 0.3 | 0.30 | 0.92 | execution, layout, template_workshop | P-33 修复后可读 |
| 136 | - **置信度**: 0.3 | 0.30 | 0.93 | business_design, strategy_intent, layout | P-33 修复后可读 |
| 137 | - **置信度**: 0.3 | 0.30 | 0.95 | template_workshop | P-33 修复后可读 |
| 139 | - **置信度**: 0.3 | 0.30 | 0.95 | template_workshop | P-33 修复后可读 |
| 147 | - **置信度**: 0.3 | 0.30 | 0.88 | execution | P-33 修复后可读 |
| 149 | - **置信度**: 0.3 | 0.30 | 0.92 | execution, layout, case_example | P-33 修复后可读 |
| 151 | - **置信度**: 0.3 | 0.30 | 0.92 | layout, template_workshop | P-33 修复后可读 |
| 154 | - **置信度**: 0.3 | 0.30 | 0.92 | market_insight, layout | P-33 修复后可读 |
| 157 | - **置信度**: 0.3 | 0.30 | 0.95 | market_insight, capability, template_workshop | P-33 修复后可读 |
| 158 | - **置信度**: 0.3 | 0.30 | 0.93 | business_design, layout, template_workshop | P-33 修复后可读 |
| 160 | - **置信度**: 0.3 | 0.30 | 0.95 | capability, case_example, template_workshop | P-33 修复后可读 |
| 161 | - **置信度**: 0.3 | 0.30 | 0.95 | capability, template_workshop | P-33 修复后可读 |
| 162 | - **置信度**: 0.3 | 0.30 | 0.92 | capability, layout, case_example | P-33 修复后可读 |
| 165 | - **置信度**: 0.3 | 0.30 | 0.95 | layout, case_example | P-33 修复后可读 |
| 166 | - **置信度**: 0.3 | 0.30 | 0.92 | template_workshop | P-33 修复后可读 |
| 167 | - **置信度**: 0.3 | 0.30 | 0.95 |  | P-33 修复后可读 |
| 170 | - **置信度**: 0.3 | 0.30 | 0.95 | execution, capability, case_example | P-33 修复后可读 |
| 171 | - **置信度**: 0.3 | 0.30 | 0.92 | execution, layout, case_example | P-33 修复后可读 |
| 172 | - **置信度**: 0.3 | 0.30 | 0.92 | capability, case_example | P-33 修复后可读 |
| 176 | - **置信度**: 0.3 | 0.30 | 0.95 | template_workshop | P-33 修复后可读 |
| 179 | - **置信度**: 0.3 | 0.30 | 0.85 |  | P-33 修复后可读 |
| 183 | - **置信度**: 0.3 | 0.30 | 0.92 | template_workshop | P-33 修复后可读 |
| 184 | - **置信度**: 0.3 | 0.30 | 0.92 | template_workshop | P-33 修复后可读 |
| 188 | - **置信度**: 0.3 | 0.30 | 0.96 | template_workshop | P-33 修复后可读 |
| 189 | - **置信度**: 0.3 | 0.30 | 0.95 | template_workshop | P-33 修复后可读 |
| 190 | - **置信度**: 0.3 | 0.30 | 0.93 |  | P-33 修复后可读 |
| 191 | - **置信度**: 0.3 | 0.30 | 0.88 |  | P-33 修复后可读 |
| 192 | - **置信度**: 0.3 | 0.30 | 0.92 | template_workshop | P-33 修复后可读 |
| 193 | - **置信度**: 0.3 | 0.30 | 0.95 | capability | P-33 修复后可读 |
| 195 | - **置信度**: 0.3 | 0.30 | 0.95 | market_insight, template_workshop | P-33 修复后可读 |
| 198 | - **置信度**: 0.3 | 0.30 | 0.95 | case_example, template_workshop | P-33 修复后可读 |
| 199 | - **置信度**: 0.3 | 0.30 | 0.95 | business_design, strategy_intent | P-33 修复后可读 |
| 203 | - **置信度**: 0.3 | 0.30 | 0.95 | market_insight, execution, layout | P-33 修复后可读 |
| 206 | - **置信度**: 0.3 | 0.30 | 0.95 | template_workshop | P-33 修复后可读 |
| 207 | - **置信度**: 0.3 | 0.30 | 0.95 | market_insight, capability, case_example | P-33 修复后可读 |
| 208 | - **置信度**: 0.3 | 0.30 | 0.95 |  | P-33 修复后可读 |
| 210 | - **置信度**: 0.3 | 0.30 | 0.95 | layout | P-33 修复后可读 |
| 213 | - **置信度**: 0.3 | 0.30 | 0.93 | capability, case_example | P-33 修复后可读 |
| 214 | - **置信度**: 0.3 | 0.30 | 0.92 | case_example, template_workshop | P-33 修复后可读 |
| 216 | - **置信度**: 0.3 | 0.30 | 0.95 | case_example, template_workshop | P-33 修复后可读 |
| 217 | - **置信度**: 0.3 | 0.30 | 0.95 | template_workshop | P-33 修复后可读 |
| 218 | - **置信度**: 0.3 | 0.30 | 0.95 | market_insight, capability, layout | P-33 修复后可读 |
| 219 | - **置信度**: 0.3 | 0.30 | 0.95 |  | P-33 修复后可读 |
| 220 | - **置信度**: 0.3 | 0.30 | 0.92 | layout | P-33 修复后可读 |
| 221 | - **置信度**: 0.3 | 0.30 | 0.95 | case_example | P-33 修复后可读 |
| 222 | - **置信度**: 0.3 | 0.30 | 0.92 | capability, layout, case_example | P-33 修复后可读 |
| 226 | - **置信度**: 0.3 | 0.30 | 0.95 | layout, template_workshop | P-33 修复后可读 |
| 228 | - **置信度**: 0.3 | 0.30 | 0.95 | capability, layout, template_workshop | P-33 修复后可读 |
| 241 | - **置信度**: 0.3 | 0.30 | 0.96 | layout, case_example, template_workshop | P-33 修复后可读 |
| 243 | - **置信度**: 0.3 | 0.30 | 0.95 | business_design, execution, layout | P-33 修复后可读 |
| 247 | - **置信度**: 0.3 | 0.30 | 0.95 | strategy_intent, case_example, template_workshop | P-33 修复后可读 |
| 249 | - **置信度**: 0.3 | 0.30 | 0.95 | template_workshop | P-33 修复后可读 |
| 253 | - **置信度**: 0.3 | 0.30 | 0.95 | capability, layout, case_example | P-33 修复后可读 |
| 255 | - **置信度**: 0.3 | 0.30 | 0.95 | layout, case_example | P-33 修复后可读 |
| 256 | - **置信度**: 0.3 | 0.30 | 0.92 |  | P-33 修复后可读 |
| 258 | - **置信度**: 0.3 | 0.30 | 0.95 | execution, capability, layout | P-33 修复后可读 |
| 260 | - **置信度**: 0.3 | 0.30 | 0.95 | capability, layout, case_example | P-33 修复后可读 |
| 264 | - **置信度**: 0.3 | 0.30 | 0.95 | layout, case_example, template_workshop | P-33 修复后可读 |
| 266 | - **置信度**: 0.3 | 0.30 | 0.95 | layout, case_example | P-33 修复后可读 |
| 271 | - **置信度**: 0.3 | 0.30 | 0.95 | layout, template_workshop | P-33 修复后可读 |
| 274 | - **置信度**: 0.3 | 0.30 | 0.95 | case_example, template_workshop | P-33 修复后可读 |
| 276 | - **置信度**: 0.3 | 0.30 | 0.95 | layout, template_workshop | P-33 修复后可读 |
| 280 | - **置信度**: 0.3 | 0.30 | 0.95 | execution | P-33 修复后可读 |
| 282 | - **置信度**: 0.3 | 0.30 | 0.95 | layout | P-33 修复后可读 |
| 285 | - **置信度**: 0.3 | 0.30 | 0.97 | template_workshop | P-33 修复后可读 |
| 289 | - **置信度**: 0.3 | 0.30 | 0.95 |  | P-33 修复后可读 |
| 290 | - **置信度**: 0.3 | 0.30 | 0.93 | layout, case_example | P-33 修复后可读 |
| 291 | - **置信度**: 0.3 | 0.30 | 0.92 | strategy_intent, case_example, template_workshop | P-33 修复后可读 |
| 293 | - **置信度**: 0.3 | 0.30 | 0.93 | business_design, template_workshop | P-33 修复后可读 |

## 全量 299 张审计表

| 幻灯片 | 标题 | 类型 | 有效置信度 | Parse Error | 框架域 | 深度信号 | 潜力 |
|:--|:--|:--|--:|:--|:--|:--|:--|
| 00 | 战略破局营 | 幻灯片 | 0.95 | 否 | capability, template_workshop | has_template | high |
| 01 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | case_example, template_workshop | has_template, has_examples | low |
| 02 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | business_design | has_failures | low |
| 03 | 开篇案例：跌落凡尘 | 幻灯片 | 0.92 | 否 | case_example | has_examples | low |
| 04 | 战略的意义 | 幻灯片 | 0.95 | 否 |  |  | low |
| 05 | 为什么我们做战略？ | 幻灯片 | 0.95 | 否 |  | has_questions | low |
| 06 | 不重视战略的后果： | 幻灯片 | 0.95 | 否 | business_design, layout | has_failures | medium |
| 07 | 为什么"要做"战略？ | 幻灯片 | 0.92 | 否 | layout | has_cross_domain | low |
| 08 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | execution, capability | has_questions, has_examples | medium |
| 09 | 战略是什么? | 幻灯片 | 0.95 | 否 |  |  | low |
| 10 | 问题1：为什么有的公司就是比别的公司业绩表现好？ | 幻灯片 | 0.95 | 否 | case_example | has_questions, has_examples | low |
| 11 | 战略关键词一：选择 | 幻灯片 | 0.93 | 否 |  |  | low |
| 12 | 问题2：为什么用户愿意持续选你，而非你的对手？ | 幻灯片 | 0.95 | 否 |  | has_questions | low |
| 13 | 战略关键词二：竞争优势 | 幻灯片 | 0.95 | 否 |  | has_questions, has_cross_domain | low |
| 14 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | case_example | has_examples | low |
| 15 | 问题3：做生意，是可以写个战略然后照着执行的吗？ | 幻灯片 | 0.95 | 否 | business_design, market_insight | has_steps, has_questions | high |
| 16 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | capability, layout | has_template, has_cross_domain | high |
| 17 | 我对战略的定义： | 幻灯片 | 0.95 | 否 | capability, template_workshop | has_template | high |
| 18 | 练习：一起来玩造句游戏吧~~ | 幻灯片 | 0.95 | 否 | case_example | has_examples | low |
| 19 | 战略做什么? | 幻灯片 | 0.95 | 否 |  |  | low |
| 20 | 企业战略金字塔：公司、业务与职能协同 | 框架图 | 0.95 | 否 | capability, layout | has_questions, has_examples | high |
| 21 | 案例：W&C战略金字塔对比 | 幻灯片 | 0.93 | 否 | capability, layout | has_template, has_examples | high |
| 22 | 战略的九个工作维度 | 框架图 | 0.95 | 否 | market_insight, layout | has_template, has_questions | high |
| 23 | 战略工作的核心在于解决关键增长问题！ | 幻灯片 | 0.95 | 否 | capability, layout | has_template, has_questions | high |
| 24 | 战略怎么做？什么时候做？ | 幻灯片 | 0.95 | 否 | template_workshop | has_template, has_questions | high |
| 25 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | execution, capability | has_steps | high |
| 26 | 企业不同生命周期的战略怎么做？ | 信息图 | 0.96 | 否 | capability, layout | has_steps, has_template | high |
| 27 | 战略是一名统帅最重要的基本功 | 幻灯片 | 0.92 | 否 |  |  | low |
| 28 | 一、统帅的战略角色不可替代 | 幻灯片 | 0.95 | 否 | capability, layout | has_questions, has_cross_domain | medium |
| 29 | - **置信度**: 0.3 | 未识别 | 0.96 | 是 | capability, layout |  | medium |
| 30 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | capability, template_workshop | has_questions | high |
| 31 | 战略要练哪几个方面的基本功? | 幻灯片 | 0.95 | 否 | template_workshop | has_template, has_questions | high |
| 32 | 战略基本功 5C模型 | 幻灯片 | 0.95 | 否 | business_design, strategy_intent | has_cross_domain | medium |
| 33 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | template_workshop | has_template | high |
| 34 | 以IBM "BLM业务领导力模型" 为例 | 框架图/幻灯片 | 0.95 | 否 | business_design, market_insight | has_steps, has_template | high |
| 35 | BLM的演化：华为五看三定 | 幻灯片 | 0.95 | 否 | business_design, market_insight | has_steps, has_template | high |
| 36 | 业绩差距与机会差距 | 框架图 | 0.95 | 否 | business_design, market_insight |  | medium |
| 37 | 目录 CONTENTS | 幻灯片 | 0.93 | 否 | strategy_intent, template_workshop | has_template | low |
| 38 | 我们的业绩差距 - 内 | 幻灯片 | 0.82 | 否 | strategy_intent, template_workshop | has_template, has_cross_domain | low |
| 39 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | strategy_intent, template_workshop | has_template | high |
| 40 | 业绩差距外部原因简析 | 幻灯片 | 0.92 | 否 | strategy_intent, template_workshop | has_template, has_questions | high |
| 41 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | strategy_intent, layout | has_steps | high |
| 42 | 鱼骨图详解1 - 销售 | 框架图 | 0.92 | 否 | strategy_intent, case_example | has_template, has_examples | high |
| 43 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | layout, case_example | has_steps, has_template | high |
| 44 | 鱼骨图详解2 - EBIT | 教学示意图 | 0.93 | 否 | strategy_intent | has_template | high |
| 45 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | layout, template_workshop | has_template, has_questions | high |
| 46 | 鱼骨图详解3 - 库存 | 幻灯片 | 0.93 | 否 |  | has_template, has_questions | high |
| 47 | 根因分析3 – 库存 | 幻灯片 | 0.93 | 否 | case_example, template_workshop | has_template, has_questions | low |
| 48 | 根因分析4 – 管理问题 | 框架图 | 0.95 | 否 | layout, case_example | has_steps, has_questions | high |
| 49 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | capability, case_example | has_steps, has_examples | high |
| 50 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | strategy_intent, case_example | has_template | low |
| 51 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | strategy_intent, template_workshop | has_template | low |
| 52 | 新品类机会差距 1 | 幻灯片 | 0.95 | 否 | strategy_intent, capability | has_examples, has_cross_domain | medium |
| 53 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | strategy_intent, case_example | has_template, has_examples | high |
| 54 | - **置信度**: 0.3 | 未识别 | 0.88 | 是 | strategy_intent |  | medium |
| 55 | 新用户需求机会差距 1 | 幻灯片 | 0.88 | 否 | strategy_intent | has_cross_domain | medium |
| 56 | 价值链上的新生意机会 1 | 框架图 | 0.92 | 否 | market_insight, layout | has_steps, has_template | high |
| 57 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | strategy_intent, layout | has_template | low |
| 58 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | business_design, market_insight |  | medium |
| 59 | 战略意图 | 幻灯片 | 0.92 | 否 | strategy_intent, case_example | has_steps, has_template | high |
| 60 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | case_example | has_steps, has_examples | high |
| 61 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | business_design, market_insight | has_cross_domain | medium |
| 62 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | business_design, market_insight | has_steps, has_failures | high |
| 63 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | market_insight, strategy_intent |  | low |
| 64 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | market_insight, case_example | has_template, has_examples | high |
| 65 | 目录 | 幻灯片 | 0.95 | 否 | market_insight, strategy_intent | has_examples | low |
| 66 | 产业链机会和行动计划 | 框架图 | 0.95 | 否 | market_insight, execution | has_steps, has_template | high |
| 67 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | market_insight, capability | has_steps, has_template | high |
| 68 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | market_insight, strategy_intent |  | low |
| 69 | 3.3 细分市场分析-市场总量 | 幻灯片 | 0.95 | 否 | case_example | has_examples | medium |
| 70 | 细分市场分析逻辑 | 幻灯片 | 0.95 | 否 | market_insight, capability | has_steps, has_template | high |
| 71 | - **置信度**: 0.3 | 未识别 | 0.96 | 是 | market_insight, template_workshop | has_template, has_cross_domain | high |
| 72 | 目录 | 幻灯片 | 0.95 | 否 | market_insight, strategy_intent |  | low |
| 73 | 3.4 波特五力分析 | 教学示意图 | 0.95 | 否 | market_insight |  | medium |
| 74 | 3.4 波特五力分析（1/5） | 幻灯片 | 0.95 | 否 | market_insight, case_example | has_template, has_examples | high |
| 75 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | market_insight, strategy_intent |  | low |
| 76 | 目录 CONTENTS | 幻灯片 | 0.95 | 否 | market_insight, capability | has_template | low |
| 77 | 3.5 竞争对手定义 | 幻灯片 | 0.95 | 否 | market_insight | has_cross_domain | medium |
| 78 | - **置信度**: 0.3 | 未识别 | 0.88 | 是 | market_insight, capability | has_template | high |
| 79 | 3.5 竞争格局分析-利润率 (2/3) | 幻灯片 | 0.88 | 否 | market_insight, capability | has_template | high |
| 80 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | market_insight, execution | has_steps, has_template | high |
| 81 | 目录 CONTENTS | 幻灯片 | 0.96 | 否 | market_insight, capability |  | low |
| 82 | 竞品B关键成功要素分析（2/4） | 幻灯片 | 0.92 | 否 | market_insight, case_example | has_template, has_examples | high |
| 83 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | market_insight, case_example | has_examples | medium |
| 84 | 我司与竞品关键成功因素-对比 (1/2) | 信息图 | 0.92 | 否 | market_insight, capability | has_template, has_examples | high |
| 85 | 关键成功因素-总结&策略（2/2） | 幻灯片 | 0.96 | 否 | market_insight, case_example | has_template, has_examples | high |
| 86 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | market_insight, strategy_intent | has_template, has_cross_domain | high |
| 87 | 形成我们的SWOT分析 | 教学示意图 | 0.95 | 否 | market_insight, template_workshop | has_template | high |
| 88 | 创新焦点 | 框架图 | 0.95 | 否 | business_design, market_insight | has_questions, has_cross_domain | medium |
| 89 | 增长从哪里来 | 框架图 | 0.95 | 否 | layout, case_example | has_steps, has_examples | low |
| 90 | 创新往哪里找： | 框架图/幻灯片 | 0.82 | 否 |  | has_steps, has_cross_domain | low |
| 91 | 通过安索夫矩阵探讨未来业务的发展方向 | 框架图 | 0.95 | 否 | layout, template_workshop | has_template, has_questions | high |
| 92 | 提供什么产品/服务(解决方案)? | 幻灯片 | 0.95 | 否 |  | has_steps, has_cross_domain | high |
| 93 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | case_example, template_workshop | has_template, has_examples | high |
| 94 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | template_workshop | has_template | high |
| 95 | 我们的渠道组合策略 | 幻灯片 | 0.92 | 否 | template_workshop | has_template | high |
| 96 | 创新焦点——总结 | 幻灯片 | 0.95 | 否 | business_design, strategy_intent | has_template, has_questions | high |
| 97 | 业务设计 | 框架图 | 0.95 | 否 | business_design, market_insight | has_template, has_cross_domain | high |
| 98 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | business_design, market_insight | has_questions | medium |
| 99 | 业务设计大定势：六要素*三步骤 | 教学示意图/幻灯片 | 0.95 | 否 | business_design, market_insight | has_steps, has_template | high |
| 100 | 业务设计1：客户选择 | 幻灯片 | 0.95 | 否 | business_design |  | medium |
| 101 | 为哪些目标用户服务？她们有何需求/痛点？ | 幻灯片 | 0.95 | 否 | capability | has_steps, has_questions | high |
| 102 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | capability, template_workshop | has_template | high |
| 103 | 示例：目标客群定位与描述 | 幻灯片 | 0.93 | 否 | capability, case_example | has_template, has_examples | high |
| 104 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | business_design, layout | has_template, has_examples | high |
| 105 | 示例：差异化的客群经营策略 | 幻灯片 | 0.92 | 否 | layout, case_example | has_template, has_examples | high |
| 106 | 业务设计2 - 价值主张 | 幻灯片 | 0.95 | 否 | business_design |  | medium |
| 107 | 二、价值主张 | 幻灯片 | 0.95 | 否 | business_design, template_workshop | has_template, has_questions | high |
| 108 | 顾客有何需求？需求有何变化？ | 框架图 | 0.92 | 否 | capability, template_workshop | has_cross_domain | high |
| 109 | 依据前面分群的目标消费者特征描述，思考其价值主张： | 幻灯片 | 0.95 | 否 | business_design, capability | has_template, has_questions | low |
| 110 | 对价值主张排序，并用一段话进行描述 | 幻灯片 | 0.92 | 否 | business_design, case_example | has_template, has_examples | high |
| 111 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | capability, case_example | has_template, has_examples | high |
| 112 | 对比竞品，设定未来的价值主张与定位 | 框架图 | 0.95 | 否 | business_design, market_insight | has_template, has_examples | high |
| 113 | 得出我们的差异化核心价值主张 | 框架图 | 0.93 | 否 | business_design, case_example | has_template, has_examples | high |
| 114 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | business_design, template_workshop | has_template | high |
| 115 | 价值获取：如何实现我们的价值主张？ | 幻灯片 | 0.95 | 否 | business_design, template_workshop | has_template, has_questions | high |
| 116 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | capability, template_workshop | has_steps, has_template | high |
| 117 | 盈利模式示例 - M采用代理加盟的连锁加盟模式（1/4） | 信息图 | 0.95 | 否 | business_design, capability | has_template, has_examples | high |
| 118 | 如何实现持续的价值增值(经营壁垒)？ | 幻灯片 | 0.96 | 否 | execution, layout | has_template, has_examples | high |
| 119 | 业务设计4：活动范围 | 幻灯片 | 0.93 | 否 | business_design, template_workshop | has_template | high |
| 120 | 活动范围 | 幻灯片 | 0.95 | 否 | business_design, market_insight | has_questions, has_cross_domain | medium |
| 121 | 活动范围 | 框架图 | 0.92 | 否 | business_design, execution | has_template, has_examples | high |
| 122 | 业务设计5 战略控制点 | 幻灯片 | 0.95 | 否 | business_design |  | medium |
| 123 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | business_design, capability | has_template, has_questions | high |
| 124 | 价值定位模型 | 幻灯片 | 0.95 | 否 | business_design, layout | has_template, has_cross_domain | high |
| 125 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | business_design, case_example | has_template, has_questions | high |
| 126 | 业务设计6 风险管理 | 幻灯片 | 0.95 | 否 | business_design |  | medium |
| 127 | 业务设计的风险识别与评估 | 幻灯片 | 0.92 | 否 | business_design, layout | has_steps, has_template | high |
| 128 | 1、识别和评估风险：麦肯锡7-S模型 | 教学示意图 | 0.95 | 否 | business_design, execution | has_steps, has_questions | low |
| 129 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | business_design, template_workshop | has_steps, has_template | high |
| 130 | 业务设计7 总结 | 幻灯片 | 0.95 | 否 | business_design, template_workshop | has_template | high |
| 131 | 业务设计结果示例 | 框架图 | 0.95 | 否 | business_design, execution | has_steps, has_template | high |
| 132 | 为公司各业态/业务单元制订不同的业务设计概要 | 框架图 | 0.95 | 否 | business_design, capability | has_steps, has_template | high |
| 133 | 关键任务 | 框架图 | 0.95 | 否 | business_design, market_insight | has_steps, has_questions | high |
| 134 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | execution, layout | has_template | low |
| 135 | 公司业务策略汇总 | 幻灯片 | 0.93 | 否 | template_workshop | has_steps, has_template | high |
| 136 | - **置信度**: 0.3 | 未识别 | 0.93 | 是 | business_design, strategy_intent | has_template | high |
| 137 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | template_workshop | has_template | high |
| 138 | 公司级关键举措推进表 | 信息图 | 0.95 | 否 | template_workshop | has_template | high |
| 139 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | template_workshop | has_steps, has_template | high |
| 140 | 财务预测 | 幻灯片 | 0.92 | 否 | layout | has_template | high |
| 141 | 最终交付：战略蓝图（三年） | 框架图 | 0.93 | 否 | capability, case_example | has_steps, has_template | high |
| 142 | 公司/各BU/业务单元/业态 的战略地图 | 框架图 | 0.95 | 否 | business_design, market_insight | has_template | high |
| 143 | 目录 CONTENTS | 幻灯片 | 0.95 | 否 | execution, layout |  | low |
| 144 | 支撑战略目标所需打造的全部核心能力 | 框架图 | 0.92 | 否 | execution, capability | has_template, has_examples | high |
| 145 | 核心能力评估矩阵 | 框架图 | 0.95 | 否 | capability, layout | has_steps, has_template | high |
| 146 | 目录 CONTENTS | 幻灯片 | 0.95 | 否 | execution, layout |  | low |
| 147 | - **置信度**: 0.3 | 未识别 | 0.88 | 是 | execution | has_questions, has_cross_domain | low |
| 148 | 逐个检查与内外部合作伙伴的依赖关系 | 幻灯片 | 0.95 | 否 | template_workshop | has_template, has_questions | high |
| 149 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | execution, layout | has_template | low |
| 150 | 资源与支撑体系 | 信息图 | 0.93 | 否 | market_insight, execution |  | medium |
| 151 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | layout, template_workshop | has_template | high |
| 152 | 财务资源分配 | 幻灯片 | 0.95 | 否 | layout, template_workshop | has_template, has_cross_domain | high |
| 153 | IT资源排布 | 幻灯片 | 0.95 | 否 | layout | has_steps, has_template | high |
| 154 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | market_insight, layout |  | medium |
| 155 | 公关资源：借助政策和政府公信力 | 幻灯片 | 0.95 | 否 | layout, template_workshop | has_template | high |
| 156 | 金融资源：联合多方金融势力 | 信息图 | 0.92 | 否 | layout |  | low |
| 157 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | market_insight, capability | has_steps, has_template | high |
| 158 | - **置信度**: 0.3 | 未识别 | 0.93 | 是 | business_design, layout | has_template | high |
| 159 | 目录 CONTENTS | 幻灯片 | 0.92 | 否 | capability, template_workshop | has_template | low |
| 160 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | capability, case_example | has_steps, has_template | high |
| 161 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | capability, template_workshop | has_template | high |
| 162 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | capability, layout | has_steps, has_template | high |
| 163 | 关键任务卡片（将次年工作任务逐一细化） | 框架图 | 0.95 | 否 | execution, layout | has_steps, has_template | high |
| 164 | 目录 CONTENTS | 幻灯片 | 0.95 | 否 | capability | has_steps | low |
| 165 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | layout, case_example | has_steps, has_examples | high |
| 166 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | template_workshop | has_steps, has_template | high |
| 167 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 |  | has_template | high |
| 168 | 最终交付：2、财务目标（渠道维度） | 幻灯片 | 0.92 | 否 | template_workshop | has_template | high |
| 169 | 最终交付：2、财务目标（区域维度） | 幻灯片 | 0.95 | 否 | template_workshop | has_template | high |
| 170 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | execution, capability | has_template, has_examples | high |
| 171 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | execution, layout | has_template, has_questions | high |
| 172 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | capability, case_example | has_template, has_examples | high |
| 173 | 风险应对 | 幻灯片 | 0.92 | 否 | business_design, template_workshop | has_template | high |
| 174 | 目录 CONTENTS | 幻灯片 | 0.93 | 否 | capability |  | low |
| 175 | 三年计划财务结果 | 幻灯片 | 0.95 | 否 |  | has_template | high |
| 176 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | template_workshop | has_template | high |
| 177 | 净利润变动分析 | 信息图 | 0.95 | 否 |  |  | low |
| 178 | 三年挑战收入目标 | 幻灯片 | 0.95 | 否 | template_workshop | has_template | high |
| 179 | - **置信度**: 0.3 | 未识别 | 0.85 | 是 |  | has_template | high |
| 180 | 分渠道净收入 | 幻灯片 | 0.92 | 否 | template_workshop | has_template | low |
| 181 | 市场费用明细 | 幻灯片 | 0.92 | 否 | layout |  | low |
| 182 | 行销费用明细 | 幻灯片 | 0.92 | 否 | template_workshop | has_template | high |
| 183 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | template_workshop | has_template | high |
| 184 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | template_workshop | has_template | high |
| 185 | 各部门行政费用 | 框架图 | 0.95 | 否 | template_workshop | has_template | high |
| 186 | 组织架构调整及人工效能提升 | 幻灯片 | 0.92 | 否 | layout, template_workshop | has_template | high |
| 187 | 资本支出三年计划 | 幻灯片 | 0.95 | 否 | template_workshop | has_template | high |
| 188 | - **置信度**: 0.3 | 未识别 | 0.96 | 是 | template_workshop | has_template | high |
| 189 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | template_workshop | has_template | high |
| 190 | - **置信度**: 0.3 | 未识别 | 0.93 | 是 |  |  | low |
| 191 | - **置信度**: 0.3 | 未识别 | 0.88 | 是 |  | has_template | high |
| 192 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | template_workshop | has_template | high |
| 193 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | capability | has_questions | medium |
| 194 | 战略洞察双引擎：从看到到看透 | 幻灯片 | 0.92 | 否 | capability, layout |  | medium |
| 195 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | market_insight, template_workshop | has_template, has_cross_domain | high |
| 196 | 小组PK：5秒抢答 | 幻灯片 | 0.96 | 否 |  |  | low |
| 197 | 案例背景 | 幻灯片 | 0.95 | 否 | capability, case_example | has_questions, has_examples | medium |
| 198 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | case_example, template_workshop | has_steps, has_template | high |
| 199 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | business_design, strategy_intent |  | medium |
| 200 | 答案找不到，更上一层楼（注意：每次只上一层楼） | 框架图 | 0.95 | 否 | strategy_intent, template_workshop | has_questions, has_cross_domain | high |
| 201 | 另一种工作顺序（从上往下的假设验证） | 幻灯片 | 0.95 | 否 | layout, template_workshop | has_steps, has_template | high |
| 202 | 小组PK：连线题 | 幻灯片 | 0.95 | 否 |  |  | low |
| 203 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | market_insight, execution | has_steps, has_template | low |
| 204 | 模型选择的心智模式 | 幻灯片 | 0.95 | 否 | capability | has_questions, has_cross_domain | medium |
| 205 | 2、角度引擎——配置你的"认知透镜组合" | 幻灯片 | 0.95 | 否 |  | has_steps, has_questions | high |
| 206 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | template_workshop | has_template, has_questions | high |
| 207 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | market_insight, capability | has_examples | medium |
| 208 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 |  | has_questions, has_failures | low |
| 209 | 案例：百分之百的准确率 | 幻灯片 | 0.95 | 否 | case_example | has_examples | low |
| 210 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | layout | has_questions, has_failures | low |
| 211 | 案例：看不到的全局库存 | 幻灯片 | 0.92 | 否 | case_example | has_examples | low |
| 212 | 小组练习：拯救书店 | 幻灯片 | 0.95 | 否 | layout, case_example | has_template, has_examples | low |
| 213 | - **置信度**: 0.3 | 未识别 | 0.93 | 是 | capability, case_example | has_examples, has_cross_domain | medium |
| 214 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | case_example, template_workshop | has_steps, has_template | low |
| 215 | 第2阶段：聚焦镜练 | 幻灯片 | 0.92 | 否 | capability, case_example | has_steps, has_template | low |
| 216 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | case_example, template_workshop | has_steps, has_template | low |
| 217 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | template_workshop | has_template | high |
| 218 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | market_insight, capability | has_steps, has_template | low |
| 219 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 |  | has_questions, has_failures | low |
| 220 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | layout | has_steps, has_questions | high |
| 221 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | case_example | has_examples | low |
| 222 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | capability, layout | has_steps, has_template | high |
| 223 | 第1阶段：现状→问题（模型与图表环节） | 幻灯片 | 0.95 | 否 | capability, case_example | has_steps, has_questions | high |
| 224 | 第2阶段：问题→根因（假设循环环节） | 教学示意图 | 0.95 | 否 | template_workshop | has_steps, has_template | high |
| 225 | 第3阶段：根因→改进方向（角度引擎环节） | 幻灯片 | 0.93 | 否 | case_example, template_workshop | has_steps, has_template | high |
| 226 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | layout, template_workshop | has_steps, has_template | high |
| 227 | 洞察力到底在修炼什么？ | 框架图 | 0.93 | 否 | market_insight, capability | has_steps, has_template | high |
| 228 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | capability, layout | has_steps, has_template | high |
| 229 | 洞察力如何修炼：一个实践框架 | 幻灯片 | 0.95 | 否 | capability, case_example | has_template, has_questions | low |
| 230 | 2.3 战略基本功-战略布局 | 幻灯片 | 0.92 | 否 | template_workshop | has_template | high |
| 231 | 战略布局 | 幻灯片 | 0.95 | 否 | capability, layout | has_steps, has_examples | high |
| 232 | 当前企业战略布局的挑战与痛点 | 幻灯片 | 0.95 | 否 | market_insight, capability | has_template, has_failures | high |
| 233 | 1、增长型战略布局 | 幻灯片 | 0.95 | 否 | layout, template_workshop | has_template | high |
| 234 | 碗里和锅里的生意：战不战？退不退？留不留？ | 幻灯片 | 0.92 | 否 |  | has_questions, has_cross_domain | low |
| 235 | 碗里和锅里的生意：战不战？退不退？留不留？ | 幻灯片 | 0.95 | 否 | layout, template_workshop | has_steps, has_template | high |
| 236 | 田里的生意：大不大？小不小？赌不赌？ | 框架图 | 0.95 | 否 | layout | has_template, has_cross_domain | high |
| 237 | 挖掘细分市场机会的五大绝招 | 幻灯片 | 0.95 | 否 |  |  | low |
| 238 | 小李飞刀：打"进化"时间差 | 幻灯片 | 0.92 | 否 | case_example | has_examples, has_cross_domain | medium |
| 239 | 2. 分筋错骨手：与市场常识反向而行 | 幻灯片 | 0.92 | 否 | market_insight, case_example | has_examples | medium |
| 240 | 葵花点穴手：聚焦细分客群 | 幻灯片 | 0.93 | 否 | market_insight, layout | has_examples | medium |
| 241 | - **置信度**: 0.3 | 未识别 | 0.96 | 是 | layout, case_example | has_template, has_examples | high |
| 242 | 降龙十八掌：寻找价值链上其它环节的市场机会 | 幻灯片 | 0.95 | 否 | business_design, case_example | has_examples | medium |
| 243 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | business_design, execution | has_examples, has_cross_domain | medium |
| 244 | 田里的生意：拆用户→拆场景→挖内核 | 幻灯片 | 0.95 | 否 | business_design, market_insight | has_failures, has_cross_domain | medium |
| 245 | 不同业务类型，不同的关注重点 | 幻灯片 | 0.95 | 否 | business_design, layout | has_template, has_examples | high |
| 246 | 三个地平线：短中长期各项业务如何管理？ | 教学示意图/框架图 | 0.95 | 否 | strategy_intent, capability | has_template | high |
| 247 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | strategy_intent, case_example | has_template | low |
| 248 | 1、全业务BCG矩阵分析 | 幻灯片 | 0.96 | 否 | layout, case_example | has_template, has_questions | high |
| 249 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | template_workshop | has_template, has_cross_domain | high |
| 250 | 3、填写三个地平线图（时间3~5年） | 框架图 | 0.96 | 否 | strategy_intent, layout | has_steps, has_template | high |
| 251 | 初步描绘三个地平线的目标与策略 | 幻灯片 | 0.96 | 否 | strategy_intent, template_workshop | has_template, has_questions | high |
| 252 | 撤退型战略布局 | 幻灯片 | 0.95 | 否 | layout | has_steps, has_cross_domain | high |
| 253 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | capability, layout | has_steps, has_questions | high |
| 254 | 撤退型布局2 去除 | 幻灯片 | 0.95 | 否 | layout, case_example | has_steps, has_examples | high |
| 255 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | layout, case_example | has_steps, has_examples | high |
| 256 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 |  | has_questions | low |
| 257 | 战略布局中的转型路径 | 幻灯片 | 0.95 | 否 | capability, layout | has_template, has_examples | high |
| 258 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | execution, capability |  | medium |
| 259 | 突破型布局1 重新想象 | 幻灯片 | 0.95 | 否 | market_insight, layout | has_template, has_questions | high |
| 260 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | capability, layout | has_examples, has_cross_domain | medium |
| 261 | 突破型布局2 击破边界2 | 幻灯片 | 0.92 | 否 | capability, layout | has_examples, has_cross_domain | medium |
| 262 | 小组讨论：家装生态平台 | 幻灯片 | 0.95 | 否 |  |  | low |
| 263 | 重要工具：平台商业模式地图 | 框架图 | 0.95 | 否 | business_design, layout | has_template, has_examples | high |
| 264 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | layout, case_example | has_template, has_examples | high |
| 265 | 突破型布局3 后手布局2 | 幻灯片 | 0.95 | 否 | execution, capability | has_steps, has_examples | high |
| 266 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | layout, case_example | has_examples, has_cross_domain | medium |
| 267 | 小组练习 | 幻灯片 | 0.95 | 否 | case_example |  | low |
| 268 | 小组共创：突破性战略布局能力练习 | 幻灯片 | 0.95 | 否 | capability, layout | has_steps, has_template | low |
| 269 | 2.4 战略基本功-价值创造体系 | 幻灯片 | 0.92 | 否 | template_workshop | has_template | high |
| 270 | 案例：高端白酒专卖店体系 | 幻灯片 | 0.93 | 否 | case_example | has_examples | low |
| 271 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | layout, template_workshop | has_template, has_questions | high |
| 272 | 价值创造体系示例：某定位公司"万箭穿心"模型 | 框架图 | 0.95 | 否 | layout, case_example | has_steps, has_examples | high |
| 273 | 如何构建价值创造体系：三层架构+五大原则 | 幻灯片/框架图 | 0.93 | 否 | business_design, strategy_intent | has_steps, has_failures | high |
| 274 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | case_example, template_workshop | has_template | low |
| 275 | 诊断并优化你的价值创造体系 | 幻灯片 | 0.95 | 否 | business_design, execution | has_steps, has_template | high |
| 276 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | layout, template_workshop | has_template | high |
| 277 | 2.5 战略基本功-变革管理 | 幻灯片 | 0.95 | 否 | execution, capability |  | medium |
| 278 | 战略执行的最大挑战到底是什么？ | 幻灯片 | 0.95 | 否 |  | has_questions | low |
| 279 | 内外部环境高速变化，绝不会依你意愿来行事 | 信息图 | 0.88 | 否 | execution, capability | has_cross_domain | medium |
| 280 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | execution | has_failures, has_cross_domain | low |
| 281 | 应对之道：变革管理的三个层级 | 幻灯片 | 0.95 | 否 | execution |  | low |
| 282 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 | layout | has_template, has_cross_domain | high |
| 283 | 变革管理的基本功：维持四大平衡 | 框架图 | 0.95 | 否 | execution, template_workshop | has_template | high |
| 284 | 适配变革的组织结构：三大平衡特征 | 幻灯片 | 0.92 | 否 | execution, layout | has_steps | high |
| 285 | - **置信度**: 0.3 | 未识别 | 0.97 | 是 | template_workshop | has_steps, has_template | high |
| 286 | 小组任务 | 幻灯片 | 0.92 | 否 | template_workshop | has_template | high |
| 287 | 最终真实案例路演 | 幻灯片 | 0.92 | 否 | case_example | has_examples | low |
| 288 | 每组推出一个案例，为最终对决制订战略： | 幻灯片 | 0.95 | 否 | strategy_intent, layout | has_steps, has_template | high |
| 289 | - **置信度**: 0.3 | 未识别 | 0.95 | 是 |  | has_steps, has_questions | high |
| 290 | - **置信度**: 0.3 | 未识别 | 0.93 | 是 | layout, case_example | has_questions, has_examples | medium |
| 291 | - **置信度**: 0.3 | 未识别 | 0.92 | 是 | strategy_intent, case_example | has_template | low |
| 292 | 机会差距分析： | 幻灯片 | 0.88 | 否 | strategy_intent, template_workshop | has_template, has_cross_domain | high |
| 293 | - **置信度**: 0.3 | 未识别 | 0.93 | 是 | business_design, template_workshop | has_template, has_questions | high |
| 294 | 业务设计大定势：六要素*三步骤 | 框架图 | 0.95 | 否 | business_design, template_workshop | has_steps, has_template | high |
| 295 | 战略主题-战略举措-行动任务（三年） | 框架图 | 0.95 | 否 | capability, template_workshop | has_template | high |
| 296 | 财务预测 | 信息图 | 0.92 | 否 | layout, template_workshop | has_template, has_cross_domain | high |
| 297 | "九层宝塔" 模型简介 | 框架图 | 0.95 | 否 | template_workshop | has_questions, has_cross_domain | high |
| 298 | 感谢聆听 - 课程结束页 | 幻灯片 | 0.95 | 否 |  |  | low |
