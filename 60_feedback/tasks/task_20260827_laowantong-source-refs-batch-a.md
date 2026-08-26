---
id: 557
assignee: laowantong
status: pending_review
updated_at: '2026-08-26T18:50:38.178442+00:00'
version: v0.1
instance: laowantong
code_files: []
---

# #557 死引治理批次 A：inbox 原稿归档 + 引用校正（934 条/319 卡）

- **任务号**：#557
- **状态**：queued
- **assignee**：laowantong（欧阳锋批次验收）
- **优先级**：P1（死引率 24.2%，本批占 91.2% 且修复成本最低——机械动作不补内容）
- **立项**：2026-08-27 王语嫣（#543 治理方案裁定：批次 A 采纳，口径=**归档到 10_raw/sources/ 再改引用**，不原位改——inbox 是流转区不是存储区，引用长期指 inbox 会继续腐坏；KF-020 归档先例同口径）
- **依赖**：#551 完成后开工（老顽童单线程）

## 任务

1. **数据源**：`60_feedback/analysis/source-refs-health-latest.json`（剥锚后口径）筛「指向 00_inbox 的死引」934 条/319 卡
2. **逐条处置**：确认原稿在 00_inbox 何处 → `git mv` 归档到 `10_raw/sources/`（按域/主题归子目录）→ 卡片 source_refs 改指向归档后路径
3. **分批**：按域分批（参照 #426 模式），每批落盘即 commit（E040），批次报告含：处理数/归档目标/改卡清单
4. **原稿真不在 inbox 的**（引用虚空且找不到原稿）：单独列清单报王语嫣，不硬修不删引用

## 建模方案（L1 出牌，2026-08-27 老顽童）

依赖链：`[素材] → [边界] → [结构] → [过程] → [质量]`

| 位 | 牌号 | 一句话理由 |
|:--|:--|:--|
| 素材 | #2 先全文扫描再选策略 | dry-run 先行：932 条 inbox 死引剥锚后实测——633 原稿在（91 个唯一文件）/299 真亡；数据源声称「剥锚后口径」但实际未剥 ` Lxxxx-Lxxxx`/`#L`/` - src_unknown` 三种锚（checker 只剥 `:NN`），637 条死引是锚点格式误报 |
| 边界 | B1 半套修改=静默失效 | **关键拦截**：91 个待搬文件被全库 850 条引用（含 217 条活引用），只改死引清单=制造 850 条新死引（P-29 级事故）。必须搬文件+全库引用改写一体执行 |
| 结构 | #11 先 dry-run 再 apply | 范围声明：搬 91 文件（00_inbox→10_raw/sources/<主题子目录>），改 ~850 条 source_refs（只动 frontmatter 该字段，锚点保留并规范化为 `:NN-MM` 形，`- src_unknown` 污染后缀剥除），不动正文 |
| 过程 | #12 先抽样 10% 再放量 | 最小子目录批先导（单文件批），yaml.safe_load+路径存在性双验 → 再按子目录分批放量 |
| 过程 | P-31 回退点 | 批量前 `kdo snapshot` 打 tag |
| 质量 | #14 先跑脚本确认 | 验收=check-source-refs 重扫 vs 1024 基线差集对账，不凭脚本自报 |
| 质量 | L11 清单三问 | 批次报告附机读 TSV（卡→旧路径→新路径），判定=路径存在性可独立复跑 |

**299 条真亡引用**：原稿不在 inbox（管项目 69/解放思想探索营 39/半肥猫开放麦 33 等），按任务边界不硬修不删，单独出清单报王语嫣。

## 边界

- 只动「指向 00_inbox」的死引；reviewed 卡的死引属批次 B（另立单，不走本批）
- 00_inbox 只增不删铁律不适用本条——归档搬运（git mv 留痕）是标准流转，不是删除
- 不动卡片正文内容，只改 source_refs 字段

## 执行报告（完成后回填）

**改动文件**（清单）：`30_wiki/` 348 卡 source_refs 改写（逐卡见 `60_feedback/tasks/task_20260827_laowantong-source-refs-batch-a/manifest-cards.txt`）；91 原稿 git mv 至 `10_raw/sources/<主题子目录>/`（见 `manifest-renames.txt`）；`40_outputs/code/scripts/src-refs-archive-migrate.py`（新工具，已登记 README）；`60_feedback/analysis/source-refs-health-latest.{json,md}`（重扫产物）；批次报告+真亡清单（`60_feedback/tasks/task_20260827_laowantong-source-refs-batch-a/`）
**完成内容**（一句话）：91 个 inbox 原稿归档 10_raw/sources，850 条 source_refs 同步改写（含锚点规范化 `:NN-MM`、多区间拆行、P-29 孤儿污染清除），refs_missing 从 1024 降至 267（inbox 死引 932→178），299 条真亡引用列清单报王语嫣。
**验证**（命令+输出）：
  - `python 90_control/scripts/check-source-refs.py --report-dir 60_feedback/analysis` → refs_missing 1024→267 / inbox 死引 932→178 / refs_line_anchor 2→728 全 alive（数字见批次报告对账表，可独立复跑）
  - 每批执行后 `yaml.safe_load` 全量验证被改卡 frontmatter 可解析（脚本内置，零 FAIL 才写盘；试点批额外全路径存在性核验 ALL_EXIST=True）
  - 差集对账：处理 850 条 vs 下降 754 条——差异来源在批次报告「差集口径说明」如实拆解（折叠锚点重复计数/拆行粒度/嵌套拍平），manifest 机读文件支持第三方复算
**未做项**（边界）：①299 条真亡引用按任务边界未动，清单报王语嫣（`gone-refs-report.md`）②口喷在途文件 `:A` 新型锚点 6+ 条未动（文件 git 未跟踪+checker 不识别，建议归 #543 族）③reviewed 卡死引的内容级修复属批次 B ④遗留 267 条 missing 中的非 inbox 存量（https 外链/编码残缺文件名等）不属本批
**需要谁动作**：欧阳锋批次验收（重点审：批次报告「⚠️ 事故自报」节——收尾 commit 误扫入 6 个他方未提交改动含 zhu-time-os.md 审查记录，未做回退手术，需原作者认领）；王语嫣裁定真亡清单处置
**⚠️ 事故自报**：收尾 commit `5c2555e44` 误用 `git add -A` 扫入 6 个他方未提交改动（含 zhu-time-os.md 未提交审查记录），因撞见实例活跃（index.lock）未做回退手术防丢对方写入，全量可见可认领；handle-the-business 批因 lock 撞车裂成两 commit（`03ae9f80e`+`18bf24cf6`，后者带 14 个 wechat 管道自动产物）。教训已记 friction-log：批次 commit 永远枚举显式路径。

## 验收

- 每批 commit + 批次报告；全部批次完成后 check-source-refs 重扫，缺失数从 1024 基线的下降量 ≈ 本批处理量（差集对账）；欧阳锋批次验收

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 2 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（「未提交审查记录」）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）
