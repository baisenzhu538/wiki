---
id: task_20260809_wangyuyan-coaching-leadership-assistant-norm
assignee: claude
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-09
updated_at: '2026-08-09T11:49:22.750789+00:00'
priority: P1
wsjf: 2.5
---

# 教练式领导力助理 Agent 编排（#300 · TCPR 角色可切换规范版）

## 任务目标

承接 #282 的命名/定位调整（用户铁律 E025：不在原任务改，另开新任务）——**统一"XX 助理"命名 + TCPR 四角色按场景可切换**（2026-08-09 用户确立的 Agent 命名规范，已写入 #263 流水线）。

## 背景

- #282（教练式领导力 Agent）已送审且欧阳锋已审（B+ 条件），**原任务冻结不动**
- 用户确立命名规范："以后都是统一按照助理方来，按照 TCPR，可以切换角色的。你如果写成教练，就只能做教练了"
- spec 新版已就位：`agents/coaching-leadership-assistant/SPEC.md`（id: spec-coaching-leadership-assistant，TCPR 助理角色切换声明）

## 规格

1. spec 已编排完成（assistant 版本：默认 Assistant 身份 + T/C/P/R 按问题类型切换 + 回复首行声明角色 + 用户可指定角色）
2. 本任务 = spec 送审 + 部署协调：
   - spec 送欧阳锋终审（复用 #282 审查结论：C1 等 #288 前置、C2 死链已修——新 spec 已含修复）
   - 终审通过后黄药师三件套注入（agents/coaching-leadership-assistant/ + cap_hub 注册 + 飞书）
3. 与 #282 关系：#300 是 #282 的规范演进；#282 保持原审查链（教练式领导力 Agent 原版），#300 落地助理化版本——两 spec 共存，生产以 #300 为准

## 验收标准

- spec 过欧阳锋终审（TCPR 切换声明 / 边界 / 基线用例齐全）
- cap_hub 注册 active + 飞书可用（"我要怎么带老油条下属"→ 返回角色声明 + 五阶梯定位 + 话术）
- 自举踩坑 ≥1 条沉淀

## 依赖

- **#288 reviewed**（C1 前置：21 卡牌矩阵/段位清单/dk×3/莫非完整故事——数据源完整性铁律）
- #280/#281 reviewed（已满足）

## 边界

- 不修改 #282 任务单/队列行/审查记录（E025 铁律）
- 不重复编排 spec（assistant 版本已就位，本任务只走审+部署）

## 终审记录（2026-08-09 欧阳锋）

**verdict: PASS（条件）A- · blocking: 🟠1 · methodology v2.2**

O0 溯源验证：
1. **C2 死链修复确认（#282 条件在 #300 全修）**：related 4/4 无死链——agent-spec-复盘教练 ✅ / tool-yitang-daily-weekly-meeting-hosting ✅
2. **C1 数据源 15/15 全就位**：#280 framework×3 + tool×3 / #288 21 卡牌 + 段位 + dk×3 / #281 bridge / case×3（含莫非半导体）——全部已 reviewed
3. **TCPR 可切换规范落地**（用户命名规范：统一"XX 助理"，角色按场景切换不锁死）——默认 Assistant + 按问题类型切换 T/C/P/R + 回复首行声明角色 + 用户可指定角色
4. 结构完整：五阶梯定位诊断表/硬币诊断/21 卡牌匹配/话术/输出格式/边界 5 条（双边界声明）/基线用例（老油条案例证据链完整——莫非案例已就位）/三件套/自举/双实例纪律
5. E018 合规：status=draft + reviewed_by 待审查（未自标）

条件项：
- **C1 部署件路径修正**：三件套需求 L146"部署件：agents/coaching-leadership-**coach**/ 目录"应为 **coaching-leadership-assistant/**（复制 #282 时路径未更新——实际 spec 在 assistant 目录，黄药师部署前需修正）

五维：溯源 90/逻辑 90/暗知识 90/可操作 85/表达 90 → 总分 89（A- 上限——路径瑕疵）
