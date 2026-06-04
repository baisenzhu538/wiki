---
title: "KDO 能从 Codex 调试复盘学到什么"
type: improvement-plan
status: draft
domain:
  - master
created_at: 2026-06-04
updated_at: 2026-06-04
author: 黄药师
tags:
  - "#domain/knowledge-management"
  - "#domain/embedded"
  - "#method/evaluation-method"
---

# KDO 能从 Codex 调试复盘学到什么

> 触发：Codex 完成广冷红外板 V2.2 三阶段调试，产出了一份高质量方法论复盘。
> 问题：KDO 当前能捕获这个吗？不能的话差在哪？

---

## 一、这份复盘里有什么价值

| 层次 | 内容 | KDO 当前是否可捕获 |
|:----|:-----|:-----------------:|
| 事实层 | 根因=SN74LVC2G07 开漏→RCLK 缓坡 | ✅ 故障分析报告已记录 |
| 过程层 | 三阶段：盲试→诊断→逻辑修正 | ⚠️ 散落在对话里，无结构化记录 |
| 方法层 | "先诊断后修复""分段隔离""诊断版固件" | ❌ 无对应卡片类型 |
| 模式层 | 电平转换引入时序问题的通用排查路径 | ❌ 无对应卡片类型 |

**KDO 抓住了"是什么"，漏掉了"怎么做"和"为什么这样做"。**

---

## 二、KDO 的三个 Gap

### Gap 1：pitfalls/corrections 只记点，不记过程

P-1 到 P-20 都是"症状→根因→对策"的单点记录。Codex 这份复盘有价值的是**三阶段的转换逻辑**：
- 为什么从第一阶段切换到第二阶段？（意识到盲试无效 → 需要诊断手段）
- 诊断版固件的设计思路是什么？（不是修 bug，是造一个工具来定位 bug）
- 第三阶段的"分段隔离"如何加速了变量组合的调试？

KDO 的 pitfall 格式装不下这种过程性知识。它记录的是"不要做什么"，不是"应该怎么做"。

### Gap 2：方法论没有归属

这个复盘天然产出的是一个 **debugging playbook**（嵌入式红外/对射调试 checklist），但 KDO 当前：
- `30_wiki/concepts/` — 给领域知识（不适用）
- `40_outputs/capabilities/skills/` — 给可执行工具（太大了）
- `40_outputs/capabilities/playbooks/` — **这里是对的**，但缺少"从经验到 playbook"的提炼流程

### Gap 3：外部经验没有注入通道

KDO 飞轮是 `feedback → improve`，但 feedback 只能来自自己系统的产出（文章、卡片）。Codex 的这次经验是外部导入的——不是通过 kdo feedback 进来的，是用户在聊天里直接喂的。

**KDO 缺少一个"外部经验注入"的入口**——别人学到了东西，怎么喂给 KDO？

---

## 三、具体改进建议

### 建议 1：新增 `methodology` 子类型到 40_outputs

当前 capabilities 五种子类型：skills / agents / workflows / evals / playbooks / prompts

缺一个 **methodologies**（方法论卡）——不是可执行技能，是"在什么情况下应该怎么做"的决策框架。

```
methodologies/
  embedded-ir-debugging.md     ← 从本次复盘提炼
  diagnostic-first-principle.md   ← 通用原则
  segment-isolation-verification.md  ← 分段隔离法
```

### 建议 2：pitfalls 增加"可复用方法"字段

当前 pitfall 格式：
```
症状 → 根因 → 对策
```

建议增加：
```
症状 → 根因 → 对策 → 可复用方法（如果是通用模式）
```

例如本次可以加一条：
```
P-21: 嵌入式调试中盲目调参 → 没有诊断手段就调参数是撞运气
  → 先做诊断版固件排除硬件故障 → 可复用：diagnostic-first-principle
```

### 建议 3：kdo capture 支持"经验注入"

现在 `kdo capture` 捕获文本/URL/文件。能不能加一个 `--kind experience`，专门用于"别人告诉我一个教训/方法"？

```
kdo capture "嵌入式红外调试三步法" --kind experience --source codex
```

自动路由到 `20_memory/` 或 `40_outputs/capabilities/playbooks/`。

### 建议 4：checklist 作为一等公民

这次复盘最有复用价值的就是那个四步 checklist（硬件验证→时序诊断→分段隔离→判断逻辑）。KDO 当前没有任何地方专门存 checklist。

建议 `40_outputs/capabilities/checklists/` 或并入 playbooks。

---

## 四、优先级判断

| 建议 | 影响 | 工作量 | 优先级 |
|:----|:--:|:--:|:--:|
| 建议 2（pitfalls 加方法字段） | 小 | 低 | **立即做** |
| 建议 4（checklist 一等公民） | 中 | 低 | 短期 |
| 建议 1（methodology 子类型） | 中 | 中 | 中期 |
| 建议 3（capture --kind experience） | 高 | 高 | 长期 |

---

## 五、即时行动

- [x] 复盘文件已写入 `20_memory/embedded-debugging-retrospective-20260604.md`
- [ ] 追加 P-21 到 pitfalls.md（盲目调参反模式）
- [ ] 提炼一份 embedded-ir-debugging playbook 到 `40_outputs/capabilities/playbooks/`
- [ ] 更新 context.md

---

*黄药师 · 2026-06-04*
