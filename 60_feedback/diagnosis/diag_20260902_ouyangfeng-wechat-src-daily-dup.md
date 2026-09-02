---
type: proposal
status: orchestrated
audience: 王语嫣
date: 2026-09-02
author: 欧阳锋
---

# 建议书：wechat 逐字稿转正管线每日重复生成（散点主因）+ 两项附带发现

## 现象（一句话）

`10_raw/sources/` 里同一批微信公众号逐字稿每天被重新复制一份新日期前缀文件——163 个文件只有 16 个唯一内容，**147 个纯重复**，且以 ~17 个/天的速度继续增长；这些是 Obsidian 图谱"大量散点"的主来源。

## 证据（字节级，欧阳锋 2026-09-02 亲验）

1. 全量清点 `10_raw/sources/src_*_wechat_*.md`：163 文件 / 16 唯一内容（md5 分组），冗余 147；日期分布 08-18(3) → 08-19~08-27(12~14/天) → 08-31~09-02(17/天)。
2. 同 hash 三日文件 md5 逐字节相等（例：`346efef2737b383b` 的 08-31/09-01/09-02 三份 md5 均为 `42a851c5...`）。
3. 该目录占 sources 层 1014 个 md 的 16%，其中 14.5% 是纯重复。
4. 51 个 08-31~09-02 的新重复文件至今 untracked（见附带发现②）。

## 根因（字段级定位）

`kdo-tools/wechat_promote.py:59-62` `promote_transcript()`：

```python
target = SOURCES_DIR / f"src_{date.today().isoformat()}_wechat_{hash_id}.md"
if target.exists():   # ← 去重键里含"今天"，跨天永不命中
    return True
```

去重存在性检查的文件名含 `date.today()`——昨天生成的 `src_2026-09-01_wechat_X.md` 挡不住今天再生成 `src_2026-09-02_wechat_X.md`。**去重结构上注定失效**，不是偶发。注意：#516 修的 `_processed` 去重只覆盖 `promote_case`（case 卡，L110-115），`promote_transcript`（逐字稿）从未有有效去重——08-18 管线上线首日即开始重复。

**与"飞书代班"的关系（对老朱口径）**：此 bug 08-18 就存在，非代班期引入；代班期（08-31~09-02，Kimi 无额度）无人巡检 sources 层，堆积加速到 17/天且无人发现。

## 修复建议

- **R1（止血，黄药师，小改）**：存在性检查改为按 hash 全历史匹配——`any(SOURCES_DIR.glob(f"src_*_wechat_{hash_id}.md"))`。附回归测试（同 hash 两日重跑应 skip）+ assert 生效计数（#426 断言纪律）。
- **R2（清存量，黄药师，先 dry-run + 批量三问）**：删除 147 个冗余文件，保留规则=**引用感知**：有卡引用的 hash 保留被引用日期份（已查实 2 组：`src_2026-08-20_wechat_2404c1658025473c` 被 30_wiki 引用 6 次、`src_2026-08-19_wechat_e7536bf1d8f1a7b1` 被引用 1 次，这两个日期份必须保留）；无引用组保留最早日期份。删前全库 grep 引用对账，删后跑 `kdo index --incremental`。
- **R3（防复发）**：把"同 hash 多日期份"检测加进 vault-integrity-check / 孤岛扫描例行项，重复组 >0 即报警。
- **R4（观察）**：重复文件同内容 16 倍进入检索索引，可能稀释 kdo search 排序——R2 清理后复扫验证。

## 附带发现（建议各立小单）

- **① `90_control/scripts/count_wiki_islands.py` 崩溃**：related 字段为列表型条目时 `clean_link` 收 list 报 AttributeError（L44）——孤岛扫描器当前不可用，修 R2 前想拿孤岛基线得先修它。
- **② vault backup 自动提交停摆**：最后一次 `vault backup` commit = 2026-08-26 22:57（d4dbfc582），此后 51+ 文件 untracked 至今——数据安全破口，需排查 backup 定时任务。
- **③ `.obsidian/` 配置不在任何备份面（老朱"点全变黑"根因）**：`.obsidian/` 从未入 git（ab2bd33ba 移除跟踪）、git bundle 只含跟踪文件、L1 归档不采配置层（实测 08-29/30/31 zip 内零 .obsidian）、坚果云从未同步 wiki（#589 证据#6）、VSS 仅存 5/15 影子且其中无 `.obsidian`（实测）——**08-31 整树消失事故中 `.obsidian` 被一并删除，git bundle 恢复无法带回，图谱 colorGroups 永久丢失**（现 graph.json `colorGroups: []`）。用户今晚首开 Obsidian 触发生成默认配置（全目录 mtime=09-02 01:03），全部节点退化为默认色。建议：把 `.obsidian/graph.json` 等关键 UI 配置纳入备份面或恢复 git 跟踪（`.obsidian` 内仅排除 workspace.json 等易变文件）。配色方案需重建（旧方案无副本可考）。

## 验收口径

- R1：构造同 hash 两日重跑用例，第二次输出 "⏭️ 已转正" 且 sources 目录零新增。
- R2：清理后 `src_*_wechat_*` 文件数 = 16（每 hash 恰 1 份），全库 grep 零断引，`kdo lint` 无新 ERROR。
- R3：integrity check 输出含 dup-hash 计数行。

---

## 王语嫣处置注记（09-02 21:38 补）：主证据件——R1/R2 已由 #601 落地（reviewed PASS A-），决策点经 diag_20260902_ouyangfeng-pending-decisions 裁定（点2 上行挂起至 09-09），status 漏翻，补正 orchestrated。
