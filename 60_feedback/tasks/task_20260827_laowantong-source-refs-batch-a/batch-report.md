# #557 批次A 批次报告：inbox 死引原稿归档 + 引用校正

> 执行：老顽童 2026-08-27 凌晨 ｜ 回退点：`snapshot-20260826-182328` ｜ 数据源：`60_feedback/analysis/source-refs-health-latest.json`（00:21 基线版）

## 总量对账（独立可复跑）

| 指标 | 基线（00:21） | 完成后（02:50） | 变化 |
|:--|--:|--:|:--|
| refs_missing 全库 | 1024 | 267 | **-757** |
| 其中指向 00_inbox | 932 | 178 | **-754** |
| refs_ok | 3202 | 3929 | +727 |
| refs_line_anchor（checker 可识别锚） | 2 | 728 | +726（全部 alive） |
| total_refs | 5910 | 5931 | +21（多区间锚拆行所致） |

复跑命令：`python 90_control/scripts/check-source-refs.py --report-dir 60_feedback/analysis`（注意：不带 --report-dir 只打印不落盘，基线 JSON 不更新——过程发现之一）

**差集口径说明（如实）**：处理量=91 文件归档 + 850 条引用改写（633 死引 + 217 活引用同步改写防断链）；下降量 754 > 633 的差（121）来自：折叠锚点续行此前被重复计缺失、多区间锚拆分改变计数粒度、嵌套 YAML 拍平释放的同路径多条目。机读对账文件见下方 manifest，可独立复跑证伪（L11）。

## 处置明细

- **归档**：91 个原稿 `git mv` 00_inbox → `10_raw/sources/<主题子目录>/`（保留主题下子目录层级防同名碰撞——`p001.txt` 类文件名在多课程目录下重名，dry-run 曾暴露 6 组碰撞）
- **引用改写**：850 条 source_refs（321 卡），只动 frontmatter 该字段；锚点规范化 ` L3018-L3400`→`:3018-3400`、`#L187-L325`→`:187-325`、多区间 `L280-L282,L392-L394`→拆多行单锚（checker 只认行尾 `:NN(-MM)` 单锚）
- **reviewed 卡说明**：850 条中 222 条在 reviewed 卡——Boundary 条款「reviewed 卡的死引属批次 B」是指内容级修复；本批对 reviewed 卡只做**搬运联动的指针更新**（不动=制造 222 条新死引，B1 半套修改判词），零内容改动
- **收尾清理**（迁移副产物，25 卡）：折叠锚点续行合并、嵌套 `  - src_unknown` 孤儿行清除（P-29 污染，同级顶格占位未动）、嵌套引用拍平

## 批次轨迹（每批一 commit）

| 批次 | 文件 | 卡 | 引用 |
|:--|--:|--:|--:|
| 试点 case-study | 1 | 9 | 42 |
| sales（含 2 卡缩进手修） | 8 | 23 | 28+手修 |
| banfeimao-openmic | 5 | 11 | 33 |
| manage-the-team | 4 | 7 | 9 |
| demand-analysis | 3 | 8 | 11 |
| profit-first | 2 | 15 | 31 |
| key-assumptions | 2 | 2 | 5 |
| ai-outpost-ep2 | 1 | 6 | 6 |
| strategy | 1 | 18 | 18 |
| research-topics | 1 | 64 | 64 |
| thought-liberation | 1 | 8 | 8 |
| multimodal-output | 1 | 4 | 8 |
| banfeimao-offline | 2 | 4 | 12 |
| yitang-five-step / -growth | 2 | 9 | 10 |
| yitang-lectures（根目录散件） | 13 | 33 | 60 |
| handle-the-business | 45 | 120 | 529 |
| 收尾清理 commit | — | 25 | 47+3 |

## ⚠️ 事故自报：git add -A 误扫入他方未提交改动

收尾清理 commit（`5c2555e44`）用 `git add -A 30_wiki` 扫入了 **6 个非本任务的他人未提交改动**：

- `30_wiki/personal-os/zhu-time-os.md`——**一段未提交的审查记录**（退回补内容结论+P1/P2 清单，作者应为欧阳锋/王语嫣某实例的进行中工作）
- `30_wiki/frameworks/framework-truman-feature-thinking-core.md`——内容增补 18 行
- `30_wiki/frameworks/framework-truman-feature-layered-system.md`、`framework-visual-analysis-four-dimensions.md`、`30_wiki/concepts/concept-token-capital.md`、`30_wiki/tools/tool-zhu-ai-deliberate-practice-roadmap.md`——未提交改动（性质未逐一核对）

**处置**：未做 git 手术回退——另一实例当时活跃（index.lock 撞车实证），回退+重放有撞丢对方新写入的风险。改动在 commit 中完整可见（`git show 5c2555e44 -- <文件>`），请原作者认领确认。教训已记 friction-log：批次 commit 永远枚举显式路径，禁 `-A`。

另：handle-the-business 批因 index.lock 撞车裂成两个 commit（`03ae9f80e`+`18bf24cf6`），后者顺带扫入 14 个 wechat 管道自动产物（`10_raw/sources/src_2026-08-27_wechat_*`，本属 auto-backup 会收的件）——无害但如实记账。

## 机读对账文件（L11）

- `manifest-renames.txt`——92 条 git rename 记录（snapshot..HEAD，含新旧路径）
- `manifest-cards.txt`——全部改动卡清单（341 行含批次边界）

## 残留 267 条 missing 的构成（非本批范围）

- 178 条指向 00_inbox：原稿真亡（见 `gone-refs-report.md` 报王语嫣）+ 口喷在途文件 `:A` 锚点新型式
- 其余：https 外链 22、60_feedback 内部引用 8、编码残缺文件名（`一?`）等存量问题
