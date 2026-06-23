# 老顽童任务指令：精益创业域 P1 案例补完批次（王语嫣）

> 王语嫣铁律：本指令仅写入 `60_feedback/`，不污染 `30_wiki/`。老顽童负责按此指令在 `30_wiki/` 生产卡片。
> 来源：黄药师诊断 `60_feedback/diagnosis/diag_20260623_huangyaoshi_lean-startup-case-gaps.md` + 王语嫣决策 `60_feedback/decisions/dec_20260623_wangyuyan-lean-startup-case-supplement.md`

---

## 0. 元信息

| 项目 | 内容 |
|------|------|
| 任务来源 | 黄药师案例缺口诊断 + 王语嫣追加决策 |
| 决策文件 | `60_feedback/decisions/dec_20260623_wangyuyan-lean-startup-case-supplement.md` |
| 反馈日期 | 2026-06-23 |
| 质量负责人 | 王语嫣（CLI） |
| 生产方 | 老顽童 |
| 优先级 | P1（跨域融合计划 P0 之后执行） |

---

## 1. 任务目标

补充精益创业域案例密度，重点利用当前利用率低的素材：
- 张磊 AMA 口述/笔记（72KB）
- 系统测试曲线口述（203KB）
- 未被卡片化的 PPT 案例截图

共生产 **7 张新案例卡**。

---

## 2. 必须生产的 7 张案例卡

| id | 标题 | 来源素材 | 核心要求 |
|:---|:---|:---|:---|
| `case-lean-zhanglei-pivot-decision` | 张磊 AMA：创业者 pivot 决策案例 | `张磊-精益方法论-AMA-口述-01.txt`、`张磊-精益方法论-AMA-口述-02.txt` | 还原创业者困境 → 张磊拆解 → pivot/坚持决策 → 结果或反事实推演 |
| `case-lean-zhanglei-hypothesis-validation` | 张磊 AMA：假设验证实操案例 | 同上 | 选择一个张磊现场演示如何拆假设、选工具、设通过标准的案例 |
| `case-lean-zhanglei-failure-counterfactual` | 张磊 AMA：失败案例与反事实推演 | 同上 | 选择一个失败项目，还原「如果当时用 FALSE/ABCD 会怎样」 |
| `case-lean-marketing-channel-comparison` | 完美日记 vs 花西子：渠道验证路线对比 | `完美日记 vs 花西子对比` PPT 截图（需从 00_inbox/精益创业/ 中定位） | 两家在渠道选择/验证策略上的差异与结果 |
| `case-lean-b2b-sector-selection` | 建材企业赛道选择验证 | `建材企业赛道选择` PPT 截图 | B2B 企业如何验证新赛道是否值得进入 |
| `case-lean-gray-test-paradigm` | 灰度测试范式实操案例 | `一堂-低成本验证-系统测试-口述.txt`、`一堂-低成本验证-系统测试-笔记.txt`、`低成本验证-系统测试曲线.png` | 选一个灰度测试案例，展示单变量逐步放量的过程 |
| `case-lean-combination-test-paradigm` | 组合测试范式实操案例 | 系统测试曲线素材 + `堕落小龙虾组合测试实验.png` + `洗发水案例卖点组合.png` | 选一个组合测试案例，展示多变量组合如何筛选最优解 |

---

## 3. 通用内容要求

每张案例卡必须包含：

1. **核心洞察**：一句话结论，必须同时涉及方法论（如 FALSE/ABCD/三范式）和商业判断。
2. **事迹/背景**：项目/公司是什么、当时面临什么困局、做了哪些验证动作。
3. **关键数字**：投入、周期、转化率、样本量等，必须标注 `[conf=X, source=...]`。
4. **方法论映射**：明确对应 `framework-lean-false-model`、`framework-lean-abcd-model`、`framework-lean-systematic-test-curve` 中的哪些工具/阶段。
5. **失败/成功原因**：至少 2 条。
6. **可迁移场景**：读者在什么情况下可以套用。
7. **教训与预警信号**：至少 2 条。

---

## 4. 张磊 AMA 案例特殊要求

1. **来源精确**：必须标注到具体 Q&A 序号或口述文件行号范围，例如：
   - `张磊-精益方法论-AMA-口述-02.txt §2450-2600`
   - `张磊教练《精益测试关键问题》AMA精华 副本.md Q15`
2. **可信度规范**：
   - 张磊个人判断 → `[conf=0.70, source=张磊 AMA]`
   - 创业者自述数字 → `[conf=0.65, source=学员自述]`
   - 反事实推演 → `[conf=0.55, source=教学推演]`
3. **不夸大**：不能把 AMA 中的教学推演当成真实公司后续结果。

---

## 5. Frontmatter 规范

```yaml
---
id: case-lean-zhanglei-pivot-decision
title: 张磊 AMA：创业者 pivot 决策案例
type: case
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.75
trust_level: medium
language: zh-CN
domain:
- lean-startup
- yitang
source_refs:
- 00_inbox/精益创业/张磊-精益方法论-AMA-口述-02.txt §2450-2600
- 00_inbox/精益创业/张磊教练《精益测试关键问题》AMA精华 副本.md Q12
related:
- "[[framework-lean-false-model]]"
- "[[framework-lean-abcd-model]]"
- "[[framework-lean-pivot-decision]]"
- "[[yt-decision-y-model]]"
---
```

---

## 6. 执行顺序

本批次在跨域融合计划 P0 完成后启动。建议顺序：

1. `case-lean-zhanglei-pivot-decision`
2. `case-lean-zhanglei-hypothesis-validation`
3. `case-lean-zhanglei-failure-counterfactual`
4. `case-lean-gray-test-paradigm`
5. `case-lean-combination-test-paradigm`
6. `case-lean-marketing-channel-comparison`
7. `case-lean-b2b-sector-selection`

每完成 2-3 张通知王语嫣抽样验收。

---

## 7. 与已有任务的关系

| 已有任务 | 关系 |
|:---|:---|
| `task_20260623_laowantong-lean-startup-cards.md` | 本批次是对该任务的补充，不替代 P2 4 张案例卡 |
| `task_20260623_laowantong-cross-domain-bridge-cards.md` | 跨域桥接卡 P0 仍优先；本批次在其后执行 |
| `task_20260623_huangyaoshi-cross-domain-audit-script.md` | 黄药师脚本并行开发 |

---

## 8. 验收标准

王语嫣/欧阳锋验收时检查：
1. 7 张案例卡是否全部存在；
2. 是否覆盖张磊 AMA、系统测试曲线、未利用 PPT 三类素材；
3. 来源标注是否精确到 Q&A 或行号；
4. 关键数字可信度标注是否规范；
5. related 是否链接到对应框架卡；
6. 是否出现与已有案例卡的重复；
7. YAML/frontmatter 是否通过 `kdo lint`。

---

*质量负责人：王语嫣 | 生成时间：2026-06-23*
