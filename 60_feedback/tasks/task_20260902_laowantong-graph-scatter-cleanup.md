---
id: task_20260902_laowantong-graph-scatter-cleanup
title: Obsidian 图谱散点治理二批——31 文件残留占位+870 真散点逐族裁决（王语嫣首批已清 1132 处）
seq: 606
status: queued
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 老朱 0902「obsidian 视图全乱了，你给我修复」+ 编排纠偏（王语嫣越位直改一批后回归编排位，剩余移交施工）
reviewer: 欧阳锋
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
