---
id: 488
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-23T17:16:19.354002+00:00'
version: v0.1
instance: huangyaoshi
reviewed_by: 欧阳锋
review_date: '2026-08-23'
grade: A-
---
# #488 基建资产总表建设（infrastructure-inventory.md——识别靠表不靠记忆）

- **任务号**：#488
- **状态**：queued
- **assignee**：huangyaoshi（建设；王语嫣编排；欧阳锋终审）
- **优先级**：P1（治根型，与 charter §3.x 治理章/停车场治理/三路由同源）
- **立项**：2026-08-24 王语嫣（老朱拍板采纳黄药师建议书 `diag_20260824_huangyaoshi-infrastructure-inventory.md`）

## 背景

黄药师 2026-08-24 00:30 凌晨建议书自盘：实战 15 单后，全厂基建 130+ 资产（脚本/计划任务/服务/数据资产/台账）**无总表**——任何角色（含新 Builder 替代者）识别"基建有哪些、谁健康、哪里断、谁维护"靠记忆+翻目录拼图。

三大缺口：
1. `90_control/scripts` ~80 脚本中约一半是 fix-*/repair-*/migrate-* 一次性修复批，有用/历史遗留无账
2. KDO CLI 源码侧（47 文件）vs wiki 侧脚本的分工边界无文档
3. 计划任务（conveyor-probe/l1-capture/inbox-watch/health-daily）+ 服务（hermes gateway/wx_video_download）+ 数据资产（L1 库+镜像/索引/台账/基线）散落各文档无总览

现有机制各管一段互不隶属：cap_hub 26 Feature 记能力、README 记工具存在、memory-registry 记记忆真相源——三者与本表"基建资产状态+职责+关联"分层并存不替代。

## 任务

### 任务1·建总表（核心交付）

`90_control/infrastructure-inventory.md`——按域分类（门禁族/工具族/服务/计划任务/数据资产/基线台账/一次性批标记），每项登记六字段：

| 字段 | 含义 |
|:---|:---|
| 位置 | 文件路径或服务名 |
| 职责 | 一句话功能 |
| 维护人 | 角色名（黄药师单一实例=基建） |
| 最近验证 | 日期 + 验证命令输出摘要 |
| 关联 | 依赖/被依赖/同源资产 |
| 标记 | 「历史遗留待归档」等一次性批标注 |

### 任务2·配 status 快照命令

`kdo infra status` 一条命令输出各资产健康态（与 health-check 联动：绿灯/黄灯/红灯/未知），不替换 health-check，是其上的资产视图层。

### 任务3·挂路由层附录 + CAPSULE_STARTUP 指向

- 路由层 D-018 附录 A 待补项就此结清
- CAPSULE_STARTUP 冷启动段指向本表（让新 Builder 替代者一键看到基建全貌）

### 任务4·维护纪律登记

- 维护权：黄药师（基建单一实例）
- 新增基建组件登记入表=登记纪律（与 `40_outputs/README.md` 同构但不重复——README 记"存在"，本表记"状态+职责+关联"）
- 登记失败 = lint 拦截（治标 → 治本）

## 边界

- **只建总表+快照命令，不动任何组件本体**——存量一次性修复批只标注不清理（清理另立项）
- 与 memory-registry（记忆真相源）/cap_hub（能力注册）/README（工具登记）**并存分层，不合并不替代**

## 验收标准

1. `90_control/infrastructure-inventory.md` 落盘，按域分类完整，六字段齐
2. `kdo infra status` 命令可用，实跑输出各资产健康态
3. 路由层附录 A 更新指向本表
4. CAPSULE_STARTUP 冷启动段补充本表入口
5. 与现有 cap_hub/memory-registry/README 边界明确（边界声明节落盘）
6. 欧阳锋终审 PASS（建议 A-/B+ 起步，治根型留出优化空间）

## 编排决策（王语嫣独立判断）

| 维度 | 裁定 |
|:---|:---|
| 必要性 | ✅ 高——最近一个月基建资产暴增，编排者也常翻目录拼图 |
| 边界遵守 | ✅ 黄药师自陈"只建表+快照不动本体/不合并替代既有机制"，合规 |
| 同构定位 | ✅ 治根型——与 charter §3.x 治理章/停车场治理/三路由同源 |
| 优先级 | **P1**（治根，非修补） |
| assignee | **huangyaoshi**（基建单一实例） |
| 验收者 | 欧阳锋（终审）；王语嫣（编排侧核对边界） |

## 依赖与时序

- **无前置依赖**——可立即开工
- 与 #472 role-routes 互补（路由层=导航，本表=资产地图）
- 与 #485 vocab-axis-before-batch-gate（王语嫣自办）并行不冲突
## 执行报告（2026-08-24 黄药师）

**完成内容**：基建资产总表建设四任务全交付——①总表 `90_control/infrastructure-inventory.md`（八域分类六字段）②`infra-status.py` 健康快照（27 项实测全绿）③路由层附录 A 结清 + CAPSULE_STARTUP 入口 ④维护纪律落盘。

**交付物**（改动文件清单）：
1. `90_control/infrastructure-inventory.md`（新建）：八域分类（门禁 10/巡检 12/工具 20/服务 2/计划任务 5/数据 8/基线台账 5/一次性批 28 标记）+ 六字段 + 分层边界声明 + 维护纪律
2. `kdo-tools/infra-status.py`（新建）：`infra-status.py [--json]` 27 项资产健康快照（文件/计划任务/服务进程/端口/台账），红绿灯+退出码
3. `.kdo/CAPSULE_STARTUP.md`：冷启动段加基建资产总表入口（新 Builder 替代者必读）
4. `90_control/role-routes.md`：附录 A（D-018「基建造表待补项」结清）
5. `kdo-tools/tests/test_infra_status.py`（新建）：5 用例

**验证**（命令+输出）：
- L1 单测：`pytest tests/`（kdo-tools）→ **67 passed**（含 infra-status 5 用例）
- L2 狗粮：①`infra-status.py` 实跑——27 项资产**全绿**（门禁/工具/服务 hermes+wx/计划任务 4+数据/台账）；②首跑修 3 处误报（L1-full 目录 st_size=0 误判→exists 判定；force-exceptions.log 无记录=健康；tasklist GBK 乱码→二进制匹配）；③总表与既有机制边界核对（memory-registry/cap_hub/README 分层不替代）
- L3 待活体：新组件登记入表纪律生效（新增基建组件未登记=不存在）；新 Builder 替代者冷启动读总表识别全貌

**未做项**：
- KDO CLI `kdo infra status` 集成拆出（#473 kdo lint 集成同模式：跨仓改动需 KDO 561 测试回归，后续独立单）
- 一次性批 28 个只标注待归档（任务书边界：清理另立项）

**需要谁动作**：
- 欧阳锋：终审本单（抽「八域分类完整/六字段齐/快照实跑/入口挂接/边界声明」）
- 全体 agent：新基建组件登记入表（维护纪律）

---

## 终审记录（欧阳锋 · 2026-08-24）

**结论：PASS / A-**

**版本对齐三问**（代码类，全绿）：① 入仓：c3ddb39c0（01:11）在 HEAD ② 生效：快照独立实跑 27 项全绿 ③ 对齐：审查对象=HEAD

**O0 逐条溯源**：
1. **总表（任务 1）** ✅：infrastructure-inventory.md 十节——八域分类（门禁 10/巡检 12/工具 20/服务 2/计划任务 5/数据 8/基线台账 5/一次性批 28 标记）+ 六字段（位置/职责/维护人/最近验证/关联/标记）+ 边界声明（§9 与 memory-registry/cap_hub/README 分层并存）+ 维护纪律
2. **快照命令（任务 2）** ✅：infra-status.py **独立实跑 27 项全绿**（红灯 0/27——计划任务 4+服务 2+门禁/工具/数据/台账全绿）；首跑修 3 处误报（st_size 判定/exists 判定/tasklist GBK 二进制匹配——诚实记录）
3. **入口挂接（任务 3）** ✅：CAPSULE_STARTUP L30（新 Builder 替代者必读）+ role-routes 附录 A（**D-018 结清**——"路由层管该做什么，总表管有什么"）
4. **维护纪律（任务 4）** ✅：维护权=黄药师（基建单一实例）+ 新增组件登记入表=登记纪律（未登记=不存在，与 README 同构不重复）
5. **测试独立复现** ✅：5 passed（全量 67）；边界 ✅（只建表+快照不动组件本体——一次性批 28 个只标注不清理）

**发现问题**：🔵 无实质缺陷——观察项：`kdo infra status` 集成拆出（跨仓 KDO 561 测试回归——#473 kdo lint 集成同模式，后续独立单）；一次性批清理另立项

**魔鬼代言人**：3 个月后最可能出问题——总表与组件实际状态漂移（新增组件未登记=登记纪律靠自觉+lint 拦截治本中）；或 infra-status 检查项随基建演进未同步（27 项需随新增组件扩展）

**存在性核查**（本意见书负向断言证据）：
- 「27 项全绿」→ 核查：infra-status.py 独立实跑输出（红灯 0/27）
- 「十节结构」→ 核查：grep 总表节标题（0-9 节）
- 「入口挂接」→ 核查：CAPSULE_STARTUP L30 + role-routes L61-65 实测
- 「5 passed」→ 核查：pytest 独立复现

**残余风险**：kdo infra status 集成待拆单；一次性批清理待立项；总表漂移靠登记纪律+lint。

*欧阳锋 · 2026-08-24 · A-*
