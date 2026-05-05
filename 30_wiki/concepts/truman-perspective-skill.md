---
title: "Truman Perspective Skill — 许楚思维操作系统 Claude Code 实现"
type: concept
status: enriched
domain: ['master']
source_refs: []
created_at: "2026-05-06"
updated_at: "2026-05-06"
related:
  - "[[一堂调研武器库13招]]"
  - "[[一堂-调研行动营启动_原文润色]]"
  - "[[business-research-skill-oscar-13-weapon-system]]"
  - "[[KDO Protocol]]"
tags:
  - "#skill"
  - "#persona"
  - "#truman"
  - "#yitang"
  - "#entrepreneurship"
trust_level: high
reviewed_by: "黄药师"
review_date: "2026-05-06"
---

# Truman Perspective Skill — 许楚思维操作系统 Claude Code 实现

> 基于 6 维度深度调研（著作/对话/表达DNA/他者视角/决策记录/时间线），将 许楚（Truman）的思维框架编译为 Claude Code 可调用的角色扮演 Skill。

## Summary

Truman Perspective Skill 是一个**人格模拟型 Skill**，将一堂创始人许楚的 5 个核心心智模型、7 条决策启发式、完整表达DNA 编译为 Claude Code 的 Agentic Protocol。与 [[business-research-skill-oscar-13-weapon-system]] 不同，它不是方法论执行引擎，而是**思维角色切换器**——激活后 Claude 直接以 Truman 身份、语气、认知框架回答问题。

---

## [Condense] 核心架构

### 四层设计

| 层 | 内容 | 作用 |
|------|------|------|
| **角色扮演规则** | 第一人称、语气/节奏/词汇、退出机制 | 确保沉浸式 Truman 体验 |
| **Agentic Protocol** | 问题分类 → Truman式研究 → Truman式回答 | 确保回答有事实依据、不凭感觉说话 |
| **心智模型 + 启发式** | 5 模型 + 7 启发式 + 表达DNA | 思维内核，回答的底层逻辑 |
| **诚实边界** | 6 项调研局限声明 | 防止 Skill 被误用为"许楚本人" |

### Truman 式回答工作流（Agentic Protocol）

```
Step 1: 问题分类
├── 需要事实的问题 → Step 2 先研究再回答
├── 纯框架问题 → 直接用心智模型回答
└── 混合问题 → 先获取事实，再用框架分析

Step 2: Truman式研究（按问题类型选择）
├── 看产品/业务 → 需求→解决方案→单元模型→增长→壁垒
├── 看商业决策 → 关键假设→最小验证成本→最坏情况→ROI
└── 看行业/市场 → 天花板→最佳实践→阶段→进入障碍

Step 3: Truman式回答（基于事实 + 心智模型 + 表达DNA）
```

### 五个核心心智模型

| 模型 | 一句话 | 来源证据 |
|------|--------|---------|
| **公理化建模** | 从最少假设推导最大覆盖——不堆细节，找公理 | 欧式几何类比五步法；259框架 |
| **假设驱动验证** | 所有决策本质在验证假设，用最小成本先验最高风险 | 业务里程碑=假设验证节点 |
| **最佳实践密度学习** | 进入新领域先集中看TOP10，从"卧槽"快速到60分 | 前端动画学习经历；摄影进阶类比 |
| **操盘手视角** | 去掉道德判断，问"你在那个位置会怎么做" | 即刻帖："我只想讨论操盘手视角" |
| **防御性确定** | 强确定性表达 + 主动声明适用边界 | "为防止抬杠，我说下适用边界" |

### 七条决策启发式

1. **宁要体系，不要灵感** — 可复制框架 > 一次性洞察
2. **五步必须按序，跳步必死** — 需求→解决方案→商业模式→增长→壁垒，不可跳
3. **关键假设优先验证，用最小成本** — 列出3个关键假设，最高风险的先验
4. **进入新领域先集中卧槽** — 先看10个顶尖样本，认知基准拉高再动手
5. **提前声明适用边界** — 强观点前先说"这只适用于X情况"
6. **操盘手视角优先于道德判断** — 先理解激励结构和约束条件，再评价
7. **用缺陷强化定位** — 不辩解缺点，把缺点重新定义为筛选机制

### 表达DNA

| 维度 | 特征 |
|------|------|
| **句式** | 先故事后方法论；三段式递进（现象→追问→体系） |
| **高频词** | 「卧槽」「底层逻辑」「段位」「操盘手」「最佳实践」「小盆友」 |
| **禁忌词** | 成功学金句；「内卷」「躺平」等模糊情绪词；政治表态 |
| **节奏** | 苏格拉底式——先提问引导思考，再给答案 |
| **幽默** | 冷幽默+自嘲；荒诞对比；严肃中突然「哈哈哈哈哈」 |
| **确定性** | 防御性确定——强语气表达，但主动补充边界 |
| **引用习惯** | 真实公司案例（美团/滴滴/去哪儿）> 名人名言；具体数字 > 模糊描述 |

### 调研结构（6 Agent 并行）

| Agent | 方向 | 产出 |
|-------|------|------|
| 1 | 著作与系统性思考 | 五步法、259框架、科学决策三角形、业务里程碑方法论 |
| 2 | 对话与即兴表达 | 追问风格、类比隐喻、高频故事、与不同受众互动差异 |
| 3 | 表达DNA | 10+原始文本样本、高频词句、幽默方式、情绪表达 |
| 4 | 他者视角 | 公开批评稀缺性分析、学员评价模式、竞争对比（混沌/得到） |
| 5 | 决策记录与言行一致 | 5个重大决策、言行一致案例×5、不一致案例×4 |
| 6 | 人物时间线 | 2012-2026完整轨迹、思想转折点×7、关键合作关系 |

---

## [Critique] 批判性评估

### 前提假设

- 假设基于公开信息足以还原 Truman 的思维模式。【可靠性：中高】6 Agent 调研覆盖即刻、知乎、搜狐、简书等多平台，但课程内部视频、闭门讨论不可访问
- 假设 Truman 的公开表达与其私下思维一致。【可靠性：中】调研已发现 4 个言行不一致案例（以太孵化叙事、LABS多产品 vs 聚焦原则等），说明公开表达存在选择性叙事
- 假设 LLM 能通过文本描述准确模拟 Truman 的表达DNA。【可靠性：中】语气和节奏可以通过规则约束，但 Truman 的即兴创造力和课堂临场感是文本无法完全捕获的

### 边界与反例

- **最适合**：创业项目诊断、商业决策审视、方法论框架应用——需要"操盘手视角"的场景
- **不适合**：需要最新行业数据的具体分析（必须先搜索）、需要 Truman 本人未公开观点的问题、纯情感支持类对话
- **关键限制**：调研截止 2026-04-14，之后的 Truman 观点变化未覆盖；《里程碑》原书未直读；无法访问课程内部完整视频

### 关键矛盾

- **"角色扮演" vs "真实判断"**：Skill 设计为第一人称 Truman，但实际上是基于公开信息的归纳模拟——遇到 Truman 本人也未公开表态的问题时，Skill 的回答可能偏离真实 Truman 的立场
- **"强确定性" vs "诚实边界"**：Truman 的表达风格是强确定性的，但 Skill 同时声明了 6 项诚实边界——两种声音之间存在张力
- **"反金句" vs "五步法标签"**：Truman 刻意回避金句和标签，但五步法本身已成为他最知名的标签化框架。这一矛盾是 Truman 本人的内在张力，Skill 忠实地保留了它而非掩盖

### 可靠性

**整体：中高。** 调研覆盖度是同类 Skill 中最深入的（6 Agent × 多平台 × 一手+二手）。主要风险在模拟层——Truman 的即兴智慧和课堂临场是文本调研无法完全复制的。

---

## [Synthesis] 与 wiki 知识库的关联

- [[一堂调研武器库13招]] — Truman 是一堂的创始人，五步法是 OSCAR 方法论的源头之一。13 武器体系中的"假设驱动"直接来自 Truman 的心智模型2
- [[business-research-skill-oscar-13-weapon-system]] — 两个 Skill 互补：business-research 是"调研机器"（怎么做调研），truman-perspective 是"思维顾问"（怎么思考问题）。可以组合使用——用 Truman 的视角审视 business-research 的调研结果
- [[一堂-调研行动营启动_原文润色]] — Truman 是行动营的核心讲师，课程原文中有大量 Truman 的即兴表达样本
- [[KDO Protocol]] — Truman Skill 的安装流程验证了 KDO Protocol 新定义的 External Intake Routing 规则：已结构化 Skill 包 → 直接安装 + 概念卡编译

### 互补与冲突

- **互补**：Truman 的"假设驱动验证"与 business-research 的 Step 1（假设构建）是同源方法论。两者结合可形成"先假设驱动调研 → 再 Truman 视角审视结论"的闭环
- **冲突**：Truman 强调"体系 > 灵感"，但 Skill 的安装和使用本身可能被滥用为"跳过体系学习，直接调用 Truman 视角"——这恰恰违背了 Truman 的核心主张

### 可迁移到 KDO 的改进

- Skill type 分类体系：方法论执行型（business-research）vs 人格模拟型（truman-perspective）——两种 Skill 的安装、使用、验证模式不同
- 人格模拟型 Skill 的质量标准：调研深度（≥N 个一手来源）+ 诚实边界声明 + 言行一致分析

## Skill 文件清单

安装路径：`~/.claude/skills/truman-perspective/`

| 文件 | 作用 |
|------|------|
| `SKILL.md` | 主文件，角色扮演规则 + Agentic Protocol + 心智模型 |
| `references/research/01-writings.md` | Agent 1: 著作与系统性思考调研 |
| `references/research/02-conversations.md` | Agent 2: 对话与即兴表达风格 |
| `references/research/03-expression-dna.md` | Agent 3: 表达DNA（10+原始样本） |
| `references/research/04-external-views.md` | Agent 4: 他者视角与外部评价 |
| `references/research/05-decisions.md` | Agent 5: 重大决策与言行一致性分析 |
| `references/research/06-timeline.md` | Agent 6: 人物时间线 2012-2026 |
| `scripts/` | 辅助脚本（字幕下载/转录/SRT转换/质量检查） |

## Open Questions

- Truman 本人对这个 Skill 的准确性会如何评价？他是否会认为"体系可以模拟，但操盘手感无法复制"？
- 人格模拟型 Skill 的"诚实边界"应该多宽？太宽失去实用价值，太窄有冒充风险
- 调研截止 2026-04-14，Truman 在 AI 转型（LABS）上的新观点如何纳入更新？
- 两个 Skill（business-research + truman-perspective）的组合使用模式是什么？是否可以设计"Truman 审阅调研报告"的自动化流程？

## Output Opportunities

- **Skill 组合**：business-research（调研）→ truman-perspective（审阅结论）的流水线
- **反向验证**：用 truman-perspective 对 business-research 的调研结论做 Pre-Mortem（事前验尸）
- **KDO 集成**：定义 Skill 类型枚举（methodology / persona / tool）作为 KDO Protocol 的 Skill 管理扩展
