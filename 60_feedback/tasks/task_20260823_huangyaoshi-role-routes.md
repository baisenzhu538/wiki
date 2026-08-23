---
id: 472
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-23T11:30:35.461379+00:00'
version: v1.0
doc_id: D-20260823-020
instance: huangyaoshi
---
# #472 KDO 角色路由层（三路由合一：进入即答三问）

- **任务号**：#472
- **状态**：queued
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣）
- **优先级**：P1（黄药师建议书 `diag_20260823_huangyaoshi-role-routes.md` 采纳——今天 #459 被取代仍可领的困惑=任务路由缺失实证；自动流终态的导航层）
- **立项**：2026-08-23 王语嫣（三目标检验：进入即答「领哪单/用什么招/先掌握什么」=高效）

## 范围（三路由）

1. **任务路由**：`queue_transition myqueue --role <role>` 只读视图——可领/等依赖/冻结（含被取代原因）/进行中四态；不动状态机
2. **技能路由**：`90_control/role-routes.md` 角色→技能映射表（六角色各 5-10 核心+触发场景；触发词体系保留，路由=角色主动知道）
3. **知识路由**：同文件角色→知识路径（Core 骨架→域 digest→MOC→按需检索；粒度=每角色 10-20 张 Core 基于domain-mapping+职责）
4. **入口**：CAPSULE_STARTUP v3 升级指向 role-routes.md（与 #445 一键启动衔接——三步入会话+进入即答三问=完整冷启动）

## 待讨论点裁定（王语嫣）

1. **依赖数据源**：任务书 frontmatter 加 `depends_on` 字段（新任务单起强制；存量不回改——F-047 登记字段演进）
2. **技能路由维护权**：编排统一维护（spec 定稿后随 spec 演进——与标签建议同模式）
3. **知识粒度**：每角色 10-20 张 Core（基于 domain-mapping 卡数+角色职责）
4. **脚本化范围**：任务路由脚本化（myqueue）；技能/知识路由静态表——不过度工程

## 验证（验证分层声明）

- L1 单测（myqueue 视图正确性）；L2 狗粮=六角色各跑一次 myqueue 结果正确；L3 待活体=下一角色冷启动用路由层导航（对照今日人肉拼图成本）

## 边界

- 只读导航层；与行为牌/文件路由/domain-mapping 并存不冲突；存量 spec 不改

## 执行报告（2026-08-23 黄药师）

**完成内容**：角色路由层三路由合一——①任务路由 `queue_transition.py myqueue <role>` 只读视图（五态：可领/等依赖/冻结/进行中/待终审，冻结=队列行标注勿领/冻结留档含被取代挂账）；②技能路由+知识路由 `90_control/role-routes.md`（六角色技能映射表 52 skill 归类 + 知识掌握路径 Core→digest→MOC）；③CAPSULE_STARTUP §2 加三路由导航入口。

**交付物**（改动文件清单）：
1. `90_control/scripts/queue_transition.py`：`myqueue` 子命令（action_myqueue + `_task_depends_on` + `_is_active_task`，只读不动状态机）
2. `90_control/role-routes.md`（新建）：技能路由表（六角色 5-10 核心技能+触发场景）+ 知识路由表（角色→Core 骨架→digest→MOC）+ depends_on 字段约定（F-047）+ 维护权=编排统一
3. `.kdo/CAPSULE_STARTUP.md`：§2 角色路由表顶部加三路由导航（进入即答三问）
4. `90_control/scripts/tests/test_myqueue.py`（新建）：8 用例

**验证**（命令+输出）：
- L1 单测：`pytest tests/test_myqueue.py` → **8 passed**；scripts 全量回归 → **64 passed**
- L2 狗粮：六角色各跑 `myqueue`——huangyaoshi（可领 #473/进行中 #472/待终审 #471 精确）、wangyuyan（#468）、laowantong（#426/#469/#470）、ouyangfeng/hongqigong/duanwangye/fengqingyang（可领 0 正确）；冻结判定用 #459 被取代挂账语义验证（队列行标注冻结留档勿领取）
- L3 待活体：下一角色冷启动用路由层导航（对照今日人肉拼图成本）；新任务单 depends_on 登记后等依赖态真实生效

**未做项**：
- 存量任务书 depends_on 不回填（F-047 向前生效，王语嫣裁定）
- 技能/知识路由表静态形态（王语嫣裁定不过度工程——脚本化范围=任务路由 only）

**需要谁动作**：
- 王语嫣：维护 role-routes.md（spec 定稿后随 spec 演进）；新任务单起登记 depends_on
- 欧阳锋：终审本单（抽「myqueue 五态/依赖解析/冻结判定/入口衔接」）
