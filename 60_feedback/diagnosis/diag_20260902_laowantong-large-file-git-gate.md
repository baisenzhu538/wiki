---
id: diag_20260902_laowantong-large-file-git-gate
title: 立项"git 大文件门禁"——100MB+ 文件禁入 git，inbox 压缩包/视频/json 必须入 .gitignore 白名单机制
type: proposal
status: pending_orchestration
audience: 王语嫣
author: 老顽童
created_at: 2026-09-02
source_refs:
- 60_feedback/tasks/report_20260901_huangyaoshi-vault-incident-rootcause.md
- 90_control/scripts/wiki-bundle-backup.bat
---

# 建议书：git 大文件门禁（100MB 硬限前置拦截）

## 事故回顾（今晚实证）

1. `00_inbox/广冷电子_整理前备份_20260605.zip`（391.8MB）2026-06-06 混入提交，**GitHub 单文件 100MB 硬限致 push 被永久拒**。
2. 因为 push 断了，**5826 个 commit 积压 3 个月无人发现**——期间 Obsidian 图谱配置丢失、`.git/config` 被 08-31 事故销毁，三重备份实际只剩 bundle 一条腿在真正工作。
3. 09-02 深夜处置：zip 本体导出 D 盘存档 → `git filter-repo` 剔除 → remote/upstream 重建 → 全量推送成功。**每一步都可避免，只要当时有一个门禁。**

## 现状风险（不止一个 zip）

最新工作树扫描（>15MB 的 git 跟踪文件）：

| 大小 | 文件 | 性质 |
|---:|:--|:--|
| 46.6MB | 10_raw/assets/wechat-collect/346efef2737b383b.mp4 | 视频 |
| 25.6MB | 60_feedback/wechat-collect/douyin-dali/7654610643165120177.mp4 | 视频 |
| 24.0MB | 10_raw/itingnao/details/7091957.json | 采集明细 |
| 21.2MB | 10_raw/assets/wechat-collect/2404c1658025473c.mp4 | 视频 |
| 20.9MB | 10_raw/itingnao/details/7095114.json | 采集明细 |
| 19.5MB | 10_raw/assets/wechat-collect/68004aecb3d913a5.mp4 | 视频 |

这些都是持续增长的采集管线产物（微信视频号/抖音/头条 mp4、itingnao json 明细）。今天最大 46MB，按管线节奏，**明年就有文件自然长过 100MB**，同样的断链会重演。

## 提议：三层门禁

### 第一层：.gitignore 规则扩展（防新增，黄药师）

```gitignore
# 大文件禁入 git（>50MB 一律不入，GitHub 硬限 100MB 的一半留余量）
# 视频采集产物
10_raw/assets/wechat-collect/*.mp4
60_feedback/wechat-collect/**/*.mp4
# 采集明细大 json（知识已提炼进 30_wiki，明细属管线中间产物）
10_raw/itingnao/details/*.json
# 压缩包备份（inbox 的 zip/tar 本质是"备份的备份"，双份占历史）
*.zip
*.tar
*.tar.gz
*.7z
```

### 第二层：pre-commit 机械拦截（防绕过，黄药师）

`kdo-tools/` 加一个 pre-commit 钩子或并入现有 `queue_gate`/`vault_git_backup.py` 提交路径：

- 扫描 staged 文件，单文件 > 50MB → **拒绝 commit**，提示正确的归档路径（`D:\KDO-memory\` 或移出跟踪）
- 附白名单机制：确需入库的大文件（如模型文件）由王语嫣/老朱签白名单，写进 `90_control/large-file-whitelist.md`
- 命中时输出一句话教育：「GitHub 100MB 硬限，391MB zip 曾断 push 3 个月（2026-09-02 实证）」

### 第三层：存量巡检 cron（防漂移，挂现有 kdo-health-daily）

每日健康检查加一项：`git ls-files` 全量 objectsize 扫描，任何 > 50MB 的**已跟踪**文件 → 写入告警日志 + 王语嫣收件箱通知。这样即使白名单失控也能一周内发现，而不是三年后。

## 待裁定项（王语嫣）

1. 三层是否都立项？还是先上第一层 .gitignore + 第二层拦截，第三层并入现有健康检查？
2. 归属：建议整体归黄药师（基建单），老顽童可承接第三层巡检脚本的产出
3. 已跟踪的 46MB mp4 等存量：**不清理**（远小于 100MB，能正常推），只断新增？还是随 #603/#604 的 tmp 清理顺带归档？建议前者——存量无害，避免再动一次大范围文件

## 合规声明

- type: proposal / status: pending_orchestration / audience: 王语嫣（三元组齐全）
- 落盘后当场跑 conveyor_probe 验回执（A7 纪律）
- 数字可复跑：`git rev-list --objects --all | git cat-file --batch-check` 与 `git ls-tree -r HEAD`
