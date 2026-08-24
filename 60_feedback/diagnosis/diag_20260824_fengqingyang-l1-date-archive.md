---
id: diag_20260824_fengqingyang-l1-date-archive
title: 建议书：L1 全量上下文「按日期增量目录 + 每日 zip 归档」
type: proposal
status: pending_orchestration
author: 风清扬
audience: 王语嫣
date: 2026-08-24
---

# 一、结论先行

- 老朱 08-24 问：「记忆胶囊是否可以按日期命名 + 压缩储存？」——**可以，而且这就是正确结构**。它与「取消每日整份快照」不冲突：取消的是「整份重拷」，不是「按日期」。
- 现状（实测）：压缩已做（ZIP_DEFLATED，08-23 整份 770MB→75MB ≈10x）；日期命名只在归档层（`2026-08-23.zip`/`2026-08-24.zip`），热层是 `tool/rel` 平铺、无日期维度；`_archive_old_days()` 期待「日期命名目录」但 `capture()` 写「工具命名目录」→ **归档函数现为死代码**（仅 02:07 迁移时生效一次）。
- 建议：`l1_capture.py` 改为「日期增量目录 + 每日 zip 归档」，锚点复用已拍板的 **06:00**。

# 二、现状实测（非转述）

- 热层 `L1-full/`：claude 171.7MB / codex 161.1MB / hermes 160.7MB / kimi 455.5MB / qwen 0.2MB（合计 ~950MB，hash 去重后 ~903MB）。
- 归档层 `L1-full-archive/`：`2026-08-23.zip` 75.1MB、`2026-08-24.zip` 237.8MB（均为 02:07/02:11 迁移时一次生成）。
- 死代码定位：`capture()` 写 `L1_ROOT/<tool>/<rel>`；`_archive_old_days()` 只认 `L1_ROOT/<YYYY-MM-DD>`（`name.startswith("20")`）→ 现在永远匹配不到，归档不触发。

# 三、正确结构（三层）

- **热层**：`L1-full/<YYYY-MM-DD>/` 当天增量目录——mtime 判重，只放「当天变化文件」，不整份重拷（守住 #491 日增量铁律）。
- **归档层**：每日 06:00 把「昨天目录」zip → `L1-full-archive/YYYY-MM-DD.zip`，删原目录（幂等：已归档过则只删目录不重复 zip）。
- **索引**：`trace-index.md` 按日期 append（已有，保留）。

# 四、与每日审计轮的衔接

- 06:00 同一锚点跑两件事：① 归档昨天（`l1_capture.py`）② 抽数 digest（`daily-audit-digest.py`）。
- 风清扬审计读法：热层当天直读 + 历史天按需解压 `YYYY-MM-DD.zip`（默认不碰冷层，省 token）。

# 五、验收标准

- 改后热层按日期、归档按天 zip、无整份重拷（日增只含变化文件）。
- 归档幂等：重跑不重复 zip、不丢文件；归档后热层只留当天。
- `_archive_old_days()` 重新生效（不再死代码）。
- 历史天 zip 体积随日志压缩比显著下降（目标：不再出现日增数百 MB）。

# 六、建议汇总

| # | 动作 | 对象 | 优先级 |
|:--|:--|:--|:--|
| 1 | `l1_capture.py` 改「日期增量目录 + 每日 zip 归档」 | 黄药师 | P1 |
| 2 | 归档锚点并入 06:00 抽数 | 黄药师 | P1 |