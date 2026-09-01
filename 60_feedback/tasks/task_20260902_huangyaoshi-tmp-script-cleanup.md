---
id: task_20260902_huangyaoshi-tmp-script-cleanup
title: tmp 一次性脚本清理（散点审计 R5，P1）：根目录 59 + kdo-tools 25
seq: 603
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
priority: P1
updated_at: '2026-09-01T17:55:21.569718+00:00'
instance: huangyaoshi
---

# #603 tmp 脚本清理

## 背景

风清扬审计 P1：vault 根目录 59 个 `_tmp_/_debug/_fix/tmp_*` 散落脚本与 txt（`_fix_source_refs_step1/2/3/final.py` 四版并存等），`kdo-tools/tmp_*` 25 个一次性脚本（3 个转写变体、3 个抓视频版本、1 个读凭据的 `tmp_publish_md.py`）。

## 范围

1. **前置（必须先做）**：`_tmp_skill_health.json`（29KB）被 `60_feedback/diagnosis/建议书_20260901_skill健康度勘察与检测方法论.md:146` 引用——先把引用改指归档后位置（或把该文件归档到 `90_control/baseline/` 并同步改引用），再动其余。
2. 根目录 59 个 + `kdo-tools/tmp_*` 25 个：逐个判定——有正式替代品的归档 `_tmp/`（已在 .gitignore 则直接移入），含凭据读取逻辑的 `tmp_publish_md.py` 单独标注随 #600 处置口径。
3. **归档不删除**：移 `_tmp/` 或隔离区，保留 git 历史可追溯。

## 安全栏

- 批量三问（dry-run 全量清单 → 范围声明 → 非空不覆盖）。
- 每个被移动文件先 grep 全库引用（含 .md 引用与脚本 import），有引用的列入「例外保留」清单随执行报告交付，不强行移动。
- 不碰 `_tmp/` 以外任何 30_wiki/40_outputs 正文内容。

## 交付物

归档后目录清单 + 例外保留清单 + 引用对账表 + 执行报告五字段。

## 验收

欧阳锋终审：根目录 `_tmp_/_debug/_fix/tmp_*` 清零（例外清单除外）+ `_tmp_skill_health.json` 引用链不断 + 抽查 5 个归档文件可追溯。
