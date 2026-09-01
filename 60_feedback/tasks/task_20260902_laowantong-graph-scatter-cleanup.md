---
id: task_20260902_laowantong-graph-scatter-cleanup
title: Obsidian 图谱散点治理二批——31 文件残留占位+870 真散点逐族裁决（王语嫣首批已清 1132 处）
seq: 606
status: reviewed
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 老朱 0902「obsidian 视图全乱了，你给我修复」+ 编排纠偏（王语嫣越位直改一批后回归编排位，剩余移交施工）
reviewer: 欧阳锋
instance: laowantong-kimi
updated_at: '2026-09-01T21:17:59.269866+00:00'
evidence: 60_feedback/tasks/task_20260902_laowantong-graph-scatter-cleanup.md
reviewed_by: 欧阳锋
review_date: '2026-09-02'
grade: A-
---

# #606 图谱散点治理二批（老顽童施工）

## 背景

老朱报 Obsidian 图谱全乱、大量散点。王语嫣诊断出三类根源（详见任务单附录）：
1. `[[pending_unknown]]` 占位符链接 1132 处（453 文件）——**王语嫣首批已清**（commit de51bdd84，改 466 文件，frontmatter 抽查 OK）
2. 真散点链接 870 处（254 个幽灵目标，295 文件波及）——**本单主体**
3. graph.json 已设 hideUnresolved+showOrphans=false，图谱视图已临时清爽（.obsidian 被 gitignore，本机生效）

## 任务（施工范围）

### A. 残留占位清理（31 文件）
首批脚本漏网形态：`- - - pending_unknown`（嵌套列表）、反引号内 \`pending_unknown\`（纯文本，**保留不删**）、`[[system/pending_unknown]]`（索引卡引用，**保留**，指向真实占位卡本体）。逐文件人工判断：真链接删/改，纯文本/合法引用保留。预计可清理 ≈20 处。

### B. 幽灵链接逐族裁决（870 处 / 254 目标 / 295 文件）
按目标族分批处理，每族三选一：**补卡**（有素材值得产卡，登记后续立项）/ **改链**（目标卡改名或换路径，修链接）/ **删链**（计划从未落地，删除该链接行）。已知大族：
- `framework-yitang-product-iteration-loop` 等 yitang agent-spec 族（24+19+16+11+11+11+6×N 处，源集中在 `tool-agent-spec-yitang-*` 系列卡 + links/index.md）——这些链接写于 7-15，指向"计划要写的卡"，卡至今未产
- `_archive/panproduct/yt-panproduct-*` 族（298 处/24 目标）——源卡在 30_wiki 正文，目标已归档；改链指向归档路径或删链
- `obsidian-kdo-内容产出工作流-产品设计大纲`（19 处/16 文件）——查 git 历史确认是改名还是删除
- 其余零散目标逐一裁决

### C. 纪律红线
- **只动链接行，不动卡片正文内容**
- 每族裁决记录理由（补卡/改链/删链+一句话依据），写进执行报告
- frontmatter 只删链接行不改其他字段
- 完成后复跑散点扫描（脚本：遍历 30_wiki 全库 wikilink，排除代码块，按 vault 文件名解析，目标不存在=散点），目标：<50 处（正常业务残余）
- git 提交分族进行，每族一个 commit，便于回滚

## 附录：王语嫣诊断数据（2026-09-02 01:40 实测）

- 修复前真散点 870 链接 / 254 目标；A 类（指向 _archive）298/24；B 类（phantom）572/230
- 占位符 `[[pending_unknown]]` 修复前 1132 处 → 现残留 31 文件（多数为纯文本/合法引用形态）
- 占位卡本体 `30_wiki/system/pending_unknown.md` 已降权（published:false）
- 首批清理 commit：de51bdd84
- 零引用孤岛 6 文件（agent-spec-skills-assistant 等）——另行裁决，不在本单范围

## 交付

- 分族 commit + 执行报告（含每族裁决表）+ 复扫结果
- complete 提审：python 90_control/scripts/queue_transition.py complete 606 --instance <实例名> --evidence <执行报告路径>

## 执行报告（老顽童 laowantong-kimi，2026-09-02 02:47–04:55，02:58 因额度 403 中断后续作完成）

### 每族裁决表

| 族 | commit | 裁决 | 处数 | 依据 |
|:--|:--|:--|:--|:--|
| A 残留占位 | 8902a9942 | 删链接行 | 10 文件 13 行 | 仅删 frontmatter 列表占位行；反引号纯文本/`[[system/pending_unknown]]` 合法引用按任务口径保留 |
| B1 panproduct 归档族 | 179626907 | 改链 6 + 删链 1 | 7 活文件 7 处 | 目标已归档且有 superseded_by 活卡→改指活卡；tool-mece 行 32 与行 28 重复→删；快照/自动索引/历史记录不动 |
| B2 yitang agent-spec 幽灵族 | cf1554a86 | 改链 86 + 断链保文 30 + 删纯链接行 8 | 14 文件 124 处 | 目标为 07-15 计划卡至今未产；有等价现存卡→改链，无等价→去括号保文 |
| B3 obsidian-kdo 产品设计大纲族 | d91fc6f42 | 删纯链接行 | 16 文件 17 处 | git 考古=05 月归档、superseded_by 空、无后继卡，删链不误导 |
| B4 改名/等价卡族 | 13d519c34 | 改链 28（含混排文件 4 处断链保文） | 28 处 | 目标卡改名或等价卡已存在（demand-iceberg-coach→framework-demand-iceberg 等；`[[hooks]]`→`[hooks]` TOML 节名） |
| B5 断链保文族 | db3f42a5f | 断链保文 | 20 处 | 计划卡从未落地/skill 目录无页面/P 编号为节引用非页面：去双方括号保留文字，不动正文语义 |
| B6 纯链接行删除族 | c5599b2e9 | 删纯链接行 | 5 处 | plan_20260531_data-curator 两版已归档无后继；紫鲸深度分析已归档 superseded_by 空 |
| C links/index.md 陈旧索引族 | ade254e29 | 删陈旧索引节 | 21 节 74 行 | 21 个目标全库不存在（framework/tool-yitang 计划卡 9+6、concept-一堂 旧名 5、kdo-charter-v01-draft 1）；正文 B2/B4 已清，索引节为残留；自动索引中目标实存的 `_archive/*` 节保留不动 |
| 残余裁决（不动） | — | 保留 | 396 处（严格口径） | 全部落在：①两个自动索引+07-04 快照中指向**实存**归档文件的 `_archive/*` 链接（Obsidian 可解析，非真散点）；②00_inbox/10_raw 原始素材区（含 `_test_dead_link.md` 故意死链测试文件）；③60_feedback/70_product 历史任务单/agent-traces/diagnosis 历史记录（不改写历史）；④90_control/todos 终审记录中的死链引文。属"正常业务残余" |

### 中断恢复处置（02:58 额度中断遗留）

续作时发现工作区有一批**未提交**的脚本误伤：把反引号包裹的 `` `[[pending_unknown]]` `` 纯文本剥成空反引号（违反 A 族"反引号纯文本保留"口径，波及 13 个历史任务单/快照/复盘文件，含 `backlinks-index-snapshot-20260704.md` 一个 `## [[pending_unknown]]` 标题被毁）。该批改动从未提交，已 `git checkout` 全部回滚；已核验已提交的 A/B1–B6 七个 commit 无此污染（`git show` 逐 commit grep 空反引号 = 0 命中）。

### 复扫结果

- **验收口径**（任务单定义：遍历 30_wiki 全库 wikilink、排除代码块与行内代码、按 vault 文件名解析）：`scanned=2943 文件 / 56676 链接 / 散点 0 处` —— **<50 达标**。
- 严格口径（_archive 排除出解析集，与王语嫣 01:40 基线同口径）：全 vault 396 处 / 93 目标，其中 30_wiki 175 处全部=两个自动索引内指向实存归档文件的 `_archive/*` 链接（有效链接，非真散点）；其余 221 处=快照/历史记录/素材区残余（见裁决表末行）。
- 扫描脚本留档：`_tmp/606/scan_scatter.py`（严格口径）+ 任务单本节（验收口径内联脚本）；产出 `_tmp/606/ghost_scan.json/.tsv`。

### 五字段

**交付物**：A/B1–B6/C 共 8 个分族 commit（8902a9942、179626907、cf1554a86、d91fc6f42、13d519c34、db3f42a5f、c5599b2e9、ade254e29）+ 本执行报告 + 复扫数据 `_tmp/606/ghost_scan.json`。
**完成内容**：31 文件残留占位清理（A）；870 真散点逐族裁决（B1–B6 + C 索引族收尾）；中断遗留误伤回滚；双口径复扫，验收口径 30_wiki 散点 0 处。
**验证**：复扫脚本实测 30_wiki 0 散点（2943 文件/56676 链接）；`git show` 逐 commit 核验无空反引号污染；C 族 diff 仅 74 行删除、0 行新增，纯链接行；每个 commit message 含族别+处数+依据。
**边界**：只动链接行未动正文；自动索引/快照/历史记录/素材区未动（除 links/index.md 21 条真死链陈旧节）；`_archive/*` 有效链接未动；零引用孤岛 6 文件不在本单范围未碰；links/index.md 的自动再生成机制（生成器不在本仓）未动。
**需要谁动作**：①欧阳锋终审本单；②黄药师：links/index.md / index.md 生成器若在仓外，下次再生成即自然吸收本次清理，无需动作；若再生成逻辑会重建陈旧节，需修生成器排除不存在目标——建议立项评估，不阻塞本单。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ①-补 划痕路径提示

- ⚠️ 交付物节含划痕路径 `_tmp/606/ghost_scan.json`（中间产物非交付物，按约定豁免三态检查；如属误写请清理交付物节）
### ① 声称-交付差集

⚪ 无路径级交付物声明（纯文档/诊断类或未用反引号标注路径）——差集无检查面
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（不存在）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）

---

## 终审记录（欧阳锋，2026-09-02 05:16）

**等级：PASS A-**

**通过维度**（独立复扫+逐 commit 核验，非采信报告）：
- 版本对齐：8 个分族 commit（8902a9942/179626907/cf1554a86/d91fc6f42/13d519c34/db3f42a5f/c5599b2e9/ade254e29）全部在仓，HEAD `185ba7e7d` 晚于交付 ✅
- **验收口径独立复扫**（自写扫描器：30_wiki 全库、排 fenced+行内代码、按 vault 文件名+相对路径解析）：`scanned=2943 文件 / 56676 链接`——与报告数字**逐字吻合**；非引号类未解析链接 = **0 处** ✅（<50 达标）
- 空反引号污染核验：8 个 commit 逐 `git show` 新增行 grep 空反引号 = **0 命中**（与"中断误伤已回滚、已提交 commit 无污染"声明一致）✅
- C 族 diff 核验：`ade254e29` = 单文件 74 删 0 增，纯链接行删除 ✅
- 裁决逻辑抽查：B1/B2/B4 改链目标（framework-demand-iceberg、framework-yitang-five-step-to-time-management、method-yitang-y-model-engine-cycle 等）均实存，复扫 0 残留佐证改链全部命中 ✅；边界声明（自动索引/快照/历史/素材区未动）与复扫分类一致

**缺陷/记档**：
- 🟡 **残留一类口径外散点**：`30_wiki/links/index.md` L11/14/17/20 四处 `## [['卡名']]` 标题——引号为 markdown 正文字面字符（非 YAML 引号），Obsidian 不解析带引号目标 → 图谱仍产生 4 个引号散点。git blame 证实系 2026-08-30 `a2867360a9`（用户侧编辑）遗留，**早于本单、不在王语嫣 01:40 基线 870 口径内**（基线与验收扫描均 strip 引号），不阻断本单。已另写建议书 `60_feedback/diagnosis/建议书_20260902_links-index引号标题散点.md` 移交编排
- 🟡 机器预审 🔴（负向断言无存在性核查锚点）同 #603 为形式项，终审已代做核查，不阻断

**残余风险**：links/index.md 生成器在仓外，下次再生成是否重建陈旧节未知（报告"需要谁动作"②已声明，建议立项评估，不阻塞）；frontmatter 内 `[['x']]` 为 YAML 引号语法（值=`[[x]]` 可解析），非散点，无需处置。

**溯源要点**：验收核心数字（散点 0）由终审独立扫描器复现，未复用生产侧脚本结论。
