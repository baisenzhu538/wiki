---
id: task_20260902_huangyaoshi-wechat-promote-dedup-fix
title: wechat_promote 去重根治 + sources 存量 147 份重复处置（散点审计 R2/R3 + 欧阳锋建议书，P0）
seq: 601
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
priority: P0
updated_at: '2026-09-02T01:25:00+08:00'
---

# #601 wechat_promote 去重根治 + 存量去重

## 背景

`kdo-tools/wechat_promote.py:59-62` 去重键含 `date.today()`，跨天重跑必复制。欧阳锋字节级实证：`10_raw/sources/src_*_wechat_*.md` 163 个文件仅 16 个唯一内容，**147 个纯重复**，每日 +17 继续增长（bug 自 08-18 上线即存在）。建议书：`60_feedback/diagnosis/diag_20260902_ouyangfeng-wechat-src-daily-dup.md`。

## 范围（四件）

1. **修 bug**：`promote_transcript()` 存在性检查改为按 hash 全历史匹配——`any(SOURCES_DIR.glob(f"src_*_wechat_{hash_id}.md"))`。
2. **回归测试**：同 hash 跨天重跑必须 skip（断言生效计数，#426 断言纪律）；红绿自证。
3. **seen_links.txt URL 归一化**：`&`/`&amp;`/exportkey 变体归一后查重（风清扬 P0-B-3）。
4. **存量 147 份处置（引用感知）**：
   - 有卡引用的 hash 保留**被引用的那份**（欧阳锋已查实 2 组：`src_2026-08-20_wechat_2404c1658025473c` 被引用 6 次、`src_2026-08-19_wechat_e7536bf1d8f1a7b1` 被引用 1 次——动手前重新 grep 对账，以实测为准）；
   - 无引用组保留最早日期份；
   - 冗余份**不直接删**——移到 `90_control/.sandbox/quarantine-20260902/sources-dup/` 隔离区，观察 7 天无碍后清除；
   - 处置后跑 `kdo index --incremental`。

## 明确不做（王语嫣裁定）

- **inbox 原件不删不移**：`00_inbox/wechat-collect/src_wechat_*` 是 case 卡 `source_refs` 的锚点（F-KDO-015 不断溯源链）。风清扬 R2 的「promote 后移走 inbox 原件」裁定驳回——重复治理只动 10_raw/sources 层。
- 不动 30_wiki 任何卡片正文。

## 安全栏

1. 批量三问：dry-run 输出全量清单 → 范围声明 → 隔离区非空不覆盖。
2. 删/移前全库 grep 引用对账（含 pending-cards 与 30_wiki），对账表附执行报告。
3. 引用路径含中文，清单生成用 `git ls-files -z` / Python NUL 分隔（铁律 §10）。

## 验收

欧阳锋终审：bug 修复后连续两天跑 promote 零新增重复 + 回归测试过 + 147→0（隔离区计数一致）+ 被引用 2 组实测未断链。
