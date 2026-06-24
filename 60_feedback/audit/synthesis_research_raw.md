# 研究域案例交叉分析（原始素材）

> 生成时间：2026-06-24
> 分析范围：`C:/Users/Administrator/Desktop/wiki/30_wiki/cases/` 中 `domain` 包含 `research` 的 case 卡片，以及明确映射到研究/假设验证方法论的相关案例。
> 目的：为王语嫣提供可复审的原始模式分析，不做最终合成卡片。

---

## 一、扫描范围与方法

- 过滤条件：`type: case` + (`domain` 含 `research` / `id` 以 `case-research-` 开头 / 内容明显映射研究方法论)。
- 共扫描 **40** 张案例卡：38 张 `domain: [..., research]` 的研究案例 + 2 张虽未标 `research` 但直接映射 `yt-research-hypothesis-test` 的关键假设案例。
- 提取字段：id、title、一句话核心洞察、失败根因/警示、映射框架/工具、反直觉点。

---

## 二、案例清单（按研究类型分组）

### 用户/场景访谈与 JTBD

- **id**: `case-yitang-pet-fostering-user-research`  
  **title**: 案例：宠物寄养——观察现有替代方案  
  **核心洞察**: 理解用户的最佳方式不是问“你会用我的产品吗”，而是观察“你现在怎么解决这个问题”——行为比语言更诚实。  
  **失败根因/警示**: 跳过替代方案观察直接做产品。  
  **映射框架/工具**: tool-yitang-user-interview-5steps  
  **反直觉点**: 不急着做产品，先看用户在没有你产品时的真实替代方案。

- **id**: `case-yitang-doorstep-nail-service-context`  
  **title**: 案例：上门美甲——在用户真实场景中访谈  
  **核心洞察**: “魔鬼在现场”：在真实场景中观察+访谈的信息密度，远高于会议室访谈。  
  **失败根因/警示**: 在会议室/微信里做脱离场景的访谈。  
  **映射框架/工具**: tool-yitang-user-interview-5steps、dk-yitang-research-scale-vs-depth  
  **反直觉点**: 同一用户在不同场景下说出的需求可能完全相反。

- **id**: `case-yitang-doorstep-pet-feeding-trust`  
  **title**: 案例：上门宠物喂养——用调研解决信任障碍  
  **核心洞察**: 信任问题的解法往往不在本品类，而在相邻品类（家政/维修/月嫂）的最佳实践里。  
  **失败根因/警示**: 把需求验证和信任验证混为一谈。  
  **映射框架/工具**: tool-yitang-user-interview-5steps  
  **反直觉点**: 用户不是不需要服务，而是不知道怎么让一个陌生人进自己家。

- **id**: `case-yitang-homestay-reception-design`  
  **title**: 案例：民宿接待方案——用调研优化服务体验设计  
  **核心洞察**: 服务设计的调研重点是“看别人怎么做”+“听用户怎么骂”，二者相加才是改进清单。  
  **失败根因/警示**: 拍脑袋写 SOP。  
  **映射框架/工具**: tool-yitang-user-interview-5steps  
  **反直觉点**: 竞对的 SOP 和用户的差评同样重要。

- **id**: `case-yitang-voice-robot-companion-design`  
  **title**: 案例：陪伴式语音机器人——声音设计如何调研  
  **核心洞察**: 在新品类创新前，先调研旧品类（Siri/小爱/导航）的声音规律，人对声音的偏好有稳定模式。  
  **失败根因/警示**: 先做一版再测试，无参照地“创新”。  
  **映射框架/工具**: tool-yitang-user-interview-5steps  
  **反直觉点**: 语音产品虽新，但声音偏好规律不必重新发明。

- **id**: `case-yitang-ski-project-user-as-expert`  
  **title**: 案例：滑雪项目——把用户当专家访谈  
  **核心洞察**: 重度用户就是行业专家，他们对需求和替代方案的认知往往超过分析师。  
  **失败根因/警示**: 只访谈行业分析师或普通用户，忽视重度用户。  
  **映射框架/工具**: framework-yitang-expert-interview-10steps、tool-yitang-user-interview-5steps  
  **反直觉点**: 用户调研和专家访谈的边界在深度用户身上是模糊的。

- **id**: `case-yitang-jtbd-story-formula`  
  **title**: 案例：JTBD故事公式——从用户故事中提取需求  
  **核心洞察**: JTBD 故事公式强制用户回溯真实行为路径，一个完整故事抵得上 100 份问卷。  
  **失败根因/警示**: 直接问“你有什么需求”或只问观念。  
  **映射框架/工具**: tool-yitang-user-interview-5steps、yt-research-user-jtbd  
  **反直觉点**: 最有价值的信息是“我试过什么但不行”。

- **id**: `case-yitang-consumer-offline-channel-decision`  
  **title**: 案例：消费品线下渠道决策——先访谈再算账  
  **核心洞察**: 渠道决策不能只靠行业报告，必须先访谈一线从业者拿真实数据，再用单元模型计算。  
  **失败根因/警示**: 只看报告增长率，忽视进场费、账期、退货率。  
  **映射框架/工具**: tool-yitang-user-interview-5steps、tool-yitang-consumer-goods-research  
  **反直觉点**: 报告写增长率 15%，经销商说进场费半年涨了 30%。

- **id**: `case-yitang-mvp-reward-interview-waste`  
  **title**: 案例：MVP阶段花钱做用户访谈的浪费  
  **核心洞察**: 用户访谈质量不取决于花了多少钱或样本量，而取决于是否访谈了对的人。  
  **失败根因/警示**: MVP 阶段未做用户画像就花钱做正式访谈/焦点小组。  
  **映射框架/工具**: framework-yitang-expert-interview-10steps、concept-ceo-must-do-user-research  
  **反直觉点**: 花大钱可能买到错误人群的错误反馈。

### 竞品/供应链情报与社会工程

- **id**: `case-yitang-competitor-pricing-intelligence`  
  **title**: 案例：假装订货套取竞品真实价格  
  **核心洞察**: 供应链端是商业情报的“软肋”——竞品可以对对手保密，却很难对“潜在客户”保密。  
  **失败根因/警示**: 拿官网标价当真实价格。  
  **映射框架/工具**: tool-yitang-reverse-data-analysis、tool-yitang-social-engineering-research  
  **反直觉点**: 假装采购方不仅不会被防，还会拿到真实报价、折扣结构和账期。

- **id**: `case-yitang-mahjong-machine-fake-order`  
  **title**: 案例：假装订货套取麻将机竞品数据  
  **核心洞察**: “假装上下游角色”是获取竞品数据最高效的社会工程手段——你不是刺探者，而是“潜在大客户”。  
  **失败根因/警示**: 直接询问竞品价格/出货量。  
  **映射框架/工具**: tool-yitang-reverse-data-analysis、tool-yitang-social-engineering-research  
  **反直觉点**: 对方会主动展示最好的一面，把真实批发价和折扣结构交给你。

- **id**: `case-yitang-supplier-security-guard`  
  **title**: 案例：通过保安打听到工厂收购价  
  **核心洞察**: 供应链上任何“知道内情且愿意说”的人都可能掌握核心信息，不一定是高管。  
  **失败根因/警示**: 只找工人/管理层，忽视长期在场的外围角色。  
  **映射框架/工具**: tool-yitang-supply-chain-research、tool-yitang-field-research  
  **反直觉点**: 24 小时在场的保安竟是股东亲戚，知道老板真实心理价位。

- **id**: `case-yitang-hardware-factory-photo`  
  **title**: 案例：从朋友圈照片找到代工厂  
  **核心洞察**: 朋友圈照片的微小细节（工厂铭牌）可成为破解供应链的关键线索。  
  **失败根因/警示**: 被拒绝两次后就放弃。  
  **映射框架/工具**: tool-yitang-supply-chain-research、dk-yitang-digging-belief  
  **反直觉点**: 花 3 小时放大照片角落，省下几十万开模费。

- **id**: `case-zhanglei-furniture-overseas-market-selection`  
  **title**: 案例：张磊——洗衣液蹲超市+假扮促销员  
  **核心洞察**: 最原始的方法（蹲超市+假扮促销员）往往比报告更接近真实购买行为。  
  **失败根因/警示**: 依赖问卷或二手报告判断新品类需求。  
  **映射框架/工具**: tool-yitang-field-research、tool-yitang-social-engineering-research  
  **反直觉点**: 蹲在货架前看 2 小时，比看 20 份消费者报告更接近真相。

- **id**: `case-zhanglan-amusement-park-undercover`  
  **title**: 案例：张兰假扮游乐园店长卧底15天  
  **核心洞察**: 穿上工服、真正融入现场运营足够长时间，能拿到最不可篡改的一手信息。  
  **失败根因/警示**: “参观式调研”或短期观察。  
  **映射框架/工具**: tool-yitang-social-engineering-research、tool-yitang-field-research  
  **反直觉点**: 不需要高端方法，当 15 天服务员即可。

### 实地渗透与身份交叉验证

- **id**: `case-zhanglei-nursing-home-family`  
  **title**: 案例：假扮孙子调研养老院真实状况  
  **核心洞察**: 线上潜入家属群+线下假扮家属的双重渗透，可互为交叉验证。  
  **失败根因/警示**: 只看养老院宣传册/表面服务。  
  **映射框架/工具**: tool-yitang-social-engineering-research、tool-yitang-field-research  
  **反直觉点**: 在食堂吃饭、和其他家属聊天，能拿到宣传册永远不会写的内容。

- **id**: `case-yitang-elderly-home-roleplay`  
  **title**: 案例：假扮家属潜入养老院微信群  
  **核心洞察**: 最关键的信息往往在“外部不可见但信息密集”的场景里（家属微信群），需要合法融入。  
  **失败根因/警示**: 只看公开渠道和财务报表。  
  **映射框架/工具**: tool-yitang-social-engineering-research、tool-yitang-field-research  
  **反直觉点**: 假扮家属进群能拿到早期入住率爬坡曲线和真实满意度。

- **id**: `case-yitang-fake-interview-intelligence`  
  **title**: 案例：假扮面试发现行业红利退潮  
  **核心洞察**: 用“面试者”身份渗透到多家公司内部，可发现活下来的玩家不愿说的系统性衰退。  
  **失败根因/警示**: 只调研品牌方、头部公司、赚钱的同行。  
  **映射框架/工具**: tool-yitang-job-intelligence-research、tool-yitang-social-engineering-research  
  **反直觉点**: 面试一圈后发现红利期退潮，避免了大笔投资损失。

- **id**: `case-liutao-douyin-team-leader-9m`  
  **title**: 案例：刘涛——从信息碎片拼出抖音团长赛道真相  
  **核心洞察**: 同一问题用多个身份（加盟商/亏钱同行/面试者/客户）从不同角度交叉验证，才能拼出完整图景。  
  **失败根因/警示**: 相信单一来源或官方数据。  
  **映射框架/工具**: framework-yitang-high-level-execution、dk-yitang-digging-belief、tool-yitang-job-intelligence-research  
  **反直觉点**: 翻评论区、照片、朋友圈比高端工具更有效。

- **id**: `case-zhanglei-twist-egg-machine-yogurt-nursing`  
  **title**: 案例：张磊——扭蛋机+酸奶+养老院，调研先行的连续创业  
  **核心洞察**: 连续创业成功的关键不是经验，而是每次进入新品类都用调研把认知空白填上。  
  **失败根因/警示**: 凭过去经验跳过新领域调研。  
  **映射框架/工具**: framework-yitang-high-level-execution  
  **反直觉点**: 有经验的人反而更依赖调研，而不是跳过调研。

### 公开数据、反向数据与实地大样本

- **id**: `case-yitang-luckin-field-research`  
  **title**: 案例：瑞幸做空——实地调研的教科书  
  **核心洞察**: 实地调研不需要“聪明”，需要“狠”——愿意投入足够的时间和人力。  
  **失败根因/警示**: 想靠小聪明或小样本走捷径。  
  **映射框架/工具**: tool-yitang-field-research、framework-yitang-high-level-execution  
  **反直觉点**: 92 个全职+1400 多名兼职，收集 25000 多张小票，从财报中找出欺诈。

- **id**: `case-yitang-travel-receipt-analysis`  
  **title**: 案例：旅行公司收据分析——从单据反推真实数据  
  **核心洞察**: 订单号、收据、小票等不起眼的数字是不可篡改的交易记录，可反推真实经营数据。  
  **失败根因/警示**: 依赖财报/宣传数据。  
  **映射框架/工具**: tool-yitang-reverse-data-analysis、tool-yitang-field-research  
  **反直觉点**: 自增订单号可推算总订单量，小票拼起来比财报更真实。

### 行业报告、招股书与二手研究

- **id**: `case-doris-crossborder-ecommerce-opportunity`  
  **title**: 案例：跨境电商机会识别——从报告到行动  
  **核心洞察**: 跨境电商是数据最丰富的行业之一，问题不是数据不够，而是不知道去哪找、怎么用。  
  **失败根因/警示**: 品类/市场多而无目标地乱搜。  
  **映射框架/工具**: framework-doris-industry-report-4step  
  **反直觉点**: 海关有每一单的进出口数据。

- **id**: `case-doris-outbound-travel-community`  
  **title**: 案例：出境游产业链拆解  
  **核心洞察**: 一份好行业报告里的产业链图，价值可能超过报告其他部分的总和。  
  **失败根因/警示**: 通读报告不抓重点。  
  **映射框架/工具**: framework-doris-industry-report-4step  
  **反直觉点**: 一页图直接回答“谁赚什么钱”。

- **id**: `case-doris-catering-chain-benchmark`  
  **title**: 案例：餐饮连锁对标调研  
  **核心洞察**: 餐饮连锁上市公司招股书把单店模型、翻台率、扩张节奏写得清清楚楚，可直接当 benchmark。  
  **失败根因/警示**: 自己重新做实验。  
  **映射框架/工具**: framework-doris-industry-report-4step、tool-yitang-financial-report-intelligence  
  **反直觉点**: 别人的验证数据免费可得。

- **id**: `case-doris-grab-industry-cognition`  
  **title**: 案例：Doris 7天从零建立行业认知  
  **核心洞察**: 不需要先成为专家才能判断——用 5 个关键信息点 7 天内达到能和专家平等对话的水平。  
  **失败根因/警示**: 试图慢慢积累行业知识再下结论。  
  **映射框架/工具**: framework-doris-industry-report-4step、tool-doris-industry-report-search-tips  
  **反直觉点**: 28 页产业综述来自有限的初始关键词扩展。

- **id**: `case-doris-beauty-ecommerce-channel`  
  **title**: 案例：美妆行业渠道效率发现  
  **核心洞察**: 行业报告里有现成的渠道效率数据，咨询公司×平台联合报告通常是高质量来源。  
  **失败根因/警示**: 凭感觉选渠道。  
  **映射框架/工具**: framework-doris-industry-report-4step、tool-doris-industry-report-search-tips  
  **反直觉点**: 抖音/小红书转化效果来自贝恩×阿里妈妈联合报告。

- **id**: `case-doris-2014-music-streaming-prediction`  
  **title**: 案例：2014年预判音乐流媒体趋势  
  **核心洞察**: 权威行业报告+正确解读框架可支撑融资级商业判断，关键是读出“稳态 B”。  
  **失败根因/警示**: 只看报告本身，不读出不可逆趋势。  
  **映射框架/工具**: framework-doris-industry-report-4step  
  **反直觉点**: IFPI 报告提前多年预判流媒体成为主流。

- **id**: `case-popmart-prospectus-pricing`  
  **title**: 案例：泡泡玛特招股书——IP产品毛利率60-70%  
  **核心洞察**: 公开招股书是免费的 benchmark 报告，可判断自身定价/毛利是否合理。  
  **失败根因/警示**: 花钱找咨询公司做基础定价基准。  
  **映射框架/工具**: tool-yitang-financial-report-intelligence、tool-yitang-ipo-annual-report-cheat-sheet  
  **反直觉点**: 招股书里的毛利率可直接当定价基准。

- **id**: `case-neworiental-prospectus-marketing`  
  **title**: 案例：新东方招股书——营销渠道全览  
  **核心洞察**: 行业龙头的招股书等于已被大规模执行验证过的获客方法论。  
  **失败根因/警示**: 自己从零摸索获客渠道。  
  **映射框架/工具**: tool-yitang-financial-report-intelligence  
  **反直觉点**: 公开文件里包含经过验证的 6 种营销方式清单。

- **id**: `case-proya-betaine-skincare-benchmark`  
  **title**: 案例：贝泰妮招股书——敏感肌市场的完整画像  
  **核心洞察**: 一份招股书系统拆解后，等于免费拿到顶级咨询公司级别的行业分析报告。  
  **失败根因/警示**: 重复做已被披露的行业分析。  
  **映射框架/工具**: tool-yitang-financial-report-intelligence、tool-yitang-comparable-company-selection  
  **反直觉点**: 敏感肌人群占比、复购率、线上渠道占比全在招股书。

- **id**: `case-yitang-beauty-device-overseas-sales`  
  **title**: 案例：美容仪出海——用行业报告判断海外市场  
  **核心洞察**: 出海不需要每个市场都飞，先用行业报告筛选 2-3 个潜力国家，再实地验证。  
  **失败根因/警示**: 无差别实地考察所有潜在市场。  
  **映射框架/工具**: framework-doris-industry-report-4step、tool-yitang-overseas-research  
  **反直觉点**: 不出国门即可先筛掉大部分市场。

- **id**: `case-yitang-sanjieke-benchmark-failure`  
  **title**: 案例：对标三节课做C端，半年后发现对方已转型B端  
  **核心洞察**: 专家访谈得到的是“静态快照”，必须有时间戳意识：信息是何时产生的？现在是否仍然成立？  
  **失败根因/警示**: 把专家访谈的静态快照当长期真理。  
  **映射框架/工具**: framework-yitang-expert-interview-10steps、dk-yitang-expert-interview-5-traps  
  **反直觉点**: 三轮饭局打听到的内部模型，半年后完全失效。

### 假设驱动、赛道选择与系统性决策

- **id**: `case-yitang-track-selection-research`  
  **title**: 案例：一堂赛道选择——用调研方法论选创业方向  
  **核心洞察**: 用 OSL 五步法系统做赛道调研，既验证可行性也明确差异化定位。  
  **失败根因/警示**: 凭感觉或追风口选赛道。  
  **映射框架/工具**: framework-yitang-oscar-research、yt-research-osl-framework  
  **反直觉点**: 一堂自己就是调研方法论的最佳案例。

- **id**: `case-xian-franchise-location-decision`  
  **title**: 案例：西安加盟选址——系统调研vs拍脑袋  
  **核心洞察**: 异地加盟最大风险是用一线城市数据推断新一线城市，必须拿到目标城市真实数据。  
  **失败根因/警示**: “想当然”式调研只看样板店和官方材料。  
  **映射框架/工具**: tool-yitang-store-franchise-research、tool-yitang-field-research  
  **反直觉点**: 最该访谈的是已关店加盟商和商业地产中介。

- **id**: `case-yitang-senior-university-product-design`  
  **title**: 案例：老年大学——用假设链逐层验证赛道可行性  
  **核心洞察**: 不要直接回答“我能做吗”，把问题拆成依赖链逐层验证，L1 不成立则 L2/L3 不用看。  
  **失败根因/警示**: 跳过基础假设直接回答自身可行性。  
  **映射框架/工具**: tool-yitang-user-interview-5steps、dk-yitang-research-question-quality  
  **反直觉点**: “我能切入什么细分”在“有没有商业模式”未验证前不重要。

- **id**: `case-liutao-electric-bike-localization`  
  **title**: 案例：电动车出海本地化——从0调研目标市场  
  **核心洞察**: 出海的第一个决策不是“选哪个国家”，而是建立一套可重复的海外市场评估框架。  
  **失败根因/警示**: 靠单份报告下结论。  
  **映射框架/工具**: framework-yitang-high-level-execution、tool-yitang-overseas-research  
  **反直觉点**: 调研应成为可持续的认知基础设施，而非一次性行为。

- **id**: `case-yitang-ai-time-management-coach`  
  **title**: 案例：AI辅助调研——时间管理教练产品验证  
  **核心洞察**: AI 可把调研从 2 周压缩到 2-3 天，但前提是人已掌握调研方法论。  
  **失败根因/警示**: 让 AI 无方向地执行。  
  **映射框架/工具**: tool-yitang-ai-research-workflow、dk-yitang-ai-research-prompt-craft  
  **反直觉点**: 人机协作的瓶颈在人，不在 AI。

- **id**: `case-一堂-陈贤敏汉堡-hypothesis-validation`  
  **title**: 案例：陈贤敏中式汉堡先开实验店验证关键假设  
  **核心洞察**: 资源越充足，越应克制愿望思维，把资源变成验证关键假设的工具而非扩张赌注。  
  **失败根因/警示**: 跳过关键假设直接多店扩张。  
  **映射框架/工具**: concept-一堂-hypothesis-driven-business-methodology、yt-research-hypothesis-test、yt-entrepreneur-lean-validation  
  **反直觉点**: 有资本开 3 家店，却选择先开 1 家实验店。

- **id**: `case-一堂-无人餐厅-hypothesis-failure`  
  **title**: 案例：一堂无人餐厅项目因忽视关键假设而失败  
  **核心洞察**: 未验证“机器人经营价值/行业机会/单元模型”等前置假设就 all in，最终现金流烧光。  
  **失败根因/警示**: 把营销热度和美好愿望当成需求验证。  
  **映射框架/工具**: concept-一堂-hypothesis-driven-business-methodology、concept-一堂-key-assumptions、yt-lean-assumption-verification-3means  
  **反直觉点**: 有京东背书和大量媒体流量仍失败，机器人维护人力反而比传统餐厅还多。

---

## 三、跨案例反复出现的模式（原始分析）

### 模式 1：高价值信息往往藏在“非正式/非公开身份”里，需要沉浸式角色扮演才能获取

**描述**：大量案例显示，真正决定判断质量的信息（养老院真实运营、抖音团长衰退、竞品真实报价、工厂心理价位）并不在公开渠道或高管访谈中，而是在一线员工、家属群、保安、评论区、朋友圈等“低门槛但高信息密度”的场景里。获取这些信息的关键不是更贵的数据库，而是设计一个合法、可信的“身份”，让自己进入目标信息流。

**支持案例**：
- `case-zhanglei-nursing-home-family`
- `case-yitang-elderly-home-roleplay`
- `case-yitang-fake-interview-intelligence`
- `case-yitang-supplier-security-guard`
- `case-yitang-competitor-pricing-intelligence`
- `case-zhanglan-amusement-park-undercover`

**框架覆盖 vs 缺口**：tool-yitang-social-engineering-research、tool-yitang-field-research、tool-yitang-job-intelligence-research 已覆盖部分方法，但现有 UX/市场研究主流框架较少讨论“合法伪装身份”的伦理边界、身份设计清单和退出策略，存在实践指南缺口。

### 模式 2：单一信息源极易被误导，必须依赖“行为痕迹+多源交叉验证”

**描述**：无论是用户自述、专家访谈还是行业报告，单一来源都可能失真。案例反复通过小票/订单号、现场观察、多身份访谈、线上社群+线下体验的组合，把“说的话”和“做的事”对照起来。高质量研究的核心不是样本量，而是不同来源之间的三角验证。

**支持案例**：
- `case-yitang-travel-receipt-analysis`
- `case-yitang-luckin-field-research`
- `case-liutao-douyin-team-leader-9m`
- `case-yitang-hardware-factory-photo`
- `case-yitang-pet-fostering-user-research`

**框架覆盖 vs 缺口**：tool-yitang-reverse-data-analysis、dk-yitang-research-cross-validation-cost、framework-yitang-high-level-execution 提供方法，但缺少一个统一的“验证成本-置信度”决策表，帮助研究者判断何时该增加一个验证源、何时可以停止。

### 模式 3：用户“真实需求”更易在真实场景和完整行为故事中浮现，而非直接提问

**描述**：直接问“你要什么”会得到愿望清单或迎合式回答；JTBD 故事公式、现场观察、重度用户访谈则逼迫受访者回溯真实行为路径。案例中大量失败根因都是“在错误场景问错人”，而成功做法都强调观察替代方案、在真实环境中访谈、把重度用户当专家。

**支持案例**：
- `case-yitang-jtbd-story-formula`
- `case-yitang-doorstep-nail-service-context`
- `case-yitang-pet-fostering-user-research`
- `case-yitang-ski-project-user-as-expert`
- `case-yitang-consumer-offline-channel-decision`

**框架覆盖 vs 缺口**：tool-yitang-user-interview-5steps、yt-research-user-jtbd、framework-yitang-expert-interview-10steps 已覆盖。缺口在于“如何把线上/远程访谈还原到现场语境”以及“AI 辅助访谈时如何防止生成式诱导偏见”。

### 模式 4：二手数据（招股书/行业报告）可快速建立基准，但必须警惕“静态快照”和表面数据

**描述**：Doris 系列和招股书案例证明，行业报告、招股书、海关数据能以极低成本给出市场规模、渠道效率、单店模型、毛利率等基准。但“对标三节课”案例同时警告：专家访谈和招股书都是静态快照，半年后可能失效。研究者需要给每条二手信息打上时间戳，并用实地或一手数据验证关键假设。

**支持案例**：
- `case-popmart-prospectus-pricing`
- `case-proya-betaine-skincare-benchmark`
- `case-doris-catering-chain-benchmark`
- `case-doris-2014-music-streaming-prediction`
- `case-yitang-sanjieke-benchmark-failure`
- `case-yitang-beauty-device-overseas-sales`

**框架覆盖 vs 缺口**：framework-doris-industry-report-4step、tool-yitang-financial-report-intelligence 提供流程。缺口是“二手信息新鲜度评估表”和“从二手数据到可证伪假设的转化模板”，dk-yitang-research-source-freshness 有概念但缺操作化工具。

### 模式 5：研究必须先服务决策，错误的研究顺序会放大资源浪费

**描述**：多个案例强调“先画像再访谈”“先假设链再验证”“先筛国家再实地考察”“先开实验店再扩张”。MVP 访谈浪费、无人餐厅失败、老年大学假设链、西安选址三层法等共同指向：研究的效率取决于问题与决策的匹配度，而不是研究本身的精致程度。研究活动的排序错误（如样本量>样本对、规模化>验证）往往比研究技术错误代价更大。

**支持案例**：
- `case-yitang-mvp-reward-interview-waste`
- `case-一堂-无人餐厅-hypothesis-failure`
- `case-一堂-陈贤敏汉堡-hypothesis-validation`
- `case-yitang-senior-university-product-design`
- `case-xian-franchise-location-decision`
- `case-liutao-electric-bike-localization`

**框架覆盖 vs 缺口**：concept-一堂-hypothesis-driven-business-methodology、dk-yitang-research-question-quality、yt-lean-assumption-verification-3means 已提供思路。缺口是“研究决策映射表”——把每个研究动作对应到具体决策、前置假设和通过标准，避免为了研究而研究。

---

## 四、值得进一步追问的缺口

1. **伦理与合规边界**：社会工程/身份伪装方法在研究中极为有效，但现有卡片几乎未涉及合法性、隐私和退出机制。
2. **AI 辅助研究的质控**：`case-yitang-ai-time-management-coach` 提出效率提升，但缺少 AI 幻觉、数据污染和诱导偏见的系统校验方法。
3. **研究停止规则**：案例强调多源验证，但何时“够用了”？缺少基于决策风险的置信度/成本权衡工具。
4. **从研究到行动的转化**：大量案例停在“获得认知”，下一步如何转化为产品假设、MVP、单元模型验证，尚缺统一的工作流。
