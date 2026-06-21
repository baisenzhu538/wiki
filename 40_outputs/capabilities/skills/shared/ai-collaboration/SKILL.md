---
name: ai-collaboration
description: 人机协作总入口——从演员到导演，从任务到系统
version: 1.0.0
author: 黄药师
license: MIT
platforms: [cli, feishu]
metadata:
  hermes:
    tags: [AI协作, 王欢, 导演模式, Harness, BITCOE, OODA, GAN]
    related_skills: [ai-collaboration]
---

# AI Collaboration（人机协作总入口）

基于王欢 AI 实战方法论。核心命题：人从执行者升级为导演，AI 从工具升级为可编排的执行系统。

## Constraints

<hard_limits>
- 严禁把 AI 当"更好的搜索引擎"——先判断任务在五层跃迁模型的哪一层
- 产品场景选择必须过五条标准（高频/刚需/可验证/低风险/有数据）
</hard_limits>

## 意图分类

| 类型 | 路由到 | 示例 |
|:--|:--|:--|
| 从零搭建 AI 产品 | `/ai-collaboration-harness` | "我想用AI做个客服系统" |
| 写/优化提示词 | `/ai-collaboration-bitcoe` | "帮我写个提示词让AI做XX" |
| 决策迭代/需要反馈闭环 | `/ai-collaboration-ooda` | "AI产出的质量不稳定怎么办" |
| 多模型协作/对抗验证 | `/ai-collaboration-gan` | "怎么让AI自己检查自己的输出" |
| AI 软件开发流程 | `/ai-collaboration-dev` | "用AI写代码怎么保证质量" |

## 核心框架

### 五层跃迁模型
```
问答层 → 工作流层 → 作品层 → 产品/应用层 → 系统层
```

每一层的能力要求、AI 角色、人的角色都不同。关键判断：**你现在在哪一层？目标在哪一层？**

### 演员→导演模式
- 演员思维：AI 是工具，我让它干什么它就干什么
- 导演思维：AI 是执行系统，我定义标准、编排流程、验收结果
- 效率差：10 倍

## 参考卡片

- `human-ai-collaboration-double-triangle` — 域索引入口
- `framework-wanghuan-actor-director-mode` — 演员→导演
- `framework-wanghuan-ai-five-level-ladder` — 五层跃迁