---
id: huangyaoshi-codex-lessons-review
title: "审查请求：Codex 调试复盘 → KDO 系统改进 4 条建议"
type: task
status: pending_review
assigned_to: 欧阳锋
submitted_by: 黄药师
created_at: 2026-06-04
source_refs:
  - kdo-lessons-from-codex-debug-20260604
  - embedded-debugging-retrospective-20260604
---

# 审查请求：Codex 调试复盘 → KDO 系统改进 4 条建议

> **提交人**：黄药师
> **审查人**：欧阳锋
> **背景**：Codex 完成广冷红外板 V2.2 三阶段调试复盘，产出了一份高质量方法论总结。黄药师分析了 KDO 当前能否捕获这类经验，识别了 3 个 Gap，提出 4 条改进建议。需要欧阳锋审查拍板：做哪个、不做哪个、顺序如何。

---

## 背景：发生了什么

Codex 在广冷红外板 V2.2 调试中经历三个阶段：
1. 盲试（Ir_Delay 15→500，零进展）
2. 诊断切入（做诊断版固件，排除硬件故障，定位到 595 时序问题）
3. 逻辑修正（分段隔离 + 业务理解驱动判断逻辑）

产出一份复盘，含：
- 根因分析（SN74LVC2G07 开漏 → RCLK 缓坡）
- 可复用方法（diagnostic-first-principle / 分段隔离 / 电平转换排查路径）
- 通用 checklist（硬件验证→时序诊断→分段隔离→判断逻辑）

黄药师已将复盘结构化入库：
- `20_memory/embedded-debugging-retrospective-20260604.md`
- `40_outputs/capabilities/playbooks/embedded-ir-debugging.md`
- P-21 追加到 `.agent/pitfalls.md`

---

## 识别的 3 个 Gap

| Gap | 问题 | 影响 |
|-----|------|------|
| 1 | pitfalls 只记"症状→根因→对策"，不记"应该怎么做"的过程性知识 | 三阶段转换逻辑、诊断版设计思路等无法结构化存储 |
| 2 | 方法论/playbook 没有标准归属路径 | 复盘天然产出 debug playbook，但 KDO 缺少从经验到 playbook 的提炼流程 |
| 3 | 外部经验没有注入通道 | Codex 的经验是通过聊天手动喂的，不是通过 `kdo feedback` 进入的 |

---

## 4 条改进建议（按优先级排序）

### 建议 2（P0，立即做）：pitfalls 增加"可复用方法"字段

**当前格式**：
```
症状 → 根因 → 对策
```

**建议格式**：
```
症状 → 根因 → 对策 → 可复用方法（如果是通用模式）
```

**例子**：P-21 加 `可复用方法：diagnostic-first-principle`

**工作量**：~10min（改 pitfall 模板 + 补已有 pitfall 的方法字段）
**影响**：小但精准——打通 pitfall → methodology 的链路

---

### 建议 4（P1，短期）：checklist 作为一等公民

**目前**：KDO 没有任何地方专门存 checklist。

**建议**：`40_outputs/capabilities/checklists/` 或并入 playbooks

**例子**：本次产出的嵌入式红外/对射调试四步 checklist

**工作量**：~30min（建目录 + 模板 + 迁移已有 checklist）
**影响**：中——checklist 是最高 ROI 的知识形态（直接可执行）

---

### 建议 1（P2，中期）：新增 methodology 子类型

**当前 capabilities 类型**：skills / agents / workflows / evals / playbooks / prompts

**缺**：methodologies（方法论卡）——不是可执行技能，是"在什么情况下应该怎么做"的决策框架

**建议目录**：
```
40_outputs/capabilities/methodologies/
  diagnostic-first-principle.md
  segment-isolation-verification.md
  level-shift-timing-troubleshooting.md
```

**工作量**：~1h（改 artifacts.py subtype 枚举 + 模板 + 1-2 个示例）
**影响**：中——给方法论一个明确的归属

---

### 建议 3（P3，长期）：kdo capture 支持经验注入

**目前**：`kdo capture` 捕获文本/URL/文件

**建议**：
```
kdo capture "嵌入式红外调试三步法" --kind experience --source codex
```
自动路由到 `20_memory/` 或 `40_outputs/capabilities/playbooks/`

**工作量**：~2-3h（新 capture kind + 自动分类路由 + 模板生成）
**影响**：高——打通外部经验→KDO 的正式通道

---

## 审查决定（欧阳锋填写）

| 建议 | 决定 | 理由/备注 |
|------|:--:|------|
| 建议 2（pitfalls 加方法字段） | **✅ 做 P0** | 改 pitfall 模板 + 补已有条目的方法字段。~10min |
| 建议 4（checklist 一等公民） | **✅ 做 P1** | 先放 `40_outputs/capabilities/playbooks/` 过渡，不新建目录。跑通后再评估是否拆分 |
| 建议 1（methodology 子类型） | **🟡 暂缓 P2** | `90_control/electronics-practice/` 已覆盖同类需求。等该目录跑完 3 个项目后再评估是否升级到 capabilities |
| 建议 3（capture --kind experience） | **⬜ 本阶段不做 P3** | 方向对，优先级低。当前通过聊天注入的路径虽不完美但够用。等 methodology 子类型跑通后再来考虑 |

**附加指令**：

建议 2 和 4 由黄药师执行。建议 1 和 3 放入待排期清单，当前不投入开发。

---

*黄药师提交 · 2026-06-04*
