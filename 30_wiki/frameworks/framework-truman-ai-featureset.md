---
id: framework-truman-ai-featureset
title: Truman 自用 AI FeatureSet 四层模型（精简版）
type: framework
status: draft
author: 老顽童
reviewed_by: pending
confidence: 0.8
trust_level: medium
domain:
- ai-collaboration
- strategy
aliases:
- AI FeatureSet
- Truman自用FeatureSet
- FeatureSet四层模型
- 用Feature思维刻意练习
source_refs:
- 00_inbox/AI-study/一堂-AI学习-truman自用的AI FeatureSet_paddle_ocr.txt
- 10_raw/sources/feature-periodic-table-v1.0.json
related:
- '[[framework-truman-feature-layered-system]]'
- '[[framework-kdo-modeling-methodology]]'
discoverable_by:
- AI FeatureSet
- 四层模型
- 刻意练习
- Feature思维
created_at: '2026-08-28'
updated_at: '2026-08-28'
version: v0.1
tags:
- audience:general
- scene:learning
- skill-level:intermediate
- source-person:truman
- method:feature-thinking
---

# Truman 自用 AI FeatureSet 四层模型（精简版）

> **定位声明**：本卡是 [[framework-truman-feature-layered-system]]（Feature 周期表 100 项完整版，L0-L5 分层）的**精简自用版**——Truman 个人高水平刻意练习用的 30+ 项四层视角。查完整周期表/点菜式调用走主卡与 `kdo-tools/feature_menu.py`；本卡回答「高手自己日常用哪几层哪几项」。
> **素材说明**：源为 OCR 转录（`一堂-AI学习-truman自用的AI FeatureSet_paddle_ocr.txt`），噪声已对照 Feature 周期表 v1.0 逐项还原；拿不准处标 ⚠️AI 推断。

## 四层结构总览

| 层 | 管什么 | 子域 | 项数 |
|:--|:--|:--|:--|
| 一、LLM 层（大模型层） | 模型与提示词本身 | 选模型 / 提示词 | 10 |
| 二、数据层 | 给模型喂什么、怎么喂 | 上下文控制 / 增强数据 | 13 |
| 三、协作层 | AI 作为高阶角色怎么配合 | 反向系列 / 拆分任务 | 10 |
| 四、效率层 | 流程化与规模化 | 做工作流 / 效率提升 | 5+ |

## 一、LLM 层（大模型层）

**选模型**
1. 使用不同模型（周期表：模型选择）
2. 使用不同版本
3. 模型的参数（周期表：温度/Top-K/Top-P/频率惩罚/随机种子）
4. 同时抽卡（周期表：同时抽点测试——同 prompt 多跑几次挑最好）
5. 模型组合

**提示词**
1. 提示词迭代（OCR 原文"送代"→迭代，周期表：Prompt 版本管理）
2. 风格设定（周期表：语气风格/优化词语）
3. 多轮对话
   - 赋予角色（OCR"歌子角色"⚠️AI 推断，周期表：赋予角色）
   - 用户角色（周期表：用户身份）
   - 任务要求
   - 背景信息
   - 负面限制
   - 输出要求
   - 行文规则

## 二、数据层

**上下文控制**
1. 更大上下文（周期表：最大上下文长度）
2. 渐进式披露
3. 复制粘贴
4. 分段标注（OCR"分展标注"⚠️AI 推断）
5. 重点标注
6. 主动摘要（OCR"主动搞要"⚠️AI 推断）
7. 使用 Skill（周期表：用自然语言封装 Skill）
8. 数据分层

**增强数据**
1. 给案例集（周期表：Few-shot 示例）
2. 专家资料（周期表：给 DataPack）
3. 用多模态
4. 联网搜索
5. 接入 API（周期表：API 调用）
6. 使用 RAG（周期表：RAG 检索增强）

## 三、协作层

**AI 高阶角色 · 反向系列**（让 AI 反向驱动你）
1. 反向提示
2. 反向教我（OCR"反向数我"→周期表实有"反向教我"，直接命中还原）
3. 反向采访
4. 反向记录

**拆分任务**
1. 拆解环节
2. 剥离场景（OCR"别离场景"→周期表：剥离最小场景）
3. 多轮确认
4. 使用 CoT（链式思考）
5. 使用 CoV（视觉链式思考）
6. 使用 ReAct（周期表：ReAct 模式）

## 四、效率层

**做工作流**
1. 设计工作流
2. 分支循环（OCR"分支环"⚠️AI 推断；周期表相邻项：新开窗分支测试）
3. 使用插件（周期表：插件调用）

**效率提升**
1. 模型匹配（OCR"楼型正配"⚠️AI 推断——任务书已预判；语义=按任务配模型，周期表：能换模型找最好/快慢切换）
2. 并行调度

## Synthesis

四层不是并列清单而是依赖链：**LLM 层是地基**（模型和提示词没玩熟，上层都是空转）→ **数据层是杠杆**（同一个模型，喂法决定产出上限——上下文控制+增强数据 13 项是全表最密的子域）→ **协作层是范式转移**（反向系列=让 AI 驱动你而不是你驱动 AI，这是"高阶角色"和"工具"的分水岭）→ **效率层是规模化**（工作流把前三次的成功固化成可复用资产）。刻意练习的顺序暗示：不要跳层——先在 LLM 层把"同时抽卡/参数/组合"练成直觉，再谈工作流（这套"先 X 再 Y"的依赖链思路与 [[framework-kdo-modeling-methodology]] 的组件建模同源）。与 100 项完整版的关系：本版是 Truman 自用高频子集，四层视角是入口叙事，[[framework-truman-feature-layered-system]] 才是全景。

## 不要用的场景（When NOT to Use）

| 场景 | 原因 | 替代 |
|:--|:--|:--|
| 查某 Feature 的精确定义/分层（L0-L5） | 本卡是精简视角，项名有 OCR 还原误差 | 主卡 [[framework-truman-feature-layered-system]] + `feature_menu.py` |
| 当作 30+ 项的封闭全集 | "等"字结构——OCR 原文有省略，效率层项数明显少于其他层 | 以周期表 100 项为全集，本卡为高频子集 |
| 新手按四层自学 AI | 本卡无操作细节，只有项名 | 配合完整版分层路径（L0 起步） |

## 失败模式

| 失败模式 | 真实信号 | 修复动作 |
|:--|:--|:--|
| OCR 噪声当原文引用 | 引用本卡项名与周期表对不上 | 以周期表 100 项为准对账；本卡 ⚠️ 标记处即风险点 |
| 拿精简版当全集回答 | 回答"Truman FeatureSet 有哪些"时只列 30+ 项 | 先声明"这是精简自用版"，指主卡给全集 |
| 跳层练习 | 没练过同时抽卡就在设计工作流 | 回 LLM 层补地基（Synthesis 的依赖链） |

## Critique

1. **OCR 单源风险**：全卡源自单张图的一次 OCR，虽对照周期表还原，仍有 4 处 ⚠️AI 推断未获原文证实——置信度上限受此约束。
2. **效率层明显单薄**（5+ 项 vs 数据层 13 项）：可能是原图截取不全，也可能是 Truman 自用版本就如此——无法从现有素材分辨，如实标注。
3. **四层分类法与周期表 L0-L5 分层是两套正交维度**（主题层 vs 难度层），本卡未做映射——映射表是有价值的后续工作（可挂主卡迭代）。

## Action Triggers

| 触发条件 | 动作 |
|:--|:--|
| 用户问"Truman 怎么用 AI/Feature 思维怎么练" | 给四层图 + 指主卡查单项细节 |
| 用户问某具体 Feature | 直接查 [[framework-truman-feature-layered-system]]/`feature_menu.py`，不用本卡 |
| 新素材涉及 Feature 周期表更新 | 改主卡和 JSON 底表，本卡只跟随不动 |

---

*v0.1 · 2026-08-28 · 老顽童按 #571 产：OCR 源对照 Feature 周期表 v1.0 还原，⚠️ 标记 4 处推断待原文证实*
