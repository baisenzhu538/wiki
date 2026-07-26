---
id: task_20260726_wangyuyan-positioning-statement-lint
task_id: 199
assignee: hermes
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-07-26
created_at: 2026-07-26
updated_at: '2026-07-26T07:21:15.686279+00:00'
domain: system
priority: P1
reviewed_by: 欧阳锋
review_date: '2026-07-26'
grade: A
---

# 牌 L8 机械执行层：定位声明 lint 规则

## 背景

牌 L8 已立规：**每张子卡 → 先写定位声明（"属于 XX 框架的 Y 步"）→ 再写正文内容。**

当前缺失机械执行层——靠人记。本任务把 L8 落地为 `kdo pre-submit` 的 lint 规则，让机器拦、不靠人记。

## 流程设计

```
新卡生产
  → 老顽童不写定位声明
    → kdo pre-submit 报 WARNING
      → 欧阳锋看到 WARNING 退回
        → 老顽童补上定位声明
          → 再提交
```

## 任务

### 黄药师：lint 规则（依赖项，先完成）

| 动作 | 说明 |
|:--|:--|
| `kdo pre-submit` 新增 L8 检查 | 每张子卡（非 framework/digest/hub）检查正文第一节是否为定位声明 |
| 定位声明匹配模式 | `属于 .+ 的 .+ 步` 或 `属于 .+ 框架` 或等价模式 |
| 输出级别 | WARNING（非 ERROR）——缺定位声明不阻断提交，但欧阳锋可见 |
| 存量卡 | 不触发 WARNING——只检查本次提交新增/修改的卡 |

### 老顽童（Hermes）：生产流程

| 动作 | 说明 |
|:--|:--|
| 新卡定位声明 | 每张新卡正文第一节写定位声明（格式：`> 定位：属于 [[framework-xxx]] 的 Y 步。`） |
| 存量卡 | 不单独返工。该卡因其他原因返工时顺手补上 |
| 提交前自检 | `kdo pre-submit` → 看到 L8 WARNING → 补上 → 再提交 |

## 定位声明格式规范

```
> 定位：属于 [[framework-xxx]] 的第 Y 步「步骤名」。
```

示例：
- `> 定位：属于 [[framework-一堂-基本功-四字诀拆建推练]] 的第 1 步「拆」。`
- `> 定位：属于 [[framework-yitang-case-crafting-four-step]] 的第 3 步「挖专业度」。`
- `> 定位：属于 [[framework-ouyangfeng-review-methodology]] 的五轴审查·正确性轴。`

## 验收标准

1. 黄药师：`kdo pre-submit` 对缺定位声明的新卡输出 WARNING
2. 黄药师：存量卡不触发 WARNING
3. 老顽童：任务单模板/生产流程中确认定位声明写入步骤
4. 欧阳锋：审查流程中确认"看到 L8 WARNING → 退回"

## 执行顺序

1. 黄药师先完成 lint 规则（依赖项）
2. lint 规则上线后老顽童按流程执行（本任务领取）
3. 欧阳锋审查时执行退回逻辑

## 边界

- 不批量返工存量卡
- framework/digest/hub 卡不强制定位声明（自身就是定位锚点）
- WARNING 不是 ERROR——不阻断 pre-submit，但欧阳锋有权退回
