# KDO 卡片质量门禁报告

**扫描时间**：2026-06-21  
**扫描范围**：30_wiki 全库 1703 张卡片  
**锚定评分**：1/5 — 不可用
**P0 阻塞问题卡片**：351 张  
**P1 修复问题卡片**：238 张  
**完全干净卡片**：1117 张  
**YAML 解析错误**：343 张  

---

## 锚定评分标准（Harness 1-5 + 取较低值）

| 分 | 标签 | 标准 |
|---|---|---|
| 5 | 可发布 | P0=0, P1<2%, 零CRITICAL |
| 4 | 可靠 | P0<1%, source_refs 真实 |
| 3 | 可用 | P0<5%, 骨架完整 |
| 2 | 草稿 | 需大量修复 |
| 1 | 不可用 | P0≥15% 或违反铁律 |

---

## P0 阻塞问题清单

| 文件 | P0 问题 |
|---|---|
| `cases\case-ai-agent-milestone-design.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 34, column 1:
    ---# 案例：Truman 用 AI Agent 3 小时设计 ... 
    ^
could not find expected ':'
  in "<unicode string>", line 36, column 1:
    > **Burn line**: 全程不动手，42 轮口授反馈， ... 
    ^ |
| `cases\case-ether-online-acquisition.md` | YAML 解析错误: None |
| `cases\case-five-step-fake-vs-real-barriers.md` | YAML 解析错误: None |
| `cases\case-five-step-growth-first-lever.md` | YAML 解析错误: None |
| `cases\case-gudong-tea-shop-foresight.md` | YAML 解析错误: None |
| `cases\case-hr-saas-feature-usage-trap.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 35, column 1:
    ---# HR SaaS：把“功能使用率↑续费率↑”当因果的功能堆砌陷阱
    ^
could not find expected ':'
  in "<unicode string>", line 37, column 1:
    > 一堂业务公式拆解培训中的“相关≠因果”错误示范：一个年 GM ... 
    ^ |
| `cases\case-ji-hao-skill-market-problem-validation.md` | YAML 解析错误: None |
| `cases\case-livestream-sop-modeling.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 45, column 1:
    ---# 案例：直播前热身 SOP 建模
    ^
could not find expected ':'
  in "<unicode string>", line 47, column 1:
    > **Burn line**: 直播状态不是运气，而是一套可以 ... 
    ^ |
| `cases\case-milktea-five-step.md` | YAML 解析错误: None |
| `cases\case-modeling-abstraction-reliability-ladder.md` | YAML 解析错误: None |
| `cases\case-modeling-abstraction-yitang-models.md` | YAML 解析错误: None |
| `cases\case-modeling-essence-schools.md` | YAML 解析错误: None |
| `cases\case-modeling-process-livestream-roles.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 47, column 1:
    ---# 流程建模案例：直播开播团队分工与检查清单
    ^
could not find expected ':'
  in "<unicode string>", line 49, column 1:
    > 来源：`src_20260614_c62e0e61`（Tru ... 
    ^ |
| `cases\case-modeling-process-sop-evolution.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 47, column 1:
    ---# 流程建模案例：一堂 2021-2024 年 SOP 清单演进史
    ^
could not find expected ':'
  in "<unicode string>", line 49, column 1:
    > 来源：Truman-高阶建模-流程建模-图-01 | 一堂建 ... 
    ^ |
| `cases\case-modeling-process-sop-examples.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 45, column 1:
    ---# 流程建模案例：10 个学员企业的 SOP 实践样本
    ^
could not find expected ':'
  in "<unicode string>", line 47, column 1:
    > 来源：Truman-高阶建模-流程建模-图-02 | 一堂建 ... 
    ^ |
| `cases\case-personal-map-modeling.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 48, column 1:
    ---# 案例：一堂个人地图的完整建模过程
    ^
could not find expected ':'
  in "<unicode string>", line 50, column 1:
    > **Burn line**: 一张 10 万美金级别的地图， ... 
    ^ |
| `cases\case-shampoo-product-kernel.md` | YAML 解析错误: None |
| `cases\case-smart-medicine-cabinet-business-model-validation.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 26, column 1:
    ---# 智能药柜推广项目：录音商业模式命题交叉验证
    ^
could not find expected ':'
  in "<unicode string>", line 28, column 1:
    > **核心定位**：本卡基于 4 条内部听脑录音（124166 ... 
    ^ |
| `cases\case-smart-medicine-cabinet-corporate-risk.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 26, column 1:
    ---# 知识卡草稿：智能药柜推广项目 · 公司/股权/资金风险
    ^
could not find expected ':'
  in "<unicode string>", line 28, column 1:
    **卡片编号**：kc_itingnao_corporate-r ... 
    ^ |
| `cases\case-smart-medicine-cabinet-failure-patterns-library.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 47, column 1:
    ---# 智能药柜失败模式案例库
    ^
could not find expected ':'
  in "<unicode string>", line 49, column 1:
    > **核心定位**：汇总公开渠道可获取的智能药柜/无人药房失败 ... 
    ^ |
| `cases\case-toc-content-platform-correlation-trap.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 34, column 1:
    ---# ToC 内容付费平台：把“流量↑转化率↓”当因果导致的投放崩盘
    ^
could not find expected ':'
  in "<unicode string>", line 36, column 1:
    > 一堂业务公式拆解培训中的“相关≠因果”错误示范：一个月 GM ... 
    ^ |
| `cases\case-toc-ecommerce-formula-misjudgment.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 35, column 1:
    ---# ToC 消费品电商：业务公式拆解误判导致放量亏损
    ^
could not find expected ':'
  in "<unicode string>", line 37, column 1:
    > 一堂业务公式拆解培训的核心案例：一个创始人有 10 年经验的 ... 
    ^ |
| `cases\case-treadmill-demand-analysis.md` | YAML 解析错误: None |
| `cases\case-truman-ai-partner.md` | YAML 解析错误: None |
| `cases\case-truman-ai-skill-engineering-guide.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 50, column 1:
    ---# 案例：Truman 如何用 3 小时做出高阶 AI S ... 
    ^
could not find expected ':'
  in "<unicode string>", line 52, column 1:
    > **Burn line**: 不是让 AI 随便写个 Ski ... 
    ^ |
| `cases\case-truman-ai-skill-self-packaging.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 45, column 1:
    ---# AI 自复盘自封装：Truman 怎么让 AI 把自己 ... 
    ^
could not find expected ':'
  in "<unicode string>", line 47, column 1:
    > **Burn line**: 不是人写 skill——是 A ... 
    ^ |
| `cases\case-truman-livestream-sop-iteration.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 38, column 1:
    ---# Truman 直播 SOP 三年迭代：从 0 到 50 ... 
    ^
could not find expected ':'
  in "<unicode string>", line 40, column 1:
    > **这不是方法论——这是方法论在现场长出来的过程。**
    ^ |
| `cases\case-truman-motivation-map-12-versions.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 43, column 1:
    ---# 动机地图12版迭代：先观察再设计
    ^
could not find expected ':'
  in "<unicode string>", line 45, column 1:
    > Truman在设计一堂的"学习动机地图"时，没有先画设计稿， ... 
    ^ |
| `cases\case-truman-personal-growth-map-creation.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 47, column 1:
    ---# Truman 个人地图创作：从模糊想法到四格天花板的七步
    ^
could not find expected ':'
  in "<unicode string>", line 49, column 1:
    > **Burn line**: AI 出了几个版本全是"分类不 ... 
    ^ |
| `cases\case-truman-poker-deck-roi.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 46, column 1:
    ---# 扑克牌案例：同样的任务，两个同学评估结果截然相反
    ^
could not find expected ':'
  in "<unicode string>", line 48, column 1:
    > Truman 在 ROI 决策高度课上分享了一个真实内部案例 ... 
    ^ |
| `cases\case-truman-prd-checklist-evolution.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 42, column 1:
    ---# Truman的PRD清单进化
    ^
could not find expected ':'
  in "<unicode string>", line 44, column 1:
    > Truman在知识萃取探索营中回溯了他早期在去哪儿做产品经理 ... 
    ^ |
| `cases\case-truman-yitang-foresight.md` | YAML 解析错误: None |
| `cases\case-unit-model-gashapon.md` | YAML 解析错误: None |
| `cases\case-xiaolong-ecommerce-foresight.md` | YAML 解析错误: None |
| `cases\case-yitang-double-triangle-confidence.md` | YAML 解析错误: None |
| `cases\case-yitang-education-supply-chain.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 33, column 1:
    ---# 案例：一堂是「教育供应链创新公司」——从真实实践里种菜 ... 
    ^
could not find expected ':'
  in "<unicode string>", line 35, column 1:
    > **Burn line**: 一堂不是包装 IP 讲别人课的 ... 
    ^ |
| `cases\case-yitang-model-asset-inventory.md` | YAML 解析错误: None |
| `cases\case-yitang-model-valuation-flywheel.md` | YAML 解析错误: None |
| `cases\case-yitang-radar-chart-selection.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 50, column 1:
    ---# 案例：一堂雷达图评选机制——从 Truman 拍板到「 ... 
    ^
could not find expected ':'
  in "<unicode string>", line 52, column 1:
    > **Burn line**: 当评选对象多到 CEO 拍不了 ... 
    ^ |
| `cases\case-yitang-tob-grinding-machine.md` | source_refs 为空 |
| `cases\case-yitang-weekly-modeling-engine.md` | YAML 解析错误: None |
| `cases\case-一堂-无人餐厅-hypothesis-failure.md` | YAML 解析错误: None |
| `cases\industrial-ai-ops-cases.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 25, column 1:
    ---# 产业 AI 运营落地：酒店/房产/电商三大案例的去伪存真
    ^
could not find expected ':'
  in "<unicode string>", line 27, column 1:
    > 来源：听脑录音 5640373/5639853/563856 ... 
    ^ |
| `cases\smart-medicine-cabinet-clinic-risk-observation.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 45, column 1:
    ---# 诊所 + 智能药柜协同模式：一线观察与风险提示
    ^
could not find expected ':'
  in "<unicode string>", line 47, column 1:
    > **核心定位**：本卡基于一份广州增城/新塘小型诊所老板的访 ... 
    ^ |
| `concept-card-index-latest.md` | YAML 解析错误: None |
| `concepts\ai-collaboration-mindset-shift.md` | YAML 解析错误: None |
| `concepts\ai-landing-scene-selection.md` | YAML 解析错误: None |
| `concepts\ai-learning-closed-loop.md` | YAML 解析错误: None |
| `concepts\ai-native-im-multi-agent.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 21, column 1:
    ---# AI 原生 IM：让 Agent 成为一等公民的协作基础设施
    ^
could not find expected ':'
  in "<unicode string>", line 23, column 1:
    > 来源：听脑录音 5383332 + 公开信源六层交叉验证  
    ^ |
| `concepts\ai-native-五层进阶从答案到效率到作品到产品到系统.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 45, column 1:
    ---# AI Native 五层进阶：从答案，到效率，到作品， ... 
    ^
could not find expected ':'
  in "<unicode string>", line 47, column 1:
    > **核心定位**：一个普通人从”把AI当搜索框”到”搭建个人 ... 
    ^ |
| `concepts\ai单元模型口述蒋老师.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 31, column 1:
    ---# AI+单元模型口述（蒋老师/磊哥）
    ^
could not find expected ':'
  in "<unicode string>", line 33, column 1:
    > **一句话定位**：单元模型是商业可行性的最后一道防线——A ... 
    ^ |
| `concepts\ai数据理解第一课.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 29, column 1:
    ---# AI数据理解第一课
    ^
could not find expected ':'
  in "<unicode string>", line 31, column 1:
    > **核心定位**：AI时代普通人唯一能建立护城河的方向是数据 ... 
    ^ |
| `concepts\ai时代判断力口述-3.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 26, column 1:
    ---# AI时代判断力口述（国帅）
    ^
could not find expected ':'
  in "<unicode string>", line 28, column 1:
    > **一句话定位**：AI接管Process（加工推理）后，人 ... 
    ^ |
| `concepts\business-research-skill-oscar-13-weapon-system.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 17, column 1:
    ---# Business Research Skill — O ... 
    ^
could not find expected ':'
  in "<unicode string>", line 19, column 1:
    > huanwang.org 出品，v2.1.0。将 一堂 OS ... 
    ^ |
| `concepts\concept-five-step-growth-to-barrier-transition.md` | YAML 解析错误: None |
| `concepts\concept-mckinsey-issue-tree.md` | YAML 解析错误: None |
| `concepts\concept-mckinsey-mece.md` | YAML 解析错误: None |
| `concepts\concept-smart-medicine-cabinet-consumer-acceptance.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 21, column 1:
    ---# 消费者购药行为与智能药柜接受度
    ^
could not find expected ':'
  in "<unicode string>", line 23, column 1:
    > **核心定位**：从需求侧梳理消费者夜间/应急用药需求、购药 ... 
    ^ |
| `concepts\concept-smart-medicine-cabinet-digital-pharmacy-diagnosis.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 19, column 1:
    ---# 知识卡草稿：智能药柜/数字药房项目诊断
    ^
could not find expected ':'
  in "<unicode string>", line 21, column 1:
    > 卡片编号：kc_itingnao_digital-pharm ... 
    ^ |
| `concepts\concept-smart-medicine-cabinet-giants-why-not-clinic-cabinet.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 20, column 1:
    ---# 巨头为何不做诊所+智能药柜：竞争格局与壁垒分析
    ^
could not find expected ':'
  in "<unicode string>", line 22, column 1:
    > **核心定位**：从阿里健康、京东健康、美团买药、饿了么、叮 ... 
    ^ |
| `concepts\concept-smart-medicine-cabinet-international-models.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 20, column 1:
    ---# 国际自动取药机/药房模式经验与启示
    ^
could not find expected ':'
  in "<unicode string>", line 22, column 1:
    > **核心定位**：梳理日本、美国、欧洲在自动售药机/自动取药 ... 
    ^ |
| `concepts\concept-smart-medicine-cabinet-platform-cooperation-validation.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 19, column 1:
    ---# 智能药柜平台合作命题交叉验证
    ^
could not find expected ':'
  in "<unicode string>", line 21, column 1:
    ## 一、已记录的关键数字（原样保留）
    ^ |
| `concepts\concept-smart-medicine-cabinet-supply-chain-validation.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 19, column 1:
    ---# 智能药柜供应链/技术交叉验证（知识卡草稿）
    ^
could not find expected ':'
  in "<unicode string>", line 21, column 1:
    ## 1. 一句话摘要
    ^ |
| `concepts\concept-thousand-people-square.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 44, column 1:
    ---# 千人广场模型：一堂做课背后的统计建模理念
    ^
could not find expected ':'
  in "<unicode string>", line 46, column 1:
    > **Burn line**: 一堂不是为三五个人做课，而是对 ... 
    ^ |
| `concepts\concept-一堂-hypothesis-driven-business-methodology.md` | YAML 解析错误: None |
| `concepts\concept-一堂-kernel-iteration.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 29, column 1:
    ---# 产品内核迭代：从静态到动态的五方向演化
    ^
could not find expected ':'
  in "<unicode string>", line 31, column 1:
    > **产品内核迭代的本质：产品内核不是一次性定死的，而是需要随 ... 
    ^ |
| `concepts\concept-一堂-kernel-validation.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 30, column 1:
    ---# 产品内核验证：三维度评估 + 六策略验证
    ^
could not find expected ':'
  in "<unicode string>", line 32, column 1:
    > **产品内核验证的本质：在投入实质性资源之前，用最小成本确认 ... 
    ^ |
| `concepts\concept-一堂-key-assumptions.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 31, column 1:
    ---# 关键假设思维：259工具与假设驱动的创业方法
    ^
could not find expected ':'
  in "<unicode string>", line 33, column 1:
    > 黄药师骨架 · 老顽童填内容
    ^ |
| `concepts\concept-一堂-product-kernel.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 32, column 1:
    ---# 产品内核：用户愿意选择你的最小解决方案
    ^
could not find expected ':'
  in "<unicode string>", line 34, column 1:
    > **产品内核的本质是一套“用户决策逻辑解构工具”——它帮你从 ... 
    ^ |
| `concepts\contingency-decision-making.md` | YAML 解析错误: None |
| `concepts\course-to-skill-conversion.md` | YAML 解析错误: None |
| `concepts\ec工业化规范手册-v2.8.0.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 21, column 1:
    ---# EC工业化规范手册 v2.8.0
    ^
could not find expected ':'
  in "<unicode string>", line 23, column 1:
    > **定位**：鑫港湾HIS系统 · 执行卡片（Executi ... 
    ^ |
| `concepts\fd-forward-deployment.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 23, column 1:
    ---# Forward Deployment（FD）模式：企业 ... 
    ^
could not find expected ':'
  in "<unicode string>", line 25, column 1:
    > 来源：听脑录音 6086504 + 公开信源六层交叉验证  
    ^ |
| `concepts\find-old-do-small.md` | YAML 解析错误: None |
| `concepts\graph-rag.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 22, column 1:
    ---# Graph RAG — Knowledge-Graph ... 
    ^
could not find expected ':'
  in "<unicode string>", line 24, column 1:
    ## Claims
    ^ |
| `concepts\kdo-flywheel.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 26, column 1:
    ---# KDO 飞轮 — 建造→使用→反思→实验
    ^
could not find expected ':'
  in "<unicode string>", line 28, column 1:
    > **核心定位**：KDO 不是静态知识库，是**每一圈产出都 ... 
    ^ |
| `concepts\kdo-yaml-frontmatter-safety.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 40, column 1:
    ---# KDO YAML Frontmatter 安全操作指南
    ^
could not find expected ':'
  in "<unicode string>", line 42, column 1:
    > **背景**：2026-05-31 Data Curator ... 
    ^ |
| `concepts\modeling-three-values.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 44, column 1:
    ---# 建模的三重价值：确定性、框架性、迁移性
    ^
could not find expected ':'
  in "<unicode string>", line 46, column 1:
    > **Burn line**: 所有模型最终都是为了解决三个问 ... 
    ^ |
| `concepts\prd-as-ai-instruction.md` | YAML 解析错误: None |
| `concepts\skill-ai-four-elements-validation.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 53, column 1:
    ---# 技能：真需求四要素验证法
    ^
could not find expected ':'
  in "<unicode string>", line 55, column 1:
    > **来源**：纪浩（AI俱乐部-AI协作方法论-口述）
    ^ |
| `concepts\skill-ai-info-literacy-three-layer.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 53, column 1:
    ---# 技能：AI输出三层防护检查法
    ^
could not find expected ':'
  in "<unicode string>", line 55, column 1:
    > **来源**：基于 master-ai-info-liter ... 
    ^ |
| `concepts\skill-ai-problem-question-check.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 52, column 1:
    ---# 技能：Problem vs Question 区分法
    ^
could not find expected ':'
  in "<unicode string>", line 54, column 1:
    > **来源**：纪浩（AI俱乐部-AI协作方法论-口述）
    ^ |
| `concepts\skill-使用一页纸速查卡快速调用框架.md` | YAML 解析错误: None |
| `concepts\skill-水水-管理决策权重偏差.md` | YAML 解析错误: None |
| `concepts\skill-纪浩-AI使用边界管理法.md` | YAML 解析错误: None |
| `concepts\skill-纪浩-AI对话上下文隔离.md` | YAML 解析错误: None |
| `concepts\skill-纪浩-AI工具脚本化约束.md` | YAML 解析错误: None |
| `concepts\skill-纪浩-Agent开工检查单制作法.md` | YAML 解析错误: None |
| `concepts\skill-纪浩-Problem与Question区分法.md` | YAML 解析错误: None |
| `concepts\skill-纪浩-任务交付物标准化.md` | YAML 解析错误: None |
| `concepts\skill-纪浩-低成本输出验证法.md` | YAML 解析错误: None |
| `concepts\skill-纪浩-处理AI生成代码运行异常.md` | YAML 解析错误: None |
| `concepts\skill-马易-业务为先的AI中台建设.md` | YAML 解析错误: None |
| `concepts\smart-medicine-cabinet-national-policy-redlines.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 36, column 1:
    ---# 自助售药机国家政策与红线（2024 年第 48 号公告解读）
    ^
could not find expected ':'
  in "<unicode string>", line 38, column 1:
    > **核心定位**：国家药监局对自助售药机的销售品类有明确红线 ... 
    ^ |
| `concepts\smart-medicine-cabinet-o2o-cost-structure.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 37, column 1:
    ---# 医药 O2O 成本与毛利结构
    ^
could not find expected ':'
  in "<unicode string>", line 39, column 1:
    > **核心定位**：药柜若作为 O2O 前置仓，平台抽成和配送 ... 
    ^ |
| `concepts\smart-medicine-cabinet-regional-policy-map.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 36, column 1:
    ---# 各省市自助售药机政策差异地图
    ^
could not find expected ':'
  in "<unicode string>", line 38, column 1:
    > **核心定位**：国家底线是"仅乙类 OTC"，但各省市在设 ... 
    ^ |
| `concepts\structured-ai-workspace.md` | YAML 解析错误: None |
| `concepts\truman-perspective-skill.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 21, column 1:
    ---# Truman Perspective Skill —  ... 
    ^
could not find expected ':'
  in "<unicode string>", line 23, column 1:
    > 基于 6 维度深度调研（著作/对话/表达DNA/他者视角/决 ... 
    ^ |
| `concepts\web-scraping-三剑客-scrapling-crawl4ai-firecrawl.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 18, column 1:
    ---# Web Scraping 三剑客 — Scraplin ... 
    ^
could not find expected ':'
  in "<unicode string>", line 20, column 1:
    > 2026年AI时代三大网页抓取技术。一句话定位：Firecr ... 
    ^ |
| `concepts\yitang-course-map.md` | YAML 解析错误: None |
| `concepts\yitang-huazong-ama-by-industry.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 17, column 1:
    ---# 花总AMA按行业分类整理
    ^
could not find expected ':'
  in "<unicode string>", line 19, column 1:
    > 原文：yitang-huazong-ama-20250526
    ^ |
| `concepts\yitang-huazong-ama-summary.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 16, column 1:
    ---# 花总AMA精华摘要
    ^
could not find expected ':'
  in "<unicode string>", line 18, column 1:
    > 原文：yitang-huazong-ama-20250526
    ^ |
| `concepts\yitang-methodology-system.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 48, column 1:
    ---# 一堂方法论体系：从科学做事到无限进步
    ^
could not find expected ':'
  in "<unicode string>", line 50, column 1:
    > Source: 90_control/itingnao-ki ... 
    ^ |
| `concepts\yt-barrier-identification-skill.md` | YAML 解析错误: None |
| `concepts\yt-business-formula-l6-essence-formulas.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 33, column 1:
    ---# 业务公式 L6 魔法参数：跨行业本质公式集锦
    ^
could not find expected ':'
  in "<unicode string>", line 35, column 1:
    > 业务公式拆解到 L5 之后，如果继续追问“用户为什么买/为什 ... 
    ^ |
| `concepts\yt-business-formula-ten-paradigms.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 33, column 1:
    ---# 一堂业务公式十大经典范式
    ^
could not find expected ':'
  in "<unicode string>", line 35, column 1:
    > 一堂把常见业务增长问题抽象为 10 个公式范式，按「收入提升 ... 
    ^ |
| `concepts\yt-composite-pan-product-methodology.md` | YAML 解析错误: None |
| `concepts\yt-concept-ai-guard-brain.md` | YAML 解析错误: None |
| `concepts\yt-concept-weapon-arsenal.md` | YAML 解析错误: None |
| `concepts\yt-decision-ai-partner.md` | YAML 解析错误: None |
| `concepts\yt-decision-canvas.md` | YAML 解析错误: None |
| `concepts\yt-decision-consensus-iceberg.md` | YAML 解析错误: None |
| `concepts\yt-decision-full-process.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 99, column 1:
    ---# 科学决策全景流程：有意识→写初版→细打磨→有共识→复盘 ... 
    ^
could not find expected ':'
  in "<unicode string>", line 103, column 1:
    > 来源：一堂《科学决策·ROI决策实践》全景地图篇。Y模型是" ... 
    ^ |
| `concepts\yt-decision-habit-shift.md` | YAML 解析错误: None |
| `concepts\yt-decision-height-toolkit.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 84, column 1:
    ---# 高度分析工具：上帝视角四维提升法 + 高水平共识曲线
    ^
could not find expected ':'
  in "<unicode string>", line 86, column 1:
    ## Summary
    ^ |
| `concepts\yt-decision-review.md` | YAML 解析错误: None |
| `concepts\yt-decision-width-method.md` | YAML 解析错误: None |
| `concepts\yt-decision-y-model.md` | YAML 解析错误: None |
| `concepts\yt-entrepreneur-five-step-method.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 100, column 1:
    ---# 一堂五步法
    ^
could not find expected ':'
  in "<unicode string>", line 102, column 1:
    > 来源：一堂课程体系 | 阶段：预判阶段/核心框架。[[yit ... 
    ^ |
| `concepts\yt-entrepreneur-growth-flywheel.md` | YAML 解析错误: None |
| `concepts\yt-entrepreneur-key-hypotheses.md` | YAML 解析错误: None |
| `concepts\yt-entrepreneur-lean-validation.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 65, column 1:
    ---# 低成本验证/MVP
    ^
could not find expected ':'
  in "<unicode string>", line 67, column 1:
    > 来源：一堂课程体系 | 阶段：起盘阶段。[[yitang-c ... 
    ^ |
| `concepts\yt-entrepreneur-liberate-thinking.md` | YAML 解析错误: None |
| `concepts\yt-entrepreneur-needs-analysis.md` | YAML 解析错误: None |
| `concepts\yt-entrepreneur-research-cognition.md` | YAML 解析错误: None |
| `concepts\yt-entrepreneur-unit-model.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 54, column 1:
    ---# 单元模型
    ^
could not find expected ':'
  in "<unicode string>", line 56, column 1:
    > 来源：一堂课程体系 | 阶段：预判阶段/核心框架。[[yit ... 
    ^ |
| `concepts\yt-five-step-common-pitfalls.md` | YAML 解析错误: None |
| `concepts\yt-five-step-implementation.md` | YAML 解析错误: None |
| `concepts\yt-five-step-method.md` | YAML 解析错误: None |
| `concepts\yt-foresight-15-char-mantra.md` | YAML 解析错误: None |
| `concepts\yt-foresight-ab-steady-state.md` | YAML 解析错误: None |
| `concepts\yt-foresight-business-spectrum.md` | YAML 解析错误: None |
| `concepts\yt-foresight-deliverables-four-levels.md` | YAML 解析错误: None |
| `concepts\yt-foresight-probability-engineering.md` | YAML 解析错误: None |
| `concepts\yt-management-business-formula.md` | YAML 解析错误: None |
| `concepts\yt-management-company-culture.md` | YAML 解析错误: None |
| `concepts\yt-management-conversion-hacking.md` | YAML 解析错误: None |
| `concepts\yt-management-finance-basics.md` | YAML 解析错误: None |
| `concepts\yt-management-onboarding.md` | YAML 解析错误: None |
| `concepts\yt-management-partnership-equity.md` | YAML 解析错误: None |
| `concepts\yt-management-scientific-decision.md` | YAML 解析错误: None |
| `concepts\yt-management-scientific-hiring.md` | YAML 解析错误: None |
| `concepts\yt-management-team-knowledge.md` | YAML 解析错误: None |
| `concepts\yt-management-toolkit-overview.md` | YAML 解析错误: None |
| `concepts\yt-model-aesthetic-progression.md` | YAML 解析错误: None |
| `concepts\yt-model-conversion-optimization.md` | YAML 解析错误: None |
| `concepts\yt-model-dual-triangle-competitiveness.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 45, column 1:
    ---# 双三角竞争力模型 (Yitang Dual Trian ... 
    ^
could not find expected ':'
  in "<unicode string>", line 47, column 1:
    > 来源：一堂《AI 时代的竞争力·双三角模型》（2025.9. ... 
    ^ |
| `concepts\yt-model-entrepreneur-map.md` | YAML 解析错误: None |
| `concepts\yt-model-five-step-canvas.md` | YAML 解析错误: None |
| `concepts\yt-model-ipo-learning-strategy.md` | YAML 解析错误: None |
| `concepts\yt-model-pan-product-36-strategies.md` | YAML 解析错误: None |
| `concepts\yt-model-pan-product-aesthetic-toolkit.md` | YAML 解析错误: None |
| `concepts\yt-model-pan-product-climbing-map.md` | YAML 解析错误: None |
| `concepts\yt-model-pan-product-demand-toolkit.md` | YAML 解析错误: None |
| `concepts\yt-model-pan-product-execution-toolkit.md` | YAML 解析错误: None |
| `concepts\yt-model-pan-product-three-virtues.md` | YAML 解析错误: None |
| `concepts\yt-model-personal-map.md` | YAML 解析错误: None |
| `concepts\yt-model-personal-pitch-toolkit.md` | YAML 解析错误: None |
| `concepts\yt-model-progress-map.md` | YAML 解析错误: None |
| `concepts\yt-model-prompt-engineering.md` | YAML 解析错误: None |
| `concepts\yt-note-ai-human-division.md` | YAML 解析错误: None |
| `concepts\yt-note-checklist-concept.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 56, column 1:
    ---# 一堂笔记法：清单体笔记的核心概念与原理
    ^
could not find expected ':'
  in "<unicode string>", line 58, column 1:
    > 来源：一堂《AI时代清单体笔记》完整课程。Truman十年刻 ... 
    ^ |
| `concepts\yt-panproduct-aesthetic-collection.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-aesthetic-imagination.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-aesthetic-modeling.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-aesthetic-pool.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-demand-five-step-method.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-demand-industry-canvas.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-demand-motivation-resistance.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-demand-multi-perspective.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-demand-need-discovery.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-demand-peak-end-rule.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-demand-project-background.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-demand-scenario-walkthrough.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-demand-surprise-formula.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-demand-user-perspective.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-demand-user-segmentation.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-execution-10x-validation.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-execution-business-modeling.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-execution-core-and-boundary.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-execution-design-principles.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-execution-good-tools.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-execution-hypothesis-decomposition.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-execution-idea-spark.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-execution-incubation-polish.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-execution-liberate-thinking.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-execution-logic-mece.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-execution-low-cost-mvp.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-execution-management-trilogy.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-execution-milestone-breakdown.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-execution-realistic-simulation.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-execution-review-iteration.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-execution-risk-management.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-execution-roi-analysis.md` | YAML 解析错误: None |
| `concepts\yt-panproduct-execution-war-room.md` | YAML 解析错误: None |
| `concepts\yt-personal-ai-capability.md` | YAML 解析错误: None |
| `concepts\yt-personal-deep-review.md` | YAML 解析错误: None |
| `concepts\yt-personal-ipo-learning.md` | YAML 解析错误: None |
| `concepts\yt-personal-knowledge-extraction.md` | YAML 解析错误: None |
| `concepts\yt-personal-pan-product-02.md` | YAML 解析错误: None |
| `concepts\yt-personal-pan-product-aesthetics.md` | YAML 解析错误: None |
| `concepts\yt-personal-pan-product-concepts.md` | YAML 解析错误: None |
| `concepts\yt-personal-pan-product-exploration.md` | YAML 解析错误: None |
| `concepts\yt-personal-pan-product-practice.md` | YAML 解析错误: None |
| `concepts\yt-personal-pan-product-tools.md` | YAML 解析错误: None |
| `concepts\yt-personal-scientific-expression.md` | YAML 解析错误: None |
| `concepts\yt-personal-y-model-exploration-2.md` | YAML 解析错误: None |
| `concepts\yt-pitch-aphorism.md` | YAML 解析错误: None |
| `concepts\yt-pitch-colloquialization.md` | YAML 解析错误: None |
| `concepts\yt-pitch-conflict.md` | YAML 解析错误: None |
| `concepts\yt-pitch-emotionalization.md` | YAML 解析错误: None |
| `concepts\yt-pitch-materialization.md` | YAML 解析错误: None |
| `concepts\yt-pitch-scenarization.md` | YAML 解析错误: None |
| `concepts\yt-pitch-sublimation.md` | YAML 解析错误: None |
| `concepts\yt-prompt-engineering-andrew-ng.md` | YAML 解析错误: None |
| `concepts\yt-three-dimension-opportunity-matrix.md` | YAML 解析错误: None |
| `concepts\yt-tob-sales-unit-model.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 46, column 1:
    ---# To B 单销售模型：时间闭环 + 空间闭环
    ^
could not find expected ':'
  in "<unicode string>", line 48, column 1:
    > To B 业务最容易被忽视的单元模型不是单订单，而是**单销 ... 
    ^ |
| `concepts\yt-tool-best-practice-learning.md` | YAML 解析错误: None |
| `concepts\yt-tool-fab-persuasion.md` | YAML 解析错误: None |
| `concepts\yt-tool-foresight-canvas.md` | YAML 解析错误: None |
| `concepts\yt-tool-mental-model-refinement.md` | YAML 解析错误: None |
| `concepts\yt-tool-product-core-canvas.md` | YAML 解析错误: None |
| `concepts\yt-tool-y-model-ruler.md` | YAML 解析错误: None |
| `concepts\yt-unit-model-build.md` | YAML 解析错误: None |
| `concepts\yt-unit-model-concept.md` | YAML 解析错误: None |
| `concepts\yt-unit-model-selection.md` | YAML 解析错误: None |
| `concepts\互联网医院模式深度调研报告.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 21, column 1:
    ---# 互联网医院模式深度调研报告
    ^
could not find expected ':'
  in "<unicode string>", line 23, column 1:
    > **核心问题**：诊所远程问诊送药的合规路径与商业闭环是否走得通？
    ^ |
| `concepts\人机协作决策-双三角模型.md` | YAML 解析错误: None |
| `concepts\学会提问在信息洪流中锻造批判性思维的利刃.md` | YAML 解析错误: None |
| `concepts\诊所o2o外卖平台业务深度调研报告.md` | YAML 解析错误: None |
| `concepts\鑫港湾his系统分阶段整改报告.md` | YAML 解析错误: None |
| `dark-knowledges\dk-c10-batch-tool-no-dry-run.md` | YAML 解析错误: None |
| `dark-knowledges\dk-c11-hongqigong-skip-review.md` | YAML 解析错误: None |
| `dark-knowledges\dk-c4-selfcheck-superseded.md` | YAML 解析错误: None |
| `dark-knowledges\dk-c5-todo-false-positive.md` | YAML 解析错误: None |
| `dark-knowledges\dk-c6-large-source-overflow.md` | YAML 解析错误: None |
| `dark-knowledges\dk-c7-auto-backup-conflict.md` | YAML 解析错误: None |
| `dark-knowledges\dk-c8-format-complete-mind-empty.md` | YAML 解析错误: None |
| `dark-knowledges\dk-c9-batch-trigger-garbage.md` | YAML 解析错误: None |
| `dark-knowledges\dk-f10-broken-source-refs.md` | YAML 解析错误: None |
| `dark-knowledges\dk-f12-builder-context-deadlock.md` | YAML 解析错误: None |
| `dark-knowledges\dk-f3-state-json-race-condition.md` | YAML 解析错误: None |
| `dark-knowledges\dk-f4-wrong-workdir.md` | YAML 解析错误: None |
| `dark-knowledges\dk-f5-stale-feedback-ref.md` | YAML 解析错误: None |
| `dark-knowledges\dk-f6-cjk-skeleton-corruption.md` | YAML 解析错误: None |
| `dark-knowledges\dk-f7-surface-translation.md` | YAML 解析错误: None |
| `dark-knowledges\dk-f8-phony-wikilink.md` | YAML 解析错误: None |
| `dark-knowledges\dk-f9-generic-critique.md` | YAML 解析错误: None |
| `dark-knowledges\dk-infrastructure-guardrails-over-checklist.md` | YAML 解析错误: None |
| `dark-knowledges\dk-kdo-leaky-pipe-pressure.md` | source_refs 为空 |
| `dark-knowledges\dk-mckinsey-hypothesis-driven-pitfalls.md` | YAML 解析错误: None |
| `dark-knowledges\dk-modeling-ai-without-judgment.md` | YAML 解析错误: None |
| `dark-knowledges\dk-modeling-business-visual-logic-match.md` | YAML 解析错误: None |
| `dark-knowledges\dk-modeling-checklist-formatting-rules.md` | YAML 解析错误: None |
| `dark-knowledges\dk-modeling-counterexample-driven.md` | YAML 解析错误: None |
| `dark-knowledges\dk-modeling-course-rnd-ripe-fruit.md` | YAML 解析错误: None |
| `dark-knowledges\dk-modeling-logical-cleanliness-root.md` | YAML 解析错误: None |
| `dark-knowledges\dk-p1-model-switch-env.md` | YAML 解析错误: None |
| `dark-knowledges\dk-p10-oral-ban.md` | YAML 解析错误: None |
| `dark-knowledges\dk-p11-regex-cutoff.md` | YAML 解析错误: None |
| `dark-knowledges\dk-p13-token-burn.md` | YAML 解析错误: None |
| `dark-knowledges\dk-p14-zombie.md` | YAML 解析错误: None |
| `dark-knowledges\dk-p18-yaml-parser.md` | YAML 解析错误: None |
| `dark-knowledges\dk-p19-quote-yaml.md` | YAML 解析错误: None |
| `dark-knowledges\dk-p20-bigram-fail.md` | YAML 解析错误: None |
| `dark-knowledges\dk-p5-cc-connect-config.md` | YAML 解析错误: None |
| `dark-knowledges\dk-p6-session-resume-fail.md` | YAML 解析错误: None |
| `dark-knowledges\dk-p7-ocr-skip.md` | YAML 解析错误: None |
| `dark-knowledges\dk-p8-toolkit-forget.md` | YAML 解析错误: None |
| `dark-knowledges\dk-p9-glob-miss.md` | YAML 解析错误: None |
| `dark-knowledges\dk-small-format-error-cascades-to-system-failure.md` | YAML 解析错误: None |
| `dark-knowledges\dk-state-residue-is-the-silent-killer.md` | YAML 解析错误: None |
| `dark-knowledges\dk-tool-chain-naming-is-infrastructure.md` | YAML 解析错误: None |
| `dark-knowledges\dk-yb11-visual-book-reverse.md` | YAML 解析错误: None |
| `dark-knowledges\dk-yb18-small-shop-image-mismatch.md` | YAML 解析错误: None |
| `dark-knowledges\dk-yb19-visual-strategy-price-match.md` | YAML 解析错误: None |
| `dark-knowledges\dk-yb23-ai-pre-screen-three-minutes.md` | YAML 解析错误: None |
| `dark-knowledges\dk-yb30-ecommerce-channel-version.md` | YAML 解析错误: None |
| `dark-knowledges\dk-yitang-business-formula-plus-times-trap.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 34, column 1:
    ---# 业务公式拆解：先切分再拆转化，+ 与 × 写错会误导决策
    ^
could not find expected ':'
  in "<unicode string>", line 36, column 1:
    ## 原始表述
    ^ |
| `decisions\agent-ecosystem-design.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 17, column 1:
    ---# KDO Agent 体系建设方案
    ^
could not find expected ':'
  in "<unicode string>", line 19, column 1:
    > 状态：**待欧阳锋裁决**。三个核心问题未定：agent 数 ... 
    ^ |
| `decisions\huangyaoshi-data-alignment-response.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 28, column 1:
    ---# 黄药师对齐回应：对欧阳锋补充的意见 + 4 个分歧
    ^
could not find expected ':'
  in "<unicode string>", line 30, column 1:
    > 阅读前提：已读欧阳锋的 `ouyangfeng-data-a ... 
    ^ |
| `decisions\kdo-ec-industrialization-migration-proposal.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 35, column 1:
    ---# EC工业化规范 → KDO管线迁移方案（征求意见稿）
    ^
could not find expected ':'
  in "<unicode string>", line 37, column 1:
    > 黄药师起草，请欧阳锋审查，最终由老朱拍板。
    ^ |
| `decisions\labeling-final-consolidation.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 26, column 1:
    ---# 数据标注方案最终汇总 — 三方调研 + 黄药师独立判断
    ^
could not find expected ':'
  in "<unicode string>", line 28, column 1:
    > 汇总人：黄药师
    ^ |
| `decisions\labeling-research-alignment.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 25, column 1:
    ---# 两份标注调研的对齐：黄药师 × 老顽童
    ^
could not find expected ':'
  in "<unicode string>", line 27, column 1:
    ## 路线差异
    ^ |
| `decisions\modeling-capability-for-kdo.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 49, column 1:
    ---# KDO 内容路线决策：建模能力在知识库建设中的应用
    ^
could not find expected ':'
  in "<unicode string>", line 51, column 1:
    > **Burn line**: KDO/wiki 的建设不是整 ... 
    ^ |
| `decisions\plan_20260503_f3e9a2b1-improvement-plan.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 21, column 1:
    ---# Improvement Plan plan_20260 ... 
    ^
could not find expected ':'
  in "<unicode string>", line 23, column 1:
    ## 来源
    ^ |
| `decisions\plan_20260621_skill-iteration-standard.md` | 缺少 trust_level |
| `decisions\sprint-6-cli-gap-proposal.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 21, column 1:
    ---# Sprint 6 CLI 缺口修复提案
    ^
could not find expected ':'
  in "<unicode string>", line 23, column 1:
    > **触发**：老顽童飞轮第一圈 6 篇文章的 Feedbac ... 
    ^ |
| `decisions\truman-ai-partner-design-analysis.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 22, column 1:
    ---# Truman AI Partner（阿蕊老师）设计反推
    ^
could not find expected ':'
  in "<unicode string>", line 24, column 1:
    ## 摘要
    ^ |
| `entities\Kimi-月之暗面.md` | YAML 解析错误: None |
| `entities\YC-Y-Combinator.md` | YAML 解析错误: None |
| `entities\一堂.md` | YAML 解析错误: None |
| `entities\紫鲸AI.md` | YAML 解析错误: None |
| `entities\鑫港湾.md` | YAML 解析错误: None |
| `frameworks\ai-complex-communication.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 22, column 1:
    ---# AI 辅助复杂职场沟通：角色扮演、攻防演练与受众适配
    ^
could not find expected ':'
  in "<unicode string>", line 24, column 1:
    > 来源：听脑录音 5641781 + 公开信源六层交叉验证  
    ^ |
| `frameworks\beverage-foodservice-channel.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 26, column 1:
    ---# 餐饮渠道饮料开发：草本浓缩饮品的渠道-产品-工艺框架
    ^
could not find expected ':'
  in "<unicode string>", line 28, column 1:
    > 来源：听脑录音 3305831/3222718/284232 ... 
    ^ |
| `frameworks\business-formula-to-kdo-card-quality.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 43, column 1:
    ---# 业务公式 ABC → KDO 卡片质量
    ^
could not find expected ':'
  in "<unicode string>", line 45, column 1:
    > **Burn line**: GMV = 线索×转化×客单价 ... 
    ^ |
| `frameworks\concept-maister-trusted-advisor.md` | YAML 解析错误: None |
| `frameworks\concept-mckinsey-7s.md` | YAML 解析错误: None |
| `frameworks\concept-mckinsey-hypothesis-driven.md` | YAML 解析错误: None |
| `frameworks\framework-strategy-basics-03-layout.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 13, column 1:
    "[[tool-strategy-three-horizons]]"
    ^
could not find expected ':'
  in "<unicode string>", line 13, column 35:
    "[[tool-strategy-three-horizons]]"
                                      ^ |
| `frameworks\framework-strategy-basics-05-change.md` | id (framework-strategy-basics-04-system) 与文件名 (framework-strategy-basics-05-change) 不一致 |
| `frameworks\framework-yitang-research-quality-gate.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    id: framework-yitang-research-qu ... 
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 21, column 1:
    - "[[concept-harness-scoring-anc ... 
    ^ |
| `frameworks\model-quality-four-levels.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 38, column 1:
    ---# 模型可信度四层标准 + 千人广场模型
    ^
could not find expected ':'
  in "<unicode string>", line 40, column 1:
    > **Burn line**: 科学是靠反例驱动的。我们建模型 ... 
    ^ |
| `frameworks\modeling-to-kdo-toolchain.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 45, column 1:
    ---# 建模三段论 → KDO 工具链映射
    ^
could not find expected ':'
  in "<unicode string>", line 47, column 1:
    > **Burn line**: 建模不是抽象概念——每个阶段都 ... 
    ^ |
| `frameworks\sales-pitch-bias-patterns.md` | YAML 解析错误: None |
| `frameworks\smart-device-foodservice-automation.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 25, column 1:
    ---# 智能设备外卖对接：无人零售接入美团/饿了么的技术与商业模式
    ^
could not find expected ':'
  in "<unicode string>", line 27, column 1:
    > 来源：听脑录音 6009986 + 公开信源六层交叉验证  
    ^ |
| `frameworks\yt-business-formula-business-pattern-selector.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 46, column 1:
    ---# 业务公式商业模式选型框架：单次成交型 vs 持续复购型
    ^
could not find expected ':'
  in "<unicode string>", line 48, column 1:
    > 一堂业务公式拆解培训中的“前置选型器”：不要一上来就拆 `G ... 
    ^ |
| `frameworks\yt-business-formula-qualitative-metrics-library.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 37, column 1:
    ---# 业务公式定性参数行为化指标库
    ^
could not find expected ':'
  in "<unicode string>", line 39, column 1:
    > 业务公式拆到 L3-L4 时，会出现大量定性参数（如信任度、 ... 
    ^ |
| `frameworks\yt-decision-abcd-model.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 24, column 1:
    ---# 一堂·关键假设ABCD模型
    ^
could not find expected ':'
  in "<unicode string>", line 28, column 1:
    ## 核心定义
    ^ |
| `frameworks\yt-tob-barriers.md` | source_refs 为空 |
| `frameworks\yt-tob-demand-metrics.md` | source_refs 为空 |
| `frameworks\yt-tob-growth-channel.md` | source_refs 为空 |
| `frameworks\yt-tob-solution-model.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 45, column 1:
    ---# To B 解决方案类型矩阵
    ^
could not find expected ':'
  in "<unicode string>", line 47, column 1:
    > "To B 业务不存在唯一的标准答案，关键是把业务按多个维度 ... 
    ^ |
| `frameworks\yt-tob-unit-model.md` | source_refs 为空 |
| `frameworks\yt-unit-model-ladder.md` | YAML 解析错误: None |
| `frameworks\yt-unit-model-overview.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 42, column 1:
    ---## Reusable Knowledge
    ^
could not find expected ':'
  in "<unicode string>", line 44, column 1:
    ### 核心定义
    ^ |
| `projects\互联网医院项目.md` | YAML 解析错误: None |
| `projects\诊所O2O项目.md` | YAML 解析错误: None |
| `projects\鑫港湾HIS项目.md` | YAML 解析错误: None |
| `systems\agent-external-brain-design.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 17, column 1:
    ---# Agent 外挂大脑设计
    ^
could not find expected ':'
  in "<unicode string>", line 19, column 1:
    > **一句话**：在项目根目录下扔三个 Markdown 文件 ... 
    ^ |
| `systems\agent-native-card-design.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 18, column 1:
    ---# Agent 原生知识卡设计规范 v2
    ^
could not find expected ':'
  in "<unicode string>", line 20, column 1:
    ## 定位
    ^ |
| `systems\graph-rag-retrieval-layer.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 22, column 1:
    ---# Graph RAG 检索层技术说明
    ^
could not find expected ':'
  in "<unicode string>", line 24, column 1:
    > **实际实现：LightRAG（图 + 向量混合检索）**
    ^ |
| `systems\kdo-batch-produce-req014.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 20, column 1:
    ---# REQ-014 批量 Produce 12 篇 Enr ... 
    ^
could not find expected ':'
  in "<unicode string>", line 22, column 1:
    > 将 12 篇已 enrich 但尚未 produce 的 w ... 
    ^ |
| `systems\kdo-protocol.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 24, column 1:
    ---# KDO Protocol — AI-Agent Ope ... 
    ^
could not find expected ':'
  in "<unicode string>", line 26, column 1:
    ## Core Points
    ^ |
| `systems\workflow-knowledge-collision.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 30, column 1:
    ---# 知识碰撞工作流：产出前先碰撞知识库
    ^
could not find expected ':'
  in "<unicode string>", line 32, column 1:
    > 核心原则：在产出之前，先拿当前问题去碰撞知识库里的已有框架。 ... 
    ^ |
| `tools\concept-toyota-5-whys.md` | YAML 解析错误: None |
| `tools\skill-mckinsey-hypothesis-driven-workflow.md` | YAML 解析错误: None |
| `tools\smart-medicine-cabinet-financial-model.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 41, column 1:
    ---# 智能药柜单点财务模型与回本测算表
    ^
could not find expected ':'
  in "<unicode string>", line 43, column 1:
    > **核心定位**：药柜推广的经济可行性取决于**点位质量 > ... 
    ^ |
| `tools\smart-medicine-cabinet-fraud-detection.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 38, column 1:
    ---# 智能药柜/智慧药房招商骗局识别清单
    ^
could not find expected ':'
  in "<unicode string>", line 40, column 1:
    > **核心定位**：智能药柜/智慧药房招商领域存在典型骗局模式 ... 
    ^ |
| `tools\tool-ai-skill-engineering-guide.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 45, column 1:
    ---# 高阶 AI Skill 工程指南：用 AI 辅助封装高 ... 
    ^
could not find expected ':'
  in "<unicode string>", line 47, column 1:
    > 来源：一堂建模能力培训（Truman）口述稿 | 背景：为封 ... 
    ^ |
| `tools\tool-clinic-cabinet-legal-contract-guide.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 20, column 1:
    ------
    ^
could not find expected ':'
  in "<unicode string>", line 22, column 1:
    ## Purpose
    ^ |
| `tools\tool-clinic-medical-shortvideo-compliance.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 20, column 1:
    ------
    ^
could not find expected ':'
  in "<unicode string>", line 22, column 1:
    ## Purpose
    ^ |
| `tools\tool-demand-iceberg-l1-user.md` | YAML 解析错误: None |
| `tools\tool-demand-iceberg-l2-scenario.md` | YAML 解析错误: None |
| `tools\tool-demand-iceberg-l3-core-job.md` | YAML 解析错误: None |
| `tools\tool-demand-iceberg-l4-job-map.md` | YAML 解析错误: None |
| `tools\tool-demand-iceberg-l5-forces.md` | YAML 解析错误: None |
| `tools\tool-demand-iceberg-l6-hypothesis.md` | YAML 解析错误: None |
| `tools\tool-smart-medicine-cabinet-compliance-checklist.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 19, column 1:
    ------
    ^
could not find expected ':'
  in "<unicode string>", line 21, column 1:
    ## Purpose
    ^ |
| `tools\tool-smart-medicine-cabinet-site-selection-guide.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 22, column 1:
    ------
    ^
could not find expected ':'
  in "<unicode string>", line 24, column 1:
    ## Purpose
    ^ |
| `tools\tool-strategy-activity-scope.md` | YAML 解析错误: None |
| `tools\tool-strategy-control-points.md` | YAML 解析错误: None |
| `tools\tool-strategy-risk-management.md` | YAML 解析错误: None |
| `tools\tool-strategy-value-capture.md` | YAML 解析错误: None |
| `tools\tool-strategy-value-proposition.md` | YAML 解析错误: None |
| `tools\yt-pitch-metaphor.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 35, column 1:
    ---# 讲香·比喻化
    ^
could not find expected ':'
  in "<unicode string>", line 37, column 1:
    > 十指模型右手第一指——向上抽象。用已知解释未知，帮用户建立一 ... 
    ^ |
| `tools\yt-pitch-quantification.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 34, column 1:
    ---# 讲香·数字化
    ^
could not find expected ':'
  in "<unicode string>", line 36, column 1:
    > 十指模型左手第三指——向下具象。客观的数字让用户默认「这就是 ... 
    ^ |
| `tools\yt-pitch-storytelling.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 36, column 1:
    ---# 讲香·故事化
    ^
could not find expected ':'
  in "<unicode string>", line 38, column 1:
    > 十指模型左手第四指——向下具象。一讲故事用户耳朵就支棱起来— ... 
    ^ |
| `tools\yt-tob-customer-sabc.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 47, column 1:
    ---# To B 客户 SABC 自定义切分法
    ^
could not find expected ':'
  in "<unicode string>", line 49, column 1:
    > 头部/腰部/腿部只是极简经验模型，真正有效的客户分层必须基于 ... 
    ^ |
| `tools\yt-tool-business-formula-metrics-checklist.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 32, column 1:
    ---# 业务公式数据埋点设计清单
    ^
could not find expected ':'
  in "<unicode string>", line 34, column 1:
    > 业务公式拆到 L3-L4 后，每个定性参数都需要 3-5 个 ... 
    ^ |

---

## P1 修复问题清单

| 文件 | P1 问题 |
|---|---|
| `cases\case-candy-problem-os-vpn.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-demand-financial-literacy.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-demand-milkshake-jtbd.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-demand-pharma-bigdata.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-demand-restaurant-hiring.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-demand-rural-5g.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-demand-silver-parenting.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-doris-beauty-ecommerce-channel.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-doris-catering-chain-benchmark.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-doris-crossborder-ecommerce-opportunity.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-doris-grab-industry-cognition.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-doris-outbound-travel-community.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-liutao-douyin-team-leader-9m.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-liutao-electric-bike-localization.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-neworiental-prospectus-marketing.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-popmart-prospectus-pricing.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-proya-betaine-skincare-benchmark.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-cool-boiled-water.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-edward-jones.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-fangte-disney.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-lekai-film.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-li-ka-shing.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-longzhong-plan.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-practice-10-turnaround.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-practice-11-third-place.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-practice-12-zero-loss.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-practice-ranpeng-crossborder.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-practice-ranpeng-milk-powder.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-shell-oil.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-wuxi-suntech.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-xiaobear.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-ai-time-management-coach.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-beauty-device-overseas-sales.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-competitor-pricing-intelligence.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-consumer-offline-channel-decision.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-doorstep-nail-service-context.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-elderly-home-roleplay.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-fake-interview-intelligence.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-hardware-factory-photo.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-jtbd-story-formula.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-luckin-field-research.md` | confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-mahjong-machine-fake-order.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-pet-fostering-user-research.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-sanjieke-benchmark-failure.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-ski-project-user-as-expert.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-supplier-security-guard.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-track-selection-research.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-travel-receipt-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-zhanglan-amusement-park-undercover.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-zhanglei-furniture-overseas-market-selection.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-zhanglei-nursing-home-family.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\concept-candy-ai-as-collaborator.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `concepts\concept-harness-cattle-not-pets.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\concept-harness-scoring-anchors.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `concepts\concept-strategy-evolution-cycle.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\concept-strategy-framework-landscape.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\concept-yitang-ai-research-10-assumptions.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `concepts\concept-yitang-ideal-research-goal.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\concept-yitang-research-facts-first.md` | dangling 链接: dk-yitang-research-expert-trap, dk-yitang-research-expert-trap |
| `concepts\concept-yitang-research-objective.md` | dangling 链接: tool-yitang-research-checklist, case-yitang-haidilao-service-research, tool-yitang-research-checklist, dk-yitang-research-novice-vs-veteran, case-yitang-haidilao-service-research |
| `concepts\concept-yitang-research-scope.md` | dangling 链接: tool-yitang-research-checklist, tool-yitang-research-checklist, dk-yitang-research-novice-vs-veteran, dk-yitang-research-cost-match, dk-yitang-research-novice-vs-veteran |
| `dark-knowledges\dk-demand-feature-stacking.md` | type 值异常: dark_knowledge; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-demand-hidden-need.md` | type 值异常: dark_knowledge; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-demand-misjudgment-rate.md` | type 值异常: dark_knowledge; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-demand-pitfall-dialer.md` | type 值异常: dark_knowledge; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-demand-pitfall-financial-literacy.md` | type 值异常: dark_knowledge; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-demand-pitfall-indonesia-insurance.md` | type 值异常: dark_knowledge; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-demand-pitfall-restaurant-hiring.md` | type 值异常: dark_knowledge; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-demand-pitfall-rural-5g.md` | type 值异常: dark_knowledge; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-demand-pitfall-tier4-housekeeping.md` | type 值异常: dark_knowledge; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-demand-pitfall-travel-agent.md` | type 值异常: dark_knowledge; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-demand-premature-solution.md` | type 值异常: dark_knowledge; confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-demand-switching-cost.md` | type 值异常: dark_knowledge; confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-strategy-01-not-goal-setting.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-strategy-02-three-paradoxes.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-strategy-03-advantage-temporary.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-strategy-04-consulting-trap.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-strategy-05-positioning-trap.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-strategy-06-dividend-to-strategy.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-strategy-07-strategy-vs-dividend.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-strategy-08-not-local-optimum.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-strategy-consulting-jokes.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-strategy-essence-four-elements.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-strategy-longzhong-four-failures.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-strategy-three-must-do-moments.md` | trust_level=high 但 source 仅 1 个 |
| `decisions\plan_20260621_domain-index-infrastructure.md` | status 值异常: approved; dangling 链接: check-source-refs.py, track-production-progress.py |
| `decisions\plan_20260621_skill-iteration-standard.md` | status 值异常: approved |
| `dk\dk-yitang-ai-research-prompt-craft.md` | type 值异常: dark_knowledge |
| `dk\dk-yitang-cross-case-pattern-failure-premium.md` | type 值异常: dark_knowledge |
| `dk\dk-yitang-cross-case-pattern-identity-escalation.md` | type 值异常: dark_knowledge |
| `dk\dk-yitang-digging-belief.md` | type 值异常: dark_knowledge; trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-expert-interview-5-traps.md` | type 值异常: dark_knowledge; trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-public-info-is-enough.md` | type 值异常: dark_knowledge; trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-research-ai-hallucination.md` | type 值异常: dark_knowledge; confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-research-best-practice-first.md` | type 值异常: dark_knowledge |
| `dk\dk-yitang-research-cost-value-match.md` | type 值异常: dark_knowledge; trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-research-cross-validation-cost.md` | type 值异常: dark_knowledge |
| `dk\dk-yitang-research-desperate-effort.md` | type 值异常: dark_knowledge; trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-research-goal-before-efficiency.md` | type 值异常: dark_knowledge; trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-research-question-quality.md` | type 值异常: dark_knowledge |
| `dk\dk-yitang-research-scale-vs-depth.md` | type 值异常: dark_knowledge |
| `dk\dk-yitang-research-source-freshness.md` | type 值异常: dark_knowledge; trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-research-starter-vs-veteran.md` | type 值异常: dark_knowledge; confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-survivor-bias-in-research.md` | type 值异常: dark_knowledge; confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `entities\七件事集团.md` | confidence=0.9 但 source 仅 1 个 |
| `frameworks\framework-candy-transcript-workflow.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-demand-opportunity-spectrum.md` | trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-demand-usp-model.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-multi-agent-research-architecture.md` | dangling 链接: concepts/kimi-深度调研集群方法论-deep-research-swarm |
| `frameworks\framework-ouyangfeng-review-methodology.md` | status=draft 但 confidence=0.88 |
| `frameworks\framework-strategy-basics-01-core.md` | trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-strategy-basics-02-insight.md` | trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-strategy-basics-04-system.md` | trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-strategy-basics-05-change.md` | trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-yitang-expert-interview-10steps.md` | dangling 链接: tool-yitang-linkedin-expert, tool-yitang-linkedin-expert |
| `frameworks\framework-yitang-high-level-execution.md` | dangling 链接: tool-yitang-research-acquisition, tool-yitang-research-reasoning, tool-yitang-research-reasoning, tool-yitang-research-acquisition |
| `frameworks\framework-yitang-high-level-plan.md` | dangling 链接: tool-yitang-research-checklist, tool-yitang-research-checklist |
| `frameworks\framework-yitang-iterative-recursive-digging.md` | dangling 链接: dk-yitang-research-determination, dk-yitang-research-survivorship-bias, dk-yitang-research-novice-vs-veteran, dk-yitang-research-novice-vs-veteran, dk-yitang-research-survivorship-bias |
| `frameworks\framework-yitang-oscar-research.md` | dangling 链接: tool-yitang-research-checklist, tool-yitang-research-acquisition, tool-yitang-research-reasoning, tool-yitang-research-reasoning, tool-yitang-research-checklist |
| `frameworks\framework-yitang-research-weapon-supplement-2026.md` | status=draft 但 confidence=0.88 |
| `frameworks\framework-yitang-six-layer-cross-validation.md` | dangling 链接: case-yitang-haidilao-service-research, tool-yitang-research-facts-first, case-yitang-haidilao-service-research, dk-yitang-research-expert-trap, tool-yitang-research-facts-first |
| `frameworks\yt-tob-barriers.md` | trust_level=high 但 source 仅 0 个 |
| `prompt-methodology\prompt-demand-ai-coach.md` | type 值异常: prompt-methodology; confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-agent-research-pipeline.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-agent-research-supervisor.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-agent-research-swarm.md` | dangling 链接: concepts/kimi-深度调研集群方法论-deep-research-swarm |
| `tools\tool-candy-oral-polish.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-candy-positioning-canvas.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-ci-define-phase.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-ci-implement-phase.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-agent-auto-verify.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-agent-case-match.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-agent-l4-case-match.md` | dangling 链接: tool-demand-agent-l3-multi-hypothesis |
| `tools\tool-demand-agent-multi-hypothesis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-agent-signal-substitute.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-assessment-triangle.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-blindspot-checklist.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-four-forces.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-report-template.md` | dangling 链接: demand-analysis-synthetic, five-step-barrier |
| `tools\tool-devils-advocacy.md` | dangling 链接: concept-半肥猫-ai-research-validation; confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-harness-adversarial-tester.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-indicators-signposts.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-key-assumptions-check.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-prompt-iceberg-demand-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-prompt-jtbd-scenario-coach.md` | dangling 链接: framework-yitang-jtbd-theory; confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-prompt-usp-demand-analysis.md` | dangling 链接: framework-yitang-usp-model, framework-yitang-jtbd-theory |
| `tools\tool-prompt-usp-quick-scan.md` | dangling 链接: framework-yitang-usp-model; trust_level=high 但 source 仅 1 个 |
| `tools\tool-red-team-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-12-word-test.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-business-summary.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-capability-matrix.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-competition-traps.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-fishbone.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-five-see-three-set.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-four-layers.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-four-moves.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-gap-analysis.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-map.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-nine-problems.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-pareto.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-sentence-formula.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-three-horizons.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-ai-assisted-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-ai-assisted-organize.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-ai-monitoring-alert.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-ai-report-drafting.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-amazon-bestseller.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-anonymous-product-testing.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-app-store-data.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-app-store-review.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-baidu-index.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-behavioral-observation.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-bidding-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-bp-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-business-registration-check.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-channel-agent-interview.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-comparable-company-selection.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-competitor-financial-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-conference-networking.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-consulting-business-research.md` | dangling 链接: tool-yitang-expert-interview-10steps |
| `tools\tool-yitang-consumer-goods-research.md` | dangling 链接: tool-yitang-product-reverse-engineering |
| `tools\tool-yitang-court-record-search.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-database-index.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-douyin-data.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-employee-directory.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-executive-speech-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-expert-network-platform.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-financing-intelligence.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-forum-data.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-government-data-search.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-hardware-product-disassembly.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-in-home-experience-research.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-industry-report-search.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-ipo-annual-report-cheat-sheet.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-news-monitoring.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-online-product-experience.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-partner-data-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-patent-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-pc-web-data.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-people-network-database.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-product-full-experience.md` | dangling 链接: case-yitang-haidilao-service-research, tool-yitang-offline-product-experience, tool-yitang-offline-product-experience, case-yitang-haidilao-service-research |
| `tools\tool-yitang-public-information-research.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-public-sentiment-research.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-recruit-user-interview.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-research-best-practice.md` | dangling 链接: case-yitang-haidilao-service-research, dk-yitang-research-survivorship-bias, dk-yitang-research-novice-vs-veteran, case-yitang-haidilao-service-research, dk-yitang-research-novice-vs-veteran |
| `tools\tool-yitang-research-company-disassembly.md` | dangling 链接: case-yitang-haidilao-service-research, dk-yitang-research-survivorship-bias, dk-yitang-research-novice-vs-veteran, case-yitang-haidilao-service-research, dk-yitang-research-novice-vs-veteran |
| `tools\tool-yitang-research-competitive-quadrant.md` | dangling 链接: case-yitang-haidilao-service-research, dk-yitang-research-novice-vs-veteran, case-yitang-haidilao-service-research, dk-yitang-research-novice-vs-veteran |
| `tools\tool-yitang-research-competitor-tracking.md` | dangling 链接: case-yitang-haidilao-service-research, dk-yitang-research-novice-vs-veteran, case-yitang-haidilao-service-research, dk-yitang-research-novice-vs-veteran |
| `tools\tool-yitang-research-cross-validation.md` | dangling 链接: tool-yitang-research-facts-first, dk-yitang-research-expert-trap, dk-yitang-research-expert-trap, tool-yitang-research-facts-first |
| `tools\tool-yitang-research-deep-attribution.md` | dangling 链接: dk-yitang-research-novice-vs-veteran, dk-yitang-research-determination, dk-yitang-research-novice-vs-veteran, dk-yitang-research-determination |
| `tools\tool-yitang-research-exhaust-means.md` | dangling 链接: dk-yitang-research-novice-vs-veteran, dk-yitang-research-novice-vs-veteran |
| `tools\tool-yitang-research-follow-map.md` | dangling 链接: case-yitang-haidilao-service-research, dk-yitang-research-survivorship-bias, dk-yitang-research-novice-vs-veteran, case-yitang-haidilao-service-research, dk-yitang-research-novice-vs-veteran |
| `tools\tool-yitang-research-industry-scan.md` | dangling 链接: dk-yitang-research-novice-vs-veteran, dk-yitang-research-novice-vs-veteran |
| `tools\tool-yitang-research-intelligence-map-in-hand.md` | dangling 链接: dk-yitang-research-novice-vs-veteran, dk-yitang-research-novice-vs-veteran |
| `tools\tool-yitang-research-normalize-summary.md` | dangling 链接: dk-yitang-research-novice-vs-veteran, dk-yitang-research-novice-vs-veteran |
| `tools\tool-yitang-research-quantitative-modeling.md` | dangling 链接: tool-yitang-research-facts-first, dk-yitang-research-expert-trap, dk-yitang-research-expert-trap, tool-yitang-research-facts-first |
| `tools\tool-yitang-research-single-point-sniper.md` | dangling 链接: dk-yitang-research-novice-vs-veteran, dk-yitang-research-determination, tool-yitang-research-hypothesis-test, tool-yitang-research-hypothesis-test, dk-yitang-research-novice-vs-veteran |
| `tools\tool-yitang-research-two-dimensional-positioning.md` | dangling 链接: case-yitang-haidilao-service-research, dk-yitang-research-novice-vs-veteran, case-yitang-haidilao-service-research, dk-yitang-research-novice-vs-veteran |
| `tools\tool-yitang-research-unit-model.md` | dangling 链接: case-yitang-haidilao-service-research, dk-yitang-research-novice-vs-veteran, dk-yitang-research-cost-match, case-yitang-haidilao-service-research, dk-yitang-research-novice-vs-veteran |
| `tools\tool-yitang-research-validate-assumption.md` | dangling 链接: tool-yitang-research-hypothesis-test, case-yitang-haidilao-service-research, dk-yitang-research-novice-vs-veteran, tool-yitang-research-hypothesis-test, case-yitang-haidilao-service-research |
| `tools\tool-yitang-reverse-data-analysis.md` | dangling 链接: tool-yitang-web-crawler-research, tool-yitang-offline-store-reconnaissance, tool-yitang-id-increment-analysis, tool-yitang-product-reverse-engineering, tool-yitang-id-increment-analysis |
| `tools\tool-yitang-review-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-securities-research.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-shareholder-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-signup-statistics.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-social-media-interview.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-social-media-monitoring.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-stock-data.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-supplier-interview.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-supply-chain-research.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-tech-project-research.md` | dangling 链接: tool-yitang-product-reverse-engineering |
| `tools\tool-yitang-trend-data.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-weapon-media-search.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-weapon-third-party-database.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-wechat-group-infiltration.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-wechat-index.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-weibo-index.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-xiaohongshu-data.md` | trust_level=high 但 source 仅 1 个 |

---

## 使用说明

运行门禁脚本：
```bash
python 90_control/scripts/kcard-quality-gate.py
```

P0 问题必须在卡片进入 enriched/reviewed/stable 前修复。
P1 问题应在发布前修复。