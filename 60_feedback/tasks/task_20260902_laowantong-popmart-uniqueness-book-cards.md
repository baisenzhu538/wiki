---
id: 596
task_id: task_20260902_laowantong-popmart-uniqueness-book-cards
title: 拆书会218《因为独特》卡组4张（泡泡玛特王宁长期主义经营）
status: in_progress
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-02
reviewer: ouyangfeng
source_refs:
- 00_inbox/泡泡玛特的拆解/拆书会第218期《因为独特》· 精华提炼.md
related_tasks:
- '#469'
- '#470'
instance: laowantong
updated_at: '2026-09-01T16:09:46.118201+00:00'
---

# 任务：拆书会218《因为独特》卡组 4 张

## 背景
- 素材：`00_inbox/泡泡玛特的拆解/拆书会第218期《因为独特》· 精华提炼.md`（李翔书，主角泡泡玛特王宁，10715B，段王爷 09-01 23:01 落 inbox 的精华提炼件）。
- 王语嫣入口诊断（09-02 00:02）：域归属=**strategy + 拆书会系列**；对照已有卡 `case-popmart-prospectus-pricing`（招股书 IP 毛利率）与 `tool-blind-box-mechanism`（盲盒机制）**不撞车**——本书增量在长期主义经营观层面。
- inbox 自动化流水线立项（0831/0901 老朱直令：高价值素材直接编排产卡，终审归欧阳锋）。

## 任务（4 卡候选，最终形态按 W6 三方法定夺）
1. **framework**：尊重时间尊重经营——长期主义经营观（该十年做成的事就十年/企业如树剪枝/逆风飞翔长肌肉）。
2. **method**：减宽加深——砍掉 80% 外采聚焦潮玩/每年仍控 100 个系列/七分饱理论（停售限量）。
3. **concept**：满足感×存在感——消费解决两件事（近视眼镜 vs 黑框眼镜）；peace/love/enjoy/celebrate 四词消费阶梯。
4. **dk 或 case**：品牌感官包裹感——盖住 logo 也认得/门店如教堂/唱片公司模式（餐厅唱歌的"周杰伦"录下来卖到全世界）。

## 验证
- 4 卡 pre-submit 全过；O0 溯源锚点用提炼件路径+行号（原句可锚）。
- related 与已有 2 卡互链双向 0 死链；新卡间互链。
- 欧阳锋终审。

## 边界
- **转述二等标注（#470 拆书会系列口径）**：素材为段王爷精华提炼件（转述层），拆书会口述原文不在库——source 标注提炼件路径并注明「转述二等：提炼件」。
- 原素材不动（00_inbox 只增不删）；不重复已有 2 卡内容只互链。
- 王宁原话引用保持原样不美化（金句段 L145-159 一等锚）。
- 素材文件头有重复标题行（段王爷已知 E003 摩擦已自修技能），不影响内容锚定。

## 需要谁动作
- 老顽童：按队列序施工（W6 三方法前置），完成后 queue_transition submit 提审。
- 欧阳锋：终审。

## 建模方案（L1 出牌，2026-09-02 老顽童）

三方法前置（charter §2.3 / W6）：①全网调研（动态饱和）②六层交叉验证 ③九层深挖——跑完才写卡，记录落「## 执行报告」。

组件出牌链（17 张牌抽 8）：
- [素材牌·牌2+牌3 先全文扫描/先口述稿]：提炼件 168 行全量精读（含金句段 L145-159 一等锚）；转述二等标注按 #470/#216 拆书会系列口径
- [边界牌·牌6 先查已有卡]：grep 实证存量 2 卡（case-popmart-prospectus-pricing=招股书毛利率 benchmark；tool-blind-box-mechanism=盲盒机制判断）——本批增量=长期主义经营观层，只互链不重复
- [边界牌·牌7 先对标准则]：WebSearch 国际对标（Porter 聚焦战略 / P&G 品牌剪枝 / Brakus 品牌体验 / Lindstrom 感官品牌），术语不冲突再命名
- [结构牌·牌9 先framework再concept]：卡1 framework=卡组总纲；卡2 method/卡3 concept/卡4 case=解压层
- [过程牌·L8 子卡先定位]：卡2/3/4 首行声明归属卡组、指回总纲
- [过程牌·牌5 先判归属]：domain=strategy（domain-mapping 枚举内）；拆书会=来源进 source_context/aliases/tags 不进 domain（#531 W10+「来源不当域」纪律）
- [质量牌·L3+L4 先深挖+pre-submit]：每卡失败模式自带症状+修复；pre-submit 逐卡跑全过

## 执行报告（2026-09-02 老顽童）

**完成内容**：拆书会218《因为独特》4 卡全部落库并通过 pre-submit（全 PASS）+自攻击（🔴0/🟡2：1 已修复 1 报裁定）+互链双向验证（0 死链）；三方法①检索通道故障按存疑口径处理已逐卡标注，②六层交叉验证与③九层深挖记录在各卡迭代日志。W6 三方法前置完成，组件出牌已落本单「建模方案」节。

**文件清单**（新增 4 卡）：
- 30_wiki/frameworks/framework-popmart-long-termism-operating-philosophy.md（总纲，type: framework）
- 30_wiki/tools/tool-popmart-narrow-and-deep.md（减宽加深，**任务单原拟 type: method，因 pre-submit 新卡白名单无 method 改落 tool**，判断法结构不变）
- 30_wiki/concepts/concept-satisfaction-vs-existence.md（满足感×存在感）
- 30_wiki/cases/case-popmart-brand-sensory-wrap.md（品牌感官包裹感）

互链改动（已有 2 卡 related 补反向链接，正文零改动）：
- 30_wiki/cases/case-popmart-prospectus-pricing.md
- 30_wiki/tools/tool-blind-box-mechanism.md

配套：60_feedback/adversarial/atk_20260902_popmart-uniqueness-cardset.md（自攻击报告）

**验证**（实测输出）：
- pre-submit 4 卡全 PASS：framework 65/100、tool 50/100、concept 50/100、case 50/100；各 1 条 CONCEPT_CROSSCHECK 提示制 WARNING（通用词撞他域权威卡，已人工核对语境不冲突：本组「放大器」=盲盒热销放大器非 AI 放大器、「护城河」=王宁原话引文、「判断力」=通用语境），明细见各卡运行输出，如实随单附上
- 互链双向：新卡→6 目标（卡组 3+已有 2+…）全部 OK-exist，unresolved-wikilinks: NONE；已有 2 卡→新卡反向链接已补
- 行数门禁：134/122/121/132 行，全部 ≥100
- 转述二等：4 卡 source_context 均按 #470/#216 口径标注「转述二等（原书一等，原书不在库）」，原话锚全部带提炼件行号（金句段 L145-159 已用）

**未做项/边界**：
- 三方法①全网调研未完成在线核实（web_search 三连超时+web_extract 拒抓+curl 不通，#586 同族故障）——国际对标（Porter 聚焦/P&G 剪枝/Brakus 品牌体验/魏布伦效应）用训练记忆内置并逐卡显式标注存疑，**建议检索通道恢复后补验**（补验责任：下批任一 popmart 卡任务顺带执行）
- 素材 §二.2「MOLLY 诞生（Sonny Angel 危机→自有 IP）」未入卡组（任务单只定 4 卡不越界）——自攻击 🟡 发现，**报欧阳锋裁定是否补卡（候选 case-popmart-molly-transition）**
- 原素材未动（00_inbox 只增不删）；卡组数字全部标「待核」（转述件自述）

**需要谁动作**：
- 欧阳锋：终审 4 卡；顺带裁定 MOLLY 诞生卡候选是否补立项
- 黄药师：新卡入库后跑 `kdo index --rebuild`（老顽童不自行跑）
