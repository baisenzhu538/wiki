# ⛔ 已废弃 — 2026-07-07

> **此文件不再维护。** 本任务已完成。当前任务领取见 `production-queue.md`。

---

# 老顽童执行任务单（历史档案）

> **发单人**：王语嫣  
> **执行人**：老顽童  
> **接收人/审批人**：欧阳锋  
> **日期**：2026-06-20  
> **来源**：`70_product/tasks/laowantong-batch-2026-06-20.md`

---

## 任务 1：Master 域 7 张卡规范化（优先级：P1）

### 任务概述

7 张 Master 域卡片已存在，但 frontmatter 不规范、source_refs 指向虚假 source、source_person/source_context 缺失。老顽童需接管并规范化，**不是重写正文**。

### 执行顺序

按 #6 → #1 → #2 → #3 → #4 → #5 → #7 执行：

| 序号 | 卡 ID | 标题 | 所在目录 |
|:---:|:---|:---|:---|
| #6 | `master-ai-info-literacy` | AI 信息素养框架 | `30_wiki/concepts/` |
| #1 | `master-cognitive-bias-diagnosis` | 认知偏差快速诊断清单 | `30_wiki/concepts/` |
| #2 | `master-decision-hygiene` | 决策卫生五步法 | `30_wiki/concepts/` |
| #3 | `master-first-principles` | 第一性原理 | `30_wiki/concepts/` |
| #4 | `master-systems-thinking` | 系统思考 | `30_wiki/concepts/` |
| #5 | `master-antifragile-checklist` | 反脆弱决策检查清单 | `30_wiki/concepts/` |
| #7 | `master-knowledge-compound` | 知识复利 | `30_wiki/concepts/` |

### 每张卡必做

1. **frontmatter 标准化**
   - `author: 老顽童`
   - `reviewed_by: 欧阳锋`
   - `review_date: '2026-06-20'`
   - `updated_at: '2026-06-20'`
   - 添加 `source_person` 和 `source_context`

2. **source_refs 替换**
   - 移除虚假 source（如 `10_raw/sources/src_20260503_52ae08ba-kdo_product_design_agent_final.md`）
   - 替换为 2–3 个真实存在的 source
   - 规范路径：`10_raw/sources/<filename>.md`

3. **confidence / trust 调整**
   - `confidence`：建议 0.75–0.78
   - `trust_level`：统一为 `medium`

4. **related 互链**
   - 保留现有有效 related
   - 补充至少 2 条 master 域内部互链
   - 如正文引用 yt-* 卡，检查并补双向链接

5. **内容格式检查**
   - 确保有「边界/失败模式」小节（表格形式，≥2 条适用边界 + ≥2 条失败模式）
   - 确保有「Action Checklist / 使用步骤」
   - 如 `diagnostic_signals` 仍在 frontmatter 中，移入正文并改为表格

6. **改完一张跑一张 lint**
   - 命令：`python 90_control/scripts/kdo_lint.py 30_wiki/concepts/<卡名>.md`
   - 禁止批量改后统一跑

### 推荐 source 素材池

| 素材主题 | 推荐 source 文件 |
|:---|:---|
| 科学决策 / ROI | `10_raw/sources/src_20260516_e7a0024e-一堂-科学决策-ROI决策高度实操课口述04.md` |
| 发现决策 | `10_raw/sources/src_20260522_1a2ffc3e-ocr-一堂-科学决策-发现决策.md` |
| 思考习惯 / 认知偏差 | `10_raw/sources/src_20260522_23b5714d-ocr-一堂-科学决策-高度-两种典型的思考习惯.md` |
| 决策经验值 | `10_raw/sources/src_20260522_4f3415a1-ocr-一堂-科学决策-深度-决策经验值.md` |
| 关键假设 / 第一性 | `10_raw/sources/src_20260522_3261e6bd-ocr-一堂-科学决策-关键假设abcd模型.md` |
| 关键训练清单 | `10_raw/sources/src_20260522_ac7f8874-ocr-一堂-科学决策-关键训练清单重要.md` |
| 双三角 / 系统思考 | `10_raw/sources/src_20260522_d96543bb-ocr-一堂-科学决策-一堂双三角磨合追求-从入门到无限进步.md` |
| 决策三角形 | `10_raw/sources/src_20260522_f3429a35-ocr-一堂-科学决策-决策三角形.md` |
| 人机协作 / 信息素养 | `10_raw/sources/src_20260522_33c40d41-ocr-一堂-科学决策-人机协作决策.md` |
| 知识萃取 | `10_raw/sources/src_20260614_239c9f4e-一堂-知识萃取探索营.md` |
| 通用学习 / 思维 | `10_raw/sources/src_20260522_0af1f6dd-learning-thinking.md` |
| 批判性思维 | `10_raw/sources/src_20260524_836ad51c-学会提问在信息洪流中锻造批判性思维的利刃.md` |
| AI Native 五层进阶 | `10_raw/sources/src_20260524_3cadf228-ai-native-五层进阶从答案到效率到作品到产品到系统.md` |
| 萃取总结 | `10_raw/sources/src_20260510_14db4c2b-萃取总结.md` |

### 7 张卡 source 建议分配

| 卡 ID | 建议 source（选 2–3 个） | source_person | source_context |
|:---|:---|:---|:---|
| `master-ai-info-literacy` | 人机协作决策 + 学会提问 + 知识萃取探索营 | 王语嫣/一堂科学决策课程 + 公开著作 | 一堂科学决策课程、知识萃取探索营与《学会提问》公开阅读笔记综合 |
| `master-cognitive-bias-diagnosis` | 两种典型思考习惯 + 决策经验值 + 关键训练清单 | 王语嫣/一堂科学决策课程 | 一堂科学决策课程中关于思考习惯、决策经验值与关键训练清单的笔记综合 |
| `master-decision-hygiene` | 发现决策 + 关键训练清单 + ROI 决策口述 | 王语嫣/一堂科学决策课程 | 一堂科学决策课程关于发现决策、关键训练清单与 ROI 实操的笔记综合 |
| `master-first-principles` | 关键假设 ABCD 模型 + 知识萃取探索营 + learning-thinking | 王语嫣/一堂科学决策课程 + 公开学习材料 | 一堂科学决策课程关键假设模型、知识萃取探索营与通用学习方法论综合 |
| `master-systems-thinking` | 双三角磨合 + 决策三角形 + AI Native 五层进阶 | 王语嫣/一堂科学决策课程 + AI Native 方法论 | 一堂科学决策课程双三角/决策三角形与 AI Native 五层进阶方法论综合 |
| `master-antifragile-checklist` | 决策经验值 + 关键训练清单 + ROI 决策口述 | 王语嫣/一堂科学决策课程 | 一堂科学决策课程关于决策经验值、关键训练清单与 ROI 实操的笔记综合 |
| `master-knowledge-compound` | 知识萃取探索营 + learning-thinking + 萃取总结 | 王语嫣/一堂知识萃取课程 | 一堂知识萃取探索营与学习/萃取方法论综合 |

### 验收标准

- [x] 7 张卡 frontmatter 均含 `source_person`、`source_context`、真实 `source_refs`
- [x] `author=老顽童`，`reviewed_by=欧阳锋`，`review_date=2026-06-20`
- [x] `confidence=0.92`，`trust_level=high`（最终验收确认）
- [x] `source_person=Truman`，`source_context` 精确化为"课程名——具体主题"
- [x] `source_refs` 路径标准化为无前缀形式（`src_<hash>-... .md`）
- [x] 每张卡 related 互链 ≥5 条
- [x] 每张卡有「边界/失败模式」表 + Action Checklist
- [x] 7 张全部完成后质量门禁无新增 P0/P1

### 完成状态

✅ **已完成并验收通过**（2026-06-20）

---

## 任务 2：调研方法论域拆卡（优先级：P1，资料已到位）

### 任务概述

欧阳锋已将 `business-research skill v2.1.0` 归档到：

```
10_raw/sources/src_20260620_business-research-skill-v2.1.0/
├── SKILL.md                          # 主文档：OSCAR + 13 武器体系 + Step 0-15 工作流
├── references/
│   ├── ach-methodology.md            # ACH 竞争假设矩阵
│   ├── analysis-frameworks.md        # 竞争格局分析框架
│   ├── bias-checklist.md             # 偏见级联检查清单
│   ├── ci-platforms.md               # 信息哨兵系统与 CI 平台
│   ├── databases-index.md            # 关键数据库索引
│   ├── market-sizing.md              # 市场规模估算方法论
│   ├── report-guide.md               # 报告配图与排版规范
│   ├── research-principles.md        # AI 调研十原则
│   ├── style-guide.md                # 商业调研报告 Style Guide
│   └── weapon-action-templates.md    # 13 武器行动模板
└── templates/
    ├── fact-card.md                  # 事实卡片模板
    ├── report-structure.md           # 报告结构模板
    └── weapon-checklist.md           # 武器检查清单模板
```

老顽童需基于以上素材，将调研方法论拆分为标准 30_wiki 卡片。**优先复用工单中已有的 8 个调研域卡 ID**，不足时再新建。

### 必拆卡片清单（至少 8 张）

| 卡 ID | 类型 | 标题 | 主要素材来源 |
|:---|:---:|:---|:---|
| `yt-research-osl-framework` | framework | OSL调研五步法：一堂通用商业调研框架 | `SKILL.md` 中 OSCAR 方法论 + Step 0-2 |
| `yt-research-intelligence-map` | framework | 情报获取全景地图：13+渠道穷尽手段 | `SKILL.md` Step 2 武器决策表 + `databases-index.md` |
| `yt-research-competitor-toolkit` | tool | 竞品拆解工具包：三层分类+内核边界+单元模型对标 | `SKILL.md` 武器1/2/4/5 + `analysis-frameworks.md` |
| `yt-research-expert-interview` | tool | 专家访谈工具：2小时获取行业共识的标准流程 | `SKILL.md` 武器10 + `weapon-action-templates.md` |
| `yt-research-user-jtbd` | tool | 用户深度访谈工具：JTBD视角区分“说的”和“真正要的” | `SKILL.md` 武器3 + `weapon-action-templates.md` |
| `yt-research-industry-canvas` | tool | 行业分析画布：五维快速扫描+二维定位 | `SKILL.md` 武器11/12/13 + `market-sizing.md` |
| `yt-research-hypothesis-test` | tool | 假设验证调研工具：关键假设→可证伪问题→最小实验 | `SKILL.md` Step 7-8 + `ach-methodology.md` |
| `yt-research-mindset` | concept | 调研认知升级：从“原创自信”到“情报驱动” | `SKILL.md` 核心理念 + `research-principles.md` |

### 可选扩展卡片（如 8 张核心卡拆完后仍有余力）

| 卡 ID | 类型 | 标题 | 素材来源 |
|:---|:---:|:---|:---|
| `yt-research-source-rating` | concept | 信源分级与事实卡片：五级评分体系 | `SKILL.md` Step 6 + `templates/fact-card.md` |
| `yt-research-pre-mortem` | tool | Pre-Mortem 反向证据门：在拍板前先找反例 | `SKILL.md` Step 8 + `bias-checklist.md` |
| `yt-research-market-sizing` | tool | 市场规模估算三角验证法 | `market-sizing.md` |
| `yt-research-ci-platforms` | tool | 商业情报信息哨兵系统搭建指南 | `ci-platforms.md` |
| `yt-research-report-style` | tool | 商业调研报告 Style Guide | `style-guide.md` + `report-guide.md` |

### 拆卡原则

1. **不是搬运**：每张卡必须提炼出「一句话讲清楚 + 核心洞察 + 边界/失败模式表 + Action Checklist + ≥2 条互链」。
2. **source 规范**：每张卡 `source_refs` 必须指向 `10_raw/sources/src_20260620_business-research-skill-v2.1.0/` 下的具体文件，并精确到相关小节/段落。
3. **避免重复**：8 张核心卡之间应有清晰边界，不要把 OSCAR 全部内容塞进第一张卡。
4. **confidence 控制**：基于单一 Skill 素材拆出的工具/框架卡，`confidence` 建议 0.75–0.78，`trust_level` 建议 `medium`。
5. **互链优先**：新卡之间先互链；与已有 yt-research-*、yt-decision-*、yt-entrepreneur-* 卡建立反向链接。
6. **改一张跑一张 lint**：`python 90_control/scripts/kdo_lint.py 30_wiki/<目录>/<卡名>.md`

### 验收标准

- [ ] 至少完成 8 张核心卡
- [ ] 每张卡 frontmatter 完整（含 source_person / source_context / source_refs / author / reviewed_by）
- [ ] 每张卡有边界/失败模式表 + Action Checklist
- [ ] 每张卡 ≥2 条互链
- [ ] 全库 lint 无新增 ERROR
- [ ] 全库质量门禁 P0/P1 无新增
- [ ] 调研域 index（`30_wiki/index.md` 或等效位置）已更新

---

## 任务 3：KF-021 收尾协助（已完成，无需执行）

**状态**：✅ 已完成（2026-06-18 验收通过）。

- 33 张 content 卡已全部处理（18 张降级 draft，15 张保留 enriched/stable）
- 验收报告：`60_feedback/audit/kf-021-section22-final-acceptance-2026-06-18.md`
- 无需老顽童再执行

---

## 严禁事项

- ❌ 不要批量改卡后统一跑 lint——改一张跑一张
- ❌ 不要编造 source 或数字——找不到就标“待验证”
- ❌ 不要把策略和话术/表达混存在同一个文件
- ❌ 不要写“步骤跳过→严格按步骤执行”这种模板化失败模式
- ❌ 不要在新卡里用王语嫣/欧阳锋作为 author（老顽童是 author，reviewed_by 才写欧阳锋）
- ❌ 不要动 `concept-card-index-latest.md` 的 P0 问题——那是黄药师的脚本问题

---

## 完成回执

老顽童每完成一个任务，请在此文件末尾追加完成小结，并通知欧阳锋审查。

### 建议执行顺序

1. **先执行任务 1（Master 域 7 张卡）**：每张卡改动范围小，容易快速验证标准。
2. **再执行任务 2（调研域拆卡）**：工作量较大，建议先做 3 张核心卡（`yt-research-osl-framework`、`yt-research-intelligence-map`、`yt-research-mindset`）让欧阳锋抽检，通过后再继续。

