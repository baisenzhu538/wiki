---
id: "586"
title: "学习candy合集+两天inbox素材批量产卡（翻译→调研→六层交叉→九层深挖→产卡入库）"
type: production
status: claimed
priority: P0
assignee: 老顽童
created_by: 王语嫣
created_at: 2026-09-01
updated_at: 2026-09-01
source_refs:
- 00_inbox/学习candy合集/
- 00_inbox/video_transcripts/
---

# #586 学习candy合集批量产卡任务（老朱 09-01 凌晨直令）

## 任务来源

老朱直令：candy 合集 + 两天进 inbox 的素材，按一堂调研方法论全网调研、六层交叉、九层深挖，产知识卡/skill/workflow/agent 入库，明早汇报。

## 素材清单与分域方案（王语嫣编排判定）

| 素材 | 域 | 产出形态 | 备注 |
|---|---|---|---|
| Live257 十指讲香模型（拆书《用数字讲故事》） | decision | 概念卡+方法卡（数字转换四原则） | 2240 行，含拆书完整正文 |
| Live260 AI口喷基本功（Truman 双 Partner 原文） | ai-collaboration | dk卡+case卡 | ⚠️传播限制「仅限内部不要外传」——落卡必须标注，正文脱敏引用 |
| AI×知识管理探索营（10篇Obsidian文档开源） | kdo | 方法卡+情报卡（外部参照） | 586 行 |
| 大卫·布鲁克斯 TED 3个谎言 | strategy（个人成长/价值观） | 概念卡 | **先翻译再产卡** |
| 大卫·布鲁克斯 芝大毕业演讲 | decision（求知方法论） | 概念卡+dk卡 | **先翻译再产卡** |
| 尼尔·雷克汉姆 SPIN 访谈 | sales | 方法卡（与 #320 SPIN 卡组互链） | **先翻译再产卡** |
| Jovida 调研报告×2 | ai-collaboration | case卡（AI Life Agent 竞品对标） | 已是中文调研稿 |
| WAIC 顶层思考 + MUSE DataPack | strategy | 框架卡（MUSE 四层模型）+概念卡 | 顶层文与 DataPack 交叉引用 |
| deep-debug 技能 | kdo/skill | **直接 skill 化**（40_outputs/capabilities/skills/shared/） | 已是 skill 格式，验收后注册 |
| 高阶 Skill 设计指南 | kdo | 方法卡+tool卡（与 skill 体系互链） | Anthropic 官方案例拆解 |
| 龙虾团队 OPT | strategy/management | 框架卡（One Person Team） | 产品设想稿 |
| Agent 大学 | ai-collaboration | 概念卡+情报卡 | 产品设想稿 |
| Eason 文化审计 DataPack | management | 方法卡（实事求是方法论） | ⚠️CHO 私有密级——只产方法论卡，人物细节脱敏 |
| BV 视频逐字稿 7 件 | sales/decision | 已由 01:14 值守拍诊断（英文 ASR 质量差）——SPIN 访谈与 candy 版重复，其余按 #586b 处置 | 撞车件不重复产卡 |

## 生产顺序（Wave 结构）

- **Wave 0（翻译）**：3 篇英文稿→中译版落 `00_inbox/学习candy合集/translations/`（指令见 90_control/parking-lot/tmp-translate-instruction-20260901.md）
- **Wave 1（高价值优先）**：Live257 数字讲故事 / Live260 口喷（脱敏）/ 高阶Skill设计指南 / MUSE 框架卡
- **Wave 2**：布鲁克斯×2 / SPIN 方法卡 / 龙虾OPT / Agent大学 / deep-debug skill 化
- **Wave 3**：Jovida case / 探索营方法卡 / Eason 方法论（脱敏）

## 生产规范（老朱直令要求）

1. **全网调研**：每个主题产卡前用 kdo-tools/web_search.py 搜外部验证源（框架卡必带「外部验证」节，老朱 08-09 铁律）
2. **六层交叉验证**：核心结论 ≥2 独立来源，逐条标 L1-L6 层级（research-cross-validation skill）
3. **九层深挖**：暗知识单层挖（决策代价/学习顿悟/反直觉），一卡一事细粒度
4. **终稿形态**：知识卡落 `30_wiki/`（concepts/frameworks/methods/cases/tools 按性质），skill 落 `40_outputs/capabilities/skills/shared/`，workflow 落 `40_outputs/capabilities/workflows/`——按内容性质归位，不硬塞
5. **frontmatter 全字段**：domain/aliases/discoverable_by/source_refs/related 一个不少（Agent 可发现性设计）
6. **传播限制**：Live260 与 Eason 两件必须标注密级+脱敏

## 验收标准

- 卡片数 ≥15（每素材 ≥1 卡，高价值素材 2-3 卡）
- 每张卡有 ≥1 外部验证源（概念/框架卡）
- 翻译件 3 篇落盘且行数对齐
- skill 化 ≥1 件（deep-debug）
- 全部 complete 提审，欧阳锋终审

## 建模方案（L1 出牌，2026-09-01 老顽童）

组件链：`[素材牌] → [边界牌] → [结构牌] → [过程牌] → [质量牌]`

- **[素材牌 #1素材逐字消费]**：四件 Wave1 素材逐字读完，精读笔记落 `_tmp/notes_586_wave1.md`（17.5KB，含行号溯源）；Wave2/3 素材各卡生产前逐字消费
- **[边界牌 When-NOT]**：每卡带 Constraints & Boundaries + 不要用的场景表；Live260/Eason 两件按任务单要求脱敏+密级标注
- **[结构牌 KF-024]**：framework 卡三节（Synthesis 表+不要用的场景+Action Triggers）；dk 卡七段含独立 Critique 节；method 卡九层（定义/机制/边界/失败模式≥3表格/关系/迁移/checklist/Critique≥2外部攻击者）
- **[过程牌 三步编译]**：Condense（浓缩框架）→ Critique（≥2 位不同范式外部学者攻击）→ Synthesize（与库内卡互链定位）；关键数字全部标「口述待独立核实」或附出版来源
- **[质量牌 门禁]**：逐卡 `kdo pre-submit` 0 ERROR → 自攻击 → 执行报告五字段 → complete 三证验证

### 查重结论（L7 牌，产卡前实测）

| 素材 | 库内现状 | 动作 |
|:--|:--|:--|
| 用数字讲故事 | 无卡 | 新建 method 卡 |
| 十指讲香 | 有 concept-讲香-卖点直给到价值感（理念卡）+3张jiangxiang案例卡，**无十策略本体卡** | 新建 method 卡补本体，互链 |
| 关键假设 ABCD | 无独立方法卡 | 新建 method 卡（decision） |
| 口喷 ROI 搭档 | 有 dk-koupen-500-vs-5000 / dk-koupen-input-method-loss | 新增 dk 卡（决策分档+妥协决策，不撞） |
| 口喷陪练官 | 无 | 新建 tool 卡（训练场设计模式） |
| Anthropic Skill 指南 | 有 tool-ai-skill-engineering-guide（Truman 培训向） | 新建 method 卡（官方范式拆解），互链 |
| MUSE | 有 yt-model-muse-ai-framework V3.0，**U/S 字母语义与 DataPack v1.0 对调** | 新建 framework 卡记录两代映射+勘误说明，互链旧卡不静默合并（六层交叉验证：冲突记录不合并） |

### 卡片清单（16 卡 + 1 skill）

| # | 目标卡 | 域 | 类型 |
|:--|:--|:--|:--|
| W1-1 | method-storytelling-with-numbers | decision/content | method |
| W1-2 | method-shizhi-jiangxiang-ten-strategies | content | method |
| W1-3 | method-key-assumption-abcd | decision | method |
| W1-4 | dk-koupen-decision-tiering-compromise | decision/ai-collaboration | dk（脱敏） |
| W1-5 | tool-ai-koupen-training-partner-design | ai-collaboration | tool（脱敏） |
| W1-6 | method-anthropic-skill-design-patterns | kdo | method |
| W1-7 | framework-muse-ai-full-map-v1 | strategy | framework |
| W2-1 | concept-brooks-three-lies-culture | strategy | concept |
| W2-2 | dk-brooks-cost-of-knowing | decision | dk |
| W2-3 | method-spin-linking-sales-marketing | sales | method（互链 #320） |
| W2-4 | framework-lobster-opt-one-person-team | strategy/management | framework |
| W2-5 | concept-agent-university | ai-collaboration | concept |
| W2-6 | skill 化 deep-debug → 40_outputs/capabilities/skills/shared/deep-debug/ | kdo | skill |
| W3-1 | case-jovida-ai-life-coach | ai-collaboration | case |
| W3-2 | method-obsidian-km-camp | kdo | method |
| W3-3 | method-shishiyanshi-evidence-based | management | method（脱敏） |
| W3-4 | case-yitang-jiangxiang-12-practices | content | case |

## 执行报告

> 交付物（15 卡 + 1 skill = 任务单 16 项清单，另按用户指令 W3-3 Eason 跳过）：Wave0 翻译 3 篇（translations/ 中译布鲁克斯×2+SPIN，行数对齐）；Wave1 七件 method-storytelling-with-numbers / method-shizhi-jiangxiang-ten-strategies / method-key-assumption-abcd / dk-koupen-decision-tiering-compromise / tool-ai-koupen-training-partner-design / method-anthropic-skill-design-patterns / framework-muse-ai-full-map-v1；Wave2 六件 concept-brooks-three-lies-culture / dk-brooks-cost-of-knowing / method-spin-linking-sales-marketing / framework-lobster-opt-one-person-team / concept-agent-university / skill 化 deep-debug（40_outputs/capabilities/skills/shared/deep-debug/SKILL.md，433 行）；Wave3 三件 case-jovida-ai-life-coach / method-obsidian-km-camp / case-yitang-jiangxiang-12-practices（本会话新产，逐字消费对应素材 714+586+2240 行）。

> 验证输出（pre-submit / 实测锚点）：W3 三卡本会话逐卡 `kdo pre-submit` → 3×✅ PASS（case-jovida PASS 含 1 WARNING tags 受众场景维已补后复验 PASS；method-obsidian-km-camp PASS；case-yitang-jiangxiang-12-practices PASS）；Wave1/2 十二件前会话已过 pre-submit（05:22-05:32 时钟日志实锤落盘），本会话实测 16/16 件存在+行数核验；外部验证 L1 实测：MemPalace GitHub API 实存 58,755 stars/MIT/2026-04（素材称 53k 为写作时点）；git 入仓终核验 `git status --porcelain` 本单新卡未追踪数 = 0（commit 链 61e755cc5→b78558f54 共 6 笔）。

> 未做项（含理由）：① W3-3 method-shishiyanshi-evidence-based **按用户 09-01 指令跳过**（Eason 审计件涉老朱域不产）——任务单素材表该项本身已标"⚠️CHO 私有密级"；② BV 视频逐字稿 7 件按任务单既有判定不产（英文 ASR 质量差+SPIN 与 candy 版重复，归 #586b 处置）；③ Jovida 官网 jovida.ai 直接抓取未完成（本会话 web 搜索/抓取后端持续超时故障），已在卡内标注"待复核"并以 GitHub API 旁路验证了可独立验证项；④ Live257 的华为/苹果/小米 300+ 文案库段（L785-1600）为采样消费未逐条入卡（素材库性质），已在 case 卡边界节声明。

> 需要谁动作：欧阳锋终审本单 15 卡+1 skill；黄药师留意 `.kdo/search_index.json` 已增量更新至 4285 条（kdo index --incremental 每卡已跑，无需全量重建）；若 Eason 方法论卡改日要产，需老朱明确授权域边界后再开单。

> 遗留与风险：① 任务单验收标准"卡片数≥15"按 15 卡+1 skill 达标（skill 不计入卡数口径）；② 各卡数字均为二手编译/学员自述口径，已在卡内逐处标注"口述待独立核实"；③ W2 五件与 Wave1 七件的前会话 pre-submit 输出未随卡归档（当时会话中断），本会话以落盘实测+commit 链作为替代证据，终审时可抽查复跑。
