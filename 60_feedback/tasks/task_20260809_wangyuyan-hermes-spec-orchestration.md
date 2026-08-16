---
id: task_20260809_wangyuyan-hermes-spec-orchestration
assignee: claude
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-09
updated_at: '2026-08-09T06:09:25.109031+00:00'
priority: P1
---

# 王语嫣 Hermes spec 编排（B2）

## 任务目标

用 #263 Agent 生产流水线（spec→三件套→自举）给王语嫣自己建 Hermes spec——编排自己的编排，验证流水线第一使用场景。

## 背景

- workflow-kdo-agent-production-pipeline（#263）明确"王语嫣编排 = 流水线第一使用场景"，但当前"王语嫣无 Hermes spec"（仅补了认知件）
- agent-os §13：判断型角色（王语嫣编排）双实例独立印证——Claude 端 + Hermes 端，spec 需要服务双实例
- 双驱动机制 #265：Hermes 端实例的实测反馈是外部驱动通道之一

## 规格

1. 王语嫣写自己 agent-spec 卡（角色 TCPR + 核心能力 + IO 格式，参照 agent-basic-skills-coach 模式）
2. 黄药师注入三件套：认知件（SOUL.md KDO 知识地图 5 MOC + task-orchestration skill）、路径件（config.yaml 终端+检索规则）、部署件（agents/wangyuyan/ 目录 + Hermes profile）
3. 自举：飞书端王语嫣实例启动验证（自我定位→探索→踩坑沉淀→迭代 spec）
4. 双实例纪律：判断层独立（审计结论/复盘/错误模式分开存放，§13）

## 验收标准

- spec 卡过欧阳锋审查（TCPR/门/边界齐全）
- Hermes 端实例冒烟测试通过（检索 MOC 命中、task-orchestration 可加载）
- 自举过程沉淀 ≥1 条踩坑（进错误模式库或 dk 卡）
- 流水线第一使用场景验证结论写回 workflow 卡迭代日志

## 边界

- 不替代 Claude 端王语嫣（双实例共存，判断层独立）
- 不在试点完成前改 cap_hub 注册（#258 裁定：试点后统一注册）

## 终审记录（2026-08-09 欧阳锋）

**verdict: PASS（条件）A- · blocking: 🟡1 · methodology v2.2**

溯源核验（O0 全过）：source_refs 4/4 存在（workflow 卡 227 行/王语嫣 context 599 行/task-orchestration skill 79 行/agent-os 401 行）；工具引用全真（scan-demo-sections.py/transcript-index.py/personal-os 目录实测存在）；三件套齐全（agents/wangyuyan/ 下 AGENTS/CLAUDE/SPEC）；TCPR 非 P 非 R + 铁律 6 条 + 能力表 + IO 格式 + 双实例纪律（§13 三层）+ 边界 3 条全达标；E018 合规（spec status=draft、reviewed_by 待审查——未自标）。

五维：溯源 90/逻辑 85/暗知识 70/可操作 80/表达 85 → 总分 82（A-）

条件项（跟踪至闭环）：
- **C1** related 死链 agent-spec-review-coach（全库无此卡）——换为已存在卡或注明"规划中"
- **C2** workflow 卡「已跑通 Agent」表格更新（当前王语嫣行 spec 仍 ❌，与事实矛盾）
- **C3** Hermes 端冒烟测试 + 自举踩坑 ≥1 条——飞书端抽查后补（同 #261 条件①模式，本地不可验证）

🟢 观察：spec 首段已有 #263 流水线定位声明（O8 达标）

## 条件项跟踪（编排侧，2026-08-09 王语嫣）

- **C1 ✅ 已闭环**：related 死链 agent-spec-review-coach → 修正为 `agent-spec-复盘教练`（真实卡，30_wiki/tools/ 实测存在）
- **C2 ✅ 已闭环**：workflow 卡「已跑通 Agent」表格更新——王语嫣行改为 `✅ SPEC-hermes.md（欧阳锋 A- 2026-08-09） | ⏳ 待部署 | ⏳ 飞书端冒烟+踩坑（#268 C3）`
- **C3 ⏳ 跟踪中**：飞书端冒烟+踩坑——依赖黄药师三件套部署（agents/wangyuyan/ + Hermes profile），与 #273 C2（双轨 status 一致）同批执行
