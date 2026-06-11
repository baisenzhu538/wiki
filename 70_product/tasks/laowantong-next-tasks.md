# 老顽童后续任务

> **更新：2026-06-11** — 欧阳锋审查 CLI 批次 + 王语嫣首批产出完成。纠正记录见 `60_feedback/corrections/corr_20260611_laowantong-机会预判域-OCR遗漏+旧卡未清理.md`。**回归后先读该文件。**

---

## 🎯 当前执行顺序（从上到下，做完再开下一个）

| 顺序 | 任务 | 状态 | 参考 |
|:----:|------|:----:|:----:|
| **0** | **🔴 CLI 批量卡审核精选** | **🔜** | **skills/ 目录 10 张批量卡未经审核直接入库，需补审——能用的精修，不合格的标记暂不发布** |
| **1** | **🔴 桥接卡试点：MECE + Issue Tree** | **🔜** | **王语嫣识别缺口的首批试点。见下方详细要求** |
| **2** | 纪浩体系完整萃取 | ⏳ | 旧任务，桥接卡试点通过后再做 |
| **3** | 课转技能卡补"判断标准" | ⏳ | 清单小抄/MECE法等，内容偏薄需补深 |

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

#### 4. 攻击者（每张至少 2 位，不同范式）

从以下池中选择，优先选与桥接场景相关的：
- **Kahneman**（认知偏差、过度自信）
- **Taleb**（黑天鹅、过度结构化）
- **Christensen**（颠覆式创新、过度分析陷阱）
- **Mintzberg**（战略即实践、反对过度结构化）
- **Eric Ries**（精益创业、快速实验 vs 完美分析）

### 两步走

1. 试点产出 MECE + Issue Tree → 通知欧阳锋审查
2. 审查通过后，再铺剩余卡（按欧阳锋裁定的新优先级）：
   - P0: Hypothesis-Driven 系列（concept + skill + dk）
   - P0: 5 Whys（工具卡）
   - P1: Pyramid Principle → 7-S → Trusted Advisor

**80/20 法则不做卡**——各已有卡中已隐性使用，溯源链断不需要补卡解决。

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
