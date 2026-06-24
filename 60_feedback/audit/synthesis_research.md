> 王语嫣对 research 域 40 张 case 卡的跨案例合成报告。
> 来源：`60_feedback/audit/synthesis_research_raw.md`
> 下一步：老顽童据此产出 `dk-research-synthesis-*` 暗知识卡。

---

## 0. 元信息

| 字段 | 内容 |
|:-----|:-----|
| 域 | research |
| 扫描 case 数 | 40 |
| 合成洞察数 | 3 |
| 合成日期 | 2026-06-25 |
| 合成者 | 王语嫣 |

---

## 洞察 1：高价值信息往往藏在“非正式/非公开身份”里，需要沉浸式角色扮演

### 模式描述

真正决定判断质量的信息（养老院真实运营、抖音团长衰退、竞品真实报价、工厂心理价位）往往不在公开渠道或高管访谈中，而在一线员工、家属群、保安、评论区、朋友圈等“低门槛但高信息密度”的场景里。

获取这些信息的关键不是更贵的数据库，而是设计一个合法、可信的“身份”，让自己进入目标信息流。案例中的“假装订货”“假扮家属”“假扮面试”“潜入微信群”都是同一原理的不同形态。

### 支撑案例（≥3）

| 案例 ID | 伪装身份 | 获取的关键信息 |
|:---|:---|:---|
| `case-yitang-competitor-pricing-intelligence` | 采购方 | 竞品真实报价、折扣结构、账期 |
| `case-yitang-mahjong-machine-fake-order` | 大客户 | 麻将机真实批发价和出货量 |
| `case-yitang-supplier-security-guard` | 闲聊者 | 工厂真实心理价位 |
| `case-yitang-elderly-home-roleplay` | 家属 | 养老院真实入住率和满意度 |
| `case-yitang-fake-interview-intelligence` | 面试者 | 行业红利退潮信号 |
| `case-zhanglan-amusement-park-undercover` | 店长 | 游乐园真实运营数据 |
| `case-zhanglei-nursing-home-family` | 家属 | 养老院真实服务与口碑 |

### 框架未覆盖的理由

- `tool-yitang-social-engineering-research`、`tool-yitang-field-research`、`tool-yitang-job-intelligence-research` 已覆盖部分方法；
- 但现有框架缺少：
  - 身份设计的 checklist（选什么身份、为什么可信、如何进入场景）；
  - 伦理与法律边界（哪些身份伪装可接受、哪些不可）；
  - 退出策略（如何在不暴露真实意图的情况下退出场景）。

### 建议沉淀为 dk 卡

`dk-research-identity-craft-for-closed-information`：为获取封闭情报设计合法沉浸式身份。

---

## 洞察 2：单一信息源极易被误导，必须依赖“行为痕迹 + 多源交叉验证”

### 模式描述

无论是用户自述、专家访谈还是行业报告，单一来源都可能失真。案例反复通过小票/订单号、现场观察、多身份访谈、线上社群 + 线下体验的组合，把“说的话”和“做的事”对照起来。

高质量研究的核心不是样本量，而是不同来源之间的三角验证。但案例也暴露了一个实践难题：研究者不知道什么时候该增加一个验证源、什么时候可以停止。

### 支撑案例（≥3）

| 案例 ID | 信息源组合 | 验证方式 |
|:---|:---|:---|
| `case-yitang-travel-receipt-analysis` | 收据/订单号 | 从自增订单号推算总订单量 |
| `case-yitang-luckin-field-research` | 小票 + 现场观察 + 财报 | 25000 多张小票交叉验证 |
| `case-liutao-douyin-team-leader-9m` | 加盟商/亏钱同行/面试者/客户 | 多身份多角度拼图 |
| `case-yitang-hardware-factory-photo` | 朋友圈照片 + 供应链访谈 | 从照片铭牌找到代工厂 |
| `case-yitang-pet-fostering-user-research` | 观察替代方案 + 用户访谈 | 行为比语言更诚实 |

### 框架未覆盖的理由

- `tool-yitang-reverse-data-analysis`、`dk-yitang-research-cross-validation-cost`、`framework-yitang-high-level-execution` 提供方法；
- 但缺少一个统一的“验证成本-置信度”决策表，帮助研究者判断：
  - 当前置信度是否足以支撑决策；
  - 增加一个验证源的边际成本与边际收益；
  - 什么情况下可以停止验证。

### 建议沉淀为 dk 卡

`dk-research-triangulation-stop-rule`：多源交叉验证的停止规则与成本-置信度权衡。

---

## 洞察 3：研究必须先服务决策，错误的研究顺序会放大资源浪费

### 模式描述

多个案例强调“先画像再访谈”“先假设链再验证”“先筛国家再实地考察”“先开实验店再扩张”。研究的效率取决于问题与决策的匹配度，而不是研究本身的精致程度。

研究活动的排序错误（如样本量 > 样本对、规模化 > 验证、报告阅读 > 假设验证）往往比研究技术错误代价更大。一个精致的错误研究，比一个粗糙的正确研究更危险。

### 支撑案例（≥3）

| 案例 ID | 研究顺序错误 | 正确顺序 |
|:---|:---|:---|
| `case-yitang-mvp-reward-interview-waste` | MVP 阶段未做画像就花钱访谈 | 先画像，再访谈对的人 |
| `case-一堂-无人餐厅-hypothesis-failure` | all in 前未验证关键假设 | 先验证需求/单元模型 |
| `case-一堂-陈贤敏汉堡-hypothesis-validation` | 本可开 3 家店，选择先开实验店 | 先验证关键假设 |
| `case-yitang-senior-university-product-design` | 直接问“老年大学怎么做” | 用假设链逐层验证 |
| `case-xian-franchise-location-decision` | 未做前置筛选就实地考察 | 先筛国家/城市/商圈 |
| `case-liutao-electric-bike-localization` | 未验证本地化假设就投入 | 先验证关键假设 |

### 框架未覆盖的理由

- `concept-一堂-hypothesis-driven-business-methodology`、`dk-yitang-research-question-quality`、`yt-lean-assumption-verification-3means` 已提供思路；
- 但缺少“研究决策映射表”——把每个研究动作对应到：
  - 具体决策；
  - 前置假设；
  - 通过/不通过标准；
  - 下一步动作。

### 建议沉淀为 dk 卡

`dk-research-decision-first-mapping`：研究活动如何与决策、假设、通过标准对齐。

---

## 下一步行动

老顽童据此产出 3 张 dk 卡：

1. `dk-research-identity-craft-for-closed-information`
2. `dk-research-triangulation-stop-rule`
3. `dk-research-decision-first-mapping`

每张 dk 卡需包含：
- 一句话定义
- 模式描述（2-3 段）
- 3-5 个支撑案例（带 `[[case-xxx]]` 链接）
- 与现有 framework/tool 卡的关系（说明缺口）
- 预警信号（≥3 条）
- 可迁移场景

---

*王语嫣 · 2026-06-25*
