---
id: task_20260903_laowantong-live261-protracted-war-cards
title: Live261 战略笃定卡组：教育版论持久战 framework（科学派vs经验派矛盾分析）+ 开放麦三案例（路禹/Jacky IP/李秀慧复合弓）
seq: 633
status: reviewed
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-03
decision_source: inbox 值守拍分诊（09-03 19:38）：先例双查——存量卡 case-20260829-zhanlue-dingding-l3-extraction 是提取方法卡非内容卡，内容级增量成立
reviewer: 欧阳锋
source_refs:
- 00_inbox/Live261-一堂战略笃定作业candy-逐字稿.md
instance: laowantong
updated_at: '2026-09-03T12:47:34.295117+00:00'
evidence: 60_feedback/adversarial/atk_live261-protracted-war-cards_20260903.md
reviewed_by: 欧阳锋
review_date: '2026-09-03'
grade: A-
---

# #633 Live261 战略笃定卡组（老顽童）

## 背景

素材 58.7KB Candy 作业整理版：主件「一堂·教育版本的论持久战 V1.0」（用论持久战框架自我战略分析：科学派 vs 经验玄学派的根本矛盾/质量数量趋势三维度/内外部矛盾/持久战结论）+ 开放麦三场（路禹《战略笃定》/Jacky「IP营销的持久战」/李秀慧「复合弓业务的论持久战」）。
先例核查：存量 case-20260829-zhanlue-dingding-l3-extraction=段王爷提取方法卡（非内容卡），不撞车；strategy 域词池在（strategy.yaml）。

## 任务（W6 三方法前置）

1. **framework**：教育版论持久战——矛盾分析法做战略笃定（根本矛盾判定→质量/数量/趋势三维度→内外部分解→持久战结论结构）
2. **case ×3**：三个行业的持久战应用（各一张小 case：行业+矛盾判定+策略选择+阶段判断）
3. 互链：strategy-domain-digest 挂接 + 与论持久战/战略族存量卡互链

## 边界

- Candy=课后作业整理版，标注「Candy 整理形态」（#626 口径）；发现传播限制声明则双标注
- `_tmp_live261_blocks.json`=管线数据附件，不入编排不动它
- 六维标签建议参考 strategy.yaml 词池

## 交付

- 1 framework + 3 case + 执行报告（三方法记录+互链 0 死链实证）
- claim/complete 走 queue_transition（complete 633）

## 建模方案（L1 出牌，2026-09-03 老顽童）

素材已逐字读 868 行（主件教育版论持久战 V1.0 + 开放麦三场）。出牌链：

`[#2 素材牌：整理稿逐字读全文] → [#6 先查已有卡] → [#7 先对标准则（WebSearch 命名核查）] → [#10 结构牌：先骨架再填肉] → [#5 边界牌：适用边界/When NOT] → [#14/#16 质量牌：pre-submit+脚本实测]`

- **#2 素材牌**：Live261 逐字稿 868 行全量消费（含末尾互动/广告/闲聊段）。理由：P-31 教训，Candy 整理版易藏拼接断裂（实证：复合弓场 L788 后混入营销分享残段「星哥讲增长」，卡内需如实标注）。
- **#6 先查已有卡**：`kdo cards --domain strategy` + `kdo query 论持久战` → 存量 `framework-strategy-conviction`（战略笃定实证卡，Truman 七轮决策，传播限制标注在位）、`case-20260829-zhanlue-dingding-l3-extraction`（段王爷提取方法卡，非内容卡）——内容级增量成立，新卡与存量互链不重复。理由：P-22 防重复建设。
- **#7 先对标准则**：WebSearch 实证「On Protracted War」=毛选 1938 通行译名（军事史语境，chinahandsmagazine.org / acoup.blog），无商业战略框架同名冲突；「教育版论持久战」加限定词命名安全。理由：P-28/BRM 教训。
- **#10 结构牌**：framework 骨架=问题背景（双误判：亡国论式机械论/速胜论式唯心论）→底层矛盾（根本矛盾+质/量/趋势三维内部矛盾+外部矛盾）→结论（时间在哪边）→条件阶段（重要条件+三阶段）→具体策略（本质定义→必经之路→增长飞轮→具体问题具体分析）。case 骨架=行业+矛盾判定+策略选择+阶段判断+关键数字+证据表。
- **#5 边界牌**：framework 写适用边界（质/量双强不需持久战、双弱应换分析主体——素材 L329-335 明示）+When NOT to Use+失败模式；v2.3 要求补 Critique/Action Triggers（#626 终审 TODO 口径，本批直接补齐）。
- **#14/#16 质量牌**：每卡 `kdo pre-submit` 逐卡跑贴输出；互链 0 死链用脚本实测；complete 后 status+任务单双验证（L9）。

**标注口径（照 #626）**：素材=Candy 作业整理形态，全库无其他原始课稿→各卡 source_context 标「Candy 整理形态逐字稿，本稿即唯一一手源」；素材全文 grep「传播限制/不要外传」0 命中→无需 #322 双标注（核查记录入执行报告）。tags 参考 strategy.yaml 词池（六轴 5-8 词，来源形态词走来源维度，不进内容词）。

## 执行报告（2026-09-03 老顽童）

**交付物**：4 张卡 + digest 挂接 + 自攻击报告——①`30_wiki/frameworks/framework-education-protracted-war.md`（教育版论持久战 framework，正文含六步论证链+适用边界+失败模式 7 条+双攻击者 Critique+Synthesis 不要用场景表+Action Triggers，v2.3 全结构）②`30_wiki/cases/case-live261-luyu-strategy-conviction-maoxuan.md`（路禹场：毛选三层哲学底座+矛盾分析 15 例实例库）③`30_wiki/cases/case-live261-jacky-ip-marketing-protracted-war.md`（Jacky 场：IP 营销行业完整论持久战作业+三阶段认知演进）④`30_wiki/cases/case-live261-lixiuhui-compound-bow-dealer-war.md`（李秀慧场：复合弓 Top1 vs 最大经销商渠道战争+素材拼接断裂如实标注）⑤`30_wiki/domains/strategy-domain-digest.md` 挂接 2 行（核心框架表+关键案例表）⑥`60_feedback/adversarial/atk_live261-protracted-war-cards_20260903.md`（四路自攻击报告）。建模方案已落本单「## 建模方案」节（L1 出牌链+三方法前置记录）。

**完成内容**：素材 868 行逐字读全文（含末尾互动/广告/拼接残段）。framework 卡按任务单骨架产出：根本矛盾判定（科学派 vs 经验玄学派）→质/量/趋势三维→内外部矛盾→持久战结论→条件阶段→四件套策略；判定规则（质/量双弱换分析主体、双强不需持久战、补充速度>损耗速度）从路禹场 L329-369 补入并注明出处。三张 case 卡各含行业+矛盾判定+策略选择+阶段判断+关键数字表+证据表+双攻击者 Critique。先例双查实证：存量 `case-20260829-zhanlue-dingding-l3-extraction`=段王爷提取方法卡（非内容卡）、`framework-strategy-conviction`=战略笃定定义/实证层——本批为论证方法层+行业应用层，增量成立无撞车。Candy 标注口径照 #626：4 卡 source_context 均标「Candy 整理形态逐字稿，本稿即唯一一手源」；传播限制核查 grep 素材「传播限制/不要外传」0 命中→无双标注。

**验证**：①pre-submit 4/4 PASS（首轮 FAIL 项全修复：aliases 补源文件名 4 卡、伪逐字引文 16 处逐条对照源文逐字化或去引号、luyu 卡断链 `concept-yitang-…`→`concept-一堂-hypothesis-driven-business-methodology`、INDEX 错误经 `kdo index --incremental` 两轮归零；残留 WARNING=CONCEPT_CROSSCHECK 提示制 4 条，已人工核对——增长飞轮/矛盾论/产品内核/第一性原理/业务公式等均沿用一堂权威定义语义，无冲突）②互链 0 死链实证：find 实测 9 个被链卡 id 文件 9/9 存在（见上节清单），pre-submit WIKILINK 检查 4 卡 0 errors ③检索面：`kdo index --incremental` 后 search_index total 4199，4 卡可查 ④自攻击：四路攻击报告落盘（🔴0/🟡1 已修复——lixiuhui 卡「困局重构表+阶段判断」补生产侧推演属性标注/🟢4 留终审参考）⑤入仓：3 卡+digest+任务单经 vault backup 20:18/20:28 两拍入仓（git log 实证 `4fcae4bbd`/`c9ab1daca`）；lixiuhui 自攻击修复+攻击报告待下一拍收走（complete 前 git status 复核）。

**边界**：①4 卡均为单一来源（Candy 整理形态），讲者自述数字全部 self-report 降级标注，未经独立核实 ②lixiuhui 卡战局结局素材未披露，阶段判断为框架推演（卡内已标）③素材 L786-836 拼接段（科学营销宣讲+星哥讲增长）归属未定，本批不抢先入卡，留待对账后立项（阳谋论 dk 候选）④framework 卡 Critique/Action Triggers 按 v2.3 补齐（响应 #626 终审 TODO 口径）；#626 终审 TODO 中 framework-course-thought-production-line 卡的补节任务挂在 #629 批次，不在本单范围 ⑤`_tmp_live261_blocks.json` 按任务单边界未动。

**需要谁动作**：欧阳锋终审 #633（重点：framework 判定规则来自路禹场的跨场引用是否接受、lixiuhui 卡生产侧推演标注口径、拼接段处置方式）；王语嫣：拼接段（L786-836 科学营销宣讲/星哥讲增长）归属对账后决定是否单独立项。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 6 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）

## 终审记录

**终审结论**：PASS A-（欧阳锋 · 2026-09-03 · methodology_version v2.3）
**阻断判定**：无 Critical / High 阻断项；2 处低优先级表达层改进点（放行，不构成返工）
**五维评分**：溯源完整 24/25 · 逻辑骨架 25/25 · 暗知识密度 18/20 · 可操作性 14/15 · 表达质量 13/15 → 94（A-）

**O0 溯源**：已打开唯一 source_refs 源文件 `00_inbox/Live261-一堂战略笃定作业candy-逐字稿.md`（实测 868 行），逐条核验四卡引文与行号锚——L25/L53/L69-70（framework 原始表述）、L119/L142/L152/L210-212/L221-247（luyu 哲学三层+15 例）、L513/L519/L523/L531-L537/L553-L578/L607-609/L619-L638/L676-686（jacky）、L694-L754/L772/L786-L866（lixiuhui 战争叙事与拼接段）——全部命中，无编造、无跨场串行。

**存在性核查**（互链/死链/先例/source_refs/digest）：
- 互链：4 卡 related 共引用 10 个卡 id（3 张新卡 + 7 张存量卡），按 `id:` 逐一查证 10/10 文件存在，0 死链。
- source_refs：`check-source-refs.py` 逐卡校验 4/4 文件存在、0 污染引用。
- 先例双查：`case-20260829-zhanlue-dingding-l3-extraction`=提取方法卡、`framework-strategy-conviction`=战略笃定定义/实证层——本批为论证方法层+三行业应用层，增量成立无撞车。
- digest 挂接：`strategy-domain-digest.md` 核心框架表+关键案例表各 1 行已入位。

**审查裁定（生产方提出的三个重点）**：
1. framework 判定规则跨场引用（L329-335 质/量双弱换分析主体、L363-367 补充速度>损耗速度）——**接受**：卡片在两处标注「路禹场补充/关键补充」出处，规则语义与 framework 第三步自洽，非移花接木。
2. lixiuhui 生产侧推演标注——**核销**：「谈打抉择」节与「阶段判断」节开头均加 ⚠️ 推演属性标注，与自攻击 🟡 修复一致。
3. 拼接段处置——**接受**：「素材形态备注」节如实记录 L786 起科学营销宣讲断裂、不作为复合弓案例证据、「阳谋论」留待归属对账后另行立项，符合任务单边界。

**改进点（低优先级，放行）**：
1. framework 卡「原始表述」L69-70 引文在「然后找到更底层的规律」处收口，源文该句后续为「，然后尝试找到更底层的一般性本质」——引文收口位置偏前，语义无损，建议后续补全或将引号前移。
2. lixiuhui 卡 frontmatter source_context 标「L786-836 段」，而素材形态备注列举内容实际延至 L854/L866——边界口径小偏差（全貌已如实记录、不影响判定），建议统一为「L786-866」。
（以上两处随老顽童下批顺手修订即可，不单独立项。）

**需要谁动作**：老顽童（可选）——下批顺手修订上述两处表达层标注；王语嫣——拼接段（L786-866 科学营销宣讲/星哥讲增长）归属对账后决定「阳谋论」是否单独立项。
