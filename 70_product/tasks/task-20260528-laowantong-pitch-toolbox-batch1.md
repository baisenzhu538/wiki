---
title: "老顽童：路演工具箱 Batch 1 — 故事化+数字化+比喻化"
assigned_to: "老顽童 (Producer)"
priority: "P1"
created_at: "2026-05-28"
reviewer: "欧阳锋"
status: "in_progress"
depends_on: []
blocks: []
---

# 老顽童：路演工具箱 Batch 1 — 故事化+数字化+比喻化

## 背景

管理工具箱（F1 + T1-T8）已全部完成 ✅，欧阳锋审查 A- ✅。

**下一域：路演工具箱（个人路演）**。该域现有：

- 框架卡：`yt-model-personal-pitch-toolkit`（个人路演工具箱总览）
- 10 张技巧卡，全部在 `30_wiki/concepts/`，`type: tool`，旧 concept 格式

与之前的单元模型域工具化相同——**格式转换 + 攻击者补全 + Synthesis**。概念内容已成熟（黄药师 enriched），不需要重写主张，只需套工具卡格式并补 Critique 攻击者。

**Batch 1 选 3 张最核心的技巧**：

| 卡 | 路径 | 核心价值 |
|:--|:-----|:---------|
| 故事化 | `yt-pitch-storytelling` | 最通用的说服技巧——"故事比道理好用十倍" |
| 数字化 | `yt-pitch-quantification` | 一锤定音型——数字让人默认"这是事实" |
| 比喻化 | `yt-pitch-metaphor` | 让复杂概念秒懂——"一比喻用户就懂了" |

---

## 前置：T6/T7/T8 善后（必须优先做，~15min）

在上次审查结果 [[task-20260528-laowantong-mgmt-toolbox-batch3]] 末尾写了 2 项顺手修：

### 1. 补 Synthesis

3 张卡 `## Critique` 与 `## Action Triggers` 之间缺 `## Synthesis`。内容参考旧 concept 版的 Synthesis 迁移：

| 卡 | 旧 Synthesis 位置 | 关键内容 |
|:--|:-----------------|:---------|
| T6 | `30_wiki/concepts/yt-tool-project-health-radar.md` L261-282 | 关联卡片 8 条 + 不要用的场景 3 条 |
| T7 | `30_wiki/concepts/yt-tool-onboarding-90day.md` L303-321 | 关联卡片 7 条 + 不要用的场景 3 条 |
| T8 | `30_wiki/concepts/yt-tool-equity-checklist.md` L323-344 | 关联卡片 8 条 + 不要用的场景 3 条 |

**做法**：从旧 concept 版复制 Synthesis 内容，适配到新工具版。关联卡片中的 wikilinks 保留，删除已不相关的条目。

### 2. 旧 concept 卡改 redirect

`30_wiki/concepts/yt-tool-{project-health-radar,onboarding-90day,equity-checklist}.md` 改为 redirect 存根：

```markdown
---
id: yt-tool-xxx
title: 'XXX'
type: tool
status: redirect
---

> 本卡已迁移至 [[30_wiki/tools/yt-tool-xxx]]。
>
> 原文内容请访问目标页面。
```

---

## Batch 1：路演工具箱 — 3 张卡

### A. 格式转换

当前格式（concept 格式，在 `30_wiki/concepts/`）：

```
## Summary
## Claims
### 定义与价值
### 四个子策略
## Constraints & Boundaries
## Critique（可能有）
## Synthesis
## Action Triggers
```

目标格式（工具格式，写入 `30_wiki/tools/`）：

```
## Summary
## 进入标准（When to Use）
## 操作步骤（Step-by-Step）
### [步骤名]
1. xxx
2. xxx
## 退出标准（When to Stop）
## Critique
### 内部局限
### 外部攻击
#### [学者] — [标题]
[2-3 句实质性论证 + 紧迫感]
## Synthesis
### 关联卡片
### 不要用的场景
## Action Triggers
```

**转换规则**：

| 旧字段 | 新位置 |
|--------|--------|
| `## Summary` | 保留 |
| `## Claims > ### 定义与价值` | 精简后移入 Summary 第二段 |
| `## Claims > ### 四个子策略` | 展开为 `## 操作步骤` |
| `## Constraints & Boundaries` | 有用的内容并入 `### 内部局限`，删除空节 |
| `## Critique`（已有内容） | 保留并检查是否需要扩展 |
| `## Synthesis` | 保留并适配 |
| `## Action Triggers` | 保留 |

### B. 补攻击者

每张 concept 卡当前缺少 `## Critique > ### 外部攻击`（或只有内部局限）。需要从相关学术/行业领域寻找攻击者：

| 技巧卡 | 建议攻击者方向（每组 2 位） |
|:------|:--------------------------|
| **故事化** | Paul Zak（神经科学——好故事触发催产素，但操纵情感有伦理边界）+ Chip Heath（《让创意更有黏性》——故事的记忆优势 vs 故事忽略数据和逻辑的陷阱） |
| **数字化** | Hans Rosling（数据素养——数字让"事实"显得权威但可能误导）+ Dan Ariely（《怪诞行为学》——数字锚定效应：听众对数字的信任可能被第一个数字操纵） |
| **比喻化** | George Lakoff（认知语言学——比喻塑造思维，但也固化偏见）+ Elisabeth Camp（隐喻哲学——比喻让复杂概念易懂但也过度简化） |

**攻击者论证要求**（参考管理工具箱的展开标准）：
- 引用学者的核心研究成果
- 说明这个攻击如何针对你的工具卡的具体主张
- 包含 1 个"紧迫感"问题——让使用者睡不着觉的那种
- 不换攻击者（选定后就固定，后续 batch 同样方向）

### C. 验证

每张卡完成后：

```bash
kdo validate --v15 --card yt-tool-pitch-storytelling
kdo validate --v15 --card yt-tool-pitch-quantification 
kdo validate --v15 --card yt-tool-pitch-metaphor
```

三张全部 PASS 后通知欧阳锋审查。

---

## 执行顺序

```
Step 1: T6/T7/T8 补 Synthesis      ← 先做，~15min
Step 2: T6/T7/T8 旧卡 redirect     ← ~5min
Step 3: pitch-storytelling 转换     ← 格式 + 攻击者
Step 4: pitch-quantification 转换   ← 格式 + 攻击者
Step 5: pitch-metaphor 转换        ← 格式 + 攻击者
Step 6: kdo validate --v15         ← 全部 PASS 后通知审查
```

## 验收

| # | 验收项 | 判定 |
|:-:|------|:----:|
| 1 | T6/T7/T8 Synthesis 已补回 | grep `## Synthesis` 各卡均有 |
| 2 | T6/T7/T8 旧 concept 卡已改为 redirect | status=redirect |
| 3 | 三张路演卡在 `30_wiki/tools/`，tool 格式完整 | 路径检查 |
| 4 | 每卡 Critique 有 2 位外部攻击者，各 ≥2 句 + 紧迫感 | 人工审查 |
| 5 | `kdo validate --v15` 全部 PASS | exit 0 |
| 6 | 不破坏已有内容（Claims 内容迁移而非删除） | diff |

## 不做

- **不做** 非 Batch 1 的路演卡（故事化/数字化/比喻化之外的 7 张等下一批）
- **不做** 框架卡 `yt-model-personal-pitch-toolkit` 的修改（在后续批次一起做）
- **不做** VA 视觉分析（非视觉卡）
- **不做** `yt-decision-*` 域的路演关联（专注路演域自身）

---

*欧阳锋 · 2026-05-28*
