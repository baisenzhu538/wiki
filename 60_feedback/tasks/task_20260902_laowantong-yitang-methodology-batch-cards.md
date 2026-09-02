---
id: task_20260902_laowantong-yitang-methodology-batch-cards
title: 一堂方法论族卡组 5 件（MUSE 数据包 / 高阶Skill设计指南 / Agent大学设想 / Jovida 双报告 / Eason审计🔴）
seq: 611
status: pending_review
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-02
decision_source: inbox 01:51 批次分诊（diag_20260902_wangyuyan-inbox-batch-42 族B，老朱 0831/0901
  直令高价值素材直接编排产卡）
reviewer: 欧阳锋
source_refs:
- 00_inbox/学习candy合集/数据包：MUSE模型.md
- 00_inbox/学习candy合集/指南：高阶 Skill 设计指南.md
- 00_inbox/学习candy合集/设想：Agent大学——让你的Agent来一堂进修.md
- 00_inbox/学习candy合集/调研：Jovida AI竞争力双三角洞察报告.md
- 00_inbox/学习candy合集/调研：Jovida 深度产品调研报告.md
- 00_inbox/学习candy合集/审计：Eason文化审计与实事求是DataPack.md
related_tasks:
- '#610'
instance: laowantong-kimi
updated_at: '2026-09-02T00:27:29.607819+00:00'
evidence: 60_feedback/tasks/task_20260902_laowantong-yitang-methodology-batch-cards.md
---

# #611 一堂方法论族卡组（老顽童）

## 背景

学习candy合集 9 份新件中的一堂产品/方法论族 5-6 件（=「AI知识管理探索营」开源文档落地件），分诊判高增量。素材全部是整理稿/报告（非口述逐字稿），证据等级=二等整理件，标注来源。

## 任务（5-7 卡候选，最终形态按 W6 三方法定夺）

1. **framework-muse-model**（strategy/kdo）：MUSE 四层（Miracle/Usage/Startup/Evolution）+ E→S→U→M 传导链 + 跨层证据门槛——素材 892 行 DataPack 完整（定义/Schema/评分表/提示词），上位框架级资产
2. **tool-skill-design-advanced**（ai-collaboration/kdo）：高阶 Skill 设计指南——Anthropic 官方 Skill 拆解（七范式/四层模块/红黑线/量化评价），工程密度高，可直接指导 KDO 技能生产
3. **case-agent-university**（strategy）：Agent 大学产品设想——市场四类摸查/7层架构/MVP/商业模式（与 OPT 设想姊妹篇，OPT 体量较小可并入本卡 related 不单独产卡）
4. **case-jovida-double-triangle**（strategy）：Jovida 调研双件合一——事实底稿（创始人张心皓/功能/定价/竞品）+ 双三角框架分析（Human Loop vs Agent Loop/上下文飞轮）；先事实后框架上下篇合一张 case
5. **case-eason-culture-audit + dk-实事求是三问**（kdo 治理域）：AI Agent 价值观违规审计真实事件 + 实事求是方法论（事实三问法/信任等级制）——⚠️ 素材标🔴密级「仅限Truman审阅」：入库按 #322 先例加**传播限制标注**（内部库可用，不外传不发布）；若拿不准边界，产卡前在 todos 问王语嫣

## 验证

- pre-submit 全过；O0 溯源锚点=文件路径+行号
- MUSE 卡注意与 WAIC 顶层思考件（xuchu 同族）互链；Agent 大学卡与 OPT 件互链
- 新卡间互链 + 与 kdo-moc / strategy-domain-digest 挂接

## 六维标签建议（spec v1.6）

- 专业轴：战略 / 产品方法论 / Agent工程 / 组织治理
- 对象轴：AI产品 / Agent / 技能 / 团队
- 性质轴：框架 / 数据包 / 产品设想 / 审计案例
- 经验轴：实战 / 内测 / 复盘
- 受众轴：创业者 / 产品经理 / Agent运营者
- 来源轴：一堂 / Truman知识库 / 内测 / 外部报告（Jovida 调研 Stella）

## 边界

- 原素材不动（00_inbox 只增不删）；Eason 审计卡正文可抽象化（方法论为主，事件细节脱敏）
- 素材为一堂内部文档——全部卡加传播限制口径字段（参照 #596 转述标注同段位）

## 交付

- 5-7 张卡 + 执行报告（含三方法记录+互链实证+传播限制标注清单）
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 611 附执行报告路径）

## 建模方案（老顽童出牌，2026-09-02）

依赖链：`[素材牌] → [边界牌] → [结构牌] → [过程牌] → [质量牌]`

| 牌 | 牌号 | 一句话理由 |
|:--|:--|:--|
| 素材牌 | 组件库#2 先全文扫描再选策略 + L7 先查已有卡再新建 | 9 份合集素材先查重：5/5 主候选已被 #586 批 reviewed 卡覆盖（MUSE/Skill指南/Agent大学/OPT/Jovida），不重建 |
| 边界牌 | #322 传播限制先例 + 任务单边界节 | Eason 审计件🔴「CHO私有·仅限Truman审阅」→ 传播限制标注+正文抽象化脱敏，内部库可用不外传 |
| 结构牌 | 组件库#10 先骨架再填肉 + L8 子卡先写定位 | 增量 2 卡（case+dk）标题下先写定位声明，挂接实事求是族与 kdo 治理域 |
| 过程牌 | L2 全量素材消费 | Eason DataPack 440 行逐字读完；其余 5 件以 #586 reviewed 卡的 source_refs 对账确认同源覆盖 |
| 质量牌 | 组件库#16 先 lint 再 pre-submit + L3 深挖达标 + 自攻击 | 每卡 ≥100 行正文、case 卡带证据表、pre-submit 逐卡过、批后四路自攻击 |

## 执行报告（老顽童，2026-09-02）

**交付物**：
1. `30_wiki/cases/case-yitang-eason-truth-delivery-audit.md`（新增，正文 103+ 行，case）
2. `30_wiki/dark-knowledges/dk-yitang-fact-three-questions-trust-tiers.md`（新增，正文 132+ 行，dk）
3. 反向补链 3 张存量卡：`framework-yitang-shishi-qiushi`（related: null→补 2 链）、`concept-yihang-data-pack-ethics`（+2）、`concept-agent-university`（+2）
4. 本任务单「## 建模方案」节（L1 出牌记录）

**完成内容**：查重先行——任务单 5 主候选经 grep+kdo 检索确认已由 #586 批 reviewed 卡全覆盖：`framework-muse-ai-full-map-v1`（MUSE 数据包，source_refs 同源）、`method-anthropic-skill-design-patterns`（高阶 Skill 设计指南）、`concept-agent-university`（Agent大学）、`framework-lobster-opt-one-person-team`（OPT 姊妹篇已互链）、`case-jovida-ai-life-coach`（Jovida 双报告合一）——按 #610 先例不重建；增量锁定 Eason 审计族 2 卡（🔴密级件，任务单明确授权按 #322 先例处理，边界无拿不准项，未触发问王语嫣）。case 卡含证据表/深挖 L1-L5/六层交叉 L1-L4/双攻击者 Critique/失败模式/KDO 同构映射表；dk 卡含六字段标准节+四方法+封装判断元暗知识+双攻击者 Critique。

**验证**：① pre-submit 两卡 PASS（case 45/100、dk 40/100；各 1 条 #542 概念交叉提示制 WARNING，不拦截，已人工核对：Truman/业务公式/目标管理等引用与权威定义一致，"角色扮演"系通用语非 ai-complex-communication 概念义）；② 互链双向 0 死链（两新卡全部 [[..]] 目标经 find 验证实存，反向补链 3 处）；③ `kdo index --incremental` 至 4177，两新卡可检索；④ 传播限制标注：两新卡 frontmatter source_context + 正文首行双标注（#322/#586 先例格式：内部库可用，禁止外传禁止发布）；⑤ 数字纪律：证据表全标"单一内部文档口径待独立核实"，>80% 复发概率标注为 CHO 估计值；⑥ 自攻击四路执行：🔴0 🟡2（A 逻辑：79/40 分钟算术核验过；B 证据：单一来源已标注；C 完整性：素材消费说明过度声称已修——课程版连续谱/六段位/十大坑归位存量卡，两新卡只落 Agent 适配增量；D 时效：arXiv 2606.04990/CSA ATF 2026 新源可用），🟡 已修复复跑 PASS；⑦ 交付物已入仓 commit d743581cb（主体内容由 08:20 vault 自动备份先行入库，本次提交为后续修订 diff）。

**边界**：原素材 00_inbox 未动；Eason 事件细节按要求抽象化（方法论为主，时间线/段位对照保留结构脱敏呈现）；未触碰其余 5 张 reviewed 存量卡正文（仅概念卡 agent-university 与 data-pack-ethics 加 related 反向链、shishi-qiushi 的 related:null 补 2 链，未改其正文与 reviewed 状态）；WAIC 顶层思考件无独立卡（队列登记口径=并入本族互链），MUSE 卡为 reviewed 存量未改，WAIC 互链留待后续裁决。

**需要谁动作**：欧阳锋终审两新卡（重点：🔴密级件的脱敏口径是否达标、KDO 同构映射表的事实准确性）；如需 WAIC 顶层思考件与 MUSE 卡互链，请终审时一并裁定（涉及改 reviewed 卡，老顽童未动）。

**三方法记录**：①素材消费——Eason DataPack 440 行逐字读完（W1），其余 5 件以 #586 reviewed 卡 source_refs 对账确认同源覆盖，素材消费率口径=增量素材 100%+存量覆盖对账 5/5；②传播限制检查——源文档 L7 明示🔴「CHO 私有—仅限 Truman 审阅」，触发 #322 先例，两卡双标注；③外部对标——WebSearch 命中 arXiv《From Agent Traces to Trust》(2606.04990) 与 CSA《Agentic Trust Framework》，确认"署名真实性/信任分级"与国际前沿同构，无术语冲突（MUSE 不新建不涉及命名冲突）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 2 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
