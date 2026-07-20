---
name: content-production
description: 内容生产总入口——Candy九步法：从素材到可交付内容
version: 1.0.0
author: 黄药师
license: MIT
platforms: [cli, feishu]
metadata:
  hermes:
    tags: [内容生产, 逐字稿, 写作, Candy, 九步法]
    related_skills: [content-production]
---

# Content Production（内容生产总入口）

Candy 逐字稿九步法。核心洞察：好内容不是 AI 替你写出来的，是你把判断、经历、表达一层层喂给 AI，再不断校准出来的。

## Constraints

<hard_limits>
- 前 3 步（参考系/定位/框架）占 50% 以上时间。不急着写
- 差异化优先：不和已有内容打架
- AI 是协作者，方向感必须是人的
</hard_limits>

## 九步 Pipeline

```
Step 1-2: 定位 ──→ /content-production-positioning
Step 3-6: 草稿 ──→ /content-production-draft
Step 7-8: 润色 ──→ /content-production-polish
Step 9:   协作 —— 贯穿全程：人定方向，AI 执行
```

## 意图分类

| 问题 | 路由到 |
|:--|:--|
| "这篇东西凭什么存在？" | `/content-production-positioning` |
| "结构怎么搭？案例怎么放？" | `/content-production-draft` |
| "写完了但读起来像 AI" | `/content-production-polish` |
| 完整生产 | Pipeline 全流程 |

## 五大关键原则

1. **不急着写**：前 3 步占 50% 时间
2. **差异化优先**：做"只有你能做的东西"
3. **骨架>文采**：框架不成立，任何文字都是浪费
4. **案例逼出观点**：案例先到位，观点自然浮现
5. **配图是结构**：每张图回答一个问题

## 参考卡片
- `framework-candy-transcript-workflow` — 九步法
- `concept-candy-ai-as-collaborator` — AI 是协作者
- `tool-candy-positioning-canvas` — 定位画布
- `tool-candy-oral-polish` — 口语化润色

## KDO 卡片质量门禁（按类型）

> 详见 `references/kdo-card-quality-gates.md`。生产 KDO 卡片时，除 `kdo pre-submit` 机械检查外，还需逐卡满足类型专属要求：
> - **dk 卡**：必须有 `## Critique` section
> - **tool 卡**：`related` ≥ 5
> - **所有卡**：必须有 `diagnostic_signals` 字段、`reviewed_by: pending` 占位
> - **提交前**：检查同 ID 文件是否残留在错误目录
