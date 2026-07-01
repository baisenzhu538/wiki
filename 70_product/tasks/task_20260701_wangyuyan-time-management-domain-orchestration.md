---
id: task_20260701_wangyuyan-time-management-domain-orchestration
title: 时间管理域卡片化与升级
type: task
status: queued
priority: P2
assignee: 老顽童(Kimi)
reviewer: 欧阳锋
created_at: 2026-07-01
updated_at: 2026-07-01
expected_cards: 3
source_refs:
  - 00_inbox/时间管理/truman-时间管理课程-口述.txt
  - 00_inbox/时间管理/truman-时间管理课程-笔记.txt
  - 00_inbox/时间管理/时间管理-修炼进阶图.png
  - 00_inbox/时间管理/时间管理-深度工作冰山图.png
  - 00_inbox/时间管理/时间管理-时间管理矩阵图.png
  - 00_inbox/时间管理/时间管理-双环矩阵图.png
  - 00_inbox/时间管理/时间管理-双峰哲学模型.png
  - 00_inbox/时间管理/_processed/时间管理_整合笔记.md
  - 00_inbox/时间管理/_processed/vlm_summary.json
  - 60_feedback/diagnosis/diag_20260701_time-management-validation.md
---

# 时间管理域卡片化与升级

> 任务来源：王语嫣入口质量门诊断（`60_feedback/diagnosis/diag_20260701_time-management-validation.md`）
> 诊断结论：素材综合评级 **A-/B+**，高价值、值得纳入，首批 3 张卡。

---

## 一、任务目标

用一堂科学时间管理课程（Truman，2026）升级现有卡片，并新建 2 张核心模型卡，填补 KDO 在「个人时间管理方法论」域的缺口。

| 批次 | 卡片 | 类型 | 动作 | 优先级 |
|:---:|:---|:---|:---|:---:|
| 首批 | `yt-personal-time-management` | concept | 升级整合 | P2 |
| 首批 | `framework-yitang-time-management-triad` | framework | 新建 | P2 |
| 首批 | `concept-yitang-deep-work-iceberg` | concept | 新建 | P2 |
| 二批候选 | `concept-yitang-dark-time` | concept | 新建 | P3 |
| 二批候选 | `concept-yitang-bimodal-philosophy` | concept | 新建 | P3 |
| 二批候选 | `tool-yitang-dual-loop-matrix` | tool | 新建 | P3 |

---

## 二、素材清单

| 素材 | 形式 | 核心覆盖 | 质量 |
|:---|:---|:---|:---:|
| `truman-时间管理课程-口述.txt` | 口述转录（2624 行） | 课程完整讲述，含大量 Truman 个人实验与暗知识 | A- |
| `truman-时间管理课程-笔记.txt` | 结构化笔记（176 行） | 核心概念、精华、术语解释 | B+ |
| `时间管理_整合笔记.md` | VLM + 人工整合 | 五大图解 + 口述要点结构化 | A- |
| `vlm_summary.json` | 5 张图解 OCR + 解析 | 修炼进阶图、冰山图、矩阵图、双环矩阵、双峰模型 | A- |

---

## 三、高价值段落索引（王语嫣标注）

### 3.1 核心定义与边界（优先级 P0）

| 主题 | 素材位置 | 建议出卡 | 关键引用 |
|:---|:---|:---|:---|
| 科学时间管理定义 | 口述 160-168 行 | `yt-personal-time-management` | "针对自己的时间、精力和眼下的任务，持续迭代，成倍提升自己的时间 ROI" |
| 课程边界：不讲人生成功/精力管理/项目管理 | 口述 150-156 行 | `yt-personal-time-management` Constraints | 只讲个人工作时间的科学配置 |
| 三大流派批判 | 口述 110-135 行 | `yt-personal-time-management` Critique | 人生成功派、模糊泛化派、神奇工具派 |
| 三大认知误区 | 笔记 8-21 行 | `yt-personal-time-management` | 工具迷信、边界模糊、二极管思维 |

### 3.2 三元模型（优先级 P0）

| 主题 | 素材位置 | 建议出卡 | 关键引用 |
|:---|:---|:---|:---|
| 时间模型、任务模型、匹配模型 | 口述 358 行 / 整合笔记 35-51 行 | `framework-yitang-time-management-triad` | "你建模也就这三个模型，没有第四个了" |
| 时间模型的四层理解 | 口述 1770-1832 行 | `framework-yitang-time-management-triad` | 从 7×24 格子 → 大块小块 → 波峰波谷 → 场景质量 |
| 事情模型：任务深度 L1-L5 | 口述 1574-1606 行 / 冰山图 | `concept-yitang-deep-work-iceberg` | "事情除了大小、重要紧急之外，最重要的维度是深度" |
| 匹配模型三原则 | 口述 1906-2068 行 | `framework-yitang-time-management-triad` | 大对大/小对小、双峰哲学、暗时间 |

### 3.3 深度工作冰山图（优先级 P0）

| 主题 | 素材位置 | 关键引用 |
|:---|:---|:---|
| L1 简单执行 | 口述 1590 行 / 冰山图 | 贴发票、打电话、回消息 |
| L2 简单协作 | 口述 1590 行 / 冰山图 | 开周会、做评审、派任务 |
| L3 独立专注 | 口述 1590 行 / 冰山图 | 学课程、写作业、背单词 |
| L4 深度思考 | 口述 1596 行 / 冰山图 | 做复盘、做决策、写方案，需进入心流 |
| L5 才华涌现 | 口述 1600 行 / 冰山图 | 写文章、提假设、做营销，需灵感闪现 |
| 深度拆解案例：写文案 | 口述 1626-1724 行 | 40 分钟路上 L5 + 睡前 L4/L3 + 第二天 7 小时 L1/L2 |
| 拆解原则：努力拆解，不大不小刚刚好 | 口述 1726-1754 行 | 里程碑拆解、多版本、大纲与细化、酝酿与动手 |

### 3.4 工具选择与双环矩阵（优先级 P1）

| 主题 | 素材位置 | 建议出卡 | 关键引用 |
|:---|:---|:---|:---|
| 双环矩阵四象限 | 整合笔记 141-174 行 / 双环矩阵图 | `tool-yitang-dual-loop-matrix` | 横轴：独立↔协作；纵轴：效率↔重点；内环/外环 |
| 对称替换逻辑 | 整合笔记 169-174 行 | `tool-yitang-dual-loop-matrix` | 任务清单↔任务池、晨间日记↔周报、番茄↔甘特图、时间统计↔团队日历 |
| 工具选择原则 | 口述 1276-1312 行 | `tool-yitang-dual-loop-matrix` | "不要觉得自己不自律，只是工具不顺手" |
| 时间管理矩阵/四象限 | 口述 842-854 行 / 矩阵图 | `tool-yitang-dual-loop-matrix` | A 未雨绸缪、B 努力减少、C/D 避免陷入 |

### 3.5 双峰哲学（优先级 P1）

| 主题 | 素材位置 | 建议出卡 | 关键引用 |
|:---|:---|:---|:---|
| 双峰哲学定义 | 口述 398-448 行 / 双峰模型图 | `concept-yitang-bimodal-philosophy` | 主动把协作和独立工作分开 |
| 分时策略 | 口述 1928-1942 行 | `concept-yitang-bimodal-philosophy` | 按小时/按天/按周/按年划分 |
| Truman 个人实践 | 口述 400-448 行 | `case-truman-bimodal-experiment` | 周四在家闭关、工位只聊天不写方案 |

### 3.6 暗时间（优先级 P1）

| 主题 | 素材位置 | 建议出卡 | 关键引用 |
|:---|:---|:---|:---|
| 暗时间定义 | 口述 1992-2002 行 | `concept-yitang-dark-time` | "你的脑力 CPU 不饱和，那个时间本质上是被占了，但脑力没有" |
| 暗时间利用案例 | 口述 2006-2046 行 | `concept-yitang-dark-time` / `case-truman-dark-time-experiments` | 听汇报写大纲、通勤路上写方案、现场辅导记灵感 |
| 暗时间 + 场景激发 | 口述 2012-2014 行 | `concept-yitang-dark-time` | "按时间 × 场景激发，是巨大的杀器" |
| 时间叠加 | 口述 1178-1184 行 | `concept-yitang-dark-time` | 一边交付一边跑步、一边听汇报一边写大纲 |

### 3.7 进阶与修养（优先级 P2）

| 主题 | 素材位置 | 建议出卡 | 关键引用 |
|:---|:---|:---|:---|
| L1-L6 修炼进阶 | 修炼进阶图 / 口述 2360-2382 行 | `yt-personal-time-management` | L1 忽略时间 → L6 持续迭代 |
| 三次飞跃 | 口述 736-756 行 / 1350-1368 行 | `yt-personal-time-management` | 从粗放到工具 → 从工具到建模 → 从建模到创新 |
| 六大自我修养 | 口述 1756-2204 行 | `yt-personal-time-management` | 破除工具迷信、善于选择工具、深刻理解任务、深刻理解时间、深刻理解匹配、理解背后原理、持续提出假设 |
| 刻意练习四要素 | 口述 2384-2414 行 | 桥接 `yt-personal-deliberate-practice` | 稳定模型、非舒适区、大量重复、持续反馈 |

---

## 四、卡片规格

### 4.1 首批 3 张卡

#### Card 1: `yt-personal-time-management`（concept 升级）

| 字段 | 要求 |
|:---|:---|
| **domain** | `personal-growth` |
| **confidence** | 0.85 |
| **trust_level** | medium |
| **source_refs** | 口述稿、笔记、整合笔记、5 张图解 |
| **核心内容** | ① 科学时间管理定义；② 课程边界；③ 三大流派批判；④ L1-L6 进阶地图；⑤ 三次飞跃；⑥ 六大自我修养 |
| **Critique** | 必须包含外部攻击者：Cal Newport「慢生产力」、Oliver Burkeman「4000 周」、以及「模型迷信」风险 |
| **Synthesis** | 桥接 `yt-personal-ipo-learning`、`yt-personal-deliberate-practice`、`yt-personal-knowledge-management` |
| **Action Triggers** | 至少 3 个可执行触发器 |

#### Card 2: `framework-yitang-time-management-triad`（framework 新建）

| 字段 | 要求 |
|:---|:---|
| **domain** | `personal-growth` |
| **confidence** | 0.88 |
| **trust_level** | medium |
| **source_refs** | 口述 358 行、整合笔记 35-51 行、口述 1770-2068 行 |
| **核心内容** | ① 三元模型定义；② 时间模型四层理解；③ 事情模型 L1-L5；④ 匹配模型三原则（大对大/小对小、双峰、暗时间）；⑤ 操作步骤 |
| **Critique** | 边界：不适用于高度响应型工作；层级划分有主观性 |
| **Synthesis** | 桥接 `concept-yitang-deep-work-iceberg`、`concept-yitang-bimodal-philosophy`、`concept-yitang-dark-time` |
| **diagnostic_signals** | 至少 5 个诊断信号 |

#### Card 3: `concept-yitang-deep-work-iceberg`（concept 新建）

| 字段 | 要求 |
|:---|:---|
| **domain** | `personal-growth` |
| **confidence** | 0.82 |
| **trust_level** | medium |
| **source_refs** | 口述 1574-1724 行、冰山图、vlm_summary |
| **核心内容** | ① L1-L5 五层定义与典型任务；② 水面上下分界；③ 层级错配与伪深度陷阱；④ Truman 写文案案例 |
| **Critique** | 外部攻击：Cal Newport Deep Work、心流理论边界、L4/L5 边界模糊 |
| **Synthesis** | 桥接 `framework-yitang-time-management-triad`、`yt-personal-deliberate-practice`、`concept-flow-state`（如有） |
| **Action Triggers** | 如何做一周时间审计、如何保护 L4/L5 时段 |

### 4.2 二批候选卡（首批终审后再评估）

| 卡片 | 类型 | 核心定位 |
|:---|:---|:---|
| `concept-yitang-dark-time` | concept | 暗时间定义、CPU 不饱和隐喻、Truman 实验案例、与多任务切换成本的边界 |
| `concept-yitang-bimodal-philosophy` | concept | 双峰哲学定义、分时策略、与 Cal Newport 四哲学的对照 |
| `tool-yitang-dual-loop-matrix` | tool | 双环矩阵四象限、工具选择逻辑、对称替换、操作步骤 |

---

## 五、关键纠偏与边界

1. **数字降级**：
   - ❌ 不得把 "5-10 倍效率跃迁"、"500% 差异" 作为事实陈述。
   - ✅ 应表述为「Truman 的课程主张/个人经验估计/激励性口号」。

2. **模型归属**：
   - L1-L6、三元模型、双环矩阵、冰山图均为 **一堂课程模型**，非普适心理学量表，需明确标注来源。
   - 艾森豪威尔矩阵/四象限引用时需说明 Eisenhower + Covey 来源。

3. **边界声明**：
   - 课程方法主要适用于 **知识工作者、管理者、内容创作者**。
   - 不适用于：任务单一且时间自主权极低的环境、高度响应型职业（急诊、客服、运维危机模式）。

4. **不覆盖**：
   - 不新建独立的 GTD/番茄/OKR 工具卡（已有相关素材或过于通用）。
   - 不讨论人生使命、家庭关系、精力管理（超出课程边界）。

---

## 六、验收标准

老顽童提交时必须满足：

1. **kdo pre-submit**：目标卡 3/3 PASS，无新增 ERROR。
2. **kdo lint**：目标卡 0 ERROR，新增 WARNING 需在任务单中说明。
3. **自攻击**：调用 `/kdo-self-attack` 对 3 张卡跑四路攻击，修复所有 🔴 致命问题和大部分 🟡 严重问题。
4. **source_refs**：所有关键 Claim 有来源引用；找不到真实源文件的用 `pending_archive` 占位。
5. **related**：每张卡至少 5 条有效 wikilink，优先桥接到 `yt-personal-ipo-learning`、`yt-personal-deliberate-practice`、`yt-personal-knowledge-management`。
6. **Critique**：每张卡必须包含至少 2 个外部反对者视角或失败模式。
7. **Action Triggers**：framework/concept 卡至少 3 个可执行触发器。

---

## 七、自攻击要点（老顽童生产前必读）

按 `framework-kdo-self-attack.md` 四路攻击：

- **逻辑攻击**：L1-L5 层级是否过于任意？L4/L5 边界是否清晰？
- **证据攻击**："5-10 倍"、"500%"、"60-65% 时间分配" 是否有证据？
- **完整性攻击**：是否遗漏了响应型工作者、创意工作者的反例？是否说明了切换成本？
- **时效性攻击**：Cal Newport 的 Deep Work（2016）在 2025-2026 年是否仍适用？

---

## 八、任务状态流转

- 当前状态：`queued`
- 领取后：`claimed-kimi`
- 生产完成 + pre-submit 通过：`pending_review`
- 欧阳锋终审通过：`reviewed`

---

*王语嫣 2026-07-01*
