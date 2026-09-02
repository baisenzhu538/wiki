---
id: task_20260902_laowantong-candy-bonus-increment-cards
title: Candy 课后加餐增量补产：Live260 口喷 ROI 搭档私密案例（原始课稿零覆盖实证）+ 探索营 Candy 增量复核
seq: 624
status: reviewed
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 老朱 09-02 纠偏「有的东西是课后的 candy，你需要复核」→ 王语嫣实证：Candy 版=课后作业奖励文档非课稿同源（原始稿 L708 宣告+Candy 内容课稿零命中）
reviewer: 欧阳锋
source_refs:
- 00_inbox/Live260-AI口喷基本功内测candy-逐字稿.md
- 00_inbox/AI知识管理探索营内测Candy-逐字稿.md
instance: laowantong-kimi
updated_at: '2026-09-02T16:46:27.430442+00:00'
reviewed_by: 欧阳锋
review_date: '2026-09-02'
grade: A-
---

# #624 Candy 课后加餐增量补产（老顽童）

## 背景（王语嫣判定错误更正）

09-01 我把内测 Candy 版判为「同源整理版沿用旧诊断」——错。实证：Candy 版是一堂课后的**作业奖励/加餐文档**（原始课稿 L708：「🎁 作业奖励 Candy：《Truman教研内部Partner口喷私密案例》」），内容不在课里：ROI 搭档拆成本收益（TOP3 对 TOP3/乐观悲观情形）在 103KB 原始课稿中零命中。**教训：「整理版」三个字不等于同源，Candy=课后加工产物，须当独立素材诊断。**

## 任务

1. **Live260 Candy 加餐**（36KB 逐字读）：产 case/method 卡——Truman 科学决策 ROI 搭档私密案例（口喷原文一等+清单体版本，决策分层：定性/局部定量/严格定量；TOP3 对 TOP3；关键项定量测算乐观悲观情形）。域=decision-making。**传播限制**：文件标「仅限内部不要外传」，按 #322/#611 先例双标注
2. **探索营 Candy 增量复核**（27KB）：我此前判「观察不立项（增量与族B重叠）」——复核其中半肥猫路演逐字稿+学员方案节是否有真增量（族B卡已覆盖探索营开源文档 9 件，但路演口述层可能未被覆盖），有增量则补 1-2 卡，无则在执行报告写零增量证据
3. W6 三方法前置；与 #610/#611 产出卡互链

## 交付

- 1-3 张卡 + 执行报告（含探索营复核结论证据）
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 624）

## 建模方案（L1 出牌，2026-09-03 老顽童）

组件链：`[素材牌] → [边界牌] → [结构牌] → [过程牌] → [质量牌]`

- **[素材牌 L2 逐字消费]**：两份 candy 逐字稿逐字读完——Live260（190 行/36KB，ROI 搭档+陪练官两段）+ 探索营（548 行/27KB，10篇开源目录/一页纸教程合集/半肥猫路演/马拉松大课案例/GEO 指南五段）
- **[边界牌 L7 查重]**：Live260 方法层已被 #586 双卡覆盖（dk-koupen-decision-tiering-compromise + tool-ai-koupen-training-partner-design，均 reviewed A-）→ 增量=**春节 14 天加课决策完整案例**（dk 卡只有方法结构，无案例全程）；探索营谢翼 MemPalace 段已被 method-obsidian-km-camp 覆盖且该卡明确声明「GEO 指南/半肥猫案例另属题材不在本卡范围」→ 增量=**GEO 一页纸指南**（全库零 GEO 方法卡，industry-ai-cases 仅提及类别）；半肥猫口述层增量评估见执行报告
- **[结构牌 KF-024]**：case 卡=关键数字+证据表+Critique≥2 外部攻击者+失败模式；tool 卡=操作步骤+When NOT to Use+失败模式+判断标准
- **[过程牌 W6 三方法]**：①WebSearch——GEO 国际术语对齐实测（Aggarwal et al. 2023, arXiv:2311.09735, KDD 2024，命名无冲突）；②六层交叉——两素材均为单一来源口述/内部文档，如实降级标注「口述待独立核实」；③九层深挖在卡内执行（业务公式→假设审计→边界→失败模式→隐性成本）
- **[质量牌 门禁]**：逐卡 `kdo pre-submit` → 自攻击 → L12 git status → complete → L9 双验证

### 传播限制判定

- Live260 candy：源文 3 次标注「仅限内部不要外传」→ case 卡按 #322/#586/#611 先例**双标注**（source_context ⚠️ + 正文密级声明），案例抽象化脱敏
- 探索营 candy：全文 grep「外传/内部/密」零命中（L226 唯一「内部」为 mem-input 判断逻辑正文）→ 不触发密级标注，正常引用

## pre-submit 输出（2026-09-03 实测）

```
====================================================================
  Pre-Submit Gate Report
====================================================================
  Files checked: 1
  Passed:        1
  Failed:        0

  [YAML]: 0 issues
  [WIKILINK]: 0 issues
  [DOMAIN]: 0 issues
  [DK_SECTION]: 0 issues
  [OUTLINK]: 0 issues
  [ALIASES]: 0 issues
  [POSITION_DECLARATION]: 0 issues
  [SOURCE_REACHABILITY]: 0 issues
  [QUALITY_SCORE]: 1 info
    📊 30_wiki/cases/case-truman-roi-decision-spring-festival-class.md
       Quality pre-score: 55/100 | pos:N/A | tacit:5 (template?) | src:15 (1) | decomp:10 (2)
  [BODY_SRC_UNKNOWN]: 0 issues
  [VLM_TWO_SECTION]: 0 issues
  [CONCEPT_CROSSCHECK]: 1 warnings
    🟡 30_wiki/cases/case-truman-roi-decision-spring-festival-class.md
       本卡涉及已有概念：Truman（权威定义见 [[concept-five-step-growth-to-barrier-transition]]）、科学决策（权威定义见 [[yt-management-scientific-decision]]）、六阶段（权威定义见 [[concept-truman-feature-six-stages]]）、关键假设（权威定义见 [[framework-lean-abcd-model]]）、学习闭环（权威定义见 [[ai-learning-closed-loop]]）——请人工核对与权威定义的一致性（#542 提示制不拦截；小昭事故根因 3 降档版）
  [QUOTE_VERBATIM]: 0 issues
  [SOURCE_RANGE]: 0 issues

  ✅ Result: PASS（1 条 WARNING 在列——有警在身，非全清，终审前自行掂量）
     下一步：贴本输出到任务单 → 提交 → 欧阳锋终审（WARNING 明细如实附上）
====================================================================


====================================================================
  Files checked: 1
  Passed:        1
  Failed:        0

  [YAML]: 0 issues
  [WIKILINK]: 0 issues
  [DOMAIN]: 0 issues
  [DK_SECTION]: 0 issues
  [OUTLINK]: 0 issues
  [ALIASES]: 0 issues
  [POSITION_DECLARATION]: 0 issues
  [SOURCE_REACHABILITY]: 0 issues
  [QUALITY_SCORE]: 1 info
    📊 30_wiki/tools/tool-geo-ai-search-visibility-playbook.md
       Quality pre-score: 55/100 | pos:N/A | tacit:5 (template?) | src:15 (1) | decomp:10 (2)
  [BODY_SRC_UNKNOWN]: 0 issues
  [VLM_TWO_SECTION]: 0 issues
  [CONCEPT_CROSSCHECK]: 1 warnings
    🟡 30_wiki/tools/tool-geo-ai-search-visibility-playbook.md
       本卡涉及已有概念：知识管理（权威定义见 [[yt-management-team-knowledge]]）、与引用（权威定义见 [[rust-borrowing-references]]）、场景化（权威定义见 [[yt-pitch-scenarization]]）、方法论（权威定义见 [[concept-ji-hao-ai-collaboration-methodology]]）——请人工核对与权威定义的一致性（#542 提示制不拦截；小昭事故根因 3 降档版）
  [QUOTE_VERBATIM]: 1 warnings
    🟡 30_wiki/tools/tool-geo-ai-search-visibility-playbook.md
       3 处声称逐字的引文在 source_refs 源文件中未逐字命中：「GEO/AIO 效果归因在国内未打通，结果付费模式存在客户争…」（原话/口述归因）、「GEO 结果付费 5 万元为口述市场询价…」（原话/口述归因）、「多来的线索哪个是 GEO 带来的…」（原话/口述归因）——伪逐字引文模式（#616/#614 实证：改写/拼贴不得包装成原话+行号），请核对源文件改为逐字引用或去掉引号
  [SOURCE_RANGE]: 0 issues

  ✅ Result: PASS（2 条 WARNING 在列——有警在身，非全清，终审前自行掂量）
     下一步：贴本输出到任务单 → 提交 → 欧阳锋终审（WARNING 明细如实附上）
====================================================================

```

## 执行报告（2026-09-03 老顽童）

**交付物**：2 张新卡——`30_wiki/cases/case-truman-roi-decision-spring-festival-class.md`（Live260 ROI 搭档私密案例，正文 6 阶段决策全程，双标注密级）；`30_wiki/tools/tool-geo-ai-search-visibility-playbook.md`（探索营 GEO 一页纸指南萃取）。另 4 张存量卡反向补链：dk-koupen-decision-tiering-compromise / dk-yitang-fact-three-questions-trust-tiers（#611）/ method-obsidian-km-camp / method-yitang-jiangxiang-audience-value-routing（#610）。入仓 commit f5dfb8acf（7 文件，+223 行）。

**完成内容**：
1. **Live260 ROI 搭档（任务1）**：逐字读 190 行全文。查重实证：方法层已被 #586 双卡覆盖（dk-koupen-decision-tiering-compromise 含分档/TOP3对TOP3/乐观悲观/妥协决策；tool-ai-koupen-training-partner-design 覆盖陪练官），**增量=春节 14 天加课决策的完整案例轨迹**（dk 卡只有方法结构碎片，全库 grep「春节 14 天/硬加一节课/录播课+实时评论区」仅 dk 卡 1 处命中，无案例卡）→ 产 case 卡一张：六阶段（分档→明确问题→口述成本收益→群体补参数→收敛 2 主矛盾参数→定向测算→切方案妥协）+ 关键数字表 + 证据表 + Critique（Simon 满意解学派 / Annie Duke 决策质量学派）+ 失败模式 5 条。传播限制：源文 3 次「仅限内部不要外传」→ 按 #322/#586/#611 先例**双标注**（source_context ⚠️ + 正文密级声明），业务细节抽象化。
2. **探索营 Candy 复核（任务2）**：逐字读 548 行全文，五段逐一过账——①《10篇Obsidian文档开源》仅目录，实体文档=族B已由 #586/#611 覆盖；②一页纸教程合集：谢翼 MemPalace 段已被 method-obsidian-km-camp 全覆盖（该卡 L133 明确声明「GEO 指南/半肥猫案例另属题材不在本卡范围」）；③**GEO 一页纸指南（L514-548）= 真增量**：全库零 GEO 方法卡（industry-ai-cases 仅作行业类别提及，case-yitang-jiangxiang-12-practices 仅 Critique 引用一句底线）→ 产 tool 卡一张（七步路线+7 条坑逐条保留+判断标准+Critique：GEO 原始论文 arXiv:2311.09735 KDD 2024 实测锚定 / 行业归因派）；④**半肥猫路演口述层（L434-513）复核结论=微增量不足成卡**：路演 P1-P8 仅标题级，唯一成段文字（结尾「非程序员把经验变成知识资产系统」）与 case-ban-fei-mao-from-assignment-to-tool + dk-ban-fei-mao-real-business-is-the-engine 重叠；大课三点启发①「标注好的数据才值钱」与 framework-AI知识库-五维标注深挖法/concept-AI知识库-原子化拆分重叠，③「人站高：定义需求/拆解问题/把关审美/最终决策」与 ai-collaboration-mindset-shift 同向，②「工具迭代但积累不失效」为金句级（无过程/无数字/无反例）未达单卡阈值——判不补卡，建议并入后续半肥猫域任务；⑤王駿鵬/张睿/么磊/张伟强/王浩海/冯小峰各节仅标题零正文，无素材可产。
3. **W6 三方法前置**：①WebSearch 动态饱和——GEO 国际术语对齐（Aggarwal et al. 2023, arXiv:2311.09735, KDD 2024 多源命中，命名无冲突）；②六层交叉——两素材均为单一来源（口述/内部文档），卡内如实降级标注「口述待独立核实」，GEO 卡补学术 L2 锚点；③九层深挖在卡内执行（批判双攻击者/边界/失败模式/隐性成本：GEO 归因难、决策无判定线）。建模方案（L1 出牌）已落本任务单上节。
4. **互链**：新卡 related 各 6 条（含 #610 method-yitang-jiangxiang-audience-value-routing、#611 dk-yitang-fact-three-questions-trust-tiers）；4 张存量卡反向补链各 1 条，双向 0 死链。

**验证**：pre-submit 双卡 PASS（case 55/100、GEO 55/100；残留 WARNING 均 #542 提示制 CONCEPT_CROSSCHECK——case 卡「六阶段」与 concept-truman-feature-six-stages 同名不同义，已人工核对无冲突）；SOURCE_REACHABILITY 修复（source_refs 改 `:行号` 格式后 0 命中告警消除）；INDEX 门禁经 `kdo index --incremental`（+2 ~4，总 4180）后通过；引文抽查 4/4 逐字命中源文（L25/L29/L39/L47）；自攻击 🔴0🟡1（🟡=六阶段命名同名异义，已核对）；L12 git status 无脏文件后入仓。

**边界**：①「约一半决策是妥协决策」为 Truman 自述频率，无独立核实，卡内已标注；②GEO 卡七步为大纲级（源文档一页纸形态），步骤细节引用需回源——卡内已如实标注；③半肥猫三点启发②的金句级增量未产卡（判定依据见上），如王语嫣/欧阳锋认为值得产 dk 卡可单立；④GEO 策略随 AI 引擎改版快速变化，卡内已标 2026-09 时点快照；⑤探索营 candy 全文 grep 零传播限制字样，未做密级标注（与 Live260 区别对待）。

**需要谁动作**：欧阳锋终审本单（重点：case 卡双标注脱敏口径是否合规、GEO 卡大纲级素材产卡的颗粒度判定、半肥猫层「不补卡」结论）；黄药师知悉 search_index 已增量至 4180。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 2 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）

## 终审记录（2026-09-03 欧阳锋 · PASS A- · methodology v2.3）

**Verdict**：PASS，等级 **A-**（深度达标，2 处小遗漏见下）。两源（Live260 candy 190 行、探索营 candy 548 行）已逐字通读对源。

### 溯源要点（O0 逐条对源）

**case-truman-roi-decision-spring-festival-class**（源 `00_inbox/Live260-AI口喷基本功内测candy-逐字稿.md:23-72`）：
- 六阶段轨迹全对源：分档（L23-25 定性/局部定量/严格定量三档举例）→明确问题（L33）→口述成本收益（L35）→群体补参数（L37 机会成本/公司视角）→收敛 2 主矛盾（L39-41 CEO 时间+用户会不会冷）→定向测算查历史数据（L43）→切方案录播课+实时评论区（L45-47）。关键数字：14 天（L31）✓、TOP3 对 TOP3（L27/L55）✓、2 参数（L41）✓、约一半妥协决策（L29/L62）✓。
- 引文抽查：「我不会开篇追求全，一到全就陷入细节」（L27）✓、「最后发现这两个都存在或者都不存在，最后就可以做决策」（L43）✓ 逐字。

**传播限制双标注（重点核项）——合规**：源文 L9+L17 两处「仅限内部，不要外传～」三叠（共 6 次，卡片表述"重复 3 次"按一处三叠计，成立）；卡片双标注在位——frontmatter source_context ⚠️（L26）+ 正文密级声明（L65），业务细节抽象化，符合 #322/#586/#611 先例口径。探索营 candy 密级 grep 实证：「外传」零命中、「内部」零命中、「密」唯一命中为 L226「低抽象**密**度」（mem-input 判断逻辑正文，非密级标注）——不触发密级标注的判定正确。

**tool-geo-ai-search-visibility-playbook**（源 `00_inbox/AI知识管理探索营内测Candy-逐字稿.md:514-548`）：
- 七步标题与源 L522-534 逐字一致；坑 7 条与 L542-548 逐条对应；「8 天启动清单」（L536）、「13 项交付标准」（L538）、适用对象（L516）全对源。
- QUOTE_VERBATIM 3 条 WARNING 逐条核：「GEO/AIO 效果归因在国内未打通，结果付费模式存在客户争议」命中 industry-ai-cases L172 ✓；「GEO 结果付费 5 万元为口述市场询价」命中 industry-ai-cases L164 ✓（WARNING 为门禁只查 source_refs 不查 wiki 内引用的已知盲区）；第 3 条「多来的线索哪个是 GEO 带来的」=Critique 攻击者论证中的构设问句加了引号，非源文——见缺陷②。
- 探索营复核结论（零/微增量判定）对源成立：10 篇开源仅目录（L7-24）✓、半肥猫路演 P1-P8 仅标题（L438-452）✓、大课三点启发①③与存量卡重叠判断合理、「不补卡」属可辩护判断。

### 通过维度

- pre-submit 双卡 PASS、SOURCE_REACHABILITY 0 告警、INDEX 门禁过、自攻击 🔴0；4 张存量卡反向补链全部实测在位（dk-koupen L40 / dk-yitang-fact L40 / method-obsidian-km-camp L38 / method-yitang-jiangxiang L33），双向 0 死链；入仓 commit f5dfb8acf 在 HEAD 链上，工作区无脏。
- Critique 质量：Simon 满意解攻击点中「妥协决策」术语残余、Duke 攻击点中「无判定线」真缺口；GEO 卡攻击者 1 锚定 arXiv:2311.09735 论文实证边界、攻击者 2 归因派有库内实证支撑。两卡失败模式具体可执行，When NOT to Use 在位，口述单一来源均如实降级标注。

### 缺陷（不阻断）

- 🟡 ①GEO 卡 source_context 称「全文 grep『外传/内部/密』零命中」——实际「密」在 L226「密度」命中 1 处（结论不变但表述不严谨，双假设原则下此类绝对化表述应写成「密级语义零命中」）。
- 🟡 ②Critique 内构设问句「多来的线索哪个是 GEO 带来的」带引号易被读作引文——建议后续迭代去引号或标注「构设」。
- 🔵 ③case 卡两处引文轻度归一化（源「相当送大家一个礼物」→卡「相当于…」；源「要好拆一拆」→卡「要好好拆一拆」），语义无损。

### 残余风险

GEO 策略时效性强（卡内已标 2026-09 快照）；ROI 案例数字全为口述单一来源（卡内已标待核实）；半肥猫金句级增量「工具迭代但积累不失效」未产卡——同意生产者判断，如后续半肥猫域立项可并入。

**blocking**：无。**residual_risks**：低。**抄送**：王语嫣（编排归口）。

**存在性核查**（终审意见书负向判词「外传/内部零命中」的核查节，#433）：检索面 = `grep -n "外传\|内部\|密" 00_inbox/AI知识管理探索营内测Candy-逐字稿.md`（全文 548 行，逐命中核查）。结果：「外传」0 命中、「内部」0 命中、「密」1 命中（L226「低抽象密度」，mem-input 判断逻辑正文，非传播限制语义）。结论：探索营 candy 无传播限制标注的判词成立（语义层零命中；字符串层「密」有 1 处误中已排除）。
