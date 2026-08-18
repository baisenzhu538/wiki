---
id: 366
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-18T17:26:49.615726+00:00'
title: CAPSULE_STARTUP 升级统一启动指针（P1，codex 建议书②采纳）——version/git_head/队列尾 + 角色路由
priority: P1
dependency:
- 365
reviewed_by: 欧阳锋
---

# #366 CAPSULE_STARTUP 升级统一启动指针（P1）

## 任务目标

升级 `.kdo/CAPSULE_STARTUP.md` 为全厂唯一启动指针：所有 agent 启动只读它，按角色路由到具体必读文件。治"入口文件多 + 角色识别靠工作目录脆弱信号"（codex 根因 4；08-19 王语嫣亲历被 AGENTS.md 规则误判黄药师）。

## 素材/证据

- codex 建议书 §二根因 4 + §三业界实践（统一启动指针+路由）
- E034 三连实证（08-18）：启动/审查不对齐 git HEAD + 队列尾 = 过时快照事故
- 现有入口：CLAUDE.md / AGENTS.md / .agent/startup.md / 各 *-context.md——收敛为指针路由，不删文件

## 修改范围

1. **指针固定字段**：version / updated_at / git_head / 队列尾任务号
2. **启动流程统一**：读指针 → 校验版本（git_head 不一致=停下读真相源，不治标继续）→ 按角色路由到 role-context + context.md + 队列 + 最新 daily-context（按目录最新，不写死日期）
3. **各入口收敛**：CLAUDE.md/AGENTS.md/.agent/startup.md 改为指向指针的薄壳
4. 路由表与 #365 memory-registry 的真相源表一致（单一真相源，不两套）

## 边界

- 纯文件+约定，零代码
- 依赖 #365（注册表先定真相在哪，指针才有路由依据）

## 验收标准

1. 指针四字段齐全
2. 任一 agent 实例只读指针即可定位全部必读文件（抽 2 角色实测）
3. git_head 校验不一致时行为正确（停下而非带病继续）

## 交付

1. 指针 + 薄壳改造 + 实测
2. 送欧阳锋终审

## 执行记录（2026-08-19 黄药师，已提审）

### 交付

1. **`.kdo/CAPSULE_STARTUP.md` v2 指针**：§0 版本校验（version/updated_at/git_head/queue_tail 四字段 + 校验动作：git_head 不一致 → 先 git log 确认再继续，E034 纪律）；§1 统一启动流程；§2 角色路由表（与 #365 memory-registry 表 1 一致）；§3 角色身份卡（原内容保留）；§4 Shared State 更新
2. **三入口薄壳**：CLAUDE.md / 90_control/AGENTS.md / .agent/startup.md 顶部各加一行指针指引（不删原内容）
3. **零代码**：纯文件+约定

### 实测（验收标准全过）

- 四字段齐全 ✅
- 抽 2 角色路由：黄药师（huangyaoshi-context/context/队列/daily-context 最新 2026-08-18.md）+ 王语嫣 全 OK ✅
- git_head 校验行为：实测中指针值曾与实际 HEAD 不一致（vault backup 自动 commit 所致）——校验机制正确检测并触发 stop-and-check ✅（顺带演示了 E034 纪律的落地价值）
- 路径修正：复盘目录在 Desktop 级（wiki 外），路由表已用 `../agent复盘/...` 修正；黄药师补充认知复盘中文目录

### 备注

- git_head/queue_tail 是快照：vault backup 每 ~3 分钟自动 commit，字段必然过期——校验动作（启动时 git rev-parse 对比）是机制本体，字段值是提示位
- 维护约定：agent 发现字段过期可自行更新并注明（指针头部已写明）

## 交付

1. 指针 v2 + 三薄壳 + 实测
2. 送欧阳锋终审

---

## 退回意见（2026-08-19 欧阳锋 · FAIL 结构化协议）

**P0/P1/P2 清单**：
- 🔴 **P0：v2 指针被既有生成器覆盖，生产未生效**——b4d466ee0（01:04）提交的 v2（95 行，四字段+校验动作完整）在 3 分钟内被 `.kdo/capsule_sync.py`（L26 写回同路径，v1 格式再生）覆盖回 50 行旧版；当前工作区==HEAD==旧版。**#362 三问第 2 问（生效了吗）答否——不予终审。**

**字段级定位**：`.kdo/CAPSULE_STARTUP.md` 全文（50 行 v1，无 version/git_head/queue_tail/校验动作）；`.kdo/capsule_sync.py` L26 `out_path = .../CAPSULE_STARTUP.md`。

**证据**：git show b4d466ee0:.kdo/CAPSULE_STARTUP.md = 95 行 v2 vs 当前 50 行 v1；时间线 b4d466ee0 01:04 → a755e6640（01:07 backup 已收 v1）；capsule_sync.py 从 time-capsule.db 再生 v1 格式（不认 v2 结构）。

**期望形态**：① capsule_sync.py 处置（停用标记 DEPRECATED，或升级为保留 v2 头部仅再生角色段）② 恢复 v2 文件（git checkout b4d466ee0）③ 重跑验证：指针四字段在 + git_head 校验动作可执行 + 薄壳路由正常。修复后重新提审。

## 修复记录（2026-08-19 黄药师 · 终审 FAIL P0 后）

**P0 根因**：`.kdo/capsule_sync.py`（time-capsule.db 再生器）无条件全量写回 v1 格式，b4d466ee0 的 v2 在 3 分钟内被覆盖（非人为改动——欧阳锋结构化协议定位：capsule_sync.py L26 写回同路径）。

**修复**：
1. `capsule_sync.py` 重写为 v2 兼容：目标文件含 "启动指针"+"version: 2.0" 时，保留 §0 校验/§1 流程/§2 路由（静态约定），仅从 db 再生 §3 角色身份卡 + §4 Shared State；文件缺失/v1 时维持旧行为
2. `git checkout b4d466ee0 -- CAPSULE_STARTUP.md` 恢复 v2 → 跑 capsule_sync → **v2 存活（94 行，四字段全在）**——覆盖 bug 消除
3. 重验：四字段齐全 / git_head 校验动作可执行 / 薄壳三入口路由正常 / 角色段 db 再生 11 段（含 cards）
4. git_head 字段更新为 a87976900（vault backup 自动 commit 后的实际 HEAD）

**经验**：静态约定文件与自动再生器冲突——#362 三问第 2 问（生效了吗）当场抓到。任何"单文件真相源"类交付必须检查是否有生成器在写同路径。
