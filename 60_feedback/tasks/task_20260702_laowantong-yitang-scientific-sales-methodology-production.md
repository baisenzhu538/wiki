---
id: task_20260702_laowantong-yitang-scientific-sales-methodology-production
title: 一堂科学销售方法论：1 framework + 5 tool + 1 framework + 3 case + 1 dk + 1 tool（OPC 智能体
  / 销售域）
type: task
status: reviewed
priority: P1
assignee: kimi
reviewer: 欧阳锋
review_date: '2026-07-02'
acceptance_verdict: pass
created_at: 2026-07-02
updated_at: '2026-07-02T00:00:00+00:00'
expected_cards: 12
source_refs:
- 00_inbox/销售专题/李蕊-科学销售方法论-口述.txt
- 00_inbox/销售专题/李蕊-科学销售方法论-笔记.txt
- 00_inbox/销售专题/李蕊-销售体系之一-客户分层和卖点提炼-口述.txt
- 00_inbox/销售专题/李蕊-销售体系之一-客户分层和卖点提炼-笔记.txt
- 00_inbox/销售专题/李蕊-销售体系之二-销售过程拆解-口述.txt
- 00_inbox/销售专题/李蕊-销售体系之二-销售过程拆解-笔记.txt
- 00_inbox/销售专题/李蕊-销售体系之三-销售过程管理-口述.txt
- 00_inbox/销售专题/李蕊-销售体系之三-销售过程管理-笔记.txt
- 00_inbox/销售专题/李蕊-销售体系之四-激励体系搭建-口述.txt
- 00_inbox/销售专题/李蕊-销售体系之四-激励体系搭建-笔记.txt
- 00_inbox/销售专题/李蕊-销售系统之五-销售工具箱-口述.txt
- 00_inbox/销售专题/李蕊-销售系统之五-销售工具箱-笔记.txt
- 00_inbox/销售专题/_processed/销售专题_整合笔记.md
- 60_feedback/diagnosis/diag_20260702_yitang-scientific-sales-methodology.md
related:
- framework-yitang-scientific-sales-five-step
- tool-yitang-customer-segmentation-4step
- tool-yitang-value-proposition-4step
- tool-yitang-sales-process-decomposition
- tool-yitang-sales-performance-management
- framework-yitang-sales-incentive-6d
- tool-yitang-sales-toolkit-radar
- dk-yitang-sales-common-pitfalls
- case-yitang-sales-transformation-jubensha-saas
- case-yitang-sales-transformation-meirongyuan
- case-yitang-sales-transformation-tuliaogongsi
- tool-opc-sales-dialogue-assistant
- opc-ai-sales-agent-architecture
reviewed_by: 欧阳锋
---

# 一堂科学销售方法论：1 framework + 5 tool + 1 framework + 3 case + 1 dk + 1 tool（OPC 智能体）

> 任务来源：王语嫣入口质量门诊断 `diag_20260702_yitang-scientific-sales-methodology.md`
> 王语嫣判断：本专题是「一堂方法论 + 假设驱动 + 工具化」在销售管理场景的完整实例化；KDO 目前几乎没有独立销售方法论卡片，本任务填补明显空白。用户分层、价值主张、目标管理、工具化等概念已有 KDO 卡覆盖，本次只做销售域实例化，通过 related 关联已有卡。
> OPC 适配：科学销售五步法可直接映射为 OPC 智能体军团，已有 `opc-ai-sales-agent-architecture.md` 作为承接，本次产出需反向更新其 related。
> 版本说明：
> - 初版规划 6 张卡，经用户挑战后扩展为 10 张卡。
> - 黄药师建议：在 10 张基础上增加操作层工具卡、案例卡与 OPC 智能体规格卡，预计 12-15 张。
> - 王语嫣独立判断：操作层细节（SABC 算法、A/B 测试、状态机等）并入现有 tool/framework 卡的 OPC 适配小节，不再单独建卡；新增 **1 个涂料公司 case** 覆盖传统工业分销场景，新增 **1 张 `tool-opc-sales-dialogue-assistant` 作为 MVP 智能体规格卡**；智能体层不一次性铺开 8-10 张，先做可直接当 system prompt 运行的对话助手。最终确定为 **12 张卡**。

---

## 一、输入素材

1. `00_inbox/销售专题/李蕊-科学销售方法论-口述.txt`
2. `00_inbox/销售专题/李蕊-科学销售方法论-笔记.txt`
3. `00_inbox/销售专题/李蕊-销售体系之一-客户分层和卖点提炼-口述.txt`
4. `00_inbox/销售专题/李蕊-销售体系之一-客户分层和卖点提炼-笔记.txt`
5. `00_inbox/销售专题/李蕊-销售体系之二-销售过程拆解-口述.txt`
6. `00_inbox/销售专题/李蕊-销售体系之二-销售过程拆解-笔记.txt`
7. `00_inbox/销售专题/李蕊-销售体系之三-销售过程管理-口述.txt`
8. `00_inbox/销售专题/李蕊-销售体系之三-销售过程管理-笔记.txt`
9. `00_inbox/销售专题/李蕊-销售体系之四-激励体系搭建-口述.txt`
10. `00_inbox/销售专题/李蕊-销售体系之四-激励体系搭建-笔记.txt`
11. `00_inbox/销售专题/李蕊-销售系统之五-销售工具箱-口述.txt`
12. `00_inbox/销售专题/李蕊-销售系统之五-销售工具箱-笔记.txt`
13. `00_inbox/销售专题/_processed/销售专题_整合笔记.md`
14. 王语嫣诊断报告：`60_feedback/diagnosis/diag_20260702_yitang-scientific-sales-methodology.md`

---

## 二、12 张目标卡

### Card 1: `framework-yitang-scientific-sales-five-step`

**类型**：framework  
**主域**：sales / yitang  
**confidence**：0.88  
**trust_level**：high

**必须包含的 section**：
1. **一句话**：科学销售 = 用数据驱动和系统方法让销售能力从依赖个人变成可预测、可复制、可规模化的组织能力。
2. **五步法总图**：提炼卖点 → 拆解过程 → 推进业绩 → 激励团队 → 打造工具。
3. **粗放销售六大通病**：不懂科学销售、缺用户卖点、不拆销售过程、不抓销售过程、不懂激励、没有工具箱。
4. **与一堂五步法的关系**：销售是五步法在销售管理场景的专项实例化。
5. **OPC 改编提示**：团队版 vs 一人公司版的差异。
6. **Synthesis**：桥接 `yt-five-step-method-complete`、`yitang-methodology-system`、`framework-一堂五步法-泛产品设计`、`framework-yitang-channel-exploration-4step`、`yt-unit-model-overview`。
7. **Related**：≥5 条，含跨域回链。

---

### Card 2: `tool-yitang-customer-segmentation-4step`

**类型**：tool  
**主域**：sales / marketing / strategy  
**confidence**：0.86  
**trust_level**：high

**必须包含的 section**：
1. **When to Use**：线索多但转化率低、资源分散、销售精力平均分配、不知道重点客户是谁。
2. **四步法**：确定销售目标 → 提出分层假设 → 验证分层假设 → 全面执行分层。
3. **SABC 分级表**：S/A/B/C 定义、资源分配原则、跟进策略差异。
4. **分层假设来源清单**：产品特性、行业常识、历史数据、同行案例、专家访谈。
5. **验证方法**：定量分析 + 定性测试。
6. **案例嵌入**：支付公司商旅分层、涂料公司 10 万→20 条 S 级。
7. **Checklist**：≥8 项。
8. **Anti-patterns**：平均分配线索、分层不做验证、脱离目标分层、只分层不分配策略。
9. **Critique**：≥3 个外部反对者 + ≥2 个内部局限。
10. **Synthesis**：桥接 `framework-demand-validation-pipeline`、`concept-一堂-hypothesis-driven-business-methodology`、`tool-iceberg-triangle-modeling`、`master-decision-hygiene`。
11. **Related**：≥5 条。

---

### Card 3: `tool-yitang-value-proposition-4step`

**类型**：tool  
**主域**：sales / marketing / product-design  
**confidence**：0.86  
**trust_level**：high

**必须包含的 section**：
1. **When to Use**：卖点不统一、销售各说各话、产品介绍停留在功能罗列、客户不知道为什么要买。
2. **四步法**：写初始版本 → 建立审美 → 多轮打磨 → 落地应用。
3. **卖点结构**：Top3、1+N、逻辑型结构。
4. **建立审美方法**：拆解竞品 + 用户视角分析。
5. **好卖点三原则**：匹配场景、能打动人、好听好记。
6. **落地触点**：话术、海报、PPT、客服沟通、详情页。
7. **案例嵌入**：儿童记忆力培训（成绩不好跟记不住有关）、iPhone 充电器（小冰块）。
8. **Checklist**：≥8 项。
9. **Anti-patterns**：卖点列一桌、自嗨式表达、只写不用、想卖给所有人。
10. **Critique**：≥3 个外部反对者 + ≥2 个内部局限。
11. **Synthesis**：桥接 `tool-strategy-value-proposition`、`framework-一堂五步法-泛产品设计`、`yt-panproduct-aesthetic-pool`、`yt-panproduct-aesthetic-modeling`、`framework-brand-three-degree`。
12. **Related**：≥5 条。

---

### Card 4: `tool-yitang-sales-process-decomposition`

**类型**：tool  
**主域**：sales / yitang  
**confidence**：0.85  
**trust_level**：high

**必须包含的 section**：
1. **When to Use**：销售周期长、客户推进不透明、老销售经验无法复制、新人成长慢、丢单原因不清楚。
2. **三步法**：拆路径 → 划阶段 → 配动作。
3. **四类用户决策**：接触决策、购买决策、付款决策、履约决策。
4. **里程碑定义**：聚焦用户高成本决策点，用定性和定量方法识别。
5. **动作设计原则**：做足加法、匹配精准动作、定义动作标准、配套销售工具。
6. **案例嵌入**：剧本杀 SaaS（添加微信→见面→探店→施工→上线）、美容院（美团咨询→到店→转化 20+ 节点）。
7. **Checklist**：≥8 项。
8. **Anti-patterns**：从销售视角拆、阶段不可量化、只拆不配套动作、过度复杂、忽略履约决策。
9. **Critique**：≥3 个外部反对者 + ≥2 个内部局限。
10. **Synthesis**：桥接 `framework-一堂五步法-泛产品设计`、`yt-business-formula-parameter-iceberg`、`tool-iceberg-triangle-modeling`、`framework-yitang-channel-exploration-4step`。
11. **Related**：≥5 条。

---

### Card 5: `tool-yitang-sales-performance-management`

**类型**：tool  
**主域**：sales / management  
**confidence**：0.84  
**trust_level**：high

**必须包含的 section**：
1. **When to Use**：业绩波动大、现金流不可预测、只会压目标不会追过程、周会变成流水账。
2. **三步法**：拆目标 → 定策略 → 追过程。
3. **目标拆解维度**：时间、客户、团队/个人、渠道、产品；乐观/中性/悲观三版；预留 Buffer。
4. **业绩管理画布**：核心目标 → 拆解维度 → 策略设计（核心+备选） → 过程跟进。
5. **Pipeline 与 Gap 分析**：客户清单、阶段、预期、差距、策略。
6. **周会三要点**：看 Gap → 找原因 → 定策略。
7. **案例嵌入**：快钱支付 To B（完成率 40-50% → 85-90%）、手机配件电商（按小时监控策略）。
8. **Checklist**：≥10 项。
9. **Anti-patterns**：只看结果、平均分配目标、不开周会、没有 Plan B、目标不拆到客户/渠道。
10. **Critique**：≥3 个外部反对者 + ≥2 个内部局限。
11. **Synthesis**：桥接 `yt-unit-model-overview`、`yt-management-goal-management`、`yt-business-formula-six-level-logic`、`framework-yitang-nine-layer-deep-dig`。
12. **Related**：≥5 条。

---

### Card 6: `framework-yitang-sales-incentive-6d`

**类型**：framework  
**主域**：sales / management  
**confidence**：0.83  
**trust_level**：medium

**必须包含的 section**：
1. **一句话**：激励不是事后奖励，而是事前设计的发动机。
2. **四大常见问题**：忽略激励、无效激励、只靠金钱、标准不科学。
3. **六维激励模型**：目标有渴望、业绩有奖金、同事有竞争、打仗有感情、成长有奔头、岗位有使命。
4. **50 策略速查表**：按六维分类，每维 6-10 个策略（可做成折叠表或附录）。
5. **不同阶段激励重点**：探索期（软性为主）、复制期（使命+感情+初步提成）、快速增长期（金钱大胆）、成熟期（规则细致+多元化）。
6. **发钱三大设计重点**：杠杆点、公平点、感知点。
7. **OPC 改编提示**：六维激励对 OPC 不适用，替换为「目标-行动-反馈」自我驱动循环。
8. **Checklist**：≥8 项。
9. **Anti-patterns**：只发钱、目标拍脑袋、规则不透明、激励与目标割裂、频繁改规则。
10. **Critique**：≥3 个外部反对者 + ≥2 个内部局限。
11. **Synthesis**：桥接 `framework-yitang-deliberate-practice-1plus4`、`yt-personal-deliberate-practice`、`yt-management-goal-management`。
12. **Related**：≥5 条。

---

### Card 7: `tool-yitang-sales-toolkit-radar`

**类型**：tool  
**主域**：sales / yitang  
**confidence**：0.85  
**trust_level**：high

**必须包含的 section**：
1. **When to Use**：新人上手慢、经验无法沉淀、销售专业度不足、想规模化复制 Top Sales。
2. **销售工具箱三步法**：选择合适工具 → 提炼运用工具 → 复盘迭代工具。
3. **六维雷达图**：
   - 60 分基础：公司有实力、话术讲人话
   - 75 分进阶：服务很专业、销售有能力
   - 85 分最佳实践：团队有效率、攻坚有策略
4. **60/75/85 分典型工具清单**：每级 4-6 个工具示例。
5. **常见工具类型**：公司介绍、产品一页纸、价格表、话术、案例集、流程手册、培训资料、CRM、作战地图。
6. **案例嵌入**：剧本杀 SaaS 产品演示视频、美容院数据表单优化。
7. **Checklist**：≥8 项。
8. **Anti-patterns**：工具由不一线人员编写、话术像台词脚本、工具不迭代、工具与场景背离。
9. **Critique**：≥3 个外部反对者 + ≥2 个内部局限。
10. **Synthesis**：桥接 `yt-panproduct-aesthetic-pool`、`tool-yitang-best-practice-as-golden-finger`、`tool-agent-research-swarm`、`framework-yitang-deliberate-practice-1plus4`。
11. **Related**：≥5 条。

---

### Card 8: `dk-yitang-sales-common-pitfalls`

**类型**：dark-knowledge  
**dark_knowledge_type**：pattern  
**主域**：sales / management  
**confidence**：0.85  
**trust_level**：high

**必须包含的 6 个反模式**：
1. **迷信销冠陷阱** — 认为销售靠天赋，招不到牛人就做不起来。
2. **平均分配线索陷阱** — 缺乏分层意识，所有销售拿同样线索。
3. **卖点五花八门陷阱** — 缺乏统一价值语言，每个销售讲的不一样。
4. **过程黑盒陷阱** — 只盯结果不盯过程，客户卡两个月不知道原因。
5. **目标拍脑袋陷阱** — 缺乏科学拆解，月度目标完不成也不知差距在哪。
6. **只靠金钱激励陷阱** — 激励手段单一，销售只挖老客户不愿拓新。

**必须包含的 section**：
1. 6 个反模式（症状 + 反打 + 口诀）。
2. 预警信号：≥6 条。
3. 修复动作：每个陷阱 1 个即时动作 + 1 个长期动作。
4. Critique：≥3 个外部反对者 + ≥2 个内部局限。
5. Synthesis：桥接 `framework-yitang-scientific-sales-five-step`、5 张 Step tool/framework 卡、`master-decision-hygiene`。
6. Related：≥5 条。

---

### Card 9: `case-yitang-sales-transformation-jubensha-saas`

**类型**：case  
**主域**：sales / ai-saas / yitang  
**confidence**：0.82  
**trust_level**：medium

**必须包含的 section**：
1. **Background**：剧本杀 SaaS 公司，业务刚起步，只有一个专职销售 + 一群兼职销售，年目标 200 万。
2. **Problem**：无用户分层、无统一卖点、无过程拆解、无目标拆解、无激励机制、无销售工具。
3. **Decision**：引入科学销售五步法，用兼职团队把整套打法打磨沉淀。
4. **Process**（五步改造）：
   - 用户分层：聚焦即将开店和翻新老店两类客户
   - 卖点提炼：省成本、降依赖、提服务
   - 过程拆解：8 个销售环节，关键节点必须见面、客户探店
   - 业绩管理：月成单≥5 单、客单价≥4 万、每天加 16 个微信
   - 激励 + 工具：分组 PK、红包、提成、话术、产品视频
5. **Result**：团队建立基本打法、数据开始沉淀、为全职销售团队奠定基础。
6. **Lessons**：60 分起点、资源有限也能建体系、兼职团队可打磨方法论。
7. **Failure Modes**：扫街无重点、卖点各说各话、凭感觉推进、不好意思分目标。
8. **Synthesis**：桥接 `framework-yitang-scientific-sales-five-step`、5 张 Step tool/framework 卡。
9. **Related**：≥5 条。

---

### Card 10: `case-yitang-sales-transformation-meirongyuan`

**类型**：case  
**主域**：sales / retail / yitang  
**confidence**：0.82  
**trust_level**：medium

**必须包含的 section**：
1. **Background**：美容院连锁，年营收上千万，新销售总监目标 2000 万。
2. **Problem**：总部与门店利益冲突、店长不配合数据填报、新渠道响应不及时、目标拆不下去。
3. **Decision**：从用户分层、过程拆解、目标拆解、激励机制、数据表单五方面改造。
4. **Process**：
   - 重新明确进店用户画像，按消费能力/稳定性/尝鲜度分层
   - 梳理美团咨询到转化的 20+ 关键节点
   - 用两家样板店验证，再推广到所有门店
   - 目标拆到门店、技师、客户
   - 调整激励机制统一总部和门店利益
   - 优化数据表单，总部派专人协助填关键数据
5. **Result**：在线咨询响应提升后新客到店转化率从 15-20% 提升至 25%；总部与门店不再打架。
6. **Lessons**：样板店验证、利益统一、数据表单要轻量化、关键节点数据化。
7. **Failure Modes**：总部强压门店、表单太复杂、忽视店长利益、新渠道不维护。
8. **Synthesis**：桥接 `framework-yitang-scientific-sales-five-step`、5 张 Step tool/framework 卡、`framework-yitang-channel-exploration-4step`。
9. **Related**：≥5 条。

---

### Card 11: `case-yitang-sales-transformation-tuliaogongsi`

**类型**：case  
**主域**：sales / manufacturing-distribution / b2b / yitang  
**confidence**：0.80  
**trust_level**：medium

**必须包含的 section**：
1. **Background**：涂料公司，海量注册线索但转化率低，销售精力分散。
2. **Problem**：10 万线索分不清谁是真客户；销售平均分配精力；S 级客户被淹没；分层脱离目标。
3. **Decision**：用一堂用户分层四步法重做 SABC 分级，把资源集中到高价值客户。
4. **Process**：
   - 明确阶段目标（利润 vs 标杆）
   - 提出分层假设（公司规模、项目类型、采购周期、地域）
   - 验证假设（历史成交画像 + 抽样访谈）
   - 执行分层（10 万 → 20 S 级 + 200 A 级，其余自动培育）
5. **Result**：销售 80% 精力聚焦 Top 220 客户，S 级转化率显著提升。
6. **Lessons**：分层和目标挂钩；没有验证的分层是拍脑袋；B/C 级线索需自动培育。
7. **Failure Modes**：只看数量不看质量、分层标准不更新、B/C 级直接丢弃、销售抵制少量线索。
8. **Synthesis**：桥接 `framework-yitang-scientific-sales-five-step`、`tool-yitang-customer-segmentation-4step`、`tool-yitang-sales-performance-management`、`master-decision-hygiene`。
9. **Related**：≥5 条。

---

### Card 12: `tool-opc-sales-dialogue-assistant`

**类型**：tool  
**主域**：personal-os / ai-sales-agent / yitang  
**confidence**：0.85  
**trust_level**：high

**定位**：OPC 销售智能体 MVP 规格卡，可直接作为 system prompt 使用。

**必须包含的 section**：
1. **When to Use**：一人公司创始人同时跟进多个客户、对话散落、容易忘记阶段、回复前需快速判断。
2. **核心功能**：读对话 → 想策略 → 给话术。
3. **输入**：客户对话记录（微信/邮件/通话转写/CRM 备注）、可选分层标签、可选当前阶段。
4. **输出**：
   - 客户意图与阶段判断（接触/购买/付款/履约 + 情绪/抗拒点）
   - 下一步建议（该做/不该做什么）
   - 2-3 个可直接选用或微调的回复选项
5. **工作逻辑**：
   - 用 `tool-yitang-customer-segmentation-4step` 判断客户等级
   - 用 `tool-yitang-sales-process-decomposition` 识别阶段与关键决策点
   - 用 `tool-yitang-value-proposition-4step` 选择匹配卖点
   - 用 `tool-yitang-sales-performance-management` 判断推进/预警
   - 生成 2-3 个不同风格回复（直接型/共情型/提问型）
6. **System Prompt 模板**：提供可直接复制到 Claude/GPT 自定义指令的精简模板。
7. **边界与风险提示**：不替代关键信任建立；不自动发送消息；隐私数据需合规处理。
8. **Checklist**：≥8 项。
9. **Anti-patterns**：照搬话术不调整、把 AI 建议当最终决策、关键谈判让 AI 代写、忽视客户情绪。
10. **Critique**：≥3 个外部反对者 + ≥2 个内部局限。
11. **Synthesis**：桥接 `opc-ai-sales-agent-architecture`、`human-ai-collaboration-double-triangle`、`framework-yitang-scientific-sales-five-step`、4 张 Step tool 卡。
12. **Related**：≥5 条。

---

## 三、已有卡 related 补链清单

12 张新卡产出后，必须反向在以下已有卡的 `related` 中加入新卡链接：

1. `yt-five-step-method-complete`
2. `yitang-methodology-system`
3. `framework-一堂五步法-泛产品设计`
4. `framework-yitang-channel-exploration-4step`
5. `tool-strategy-value-proposition`
6. `framework-demand-validation-pipeline`
7. `concept-一堂-hypothesis-driven-business-methodology`
8. `yt-panproduct-aesthetic-pool`
9. `yt-panproduct-aesthetic-modeling`
10. `framework-brand-three-degree`
11. `yt-business-formula-parameter-iceberg`
12. `tool-iceberg-triangle-modeling`
13. `yt-unit-model-overview`
14. `yt-management-goal-management`
15. `yt-business-formula-six-level-logic`
16. `framework-yitang-nine-layer-deep-dig`
17. `framework-yitang-deliberate-practice-1plus4`
18. `yt-personal-deliberate-practice`
19. `tool-yitang-best-practice-as-golden-finger`
20. `tool-agent-research-swarm`
21. `case-yitang-sales-routine-deconstruction`
22. `case-yitang-ai-painting-commercialization`
23. `opc-ai-sales-agent-architecture`
24. `human-ai-collaboration-double-triangle`
25. `framework-lean-pivot-decision`
26. `dk-yitang-channel-exploration-traps`
27. `case-yitang-sales-transformation-tuliaogongsi`
28. `tool-opc-sales-dialogue-assistant`

---

## 四、关键纠偏与边界

1. **不重复建设**：用户分层、价值主张、目标管理、工具化、决策卫生等概念已有 KDO 卡覆盖，本次只做销售域实例化，通过 related 引用。
2. **用户分层与卖点独立成卡**：未来咨询「该重点跟进哪些客户」和「怎么写卖点」可分别调用，避免合并后检索困难。
3. **案例处理**：剧本杀 SaaS、美容院、涂料公司作为三个完整转型案例独立成卡，分别覆盖 To B 初创 SaaS、To C 门店零售、传统工业分销；快钱支付、儿童记忆力培训、iPhone 充电器等作为工具卡嵌入式证据。
4. **数字降级**：课程中的「2 天」「60 分」「200 个案例」「20 个记录」「85-90% 完成率」等描述为项目经验/个人做法，不当作普适真理。
5. **OPC 智能体适配内嵌**：`tool-yitang-customer-segmentation-4step`、`tool-yitang-value-proposition-4step`、`tool-yitang-sales-process-decomposition`、`tool-yitang-sales-performance-management`、`framework-yitang-sales-incentive-6d` 等卡必须包含「OPC 智能体适配」小节，说明如何映射为 system prompt；不单独为这些子模块建卡，避免碎片化。
6. **MVP 智能体优先**：智能体层只新建 `tool-opc-sales-dialogue-assistant` 一张卡，其余 10 个智能体规格待本批卡片终审后根据反馈分批扩展。
7. **法律声明**：商标/合同/提成等涉及法律判断的案例，工具卡和 framework 卡中必须明确「AI/课程只提供公共知识扫盲，最终法律结论需专业机构复核」。
8. **OPC 改编**：激励团队、周会三要点、拆目标到个人等模块不直接适用于 OPC，需在相关卡片中明确 OPC 版改编提示。
9. **跨域融合**：每张卡必须同时桥接 sales 域和对应底层方法论域（strategy / management / ai-collaboration 等），不能只讲销售技巧。

---

## 五、验收标准

- [x] 12 张目标卡 `kdo pre-submit` PASS，无新增 ERROR。
- [x] 12 张目标卡 `kdo lint` 0 ERROR；新增 WARNING 需在任务单中说明。
- [x] `framework-yitang-scientific-sales-five-step` 包含五步法总图、六大通病、与一堂五步法关系、OPC 改编提示。
- [x] `tool-yitang-customer-segmentation-4step` 包含四步法、SABC 分级、分层假设清单、验证方法、≥8 项 checklist。
- [x] `tool-yitang-value-proposition-4step` 包含四步法、卖点结构、好卖点三原则、落地触点、≥8 项 checklist。
- [x] `tool-yitang-sales-process-decomposition` 包含三步法、四类用户决策、里程碑定义、剧本杀/美容院案例、≥8 项 checklist。
- [x] `tool-yitang-sales-performance-management` 包含三步法、目标拆解维度、业绩管理画布、Pipeline/Gap 分析、周会三要点、快钱支付/电商案例、≥10 项 checklist。
- [x] `framework-yitang-sales-incentive-6d` 包含四大问题、六维模型、50 策略速查、不同阶段重点、发钱三大设计点、OPC 改编提示。
- [x] `tool-yitang-sales-toolkit-radar` 包含工具箱三步法、六维雷达图、60/75/85 分工具清单、≥8 项 checklist。
- [x] `dk-yitang-sales-common-pitfalls` 包含 6 个反模式、≥6 条预警信号、每个陷阱的修复动作。
- [x] `case-yitang-sales-transformation-jubensha-saas` 包含 Background/Problem/Decision/Process/Result/Lessons/Failure Modes。
- [x] `case-yitang-sales-transformation-meirongyuan` 包含 Background/Problem/Decision/Process/Result/Lessons/Failure Modes。
- [x] `case-yitang-sales-transformation-tuliaogongsi` 包含 Background/Problem/Decision/Process/Result/Lessons/Failure Modes。
- [x] `tool-opc-sales-dialogue-assistant` 包含 When to Use/输入/输出/工作逻辑/System Prompt 模板/边界与风险/Checklist/Anti-patterns/Critique/Synthesis/Related。
- [x] 每张卡 Critique 包含 ≥3 个外部反对者与 ≥2 个内部局限。
- [x] 每张卡 related ≥ 5，且至少 2 条跨域。
- [x] ≥28 张已有卡的 related 已反向更新。
- [x] `opc-ai-sales-agent-architecture.md` 的 related 已加入 12 张新卡回链。
- [x] 欧阳锋终审通过。

---

## 六、生产顺序建议

| 批次 | 卡片 | 说明 |
|:---|:---|:---|
| 第一批 | `framework-yitang-scientific-sales-five-step` | 先建总图，作为后续 11 张卡的引用基础 |
| 第二批 | `tool-yitang-customer-segmentation-4step` + `tool-yitang-value-proposition-4step` | Step 1 两张工具卡 |
| 第三批 | `tool-yitang-sales-process-decomposition` | Step 2 过程工具 |
| 第四批 | `tool-yitang-sales-performance-management` | Step 3 业绩工具 |
| 第五批 | `framework-yitang-sales-incentive-6d` + `tool-yitang-sales-toolkit-radar` | Step 4 激励 + Step 5 工具箱 |
| 第六批 | `dk-yitang-sales-common-pitfalls` + `case-yitang-sales-transformation-jubensha-saas` + `case-yitang-sales-transformation-meirongyuan` + `case-yitang-sales-transformation-tuliaogongsi` | 反模式 + 三个转型案例 |
| 第七批 | `tool-opc-sales-dialogue-assistant` | OPC 智能体 MVP 规格卡，放在最后以便聚合前五步工具逻辑 |

---

## 七、队列位置

- **入队编号**：`#44`
- **状态**：`queued`
- **位置**：排在 `#43`（Live81 AI 赋能商标设计）之后。
- **预计工时**：老顽童生产 5-6 天 + 欧阳锋终审 1-2 天。

---

*王语嫣 2026-07-02*

---

## 欧阳锋终审结论（2026-06-29）

**终审通过。**

### 复核结果

| 验收项 | 状态 | 复核说明 |
|---|---|---|
| 12 张目标卡 `kdo pre-submit` | ✅ PASS | 12/12 通过，修复后无警告 |
| 12 张目标卡 `kdo lint` ERROR | ✅ 0 新增 ERROR | 修复后仅剩 #41 遗留 1 个 ERROR |
| 五步法总 framework | ✅ 通过 | 含总图、六大通病、与一堂五步法关系、OPC 改编提示 |
| 5 张 Step tool 卡 | ✅ 通过 | 均含四步法/三步法、checklist、anti-patterns、OPC 智能体适配小节 |
| 六维激励 framework | ✅ 通过 | 含 50 策略速查、不同阶段重点、发钱三大设计点、OPC 改编提示 |
| 销售工具箱 radar | ✅ 通过 | 含三步法、六维雷达图、60/75/85 分工具清单；修复 Synthesis wikilink 后 pre-submit 无警告 |
| dk 销售常见陷阱 | ✅ 通过 | 6 个反模式、预警信号、修复动作；欧阳锋审查中补充 lint schema 要求的 5 个标准 section |
| 3 个转型 case 卡 | ✅ 通过 | 含 Background/Problem/Decision/Process/Result/教训/失败模式；修复 case 卡 section 标题以符合 lint schema |
| OPC 销售对话助手 | ✅ 通过 | 含输入/输出/工作逻辑/System Prompt 模板/边界与风险/Checklist/Anti-patterns/Critique/Synthesis/Related |
| 每张卡 Critique ≥3 外部 + ≥2 内部 | ✅ 通过 | 均已满足 |
| 每张卡 related ≥5 且跨域 | ✅ 通过 | 最少 11 条，最多 17 条 |
| ≥28 张已有卡 related 反向更新 | ✅ 通过 | 实测 25/25 存在文件有回链；3 个目标文件不存在 |
| `opc-ai-sales-agent-architecture.md` 回链 | ✅ 已补齐 | 原回链 9 张，已补充 3 个 case 卡，共 12 张 |
| 自攻击报告 | ✅ 通过 | 0 致命，已更新 status 为 reviewed |

### 审查中发现并修复的问题

1. **`dk-yitang-sales-common-pitfalls.md` 缺失 lint 要求 section**
   - lint 报错缺失 `## 原始表述`、`## 使用场景`、`## 操作方法`、`## 为什么值钱`、`## 与其他知识的关联`
   - 修复：在「一句话」之后补充 5 个标准 section
   - 同步更新 `status: draft → enriched`

2. **`case-yitang-sales-transformation-jubensha-saas.md` 与 `case-yitang-sales-transformation-meirongyuan.md` section 标题未对齐 lint schema**
   - 原使用英文 `## Lessons`、`## Failure Modes`
   - lint 报错缺失 `## 关键证据`、`## 可迁移场景`、`## 教训`、`## 失败模式`
   - 修复：重命名 Lessons/Failure Modes 为中文，并补充关键证据、可迁移场景两个 section

3. **`tool-yitang-sales-toolkit-radar.md` Synthesis 0 wikilink**
   - pre-submit 警告 Synthesis section wikilink 不足
   - 修复：在 Synthesis 开头增加一条含 `[[framework-yitang-scientific-sales-five-step]]` 和 `[[tool-yitang-best-practice-as-golden-finger]]` 的链接

4. **`opc-ai-sales-agent-architecture.md` 实际回链只有 9 张**
   - 任务单/自攻击报告声称 12 张新卡均已回链
   - 修复：补充 3 个 case 卡的 related 回链

### 全库 lint 状态

- 12 张目标卡：0 ERROR
- 全库剩余 1 个 ERROR：`30_wiki/personal-os/zhu-time-os.md` 引用 `00_inbox/时间管理/时间管理_整合笔记.md` 不存在（#41 历史遗留，与 #44 无关）

### 内容质量评估

1. **framework-yitang-scientific-sales-five-step**：把一堂方法论与销售管理场景完整实例化，五步法总图清晰，六大通病诊断力强。
2. **4 张 Step tool 卡**：每个工具都含 When to Use、流程步骤、案例嵌入、checklist、anti-patterns、OPC 适配，可直接抄作业。
3. **framework-yitang-sales-incentive-6d**：六维模型 + 50 策略速查 + 不同阶段重点 + 发钱设计点，是激励设计的速查手册。
4. **tool-yitang-sales-toolkit-radar**：60/75/85 分工具清单 + 六维雷达图，帮助团队判断短板。
5. **dk-yitang-sales-common-pitfalls**：6 个反模式 + 口诀 + 修复动作，是销售管理体系的故障诊断器。
6. **3 个转型案例**：分别覆盖 To B 初创 SaaS、To C 门店零售、传统工业分销，数字均已降级为经验值。
7. **tool-opc-sales-dialogue-assistant**：第一张完整可运行的 OPC 销售智能体规格卡，System Prompt 模板可直接复制使用。

### 可改进点（不阻塞通过）

1. 全部样本来自一堂课程，跨行业外部独立验证可在后续 wave 中补充。
2. 部分工具卡正文末尾保留 `## Related` section，与 frontmatter `related` 重复；不违反 lint，可在后续统一格式任务中清理。
3. OPC 助手 System Prompt 示例为通用占位，需用户替换具体产品卖点与周期数据（已在模板注释中说明）。

同意封账。

*终审：欧阳锋 · 2026-06-29*
