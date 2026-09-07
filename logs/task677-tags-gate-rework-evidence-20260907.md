# #677 tags 门禁返工验证证据（2026-09-07 huangyaoshi · 第二轮，欧阳锋 FAIL P1×2+P2 返工）

## 返工范围对照（欧阳锋终审意见书 → 修正）

| 审定问题 | 修正 |
|:--|:--|
| P1-1 普通卡 5-8 词量把 audience:/scene:/skill-level: 前缀维度计入词量（误伤 504 张候选） | `pre_submit.py` `_check_tags` 普通卡分支改计内容词（非 `:` 条目）5-8，与 dk 卡核心词口径对称（commit `1a7a2e2`） |
| P1-2 「活体复现」存在性核查失效——`4179de376^` 的 0/0 是文件不存在非零 tags | 删除该误证；改用 git 历史中真实存在的零 tags 卡版本活体复现（下文 §3） |
| P2 标杆卡 meeting-iceberg「合规」建立在错误计数上 | 按 #498 内容词口径重验：4 内容词 <5，**如实改判不合规**，不再作合规样板（§5） |

## 1. TDD 红→绿

- **红**（修前跑，4 failed 12 passed）：`test_dimension_prefixes_not_counted_passes`（graph-rag 同构 10 条目被误报）/ `test_meeting_iceberg_shape_below_band_warns`（6 条目被错放行）/ `test_normal_card_below_band_warns` / `test_normal_card_above_band_warns`——失败原因全部=总条目计数口径，与欧阳锋 P1-1 定位一致
- **绿**：16/16 passed（新增 2 例口径回归 + 4 例改口径适配 + 原 10 例不动）
- **全量回归**：KDO 仓 `655 passed, 1 skipped`（156.69s，零红）

## 2. P1-1 根治实证（graph-rag 不再误报）

- `30_wiki/concepts/graph-rag.md` tags 直读：3 前缀维度（audience:general / scene:reference / skill-level:intermediate）+ 7 内容词（知识库/KDO/检索增强/索引/工作流/工具/方法）= 10 总条目
- 修后 `_check_tags` 单测路径 → 0 issue；`run_pre_submit` 接线路径端到端 → `tags_gate_issues=0`（passed=1，另 5 条 issue 属 outlink/body_src_unknown/concept_crosscheck/source_reachability/quality_score 其他门禁）
- 与 #498 复审判词对齐（`task_20260824_laowantong-dk-tags-word-count-caliber.md` 复审记录：「graph-rag tags 块实测 7 内容词…5-8 区间达标」）

## 3. P1-2 修正——真实缺陷态活体复现（非合成）

- **误证删除声明**：原证据 §验证记录 4「`4179de376^` grep `^tags:` 计数 0/0」作废——欧阳锋核查实锤该提交中两 dk 卡文件不存在（`git show 4179de376^:<卡>` 报 `path does not exist`），0/0 是「文件不存在」非「零 tags」。两 dk 卡创建时（4179de376）即带 7 条 tags，零 tags 状态从未进入这两卡的 git 历史。
- **新活体实证**：git 历史扫描（30_wiki/concepts + 30_wiki/frameworks 前 100 文件的创建提交版本）发现 **49 张真实零 tags 卡版本**；取 `30_wiki/concepts/ai-collaboration-mindset-shift.md` @ 创建提交 `3051d146e`（type=concept，frontmatter 无 `tags:` 行【实证】）→ `git show` 物化真实历史版本 → `_check_tags` 返回 `warning | tags | No tags found. Every card needs at least audience:xxx + scene:xxx.（软期至 2026-09-14）`——缺陷态为 git 历史真实存在，非合成卡。

## 4. 误报候选独立复算（互证欧阳锋 504）

- 扫描口径：`30_wiki/**/*.md`（排 `_archive`），多行 tags 块解析，条件「5 ≤ 内容词 ≤ 8 且 总条目 > 8」→ **546 张**（2026-09-07 现行态）
- 与欧阳锋 504 的差集=扫描范围（本扫含 agent-specs/usage-logs 等 1633 张之外的有 tags 文件，全库 frontmatter 卡 2970 张）；两数独立复算互证 P1-1 误伤为数百张量级

## 5. P2 如实改判——标杆卡 meeting-iceberg

- tags 直读：2 前缀（audience:general / scene:meeting）+ 4 内容词（机制/框架/工具/复盘）= 6 总条目
- 修后判定【实证】：`run_pre_submit` 端到端 `tags_gate_issues=1`，warning「普通卡内容词 4 个（维度前缀不计词），合规区间 5-8 跨轴词」；HARD 态（env `KDO_TAGS_HARD_DATE=2026-01-01`）翻转为 **error**
- **结论如实记录**：该卡按 #498 内容词口径 4<5 **本就不合规**，原「标杆卡 6 条合规」系总条目错误读法。本卡不再作合规样板；内容词补标属内容治理，归内容侧（老顽童/王语嫣）软期内处理，黄药师不改别人卡片内容

## 6. 修后存量量化（HARD 到期治理规模，供内容侧排期）

扫描口径同 §4（非 index/meta/log/system 且有 tags 的卡 2916 张）：内容词 <5 = **2064 张** / 5-8 合规 = 840 张 / \>8 = 12 张 / 零 tags = 0 张。pre-submit 门禁只作用于提审文件，存量治理需内容侧在软期（至 2026-09-14）分批补标——规模千张级，建议编排侧分域排批次。

## 7. 两态机制不变声明

`TAGS_HARD_DATE="2026-09-14"` + env `KDO_TAGS_HARD_DATE` 未动（#669/#677 同节奏）；本轮只改词量计数口径与缺陷复现证据，接线与两态设计经欧阳锋四重点核 ①②③ 已 ✅，不在返工范围。

## kdo query 检索记录（宪法第六条，#669）

| 检索词 | 变体 | 命中 | 日期 | 结论 |
|:--|:--|:--|:--|:--|
| 标签 词量 内容词 维度 5-8 区间 | 中文 | 6（top：framework-AI知识库-五维标注深挖法 0.18 / framework-ai-sales-collaboration / framework-knowledge-base-vs-ontology 等） | 2026-09-07 | 无卡定义词量口径本体，无冲突口径 |
| tags word count caliber dimension prefix | 英文 | 4（最高 0.15 tool-yitang-government-data-search，低相关） | 2026-09-07 | 同上 |

- 口径真相源直读（受控文件，命中）：`90_control/tags-vocab-design.md` §词量口径分卡型（L42-46）+ `60_feedback/tasks/task_20260824_laowantong-dk-tags-word-count-caliber.md` 复审记录（L135-145）
- 其余定位属 grep 许可类②（代码/任务号/日志非知识检索）

## 存在性核查（本证据负向判词锚点，#433）

- 「4179de376^ 两 dk 卡文件不存在（0/0 非零 tags）」→ `git show 4179de376^:30_wiki/dark-knowledges/dk-ai-stronger-need-to-know-what-you-want.md` 报 `fatal: path ... does not exist in '4179de376^'`（欧阳锋复审同锚）
- 「git 历史存在真实零 tags 卡版本」→ 扫描脚本输出 49 张；`git show 3051d146e:30_wiki/concepts/ai-collaboration-mindset-shift.md` frontmatter 无 `tags:` 行、`type: concept`
- 「现行盘上无可复现的零 tags 受检卡」→ 全库扫描零 tags 且非 index/meta/log/system 卡 = 0 张（唯一零 tags 非索引卡 `30_wiki/personal-os/zhu-conversation-insights.md` 为 `type: system`，门禁跳过）——故活体复现必须走 git 历史
- 「graph-rag 修后 0 issue」→ `run_pre_submit(Path(wiki), ['30_wiki/concepts/graph-rag.md'])` 实跑 `tags_gate_issues=0`
- 「meeting-iceberg 修后 1 条内容词 warning」→ 同法实跑 `tags_gate_issues=1`，报文含「内容词 4 个」
