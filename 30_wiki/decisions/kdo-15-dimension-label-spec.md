---


id: kdo-15-dimension-label-spec
title: KDO 标签体系：15 维度完整定义 v1.0
type: decision
status: draft
domain: master
tags:
- src_unknown
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-16'
target_roles:
- src_unknown
- src_unknown
- src_unknown
related:
  - [[huangyaoshi-tagging-and-scope-proposal]]
  - [[dk-modeling-ai-judgment-limit]]
  - [[labeling-final-consolidation]]
  - [[dk-modeling-ai-iterative-prompting]]
  - [[labeling-research-alignment]]
  - [[data-labeling-best-practices-report]]
  - [[huangyaoshi-tagging-and-scope-proposal]]
  - [[plan_20260531_data-curator-v1.3]]
author: unknown
source_context: KDO internal decision record （原 legacy，已从 title/context/filename 推断为
  src_20260606_6dad71f1）
source_refs:
  - src_20260606_6dad71f1-hx-smj-01_v1.0-pcba加工要求_15
reviewed_by: pending
confidence: 0.6
trust_level: low
---
# KDO 标签体系：15 维度完整定义 v1.0

## 设计原则

1. **从下游决策倒推** — 每个维度对应 AI 使用数据时需要做的一个具体决策
2. **MECE** — 维度和维度之间互斥穷尽。同维度的值之间正交
3. **层级激活** — 不是每个 chunk 都填满 15 维。有些维度只在特定 chunk_type 激活
4. **描述驱动** — 每个标签值配包含/排除描述，支撑将来 Embedding 语义匹配
5. **版本追踪** — 标签体系用语义版本号，chunk 记录标注时使用的版本

---

## 一、检索组（3 维 — 每条 chunk 必标）

AI 决策：这条数据是什么？在哪？跟什么方法论相关？

### 1. domain

| 属性 | 内容 |
|------|------|
| **标注层级** | 卡属性，继承给所有块 |
| **激活条件** | 必标 |
| **标注方式** | 人工（入库时填入） |

| 值 | 包含 | 排除 |
|----|------|------|
| `master` | 通用方法论、KDO 自身、跨域桥梁 | 具体行业内容 |
| `ai-saas` | AI 产品、LLM 应用、提示工程 | 通用软件开发 |
| `healthcare` | 医疗 IT、HIS、临床决策 | 通用健康科普 |
| `yitang` | 一堂课程体系、双三角模型、五步法 | 通用创业方法论 |
| `design` | AI 设计、视觉传达、品牌设计 | 通用 UI 开发 |

### 2. chunk_type

| 属性 | 内容 |
|------|------|
| **标注层级** | 块属性，每块独立 |
| **激活条件** | 必标 |
| **标注方式** | 自动（heading 映射 + 暗知识 6 字段映射） |

| 值 | 含义 | 包含 | 排除 |
|----|------|------|------|
| `claim` | 可证伪的知识主张 | "Step 1 的核心操作是分解判断" | 纯描述性叙述 |
| `constraint` | 边界条件/限制/前提 | "不适用于日常小决策""需要独立的团队" | 操作步骤 |
| `procedure` | 操作步骤/可执行指令 | "1.先发问题清单 2.每人独立填写" | 原则性建议 |
| `definition` | 术语定义/概念解释 | "偏差是系统性倾向，噪声是随机波动" | 案例、例子 |
| `example` | 具体案例/实例 | "场景：团队要决定是否投资新项目" | 抽象原则 |
| `reference` | 引用来源/外部链接 | "来源：Kahneman《噪声》" | 内部观点 |
| `critique` | 外部攻击者观点 | "Taleb：聚合消除了有益的多样性" | 作者自己的反对意见 |
| `synthesis` | 跨域洞察/综合结论 | "与五步法的逻辑结构一致" | 单域内总结 |
| `question` | 开放问题/待探索 | "什么场景下 Y 模型不适用？" | 反问句 |
| `action_trigger` | 使用/不使用触发条件 | "当团队对同一问题有分歧时用" | 通用建议 |
| `process_data` | 过程记录/决策理由 | "改之前是 A，改之后是 B，因为…" | 最终结论 |
| `error_data` | 错误/反例/纠偏 | "C-10：批量跑导致 71 张卡被清空" | 正向案例 |
| `original_quote` | 原始引用（暗知识卡） | 口述稿原文直接引用 | 改写后的内容 |
| `use_case` | 使用场景（暗知识卡） | "在准备跑 kdo enrich 之前" | 泛化描述 |
| `operation` | 操作方法（暗知识卡） | 步骤级操作流程 | 抽象原则 |
| `boundary` | 适用边界（暗知识卡） | 具体反例/前提条件 | 通用"有局限性" |
| `why_valuable` | 为什么值钱（暗知识卡） | "AI 语料中不存在"的理由 | 通用"很值钱" |
| `cross_reference` | 知识关联（暗知识卡） | 链接到概念卡 | 空链接 |
| `extraction_guide` | 萃取指南（一组卡的统领性方法论） | "月白 AI 设计方法论" | 单卡总结 |

### 3. method_family

| 属性 | 内容 |
|------|------|
| **标注层级** | 块属性，从卡片 method tag 继承 + 内容关键词补全 |
| **激活条件** | 必标 |
| **标注方式** | 自动（卡片继承 + 内容检测） |

| 值 | 包含 | 排除 |
|----|------|------|
| `thinking-tool` | 认知模型、思维框架、启发式方法 | 具体操作工具 |
| `decision-framework` | ROI 评估、ABCD 模型、五步法、决策矩阵 | 通用思维方法 |
| `learning-method` | IPO 模型、Y 模型、科学学习方法论 | 课程内容本身 |
| `research-method` | 调研方法、访谈技巧、数据分析 | 数据工程 |
| `product-design` | 泛产品设计、MVP、用户研究 | UI 视觉设计 |
| `management-tool` | 管理工具、团队协作、OKR | 执行层面的 checklist |
| `execution-method` | 执行框架、落地策略、节奏控制 | 战略层面的方向 |
| `evaluation-method` | 评估、对标、审核框架 | 纯流程审批 |
| `communication-method` | 表达、路演、叙事方法 | 日常对话技巧 |
| `prompt-engineering` | 提示词设计、AI 交互模式 | AI 底层技术 |
| `knowledge-engineering` | 知识管理、本体设计、KDO 自身方法论 | 通用信息管理 |

---

## 二、视角组（5 维 — 有信号时激活）

AI 决策：对谁说？从什么角度说？在什么平台上说？谁说的？什么场景下说的？

### 4. audience

| 属性 | 内容 |
|------|------|
| **标注层级** | 块属性 |
| **激活条件** | 内容明确提到或隐含特定受众时 |
| **标注方式** | 自动（关键词推断）+ 人工抽检 |

| 值 | 关键信号词 | 包含 | 排除 |
|----|-----------|------|------|
| `ceo` | CEO、老板、一号位、创始人、战略 | 顶层决策者视角的表述 | 执行细节 |
| `manager` | 管理者、团队负责人、总监、主管 | 中层管理视角 | 一线操作 |
| `executor` | 执行、操作、落地、干活、一线 | 执行者视角的步骤和工具 | 战略思考 |
| `designer` | 设计师、视觉、构图、审美 | 设计从业者视角 | 非设计领域的视觉描述 |
| `developer` | 开发者、工程师、代码、API | 技术实现视角 | 非技术架构 |
| `beginner` | 入门、新手、零基础、第一次 | 无前置知识的新人视角 | — |
| `expert` | 进阶、高级、深度、专家 | 已有领域知识的专家视角 | — |
| `general` | [默认] 无特定受众 | 面向所有受众的通用表述 | — |

### 5. perspective

| 属性 | 内容 |
|------|------|
| **标注层级** | 块属性 |
| **激活条件** | 内容从特定专业角度或合规角度切入时 |
| **标注方式** | 自动（视角信号词检测） |

| 值 | 关键信号词 | 包含 | 排除 |
|----|-----------|------|------|
| `professional` | 专业术语、领域黑话、技术细节 | 需要领域知识才能理解的表述 | — |
| `compliance` | 合规、法律、隐私、版权、监管、红线 | 法规/合规角度的约束和警告 | — |
| `platform-policy` | 平台规则、违禁词、限流、封号、审核 | 平台层面的运营规则 | — |
| `roi` | ROI、成本、收益、投入产出、值不值 | 投资回报角度的分析 | — |
| `user-experience` | 用户体验、好用、感受、NPS、满意度 | 终端用户视角 | — |
| `general` | [默认] | 无特定视角 | — |

### 6. platform

| 属性 | 内容 |
|------|------|
| **标注层级** | 块属性 |
| **激活条件** | 内容提到具体平台或平台相关规则时 |
| **标注方式** | 自动（平台名检测） |

| 值 | 包含 |
|----|------|
| `xiaohongshu` | 小红书的内容规则、违禁词、封面尺寸 |
| `douyin` | 抖音的短视频规则、算法特征 |
| `wechat` | 微信公众号/视频号的规格、规则 |
| `feishu` | 飞书文档/多维表格的协作特性 |
| `obsidian` | Obsidian 的 Markdown 生态和插件体系 |
| `general` | [默认] 平台无关 |

### 7. source_person

| 属性 | 内容 |
|------|------|
| **标注层级** | 卡属性，继承给所有块 |
| **激活条件** | 暗知识卡必标；概念卡如有明确来源者则标 |
| **标注方式** | 人工（入库时填入） |

| 值 | 包含 |
|----|------|
| `月白` | 月白的口述、分享、课程内容 |
| `Truman` | Truman（一堂创始人）的口述、课程、即兴判断 |
| `欧阳锋` | 欧阳锋的审查意见、架构决策 |
| `黄药师` | 黄药师的技术决策、踩坑记录 |
| `老顽童` | 老顽童的内容生产记录、卡片 |
| `洪七公` | 洪七公的多模态产出、视觉分析 |
| `段王爷` | 段王爷的发布记录、渠道反馈 |
| `花总` | 花总的专家判断 |
| `用户` | 用户的战略决策、方向性判断、领域洞察 |
| `大眉毛` | 大眉毛的数据工程实践 |
| `徐建` | 徐建的创业/数据资产案例 |
| `multiple` | 多个来源者共同贡献 |

### 8. source_context_type

| 属性 | 内容 |
|------|------|
| **标注层级** | 卡属性，继承给所有块 |
| **激活条件** | 暗知识卡必标 |
| **标注方式** | 人工（入库时填入） |

| 值 | 含义 | 包含 |
|----|------|------|
| `oral-transcript` | 口述稿转录 | 线上/线下分享的逐字稿 |
| `live-session` | 实时对话 | 审查对话、答疑、讨论记录 |
| `written-document` | 书面文档 | 文章、方案、SOP、课程教案 |
| `code-commit` | 代码提交 | Git commit、PR 讨论 |
| `review-comment` | 审查意见 | 欧阳锋的审查记录 |
| `correction-record` | 纠偏记录 | corrections.md、pitfalls.md |
| `casual-chat` | 闲聊 | 非正式对话中的即兴判断 |
| `structured-data` | 结构化数据 | 表格、JSON、YAML 配置 |
| `experiment-log` | 实验记录 | A/B 测试、pilot、试错 |

---

## 三、质量组（4 维 — AI 校准和治理依赖）

AI 决策：这条数据能信吗？置信度多高？谁生成的？会不会过期？踩了什么坑？

### 9. confidence

| 属性 | 内容 |
|------|------|
| **标注层级** | 块属性（同卡内不同块置信度可能不同） |
| **激活条件** | 有明确证据支持程度的块 |
| **标注方式** | 从卡属性继承 + 块类型推断 |

| 值 | 判定标准 | 示例 |
|:--:|---------|------|
| `0.90` | 多源验证 + 实践经验 + 同行共识 | Kahneman 的噪声理论 |
| `0.70` | 单源强证据 + 逻辑自洽 | 月白的口喷设计范式（个人经验但逻辑清晰） |
| `0.50` | 单源 + 部分反例存在 | Truman 的某条即兴判断 |
| `0.30` | 假说/推测/个人偏好 | "我觉得未来 AI 会…" |
| `null` | 无法判断 | 纯事实陈述（"豆包支持画圈功能"） |

### 10. data_generation

| 属性 | 内容 |
|------|------|
| **标注层级** | 卡属性，继承给所有块 |
| **激活条件** | 必标 |
| **标注方式** | 人工（入库时填入） |

| 值 | 判定标准 |
|----|---------|
| `original` | 人类原生的内容（口述、手写、实拍） |
| `ai_generated` | AI 单次生成的内容 |
| `ai_on_ai` | AI 生成 → AI 再加工（叠加代际，高幻觉风险） |
| `human_ai_collab` | 人机协作（AI 生成 + 人修改） |
| `human_edited_ai` | AI 生成 → 人审核修改后定稿 |

### 11. error_root

| 属性 | 内容 |
|------|------|
| **标注层级** | 块属性 |
| **激活条件** | 仅 `chunk_type = error_data` 时激活 |
| **标注方式** | 自动（根因关键词检测） |

| 值 | 关键信号词 | 包含 |
|----|-----------|------|
| `skip-validation` | 跳过、没做、没检查、以为、直接 | 跳过了某个必要验证步骤 |
| `format-over-content` | 格式、门禁、通过、PASS | 格式检查通过但内容有问题 |
| `silent-failure` | 静默、无报错、0 pages、假成功 | 失败但无错误信号 |
| `compatibility-break` | 不兼容、旧格式、新格式、迁移 | 新旧格式/版本不兼容 |
| `naming-conflict` | 重名、共用、混用、冲突 | 命名/字段/ID 冲突 |
| `context-overflow` | 上下文、token、超载、太长 | 内容超过处理容量 |
| `human-error` | 误判、以为、忘了、漏了 | 人的判断错误或疏忽 |
| `automation-blindness` | 脚本、批量、自动、一跑 | 信任自动化工具未经人工验证 |
| `governance-gap` | 治理、护栏、防线、底线 | 缺少系统性的防护机制 |

### 12. expiry

| 属性 | 内容 |
|------|------|
| **标注层级** | 卡属性/块属性（按数据性质） |
| **激活条件** | 内容具有时效性时 |
| **标注方式** | 人工（入库时评估）+ 自动（CJK 日期检测） |

| 值 | 含义 | 示例 |
|----|------|------|
| `stable` | 长期稳定，不会因时间失效 | 认知偏误清单、决策卫生五步法 |
| `current` | 当前有效，2-3 年内可能需审查 | 2026 年的 AI 工具推荐 |
| `volatile` | 快速变化，1 年内可能过期 | 某平台的违禁词列表、当前模型价格 |
| `evergreen` | 永不过期的基础原理 | 第一性原理、MECE 原则 |
| `dated:<YYYY-MM-DD>` | 明确过期日期 | `dated:2027-01-01` |

---

## 四、价值组（3 维 — 宏观路由和优先级）

AI 决策：这条数据多重要？使用什么方式？需要什么前置知识？

### 13. value_tier

| 属性 | 内容 |
|------|------|
| **标注层级** | 卡属性，继承给所有块 |
| **激活条件** | 必标 |
| **标注方式** | 人工（入库时预判） |

| 值 | 含义 | AI 使用场景 | 卡数占比预期 |
|----|------|-----------|:--:|
| `micro` | 教材级：单次对话的上下文参考 | 单卡 query → AI 回答 | 70% |
| `meso` | 燃料级：业务工作流的稳定数据供给 | 域内多卡 → AI 完成复杂任务 | 20% |
| `macro` | 护城河级：行业独占的稀缺资产 | 全库 → 竞争壁垒 | 10% |

### 14. usage_depth

| 属性 | 内容 |
|------|------|
| **标注层级** | 卡属性 |
| **激活条件** | 必标 |
| **标注方式** | 自动（基于 value_tier + usage 频率）+ 人工调整 |

| 值 | 含义 | 适用条件 |
|----|------|---------|
| `feed` | 单次投喂：被 query 检索到即可 | 所有卡片最低等级 |
| `packaged` | 封装为 Data Pack / system prompt | 高频使用 + value_tier ≥ meso 的卡 |
| `retrieval` | RAG 知识库检索 | 已在 Graph RAG 索引中 |
| `configured` | Workflow / Agent 节点配置 | 极高频 + 稳定使用 + 决策链路上的卡 |
| `trained` | 纳入训练/微调 | 暂不启用 |

### 15. prerequisite_knowledge

| 属性 | 内容 |
|------|------|
| **标注层级** | 卡属性 |
| **激活条件** | 有前置知识依赖时 |
| **标注方式** | 人工（入库时填入） |

| 值 | 含义 |
|----|------|
| `none` | 无前置知识要求，零基础可读 |
| `basic-domain` | 需要基本的领域认知（如"知道什么是 RAG"） |
| `intermediate-method` | 需要先掌握某个方法论（如"理解五步法"） |
| `advanced-specialist` | 需要领域专家级别的知识 |
| `card:<id>` | 需要先读特定卡片（如"需要先读 master-cognitive-bias-checklist"） |

---

## 五、维度汇总

### 标注矩阵

| # | 维度 | 组 | 层级 | 激活条件 | 标注方式 | 值数量 |
|:--:|------|:--:|:--:|---------|---------|:--:|
| 1 | domain | 检索 | 卡 | 必标 | 人工 | 5 |
| 2 | chunk_type | 检索 | 块 | 必标 | 自动 | 19 |
| 3 | method_family | 检索 | 块 | 必标 | 自动 | 11 |
| 4 | audience | 视角 | 块 | 有信号 | 自动 | 8 |
| 5 | perspective | 视角 | 块 | 有信号 | 自动 | 6 |
| 6 | platform | 视角 | 块 | 有信号 | 自动 | 6 |
| 7 | source_person | 视角 | 卡 | 暗知识卡必标 | 人工 | 12 |
| 8 | source_context_type | 视角 | 卡 | 暗知识卡必标 | 人工 | 9 |
| 9 | confidence | 质量 | 块 | 有证据 | 自动+人工 | 4+null |
| 10 | data_generation | 质量 | 卡 | 必标 | 人工 | 5 |
| 11 | error_root | 质量 | 块 | error_data 时 | 自动 | 9 |
| 12 | expiry | 质量 | 卡/块 | 有时效性 | 人工+自动 | 5 |
| 13 | value_tier | 价值 | 卡 | 必标 | 人工 | 3 |
| 14 | usage_depth | 价值 | 卡 | 必标 | 自动+人工 | 5 |
| 15 | prerequisite_knowledge | 价值 | 卡 | 有前置 | 人工 | 4+ |

### 每个 chunk 实际标签数（按场景）

| 场景 | 激活维数 | 标签值数 | 说明 |
|------|:--:|:--:|------|
| 普通概念卡的 claim 块 | 3（检索组） | ~5 | domain + chunk_type + method_family |
| 含受众信号的概念卡块 | 4-5 | ~7 | + audience, perspective |
| 暗知识卡的 error_data 块 | 6-8 | ~10 | + source_person, source_context_type, error_root, confidence |
| 平台相关内容块 | 4-5 | ~7 | + platform + perspective(platform-policy) |

**实际每块标签数：5-10 个。** 在行业建议的 3-8 个范围内（AI Journal: 3-5, CSDN: 5-8）的上限。

---

## 六、标签值总数统计

| 维度 | 值数量 |
|------|:--:|
| domain | 5 |
| chunk_type | 19 |
| method_family | 11 |
| audience | 8 |
| perspective | 6 |
| platform | 6 |
| source_person | 12 |
| source_context_type | 9 |
| confidence | 4 |
| data_generation | 5 |
| error_root | 9 |
| expiry | 5 |
| value_tier | 3 |
| usage_depth | 5 |
| prerequisite_knowledge | 4 |
| **合计** | **111** |

**110 个标签值**，分布在 15 个维度中。比朋友的 100+ 略多，但因为维度分层激活（不是每个 chunk 都填 110 个），实际每块只标 5-10 个。

---

## 七、版本信息

- src_unknown
- src_unknown
- src_unknown
  - src_unknown
  - src_unknown
  - src_unknown

---

## 八、待讨论

| # | 问题 | 需要谁决策 |
|:--:|------|:--:|
| 1 | 110 个标签值是否太多？需要砍掉哪些维度或合并哪些值？ | 用户 + 欧阳锋 |
| 2 | `source_person` 和 `source_context_type` 只对暗知识卡生效——概念卡是否需要？ | 欧阳锋 |
| 3 | `expiry` 字段放在卡属性还是块属性？同卡内不同块可能时效性不同 | 黄药师 |
| 4 | `platform` 维度：KDO 实际涉足的平台有哪些？列表是否需要调整？ | 用户 |
| 5 | `error_root` 的 9 个值是否覆盖了已知失败模式的全部根因类型？ | 黄药师（对照 failure-modes.md 校对） |

---

*黄药师 · 2026-05-31*
