---
id: 488
assignee: huangyaoshi
status: queued
updated_at: '2026-08-24T01:45:00+08:00'
version: v0.1
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