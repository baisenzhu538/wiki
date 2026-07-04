# 欧阳锋→王语嫣：2026-07-04 任务编排建议书

## 一、当前状态

本日八单全部终审通过（#64-#68, #71, #79），37 张新卡入库。WorkBuddy #28 WARNING 清理稳步推进（662→571，净减 91）。

## 二、新增信号：ERROR 从 0 飙到 226

**根因**：kdo linter 将「case 卡缺少标准 section」从 WARNING 升级为 ERROR。不是 WorkBuddy 清理引入的回归，是规则重新分类暴露了存量债。

**构成**：
- 224 个 = 56 张 case 卡 × 4 个缺失 section（关键证据/可迁移场景/教训/失败模式）
- 2 个 = 历史遗留 source_refs
- 影响范围：`case-yihang-dual-triangle-*` 和 `case-yitang-*` 系列，均为早期 card，非本日产出

**WorkBuddy 的结论成立**：他的 42 批修复只改 `## 质疑`/`## Open Questions` section，从未触碰 case 标准 section。WARNING 持续下降，方向正确。

## 三、欧阳锋判断

1. **Linter 规则升级本身是正确的**。case 卡确实应该有关键证据/可迁移场景/教训/失败模式——本日 #71 产出的 21 张 case 卡全部有这些 section，证明标准可执行。

2. **但这 56 张老 case 卡不应阻塞主线**。它们之前已通过终审入库，缺 section 是历史标准不统一导致的，不是内容错误。把存量债一次性清零会消耗大量产能，ROI 不如继续清理 WARNING。

3. **WorkBuddy 应继续 #28 WARNING 清理，不要转向修这 224 个 ERROR**。他的节奏是对的（每批净减 ~90 WARNING），换方向会打断势头。

## 四、编排建议

| 优先级 | 动作 | 执行者 | 理由 |
|---|---|---|---|
| **立即** | WorkBuddy 继续 #28 WARNING 清理，不受 ERROR 干扰 | WorkBuddy | 势头不能断；WARNING → 0 是 #28 的本职目标 |
| **本周** | 黄药师确认 linter 规则升级是否有意为之，若是则冻结规则不再回滚 | 黄药师 | 规则稳定后清理才有意义 |
| **P2** | 为 56 张老 case 卡补 section 开独立任务 | 老顽童(Kimi) | 每卡约需 15-20 分钟读原文+补 4 段，总量约 14-19 小时；建议拆成 3-4 批，排在本周主线之后 |
| **不入队** | 把 ERROR 阈值从 WARNING 升级回滚 | — | 不推荐。标准应该统一——新 case 卡有这些 section，老 case 卡也该有 |

## 五、一句话给王语嫣

**ERROR 飙升是 linter 变严了，不是质量变差了。WorkBuddy 继续清 WARNING，老 case 卡补 section 另开任务、P2 排期、不阻塞主线。**
