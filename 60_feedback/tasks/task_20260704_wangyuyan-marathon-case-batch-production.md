---
id: task_20260704_wangyuyan-marathon-case-batch-production
type: task
status: pending_review
assignee: kimi
reviewer: 欧阳锋
priority: P0
created_at: 2026-07-04
updated_at: '2026-07-04T14:10:58.237076+00:00'
related:
- '[[case-yihang-dual-triangle-beike-ai-outbound]]'
- '[[case-yihang-dual-triangle-hotel-tag-sandbox]]'
- '[[case-yihang-dual-triangle-tianmo-design-delivery]]'
- '[[concept-yihang-dual-triangle-core]]'
---

# 任务 #91：双三角马拉松未入库案例批量生产

## 问题

双三角马拉松有十几个案例，Truman 在课上反复引用（L2196-2204："你真正想复刻半肥猫的数字化营销、空客的数字人、Vikki的选题……不要老盯着工作流，要理解他的双三角"）。但目前只有 9 张入库，还有 10+ 个案例在 inbox 里。

**Agent 无法回答"Vikki 怎么做 IP 选题的"这类问题**——案例根本不在索引里。

## 素材清单

| 案例 | 素材形态 | 优先级 |
|:---|:---|:---:|
| Vikki IP选题 | VLM提取（六要素完整）+ VLM图 | P0 |
| 半肥猫 数字化营销 | VLM提取 + VLM图 | P0 |
| 空客 数字人 | VLM提取 + VLM图 | P0 |
| 郭帅 | VLM提取 + VLM图 | P1 |
| 刘凯 | 口述PDF（已VLM分页提取） | P1 |
| 谭再超 | 口述PDF（已VLM分页提取） | P1 |
| 龙虾和skills训练 | 口述PDF（已VLM分页提取） | P1 |
| 一堂网站过程 | 口述PDF（已VLM分页提取） | P1 |
| AI组织行为学 | 口述PDF（已VLM分页提取）+ _text.md | P1 |
| 画布案例1 | PNG（已VLM提取） | P2 |
| 画布案例2 | PNG（已VLM提取） | P2 |

素材路径：`00_inbox/人机协作双三角/` 及 `_processed/`

## 生产要求

每张 case 卡必须包含：
- 双三角六要素映射（VLM 提取已有基础映射，需补充细节）
- 人物/动作/时间线或具体数字
- 该案例对双三角框架的独特贡献（不只是"又一个案例"）
- 口述稿原文引用（如有）
- standard case sections

## 提交方式

可分批提交。P0 的 3 张先做，欧阳锋终审通过后继续 P1。

## 验收标准

- 每张卡 `kdo pre-submit` PASS
- `kdo lint` 0 新增 ERROR
- index.md 收录
- 欧阳锋终审通过（可分批）
