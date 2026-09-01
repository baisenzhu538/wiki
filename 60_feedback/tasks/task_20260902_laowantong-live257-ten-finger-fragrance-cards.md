---
id: task_20260902_laowantong-live257-ten-finger-fragrance-cards
title: Live257 重讲十指讲香模型卡组（十指讲香 framework + 用数字讲故事 method + 发布会文案案例）
seq: 610
status: reviewed
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-02
decision_source: inbox 01:51 批次分诊（diag_20260902_wangyuyan-inbox-batch-42 族A，老朱 0831/0901
  直令高价值素材直接编排产卡）
reviewer: 欧阳锋
source_refs:
- 00_inbox/Live257-重讲十指讲香模型内测Candy-逐字稿.md
related_tasks:
- '#596'
instance: laowantong-kimi
updated_at: '2026-09-01T23:46:14.357365+00:00'
evidence: _tmp/610_evidence.md
reviewed_by: 欧阳锋
review_date: '2026-09-01'
grade: A-
---

# #610 Live257 十指讲香卡组（老顽童）

## 背景

- 素材：`00_inbox/Live257-重讲十指讲香模型内测Candy-逐字稿.md`（131KB/1747 行，水水老师拆书《用数字讲故事》奇普·希思 + 十指讲香模型学员超级案例：华为/苹果/小米发布会文案拆解，案例作者王木匠/柴翔/贾红阳/沈伟杰）
- 入口诊断：域归属=**sales（表达/营销文案）**；库内有 `讲香基本功-李頔-260731/` 同族素材目录，编排前先 grep 查重（E022：主题词「讲香」+来源词「水水/Live257」双查）
- 体量 131KB 属大素材：逐字读全文（W1 硬规则，分多次读完），scan 类工具只做索引定位

## 任务（3-4 卡候选，最终形态按 W6 三方法定夺）

1. **framework**：十指讲香模型（场景化/口语化/数字化…升华化，十要素以素材原文为准）
2. **method**：《用数字讲故事》核心方法（奇普·希思，拆书层增量）
3. **case**：发布会文案拆解超级案例（华为/苹果/小米，学员实战——挑最完整 1-2 个立 case 卡）

## 验证

- pre-submit 全过；O0 溯源锚点=逐字稿路径+行号
- related 与存量讲香族/表达族卡互链双向 0 死链
- **传播声明检查**：内测 Candy 件若含「不要外传/仅限内部」字样，按 #322 先例加传播限制标注（Live260 同族已实证有限制字样）

## 六维标签建议（spec v1.6；sales 域轴缺如——生产者试点提新词，王语嫣审词入轴）

- 专业轴：销售 / 文案 / 表达 / 讲故事
- 对象轴：发布会文案 / 产品卖点 / 客户沟通
- 性质轴：框架 / 方法 / 案例
- 经验轴：实战 / 拆解 / 复盘
- 受众轴：销售 / 市场 / 创业者
- 来源轴：Live / 一堂内测 / 拆书（奇普·希思）

## 边界

- 原素材不动（00_inbox 只增不删）；学员案例署名保留
- 王宁/水水原话引用保持原样不美化

## 交付

- 3-4 张卡 + 执行报告（含三方法记录+互链实证）
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 610 附执行报告路径）

## 执行报告（2026-09-02 老顽童 laowantong-kimi）

**交付物**：3 张增量卡——①`30_wiki/cases/case-yitang-jiangxiang-huawei-matext-launch.md`（华为 MateXT 发布会双拆解深挖 case 卡，正文 101 行）；②`30_wiki/tools/tool-yitang-jiangxiang-launch-copywriting-arsenal.md`（华为/苹果/小米发布会文案最佳实践库 tool 卡，正文 136 行，承接沈伟杰 300+ 条素材库）；③`30_wiki/methods/method-yitang-jiangxiang-audience-value-routing.md`（受众×价值×策略路由 method 卡，宁波《文案的基本修养》交叉框架展开，正文 105 行）。

**完成内容**：①查重（E022 双查「讲香」+「水水/Live257」）命中关键事实——任务三候选中 framework（十指讲香）与 method（用数字讲故事）已由 #586（2026-09-01 欧阳锋终审 PASS A-）产出的 reviewed 卡全覆盖：`method-shizhi-jiangxiang-ten-strategies`、`method-storytelling-with-numbers`、`case-yitang-jiangxiang-12-practices`，另有存量 `concept-讲香-卖点直给到价值感`/`framework-一堂-十指模型`/`tool-讲香十指模型-超级武器库`（VLM 源同名异物）/`case-一堂-小米发布会拆解`（动力阻力触点透镜不同源）——按 P-22 不重建，仅做增量；②W1 硬规则执行：131KB/1747 行逐字稿两次 Read 逐字读完（含末尾 Q&A 与学员作业全文）；③锁定三处真增量并产卡：华为 MateXT 双拆解深挖（现有光谱卡仅一行表格）、沈伟杰 300+ 文案库（#586 case 卡声明采样消费未逐条入卡）、宁波受众×价值×策略矩阵（本体卡只用了「定受众」一步，矩阵未卡片化）；④反向补链 3 张存量卡（method-shizhi/case-12-practices/method-storytelling 各 +1~3 条 related 指向新卡）；⑤传播声明检查：逐字稿两版本+v5.json 全文 grep「不要外传/仅限内部/保密/禁止外传/勿外传/不要转发/内部资料」零命中（唯一「内部」命中为华为研发内部代号），不触发 #322 标注，卡片约束节如实声明内测件性质；⑥外部验证：MateXT 发布会日期/三档价格/10.2 英寸/3.6mm/天工铰链/5600mAh/66W+50W 快充经 WebSearch 比对华尔街见闻/爱范儿/IT之家/潮新闻 2024-09-10 报道一致，预约 430 万、「电子茅台」炒作作为反例入卡；⑦三方法记录（浓缩→质疑→对标）：浓缩=逐字稿 L244-475 双拆解压缩为十指逐指对照表+叙事结构还原；质疑=每卡 ≥2 外部攻击者（Ehrenberg-Bass 学派/归因视角/版权视角/框架原创性视角/受众完备性视角）+不要用场景表；对标=国际框架对齐（奇普·希思数字转换双路线、东东枪三类受众、FAB、SPIN 路线）；⑧sales 域轴新词建议（spec v1.6 试点，提请王语嫣审词入轴）：专业轴=销售/文案/表达/讲故事；对象轴=发布会文案/产品卖点/客户沟通；性质轴=框架/方法/案例；经验轴=实战/拆解/复盘；受众轴=销售/市场/创业者；来源轴=Live/一堂内测/拆书（奇普·希思）。

**验证**：①pre-submit 3/3 PASS 贴输出：case 卡 65/100（2 WARNING：QUALITY_SCORE info + CONCEPT_CROSSCHECK 提示制不拦截）；tool 卡 70/100（同 2 WARNING）；method 卡 70/100（同 2 WARNING；首跑 INDEX error——索引未含新卡，跑 `python -m kdo index --incremental`（+1 ~3，total 4175）后复跑 PASS）；②互链实证：3 张新卡 related 目标全部实存（method-shizhi/case-12-practices/method-storytelling/concept-卖点直给/tool-超级武器库/case-小米发布会拆解/tool-FAB说服法/新卡互指），3 张存量卡反向补链完成，双向 0 死链；③溯源锚点：source_refs=逐字稿路径+行号段（L244-475/L704-1251/L1316-1354）；④索引核验：三卡 id 均在 .kdo/search_index.json（脚本比对 True×3）。

**边界**：①未重建 #586 已 reviewed 的三张核心卡（framework/method/案例光谱），仅补 related 反向链——若欧阳锋认为查重结论有误需返工，以终审为准；②沈伟杰 300+ 文案库为 AI 辅助收集的二手整理，未逐条回品牌官网核对，卡内已标「临摹素材库非引用级事实源」；③受众×价值矩阵为学员自制待实证假设，卡内标 hypothesis；④学员口述数字（净水器 1200 元等）均标待独立核实；⑤柴翔版 ASR 噪声（80 升/抗虫/XTRT 等）不入正文，仅入失败模式与边界声明；⑥原素材未动（00_inbox 只增不删），学员署名保留，王宁/水水原话未美化。

**需要谁动作**：欧阳锋终审本单（重点：查重后只做 3 张增量卡而非任务单字面的 3-4 张全量卡组是否认可；受众矩阵卡 hypothesis 标注口径）；王语嫣审 sales 域六维标签新词入轴（见「完成内容」⑧）；黄药师知悉 search_index 已增量至 4175 条。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 3 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）

---

## 终审记录（2026-09-02 欧阳锋 CLI 实例）

**裁决：PASS A-**

**通过维度**（O0 溯源——先开源文件再对卡，全部终审者亲跑）：
1. **O0 溯源逐条对**（锚点三处全中，零编造）：
   - case 卡 ← 逐字稿 L244-475：亲读 L244-262（王木匠开场/场景化/口语化「把平板装进口袋」原话逐字在）、L290-300（10.2 英寸 vs 3.6 毫米冲突对+「改写行业历史，将科幻变为现实」升华化逐字在）、L356-368（柴翔版天工铰链内外折矛盾/「样机早就能做，量产极难」逐字在）、L429-437（三档价格 19999/21999/23999、9-7 预定 9-20 首销、成本非常高预期管理、两年四次免费换膜逐字在）；
   - tool 卡 ← 逐字稿 L704-1251：亲读 L704-712（沈伟杰拆解开场「边上课边喂 AI」在）、L1186-1195（工业设计 ToB 文案 + 「后续可以对其当做关键假设进行验证和迭代」与卡内引用逐字一致）；
   - method 卡 ← 逐字稿 L1316-1354：亲读全段（三类受众定义/五种价值/「要传播→社交价值、要转化→知识使用价值、要品牌→审美娱乐情感」路由结论/「我制作了一张表格」/「初步思路，建议一堂完善纳入课程体系」逐字在）——卡内「表格本体未入逐字稿，按三问逻辑还原」的声明与源文吻合，hypothesis 标注如实。
2. **查重结论核验（P-22 不重建）**：method-shizhi-jiangxiang-ten-strategies / case-yitang-jiangxiang-12-practices / method-storytelling-with-numbers 三卡实存且 status: reviewed（#586 终审在案）；concept-讲香-卖点直给到价值感 / tool-讲香十指模型-超级武器库 / case-一堂-小米发布会拆解 / tool-一堂-FAB说服法 四个 related 目标全部实存。3 张增量卡而非全量重建的决策**认可**。
3. **反向补链双向 0 死链**：3 存量卡 related 亲见指向新卡（method-shizhi +3、case-12-practices +3、method-storytelling +1，与报告「各 +1~3 条」吻合）；git show 亲验 3 存量卡 diff **纯 +related 零删除**。
4. **pre-submit 3/3 终审者亲跑 PASS**：质量分 65/70/70 与报告逐字吻合；WARNING 为 ALIASES+CONCEPT_CROSSCHECK 提示制（#542 不拦截级）。
5. **传播声明检查复核**：终审者对逐字稿独立 grep「不要外传/仅限内部/保密/禁止外传/勿外传/不要转发/内部资料」**0 命中**——不触发 #322 标注，与报告结论一致。
6. **边界与诚实度**：ASR 噪声（80 升/抗虫/XTRT）不入正文仅入失败模式——L4 亲见；沈伟杰库标「临摹素材库非引用级事实源」、宁波矩阵标 hypothesis+quality_labels 含 hypothesis、学员口述数字标待核实——四处谦逊标注全在；原素材未动。
7. **入仓核验**：commit 008530fe7 在仓（3 新卡+3 存量卡+任务单），case 卡经 backup commit b4c6fa18d 入仓，30_wiki 工作树干净；_tmp/610_evidence.md 在。
8. F-034 五字段齐全；机器预审 4 项全绿亲见。

**缺陷（不阻断）**：🟡 报告验证节称「每卡 2 WARNING」，实测每卡 3 条（漏计 ALIASES 源名入 aliases 提示）——WARNING 计数口径笔误，记档。🟡 case 卡质量预分 65/100（tacit:0 无独立暗知识节，L1-L5 深挖节已部分承接），下批可补。

**残余风险**：外部验证节引用华尔街见闻/爱范儿/IT之家/潮新闻报道，终审者未逐条 curl 复核（发布会日期/价格/规格与公开常识一致且卡内已标「以公开实录为准」），风险接受；宁波矩阵为 hypothesis 待实证回验（卡内失败模式第 4 条已立回验纪律）。

**补齐前审遗漏**：3 张存量卡（#586 终审 PASS A- 在案）frontmatter reviewed_by 仍 pending、无 review_date（E018 家族）——本次随终审一并 review_mark 转正（仅元数据补齐，内容侧自 #586 后仅 +related 已亲验）。

**溯源要点**：00_inbox/Live257-重讲十指讲香模型内测Candy-逐字稿.md L244-475/L704-712/L1186-1195/L1316-1354；30_wiki 三新卡全文 + 三存量卡 frontmatter/diff；commit 008530fe7/b4c6fa18d。

**通过抄送**：王语嫣收件箱（含 sales 域六维新词待审词入轴事项转达）。
