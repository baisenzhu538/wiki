---
id: sprint-9-cleanup-source-refs-query-triggers
title: "Sprint 9：修复 source_refs 空值 + query_triggers 污染"
status: completed
priority: P0
assigned_to: 黄药师
reviewer: 欧阳锋
domain: all
created: 2026-05-13
target: 2026-05-14
---

## 背景

Sprint 6 终审发现三个遗留问题：
1. **source_refs 空值**：57 张卡 `source_refs: []`，KF-020 违规
2. **query_triggers 污染**：Batches 3-4 的 query_triggers 被自动从 section headers 提取（如 "与一堂方法论的关系"、"从知道到做到的鸿沟"），非真实搜索词
3. **Constraints 模板化**：~20 张 entrepreneur 卡共用 boilerplate 三条（"信息损失"+"前提假设"+"知行鸿沟"），非该工具特有边界

## Phase 1：source_refs 空值修复（P0，先做）

### 范围

```
grep 'source_refs: \[\]' 30_wiki/concepts/yt-*.md
```

| 前缀 | 数量 |
|------|:----:|
| `yt-entrepreneur-*` | 20 |
| `yt-management-*` | 15 |
| `yt-model-*` | 7 |
| `yt-personal-*` | 7 |
| **其他 yt- 卡** | ~8 |
| **合计** | **~57** |

### 操作

每张卡的 source_refs 需指向实际存在的 `10_raw/sources/` 或 `10_raw/assets/yitang/` 文件：

1. 检查该卡对应的一堂课程——多数 entrepreneur/management/personal 卡源自 `10_raw/sources/一堂-课程地图精华串讲.md`
2. 如该卡有独立源文件（如 `一堂-个人修炼-时间管理必修课.md`），指向独立文件
3. 如无独立源文件，指向课程地图串讲
4. **绝不**指向 `00_inbox/`

### 验证

`grep 'source_refs: \[\]' 30_wiki/concepts/yt-*.md` → 0 hits

## Phase 2：query_triggers 重写（P1）

### 范围

Batches 3-4 共 ~40 张卡（entrepreneur + personal 非 panproduct）。

### 问题症状

以下类型的 "triggers" 无效：
- 从 `## Critique` / `## Constraints` headers 提取的句子
- "与一堂方法论的关系" / "关联卡片" / "关键概念" 等通用 section 名
- "从知道到做到的鸿沟" / "方法论的前提假设需要检验" 等 critique 文本

### 重写标准

每条 query_triggers 应满足：
- 用户可能实际输入的中文搜索词
- 5-10 条
- 包含：工具名/方法名 + 核心概念 + 同义词/别名 + 问题场景描述

**正确示例**（来自 `yt-personal-time-management`）：
```yaml
query_triggers:
  - 时间管理
  - 优先级管理
  - 高能量窗口
  - 深度工作
  - 保护时间块
  - 日历管理
  - 时间分配
  - L3战略层
```

**错误示例**（来自抽检发现的污染）：
```yaml
query_triggers:
  - 与一堂方法论的关系
  - 从知道到做到的鸿沟
  - 关联卡片
  - 关键概念
```

### 验证

欧阳锋随机抽 3 张卡，query_triggers 全部为真实搜索词。

## Phase 3：Constraints 去模板化（P1）

### 范围

~20 张 entrepreneur 卡 Constraints 节疑似使用相同模板。

### 筛选标准

优先修复满足以下条件之一的卡：
- 当前 Constraints 仅含 boilerplate 三条（"信息损失"+"前提假设"+"知行鸿沟"）
- 该工具在 domain 中有独特边界（与其他工具存在交叉/冲突/互补的边界）

### 操作

每张卡至少 1 条 **该工具特有的** boundary claim：
- 具体场景（什么时候这个工具不好用？）
- 失败模式（用了但失败了，典型症状是什么？）
- 条件依赖（需要什么前置条件？缺了什么会失效？）

### 不修的情况

如果该卡确实只是课程目录索引（无独立方法论），Constraints 可为空——但应在 body 中明确标注卡片性质。

## 不做

- ❌ 不升级 body 格式（已在 Sprint 6 完成）
- ❌ 不填 related 边（panproduct 域已在 Sprint 7-8 完成，非 panproduct 域留 Sprint 10）
- ❌ 不新增卡片

## 质量门禁

- [x] `grep 'source_refs: \[\]' 30_wiki/concepts/yt-*.md` → 0 hits
- [x] `grep '"00_inbox' 30_wiki/concepts/yt-*.md` → 0 hits（全局仅剩 paddleocr-skill.md）
- [x] 抽查 3 张 entrepreneur 卡 query_triggers → 全部真实搜索词
- [x] 抽查 3 张 personal 卡 query_triggers → 全部真实搜索词
- [x] 抽查 2 张 entrepreneur 卡 Constraints → 至少 1 条该工具特有边界

---

## 最终交付报告（2026-05-14 黄药师）

### Phase 1：source_refs 空值修复

| 指标 | 结果 |
|------|------|
| 修复前空值卡数 | 52 |
| 修复后空值卡数 | 0 |
| 引用模式 | 48 卡 → `10_raw/sources/一堂-课程地图精华串讲.md`；12 model 卡 → 额外补充 `10_raw/assets/yitang/` 对应图片 |
| KF-020: 00_inbox 引用 | 0 hits |

### Phase 2：query_triggers 重写

| 指标 | 结果 |
|------|------|
| 处理卡数 | 31（21 entrepreneur + 10 personal） |
| 污染类型 | section header 文本（"与一堂方法论的关系"/"关联卡片"等）、Claims 片段、Constraints 回音 |
| 替换后每卡条目 | 8-10 条真实中文搜索词 |
| 验证 | 全局 0 条污染残留 |

### Phase 3：Constraints 去模板化

| 指标 | 结果 |
|------|------|
| 处理卡数 | 20 张 entrepreneur 卡 |
| 原 Constraints | 全部 3 条完全相同模板（信息损失 + 前提假设 + 知行鸿沟） |
| 新增 | 每卡 1 条工具特有 `### 4.` constraint |
| 边界类型分布 | 前置条件 4、场景失效 4、典型失败模式 4、工具盲区 4、场景不适用 2、其他 2 |

### 质量门禁

- [x] `grep 'source_refs: []' 30_wiki/concepts/yt-*.md` → 0 hits ✅
- [x] `grep '"00_inbox' 30_wiki/concepts/yt-*.md` → 0 hits ✅
- [x] 抽查 3 张 entrepreneur 卡 query_triggers → 全部真实搜索词 ✅
- [x] 抽查 3 张 personal 卡 query_triggers → 全部真实搜索词 ✅
- [x] 抽查 2 张 entrepreneur 卡 Constraints → 至少 1 条该工具特有边界 ✅
- [x] `python3 -m kdo lint` → 0 errors, 350 warnings（全部为旧卡/非 yt 卡） ✅

### 已更新文件

| 类别 | 数量 | 操作 |
|------|:----:|------|
| yt-entrepreneur-*.md | 21 | source_refs + query_triggers + Constraints |
| yt-management-*.md | 15 | source_refs |
| yt-model-*.md | 12 | source_refs |
| yt-personal-*.md | 10 | source_refs + query_triggers |
| yt-system-course-catalog.md | 1 | source_refs |

### 已知问题（非阻塞）

- kdo lint 的 350 warnings 全部来自非 yt 卡（调研报告、中文名文件）的历史问题
- 管理域和系统域卡片的 query_triggers 未在本次 sprints 范围内（Sprint 9 范围限定 entrepreneur + personal non-panproduct）
- 管理域和系统域卡片的 Constraints 未在本次 sprint 范围内

---

## 欧阳锋终审结论（2026-05-14）

### 格式门禁

| 门禁 | 结果 |
|------|:--:|
| `source_refs: []` yt-* 卡 | ✅ 0 hits（52 张已修） |
| `00_inbox` yt-* 卡 | ✅ 0 hits |

### 理解门禁：query_triggers 抽检

| 卡 | 判定 | 点评 |
|----|:--:|------|
| `yt-entrepreneur-lean-validation` | ✅ | "低成本验证""MVP""精益创业""pivot决策"——全部真人会搜 |
| `yt-entrepreneur-needs-analysis` | ✅ | "JTBD""拆推评算""六层冰山模型""四种力量模型"——精准 |
| `yt-entrepreneur-five-step-method` | ✅ | "一堂五步法""科学创业""五步法框架"——干净 |
| `yt-personal-ai-capability` | ✅ | "提示词工程""人机协同""如何与AI协作""提示词怎么写"——场景化搜索 |
| `yt-personal-y-model-practice` | ⚠️ 偏弱 | 混入了"Y模型四最""核心动词"等内部术语，但核心检索词可用 |
| `yt-personal-checklist-notes` | ✅ | "清单体笔记""销冠小抄""三阶清单体系""如何做笔记"——好 |

**与 Sprint 6 对比**：Sprint 6 的 triggers 是 100% section headers 污染（"与一堂方法论的关系""关联卡片"），Sprint 9 修复后 5/6 全干净、1 张可接受。**质量跃升明显。**

### 理解门禁：Constraints 抽检

| 卡 | 新增 #4 constraint | 判定 |
|----|-------------------|:--:|
| `yt-entrepreneur-business-growth` | 增长方法论在 PMF 前失效——在错误方向加速，浪费验证窗口 | ✅ |
| `yt-entrepreneur-scientific-method` | 可证伪性 × 时间窗口悖论——长周期判断验证赶不上机会窗口 | ✅ |

两卡的新增 constraint 均满足三个信号：
- 有具体场景（PMF 未确认 / 品牌+文化+技术路线验证以年为单位）
- 有可验证的失败症状（增长数据短暂拉升后塌陷 / 等实验回来窗口已关）
- 有替代方案或补救路径（退回五步法验证模块 / 标注低置信度+第一性原理补充）

### 裁决

**通过 ✅。** Sprint 9 三阶段全部完成，Sprint 6 遗留的三个质量问题已修复：
- source_refs 空值：52 → 0
- query_triggers 污染：31 张已重写，5/6 抽检 clean
- Constraints 模板化：20 张各新增 1 条工具特有边界

**未覆盖的已知残留**（不阻塞）：
- 管理域/系统域 query_triggers 未重写（Sprint 9 范围限定 entrepreneur + personal）
- 管理域/系统域 Constraints 未去模板化

以上两项纳入后续 sprint 按需处理，不单独建任务。
