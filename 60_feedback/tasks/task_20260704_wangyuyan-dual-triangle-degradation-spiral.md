---
id: task_20260704_wangyuyan-dual-triangle-degradation-spiral
type: task
status: reviewed
assignee: claude
reviewer: 欧阳锋
priority: P1
created_at: 2026-07-04
updated_at: '2026-07-04T16:27:25.967648+00:00'
source_task: null
related:
- '[[framework-yihang-dual-triangle-core]]'
- '[[dk-yitang-sales-common-pitfalls]]'
- '[[concept-yihang-dual-triangle-flywheel]]'
reviewed_by: 欧阳锋
review_date: '2026-07-04'
---

# 任务 #76：双三角死亡飞轮：人机协作退化螺旋 dk 卡

## 任务目标

产出 1 张 dk 卡 `dk-ai-collaboration-degradation-spiral`——双三角框架的失败模式补全。

**核心要求**：双三角飞轮只讲了正向循环（人强→AI强→省时间→人更强），但口述稿里 Truman 描述了两种反向模式。现有 KDO 没有任何一张卡覆盖这个缺口。

## 原始素材

- `00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt`
- `00_inbox/人机协作双三角/一堂双三角-人机协作模型-逐字稿.md`

## 卡片内容要求

### 1. 两个退化模式

| 模式 | 口述稿原文 | 机制 |
|:---|:---|:---|
| **互相糊弄死亡飞轮** | L1680-1688："你糊弄AI AI也糊弄你…你也不给AI输送审美，AI就全是幻觉…你还相信…最后圈越滚越差" | 人不投入→AI输出差→人不信任→投入更少 |
| **判断力退化飞轮** | L3942-3952："人好不容易到60分，加上AI变成30分…A太容易给一些比较唬人的好东西了" | AI给出表面好看的东西→人失去判断力→看不出问题→输出质量下降 |

### 2. 退化飞轮的特征信号

从口述稿提取的早期预警指标：
- 开始盲目相信AI的输出（"AIGC说啥我都对"）
- 不再追问、不再多轮调教（"3-5轮就结束战斗"）
- 审美感知钝化——给你两个方案，你说不出哪个更好
- 项目失败后归零而非积累

### 3. 对抗方法

从口述稿 L3990 提取："需要一些新的协作流程和品控的机制才能对抗这个退步"。

具体方向（口述稿暗示的）：
- 建立品控 checklist（每次AI输出必过人的判断点）
- 强制多轮对话习惯（"10到20轮就是比3到5轮质量高太多" L1696-1697）
- 定期复盘——用双三角拆解自己的协作过程（L2220-2247 的"拆自己"用法）

### 4. 标准 section 要求

- `## 定义`
- `## 为什么会出现`
- `## 失败模式清单`（至少 2 个完整模式，每个含：症状/根因/后果/早期信号）
- `## 如何对抗`
- `## Critique`
- `## Related`

## 验收标准

- `kdo pre-submit` PASS
- `kdo lint` 0 新增 ERROR
- 至少引用口述稿 3 处原文
- related ≥ 5（至少连接双三角核心框架 + 已有 dk 卡 + Y模型）

## 边界说明

- 不重复写飞轮正向逻辑（已有 `framework-yihang-dual-triangle-core` 覆盖）
- 不展开成方法论卡——这是 dk 卡，聚焦失败模式和对抗方向
