---
id: task_20260627_laowantong-channel-growth-cards
type: production_task
created_at: 2026-06-27
author: 王语嫣
assignee: Hermes 老顽童
priority: P1
scope: 一堂五步法之增长（渠道增长域）卡片化生产
related:
  - '[[diag_20260627_wangyuyan-channel-growth-nine-layer]]'
---

# Hermes 老顽童生产任务：渠道增长域卡片化

> 王语嫣已完成九层深挖 + 六层交叉验证。
> 本指令仅写入 `60_feedback/`，不污染 `30_wiki/`。老顽童负责按此指令在 `30_wiki/` 生产卡片。

---

## 0. 元信息

| 项目 | 内容 |
|------|------|
| 任务类型 | 新建卡片 |
| 素材来源 | `00_inbox/一堂五步法之增长/`（59 图 + OCR + VLM + 3 组口述/笔记） |
| 优先级 | P1 |
| 质量负责人 | 王语嫣（CLI） |
| 生产方 | Hermes 老顽童 |
| 预计产出 | 16-17 张卡（含 2 张跨域桥接卡） |

---

## 1. 素材清单

| 主题组 | 核心文件 | 内容 |
|:---|:---|:---|
| 增长飞轮 | `truman-渠道增长飞轮-口述.txt` / `笔记.txt` + 4 张图/VLM | 增长飞轮定义、小飞轮/大飞轮、亚马逊案例、设计四步法 |
| 渠道工业化生产 | `truman-渠道工业化生产-口述.txt` / `笔记.txt` + 8 张图/VLM | 工业化生产定义、节点设计、加减法、一堂做课案例 |
| 渠道探索方法论 | `truman-渠道探索方法论-口述.txt` / `笔记.txt` + 反案例 + 渠道特性 | 扫描→预判→测试→建模四步法、四案例、渠道评分 |
| 客户介绍渠道 | 动力/触点/阻力分析 3 张图/VLM | 老带新优化三要素 |
| 获客小抄 | 小抄 01-05 共 5 张图/VLM | 线上/线下/转化/推荐获客清单 |
| 案例武器库 | 案例 01-24 共 24 张图/VLM | 24 个行业真实获客清单 |

---

## 2. 待生产卡片清单

### P0：三大核心框架（3 张）

#### 2.1 `framework-yitang-growth-flywheel`

| 字段 | 要求 |
|:---|:---|
| type | framework |
| title | 增长飞轮：把单点增长变成自我强化的增强回路 |
| domain | yitang, growth, strategy |
| confidence | 0.85 |
| trust_level | medium-high |
| source_refs | `00_inbox/一堂五步法之增长/truman-渠道增长飞轮-口述.txt` |

**内容要求**：
- 一句话：找到关键增长要素的因果关系，串成自我强化的循环系统
- 区分小飞轮（个人/局部）vs 大飞轮（公司级战略）
- 四步法：列要素 → 找因果 → 测闭环 → 狂拉动
- 亚马逊飞轮五层逻辑：表象层 → 因果链 → 核心价值 → 模式壁垒 → 启动点
- 小说 app 飞轮案例：流量 → 下载 → 用户 → 创作者 → 内容 → SEO 流量
- When NOT to Use：业务价值未验证、要素间无真实因果关系、资源不足以推动飞轮
- 失败模式：强行画圈、要素过多、忽视启动点、飞轮与业务脱节
- Critique：系统动力学视角、线性增长论者、资源约束论者
- related ≥ 5：链回 `framework-yitang-channel-exploration-4step`、`framework-yitang-channel-industrialization`、`case-yitang-amazon-growth-flywheel`、`case-yitang-novel-app-flywheel`、`tool-yitang-growth-flywheel-design`

#### 2.2 `framework-yitang-channel-industrialization`

| 字段 | 要求 |
|:---|:---|
| type | framework |
| title | 渠道工业化生产：让高不确定工作持续高质量交付 |
| domain | yitang, growth, operations |
| confidence | 0.80 |
| trust_level | medium |
| source_refs | `00_inbox/一堂五步法之增长/truman-渠道工业化生产-口述.txt` |

**内容要求**：
- 一句话：面对高度不确定的工作，通过系统化流程实现持续高质量交付
- 三要素：高度不确定性 + 持续交付 + 高质量标准
- 与 SOP 的区别、与精益创业的关系（0→1 用精益，1→N 用工业化）
- 五步法：定目标 → 建节点 → 做加法 → 做减法 → 迭代优化
- 节点类型：门槛节点、检查节点、评审节点、动手节点
- 一堂做课案例：10 个环节，通过率 50%→95%，NPS 80+
- When NOT to Use：一次性项目、高度标准化工作、创意需完全自由发挥
- 失败模式：把 SOP 当工业化、流程过 rigid、忽视人的创造力
- related ≥ 5

#### 2.3 `framework-yitang-channel-exploration-4step`

| 字段 | 要求 |
|:---|:---|
| type | framework |
| title | 渠道探索四步法：科学找到可持续获客渠道 |
| domain | yitang, growth, sales |
| confidence | 0.85 |
| trust_level | medium-high |
| source_refs | `00_inbox/一堂五步法之增长/truman-渠道探索方法论-口述.txt` |

**内容要求**：
- 一句话：通过扫描 → 预判 → 测试 → 建模四步，系统找到可持续获客渠道
- 四步详细拆解：
  - 扫描：建 20-50 渠道清单，消除认知盲区
  - 预判：按渠道特性、产品匹配、确定性评分排序
  - 测试：低成本验证，拿数据说话
  - 建模：持续化、工业化，延长渠道生命周期
- 核心洞察：可持续获客是项目生存标志，比商业模式验证更重要
- 四案例映射：固体红牛、徐建发票 SaaS、马毅云电脑、一堂自身增长
- When NOT to Use：产品价值未验证、无基本资源、团队无测试能力
- 失败模式：依赖手感、跳过扫描预判、单渠道依赖、混淆人事
- related ≥ 5

---

### P1：关键工具（5 张）

#### 2.4 `tool-yitang-growth-flywheel-design`

| 字段 | 要求 |
|:---|:---|
| type | tool |
| title | 增长飞轮设计工具：从业务要素到增强回路 |
| domain | yitang, growth |
| confidence | 0.82 |
| trust_level | medium |

**内容要求**：
- 操作步骤 7-10 步，包含 worksheet 模板
- 必须含「因果强度检查表」
- 示例：用该工具设计一个知识付费/电商/社区的飞轮
- related ≥ 5

#### 2.5 `tool-yitang-channel-scan-cheat-sheet`

| 字段 | 要求 |
|:---|:---|
| type | tool |
| title | 渠道扫描小抄：线上/线下/转化/推荐获客清单 |
| domain | yitang, growth |
| confidence | 0.80 |
| trust_level | medium |
| source_refs | 获客小抄 01-05 VLM |

**内容要求**：
- 整合 4 张小抄为一张清单工具
- 分类：线上获客、线下获客、获客转化、推荐获客
- 每类给出 8-12 个具体渠道 + 适用场景
- 使用说明：扫描阶段先用此清单打开视野
- related ≥ 5

#### 2.6 `tool-yitang-channel-scoring-matrix`

| 字段 | 要求 |
|:---|:---|
| type | tool |
| title | 渠道预判评分矩阵：科学排序候选渠道 |
| domain | yitang, growth |
| confidence | 0.82 |
| trust_level | medium |

**内容要求**：
- 渠道特性五维度：大小、集中度、成本、快慢、持续性
- 产品匹配维度：标准化程度、客单价、决策复杂度
- 确定性维度：资金要求、技能要求、资源要求
- 给出评分表模板和示例
- related ≥ 5

#### 2.7 `tool-yitang-referral-channel-optimization`

| 字段 | 要求 |
|:---|:---|
| type | tool |
| title | 老带新渠道优化工具：动力 × 触点 × 阻力 |
| domain | yitang, growth |
| confidence | 0.80 |
| trust_level | medium |
| source_refs | 客户介绍增长渠道动力/触点/阻力分析 3 张 VLM |

**内容要求**：
- 动力：名、利、情三维度 + 提升策略
- 触点：峰值体验、首次购买、复购、关键时刻
- 阻力：信任顾虑、骚扰顾虑、操作门槛
- 给出检查清单和优化动作表
- related ≥ 5

#### 2.8 `tool-yitang-channel-industrialization-node-design`

| 字段 | 要求 |
|:---|:---|
| type | tool |
| title | 工业化生产节点设计工具：把复杂交付变成可控流程 |
| domain | yitang, growth, operations |
| confidence | 0.80 |
| trust_level | medium |

**内容要求**：
- 四种节点定义 + 设计原则
- 一堂做课 10 环节映射到四种节点
- 给出节点设计 worksheet
- related ≥ 5

---

### P1：典型案例（5 张）

#### 2.9 `case-yitang-amazon-growth-flywheel`

| 字段 | 要求 |
|:---|:---|
| type | case |
| title | 案例：亚马逊增长飞轮的五层逻辑 |
| domain | yitang, growth, strategy |
| confidence | 0.88 |
| trust_level | high |

**内容要求**：
- 关键要素：用户体验 → 流量 → 卖家 → 选品 → 规模经济 → 更低价格
- 五层逻辑逐层拆解
- 启动策略：早期从用户体验切入
- related ≥ 5

#### 2.10 `case-yitang-novel-app-flywheel`

| 字段 | 要求 |
|:---|:---|
| type | case |
| title | 案例：小说 app 如何用 SEO 补全增长飞轮 |
| domain | yitang, growth |
| confidence | 0.80 |
| trust_level | medium |

**内容要求**：
- 背景：亏损、增长慢、团队内耗
- 关键决策：把内容页面 URL 开放给百度 SEO
- 关键数字：200 万启动资金、2 万日活、上千万页面
- 结果：飞轮闭合
- related ≥ 5

#### 2.11 `case-yitang-yitang-course-industrialization`

| 字段 | 要求 |
|:---|:---|
| type | case |
| title | 案例：一堂如何用工业化生产保证每周高质量做课 |
| domain | yitang, growth, operations |
| confidence | 0.85 |
| trust_level | medium-high |

**内容要求**：
- 背景：早期依赖 Truman 个人，成功率 50-60%
- 关键决策：建立 10 环节工业化流程
- 关键数字：通过率 50%→95%，NPS 80+
- 10 环节清单
- related ≥ 5

#### 2.12 `case-yitang-solid-redbull-channel`

| 字段 | 要求 |
|:---|:---|
| type | case |
| title | 案例：固体红牛如何通过渠道探索找到司机群体 |
| domain | yitang, growth |
| confidence | 0.78 |
| trust_level | medium |

**内容要求**：
- 扫描 → 预判（司机群体） → 测试（加油站） → 建模（网吧/台球厅复制）
- 关键数字和决策
- related ≥ 5

#### 2.13 `case-yitang-maiyi-cloud-computer-channel`

| 字段 | 要求 |
|:---|:---|
| type | case |
| title | 案例：马毅云电脑如何扫描 60+ 渠道实现 3.7 亿营收 |
| domain | yitang, growth, b2b |
| confidence | 0.78 |
| trust_level | medium |

**内容要求**：
- 60+ 渠道扫描 → 矩阵模型 → 联想等标准化渠道
- 关键数字：3.7 亿营收
- 渠道特性维度应用
- related ≥ 5

---

### P2：索引与暗知识（2 张）

#### 2.14 `tool-yitang-industry-channel-arsenal-index`

| 字段 | 要求 |
|:---|:---|
| type | tool |
| title | 24 行业获客清单索引：跨行业渠道灵感库 |
| domain | yitang, growth |
| confidence | 0.75 |
| trust_level | medium |
| source_refs | 案例武器库 01-24 VLM |

**内容要求**：
- 不要复制 24 个行业全部内容
- 按行业类型分类（教育、餐饮、零售、SaaS、制造、服务等）
- 每类提炼 2-3 个最具代表性的获客策略
- 给出使用说明：如何结合自身业务迁移
- related ≥ 5

#### 2.15 `dk-yitang-channel-exploration-traps`

| 字段 | 要求 |
|:---|:---|
| type | dk |
| title | 渠道探索常见陷阱：18 万字共建作业里的血泪教训 |
| domain | yitang, growth |
| confidence | 0.80 |
| trust_level | medium |

**内容要求**：
- 7-10 个常见陷阱
- 每个陷阱：症状 → 根因 → 修复动作
- 来源：反案例图 + 口述中的失败模式
- related ≥ 5

---

### P1：跨域桥接卡（2 张）

> 追加依据：`diag_20260627_wangyuyan-cross-domain-bridge-supplement`

#### 2.16 `framework-yitang-channel-unit-economics`

| 字段 | 要求 |
|:---|:---|
| type | framework |
| title | 渠道单元经济模型：把每个获客渠道当作独立经济单元核算 |
| domain | yitang, growth, unit-model |
| confidence | 0.82 |
| trust_level | medium-high |
| source_refs | `00_inbox/一堂五步法之增长/truman-渠道探索方法论-口述.txt`, `yt-unit-model-concept` |

**内容要求**：
- 一句话：每个可持续渠道都应有自己的 CAC、转化率、LTV、回收周期；混合计算会让烂渠道躲在好渠道后面。
- 核心公式：
  - 单渠道单元利润 = 渠道流量 × 转化率 × 客单价 × 复购率 − 渠道获客成本
  - 渠道回收周期 = 渠道 CAC ÷（单客户月贡献毛利 × 毛利率）
  - 渠道 LTV/CAC = 渠道客户 LTV ÷ 渠道 CAC
- 五维度渠道特性（大小、集中度、成本、快慢、持续性）与单元经济的关系；
- 渠道投资组合：快回收/现金流型、可扩展型、实验型；
- When NOT to Use：产品价值未验证、渠道数据不足 3 个月、客户无法归因；
- 失败模式：混合 CAC、只看 CAC 不看回收周期、忽视渠道生命周期衰减；
- Critique：归因模型局限（last-touch 偏差）、渠道间相互 cannibalization、短期回收与长期品牌投入的冲突；
- related ≥ 7：`framework-yitang-channel-exploration-4step`, `yt-unit-model-concept`, `yt-unit-model-overview`, `tool-区分获客渠道计算单元roi`, `framework-yitang-growth-flywheel`, `tool-yitang-channel-scoring-matrix`, `case-yitang-maiyi-cloud-computer-channel`。

#### 2.17 `concept-yitang-channel-lean-validation-bridge`

| 字段 | 要求 |
|:---|:---|
| type | concept |
| title | 渠道精益验证：把渠道 0→1 测试当作一种 MVP |
| domain | yitang, growth, lean-startup |
| confidence | 0.80 |
| trust_level | medium-high |
| source_refs | `00_inbox/一堂五步法之增长/truman-渠道探索方法论-口述.txt`, `lean-startup-domain-digest` |

**内容要求**：
- 一句话：渠道探索四步法的前三步，本质上是把「渠道获客假设」当作 MVP 来低成本验证。
- 渠道 MVP 的 4 种形态：
  1. **Smoke Test Landing Page**：假着陆页 + 真广告，测 CTR/注册/预购；
  2. **Concierge Channel**：创始人/销售手动跑通首批客户，验证渠道可达性；
  3. **Borrowed Traffic**：借朋友圈/友商/交易平台流量快速测试；
  4. **Micro-Spend Ads**：小额付费（如 ¥2000-5000）验证某个渠道的基本转化。
- 与产品 MVP 的区别：产品 MVP 验证「价值假设」，渠道 MVP 验证「可达假设」；
- 与工业化的边界：0→1 用精益验证，1→N 用工业化生产；
- When NOT to Use：产品价值未验证、目标客群不清晰、预算不足以获得统计显著样本；
- 失败模式：把渠道工业化流程套在 0→1 测试上、过早放大未验证渠道、用 brand campaign 替代验证实验；
- related ≥ 7：`framework-yitang-channel-exploration-4step`, `framework-lean-false-model`, `framework-lean-abcd-model`, `tool-lean-fake-marketing`, `tool-lean-presell`, `tool-lean-leverage-traffic`, `framework-yitang-channel-industrialization`。

---

## 3. 生产规范

### 3.1 每张卡必须包含

```yaml
---
id: <严格匹配文件名>
type: <framework/tool/concept/case/dk>
title: <一句话标题>
status: enriched
domain:
  - yitang
  - growth
confidence: <按诊断要求>
trust_level: <按诊断要求>
author: 老顽童
reviewed_by: pending
source_refs:
  - <具体文件路径>
related:
  - '[[xxx]]'
  - ...
---
```

### 3.2 内容结构要求

| type | 必须段落 |
|:---|:---|
| framework | 一句话定义、核心结构图、操作步骤、When NOT to Use、失败模式、Critique、related |
| tool | Burn line、一句话、操作步骤、典型场景、When NOT to Use、失败模式、related |
| case | 背景、关键数字、关键决策、结果、业务公式/要素映射、成功原因、related |
| dk | 使用场景、N 条洞见、每条附症状/修复、边界、related |

### 3.3 质量标准

1. **不要复制笔记原文**：用九层深挖后的深度结构重新组织。
2. **source_refs 必须真实存在**：指向 `00_inbox/一堂五步法之增长/` 下的具体文件。
3. **confidence 严格按诊断要求**：不要全部写 0.85。
4. **related ≥ 5**，至少 1 个跨域链接（如 strategy、lean-startup、unit-model、ai-collaboration）。
5. **跨域桥接卡**（2.16 / 2.17）要求 `related ≥ 7`，且必须同时链回两个域的核心卡。
6. **必须跑 `kdo pre-submit`**，粘贴输出到汇报中。
7. **24 张案例武器库不要全卡化**：只建 1 张索引工具卡。
8. **避免与现有卡重复**：现有 `tool-区分获客渠道计算单元roi.md`、`tool-马易-公寓获客自跑通原则.md` 可 related，不要覆盖；`framework-yitang-channel-unit-economics` 是框架升级，非重复。

---

## 4. 提交与验收

### 4.1 提交格式

```markdown
## 渠道增长域卡片生产完成汇报

### 产出清单
| 卡片 | 类型 | 状态 |
|:---|:---|:---|
| framework-yitang-growth-flywheel | framework | enriched |
| ... | ... | ... |

### pre-submit 输出
```text
[粘贴 kdo pre-submit 输出]
```

### 需要王语嫣重点审查的项
- ...
```

### 4.2 验收流程

1. 王语嫣跑 `kdo pre-submit` 全量复核；
2. 王语嫣按九层深挖标准抽检 3-5 张卡；
3. 问题整改后，提交欧阳锋终审 P0 卡；
4. P1/P2 卡由王语嫣终审后入库。

---

## 5. 特别注意事项

- 本任务不修改旧卡，只新建；
- 若发现素材中有矛盾或不清晰处，先按最合理理解生产，并在卡片中标注 `[conf=X, source=...]`；
- 案例卡中的数字必须来自素材，不要编造；
- 亚马逊飞轮、小说 app 飞轮等经典案例不要过度演绎，保持与素材一致。

---

*任务下达：王语嫣 | 日期：2026-06-27*
