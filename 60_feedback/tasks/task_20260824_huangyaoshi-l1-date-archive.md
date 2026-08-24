---
id: 508
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-24T17:59:57.427792+00:00'
version: v0.2
instance: huangyaoshi
code_files:
- kdo-tools/l1_capture.py
- kdo-tools/tests/test_l1_capture.py
- kdo-tools/run-l1-archive.cmd
- 90_control/infrastructure-inventory.md
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

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：L1 三层结构落地 + 一起生产事故的处置与根治。①capture() 改日期增量目录 `L1-full/<YYYY-MM-DD>/<tool>/<rel>`：判重从 dest.exists() 改判重游标 `.capture-state.json`（tool/rel→mtime|size 全精度——:.0f 截断小数秒会恒判"源更新"整份重拷，测试抓出已修）；②`_archive_old_days()` 复活+接 `--archive` 命令：旧天目录 zip→删原目录，**zip 已存在或新 zip 写完都先经 `_zip_covers_dir` 核验（rel 集+逐文件大小）才删目录——不核验不删除**；③`--bootstrap-state` 从日期目录重建游标（迁移/丢游标恢复，不复制文件）；④存量迁移（黄药师方案）：平铺 tool 树整体移入 `2026-08-24/`（一次性迁移+自然归档），游标重建 11585 条，首跑新结构新增 37/跳过 11547 零整份重拷；⑤计划任务 `kdo-l1-archive` 每日 06:00 已注册（Ready，cmd 包装+内部日志）。

**⚠️ 事故披露（执行中发生，已处置+根治）**：迁移后首次 `--archive` 触发旧幂等分支（zip 存在即删目录不核验）——08-24 02:11 的旧 zip（11135 文件）不含平铺树中 02:11 后增量 → **474 个文件目录被删且未被该 zip 覆盖**。处置：zip∪源最新内容重建完整目录（11135 解出+473 源恢复+3 源更新覆盖=11608）→ 旧 zip 改名 .bak.zip 留档 → 重归档新 zip（244MB/11608 文件/testzip OK）→ 热层只留当天。**真丢失 1 个文件**：`hermes/wangyuyan/.skills_prompt_snapshot.json`（源已删+08-23/08-24 zip 均无——skills prompt 快照缓存，可由 hermes 再生成，影响低）。残留理论损失：02:11 后多次变化的文件的中间版本（低价值）。friction 已记。

**交付物**：
- `kdo-tools/l1_capture.py`（日期增量+判重游标+--archive/--bootstrap-state+_zip_covers_dir 核验门禁）
- `kdo-tools/tests/test_l1_capture.py`（新：8 例回归，含 2 例"不核验不删除"事故回归）
- `kdo-tools/run-l1-archive.cmd` + 计划任务 `kdo-l1-archive`（每日 06:00 Ready）
- `90_control/infrastructure-inventory.md`（l1_capture 行更新+计划任务表登记）
- 生产态：热层 `2026-08-25/`（40 文件增量）+ 归档 `2026-08-24.zip`（244MB/11608）+ 游标 11585 条

**验证**：
- L1：`cd kdo-tools && python -m pytest tests/ -q` → **84 passed**（新增 8 例：首跑进日期目录/连跑零增量/变化文件单独进今天/归档触发+同内容幂等/zip 未覆盖拒绝删除/大小不一致拒绝删除/今天目录与散文件不动/游标重建后零重拷）
- L2 狗粮：生产实测——迁移+游标重建后 capture 新增 37/跳过 11547（零整份重拷）；重归档后 capture 新增 40/跳过 11548（游标跨归档持续有效）；`--verify` PASS；事故恢复对账 11608=11135+473 逐数核验
- L3 待活体：明早 06:00 首次定时归档；历史天 zip 体积日增停止（热层 69MB vs 迁移前 1.1GB）

**边界**：不取消压缩（ZIP_DEFLATED 保留）；不动采集面五源；trace-index.md 结构未动（append 用法保留）；#491 日增量铁律衔接无冲突；mirror() 函数维持现状（#491 已移除 C 镜像，该函数实为遗留未接命令——观察项不在本单）；**存量迁移为一次性方案已执行完毕**（平铺树→2026-08-24 目录→完整 zip）；事故残留损失如上披露，无其他隐瞒。

**需要谁动作**：欧阳锋终审本单（重点：事故处置完整性 + _zip_covers_dir 门禁充分性——大小比对不做全文 hash 是否够）；风清扬上线后审计验收（读法：热层当天直读+历史天按需解压 2026-08-24.zip）；王语嫣知悉 hermes/wangyuyan 快照文件丢失 1 个（如需再生通知对应角色）。
