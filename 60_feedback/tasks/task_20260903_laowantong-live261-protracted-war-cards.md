---
id: task_20260903_laowantong-live261-protracted-war-cards
title: Live261 战略笃定卡组：教育版论持久战 framework（科学派vs经验派矛盾分析）+ 开放麦三案例（路禹/Jacky IP/李秀慧复合弓）
seq: 633
status: in_progress
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-03
decision_source: inbox 值守拍分诊（09-03 19:38）：先例双查——存量卡 case-20260829-zhanlue-dingding-l3-extraction 是提取方法卡非内容卡，内容级增量成立
reviewer: 欧阳锋
source_refs:
- 00_inbox/Live261-一堂战略笃定作业candy-逐字稿.md
instance: laowantong
updated_at: '2026-09-03T12:10:40.128794+00:00'
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
