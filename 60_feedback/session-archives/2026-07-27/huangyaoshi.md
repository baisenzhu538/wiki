---
session_id: huangyaoshi-2026-07-27
agent_id: huangyaoshi
date: 2026-07-27
created_at: 2026-07-26T18:05:35.732196+00:00
updated_at: 2026-07-26T18:05:35.732196+00:00
---

# huangyaoshi · 2026-07-27

# Truman 10章复盘 · 黄药师 · 2026-07-27

## 1. 做了什么

- **MCP 检索效率升级**：小昭搜"坏世界的研究"返回空——暴露索引管道落后元数据层三周。修了三层：
  - 索引层：`search_index.py` 加权索引——title 3x / aliases 3x / discoverable_by 2x / tags 2x / body 1x
  - RRF 融合层：`delivery.py` `_rrf_fuse()` 增加 tag 维度智能匹配——搜"CEO怎么设计分钱规则"→audience:ceo boost→框架卡排前
  - MCP 出口层：`kdo_search` 结果增加 aliases + tags + position 字段——小昭无需逐张 kdo_read 即可判断
- **全库 aliases 自动补充**：1,616 张卡从 source_refs 提取可发现名称→980 张噪声清理→索引重建
- **aliases 源材料名 lint 规则**：`_check_aliases_has_source_name`——source_refs 引用的材料名必须在 aliases 中。防止未来新"坏世界"出现
- **#208 #209 #212 三项任务完成**：索引管道升级 + aliases lint + RRF tag 匹配
- **cap_hub/_capability_hub 双代码库合并**：`_capability_hub/` 删除，`health_check.py` 移入 `cap_hub/`，无活代码引用
- **全库健康检查**：2,455 卡，source_refs 覆盖率 80.5%，draft 29.4%，定位声明 14%，综合健康分 55/100
- **Phase 1 多维标签**：2,337 张卡自动标注 audience + scene + skill-level，覆盖率 9.9%→96%
- **坏世界研究读后感**：赵汀阳×柯维，结合老朱巨米教训+OPC+鑫港湾实践，7000 字
- **#203 KDO 基础链路健康检查完成**：Dashboard 基线建立

## 2. 关键决策

- **小昭搜不到坏世界→不是补一个 aliases——是索引管道整体升级**。王语嫣诊断：索引管道落后元数据层三周。aliases/tags/discoverable_by 三个字段在元数据层铺开了，查询层一个没跟上。修了索引层+RRF+MCP 三层，不只是补字段
- **"标签足够"的标准重新定义**：不是覆盖率%，是外部 Agent 能否不看全文判断卡片适用性。Phase 1 的三维标签（audience/scene/skill-level）是分类标签，不是路由标签——半肥猫用标签回答"能不能用"，我们回答"属于哪类"
- **MCP search 不应该只返回 300 字 snippet**：改回 aliases + tags + position + 500 字 snippet。小昭从 6 次 MCP 调用降到 2 次
- **半肥猫 100+ 标签 vs KDO 的差距不在数量——在维度**：缺 routing 维度（method/industry/value-tier/prerequisite-knowledge），这些不能自动推断，需要 Phase 2 人工精标
- **王语嫣编排优先级判断**：Phase 2 人工精标 + Phase 3 pre-submit 强制门禁——不排专门任务，靠老顽童返工自然覆盖。P0 框架卡 4 周内自然精标到位

## 3. 新资产

- `search_index.py` — 加权索引（title 3x / aliases 3x / discoverable_by 2x / tags 2x）
- `delivery.py` — RRF tag 维度智能匹配
- `kdo-tools/mcp/tools.py` — search 返回 aliases + tags + position
- `pre_submit.py` — `_check_aliases_has_source_name` lint 规则
- `90_control/domain-routes.yaml` — 域名路由配置（10 域）
- `70_product/operations/kdo-infra-health-dashboard.md` — 基础链路健康仪表盘
- `40_outputs/content/articles/2026-07-26-reading-notes-bad-world.md` — 坏世界读后感
- `60_feedback/diagnosis/diag_20260726_huangyaoshi-tag-system-phase2-3.md` — 标签体系编排建议
- `60_feedback/diagnosis/diag_20260726_huangyaoshi-index-pipeline-upgrade.md` — 索引管道升级建议
- `60_feedback/diagnosis/diag_20260726_huangyaoshi-mcp-production-upgrade.md` — MCP+生产升级建议
- `_capability_hub/` — 已删除，合并入 `cap_hub/`

## 4. 新问题/阻塞

- **Phase 2 人工精标覆盖率不足**：#211 老顽童排队中——method/industry/value-tier 标签未标，RRF tag 维度 match 目前只能利用 audience/scene 两个维度
- **#211 阻塞 #212 的部分验收**：RRF tag match 在 method/industry 维度上暂无数据，等 Phase 2 精标后效果会更好
- **`_check_tags()` 强制门禁未激活**：等 Phase 2 标签覆盖率 >80% 后开启。代码已写
- **高价值卡仍缺 method/industry/value-tier**：P0 framework 卡 ~30 张需老顽童返工自然覆盖，预计 4 周
- **MCP kdo_search 仍依赖 Graph RAG 首次加载慢**：~30s 首次查询，非紧急但影响体验

## 5. 踩坑

- **auto_alias 脚本噪声**：1,616 张卡加了 aliases，但混入了 "inbox""拆书会第""逐字稿" 等噪声。980 张卡需要二次清理。教训：自动推断逻辑必须加噪声过滤——目录名不等于可发现名称
- **_capability_hub vs cap_hub 双代码库**：上次修 agent-spec 扫描时改了 `_capability_hub/registry.py`，狗粮没反应——实际加载的是 `cap_hub/registry.py`。30 分钟 debug。本次合并消除隐患
- **RRF fusion 路径格式不一致**：Graph RAG 返回相对路径，BM25 返回绝对路径。用文件名 stem 做 key 解决
- **坏世界研究是 KDO 盲测失败的又一次验证**：知识存在但搜不到——三个根因（标题用学术名、aliases 不覆盖源材料名、索引层不感知元数据）——和上次"销售过程"是同构问题

## 6. 下次启动最需要记住

- 索引管道已升级——aliases 3x、tags 2x、discoverable_by 2x 加权。重建索引后生效。新卡建了 aliases 后记得 `kdo index`
- RRF tag 维度匹配已生效——搜"CEO+战略"→audience:ceo boost；搜"怎么做+步骤"→scene:execution boost
- MCP search 现在返回 aliases + tags + position——外部 Agent 一次搜索即可判断，无需逐张 read
- 全库健康基线：source_refs 80.5%、draft 29.4%、定位声明 14%、综合健康分 55/100
- 停车场待办：P-23 能力中台、P-2 domain 自动加权、P-16 自动代码审查 Skill
- 三个建议书已交王语嫣：标签 Phase 2-3、索引管道升级、MCP+生产升级。她编排后入队

## 7. 🔴 必做（不完成=会话未完成）

- [x] daily-context 复盘写入
- [x] B1 门禁：本会话无新建任务单，不需要入队
- [x] 技能进化日志更新
- [x] 失忆恢复锚点更新

## 8. 黄牌/表扬

- 🟢 一天内完成索引管道三层升级（索引+RRF+MCP）+ aliases 自动补充+清理 + lint 规则 + 双代码库合并，全部狗粮通过
- 🟢 坏世界读后感——用 KDO 讲香基本功：口述风格、具体案例、个人经验、框架→操作。不是学术论文
- 🟢 小昭搜不到的根因定位准确——不是 aliases 不够，是索引管道不认识元数据。修的是管道，不是字段
- 🟡 auto_alias 脚本噪声问题——应该在 apply 前多看几个 sample，而不是直接跑全量

## 9. 五步法反思

- 实事求是：小昭搜不到坏世界——不是"卡片不存在"也不是"aliases 没写"，是三道防线（搜索→索引→元数据）全部依赖 title+body，没人告诉检索层 aliases 和 tags 是什么
- 解放思想：从"修 aliases 字段"升级到"索引管道感知元数据"。和上次从"消化 Truman 内容"到"用建模方法论改造 KDO"同构——问题的层次比表面的高一层
- 知行合一：半肥猫的标签哲学不是理解了就完了——立刻映射到 KDO：分类标签 vs 路由标签，Phase 1 vs Phase 2 的分工
- 关键假设：假设外部 Agent 需要 aliases+tags+position 就能判断→验证了。假设 tag 维度 match 能提升排序→验证了。未验证：method/industry 维度的实际效果
- 迭代：auto_alias 脚本产生噪声→立刻清理→改进 lint 规则。不等到"下次再说"

## 10. 角色定位

黄药师=Builder。本会话产出：索引管道升级（3层）+ 全库 aliases + lint 规则 + 双代码库合并 + 健康检查 Dashboard + 三个诊断建议书 + 读后感。不做卡片生产（老顽童），不做任务编排（王语嫣），不做终审（欧阳锋）。跨角色协作：审阅王语嫣诊断+小昭审计，给王语嫣写编排建议书。
