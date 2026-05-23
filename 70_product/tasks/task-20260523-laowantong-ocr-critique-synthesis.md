---
title: "老顽童任务：OCR 卡片 Critique + Synthesis 补全"
assigned_to: "老顽童 (Producer)"
priority: "P1"
created_at: "2026-05-23"
reviewer: "欧阳锋"
status: "pending"
depends_on: []
blocks: []
---

# 老顽童任务：OCR 卡片 Critique + Synthesis 补全

## 背景

欧阳锋独立审查确认：136 张 OCR 卡片完成了三步编译法的 **⅓**——Condense（Reusable Knowledge 有 4-17 条实质要点，LLM 已填充），但完全跳过了 Question（Critique）和 Synthesize（Synthesis + wikilinks）。

**不是"缺 Condense"，是"缺 Critique 和 Synthesis"。** 把有 Condense 的卡说成"未加工原料"是错误的——它们是半成品。

## 做什么

对 136 张 OCR 卡片，逐张补全：

1. **Critique（质疑）**：在 Reusable Knowledge 后、Open Questions 前，插入 `## Constraints & Boundaries` 节，包含 ≥2 个外部攻击者视角。格式参照 v1.5 标准（H4 标题 + 2-3 句论证 + 具体引用来源）。

2. **Synthesis（对标）**：在 Open Questions 后、Output Opportunities 前，插入 `## Synthesis` 节，包含 ≥2 个 `[[wikilink]]` 到已有概念卡，说明关联逻辑（互补/矛盾/延伸）。

3. **Wikilinks**：在现有正文中已有的概念引用处，补上 `[[wikilink]]`。

## 执行顺序（严格，不许跳）

| 批次 | 来源 | 数量 | 优先级依据 |
| **Batch 1** | 洪七公高优先级清单 | ~5 张 | 视觉框架→老顽童先做 VA 分析，然后继续编译 |
|
| **Batch 2** | 洪七公中优先级清单 | ~10 张 | 纯文本为主，可直接开工 |
| **Batch 3** | 剩余纯文本类 | ~30 张 | 简单列表/段落截图，OCR 文本可用 |
| **Batch 4** | 剩余混合类 | ~50 张 | 中等复杂度 |
| **Batch 5** | 低价值/OCR 失败 | ~41 张 | 评估后决定：归档 or 删除 or 合并 |

### Batch 1 试点卡（洪七公已识别，从 cross-review 提取）

| 卡 | 特征 | 洪七公建议 |
|:---|:---|:---|
| `ocr-泛产品设计落地篇` | 三列矩阵+色块+难度梯度 | 洪七公先做 VA→老顽童编译 |
| `ocr-预判模型` | 层级+雷达+Checklist 三层 | 同上 |
| `ocr-一堂-个人修炼-全景图MUSE模型` | 系统全景图 | 同上 |
| `ocr-一堂-个人修炼-科学学习IPO-全景策略` | 策略全景 | 同上 |
| `ocr-一堂-个人修炼-表达力火箭模型-执行武器库` | 模型+武器库双层 | 同上 |

**Batch 1 执行流程**：老顽童对原图做 Visual Analysis 五维法 → 产出 VA 段落 → 基于 VA + OCR 文本走三步编译法的 Critique + Synthesis。

## 怎么做（单卡模板）

在 `## Reusable Knowledge` 和 `## Open Questions` 之间插入：

```markdown
## Constraints & Boundaries

#### [学者名] — [攻击角度标题]
[2-3 句论证，含具体引用。说明这个框架/方法论在什么边界条件下失效。]

#### [学者名] — [攻击角度标题]
[2-3 句论证，含具体引用。]
```

在 `## Open Questions` 和 `## Output Opportunities` 之间插入：

```markdown
## Synthesis

### 与本库其他概念的关联

- [[相关卡片1]] — [1 句关联逻辑]
- [[相关卡片2]] — [1 句关联逻辑]

### 可迁移场景

- [场景 1]
- [场景 2]
```

## 攻击者选择原则

- OCR 卡的主题域覆盖广泛（一堂方法论、产品设计、个人修炼、科学决策等）
- 同一主题域下不同卡使用**不同的**攻击者，避免重复
- 优先使用已有卡片的攻击者（查看同 domain 下卡的 `## Constraints & Boundaries` 节）
- 标准方向：认知偏差（Kahneman）、复杂系统（Snowden）、组织社会学（Mintzberg）、反脆弱（Taleb）、创新（Christensen）等

## 验收

| # | 验收项 | 判定方式 |
|:--:|------|------|
| 1 | 每张卡有 `## Constraints & Boundaries` 节 + ≥2 H4 攻击者 | `grep "Constraints & Boundaries"` 命中 |
| 2 | 每张卡有 `## Synthesis` 节 + ≥2 `[[wikilink]]` | `grep "\[\["` 命中 ≥2 |
| 3 | 攻击者论证实质性（H4 下 ≥100 字符正文） | 人工抽检 |
| 4 | `kdo validate --v15 --card <id>` PASS | 终端 exit 0 |
| 5 | 不改动已有 Reusable Knowledge / Open Questions / Output Opportunities 内容 | diff 审查 |

## 不做什么

- **不要**重写 Reusable Knowledge（已有 LLM 产出，质量可接受）
- **不要**删除或修改 Open Questions
- **不要**修改 frontmatter（status 保持 enriched）

## 穿插规则

- 每做完 1 张卡 → 更新本文件进度表
- 每做完 5 张卡 → 通知欧阳锋抽检
- 每完成一个 Batch → 暂停，等待欧阳锋审查方向

## 进度表

| Batch | 总数 | 已完成 | 通过审查 | 备注 |
|:--:|:--:|:--:|:--:|:---|
| 1 | 5 | 5 | 5 | A+。Norman/Pye/Postman/Morozov/Papert/Orwell/Simon |
| 2+3 | ~40 | 31 | 待审 | 科学决策域清空。见下方 [[#🔍 欧阳锋审查（2026-05-23 Batch 2+3）]] |
| 4 | 50 | 0 | 0 | **洪七公正在做 VA 前置**，完成后交接给老顽童做 Critique+Synthesis |
| ↳ | ↳ | ↳ | ↳ | 详见 [[70_product/tasks/task-20260523-hongqigong-va-and-articles]] |
| 5 | 41 | 0 | 0 | 先评估，不盲目开工 |

---

## 🔍 欧阳锋审查（2026-05-23 Batch 2+3）

**31 张科学决策域 OCR 卡，整体达标，两点调整：**

### 调整 1：攻击者多样性（软约束）

当前 31 张卡中 Kahneman 13 次、Taleb 10 次，过于集中。**不需回炉全部 31 张**——质量达标的直接放行（如 `关键假设ABCD` Popper+Christensen、`稀缺机会窗口` Christensen）。只调整**纯 Kahneman+Taleb 组合的卡**，把其中一位替换为域内其他学者。

**同一域（科学决策）内，每 5 张卡至少引入 1 位新攻击者。** 可用池：

| 学者 | 攻击方向 | 示例卡 |
|:---|:---|:---|
| Popper | 证伪主义→"假设安全感" | 关键假设ABCD |
| Christensen | 颠覆创新→"公式在颠覆面前崩解" | 稀缺机会窗口 |
| Mintzberg | 涌现战略→"定量模型无法捕捉涌现" | 待用 |
| Snowden | Cynefin 复杂域→"公式在复杂域失效" | 待用 |
| Klein | 自然决策→"专家不靠公式做决策" | 待用 |
| Gigerenzer | 生态理性→"简单启发式胜过复杂公式" | 待用 |
| Thaler | 行为经济学→"公式忽视心理账户" | 待用 |
| Sterman | 系统动力学→"线性公式无法建模反馈循环" | 待用 |

### 调整 2：格式统一（硬约束）

- Critique 节标题统一为 `## Critique`（Batch 1 惯例）
- dont-use 段统一为 `### 不要用的场景`，每卡 ≥2 个场景
- 已有 `## dont-use`（英文）的卡，改为 `### 不要用的场景`
- 缺失 dont-use 段的卡，补上

### 放行标准

满足以下条件的卡**直接通过，不改**：
- 攻击者组合不全是 Kahneman+Taleb
- dont-use 段存在（中英文均可，内容实质性）
- ≥2 wikilinks + ≥2 Action Triggers

---

*欧阳锋 · 2026-05-23*
*基于洪七公 cross-review + 欧阳锋独立验证*
