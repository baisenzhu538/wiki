---
id: data-curator-role-division
title: Data Curator Skill — 五角色分工方案
type: decision
status: draft
domain:
- master
tags:
- '#domain/knowledge-management'
- '#method/evaluation-method'
created_at: 2026-05-31
updated_at: 2026-05-31
target_roles:
- 用户（决策者）
- 欧阳锋（Architect）
- 黄药师（Builder）
- 老顽童（Producer）
- 洪七公（Multimodal）
supersedes: null
related:
- three-party-data-alignment
- plan_20260531_data-curator-v1.3
- huangyaoshi-data-alignment-response
- ouyangfeng-data-alignment-response
author: legacy
source_context: KDO internal record
source_refs: []
reviewed_by: pending
confidence: 0.6
trust_level: low
---

# Data Curator Skill — 五角色分工方案

## 分工逻辑

6+1 管线不是一个角色从头做到尾的。每个环节需要的核心能力不同：

```
A 预判 → 需要业务理解（用户 + 欧阳锋）
D 识别 → 需要全库视野（欧阳锋 + 黄药师）
U 收集 → 需要多模态处理（洪七公）
C 处理 → 需要管线建设（黄药师）+ 内容生产（老顽童）
I 使用 → 需要管线建设（黄药师）
T 反馈 → 需要审查能力（欧阳锋）+ 管线建设（黄药师）
治理   → 贯穿全程（全员）
```

---

## 黄药师（Builder）— 基础设施层

**为什么是他**：脚本、模板、注册表、state.json 扩展。KDO CLI 的开发者。所有其他角色依赖他建的管线。

| 环节 | 具体产出 | 依赖 |
|------|---------|------|
| C：真原子 chunk 引擎 | `chunk_cards.py` 重写 — 主张/事实/规则级切分（30-200字/块），替换 heading 级切分 | — |
| C：萃取指南模板 | `extraction_guide` schema + 生成逻辑 + chunk 子类型注册 | — |
| C：暗知识六字段模板 | `dark-knowledge` card type schema + frontmatter 定义 | — |
| C：标签注册表 v2 | `tag-registry.yaml` 扩展 — 卡属性层（5-8个）+ 块属性层（主要维度池） | 等用户样例到 |
| C：自动标注逻辑 | `tag_cards.py` 重写 — AI 自动标注块属性 + 人工确认机制 | 标签注册表 v2 |
| U：升仓决策逻辑 | inbox → wiki 的价值预判规则 + 代际标记（data_generation） | — |
| I：使用深度标记 | `usage_depth` 字段 + 卡/块级别标记 | — |
| T：反馈闭环 | `kdo feedback` → 自动更新卡片标注 → 回到预判的闭环机制 | — |
| 治理：state.json 扩展 | chunks 字段、data_generation 字段、expiry 字段 | — |
| Schema 更新 | `concept.yaml` 加 `dark-knowledge` type + `data_generation` + `value_tier` + `usage_depth` | — |

**执行接口**：Windows PowerShell，顺序执行。

---

## 洪七公（Multimodal）— 粗加工入口层

**为什么是他**：管线的最前端。口述稿里有大量截图、框架图没有 OCR。图片不转文字，后面的所有人吃不到这些数据。

| 环节 | 具体产出 | 素材来源 |
|------|---------|---------|
| U：inbox 图片批量 OCR | 用本地 PaddleOCR 把 `00_inbox/` 下 PNG/JPG 全部转文字 | `00_inbox/design/`、`00_inbox/AI-study/` |
| U：视觉资产标注 | 图片本身的视觉维度标签（颜色、构图、风格、信息密度） | 同上 |
| U：多模态数据入库 | OCR 结果 + 原图链接 → 存为 inbox 素材，标记 `data_generation: original` | OCR 输出 |

**执行接口**：飞书 Hermes agent。从 dashboard 领任务。

**铁律**（来自 P-7 踩坑）：新域素材消化第一步 → 扫描文件夹 → 如有 PNG/JPG，**强制 OCR 全部** + **人工抽检 20%（至少 5 张）**。如果抽检识别率 < 80%，退回换方案（如先人工筛选清晰图片再 OCR），不得让低质 OCR 污染下游管线。

---

## 老顽童（Producer）— 内容生产层

**为什么是他**：暗知识卡和萃取指南需要深度内容判断。脚本自动切分打标，但"这条纠偏的核心教训是什么"、"这组数据的方法论骨架是什么"——需要人的理解。老顽童是产能主力，擅长卡片量产。

### 第一优先级：已完成域的反刍——补齐暗知识

| 任务 | 素材 | 产出类型 | 预估量 |
|------|------|---------|:------:|
| 纠偏暗知识卡 | `20_memory/corrections.md`（12条） | `dark-knowledge` | ~12 张卡 |
| 失败模式暗知识卡 | `90_control/failure-modes.md`（22种） | `dark-knowledge` | ~22 张卡 |
| 踩坑暗知识卡 | `.agent/pitfalls.md`（15条） | `dark-knowledge` | ~15 张卡 |
| 审查意见暗知识卡 | `70_product/tasks/` 各任务文件 | `dark-knowledge` | 按需 |

### 第二优先级：萃取指南——从一组卡提炼方法论

| 任务 | 素材 | 产出 |
|------|------|------|
| Design 域萃取指南 | `aigc设计基础01` + `aigc设计师实操培训01` + `aigc文创案例设计课` | "月白 AI 设计方法论萃取指南" |
| 决策域萃取指南 | `master-decision-hygiene` + `master-cognitive-bias-checklist` + `master-first-principles` | "决策卫生核心骨架" |
| 单元模型域萃取指南 | `yt-decision-y-model` + 相关 OCR 卡 | "Y模型方法论萃取指南" |

### 第三优先级：口述稿暗知识萃取

> ⚠️ 口述稿时间窗口短（讨论热度随时间流失），虽排 P3 但**不应拖太久**。建议 corrections.md 试点通过后 1-2 周内启动。 — 欧阳锋

| 任务 | 素材 | 产出 |
|------|------|------|
| Truman 工作流暗知识 | `00_inbox/AI-study/AI数据/` 四篇口述稿 | 工作流/工具用法/体悟金句 → `dark-knowledge` |
| 月白工作流暗知识 | `00_inbox/design/` 口述稿 | NotebookLM 用法/图层管理/团队协作教训 → `dark-knowledge` |

### 暗知识卡模板（六字段，替代三步编译法）

```markdown
## 原始表述
> [直接引用原话]

## 使用场景
[什么时候用？具体场景，不要泛化]

## 操作方法
[怎么做？步骤级。检验标准：另一个人读完后能照着复现]

## 适用边界
[什么时候不适用？反例是什么？]

## 为什么值钱
[为什么 AI 训练语料里没有这条？]

## 与其他知识的关联
[链接到概念卡、工具卡、其他暗知识卡]
```

**执行接口**：飞书 Hermes agent。任务写入 `70_product/tasks/laowantong-next-tasks.md`。

---

## 欧阳锋（Architect）— 审查层

**为什么是他**：新框架下审查标准变了。以前审"格式对不对"，现在审"暗知识补没补、萃取得对不对、块标注准不准"。

### 审查清单

| 审查项 | 标准 | 退回级别 |
|--------|------|:--------:|
| **暗知识卡** — 六字段完整 | 原始表述有引用、操作方法是步骤级（可复现）、使用场景不是泛化描述 | P1 |
| **暗知识卡** — 纠偏/决策理由/关键约束 | 这些暗知识是否真的能纠正 AI 行为？漏了 P0 类型的暗知识？ | P0 |
| **萃取指南** — 统领性 | 是否真的提炼了这组数据的方法论骨架？还是 Condense 换了个名字？ | P0 |
| **萃取指南** — 可操作性 | 读完指南后，AI 的产出风格/质量是否明显提升？ | P1 |
| **块级标注** — 多维视角 | audience / perspective / platform 至少各一？是否覆盖了"中医怎么说+西医怎么说"这种多视角？ | P1 |
| **块级标注** — 准确性 | AI 自动标注的结果，抽查 20%（每批至少查 1 张卡的 5 块） | P2 |
| **治理** — 代际标记 | data_generation 字段是否已填？AI 叠加数据是否降低优先级？ | P1 |
| **治理** — 全链路合规（放行前最后确认） | data_generation / value_tier / expiry / rights 各阶段字段是否已填？AI 叠加数据是否标注并降权？ | P1 |

### 退回分级标准（已与黄药师对齐）

| 级别 | 定义 | 处理 |
|:----:|------|------|
| **P0** | 纠偏/决策理由/关键约束遗漏 | 必须退回，修完再审 |
| **P1** | 重要金句/体悟/工具用法遗漏 | 退回 + 审查通过附条件（fix list），下一 session 未修则升级 P0 |
| **P2** | 边缘知识/格式/措辞问题 | 打标注，不卡流程 |

### 防退化的硬规则

- P1 "附条件通过"的 fix list 必须在**下一个 session** 内关闭
- 逾期未关闭 → 自动升级为 P0，阻塞后续批次
- 连续 3 次同一类型的 P1 → 升级为 P0

**执行接口**：Obsidian Claudian 插件。审查结论写入对应任务文件。

---

## 用户（决策者）— 方向层

| 决策 | 说明 |
|------|------|
| 宏观预判 | 哪些域是 KDO 长期战略方向？一年的数据积累重点？ |
| 暗知识优先级 | 纠偏 / 失败模式 / 口述稿 / 萃取指南，先推哪个？ |
| 标签维度取舍 | 朋友的样例到了之后，哪些维度保留、哪些砍掉？ |
| 湖仓升仓节奏 | inbox 素材处理频率？全量还是分批？ |

---

## 协作流程全景

```
用户（定方向）
  ↓
洪七公（OCR入口）→ 图片→文字，进湖（00_inbox/）
  ↓
黄药师（建管线）→ 升仓决策 → 真原子切分 → 自动打标
  ↓
老顽童（产内容）→ 暗知识卡编写 → 萃取指南撰写
  ↓
欧阳锋（审质量）→ 六字段审查 → 萃取指南审查 → 块标注抽查 → 退回或放行
  ↓
黄药师（反馈闭环）→ kdo feedback → 更新标注 → 回环到预判
```

**关键约束**（来自 AGENTS.md 禁止清单）：
- 角色之间不互相派活，都通过欧阳锋中转
- 老顽童领任务从 `laowantong-next-tasks.md`，不自己翻 inbox 找活
- 洪七公领任务从 `dashboard.md` 洪七公区，产出写入固定输出路径

**技术直连通道**（欧阳锋补充）：
- 上下游依赖的角色允许直接对接（如黄药师↔老顽童确认 schema 格式兼容、黄药师↔洪七公确认 OCR 输出格式）
- 这种对接限于**技术兼容性确认**，不涉及任务指派
- 任务指派和审查结论仍必须通过欧阳锋

---

*黄药师 · 2026-05-31*
