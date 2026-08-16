---
title: 任务建议书：知识传导链路收尾编排（给王语嫣）
type: improvement-plan
status: draft
created_at: 2026-08-16
author: 欧阳锋
audience: 王语嫣
source_refs:
  - "60_feedback/tasks/task_20260816_wangyuyan-snapshot-migration-pilot.md"
  - "60_feedback/diagnosis/diag_20260816_hermes-gateway-lock-conflict.md"
  - "60_feedback/tasks/task_20260815_wangyuyan-agent-spec-domain-cleanup.md"
---

# 任务建议书：知识传导链路收尾编排（王语嫣编排用）

> 背景：系统性工程四环（诊断 #324 → 存量补齐 #325 → 机制制度化 #326 → 快照迁移试点 #327）已全部终审闭环。本节建议书把**收尾遗留项**拆为可入队任务，由王语嫣审核编号后入 `production-queue.md`。
> 执行人原则：基建/脚本/CLI = 黄药师；内容卡 = 老顽童；部署/编排 = 王语嫣；审查 = 欧阳锋。
> 优先级依据：#327 终审裁定（源码 bug P0）+ 用户已拍板（#328 方案 B）+ 试点成功（P3 推广就绪）。

## 依赖关系

```
#328 (P0) Gateway 锁冲突修复（已拍板方案 B，已在队列）
  ├─ 观察者记录修复前后对比（首份观察样本）
#329 (P0) KDO 源码 cmd_index 修正（#327 终审裁定）
  └─ #330 (P1) #263 文档命令修正（依赖 #329 确认正确命令后写文档）
#331 (P1) P3 快照迁移推广（#327 试点成功 → AI 基本功教练 + 其余快照 agent）
#319 (P2) agent-spec domain 清扫（O-14，任务单已写待入队）
#321 (P2) 销售域 digest（已入队）
```

---

## #329 建议：KDO 源码 cmd_index 修正（P0 · 黄药师）

**目标**：修复 `kdo index --rebuild` 提前 return 0 不重建 search_index.json 的静默失效 bug（#327 试点实证）。

**证据**：`search_index.py cmd_index` L234-241——`--rebuild` 分支只调 auto_update_index 重建 index.md 后提前 `return 0`；cli.py L806 help 也写"Rebuild 30_wiki/index.md and backlinks"。

**方案选项**：
- 方案 1：`--rebuild` 语义对齐直觉——重建 search_index.json + index.md + backlinks 全量
- 方案 2：改名 `--rebuild-nav` 专指导航索引，`kdo index` 保持重建搜索索引

**验收**：① 新卡终审后 `kdo index --rebuild` → 新卡可检索（协议级 kdo_search 命中）② 回归：普通 `kdo index` 行为不变 ③ 文档同步（#330）

---

## #330 建议：#263 Step 4 文档命令修正（P1 · 黄药师）

**目标**：`workflow-kdo-agent-production-pipeline.md` Step 4 命令 `kdo index --rebuild` → 正确命令（依 #329 方案定稿）。

**补充**：全库 grep 其他文档中 `kdo index --rebuild` 误用（#325/#326 文档、迁移模式沉淀文档），一并修正。验证：修正后文档命令实测可用。

---

## #331 建议：P3 快照迁移推广（P1 · 王语嫣执行 + 老顽童内容）

**目标**：按 #327 沉淀的三步走迁移模式，推广到 AI 基本功教练 + 其余快照 agent（prompts 目录 38 个编译产物，最新 Jul 15）。

**范围**：先推广 AI 基本功教练（与销售对话助理同构，工作量 0.5d）；其余按优先级排队——快照 agent 优先"仍在活跃消费"的，纯历史快照可归档。

**验收**：① 每个迁移 agent 重编译 + 导航升级 + 真实问题命中新卡 ② 迁移模式文档更新（多实例验证后定稿）

---

## #319 建议：agent-spec domain 清扫（P2 · 老顽童内容 + 欧阳锋审）

**目标**：O-14 任务单已写（`task_20260815_wangyuyan-agent-spec-domain-cleanup.md`）——9 张 agent-spec 卡 domain 字段补齐 + 目录归属评估。请王语嫣编排入队（任务单已 queued）。

---

## 编排建议顺序

1. **#328 先行**（已在队列）——gateway 崩溃循环影响生产 agent，观察者记录前后对比
2. **#329 紧随**——索引失效静默，所有文档/脚本在用错命令；且 #331 推广依赖正确命令
3. **#330 与 #329 同批**（文档修正依赖源码方案定稿）
4. **#331 在 #330 后**（推广文档要用正确命令）
5. **#319/#321 并行不阻塞**（内容类，与基建无依赖）

## 其他待办（不急于入队，记录备查）

- test_cli_smoke state 断言过期（低优先，工作区未提交改动累积 460 行，commit 时机用户定）
- delivery.py patch commit 时机（用户定）
- O-12 WSL→Windows 迁移（待 O-13 扩容 1 周评估，swap 若活跃再启动）
- 观察者接入规范（报告落点/频率，用户补充后登记）

*欧阳锋 · 2026-08-16*
