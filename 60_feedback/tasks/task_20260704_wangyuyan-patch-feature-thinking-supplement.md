---
id: task_20260704_wangyuyan-patch-feature-thinking-supplement
type: task
status: pending_review
assignee: claude
reviewer: 欧阳锋
priority: P2
created_at: 2026-07-04
updated_at: '2026-07-04T17:55:43.438672+00:00'
source_task: task_20260704_laowantong-ai-feature-thinking-concept
related:
- '[[concept-yihang-ai-feature-thinking]]'
- '[[tool-Truman-Feature特性层训练法]]'
- '[[tool-Truman-AI能力分层学习路径]]'
---

# 任务 #83：#74 修补——Feature 思维完整操作定义

## 修补目标

#74 产出 concept 卡 + 2 张重写卡后，补充口述稿中的完整操作定义和两个遗漏案例。

## 原始素材

口述稿 L1402-1451：

**Feature 的操作定义**：
- "可操作的原子化的最小技术单位"（L1426）——能测、能 A/B 对比、不能继续拆
- "拆完之后一共也就几十个特性"（L1427）——跨工具的
- "每一个特性都有可能让你实现 A/B 测试的结果提升"（L1418）

**Feature 与 Skill 的关系**（L1428-1429）：
- "它跟 skill 是两套东西，skill 就是一个封装逻辑"

**两个遗漏案例**：

| 案例 | 口述稿位置 | Feature | 效果 |
|:---|:---|:---|:---|
| 豆包做图：文生图 vs 代码画图 | L1348-1376 | 技术路线选择（指定 Midjourney） | 莹莹用代码画 4 小时全是秃头；Truman 加一句"用 Midjourney"就出好图 |
| 龙虾 vs 爱马仕 | L1432-1436 | Feature 对比 | "龙虾火是因为有三四个核心特性，爱马仕又多了那么一两个" |

## 修补内容

**concept-yihang-ai-feature-thinking**：
- 补充 Feature 的完整操作定义（原子化 / 可测 / 跨工具）
- 补充 Feature vs Skill 区分段落
- 补充豆包和龙虾两个案例

## 验收标准

- concept 卡更新后 `kdo pre-submit` PASS
- 含"原子化 / 可测 / 跨工具"定义
- 含 Feature vs Skill 区分
- 含至少一个新增案例
- 欧阳锋终审通过

## 依赖

- #74 完成（3 张卡已交付）
