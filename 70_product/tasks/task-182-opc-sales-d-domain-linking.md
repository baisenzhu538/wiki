---
id: task_20260713_wangyuyan-opc-sales-d-domain-linking
assignee: kimi
status: pending_review
updated_at: '2026-07-13T20:11:07.788081+00:00'
---

# #182 OPC 销售域×D 域回链

## 背景

老朱 7-13 裁定三层架构：D 域=场景无关的方法论底座；OPC 销售域（27 工具/6 子域/op-mastercard，#47/#49 建）=销售场景应用层。销售域建设时 D 域不存在，33 张卡方法论隐含无底座引用。D 域卡建完后须回链。D 域不只服务销售——运营/市场/产品转化率场景复用同一底座，应用层各自实例化。

## 产出

`30_wiki/02_业务域/应用/opc销售域/` 33 张卡补 D 域引用：

1. **映射表先行**（第一步产出，交王语嫣过目后批量执行）：
   - 开场白/破冰类工具 → `framework-一堂-十指模型` + `tool-一堂-触点-tools`
   - 异议处理/议价类工具 → `framework-一堂-阻力方法论` + 12 阻力卡 + `tool-一堂-阻力消除12策小抄`
   - 客户开发子域（鱼塘/甩鱼钩）→ 触点篇三挖法+五大范式（术语对照：甩鱼钩≈挖触点）
   - 转化成交子域（12 计/成交场景）→ 12 阻力过筛 + 成交四招
   - 管理运营子域（销冠段位/培训体系）→ 销冠能力论 + `framework-一堂-动力三曲线` 分数线
   - op-mastercard → `framework-一堂-转化率总纲` + digest
2. 每卡只加引用不重写正文；source_refs 遵守铁律（路径+L行号，括号备注挪出引用条目）
3. 销售域 digest/index 不动（自成体系，D 域引用是增强不是合并）

## 边界

- 两域保持独立命名空间（op- vs 一堂-），不做卡片合并——应用层实例与方法论底座各司其职
- 依赖 D 域卡建完（#169-171+#174）；映射表可先行动工

## 流程

流程A 直通。门禁：`kdo pre-submit -f` 批量过。扫窗申报=改动清单+映射表。


---

## 映射表（终稿 · 王语嫣裁定后）

执行范围：30_wiki 正式卡 22 张（原 28 张 − .agent/prompts 独有 6 张随 #186 入库）。
③层方法论卡按"一句话测试"逐条写理由；成交四招 grep 未找到成卡，按裁定映射到 `tool-一堂-阻力消除12策小抄`。

### ① op-mastercard + 助手

| # | 文件 | 新增 D 域 related | 理由 |
|---:|:---|:---|:---|
| 1 | `personal-os/opc-ai-sales-agent-architecture.md` | `framework-一堂-转化率黑客-总纲`、`conversion-rate-domain-digest` | op-mastercard 接总纲+digest |
| 2 | `tools/tool-opc-sales-dialogue-assistant.md` | `framework-一堂-转化率黑客-总纲`、`conversion-rate-domain-digest` | 助手已有 D 域 12 阻力/12 策/动力三曲线，补总纲+digest 完成入口口径 |

### ② agent-spec 应用卡

| # | 文件 | 场景 | 新增 D 域 related | 理由 |
|---:|:---|:---|:---|:---|
| 3 | `tool-agent-spec-yitang-opening-3min.md` | 开场白 | `framework-一堂-十指模型`、`framework-一堂-触点本质论` | 开场是首次触点，十指模型管表达、触点本质论管接触机会点 |
| 4 | `tool-agent-spec-yitang-objection-handler.md` | 异议 | `framework-一堂-阻力方法论骨架`、`framework-一堂-12种阻力总表`、`tool-一堂-阻力消除12策小抄` | 异议=阻力显形，需方法论骨架+12 阻力识别+12 策消除 |
| 5 | `tool-agent-spec-yitang-customer-segmentation.md` | 客户开发 | `tool-一堂-五种挖触点`、`framework-一堂-12触点SABC分级` | 分层决定资源投向哪些触点，触点工具是下游执行层 |
| 6 | `tool-agent-spec-yitang-value-proposition.md` | 卖点提炼 | `framework-一堂-动力三曲线`、`tool-一堂-FAB说服法`、`framework-一堂-十指模型` | 卖点=构建购买动力，FAB/三曲线是动力根，十指模型管表达 |
| 7 | `tool-agent-spec-yitang-sales-process-tracker.md` | 过程追踪 | `framework-一堂-转化率提升六步法`、`framework-一堂-12种阻力总表` | 阶段卡点识别需六步法框架+12 阻力过筛 |
| 8 | `tool-agent-spec-yitang-sales-performance-monitor.md` | 业绩监控 | `framework-一堂-动力三曲线`、`framework-一堂-转化率提升六步法` | 业绩=目标动机+过程拆解，分别对应动力三曲线与六步法 |
| 9 | `tool-agent-spec-yitang-self-motivation.md` | 自我驱动 | `framework-一堂-动力三曲线`、`tool-一堂-心理激励优先机制` | 自我驱动即个人动力维持，动力三曲线+心理激励优先 |

### ③ 方法论卡（按"一句话测试"裁定）

| # | 文件 | 裁定 | 新增 D 域 related | 一句话理由 |
|---:|:---|:---:|:---|:---|
| 10 | `framework-yitang-scientific-sales-five-step.md` | ❌ 不加 | — | 五步法是一堂销售管理课总纲，D 域转化率黑客是其微观效率补充而非理论根；加总纲会模糊两课边界 |
| 11 | `framework-yitang-sales-incentive-6d.md` | ✅ 加 | `framework-一堂-动力三曲线` | 六维激励设计团队持续行动动力，动力三曲线是"心理激励优先、分阶段侧重"的理论根 |
| 12 | `tool-yitang-sales-toolkit-radar.md` | ❌ 不加 | — | 工具箱六维雷达图评估销售组织资产成熟度，十指模型只管表达侧，不能作为其理论根 |
| 13 | `tool-yitang-sales-process-decomposition.md` | ✅ 加 | `framework-一堂-转化率提升六步法` | 销售过程拆解"路径→阶段→动作"与六步法"拆解/加法/减法/讲香/组合/制作"同构，六步法是其转化节点优化理论根 |
| 14 | `tool-yitang-value-proposition-4step.md` | ✅ 加 | `framework-一堂-动力三曲线`、`tool-一堂-FAB说服法` | 卖点提炼本质是构建购买动力，FAB/名利权情/影响力三曲线是动力分层理论根，FAB 说服法是落地工具根 |
| 15 | `tool-yitang-sales-performance-management.md` | ✅ 加 | `framework-一堂-转化率提升六步法`、`framework-一堂-动力三曲线` | 业绩管理"拆目标→定策略→追过程"是六步法在销售管理中的落地，目标动机分析需动力三曲线 |
| 16 | `tool-yitang-customer-segmentation-4step.md` | ❌ 不加 | — | 用户分层是客户开发前置判断（值不值得跟），触点工具是下游执行层，不能作为理论根；D 域无直接对应卡 |
| 17 | `tool-yitang-payment-collection-playbook.md` | ✅ 加 | `framework-一堂-12种阻力总表`、`tool-一堂-阻力消除12策小抄` | 回款/履约拖延本质是"还不急/有风险/不靠谱"等阻力，12 阻力总表识别、12 策小抄消除，是其理论根 |
| 18 | `tool-yitang-daily-weekly-meeting-hosting.md` | ❌ 不加 | — | 日会/周会是销售管理节拍器，与六步法仅有"追过程"形似，会议 SOP 不是转化率方法论的理论根 |

### ④ 案例 + dk

| # | 文件 | 新增 D 域 related | 理由 |
|---:|:---|:---|:---|
| 19 | `cases/case-yitang-sales-transformation-jubensha-saas.md` | `case-一堂-阻力篇案例库`、`case-一堂-触点篇案例库` | 案例互链：剧本杀 SaaS 改造同时涉及触点设计与阻力消除 |
| 20 | `cases/case-yitang-sales-transformation-tuliaogongsi.md` | `case-一堂-触点篇案例库`、`case-一堂-组合篇案例库` | 案例互链：涂料公司分层转型是触点工业化+组合策略案例 |
| 21 | `cases/case-yitang-sales-transformation-meirongyuan.md` | `case-一堂-触点篇案例库`、`case-一堂-动力篇案例库` | 案例互链：美容院改造涉及触点响应与激励动力对齐 |
| 22 | `dark-knowledges/dk-yitang-sales-common-pitfalls.md` | `framework-一堂-12种阻力总表`、`framework-一堂-转化率提升六步法` | dk 是观察者视角反模式提炼，根在 D 域 12 阻力识别与六步法落地 |

---

## 执行报告

### 变更范围

- **正向改动**：22 张 OPC 销售域正式卡追加 D 域 related 引用
- **反向闭合**：17 张 D 域目标卡追加 OPC 销售域卡回链（保证 related 双向闭合，符合 F2 关系型边规则）
- **附带修复**：`tool-yitang-payment-collection-playbook.md` 原文件带 UTF-8 BOM，kdo_lint 此前无法解析其 frontmatter；本次去除 BOM 后暴露 6 条既有 related 缺回链，已补双向闭合
- **未改动**：销售域 digest/index、`.agent/prompts/` 目录（6 张 prompts 独有 agent-spec 随 #186 入库时统一处理）

### 文件清单

- 30_wiki 正向文件 18 张：
  - personal-os/opc-ai-sales-agent-architecture.md
  - tools/tool-opc-sales-dialogue-assistant.md
  - tools/tool-agent-spec-yitang-{opening-3min,objection-handler,customer-segmentation,value-proposition,sales-process-tracker,sales-performance-monitor,self-motivation}.md
  - frameworks/framework-yitang-sales-incentive-6d.md
  - tools/tool-yitang-{sales-process-decomposition,value-proposition-4step,sales-performance-management,payment-collection-playbook}.md
  - cases/case-yitang-sales-transformation-{jubensha-saas,tuliaogongsi,meirongyuan}.md
  - dark-knowledges/dk-yitang-sales-common-pitfalls.md
- 30_wiki 反向闭合文件 17 张：
  - domains/conversion-rate-domain-digest.md
  - frameworks/framework-一堂-{转化率黑客-总纲,十指模型,触点本质论,阻力方法论骨架,12种阻力总表,12触点SABC分级,动力三曲线,转化率提升六步法}.md
  - tools/tool-一堂-{阻力消除12策小抄,五种挖触点,FAB说服法,心理激励优先机制}.md
  - cases/case-一堂-{动力篇案例库,阻力篇案例库,触点篇案例库,组合篇案例库}.md
  - tools/tool-yitang-{sales-process-decomposition,sales-performance-management}.md
  - frameworks/framework-yitang-scientific-sales-five-step.md
  - frameworks/framework-yitang-sales-incentive-6d.md
  - dark-knowledges/dk-yitang-sales-common-pitfalls.md
  - tools/tool-opc-sales-dialogue-assistant.md

### 门禁结果

| 检查 | 命令 | 结果 |
|:---|:---|:---|
| 基线 lint | `python 90_control/scripts/kdo_lint.py 30_wiki --baseline` | 4805 条 baseline 已记录 |
| 增量 lint | `python 90_control/scripts/kdo_lint.py 30_wiki --incremental` | ✅ 0 new error |
| pre-submit | `python 90_control/scripts/pre_submit.py --manifest 90_control/.sandbox/182_changed_files.txt` | ✅ 36/36 文件 GATE PASSED |

### 脚本

- `90_control/.sandbox/apply_182_opc_d_domain_links.py`：正向+D 域反向闭合批量脚本
- `90_control/.sandbox/182_changed_files.txt`：本次变更文件清单（pre-submit manifest）

---

## 终审待审

- 状态：待 `queue_transition.py complete` 转 `pending_review`
- 欧阳锋复验建议：抽查 3-5 张卡（建议 opener/dk/payment-collection-playbook）确认 related 双向闭合与 lint 增量
