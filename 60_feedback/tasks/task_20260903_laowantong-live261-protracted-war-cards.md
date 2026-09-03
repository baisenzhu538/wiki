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
