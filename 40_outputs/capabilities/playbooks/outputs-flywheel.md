---
title: "Outputs 飞轮 — 每一次产出都是下一轮的原料"
type: capability
subtype: playbook
status: ready
target_user: KDO 所有角色 — 任何产出都不应该是终点
delivery_channel: local
source_refs:
  - knowledge-flywheel-discovery-20260602
  - proposal-kdo-flywheel-infrastructure
wiki_refs:
  - kdo-flywheel
  - sprint-20260531-retrospective
created_at: 2026-06-02
updated_at: 2026-06-02
author: 黄药师
---

# Outputs 飞轮

> **一句话**：不要把你的产出当成终点。它是下一轮的原料。

## 三个核心发现

### 1. Outputs 不是终点，是下一轮的燃料

```
老顽童的文章 → 触发黄药师的深度复盘
黄药师的复盘 → 暴露四个死刑
四个死刑 → 变成 Sprint 6 工单
Pilot 20 数据 → 发现 chunk_type bug + confidence 聚集
Bug 修复 + 数据 → 下一轮 prompt 调优
```

如果你把任一步的产出当成终点扔掉，链条就断了。**每一次产出必须有一个回收到管线的入口。** Feedback 段不是装饰品——它是飞轮的离合器。

### 2. 架构的价值不在分类，在生成

capabilities/ 的五种子类型（skill/agent/workflow/eval/playbook）全部就位后，自然产生了一条无人设计的链路：

```
kdo feedback --auto-enrich  (playbook 触发)
  → Labeler Agent 重新标注    (agent 执行)
    → Gold Standard eval 比对 (eval 验证)
      → accuracy-recovery     (playbook 介入)
        → Prompt 迭代 skill   (skill 指导)
          → labeling-pipeline (workflow 串联)
```

五种类型咬合之后，架构自己长行为。**分类只是第一步，分类之后的事才是真正值钱的。**

### 3. 深度不是挖出来的，是飞轮转出来的

不需要更聪明。只需要三个条件同时满足：

| 条件 | 含义 | 反例 |
|------|------|------|
| 建造者 = 使用者 | 建工具的人必须自己先用 | 黄药师建 label 管线，自己写出四个死刑 |
| 反馈通道畅通 | 使用者能立刻告诉建造者哪里不够好 | user 说"不够深刻"→ 开启整个链条 |
| 摩擦力可见 | 每次使用都暴露新问题 | Feedback 段强制写"不足或遗漏" |

## 如何让飞轮转起来

### 每个角色的飞轮职责

| 角色 | 你的产出 | 如何让它成为下一轮的燃料 |
|------|------|------|
| 老顽童 | 文章/卡片 | Feedback 段写三个没想清楚的问题 |
| 黄药师 | 工具/管线 | 自己先用 → 找到摩擦 → 写四个死刑 |
| 欧阳锋 | 审查/工单 | 把反馈问题升级为正式工单 |
| 用户 | 方向/判断 | 对每一轮产出说"不够深"或"够了" |

### 飞轮的停止信号

| 信号 | 含义 |
|------|------|
| 连续两轮产出的新问题全部是已知问题 | 进入稳态 |
| 下一轮需要实验数据而不是纯推理 | 转 Pilot 模式 |
| ROI 递减：下一轮深度增量 < 投入时间 | 暂停，等新数据 |

## 代码实现

飞轮已固化为 KDO 命令：

```bash
# 一圈飞轮
kdo produce --deep          # 建造+使用合一
kdo validate --article      # D1-D4 深度门禁
kdo ship --configure        # 发布 + Agent 上下文
kdo feedback --auto-enrich  # 反馈回流 → 触发下一轮
kdo label --card <id>       # 重新标注
kdo label --audit           # 数据审计 → 发现下一轮方向
```

## 关联

- [[kdo-flywheel]] — KDO 飞轮概念卡
- `knowledge-flywheel-discovery-20260602` — 飞轮发现复盘
- `proposal-kdo-flywheel-infrastructure` — 飞轮基础设施提案

---

*黄药师 · 2026-06-02*
