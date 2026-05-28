---
title: "老顽童：管理工具箱 Batch 3 — T6+T7+T8"
assigned_to: "老顽童 (Producer)"
priority: "P1"
created_at: "2026-05-28"
reviewer: "欧阳锋"
status: "in_progress"
depends_on: []
blocks: []
---

# 老顽童：管理工具箱 Batch 3 — T6+T7+T8

## 背景

上一轮已完成：

- y-model validator 修复 ✅
- 单元模型域 2 处小修 ✅
- OCR Batch 1-4 全部审查通过 ✅（最后一轮：8 张批量模板 A-）

管理工具箱已有 F1（总览）+ T1-T5（会议/招聘/OKR/战略/知识萃取），全 A/A+ 审查通过。
**Batch 3 补齐最后 3 张**，工具箱在管理域形成完整闭环。

三张卡骨架已存在（`kdo scaffold` 产出，status=draft），攻击者已就位。**需要精修格式 + 展开论证。**

---

## 三张卡现状

| 卡 | 路径 | 现有字数 | 攻击者 | 问题 |
|:-:|:----|:-------:|:-------|:----|
| T6 | `yt-tool-project-health-radar` | 755w | Flyvbjerg ✅ + Goldratt ✅ | Critique 和 Constraints & Boundaries 并存（重复） |
| T7 | `yt-tool-onboarding-90day` | 1051w | Van Maanen&Schein ✅ + Edmondson ✅ | 同上。Steps 被 `####` 格式误解析为攻击者 |
| T8 | `yt-tool-equity-checklist` | 814w | Coase ✅ + Williamson ✅ | 同上。Steps 被 `####` 格式误解析为攻击者 |

三张共同问题：
1. **`## Constraints & Boundaries` 和 `## Critique` 并存**——v1.5 只应有一个 `## Critique`，把 Constraint & Boundaries 的内容合并到 `### 内部局限`
2. **Steps 用 `####` 标记**——validator 会把所有 `####` 统计为攻击者。Steps 应改为 `### 使用步骤` 下的有序列表
3. **攻击者论证太薄**——每个攻击者只有标题没有展开段落。（Flyvbjerg "包装欺骗"和 Goldratt "人的行为"方向很好，但各只有一句话）

## 修复方法（逐卡）

### 格式修正（每卡 ~10min）

当前结构（问题）：
```
## Summary
## Claims
## Constraints & Boundaries    ← 多余
## Critique                    ← H4 误混了 Steps 和攻击者
## Synthesis
## Action Triggers
```

应改为：
```
## Summary
## Claims
### 适用边界              ← 原 Constraints & Boundaries 内容搬到这里
### 使用步骤              ← 原 Steps 用有序列表，不用 ####
## Critique
### 内部局限
#### [学者] — [标题]
[2-3 句论证]

#### [学者] — [标题]
[2-3 句论证]
### 外部攻击
#### [学者] — [标题]
[2-3 句论证]

#### [学者] — [标题]
[2-3 句论证]
## Synthesis
## Action Triggers
```

> ⚠️ **关键**：
> - 三张卡当前攻击者已全部在 `## Critique` 下（不在 Constraints 下），所以只需要把多余的 `## Constraints & Boundaries` 删掉，内容合并到 `### 内部局限`。不需要像 y-model 那样从零建容器。
> - Steps 的 `####` 全部改为普通有序列表（`1. xxx\n2. xxx`），不然 validator 误判为攻击者。

### 攻击者展开（每卡 ~20min）

攻击者方向正确，但每个需要展开为 2-3 句实质性论证：

**T6 — Project Health Radar**

| 攻击者 | 当前 | 需展开 |
|:-------|:-----|:-------|
| Bent Flyvbjerg | "科学监控在真实世界中被用来包装欺骗" | 引用《巨型项目的铁律》——项目越大越容易超预算/超期，监控工具反被用来粉饰进度。雷达的"健康"指标在政治压力下变成展示品。 |
| Eliyahu Goldratt | "雷达忽略了项目管理最大的敌人——人的行为" | 引用《目标》——局部指标达标→全局次优。团队看到雷达变黄会调整行为让指标变好看而不是解决真问题。 |

**T7 — Onboarding 90-Day**

| 攻击者 | 当前 | 需展开 |
|:-------|:-----|:-------|
| Van Maanen & Schein | "结构化 onboarding 可能正在杀死新人最值钱的东西——新鲜视角" | 引用 organizational socialization 研究——过度结构化加速同化，但也消灭了 outsider perspective。新人看到的问题可能在 Day 30 后就不"看见"了。 |
| Amy Edmondson | "没有心理安全的 onboarding 是沉默孵化器" | 引用《无畏的组织》——结构化流程如果让新人不敢质疑（"流程就是这样定的"），等于在孵化沉默。Onboarding 检查清单 ≠ 心理安全。 |

**T8 — Equity Checklist**

| 攻击者 | 当前 | 需展开 |
|:-------|:-----|:-------|
| Ronald Coase | "所有股权架构都在回答 Coase 1937 年的问题——而你可能从来没问过" | 引用《企业的性质》——企业的边界由交易成本决定。合伙开始时交易成本低，股权分配看似合理；但当资产专用性加深，Coase 问题需要重新回答。 |
| Oliver Williamson | "股权设计的最大盲区——资产专用性与要挟问题" | 引用 Williamson 治理结构理论——资产专用性越高的合伙人越容易被要挟（hold-up）。静态股权分配没有考虑贡献度随时间变化，这是 Williamson 说的"合同不完备性"的核心。 |

## 验证

每张卡修完：

```bash
kdo validate --v15 --card yt-tool-project-health-radar
kdo validate --v15 --card yt-tool-onboarding-90day
kdo validate --v15 --card yt-tool-equity-checklist
```

三张全部 PASS 后通知欧阳锋审查。

## 验收

| # | 验收项 | 判定 |
|:-:|------|:----:|
| 1 | 三张卡 `kdo validate --v15` 全部 PASS | 终端 exit 0 |
| 2 | 无 `## Constraints & Boundaries` 残留 | grep |
| 3 | Steps 不用 `####` 格式（validator 不把步骤误算为攻击者） | `kdo validate` 攻击者计数正确 |
| 4 | 每个攻击者 ≥2 句实质性论证（非仅标题） | 人工审查 |
| 5 | 不改已有攻击者选择（Flyvbjerg/Goldratt/Van Maanen/Edmondson/Coase/Williamson 不动） | diff |

## 不做

- **不做** 新增攻击者——每卡 2 位已达标
- **不做** 换攻击者——已有方向经审查确认
- **不做** VA 分析——这些是工具卡不是视觉卡
- **不做** v1.5 Warning 修复——157 个 Warning 全是 research 类型，正常水位

---

*欧阳锋 · 2026-05-28*
