---

id: tool-lean-cut-features
title: 太复杂就砍功能
type: tool
status: enriched
author: 老顽童
reviewed_by: 待审
confidence: 0.85
trust_level: medium
language: zh-CN
domain:
  - strategy
  - yitang
  - product
source_refs:
- 00_inbox/精益创业/一堂DOC-20260622212421_ocr_text.md
- 00_inbox/精益创业/一堂DOC-20260622212421_vlm_desc.md
related:
  - [[tool-lean-leverage-traffic]]
  - [[tool-lean-presell]]
  - [[tool-lean-minimum-version]]
  - [[tool-lean-fake-product]]
  - [[tool-lean-minimum-test-volume]]
  - [[framework-lean-false-model]]
  - [[framework-lean-four-principles]]
  - [[framework-lean-six-wastes]]
  - [[yt-entrepreneur-lean-validation]]
  - [[yt-entrepreneur-key-hypotheses]]
  - [[tool-泛产品落地-低成本测试MVP]]
  - [[concept-一堂-kernel-validation]]
  - [[case-lean-electric-scooter-mvp]]
---
# 太复杂就砍功能

> 用“砍掉非必要模块”替代“把第一版做完整”，让最小版本只承载最高风险假设的验证，而不是承载团队对“完美产品”的所有想象。

## 一句话定义

**太复杂就砍功能**是 MVP 范围控制工具，它验证的核心假设是：在保留产品内核价值的前提下，去掉哪些功能、模块或装饰后，目标用户仍然愿意完成那个最关键的行为（使用、付费、留存或推荐）。

## Purpose

- src_unknown
- src_unknown
- src_unknown

## 操作步骤

### 第一步：锁定当前唯一要验证的假设

- src_unknown
- src_unknown
- src_unknown

### 第二步：列出当前计划中的所有模块

把产品、门店、课程、服务或官网计划拆成独立模块，例如：

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

### 第三步：用“砍掉后是否影响关键假设”做减法

对每个模块问三个问题：

1. 砍掉它，用户还能完成那个最关键行为吗？
2. 保留它，能直接产生验证该假设所需的数据吗？
3. 延后到下一版，会让当前验证失效吗？

如果三个问题的答案都是“否”，这个模块就应该进入“延后清单”。

### 第四步：对照典型可砍模块清单快速自检

一堂讲义中列出了 6 类初版常见可砍模块 [conf=0.90, source=一堂DOC-20260622212421_ocr_text.md]：

| 可砍模块 | 典型场景 | 为什么可以延后 |
|:---|:---|:---|
| 只开发一半，要求团队砍掉 50% | 软件/硬件/服务第一版 | 把资源集中到验证核心假设的 1-2 个功能上 [conf=0.85, source=一堂DOC-20260622212421_ocr_text.md] |
| 成长体系（等级/勋章/积分） | App、社群、游戏化产品 | 属于留存放大手段，不是需求验证必需 |
| 多账号/第三方平台登录 | SaaS、工具类产品 | 手机号/邮箱注册即可验证核心行为 |
| 专业全套视觉 VI | 几乎所有早期产品 | 品牌识别可在验证后迭代，不决定需求是否存在 |
| 公司精美官网 | SaaS、消费品牌 | 落地页/海报即可承载早期验证 |
| 精装修门店/展台 | 餐饮、零售、本地生活 | 简装/快闪/摆摊即可验证选址与客群 |

### 第五步：冻结范围并发布

- src_unknown
- src_unknown
- src_unknown

## 成本 / 周期 / 样本量

| 维度 | 经验参考 | 说明 |
|:---|:---|:---|
| 范围裁剪会议 | 0.5-1 天 | 用一堂 6 类可砍模块清单做团队对齐 [conf=0.75, source=一堂DOC-20260622212421_ocr_text.md] |
| 重新排期后的最小版本 | 1 天到 4 周 | 海报/落地页 1-3 天；最小功能集 2-4 周；快闪店 1-2 周 [conf=0.70, source=讲师案例推演] |
| 成本降幅 | 常见 50%-80% | 砍掉 VI、官网、成长体系、精装修后，早期投入可显著下降 [conf=0.65, source=讲师经验判断] |
| 建议样本量 | 6-30 个真实用户 | 定性验证 6-10 人；定量验证至少 30 人或达到可区分信号 [conf=0.65, source=一堂课程经验判断] |

> 以上数字为经验区间，具体受产品形态、获客渠道、客单价和团队执行力影响，不应作为刚性标准。

## 适用边界

### 最适合

- src_unknown
- src_unknown
- src_unknown

### 需要调整

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## When NOT to Use

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 失败模式

| 失败模式 | 典型症状 | 修复方式 |
|:---|:---|:---|
| **把核心功能也砍掉** | 用户无法完成基本任务，最小版本变成“残缺版” | 回归产品内核，确保保留的功能能独立交付完整价值 [conf=0.85, source=concept-一堂-kernel-validation.md] |
| **为了砍而砍，没有假设** | 团队争论“砍哪个功能”，但说不清当前要验证什么 | 先完成关键假设排序，再拿假设当裁剪标尺 |
| **用砍功能无限拖延发布** | 每次都说“再砍掉一点就能上线”，却迟迟不面对用户 | 设定硬截止和对外发布日，截止后只修阻塞性 bug |
| **砍掉合规/安全/信任模块** | 在监管敏感或品牌敏感领域过度简化，触发法律或信任风险 | 把法规要求和客户关键决策链需求列为“不可砍”清单 |
| **砍掉后不看数据** | 发布最小版本后只看用户口头好评，不追踪关键行为 | 为每个保留功能绑定 1-2 个可观测指标 |

## 案例映射

### 正例：共享电动滑板车 A/B/C/D 四级验证

在 [[case-lean-electric-scooter-mvp]] 中，A 版计划同时包含自研滑板车、用户端 APP、礼券/会员营销功能，周期 6-12 个月、成本 200-300 万元；D 版则只保留“一张海报/落地页”来验证“中国用户是否对电动滑板出行感兴趣” [conf=0.70, source=讲师推演案例]。

- src_unknown
- src_unknown

### 反例：过早细化的连锁餐厅

在 [[framework-lean-six-wastes]] 覆盖的“过早细化”案例中，部分创业者在验证菜单和选址前就先装修门店、设计全套 VI、搭建会员系统，最终发现用户需求与假设不符时，沉没成本已经很高 [conf=0.70, source=讲师案例]。

- src_unknown
- src_unknown

## Critique

### 内部限制

1. **清单化风险**：一堂的 6 类可砍模块来自高频早期产品经验，但不是所有业务都适用；机械照搬可能把不该砍的模块砍掉 [conf=0.80, source=一堂DOC-20260622212421_ocr_text.md]。
2. **组织阻力**：“砍 50%”对团队心理冲击大，容易在执行中妥协为“砍 10%”，失去范围收敛效果。
3. **信号延迟**：过度简化可能导致用户体验失真，把“方向对但体验差”误判为“方向错”，需要在定性访谈中补全上下文。

### 外部攻击

**Eric Ries**

Ries 在《精益创业》中强调 MVP 的目的是“用最小成本完成一次 Build-Measure-Learn 循环”。砍功能是实现 MVP 的手段之一，但如果团队把“砍功能”本身当成目标，而忘了循环的测量与学习环节，就会陷入“为了小而小”的局部优化 [conf=0.85, source=Eric Ries《精益创业》]。

**Kent Beck**

Beck 的警告同样适用于砍功能：为了速度砍掉测试、监控、安全模块，可能让实验代码直接变成产品基础，留下长期技术债务。砍功能不应等于砍质量底线 [conf=0.80, source=yt-entrepreneur-lean-validation.md Critique 章节]。

---

*老顽童 · 2026-06-23 · 源：一堂精益创业 FALSE 模型讲义*
