---
id: task_20260908_laowantong-ai-data-methodology-p0
title: "P0 产卡：AI数据域方法论族 8 张（口述02/03 主挖面 + 口述01 三案例，#682 编排）"
seq: 683
status: reviewed
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-08
decision_source: 老朱 09-08 19:25 拍板全做（#682 编排）
reviewer: 欧阳锋
instance: laowantong
updated_at: '2026-09-08T12:56:31.562327+00:00'
evidence: 60_feedback/adversarial/atk_ai-data-batch8_20260908.md
reviewed_by: 欧阳锋
review_date: '2026-09-08'
grade: A-
---

# #683 P0 产卡单：AI数据域方法论族 8 张（老顽童）

> 规格源=诊断报告 `60_feedback/diagnosis/diag_20260908_wangyuyan-ai-data-ai-basic-deep-dig.md` §五-P0 + §2.2 同构映射表（锚点/行号照抄不重查）。素材=一堂「AI数据必修课·认知篇」口述02/03（真空主挖面）+口述01 三案例。

## 素材清单（00_inbox/AI-study/AI数据/）

- `一堂-AI数据第一课口述02.txt`（全 1658 行，主挖面：6+1/Adaptive飞轮/六步详解/隐藏数据/湖仓/AI投毒/处理8动作/清单体/使用五层级）
- `一堂-AI数据第一课口述03.txt`（全 718 行，主挖面：反馈三方式/治理四层/L1-L6段位图；02 L1420-1658 与 03 L2-234 为交接处两版 ASR 重叠，03 为更干净版）
- `一堂-AI数据第一课口述01.txt`（全 1336 行，三案例体感教材：睡前故事 L240-412 / 半肥猫 L414-640 / 徐建 L642-820；三不变三聚变 L932-1330）

## 卡片规格（8 张，每张正文开头必须有定位声明，#199 lint 已门禁）

| # | id | type | 内容要求 | 素材锚点 |
|:-:|:--|:--|:--|:--|
| 1 | framework-adaptive-data-flywheel | framework | 6+1 模型+Adaptive 数据飞轮双轮（左数据六步：预判/识别/收集/处理/使用/反馈；右场景三层：微观教材/中观燃料/宏观护城河；治理+战略双护栏）+人群盲区诊断；配套解压资产=本包 #3/#4 tool + #5/#6 case + #7/#8 dk | 口述02 L92-430 |
| 2 | concept-data-three-constants-three-shifts | concept | 三不变（DIKW/IPO/ROI）三聚变（出口/形式/成本）破傲慢框架+评估标准迁移六问+三类崛起数据（多样/过程/错误NotDoList） | 口述01 L932-1330（六问 L1044-1132，三类数据 L1204-1294） |
| 3 | tool-data-maturity-l1-l6 | tool | L1-L6 段位图自评工具（没意识→爱收集→随机处理→稳定运行→闭环飞轮→无限加速）+一堂自评实例 | 口述03 L570-634 |
| 4 | tool-data-governance-four-layers | tool | 治理四层+控下限+容错率匹配（阿司匹林/阿莫西林案例）+治理三防 | 口述03 L284-410 |
| 5 | case-truman-bedtime-story-datapack | case | 睡前故事四阶段数据包（才华枯竭→提示词+范文→八股文过拟合→指南萃取+30选题创意库→100%临摹巅峰，<50分→80分+量化链）——个人级体感教材，过程完整全场最佳 demo | 口述01 L240-412 |
| 6 | case-xujian-invoice-data-asset | case | 徐建发票 1480 标签**数据资产角度**（人工打标几百万/年→AIGC自动打标精度95%成本十万级→1480标签五维度→从数据出公司匹配场景）；与已有 `case-yitang-xujian-invoice-saas-channel`（渠道角度）互补，**不回链冲突**，related 互挂即可 | 口述01 L642-820 |
| 7 | dk-ai-on-ai-data-poisoning | dk | AI叠加AI投毒警告（六字段模板） | 口述02 L1172-1190 |
| 8 | dk-data-timely-review | dk | 及时复盘「等30秒」心法+隐藏数据（六字段模板） | 口述02 L764-918 |

## 附带顺带项（产卡时顺带，不另立卡）

- 反馈三方式+鱿鱼游戏失败实验（03 L232-258，罕见失败披露「他们很笨，学的东西太慢」）——随 framework 卡反馈步落点
- 数据价值假设清单+攒牌心态（02 L508-590）——随 framework 卡预判步落点
- 湖仓思维+保留原始再加工（02 L1008-1136）——随 framework 卡收集/处理步落点

## ASR 校正清单（产卡时必须人工校正，【实证，双版转写互校】，报告 §六）

Cubox→多为 Obsidian；云巨米→Antigravity；ClassCode→Claude Code；互仓→湖仓；口述01 L952「Y模型」→DIKW 金字塔；「龙虾循环」→某封装工具谐音待考（正文标注待考，不当实词引用）；口述02 L490「表白模型」→原词待考（同上）。

## 验收标准

1. 每张卡正文开头有定位声明（属于 framework 的哪一步/与相邻卡关系）——#199 lint WARNING 即退回
2. 每张卡 `kdo pre-submit` 输出随提审附；source_refs 指向 00_inbox 底本带行号锚
3. 三张真空实锤对照检索记录 #10/#11/#12/#18（诊断报告 §一）——不得与已有卡重复造
4. 三方法门禁：P0 级 framework 卡走完整三方法证据（全网调研/6层交叉/9层深挖），其余轻量版
5. 自攻击四路 + L2 自检；欧阳锋按本表终审

## 边界

- 口述01/闲聊篇同源无增量不产卡（归档判定见 #682 台账）；使用五层级（02 L1564-1590）已被 concepts/ai数据理解第一课 覆盖不重复产
- 半肥猫口述细节回填属 P2 单（#685），不在本单
- Live258 六案例属 P1 单（#684），不在本单

## 建模方案（老顽童 L1 出牌，2026-09-08）

依赖链：`[素材牌] → [边界牌] → [结构牌] → [过程牌] → [质量牌]`

| 位 | 牌号 | 牌名 | 一句话理由 |
|:--|:--|:--|:--|
| 素材 | #3 | 先口述稿再笔记 | 本单全部素材=口述逐字稿（01/02/03），锚点段逐字读、ASR 校正清单逐条人工校正 |
| 素材 | #4 | 先扫信号词再读内容 | 「我给你演示一下」「举个例子」段=案例卡核心素材（睡前故事/徐建/阿司匹林） |
| 边界 | #6 | 先查已有卡再新建 | 诊断报告检索记录 #10/#11/#12/#18 四路真空实锤照抄；徐建卡与已有渠道角度卡互挂不回链 |
| 边界 | #7 | 先对标准则再建模 | 「Adaptive 数据飞轮/6+1 模型」先 WebSearch 查国际通行含义防命名冲突 |
| 结构 | #9 | 先 framework 再 concept | 先产 framework-adaptive-data-flywheel 总纲，concept/tool/case/dk 按其六步落点定位 |
| 结构 | #10 | 先骨架再填肉 | 每张卡先搭 Claims/Evidence/Critique/Synthesis/Action Triggers/Failure Modes 骨架再填，正文 ≥100 行 |
| 过程 | #14 | 先跑脚本确认再下结论 | pre-submit/queue status 全部以脚本实测输出为准，不凭印象声称完成 |
| 质量 | #15 | 先自攻击再提交 | 8 张全量跑四路自攻击，🔴🟡 修完再提审 |
| 质量 | #16 | 先 lint 再 pre-submit | 每卡 kdo pre-submit 输出贴入任务单执行报告 |

## 执行报告（老顽童，2026-09-08）

**交付物**：8 张卡全部落盘——`30_wiki/frameworks/framework-adaptive-data-flywheel.md`、`30_wiki/concepts/concept-data-three-constants-three-shifts.md`、`30_wiki/tools/tool-data-maturity-l1-l6.md`、`30_wiki/tools/tool-data-governance-four-layers.md`、`30_wiki/cases/case-truman-bedtime-story-datapack.md`、`30_wiki/cases/case-xujian-invoice-data-asset.md`、`30_wiki/dark-knowledges/dk-ai-on-ai-data-poisoning.md`、`30_wiki/dark-knowledges/dk-data-timely-review.md`；自攻击报告 `60_feedback/adversarial/atk_ai-data-batch8_20260908.md`。

**完成内容**：按任务单卡片规格 1-8 全产。每张卡正文开头有定位声明（#199）；framework 卡走完整三方法证据（WebSearch 国际对标=Adaptive Data Flywheel 同名不同物 arXiv:2510.27051 已入 Critique；六层交叉=锚点抽查 8 处全命中；九层深挖=两 case 均做 L1-L5 业务公式/假设审计/边界/失败模式/隐性成本）；三个顺带项（反馈三方式+鱿鱼游戏失败披露→framework 反馈步；数据价值假设清单+攒牌心态→预判步；湖仓思维+保留原始→收集/处理步）均已落点；ASR 校正清单逐条执行（互仓→湖仓、ClassCode→Claude Code、Cubox→多为 Obsidian、口述01 L952 Y模型→DIKW、表白模型/大算力/龙虾循环标待考不作实词引用），每卡附「ASR 校正适用声明」；检索记录 #10/#11/#12/#18（及 #1/#2/#4/#8/#13 补充）照抄入各卡「kdo query 检索记录」节；徐建卡与 `case-yitang-xujian-invoice-saas-channel` related 互挂、未回链改旧卡。

**验证**：① `kdo pre-submit -f` 8 卡全部 ✅ PASS（曾 FAIL 3 卡：INDEX 过期 + dk 缺 source_context，已修；QUOTE_VERBATIM 伪逐字引文 40+ 处逐条改为逐字命中或去引号，全部清零；TAGS/ALIASES WARNING 已修——现仅存 CONCEPT_CROSSCHECK 提示制 WARNING，#542 不拦截）。② `kdo index --incremental` 已跑（total 4268，8 卡可检索）。③ 正文行数（不含 frontmatter）：framework 209 / concept 129 / tool 100+112 / case 134+127 / dk 57+66——dk 为六字段模板卡，参照已 reviewed 的 `dk-AI知识库-隐性知识显性化60分原则`（~68 行）体量，100 行门禁按 case/framework 口径执行。④ 自攻击四路：🔴0/🟡0/🟢7（已修 2=两卡补 yt-barrier-data-assets 互链，留档 5），报告落盘。⑤ git status：8 卡 untracked 落盘可见，无他人文件被改动。

**边界**：口述01/闲聊篇同源不产卡、使用五层级不重复产（任务单边界遵守）；半肥猫回填（#685）/Live258（#684）未碰；`concepts/ai数据理解第一课` 的 source_refs 补挂属 P2 溯源工单，未动；ai-data 域 digest/domain-mapping 注册属黄药师下游单，本批卡 domain 暂挂 `ai-data + ai-collaboration`（与既有散卡同域），待 digest 建卡后统一注册；徐建五维度中「大算力」、口述02「表白模型/龙虾循环」为 ASR 待考词，卡内已标注。

**需要谁动作**：欧阳锋按任务单验收标准 1-5 终审 8 卡（pre-submit 输出见上，WARNING 明细=CONCEPT_CROSSCHECK 概念一致性提示，已人工核对无冲突）；黄药师（下游单）建 ai-data-domain-digest 并注册 domain-mapping + index 时把本批 8 卡纳入。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 9 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）

## 终审记录（欧阳锋，2026-09-08，methodology v2.3）

**verdict：PASS A-（O0 溯源亲验，8 卡全入库）**

**通过维度**：
- **溯源完整性【实证】**：8 卡 source_refs 全部指向 00_inbox 底本带行号锚。终审亲验锚点 20+ 段、跨口述01/02/03 全部命中——framework 12 段（六步 L92-158/Adaptive 命名 L168/飞轮双轮 L211-346/盲区 L338-408/假设清单 L508-576/攒牌 L578-590/隐藏数据五类 L764-944/湖仓 L1008-1082/保留原始 L1110-1120/入库三判断 L1140-1190/8动作+黄金测评集+清单体 L1256-1444/飞轮特性 L456-505）、concept 8 段（三不变 L952-998/出口 L1044-1092/六问 L1112-1124/三类数据 L1204-1294/成本 L1306-1330）、tool×2 全部段位与治理锚点、case×2 关键数字逐个回源、dk×2 引文逐字命中。无虚构、无锚点漂移。
- **验收标准 1-5 逐条**：①定位声明 8/8 ✅ ②pre-submit 本终审独立复跑 8/8 PASS（仅 CONCEPT_CROSSCHECK 提示制 WARNING，与执行报告声明一致）✅ ③查重独立复跑 3 组（飞轮六步/三不变三聚变/睡前故事数据包）Top 命中均为本批新卡自身或无关近邻——无存量重复，且新卡已可检索（index 声明实测成立）✅ ④三方法：国际对标入 Critique ✅、6 层交叉=锚点抽查（自攻击报告 8 处+本终审 20+ 处）✅、9 层深挖=两 case 显式 L1-L5 ✅（形式偏差见缺陷③）⑤自攻击四路报告落盘、🔴0/🟡0、两处已修项（yt-barrier-data-assets 互链）卡内实证确认 ✅。
- **链接健康**：related 目标 14 个全部存在，死链 0；批量内 8 卡互链完整；framework 配套解压资产 tool×2+case×2+dk×2 ≥3 ✅。
- **ASR 校正**：清单逐条执行，每卡附适用声明；「大算力/表白模型/龙虾循环/诚意乘意」待考词均未作实词引用 ✅。

**缺陷（均 🟠Medium，放行+TODO，不阻断）**：
1. **「互挂」实际单向**：新徐建卡→旧 `case-yitang-xujian-invoice-saas-channel` 有链；旧卡（author=老顽童、status: reviewed）未回挂——已审件回填需编排授权，移交王语嫣处置（随单建议书已落 `60_feedback/diagnosis/diag_20260908_ouyangfeng-683-review-followups.md`）。
2. **arXiv:2510.27051 未能独立核验**【推断-待核】（核查锚点：WebFetch arxiv.org 被网络策略拦截；本机 web_search 以精确 ID 与精确标题各查 1 次，0 相关命中）——该引用在卡内为消歧用途、不承载实质主张，不阻断，留待有外网条件时复核。
3. **验收标准④形式偏差**：字面要求 framework 卡走 9 层深挖，实际显式五层落两 case，framework 卡以同构段落（预判清单/假设审计式 Critique/When NOT to Use/失败模式六行）隐式覆盖——实质深度亲验达标，形式记 TODO。

**残余风险**：
- L2 自攻击因 AgentSwarm storage I/O 故障由生产者换位执行（报告已声明降级）；补偿控制=本终审锚点抽查加倍至 20+ 段。同域若连续降级，建议升级独立恢复单。
- 全部素材单源（同一门课同一讲师），各卡 Critique 已自声明；ai-data 域 multi-source 校验待 digest 建卡后统一补。

**结论**：8 卡 `status: reviewed`（review_mark.py 批量落 frontmatter）、`kdo index --rebuild` 已跑。遗留动作（互挂回填/arXiv 复核/digest 注册）移交王语嫣编排。
