---

id: tool-半肥猫-课程Skill化的八步工作流
title: 技能：课程Skill化的八步工作流
type: tool
status: enriched
domain:
- src_unknown
- src_unknown
source_person: 半肥猫
source_context: AI俱乐部-AI学习落地 分享
source_refs:
- 00_inbox/半肥猫-AI学习落地-口述.md
tools_required:
- src_unknown
- src_unknown
prerequisite_skills:
- src_unknown
- src_unknown
related:
  - [[concept-半肥猫-ai-learning-toolification-methodology]]
  - [[tool-ban-fei-mao-pan-duan-ke-cheng-shi-fou-zhi-de-zuo-cheng-skill]]
  - [[tool-ban-fei-mao-she-ji-skill-de-ping-fen-gui-ze-yu-feng-xian-bian-jie]]
  - [[tool-ban-fei-mao-yong-skill-zuo-dui-bi-ce-shi-yan-zheng-xiao-guo]]
  - [[tool-ban-fei-mao-qing-xi-zi-liao-wei-markdown-ge-shi-wei-gei-ai]]
  - [[tool-ban-fei-mao-yong-yaml-ge-shi-zuo-zhi-shi-ku-yuan-zi-hua-biao-qian]]
  - [[case-ban-fei-mao-conversion-hacker-skill]]
  - [[case-ban-fei-mao-skill-ab-test]]
created_at: '2026-06-07'
updated_at: '2026-06-28'
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.75
trust_level: medium
diagnostic_signals:
- lens: 流程缺失
  follow_up: 先执行第1步质量门判断：是否有科学底层、可验证案例、明确边界
- lens: 测试缺失
  follow_up: 检查是否跳过了第7步A/B测试，测试是必需项不是可选项
- lens: 证据校准缺失
  follow_up: 执行第5步批判性审查：不默认老师全对，补充真实案例和权威资料
- lens: 维护缺失
  follow_up: 维护占生命周期80%，把维护成本计入总投入，定期迭代
- lens: 拒绝能力不足
  follow_up: 检查第4步诊断协议是否包含拒绝条件、风险分级、触发边界

---

# 技能：课程Skill化的八步工作流

## Summary

半肥猫提出的八步工作流是把外部课程/方法论转化为可复用AI Skill的工程化路径。核心逻辑：**不是每门课都值得做Skill，但值得做的课必须按工程化流程处理**。八步覆盖了从"判断"到"迭代"的完整闭环，确保Skill有边界、可测试、能拒绝、可维护。

## Claims

- src_unknown

- src_unknown

- src_unknown

- src_unknown

## 操作步骤

1. **判断是否值得做Skill**——评估课程是否有科学底层方法论、资料是否完整、方法是否经过实践检验
2. **整理课程主线为结构化文档**——去噪声、保留核心方法论、用Markdown结构化
3. **抽取案例、问答、行业应用为案例库**——正面案例+负面案例+边界案例
4. **把课程方法变成诊断协议**——适用边界、评分规则、风险分级、触发条件
5. **证据校准和课程主张审查**——不默认老师全对、补充真实案例、补充权威资料
6. **设定技能目录结构**——YAML标签、原子化文档、语义切分
7. **测试（正向+反向+高风险场景）**——用多维度评分体系做A/B测试
8. **安装、调试、迭代、写文档**——部署到AI客户端、持续积累反例、版本迭代

## Constraints & Boundaries

### 适用边界

| 边界 | 说明 |
|:-----|:-----|
| ✅ 适合 | 有科学方法论底座的培训课程 |
| ✅ 适合 | 需要反复使用的分析/诊断/决策框架 |
| ✅ 适合 | 团队内部需要统一标准的业务方法 |
| ✅ 适合 | 有专门知识管理角色的团队（≥3人） |
| ❌ 不适合 | 课程本身质量不足（东拼西凑、无方法论） → 先筛选课程质量 |
| ❌ 不适合 | 一次性使用、不需要复用的场景 → 用自然语言提示词即可 |
| ❌ 不适合 | 没有测试资源（不做A/B测试） → 测试是必需项，无测试不做Skill |
| ❌ 不适合 | 1-2人小团队且时间紧迫 → 八步流程对小型团队过于重量级 |

#| 模式 | 症状 | 修复 |
|:-----|:-----|:-----|
| **跳过质量门** | 直接开始做，浪费时间在低质量课程上 | 严格执行第1步：是否有科学底层、可验证案例、明确边界 |
| **证据校准缺失** | Skill传播了课程中的错误观点 | 不默认老师全对，做批判性审查，补充真实案例和权威资料 |
| **不做A/B测试** | 不知道Skill到底有没有用 | 测试是必需项不是可选项，用多维度评分体系做对比 |
| **忽视维护** | Skill快速过时，失效 | 维护占生命周期80%，把维护成本计入总投入，设迭代周期 |
| **过度工程化** | 追求95分Skill，但两周后才能用 | 快速变化市场中，80分但能立即用的Skill更有价值 |
| **量化暴政** | 12维度评分体系产生虚假客观感 | 承认评分主观性，用"满意解"替代"最优解" |
| **忽视用户Job** | 制造了完美Skill但用户只想快速得结论 | 先问用户想完成什么工作，再决定Skill粒度 |
| **维护陷阱** | 80%时间维护旧Skill，无法开发新Skill | 设定维护预算上限，超过则淘汰旧Skill |

## 工具/环境

- src_unknown（协助整理和结构化的辅助工具，非替代人工判断）
- src_unknown
- src_unknown

## 常见失败模式

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 为什么有效

工程化流程确保Skill的质量可控、边界清晰、可验证。八步覆盖了从"输入质量"到"输出质量"的完整闭环。

## Critique

### 内部局限

- src_unknown

- src_unknown

- src_unknown

### 外部攻击

#### Clayton Christensen 的"颠覆性创新"与"过度工程化"

**Clayton Christensen**（*The Innovator's Dilemma* 作者，哈佛商学院教授）从创新理论角度质疑这个八步流程：

- src_unknown

- src_unknown

- src_unknown

> **Christensen 的拷问**："你的八步流程制造的是'更好的马车'，但用户可能想要的是'汽车'。当一个团队把80%的时间花在维护现有Skill上时，他们就没有时间去想'是不是不该用Skill来解决这个问题'。你被自己的流程绑架了。"

#### Herbert Simon 的"有限理性"与"量化暴政"

**Herbert Simon**（诺贝尔经济学奖得主，*Administrative Behavior* 作者，"有限理性"理论提出者）从决策科学角度质疑这个流程：

- src_unknown

- src_unknown

- src_unknown

> **Simon 的拷问**："你的12维度评分体系，每个维度的分数是怎么确定的？是AI自己打的还是人打的？如果是人打的，那这套'量化'体系本质上就是主观判断的包装。你在用'看起来科学'的方法做'本质上主观'的事。这不是决策科学，这是决策戏剧。"

## Synthesis

| 关系 | 目标节点 | 说明 |
|------|----------|------|
| 上位 | [[concept-半肥猫-ai-learning-toolification-methodology]] | 八步工作流是L2课程Skill化的核心工程化路径 |
| 下位 | [[tool-ban-fei-mao-pan-duan-ke-cheng-shi-fou-zhi-de-zuo-cheng-skill]] | 八步中的第1步——质量门判断 |
| 下位 | [[tool-ban-fei-mao-she-ji-skill-de-ping-fen-gui-ze-yu-feng-xian-bian-jie]] | 八步中的第4步——诊断协议设计 |
| 下位 | [[tool-ban-fei-mao-yong-skill-zuo-dui-bi-ce-shi-yan-zheng-xiao-guo]] | 八步中的第7步——测试验证 |
| 下位 | [[tool-ban-fei-mao-qing-xi-zi-liao-wei-markdown-ge-shi-wei-gei-ai]] | 八步中的第2步——资料预处理 |
| 下位 | [[tool-ban-fei-mao-yong-yaml-ge-shi-zuo-zhi-shi-ku-yuan-zi-hua-biao-qian]] | 八步中的第6步——目录结构设计 |
| 案例 | [[case-ban-fei-mao-conversion-hacker-skill]] | 八步的完整实例——转化率黑客Skill |
| 案例 | [[case-ban-fei-mao-skill-ab-test]] | 八步中第7步的A/B测试实例 |
| 暗知识 | [[dk-ban-fei-mao-skill-rejection-value]] | "Skill的最大价值是拒绝"——八步设计的核心洞察 |
| KDO对接 | kdo-encapsulate | KDO的skill编译命令 ↔ 八步工作流的内容设计 |

## 来源

- src_unknown

## Feedback Path

- src_unknown

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？
