# 老顽童后续任务

> **更新：2026-06-12** — 全量任务已下达。从上到下逐个做，做完一个再开下一个。

---

## 🎯 当前执行顺序

| 顺序 | 任务 | 状态 | 参考 |
|:----:|:-----|:----:|:-----|
| **1** | **🔴 Pyramid Principle 桥接卡** | **🔜** | 仅剩的最后一张经典桥接卡 |
| **2** | **🔴 旧卡补互链 — P0 批次** | **🔜** | 提升图谱密度，优先修深黑节点 |
| **3** | **旧卡补互链 — P1 批次** | ⏳ | 上批完成后 |
| **4** | **王语嫣下一轮 Bridge 执行** | ⏳ | 等王语嫣 master 域巡查产出后再动 |
| — | 旧任务均已关闭 | ✅ | 0-6 全部完成 |

---

## 🔴 任务 1：Pyramid Principle 桥接卡

### 格式

这是 8 张经典桥接卡中最后一张未产的。格式跟 MECE、7-S 完全一样。

**存放路径：** `30_wiki/frameworks/concept-minto-pyramid-principle.md`

**三个条件（缺一不可，欧阳锋审查时强制执行）：**
1. Bridge 节已写 ↔ 与一堂体系的桥接关系
2. `bridges_to` frontmatter 已填（至少 1 条）
3. Synthesis 链接 ≥5 个（含至少 2 个同域横向链接）

### 攻击者选择

建议：参考 7-S 的 Mintzberg + Pfeffer、Trusted Advisor 的 Kahneman + Christensen。
不要跟已有桥接卡重复相同的攻击者组合。

可选组合：Taleb（金字塔结构在不确定性下的脆弱性）+ Eric Ries（精益创业反对过度计划）

### 源材料

`60_feedback/diagnosis/diag_20250611_consulting-skills-research.md` 中 Pyramid Principle 的 Gap 说明。

---

## 🔴 任务 2：旧卡补互链 — P0 批次

### 为什么

图谱放射状的根本原因之一是卡间互链稀疏。新卡已达标（Synthesis ≥5），但旧卡大多只有 1-2 个链接指向入口卡。

### 目标

在已有卡中，优先修被大量引用的**深黑节点**的 `related` 字段——让它们之间也有链接。

### P0 批次：深黑节点互连（约 15 张）

这些卡是图谱中的深黑色节点（被大量引用），但彼此之间几乎没有 `related` 链接：

```
1. yt-foresight-business-spectrum      ↔ yt-entrepreneur-five-step-method
2. yt-entrepreneur-five-step-method     ↔ yt-model-entrepreneur-map
3. yt-model-entrepreneur-map            ↔ yt-entrepreneur-key-hypotheses
4. yt-entrepreneur-key-hypotheses       ↔ yt-entrepreneur-unit-model
5. yt-entrepreneur-unit-model           ↔ yt-model-five-step-canvas
6. yt-five-step-method                  ↔ yt-entrepreneur-five-step-method
7. yt-model-progress-map                ↔ yt-model-entrepreneur-map
```

**操作方法：**
每对卡互相在 `related` 中加上对方。例如 `yt-foresight-business-spectrum` 的 `related` 加 `"yt-entrepreneur-five-step-method"`，反之亦然。

**完成标志：** 以上 7 对共 14 张卡全部补完双向 `related`。

### P1 批次：核心工具卡互连（约 20 张）

P0 完成后通知欧阳锋，再给 P1 列表。

---

## 任务 3：王语嫣下一轮 Bridge 执行

等王语嫣 master 域巡查结束后，按她的报告执行桥接。不急。

---

## 🔴 任务 0：CLI 批量卡审核精选

`30_wiki/skills/` 下有 10 张技能卡（`skill-ai-*` + `skill-decision-*` + `skill-cognitive-bias-*` + `skill-first-principles-*`），创建时间均为 2026-06-11 02:11:48（同一秒），明显为扫描器批量写入。

**问题**：dashboard 此前已标注"待老顽童审核精选"，你未做审核直接入库。

**操作**：
1. 逐张过这 10 张卡
2. 质量达标的 → 精修后 frontmatter 加 `reviewed_by: "laowantong"`
3. 不达标的 → frontmatter 加 `status: "needs-review"`，暂不发布
4. 筛选标准：操作步骤是否可执行、是否有常见失败模式、是否有工具/环境要求

---

## 🔴 任务 1：桥接卡试点（王语嫣需求）

### 背景

王语嫣在首次诊断中发现知识库缺少经典管理咨询框架（MECE、Issue Tree 等），但这些框架与一堂现有体系存在天然桥接点。她已在诊断记录中详细标注了 8 个缺口。

**源材料**：`60_feedback/diagnosis/diag_20250611_consulting-skills-research.md`（必读）

### 试点方案（欧阳锋裁决）

先产 **2 张试点卡** 验证"桥接式卡片"格式，通过后再铺剩余 5 张。

**试点卡**：
1. `concept-mckinsey-mece`（MECE 原则：相互独立、完全穷尽）— type: `framework`
2. `concept-mckinsey-issue-tree`（Issue Tree：结构化问题拆解）— type: `tool`

### 格式要求

#### 1. Bridge 节（必须写，区别于普通概念卡）

每张卡必须有一个 **Bridge** 节，明确标注与一堂体系的桥接点。格式：

```markdown
## Bridge to 一堂体系

| 桥接目标 | 桥接关系 | 使用场景 |
|:---------|:---------|:---------|
| [[yt-foresight-model-taxonomy]] | MECE 是其维度选择的底层原则 | 在预判分析的雷达图维度设计阶段，用 MECE 检查维度是否重叠或遗漏 |
| 案例：[具体的桥接用法示例] |
```

#### 2. source_refs

这些概念来自经典英文商业文献，不是口述稿素材。格式：

```yaml
source_refs:
  - "Rasiel, E. (1999). *The McKinsey Way*. McGraw-Hill."
  - "Minto, B. (2009). *The Pyramid Principle*. 3rd ed. FT Press."  # MECE相关章节
```

#### 3. diagnostic_signals（每张至少 2 条）

```yaml
diagnostic_signals:
  - signal: "用户说'我列了很多原因但感觉还是漏了什么'"
    framework_lens: "MECE 检查：当前维度列表是否相互独立、完全穷尽"
    follow_up_question: "你列的这几个原因之间，有没有哪个其实可以合并？有没有哪个维度被落下了？"
```

#### 4. bridges_to frontmatter（每张至少 1 条）

**Bridge 节**是正文给人读的，**`bridges_to`** 是 frontmatter 给 Graph RAG 吃的。两个都写，缺一不可。

```yaml
bridges_to:
  - target: "yt-foresight-model-taxonomy"
    relation: "provides_foundation_for"
    description: "MECE 是预判维度选择的底层原则"
    context: "一堂体系未显式命名 MECE，但它隐含在维度设计中"
```

这直接决定图谱能不能长出跨域边——你不写这个字段，图里就没有"bridges to"边，放射状结构就修不好。

#### 4. 攻击者（每张至少 2 位，不同范式）

从以下池中选择，优先选与桥接场景相关的：
- **Kahneman**（认知偏差、过度自信）
- **Taleb**（黑天鹅、过度结构化）
- **Christensen**（颠覆式创新、过度分析陷阱）
- **Mintzberg**（战略即实践、反对过度结构化）
- **Eric Ries**（精益创业、快速实验 vs 完美分析）

### 审查标准（欧阳锋审查时强制执行）

每张桥接卡必须满足以下三条才能通过：
1. **Bridge 节**已写（正文内，阐述与一堂体系的桥接关系）
2. **`bridges_to`** frontmatter 已填（至少 1 条，给 Graph RAG 吃）
3. **Synthesis 链接 ≥5 个**，其中至少 2 个是**同域横向链接**（即指向同样属于"一堂"体系的其他卡，而非仅指向目录/入口卡）

以上三条缺一不可。不满足直接退回。

---

## 🔴 执行规范：domain 标注规则（强制）

> 王语嫣诊断发现 design 域 32 张卡全部因"按出身不按内容"标注而被锁成孤岛。
> 此规范即日起强制执行，适用于所有新卡和旧卡修改。

### 核心原则

**标内容，不标出身。**

`domain` 字段标注的依据是**卡片内容讨论了什么域**，而不是**来源是谁**。

### 判定方法

读卡片的 **Summary + 第一个 Claim + Critique 第一句话**。如果这三处中出现了另一个域的核心概念，就应加上那个域的 domain。

### 示例

| 卡片 | 旧 domain（出身） | 新 domain（内容） |
|:----|:-----------------|:-----------------|
| dk-yb7（中国设计需求分层） | design | **design, yitang, business-strategy** |
| dk-yb19（视觉价格匹配） | design | **design, yitang** |
| dk-yb21（电商定价建模） | design | **design, business-strategy** |

### 已有域列表（`90_control/schemas/concept.yaml` 中完整定义）

| domain | 用途 |
|:-------|:-----|
| master | 元方法/元认知（PEAS、认知升级等跨域通用框架） |
| yitang | 一堂创业/管理/个人修炼方法论 |
| design | 设计方法、AIGC 工作流、审美 |
| consulting | 管理咨询经典工具（MECE、Issue Tree 等） |
| ai | AI 技术概念 |
| ai-collaboration | 人机协作方法论（纪浩、半肥猫等） |
| business-strategy | 商业战略、壁垒、增长 |
| product | 产品设计与产品内核 |
| entrepreneur | 创业 |
| management | 团队管理与组织 |
| personal-growth | 个人修炼、学习、笔记 |

### 典型错误

- ❌ `domain: ["design"]` 因为"月白是设计师"——不对，要看内容讲的是设计还是商业
- ❌ `domain: ["yitang"]` 因为"这是堂课的内容"——不对，如果内容讲的是设计方法，应该标 design
- ✅ 多 domain 是推荐做法——卡片讨论到几个域就标几个

### 谁执行

**老顽童**：产新卡时执行新规则。改旧卡（如 design 域 P0 的 5 张桥接）时一并修正 domain。
**王语嫣**：诊断中抽查 domain 标注质量，反馈给欧阳锋。
**欧阳锋**：审查时检查 domain 是否按内容标注，不通过则退回。

---

### 两步走

1. 试点产出 MECE + Issue Tree → 通知欧阳锋审查
2. 审查通过后，再铺剩余卡（按欧阳锋裁定的新优先级）：
   - P0: Hypothesis-Driven 系列（concept + skill + dk）
   - P0: 5 Whys（工具卡）
   - P1: Pyramid Principle → 7-S → Trusted Advisor

**80/20 法则不做卡**——各已有卡中已隐性使用，溯源链断不需要补卡解决。

---

## 任务 0 审核汇总

共审核 22 张批量卡（skill-ai-* ×18 + skill-decision-* ×2 + skill-cognitive-bias-* ×1 + skill-first-principles-* ×1）：

| 等级 | 数量 | 操作 | 代表卡片 |
|:-----|:----:|:-----|:---------|
| **A级**（达标） | 10 | 直接加 `reviewed_by: "laowantong"` | skill-decision-delay-intuition, cognitive-bias-12-check, first-principles-assumption-classify, ai-landing-five-steps, ai-four-elements-validation, ai-info-literacy-three-layer, ai-research-five-steps, ai-scene-four-elements, ai-problem-question-check, decision-outside-view |
| **B级**（格式精修后达标） | 7 | 修复表格/编号格式后加 reviewed_by | ai-old-small-checklist, ai-evidence-check, ai-system-redundancy, ai-purpose-bias-check, ai-parallel-validation, ai-narrative-test, ai-oral-spray-input |
| **C级**（不达标） | 2 | 改 `status: needs-review` | ai-ai-workspace-setup（编号混乱）, ai-prd-for-ai（内容缺失） |
| **重复卡** | 3 | 加 `superseded_by` + 改 needs-review | ai-voice-input-doubao→oral-spray-input, ai-problem-validation→four-elements-validation, ai-question-problem-checklist→problem-question-check |

---

## 任务 1 桥接卡试点汇总

产出 2 张桥接卡，均满足审查标准：

| 卡片 | 类型 | 桥接目标 | 攻击者 | 状态 |
|:-----|:-----|:---------|:---------|:-----|
| `concept-mckinsey-mece` | framework | yt-foresight-model-taxonomy, yt-entrepreneur-five-step-method, skill-mece体系框架法 | Kahneman（认知偏差）, Taleb（过度结构化） | 待欧阳锋审查 |
| `concept-mckinsey-issue-tree` | tool | yt-entrepreneur-five-step-method, yt-entrepreneur-key-hypotheses, skill-mece体系框架法 | Christensen（过度分析陷阱）, Mintzberg（战略即实践） | 待欧阳锋审查 |

**两张卡均满足三条审查标准：Bridge 节已写、bridges_to 已填、Synthesis 链接 ≥5 个（含 2+ 同域横向链接）。**

---

## 任务 2：纪浩体系完整萃取（旧）

> 之前已拆解，此处略。任务 0/1 完成后启动。

---

## 任务 3：课转技能卡补"判断标准"（旧）

`skill-清单小抄工具箱法`、`skill-mece体系框架法`、`skill-寻找学习教练法` 等课转技能卡，当前"操作步骤"几乎等于"原始表述"的翻译，没有让读者能判断自己做得对不对的标准。

每张此类卡加一个 **判断标准** 小节，例如：

```markdown
## 判断标准
- 一条好清单条目 = 别人照着做也能得到相同结果
- 你的清单条目是否满足：无歧义？可验证？可执行？
```

不多写，一段就行，但必须有。

---

## 任务 4：增加卡片间互链密度（修复图谱放射状）

**背景**：知识图谱呈放射状星形——所有卡片指向目录类页面，卡片之间互链稀疏。黄药师会修过滤逻辑去掉目录页的污染，但卡间互链密度需要你补。

**操作**：

1. **合成新卡时**（MECE、Issue Tree 等桥接卡），Synthesis 节的 wikilink 从"3-5 个"提升到 **"5-10 个"**：
   - 至少 2 个同域横向链接（同属"预判"域的卡互连）
   - 至少 1 个跨域桥接链接（如果有 `bridges_to` 字段，对应的目标卡要在 Synthesis 里写出）
   - 避免只有"指向目录/入口卡"的链接

2. **已有卡的 related 字段**——从可选改为**推荐填写**。后续有空时逐步补旧卡的 related 字段。

3. **具体目标**：以 `yt-foresight-business-spectrum`（终局光谱图）为参考，它当前 Synthesis 有 6 个链接（3 framework + 3 case），这种密度是及格线。

**参考**：`30_wiki/decisions/proposal-graph-rag-star-fix.md`
