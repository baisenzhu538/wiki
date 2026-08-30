---
id: 582
task_id: task_20260831_laowantong-arui-science-sales-cards
assignee: laowantong
status: reviewed
created_at: 2026-08-31
created_by: 王语嫣
trigger: 老朱 08-31 直令（「把她排前3的内容拔下来逐字稿，拉起自动化工作流干活」）
priority: P1
instance: laowantong
updated_at: '2026-08-30T18:37:20.438131+00:00'
reviewed_by: 欧阳锋
review_date: '2026-08-30'
grade: A-
---

# 任务单 #582：阿蕊科学销售体系——前排内容产卡（老顽童）

## 背景

老朱 08-31 直令：对「阿蕊科学销售AI体系」公众号做深度调研，把排前 3 的内容拔下来，拉起自动化工作流产卡。王语嫣已完成调研+全文抓取（非逐字稿，是公众号正文——她没有语音口述稿，正文即最完整内容形态），素材已落 `00_inbox/私董会/阿蕊科学销售/articles/`。

## 素材（已到位，4 篇阿蕊亲笔）

| # | 文件 | 标题 | 字数 | 核心内容 |
|---|---|---|---|---|
| 1 | `_arui_art_2.md` | AI用不好？90%的人卡在了打开对话框之前（三步拆解法+两案例） | 3910 | **AI三大基本功之场景拆解**：切业务线→拉时间轴→找关键点；两案例（猎头/剪辑师）；「AI是杠杆业务拆解是支点」 |
| 2 | `_arui_art_0.md` | Agent设计必读：两个案例教你精准拆解业务场景 | 2701 | 同方法论姊妹篇：三步拆解+Agent 设计落点（策略顾问/人才甄别/寻访执行三 Agent 分工） |
| 3 | `_arui_art_1.md` | 销售AI派 Agent 工具矩阵（平台介绍文） | 932 | 20+ Agent 工具库/零代码搭建器/企业知识管理——竞品平台情报 |
| 4 | `_arui_art_3.md` | 姊妹篇(上)：客户说"再考虑一下"怎么办 | 3935 | 销售基本功：客户决策成本三招 |

## 体系全景（供产卡定位，来自 art_2 尾部自述）

- **销售三大基本功**：用户分层、卖点提炼、过程拆解
- **AI三大基本功**：场景拆解、提示词逻辑设计、分析校正
- 六块基本功 → 系统提示词 → 封装 Agent

## 任务（老顽童）

1. 产 **框架卡 1 张**：阿蕊「AI落地六块基本功」体系总览（销售三基本×AI三基本双层结构），discoverable_by 别名：科学销售/阿蕊/业务场景拆解/销售AI落地
2. 产 **方法卡 1 张**：「业务场景三步拆解法」（切业务线/拉时间轴/找关键点，含两案例+判断标准「界限拆不开=不同业务线」+三层颗粒度：里程碑→关键阶段→关键动作）
3. 产 **case 卡 1 张**：猎头案例（AI 角色随业务阶段切换：验证期=专家参谋建认知 / 增长期=提效工具优化瓶颈环节——这是文章最深的暗知识）
4. 产 **情报卡 1 张**：销售AIπ 平台（20+ Agent 工具矩阵/零代码搭建——KDO 可对标的外部竞品结构）

## 边界

- 素材源=公众号正文（已征得老朱认可形态），标注「无口述稿，正文直采」
- 4 篇为同一体系交叉引用，卡片互链，总链框架卡
- 阿蕊训练营招募信息不进卡片（营销内容滤除）
- 老朱业务关联：医保终端/健康小屋销售线可用「销售三大基本功」对照——在卡内 transferable_to 标注，不展开
- ⛔ #581 私董会挂起件不在本单范围

## 验证

- 每卡 frontmatter 含 source_refs 指向 articles/ 4 文件
- 框架卡 discoverable_by 含「科学销售」「业务场景拆解」
- 欧阳锋终审
## 执行报告（老顽童 2026-08-31）

**文件清单**
- 30_wiki/frameworks/framework-arui-ai-six-fundamentals.md（新增，框架卡：AI落地六块基本功双层体系，含与一堂五步法桥接）
- 30_wiki/methods/method-arui-business-scenario-3step-decomposition.md（新增，方法卡：三步拆解法+三层颗粒度+判断标准）
- 30_wiki/cases/case-arui-headhunter-ai-role-switching.md（新增，case卡：猎头案例+AI角色随阶段切换暗知识+三Agent分工）
- 30_wiki/entities/entity-销售AIπ平台.md（新增，情报卡：竞品平台四件套+KDO对标价值，trust_level=low标注自述信源）

**完成内容**
按任务单产4卡落30_wiki，四卡互链总链框架卡；frontmatter均含source_refs指向articles/4文件（check-source-refs实测9条引用0缺失0污染）；框架卡discoverable_by含「科学销售」「业务场景拆解」；训练营招募等营销内容滤除（框架卡Critique节保留「已滤除」元记录一句）；全文件CRLF；库存量核查确认30_wiki无同源卡（grep「阿蕊/科学销售/场景拆解」命中均为一堂系及他人名卡，非本素材）。

**验证**
python 90_control/scripts/check-source-refs.py --card <四卡id> 逐卡跑：4/2/2/1条source全命中，❌0 ⚠️0；自检脚本核验4卡CRLF成立、wikilink无死链、frontmatter必备字段齐全、素材4文件存在；营销词扫描仅Critique元记录命中。

**未做项**
kdo lint 全库跑完（约9分钟，exit 1）：1925 errors/2557 warnings 全部为存量问题（业务公式系source_refs行号锚、domain/tags不一致等），grep确认本批4卡0条lint报错；「分析校正」「提示词逻辑设计」两块基本功素材未展开（源文连载未写到，框架卡已标注confidence 0.85随连载补全）；销售AIπ平台未实测（情报卡Action Triggers留回填位）；域索引卡未建（任务单未要求，sales域已有sales-domain-digest入口）。

**需要谁动作**
欧阳锋终审4卡；若lint后台结果有本批卡相关报错由我返工。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

⚪ 无路径级交付物声明（纯文档/诊断类或未用反引号标注路径）——差集无检查面
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（缺失）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）

## 执行报告（2026-08-31 老顽童）

**交付物**（4 卡全产出，02:16-02:17 会话遗留已完成，本会话核验后提审）：
- `30_wiki/frameworks/framework-arui-ai-six-fundamentals.md`（框架卡：销售三基本×AI三基本双层体系，131 行）
- `30_wiki/methods/method-arui-business-scenario-3step-decomposition.md`（方法卡：切业务线/拉时间轴/找关键点+三层颗粒度，120 行）
- `30_wiki/cases/case-arui-headhunter-ai-role-switching.md`（case 卡：猎头 AI 角色两阶段切换暗知识，108 行）
- `30_wiki/entities/entity-销售AIπ平台.md`（情报卡：salesaipai.com 竞品结构，103 行）
- `60_feedback/adversarial/atk_arui-science-sales_20260831.md`（自攻击报告：0🔴/0🟡/4🟢）

**验证**：`kdo pre-submit` 4 卡 → ✅ PASS（10 WARNING 均检查器口径级）；训练营营销内容 4 卡 0 命中（滤除彻底）；「拆不到第三层问题永远藏在黑盒里」溯源 art_2 L50 逐字一致；frontmatter 五字段+related 互链全在位（method 卡 7 条跨域）；transferable_to 场景标注落实在情报卡 Action Triggers（医保终端/健康小屋销售线对照）。

**边界**：源文为公众号正文（无口述稿，任务单已认可形态）；AI三大基本功仅场景拆解一块完整展开，框架卡按"半成品框架"入库（confidence 0.85，Critique 已注明动机偏差风险）；entity 卡未实测（trust_level: low，Action Triggers 已留实测回填口）。

**需要谁动作**：欧阳锋终审 #582。

## 终审记录（欧阳锋 2026-08-31）

**结论：PASS A-**

**审查方式**：实卡 4 张全文读 + 素材锚点独立抽验 + check-source-refs / pre-submit 独立复跑 + 撞车面全库扫描（审而不改，未动任何卡片）。

**逐项核查**
1. 溯源零编造：锚点抽验 5 组全命中——「拆不到第三层问题永远藏在黑盒里」art_2 L50 逐字；三步动作 art_2 L18-20；猎头案例安安原话 art_0 L13-30（提示词原文 L30 逐字）；「验证期=专家参谋/增长期=提效工具」art_2 L102-103（同学A/同学B 称谓与卡内注释一致）；AIπ平台四件套 art_1 L15-47。check-source-refs 独立复跑：framework 4/4、method 2/2、case 2/2、entity 1/1，❌0 ⚠️0，与执行报告自报一致。
2. 一卡一事：框架=双层体系总览 / 方法=三步拆解+三层颗粒度 / case=猎头AI角色随阶段切换 / entity=竞品平台情报，四卡无内容重叠，互链总链框架卡成立。
3. 营销滤除：4 卡全库扫描「训练营/招募/报名/优惠」等营销词，唯一命中=框架卡 Critique「已滤除」元记录一句，合规。
4. 撞车核查：30_wiki 引用 _arui_art 素材的仅本批 4 卡自身，无历史同源卡。指派指令所称「#575-579 阿蕊逐字稿族卡」查证为误记——#575-579 实为战略笃定篇（OpenClaw选型/工具对比/KDO三件套/dk复刻/战略笃定），与本批无涉；真实撞车面对象=一堂五步法（李蕊，framework-yitang-scientific-sales-five-step），本批框架卡 §四已显式桥接（前三步同构+第二层分岔差异），方法卡/实体卡亦挂 related 区分——交叉印证非撞车，处置正确。
5. related 死链：4 卡 22 条 related 目标逐一 grep，0 死链。
6. 独立验证复跑：kdo pre-submit 4 卡 ✅ PASS（10 条 WARNING 与生产者自报口径一致）；#546 终审权校验过（register ouyangfeng 后流转）。
7. 诚实度：entity 卡 trust_level=low+「10倍为宣传口径未验证」、框架卡 confidence 0.85+「半成品框架随连载补全」、执行报告「未做项」如实列 5 项（含 lint 存量剥离声明）——质量声明可信。

**存在性核查**（#433 负向判词证据层，2026-08-31 实跑）
- 「30_wiki 无 _arui_art 同源历史卡」：`grep -rl '_arui_art' 30_wiki/` → 命中 4 文件=本批 case/entity/framework/method 自身，0 张他卡。
- 「#575-579 非阿蕊族卡」：production-queue.md #575-579 行描述实读——OpenClaw选型/工具Feature对比/KDO三件套/dk复刻4卡/战略笃定框架，全部战略笃定篇，0 张涉阿蕊素材。
- 「营销词滤除」：`grep -n '训练营|招募|报名|课程价|学员价|扫码|优惠'` 4 卡 → 唯一命中=框架卡 L120 Critique「已滤除」元记录。
- 「related 0 死链」：22 条 wikilink 目标逐一 `grep -rl "id: <target>$" 30_wiki` → 0 条死链。

**扣分点（-0.5 → A- 非 A）**
- 🟡 case 卡缺定位声明（pre-submit POSITION_DECLARATION 明示「body has no positioning declaration」未补）；
- 🟡 entity/case 卡 aliases 未含「阿蕊科学销售」路径段词（pre-submit SOURCE_NAMES 提示在列，可发现性降档）；
- 🟡 框架卡 quality pre-score 50/100 偏低（pos/tacit 段缺）。

**修复项**（不阻塞 PASS，落点=归老顽童下次触碰本批卡时顺手批 TODO，不另立项）：三卡补定位声明一行；entity/case aliases 补 1-2 词；框架卡 pos/tacit 段。

**观察项**：pre-submit CONCEPT_CROSSCHECK 4 卡提示与既有概念对账（一堂五步法/AI基本功等）——#542 提示制不拦截，建议老顽童下次触碰本批卡时顺手人工核对权威定义一致性。

终审流程：queue_transition review --verdict pass --grade A-（2026-08-31 欧阳锋）。
