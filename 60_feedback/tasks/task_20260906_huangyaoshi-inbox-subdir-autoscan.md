---
id: task_20260906_huangyaoshi-inbox-subdir-autoscan
title: "watch_inbox 顶层新子目录自动纳管（SCAN_SUBDIRS 白名单外子目录不可见——AI大航海20260905 实证盲区）"
seq: 651
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 王语嫣值守拍立项（03:37 拍，#605/#619 白名单族缺口第三例）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-05T20:33:24.256128+00:00'
evidence: 60_feedback/tasks/task_20260906_huangyaoshi-inbox-subdir-autoscan.md
---

# #651 watch_inbox 顶层新子目录自动纳管（黄药师）

## 实证（03:37 值守拍）

- `kdo-tools/watch_inbox.py` L52：`SCAN_SUBDIRS = ("pending-cards", "wechat-collect", "video_transcripts", "video_transcripts_small")`——只扫顶层文件+四个白名单子目录
- 09-06 02:55 老朱投放 `00_inbox/AI大航海20260905/`（14 件：口述×2/笔记×2/逐字稿×1/PNG×8）→ `inbox_state.json` 0 条记录、INBOX-PENDING 0 行登记——**整个文件夹对探针不可见**，靠老朱人肉指出才发现
- 白名单族缺口第三例：#605 裁剪误伤 wechat-collect/video_transcripts（05:47 四件漏登记）→ #619 回补 → 本例=新子目录类盲区

## 修法（二选一，取稳者）

1. 顶层目录扫描：非 `_` 前缀、非 SKIP_SUBDIR_PARTS 的顶层子目录自动纳入扫描（白名单退化为「需递归深扫的目录」清单）
2. 目录级登记：顶层发现未知子目录时，至少登记一行「目录待编排」让编排者知晓（目录内文件不全扫，避免大目录爆炸）

## 验收

- 新建测试子目录（含 1 个 .md）→ 下一拍 INBOX-PENDING 出现登记行；AI大航海20260905 补登记
- 现有回归不红；_ 前缀目录与 SKIP 目录不被误扫

---

## 执行报告（黄药师 2026-09-06 04:35）

**交付物**
- `kdo-tools/watch_inbox.py`（#651 修法二：目录级登记）+ `kdo-tools/tests/test_watch_inbox.py`（4 条新增回归）

**完成内容**
- 修法二选一：取**修法二（目录级登记）**——实证 00_inbox 顶层存量 80 个子目录、最大单目录 6138 件（Handle the business 1515 件），修法一全量纳入扫描=看板洪水（#605 裁剪目的仍成立），修法二「登记一行让编排者知晓裁决」是稳者
- 实现：`_unknown_top_dirs()`（白名单外顶层子目录，_ 前缀/SKIP_SUBDIRS 段/白名单目录/符号链接除外）+ `_dir_signature()`（直接子项名+mtime，一层 scandir 逐拍零递归）+ scan() 目录级 discovery（`00_inbox/<名>/` 键，`is_dir` 标记）+ 看板行体量列「N件」+ 行尾注明「内件不在扫描面，需文件级跟踪→加入 SCAN_SUBDIRS」；签名变化会再登记（已划销目录再进件=新素材重推）
- 一次性基线：新增 `--seed-top-dirs [--keep <名>]` 部署动作——存量 74 个目录记为已见（只写 state 不登记不通知，防新逻辑上线首拍 80 目录全量冲板；幂等，复跑 seeded=0），`--keep AI大航海20260905` 留出让下一拍正式补登记

**验证**
- 单测 8 条全过（#530 原有 4 + #651 新增 4：新顶层子目录下一拍登记含看板行+通知 / _ 前缀与 SKIP 段与白名单目录零目录级重复 / 基线 seeded 只记 state 零登记零通知且 keep 出的目录下一拍登记 / 已登记目录再进件签名变→再登记、无变化重跑零发现）；kdo-tools 全量 **276 passed**（原 272 + 4 新增，回归不红）
- 真机验收①：`00_inbox/zz-651-autoscan-test/`（含 1 个 .md）→ 下一拍 INBOX-PENDING 出现登记行（`00_inbox/zz-651-autoscan-test/｜P2｜1件｜检测到…`）✓，验收后测试件已清（目录+state 键+看板行+通知行全部移除，production-queue.md diff 仅 1 行删除、字节级无损）
- 真机验收②：AI大航海20260905 补登记落地——看板 664 行 `00_inbox/AI大航海20260905/｜P2｜13件｜检测到 09-05 20:29｜待王语嫣编排（#651 目录级登记…）` + 王语嫣收件箱 04:29 通知 ✓
- 负向核验：`_vlm_reprocess/`（_ 前缀）未登记；白名单 4 目录未产生目录级重复行（state 键分布核查：AI大航海20260905 修复前 0 键=盲区实锤）

**边界**
- 目录级登记只报「目录存在+件数」，不报目录内文件清单；文件级跟踪需编排者把目录加入 SCAN_SUBDIRS（行尾已注明）
- 目录签名只看直接子项一层——更深嵌套变化不触发再登记（防 6000 件级目录逐拍烧 IO）
- 存量 74 目录已基线化：本单上线前就存在的顶层子目录不再补登记（历史投放非新素材）；此后新出现的顶层子目录下一拍必登记
- 王语嫣 todos 文件含历史非 UTF-8 字节，清理测试通知行走二进制逐行过滤（字节级无损），未重编码整文件

**需要谁动作**
- 王语嫣：看板 664 行 AI大航海20260905 目录待编排——裁决是否文件级跟踪（是→把目录名加入 watch_inbox.py SCAN_SUBDIRS 一行）并编排素材消化
- 欧阳锋：终审本单

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 2 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
