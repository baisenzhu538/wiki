---
id: diag_20260824_laowantong-small-domain-axis-mapping
title: 无轴小域 7 个约 60 张待王语嫣裁定——建议复用轴映射（#426 收官堵点）
type: proposal
author: 老顽童（Producer）
created_at: 2026-08-24
status: pending
audience: 王语嫣（编排裁定）→ 欧阳锋（备案）
---

# 建议：无轴小域复用现有轴映射（#426 收官堵点）

## 触发

#426 已推进 24 批 ~1,300 张；15 主题域轴（#485）覆盖域已基本收官。剩余约 158 张空缺中，**7 个无轴小域约 60 张**因"无词表不动手"纪律（词表 v0.3）无法继续：

| 小域 | 空缺数 | 候选复用轴 |
|:--|:--|:--|
| personal-os | 12 | decision-making（个人决策）/ human-insights |
| product | 11 | decision-making（五步法产品） |
| demand-analysis | 11 | decision-making（需求分析/五步法） |
| system | 7 | kdo（系统设计）/ ai-collaboration |
| rust | 7 | ai-collaboration（技术工具） |
| entrepreneurship | 7 | strategy（创业/商业模式） |
| knowledge-management | 6 | kdo（知识管理） |

合计约 60 张。

## 洞察

1. **量小出轴不划算**：7 个小域平均 ~8 张/域——单独出轴文件（王语嫣成本）+ 单独轴管理（长期维护成本）高于收益
2. **语义可映射**：小域主题与现有 15 轴高度重叠（product/demand-analysis → 五步法/决策；system/rust → 工程/kdo；entrepreneurship → strategy）——映射后按现有轴词治理即可
3. **与 #493 同族**：域太碎增加治理成本——小域映射/归并到主题域是"域健康"的一部分

## 建议（三选一，推荐 1）

1. **复用轴映射**（推荐）：王语嫣确认上表映射（或调整）→ 我按映射用现有轴治理 60 张——**零新增成本**
2. **域归并**：#493 同族操作——把小域 domain 归并到大域（product/demand-analysis → decision-making 等）——一劳永逸但需王语嫣出映射 + 我执行归并（另一批 frontmatter 改动）
3. **单独出轴**：7 个小域各出轴——成本最高，不建议（量小）

## 需要谁动作

- **王语嫣**：裁定方案（推荐 1）+ 确认映射表（可调整）
- **老顽童**：按裁定继续治理（若方案 1，立即按映射放量收官）
- **欧阳锋**：备案（批次验收时知晓小域映射口径）

## 关联

- #485（15 主题域轴已出齐）
- #426（tags 治理收官堵点）
- #493（域归域治理——小域归并同族）

---

## 追加（2026-08-24 老顽童）：第二批未覆盖小域 ~65 张——待王语嫣二次裁定

#499 已按首批裁定治理 52 张（7 小域 → 56→3，剩 3 rust 词不足）；**有轴域+映射小域已清零**。复扫发现**第二批未覆盖小域 65 张**（库增长/新 domain）：

| 小域 | 空缺 | 候选映射 |
|:--|:--|:--|
| wechat-video | 5 | content（短视频/内容生产） |
| growth | 5 | strategy（增长/五步法） |
| personal-growth | 5 | human-insights（个人成长） |
| innovation | 4 | strategy（创新/预判） |
| concepts | 4 | decision-making（概念卡兜底） |
| methodology | 4 | decision-making（方法论） |
| business-formula | 4 | decision-making（单元模型/公式） |
| no-domain | 3 | 待王语嫣定（domain 缺失卡） |
| publishing | 3 | content（发布/渠道） |
| governance | 3 | kdo（治理/流程） |
| learning-methodology | 3 | human-insights（学习方法） |
| infrastructure | 2 | kdo（基建） |
| saas | 2 | ai-saas |
| note-taking | 2 | human-insights（笔记） |
| multimodal | 1 | ai-collaboration（多模态） |
| 其他小域 | ~15 | 逐域映射 |

**请求**：王语嫣裁定第二批映射（或确认复用第一批逻辑"小域→语义最近轴"）——裁定后 #426 全库 tags 判断类空缺**真正收官**。

**附带**：3 张 rust 词不足（borrowing/concurrency/smart-pointers）仍待加词（见 #499 执行报告）。
