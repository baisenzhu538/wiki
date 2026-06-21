---
name: ai-collaboration-ooda
description: OODA人机协作决策闭环——Observe/Orient/Decide/Act迭代循环
version: 1.0.0
author: 黄药师
license: MIT
platforms: [cli, feishu]
metadata:
  hermes:
    tags: [OODA, 迭代, 决策闭环, 反馈循环]
    related_skills: [ai-collaboration]
---

# OODA 人机协作决策闭环

基于王欢方法论。OODA 闭环在人机协作中的应用——每一轮迭代都让 AI 产出更接近目标。

## OODA 四步

| 步 | 含义 | 人的动作 | AI 的动作 |
|:--|:--|:--|:--|
| **O**bserve | 观察 | 看 AI 的输出，找问题 | 产出结果 |
| **O**rient | 定位 | 分析问题根因——是提示词不对？还是任务不适合 AI？ | — |
| **D**ecide | 决策 | 决定改什么——只改一个变量 | — |
| **A**ct | 执行 | 修改提示词/流程，重新跑 | 重新产出 |

## 执行要点

### Observe: 看什么？
- AI 输出和你预期的差距在哪？
- 是格式问题？内容问题？逻辑问题？
- 记录下来，不要凭印象

### Orient: 怎么定位根因？
- 提示词不够具体？→ 加约束/示例
- 任务本身不适合 AI？→ 换方案
- AI 能力边界到了？→ 拆成更小的子任务
- 不是 AI 的问题，是你的指令有问题？→ 诚实面对

### Decide: 只改一个变量
- 每次迭代只改一个东西
- 改了提示词 → 不要同时改模型参数
- 这样才知道哪个改动有效

### Act: 重新跑
- 用同样的输入重新跑
- 对比上一次的输出
- 记录改动和效果

## OODA 循环频率

| 场景 | 循环频率 | 说明 |
|:--|:--|:--|
| 提示词调试 | 分钟级 | 快速试错 |
| AI 产品迭代 | 天级 | 收集真实反馈 |
| 系统级优化 | 周级 | 需要数据积累 |

## 常见失败

| 症状 | 根因 | 修复 |
|:--|:--|:--|
| 改了 5 次没效果 | 同时改了多个变量 | 回 O：只改一个 |
| 反复改同一个东西 | 跳过 O(定位) | 先分析根因再改 |
| OODA 太慢成瓶颈 | 追求完美再 Act | 快速出 MVP 再迭代 |

## 参考卡片
- `framework-wanghuan-ooda-loop`
- `framework-wanghuan-actor-director-mode`