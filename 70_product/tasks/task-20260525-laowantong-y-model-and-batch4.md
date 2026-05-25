---
title: "老顽童：y-model validator 修复 + OCR Batch 4 开工"
assigned_to: "老顽童 (Producer)"
priority: "P0"
created_at: "2026-05-25"
reviewer: "欧阳锋"
status: "in_progress"
depends_on: []
blocks: []
---

# 老顽童：y-model validator 修复 + OCR Batch 4 开工

## 背景

上一轮已完成：

- 单元模型域 7 张卡 ✅ 欧阳锋审查通过（A-，2 处小问题已告知）
- Part B VA 修复 14/14 ✅（#9 已改、#10 描述准确无需动、#14 已完成）
- OCR Batch 4 15 张卡的 Critique+Synthesis 已完成（7 张手写 ✅、8 张批量模板 ⚠️）

## 🔍 欧阳锋审查（2026-05-25）

### OCR Batch 4 — 8 张批量模板 ✅ 全部通过（A-）

| 卡 | 攻击者（旧→新） | VA引用Critique | VA引用OQ | 判定 |
|:---|:---------------|:-------------:|:--------:|:---:|
| 个人地图 | Kahneman→**Dewey** + Simon | ✅ 视觉/箭头 | ✅ 视觉/箭头/递进 | ✅ |
| 创业地图 | Kahneman→**Schön** + Simon | ✅ 视觉 | ✅ 箭头/模块/并列 | ✅ |
| 管理地图 | Kahneman→**Langlois** + Simon | ✅ 视觉/模块/并列 | ✅ 视觉/箭头/模块/递进 | ✅ |
| 进步大地图 | Kahneman→**Bowker/Star** + Simon | ✅ 视觉/箭头/模块 | ✅ F形/Z形/模块/递进 | ✅ |
| 高潜力成长者 | Kahneman→**Sontag** + Simon | ✅ 视觉/箭头 | ✅ 视觉/箭头 | ✅ |
| 十年修炼爬山 | Kahneman→**Sontag** + Simon→Pye | ✅ 视觉/递进 | ✅ 阅读路径/F形/模块/递进 | ✅ |
| 36计全套地图 | Kahneman→**Langlois** + Simon→Pye | ✅ 视觉/模块 | ✅ 模块/递进 | ✅ |
| 萃取总结 | Kahneman→**Bowker/Star** + Simon→Pye | ✅ 视觉/模块/布局 | ✅ 视觉/布局/递进 | ✅ |

**亮点**：8 张全部替换 Kahneman，5 位新攻击者全部启用（Dewey/Schön/Langlois/Bowker&Star/Sontag）。3 张超出最低标准，连 Simon 也换成了 Pye。Open Questions 全部重写为针对内容的实质性提问，非模板填空。Critique 和 OQ 均引用了 VA 描述的视觉结构。

### y-model validator ❌ 未修复

`yt-decision-y-model.md` 当前仍用 `## Constraints & Boundaries` 旧格式，**无 `### 外部攻击` 容器**——`#### Gary Klein` 和 `#### Daniel Kahneman` 直接挂在 `Constraints & Boundaries` 下。`kdo validate --v15` 必然 FAIL。

**修复方法**（同前）：
1. 将 `## Constraints & Boundaries` 改为 `## Critique`
2. 在 `####` 攻击者前插入 `### 外部攻击`
3. 核对格式与已 PASS 卡片（如 yt-decision-canvas）一致
4. `kdo validate --v15 --card yt-decision-y-model` 直至 exit 0

## 执行顺序

### Step 1：修 y-model validator（~10min，先做）

**目标**：`kdo validate --v15 --card yt-decision-y-model` 跑通 exit 0

**根因已定位**：当前 `####` 攻击者缺了 `### 外部攻击` 容器。Constraints & Boundaries 后直接接了 `### 内部局限` 和 `#### Gary Klein`，validator 找不到合法的 H3 heading。

**修复方法**：
1. 在 `### 内部局限` 之前插入 `### 外部攻击`，把所有 `####` 攻击者包进去
2. 确认格式与已 PASS 的卡片（如 yt-decision-canvas 等）一致
3. `kdo validate --v15 --card yt-decision-y-model` 直至 exit 0

> ⚠️ y-model 被引用 31 次，是跨域元框架。留一个已知 FAIL 会在后续批量验证时持续报警。

### Step 2：OCR Batch 4 — 15 张卡（做完 Step 1 后开）

#### 先做 7 张手写已有参照的（已有良好格式参照）

| # | 卡片 | 备注 |
|:--:|:---|:---|
| 1 | `ocr-一堂-个人修炼-全景图muse模型` | 手写模板，攻击者已到位 |
| 2 | `ocr-一堂-个人修炼-科学学习IPO-全景策略` | 同上 |
| 3 | `ocr-一堂-个人修炼-表达力火箭模型-执行武器库` | 同上 |
| 4 | `ocr-一堂y模型-科学成事道理` | 用户手动处理过，确认格式 |
| 5 | `ocr-一堂y模型实操工作流` | 同上 |
| 6 | `ocr-泛产品设计落地篇` | Batch 1-3 已完成级 |
| 7 | `ocr-预判模型` | 同上 |

#### 再做 8 张批量模板——需定点修补（按以下标准）

| # | 卡片 | 需修补 |
|:--:|:---|:------:|
| 8 | `ocr-一堂-地图-个人地图` | 3 项 |
| 9 | `ocr-一堂-地图-创业地图` | 3 项 |
| 10 | `ocr-一堂-地图-管理地图` | 3 项 |
| 11 | `ocr-一堂进步大地图` | 3 项 |
| 12 | `ocr-一堂个人地图高潜力成长者修炼全景图` | 3 项 |
| 13 | `ocr-一堂泛产品设计-十年修炼爬山地图` | 3 项 |
| 14 | `ocr-一堂泛产品设计36计-全套地图` | 3 项 |
| 15 | `ocr-萃取总结` | 3 项 |

### 修补标准（3 项）

#### 修补 1 / Critique 换 1 个攻击者（~10min/卡）

替换 Kahneman 或 Simon，从以下选一位，写一段针对该卡具体内容的攻击：

| 学者 | 攻击角度 | 适合卡片 |
|:---|:--------|:---------|
| Bowker/Star（《分类的威力》） | "分类行为的政治性"——谁有权定义这些分类？分类是否隐含价值观？ | 地图类、全景图 |
| Langlois（模块化系统边界） | "模块化的虚假独立性"——四大模块之间真有清晰边界吗？还是为了框架完整强切？ | 多模块并列图 |
| Dewey（《经验与自然》） | "工具理性的局限"——地图把学习问题工具化了，但学习本质是非线性、目的性的 | 成长路径图 |
| Schön（反映的实践者） | "行动中反思 vs 步骤化地图"——专家不按地图走，是在行动中即兴生成的 | 流程/工作流图 |
| Sontag（《疾病的隐喻》） | "框架的隐喻本身限制认知"——"修炼""进阶"等隐喻框定了想象空间 | 修炼地图类 |

#### 修补 2 / 补 1 条 Open Question（~5min/卡）

针对 VA 描述的视觉结构提问。例如进步大地图：
> "四大模块之间的箭头关系——是递进还是并列？框架中是否有模块间交互没画出来（如管理修炼的经验回流个人修炼）？"

#### 修补 3 / Synthesis 补 1 条引用 VA 结构的关联（~5min/卡）

例如：
> "这张卡的 Z 形阅读路径与 [[xxx]] 的线性结构形成对比，反映聚合思维 vs 发散思维的不同认知模式。"

### 时间紧张时的最低标准

至少完成 **修补 1**（换攻击者）。修补 2 和 3 可留到下一次统一提升批次。

## 验收

| # | 验收项 | 判定 |
|:--:|------|:----:|
| 1 | `kdo validate --v15 --card yt-decision-y-model` exit 0 | 终端 |
| 2 | 15 张卡全部有 `## Critique` 节 + ≥2 H4 攻击者 | grep |
| 3 | 批量模板 8 张卡：Kahneman/Simon 已替换为贴切攻击者 | 人工检查 |
| 4 | 替换后的攻击者不在同一域过去 5 张卡中出现过 | grep |
| 5 | 不改动已有 Reusable Knowledge / Open Questions / Output Opportunities | diff |

## 不做

- **不做** 单元模型域 2 处小修（那是欧阳锋本会话已记录，等下一轮统一修）
- **不做** VA #10（depth-ladder L3 四项描述）——已确认"图中确实未标注"，描述准确无需补
- **不做** VA #14（abcd-model frontmatter）——已完成
- **不做** OCR Batch 5（41 张低价值卡）——先评估再开工

---

*欧阳锋 · 2026-05-25*
