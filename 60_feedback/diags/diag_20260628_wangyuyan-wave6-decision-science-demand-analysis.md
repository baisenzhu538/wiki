---
id: diag_20260628_wangyuyan-wave6-decision-science-demand-analysis
type: diagnosis
status: pending_review
author: 王语嫣
created_at: 2026-06-28
updated_at: 2026-06-28
reviewer: 欧阳锋
source_refs:
- .agent/kb-evolution-direction.md
- 60_feedback/methods/method-dialogue-driven-kb-evolution.md
- 60_feedback/methods/method-systematic-dialogue-kb-evolution-hybrid.md
- 70_product/tasks/production-queue.md
---

# Wave 6 新盲区诊断报告：决策科学域 + 需求分析域

## 诊断方法

1. **全库扫描**：统计 `30_wiki/` 下 2010 张卡片的 domain/type/status 分布
2. **已 reviewed 卡片分析**：重点看近期通过欧阳锋终审的卡片，识别用户已投入资源的方向
3. **domain digest 缺口对照**：对照 `.agent/kb-evolution-direction.md` 中黄药师待启动的 3 个 domain digest
4. **冷热混合模型**：用系统扫描发现机会，用领域知识判断价值

## 当前状态关键数据

| 指标 | 数值 |
|:---|:---|
| 全库卡片数 | 2010 |
| reviewed 卡片数 | 166 |
| src_unknown 域卡片数 | ~435（domain 未正确标注） |
| 无 domain digest 的活跃域 | 决策科学、需求分析、五步法、healthcare、design 等 |

## 已 reviewed 卡片域分布（Top 10）

| Domain | 数量 | 说明 |
|:---|---:|:---|
| yitang,decision-science | 14 | 决策科学已有一定积累 |
| yitang | 10 | 一堂通用方法论 |
| demand-analysis | 10 | 需求分析已有基础 |
| yitang,growth | 9 | 渠道增长域已较成熟 |
| master | 9 | 元能力/中神通 |
| yitang,research | 8 | 研究方法论 |
| yitang,personal-growth | 7 | 个人成长少量 |
| product,yitang | 6 | 产品内核 |
| human-ai-collaboration,ai-collaboration,yitang | 6 | AI 协作 |
| panproduct,organization,yitang | 5 | 泛产品组织 |

## 盲区 A：决策科学域系统化

### 为什么是当前盲区？

- 已有 14 张 reviewed 卡片，说明用户认可该域价值，但**缺少 domain digest/index 卡**，导致 14 张卡散落在 case/dk/framework 中，没有统一入口
- 只有 1 张 framework（`yt-decision-abcd-model`），缺少决策流程、决策质量评估、认知偏差清单等核心骨架
- 已有 case 卡多为 ROI/办公场景，缺少 **AI 时代决策辅助** 的跨域桥接（决策科学 × AI 协作）
- 与 `.agent/kb-evolution-direction.md` 中「决策域 domain digest」待启动项完全吻合

### 商业价值

> 提升 Agent 在商业判断、资源分配、机会成本场景中的咨询质量；把一堂的决策案例升级为可复用的决策方法论。

### 与现有域的桥接

- 决策科学 × 需求分析：需求验证中的 go/no-go 决策
- 决策科学 × AI 协作：AI 作为决策辅助工具，何时可信、何时需人工兜底
- 决策科学 × 商业战略：战略选择、投资组合决策

### 建议建设的卡片

| ID | Type | Title | 关键问题 |
|:---|:---|:---|:---|
| `domain-decision-science-index` | index | 决策科学域索引 | 决策科学域包含哪些核心方法论？如何按场景选用？ |
| `framework-decision-quality-checklist` | framework | 决策质量六问检查表 | 一个决策做出前，必须回答哪六个问题？ |
| `framework-decision-cognitive-bias-map` | framework | 商业决策常见认知偏差地图 | 哪些认知偏差最常破坏商业决策？如何对冲？ |
| `dk-decision-when-to-defer` | dk | 何时应该推迟决策 | 什么情况下"不决策"比"快速决策"更好？ |
| `case-decision-ai-assisted-vs-human` | case | AI 辅助决策 vs 人工决策的边界案例 | 哪些决策可以交给 AI，哪些必须保留人工判断？ |

## 盲区 B：需求分析域深化

### 为什么是当前盲区？

- 已有 10 张 reviewed 卡片（3 concept + 4 dk + 3 framework），但**缺少 case 卡和 domain digest**
- 需求分析是"一堂五步法"的第一环，与产品内核、渠道增长、精益创业都有强连接，但目前这些连接主要靠相关链接，缺少**跨域桥接卡**
- 已有 framework 偏重方法论（决策链、早期验证、场景重构），缺少 **需求分析在不同商业模式（B2B/B2C/平台）中的差异化应用**
- 与 `.agent/kb-evolution-direction.md` 中「需求分析域 domain digest」待启动项完全吻合

### 商业价值

> 强化 Agent 在需求识别、需求验证、假需求识别等核心咨询场景的能力；把需求分析从产品内核的附属域升级为独立方法论域。

### 与现有域的桥接

- 需求分析 × 产品内核：需求验证如何指导 MVP 设计
- 需求分析 × 渠道增长：不同渠道对应的需求场景差异
- 需求分析 × 精益创业：假需求识别与 pivot 决策

### 建议建设的卡片

| ID | Type | Title | 关键问题 |
|:---|:---|:---|:---|
| `domain-demand-analysis-index` | index | 需求分析域索引 | 需求分析域有哪些核心工具？适用什么场景？ |
| `case-demand-b2b-enterprise-erp` | case | ToB 企业 ERP 需求分析案例 | 复杂 B2B 需求如何分层验证？ |
| `case-demand-b2c-consumer-insight` | case | ToC 消费洞察驱动需求案例 | 用户说的和做的不一致时，如何识别真需求？ |
| `framework-demand-validation-pipeline` | framework | 需求验证流水线 | 从假设到验证的完整流程是什么？ |
| `dk-demand-signal-vs-noise` | dk | 需求信号与噪音的区分 | 哪些市场信号是真需求，哪些是噪音？ |

## 优先级排序

| 盲区 | 与用户长期目标关联度 | 与现有卡片桥接潜力 | 素材可获取性 | 生产可行性 | 综合 |
|:---|:---:|:---:|:---:|:---:|:---:|
| A 决策科学域系统化 | 5 | 5 | 4 | 4 | **18/20** |
| B 需求分析域深化 | 5 | 5 | 5 | 5 | **20/20** |

**建议 Wave 6 同时启动 A + B**：两个域都已具备 10+ reviewed 卡片基础，素材充足，且都与用户核心目标（提升 Agent 咨询能力）高度相关。

## 依赖与风险

| 风险 | 说明 | 缓解 |
|:---|:---|:---|
| 与黄药师待启动的 domain digest 冲突 | 决策域、需求分析域 domain digest 本应由黄药师负责 | 黄药师负责 index/digest 的基建规格，老顽童负责内容卡片生产；分工明确 |
| 与现有 14/10 张 reviewed 卡重复 | 需要避免新建卡片与已有卡片重叠 | 王语嫣先审核已有卡片，任务单中明确每张新卡与旧卡的区别 |
| 跨域桥接卡质量风险 | 桥接卡容易变成"拼盘" | 严格按桥接卡规范：必须回答双向价值 + 含外部证据 + 明确 When NOT to Use |

## 入队建议

在 `production-queue.md` 中新增：

| 队列序号 | 任务 ID | 任务名称 | 状态 | 领取人 | 预计卡数 | 阻塞/依赖 | 来源文件 |
|:---:|:---|:---|:---:|:---:|---:|:---|:---|
| #21 | `task_20260628_laowantong-wave6-decision-science-systematization` | Wave 6-A：决策科学域系统化 | queued | 老顽童 | 5 | 依赖 Wave 6 诊断 reviewed | 本诊断报告 |
| #22 | `task_20260628_laowantong-wave6-demand-analysis-deepening` | Wave 6-B：需求分析域深化 | queued | 老顽童 | 5 | 依赖 Wave 6 诊断 reviewed | 本诊断报告 |

## 下一步动作

1. 欧阳锋审查本诊断报告
2. 用户确认是否同时深挖 A + B
3. 王语嫣根据确认结果创建 #21/#22 任务单
4. 老顽童领取并按队列顺序生产

---

*诊断人：王语嫣 | 日期：2026-06-28*
