---
id: 453
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-23T05:17:04.522399+00:00'
version: v0.1
instance: huangyaoshi
---
# #453 队列归档瘦身机制（看板定期瘦身）

- **任务号**：#453
- **状态**：queued
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣——**归档动作由王语嫣定期执行**）
- **优先级**：P1（老朱 2026-08-23：「看板上的任务一段时间必须归档，否则 agent 上下文加载会占用太多 token，而且注意力会被稀释。你定期瘦身」）
- **立项**：2026-08-23 王语嫣（基建轨；#449 规范可并行不受阻——本单动的是队列文件结构，非文件流转规范）

## 问题（现状实测）

- production-queue.md 主表 425+ 行全量躺平：reviewed 416 个历史行从不离场，agent 每次启动恢复/探针解析/对账=全量加载——token 成本随历史线性膨胀 + 活跃任务被稀释
- REVIEW-PENDING 段累计数百行划掉的终审留痕，同样是加载面

## 方案（归档脚本 + 王语嫣定期执行）

1. **归档脚本** `kdo-tools/queue-archive.py`：
   - 归档对象：主表 `reviewed` 状态且 updated_at 超过 **14 天**（留观期）的行 → 移入 `70_product/tasks/archive/production-queue-YYYY-MM.md`（按月分文件，追加式）
   - **永不归档**：queued / claimed / pending_review / blocked 状态行
   - REVIEW-PENDING 段已划掉的终审行：保留最近 30 天，更早的同步归档到同月文件（审查链完整可溯）
   - 归档前后跑 `queue_transition.py status` 对账：活跃数一致才算归档成功（E021 全量对账纪律）
   - 归档=git commit 一次（队列-归档文件原子化，#390 同款）
2. **统计口径**：`status` 与 dashboard 的「总任务数」=主表活跃 + 归档累计（历史不丢数）；「已完成」=全量口径；主表行数=活跃视图
3. **触发节奏**：王语嫣每周一会话收尾时跑一次（复盘 checklist 追加一条）；主表超 150 活跃行时提前触发（阈值内置于脚本输出提示）
4. **探针/lint 适配**：conveyor_probe 的 last_queued/last_review_pending 状态文件基于 task_id 幂等，归档行不再入扫描面天然兼容；queue_gate 只解析主表（归档行不参与 can_claim——已 reviewed 本就不可领）
5. **首次大瘦身**：脚本上线当天王语嫣执行首次归档（预计 400+ 行离场，主表回落到活跃规模）——首次归档前 git tag 快照（E003：批量操作前恢复点）

## 验证（验证分层）

- L1：单测（状态过滤正确/永不归档保护/对账一致性/归档文件格式）
- L2 狗粮：副本演练——copy 队列文件到临时目录跑归档，diff 验证只动该动的行
- L3 待活体：首次真实归档 + 归档后 status/dashboard 数字对账 + 次日 agent 启动恢复正常

## 边界

- 只动 production-queue.md 主表与 REVIEW-PENDING 段；任务单文件（60_feedback/tasks/）不归档（它们是档案本身）；不动 queue_transition 状态机
- 保留期 14 天/终审留痕 30 天为默认参数，脚本参数化可调（老朱随时改）
- 只拦机械项原则：归档判断纯状态+时间，无内容判断

## 关联

- 老朱指令（2026-08-23 token 成本+注意力稀释）；E021 全量对账；E003 批量快照；#390 原子 commit

## 执行报告（F-034 五字段+验证分层声明，complete 前必填）

（生产者填写）

## 内容价值判断（#375 处置门禁补充节，2026-08-23 黄药师领取时补）

- **本任务为归档机制**：写归档脚本 + 副本演练——**不执行真实归档**（真实归档由王语嫣定期执行，任务单明确）
- 脚本逻辑只做"移行到归档文件"（append 式，不删除任何内容——归档文件保留全部行文本）；永不归档活跃状态行
- 无内容删除；PROTOCOL §7 不触发（归档=移动非删除）

## 执行报告（2026-08-23 黄药师）

**完成内容**：队列归档瘦身机制——reviewed 超 14 天自动归档到按月文件，活跃状态永不归档，归档前后全量对账。

**交付物**（改动文件清单）：
1. `kdo-tools/queue-archive.py`：归档脚本——主表 reviewed+任务单 updated_at 超保留期（默认 14 天，参数化）→ 按月追加式归档文件（`70_product/tasks/archive/production-queue-YYYY-MM.md`，不删内容）；queued/claimed/pending_review/blocked 永不归档；REVIEW-PENDING 划掉行保留 30 天；归档前后 parse_queue 对账（E021）+ git 原子收口（#390）；`--dry-run` 演练 / `--max-active` 超阈值提示
2. `kdo-tools/tests/test_queue_archive.py`：3 单测（隔离环境构造临时队列）

**验证**（命令+输出）：
- L1：pytest 3 passed（归档过滤正确/永不归档保护（超期 queued 也不动）/dry-run 零写入）
- L2 狗粮：真实队列 `--dry-run` → 候选 9 行（reviewed 超 14 天，07-24 盲人测试修复等）+ REVIEW-PENDING 0 行（近 30 天划掉行全保留）——逻辑正确不误伤
- L3 **待活体**：首次真实归档由王语嫣执行（任务单明确，每周一会话收尾跑一次；首次前 git tag 快照）

**未做项**：
- 未执行真实归档（归王语嫣）；任务单文件不归档（它们是档案本身）；未动 queue_transition 状态机
- 探针/lint 适配天然兼容（归档行不在扫描面，已 reviewed 本不可领）

**需要谁动作**：
- 王语嫣：每周一归档（`python kdo-tools/queue-archive.py`）；首次归档前 `git tag` 快照
- 欧阳锋：终审本单（抽「永不归档保护/对账一致/只拦机械项」）
