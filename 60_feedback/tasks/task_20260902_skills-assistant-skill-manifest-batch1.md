---
id: 597
task_id: task_20260902_skills-assistant-skill-manifest-batch1
title: skill登记面批1：72个manifest.yaml补建+2个name不一致修复
status: reviewed
assignee: skills-assistant
created_by: wangyuyan
created_at: 2026-09-02
reviewer: ouyangfeng
source_refs:
- 60_feedback/diagnosis/建议书_20260901_skill健康度勘察与检测方法论.md
related_tasks:
- '#588'
- '#593'
- '#594'
- '#595'
instance: skills-assistant-kimi
updated_at: '2026-09-01T21:44:47.953554+00:00'
evidence: _tmp/evidence_597.md
reviewed_by: 欧阳锋
review_date: '2026-09-02'
grade: A-
---

# 任务：skill 登记面批 1（建议书动作 1+2）

## 背景
- Skills 助理《skill 健康度勘察与检测方法论建议书》（09-01）勘察：76 个登记 skill 中 72/76 无 manifest.yaml、72/76 无 trigger.natural_language、53/76 description<80 字符、2 个 frontmatter name 与目录名不一致——**登记面系统性欠账=「挂了但路由不可用」**。
- 王语嫣裁定（09-02 00:02）：部分采纳分批立项。本单=批 1（P0 登记面）；BOM+8 维检测例行化=批 2（#598 黄药师）；动作 4/5/6（降级/挂载/收编编排判定）待本单产出后王语嫣复核；动作 7（legacy 53 个归档）涉目录结构变更待老朱；动作 8 缓议。

## 任务
1. **72 个 manifest.yaml 补建**（样板=`deep-debug`/`anti-ai-bs-three-moves`）：每含 `trigger.natural_language`（触发词表）+ `adapted_from`（来源卡）+ `适用 agent` 字段；按 8 维 rubric（建议书 §三）自检。
2. **2 个 name 不一致修复**：`content-production-polish`（现=Vikki-human-speech）、`knowledge-collision`（现=knowledge-collision-workflow）——frontmatter name 对齐目录名。

## 验证
- 72/76 manifest 齐；INDEX.md/MOUNT-MATRIX.md 三写一致复扫通过。
- 8 维机械复扫：🔴 数量显著下降（P0 维 A/E/F 清零）；name 不一致清零。
- 欧阳锋终审。

## 边界
- **开工前置=#595 终审收口**（同域 frontmatter 面，错峰防写冲突；#595 已 pending_review 等欧阳锋）。
- 只补结构层（manifest/name）不重写 SKILL.md 正文。
- `adapted_from` 无对应来源卡的**不编造**，标 `adapted_from: null # 待复核`（#495 口径）。
- description <80 字符的顺手补齐可做，但不得虚构触发场景（从正文提炼）。

## 需要谁动作
- Skills 助理：施工+自检，完成后 queue_transition submit 提审。
- 王语嫣：产出后复核动作 4/5/6 编排判定。
- 欧阳锋：终审+后续补 manifest 批次出口门控。

## 执行报告（skills-assistant-kimi，2026-09-02 05:15）

**交付物**：`40_outputs/capabilities/skills/shared/*/manifest.yaml` 新增 72 个（连同既有 4 个=76/76 齐）；2 处 SKILL.md frontmatter name 修复；生成器脚本 `_tmp/gen_manifests_597.py`（dry-run→apply 两阶段留痕）；复扫产物 INDEX.md / MOUNT-MATRIX.md / SKILL-HEALTH.md 三写一致刷新。

**完成内容**：
1. 72 个 manifest.yaml 按 deep-debug 样板补建——每含 `trigger.natural_language`（3-6 条触发词，从各 SKILL.md description 提炼，不虚构场景）+ `adapted_from` + `适用agent`（取 INDEX 已挂载列；未挂载标 `[]`+注释待编排判定）+ changelog 变更锚点。
2. `adapted_from` 按边界纪律不编造：71 个标 `null  # 待复核`（#495 口径），仅 `research` 沿用 INDEX 已登记的 `business-research-skill-oscar-13-weapon-system`。
3. name 修复：`content-production-polish`（Vikki-human-speech→目录名）、`knowledge-collision`（knowledge-collision-workflow→目录名），只改 frontmatter name 一行。

**验证**：`scan_skills_registry.py` 复扫——INDEX 缺口清单「缺 trigger.natural_language：72→0」「name 不一致：[]」；8 维雷达：A 触发维 76/76 ✅清零、F manifest 维 ✅清零、🔴 72→24（剩 24 均为正文层欠账 B/C/D/H，超出本单"只补结构层"边界）；E 来源维未清零（71 个按纪律标 null 待复核，清零依赖王语嫣裁定来源卡归属，见下）。

**边界**：未动任何 SKILL.md 正文（仅 2 个 name 单行）；未做 description <80 字符补齐（顺手项，为避免虚构触发场景本批未做，留待内容层批次）；E 维 `adapted_from` 待复核项需来源卡归属裁定后回填；本单不触碰动作 4/5/6 编排判定。

**需要谁动作**：欧阳锋终审（重点复核：触发词提炼质量抽样、null 待复核口径是否符合 #495）；王语嫣复核 72 个 `adapted_from: null` 的来源卡归属 + 动作 4/5/6 编排判定。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ①-补 划痕路径提示

- ⚠️ 交付物节含划痕路径 `_tmp/gen_manifests_597.py`（中间产物非交付物，按约定豁免三态检查；如属误写请清理交付物节）
### ① 声称-交付差集

- 🔴 声称但文件不存在: `40_outputs/capabilities/skills/shared/*/manifest.yaml`
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）

## 终审记录（欧阳锋 CLI 实例，2026-09-02 05:4x）

**等级：PASS A-**

### 溯源验证（独立复跑/亲读，非采信报告）

| 验证项 | 报告声称 | 独立核验结果 |
|:--|:--|:--|
| manifest 齐套 | 76/76 | ✅ 亲数 `shared/*/manifest.yaml`=76、`SKILL.md`=76，无缺口目录（77 条目含 README.md 非 skill） |
| YAML 可解析+必填键 | — | ✅ 自写脚本全量 76 个 safe_load 通过，`name`/`adapted_from`/`trigger.natural_language` 非空，manifest name==目录名 76/76 |
| adapted_from 口径 | 71 null + research 沿用 | ✅ 亲数 null=71；非 null 5 个中 4 个为既有（deep-debug 空串/nine-character/research-core/skill-architecture-design），新增仅 research；来源卡 `30_wiki/concepts/business-research-skill-oscar-13-weapon-system.md` 实存 ✅ |
| name 修复 | 2 处 | ✅ `content-production-polish`/`knowledge-collision` frontmatter name 均=目录名；全量 76 目录 dir-name 一致性复扫 0 mismatch（修复面=清零，非仅 2 处） |
| 复扫数据 | 🔴72→24、A/F 清零 | ✅ 独立重跑 `scan_skills_registry.py`：🟢7/🟡45/🔴24，INDEX 缺口「缺 trigger.natural_language：0 个」；🔴 数逐字吻合 |
| 三写一致 | INDEX/MOUNT-MATRIX/SKILL-HEALTH 刷新 | ✅ 重跑扫描后 git diff 仅 3 处生成时间戳（05:14→05:40），内容零漂移；抽样 kdo-self-attack 三处互证（INDEX 触发词列/挂载列 ↔ manifest ↔ MOUNT-MATRIX 5 挂载单元）逐字吻合 |
| 版本对齐（yaml 配置类） | — | ✅ commit `0485df8d8`（09-02 05:16）在仓；审查对象为最新 HEAD；无长驻消费进程 |

### 触发词质量抽样
- `research`：触发词「商业调研/调研入口/行业分析竞品分析/帮我查一下」与 SKILL.md description 逐字同源，无虚构场景 ✅
- `kdo-self-attack`：触发词 4 条全部出自 description 语义（自攻击/对抗审查/找弱点），无编造 ✅

### 缺陷与记档
- 🟠 **research/manifest.yaml changelog 模板残留**：changelog 文案写「无来源卡 adapted_from=null 待复核」，但该 manifest 的 adapted_from 实际已填 `business-research-skill-oscar-13-weapon-system`——生成器模板文案未随非 null 分支切换，文案与字段矛盾。属注释文案瑕疵，不影响字段正确性，不阻断。**落点**：建议书 `60_feedback/diagnosis/建议书_20260902_manifest-changelog模板文案分支残留.md`（待王语嫣编排）。
- 🟡 INDEX/MOUNT/SKILL-HEALTH 生成时间戳非幂等（重跑必脏 3 行）——**落点**：#598 终审记录已记档同族（「diff 仅时间戳」不影响 fresh 判定，随下次重扫自然收口），不重复立单。
- 机器预审 🔴「声称但文件不存在 shared/*/manifest.yaml」为误报（glob 字面量被当路径核查），实际 76 个文件全在。

### 残余风险

**存在性核查**：本意见书中"不存在"仅出现于转述机器预审原文（「声称但文件不存在」）；核查方法=亲数 `shared/*/manifest.yaml` 实存 76 个（wc -l=76）+ 全量 YAML 解析 76/76 通过，误报根因=glob 字面量被当路径核查。

- 71 个 `adapted_from: null # 待复核` 需王语嫣裁定来源卡归属后回填（任务单「需要谁动作」已挂，E 维清零依赖该裁定）——符合 #495 不编造纪律，非缺陷。
- description<80 字符补齐明确留待内容层批次（边界内声明，防虚构触发场景）✅

### 边界复核
未动任何 SKILL.md 正文（git show 0485df8d8 中 2 个 SKILL.md 均仅 name 单行变更）✅；未触碰动作 4/5/6 编排判定 ✅。
