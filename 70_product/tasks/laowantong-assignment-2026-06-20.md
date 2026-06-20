# 老顽童执行任务单

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

- [ ] 7 张卡 frontmatter 均含 `source_person`、`source_context`、真实 `source_refs`
- [ ] `author=老顽童`，`reviewed_by=欧阳锋`，`review_date=2026-06-20`
- [ ] `confidence` 0.75–0.78，`trust_level=medium`
- [ ] 每张卡 ≥2 条 master 域内部互链
- [ ] 每张卡有「边界/失败模式」表 + Action Checklist
- [ ] 每张卡单独跑 lint 无 ERROR
- [ ] 7 张全部完成后跑 `python 90_control/scripts/kcard-quality-gate.py`，确认 P0/P1 无新增

---

## 任务 2：调研方法论域 8 张卡（暂缓，等待欧阳锋输入资料）

**状态**：暂缓。欧阳锋表示还需输入大量资料，暂不启动。

| 卡 ID | 类型 | 标题 |
|:---|:---:|:---|
| `yt-research-osl-framework` | framework | OSL调研五步法：一堂通用商业调研框架 |
| `yt-research-intelligence-map` | framework | 情报获取全景地图：13+渠道穷尽手段 |
| `yt-research-competitor-toolkit` | tool | 竞品拆解工具包：三层分类+内核边界+单元模型对标 |
| `yt-research-expert-interview` | tool | 专家访谈工具：2小时获取行业共识的标准流程 |
| `yt-research-user-jtbd` | tool | 用户深度访谈工具：JTBD视角区分“说的”和“真正要的” |
| `yt-research-industry-canvas` | tool | 行业分析画布：五维快速扫描+二维定位 |
| `yt-research-hypothesis-test` | tool | 假设验证调研工具：关键假设→可证伪问题→最小实验 |
| `yt-research-mindset` | concept | 调研认知升级：从“原创自信”到“情报驱动” |

**素材来源**：
- `00_inbox/ideas/一堂-创业必修-调研武器库.md`
- `00_inbox/ideas/一堂-创业必修-调研行动营.md`
- `00_inbox/ideas/一堂-创业-调研行动营口述01.md`
- `00_inbox/ideas/一堂-创业必修-需求分析.md`
- 已有 `yt-research-action-camp-launch.md`、`yt-research-weaponry-course.md`

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

老顽童完成任务 1 后，请在此文件末尾追加完成小结，并通知欧阳锋审查。

