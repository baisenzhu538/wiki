---
id: 508
assignee: huangyaoshi
status: queued
updated_at: '2026-08-24T16:00:00+00:00'
version: v0.1
---

# #508 L1 全量上下文改「日期增量目录 + 每日 zip 归档」（复活 _archive_old_days）

- **任务号**：#508
- **状态**：queued
- **assignee**：huangyaoshi（l1_capture.py 改造；欧阳锋终审；风清扬审计验收）
- **优先级**：P1（归档函数现为死代码——结构缺陷非优化项）
- **立项**：2026-08-24 王语嫣（风清扬建议书 `diag_20260824_fengqingyang-l1-date-archive.md` 裁定采纳；老朱 08-24 问「按日期命名+压缩储存」方向确认）

## 背景

现状（风清扬实测）：压缩已做（ZIP_DEFLATED，整份 770MB→75MB≈10x）；但热层 `L1-full/` 是 `tool/rel` 平铺无日期维度，`_archive_old_days()` 只认 `L1_ROOT/<YYYY-MM-DD>` 而 `capture()` 写 `tool/rel`——**归档函数永远匹配不到，现为死代码**（仅 02:07 迁移时生效一次）。正确结构三层：热层按日期增量目录（mtime 判重只放当天变化文件，守住 #491 日增量铁律）→ 归档层每日 06:00 把昨天目录 zip 成 `L1-full-archive/YYYY-MM-DD.zip` 删原目录（幂等）→ 索引 `trace-index.md` 按日期 append（已有保留）。

## 任务

1. `l1_capture.py` `capture()` 改写 `L1-full/<YYYY-MM-DD>/` 日期增量目录（mtime 判重，只放当天变化文件，不整份重拷）
2. `_archive_old_days()` 对齐新结构重新生效：每日 06:00 归档昨天目录 → zip → 删原目录；幂等（已归档过只删目录不重复 zip）
3. 归档锚点 06:00，与 #507 digest 同窗口
4. 历史存量迁移：现有 `tool/rel` 平铺热层如何过渡到日期结构（一次性迁移或自然归档——黄药师定方案，任务单内声明）

## 验证（验证分层）

- L1：改后热层按日期、归档按天 zip、无整份重拷；`_archive_old_days()` 不再死代码（构造跨天样本触发归档实测）
- L2 狗粮：归档幂等——重跑不重复 zip、不丢文件；归档后热层只留当天
- L3 待活体：历史天 zip 体积显著下降（不再出现日增数百 MB）；风清扬审计读法=热层当天直读+历史天按需解压

## 边界

- 不取消压缩（已有 ZIP_DEFLATED 保留）；不动 L1 采集面五源覆盖
- 不改 `trace-index.md` 结构（只保留 append 用法）
- 与 #491（L1 体积治理，已 reviewed）衔接不冲突：日增量铁律优先

## 关联

- 风清扬建议书 `diag_20260824_fengqingyang-l1-date-archive.md`（死代码定位+三层结构原文）
- #491（L1 体积治理：去 C 镜像+去重+日增量）/ #507（同 06:00 锚点）
- F-045（L1 现阶段唯一硬要求=保证全量保存——本单不破此约束）

## 需要谁动作

- **黄药师**：l1_capture.py 改造 + 存量迁移方案
- **风清扬**：上线后审计验收（读法切换）
- **欧阳锋**：终审本单
