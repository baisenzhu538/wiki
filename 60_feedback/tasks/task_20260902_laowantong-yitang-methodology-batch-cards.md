---
id: task_20260902_laowantong-yitang-methodology-batch-cards
title: 一堂方法论族卡组 5 件（MUSE 数据包 / 高阶Skill设计指南 / Agent大学设想 / Jovida 双报告 / Eason审计🔴）
seq: 611
status: queued
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-02
decision_source: inbox 01:51 批次分诊（diag_20260902_wangyuyan-inbox-batch-42 族B，老朱 0831/0901 直令高价值素材直接编排产卡）
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
