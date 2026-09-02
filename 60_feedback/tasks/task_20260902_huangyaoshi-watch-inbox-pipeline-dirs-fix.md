---
id: task_20260902_huangyaoshi-watch-inbox-pipeline-dirs-fix
title: watch_inbox 扫描面回补管线落点子目录（#605 裁剪误伤：wechat-collect 等管线落点出扫描面，05:47 四件静默漏登记实证）
seq: 619
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 老朱 09-02 问「偶遇→inbox→拉起工作流这条线正常吗」→ 王语嫣逐环实测发现第二环断裂
reviewer: 欧阳锋
instance: huangyaoshi-kimi
updated_at: '2026-09-02T14:42:04.561864+00:00'
evidence: 60_feedback/tasks/task_20260902_huangyaoshi-watch-inbox-pipeline-dirs-fix.md
---

# #619 watch_inbox 扫描面回补（黄药师）

## 背景（实测证据）

#605 dispatch 收口时把 watch_inbox 扫描面裁成「00_inbox 顶层文件 + pending-cards/」（watch_inbox.py L81-87）——但 wechat/BV 管线的实际落点是子目录：`wechat-collect/`、`video_transcripts/`、`video_transcripts_small/`。实证：`00_inbox/wechat-collect/src_wechat_*.md` ×4（09-02 05:47 采集落盘）未出现在 INBOX-PENDING 任何一行（grep 0 命中）——静默漏登记。

裁剪的原始目的（防 863KB dispatch 巨件）仍成立：Handle/、_vlm_output/、ocr_ingest 等大目录树**继续排除**。

## 任务

`kdo-tools/watch_inbox.py` 扫描面改为：顶层文件 + 白名单子目录（`pending-cards/`、`wechat-collect/`、`video_transcripts/`、`video_transcripts_small/`），其余子目录不扫。白名单写成常量便于日后增删。

## 验证

- 改完实跑一次扫描：05:47 的 4 件 wechat-collect 应被登记进 INBOX-PENDING（补登记或验证幂等均可）
- 大目录（Handle/ 等）确认不在扫描结果里

## 交付

- diff + 实跑登记证据 + 执行报告
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 619）

## 执行报告（2026-09-02 黄药师）

**交付物**：`kdo-tools/watch_inbox.py`（扫描面白名单化：`SCAN_SUBDIRS=("pending-cards","wechat-collect","video_transcripts","video_transcripts_small")` 常量 + `SKIP_SUBDIR_PARTS={"knowledge"}` + `_` 前缀目录段跳过；死常量 `EXCLUDE_DIRS={"wechat-collect"}` 移除，docstring 同步）；`kdo-tools/tests/test_watch_inbox.py` 新增 `test_scan_whitelist_subdirs` 回归；`90_control/notification-coverage-matrix.md` 行 9 同步（§3.19）。

**完成内容**：scan() 由「顶层+pending-cards 硬编码」改为「顶层+白名单子目录 rglob」，白名单内跳过 `_` 前缀目录段（_needs_rerun/_processed）与 `knowledge/`（wechat_promote 中间产物，case 卡另有 pending-cards/ 落点，扫了=重复派发——原 EXCLUDE_DIRS 排除 wechat-collect 的防重意图在目录内消化）。实跑前把 12 个存量未跟踪文件按 mtime<09-02 05:00 播种入 `.kdo/inbox_state.json`（均已由 wechat_promote 消费过、case 卡在 pending-cards 已在册，防 11 件陈旧 src 重复登记冲看板；其中 merge_ted.py 不在 WATCH_EXTS 本就不会登记，播种键无害冗余）。

**验证**：①`python kdo-tools/watch_inbox.py` 实跑——输出「待编排看板更新: +6」，05:47 批次 6 件（任务单记 ×4，实测 mtime 09-02 05:47 共 6 件：2404c165/346efef2/5291b61b/68004aec/e7536bf1/fe604398）全部登记进 production-queue.md INBOX-PENDING（L583-588），王语嫣收件箱推送 6 项；②重跑 exit 0 零新增（幂等）；③INBOX-PENDING 段 grep 无 Handle/_vlm_output/knowledge/_needs_rerun 路径（仅 2 处历史行含中文「知识管理」字样，非目录）；④`python -m pytest kdo-tools/tests/test_watch_inbox.py -q` 4 passed（含新增白名单回归）。

**边界**：①pending-cards/_processed 自此出扫描面（原 rglob 会扫）——已 processed 件不再因改动重登记，存量已在 state 无重报；②白名单只认四个目录名，未来新管线落点需手工加 SCAN_SUBDIRS（任务单口径「写成常量便于增删」已满足）；③播种是一次性基线对齐，已在上文声明，删 state 键可回滚；④未动 dispatch 台账开关、通知/看板函数逻辑。

**需要谁动作**：欧阳锋终审；王语嫣消费看板新增 6 行待编排。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 3 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
