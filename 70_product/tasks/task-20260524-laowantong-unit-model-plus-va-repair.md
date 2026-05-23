---
title: "老顽童任务：单元模型域编译 + VA 交叉审查修复"
assigned_to: "老顽童 (Producer)"
priority: "P0"
created_at: "2026-05-24"
reviewer: "欧阳锋"
status: "in_progress"
last_update: "2026-05-24 欧阳锋审查：Part A 7/7 ✅。Part B 7/10 完成（#1-6✅ #7✅ #8✅），3 条未完成（#9 #10 #14）。"
depends_on: []
blocks: []
---

# 老顽童任务：单元模型域编译 + VA 交叉审查修复

## 背景

两件事合一个任务书：

1. **主线**：单元模型域全量编译（已在 [[70_product/tasks/task-20260524-laowantong-unit-model-domain]] 下发，尚未开工）
2. **顺手修**：洪七公 VA 交叉审查终报的修复清单（35 张图全部审完，报告在此：[[60_feedback/corrections/va-cross-review-scientific-decision-2026-05-23-final]]）

另：用户读后感已交付 ✅（额外任务，不计入本任务指标）。

---

## Part A：单元模型域全量编译（主线）

素材：`00_inbox/单元模型/` — 5 口述稿 + 31 知识地图/框架图

执行流程参照 [[70_product/tasks/task-20260524-laowantong-unit-model-domain]]：
1. 读素材 + 理解方法论全景
2. 出 Card Map → 欧阳锋审批
3. 逐张编译（clean-transcript → ingest → 三步编译）
4. 每 5 张汇报一次

**四条纠偏仍然有效**（见原任务书）：
- 别碰 A 类（断链/frontmatter/格式是黄药师的活）
- Critique 要 5W1H + 具体失效机制
- 案例要有区分度（≥2 类型）
- Synthesis 关联说明 >30 字
- 不要规划路线图，打开素材直接做

---

## Part B：VA 交叉审查修复（顺手修，穿插做）

**来源**：洪七公终报—35 张原图逐图审查。欧阳锋已裁断：**颜色不纳入 VA。** 以下修复清单已剔除全部颜色类 bug。

### 🔴 重写（6 处，VA 张冠李戴——原 VA 写给了另一张图）

| # | 卡片 | 修复内容 |
|:---|:---|:---|
| 1 | `yt-decision-canvas` | ROI画布主图 VA — 从四象限→三栏表格矩阵 |
| 2 | `yt-decision-canvas` | ROI画布-案例01 VA — 从蓝/橙色块→黑白灰表格 |
| 3 | `yt-decision-width-method` | 宽度-企业 VA — 从四象限矩阵→双栏列表+底部通栏 |
| 4 | `yt-decision-width-method` | 宽度-团队 VA — 从三栏式→双栏+底部通栏 |
| 5 | `yt-decision-y-model` | 一堂双三角磨合追求 VA — 从坐标系→三个递进三角形 |
| 6 | `yt-decision-full-process` | 关键训练清单 VA — 从交通灯/T型→三列矩阵表格 |

### ⚠️ 小修（4 处，虚构元素或过度解读）

| # | 卡片 | 修复内容 |
|:---|:---|:---|
| 7 | `yt-decision-ai-partner` | 删除虚构"齿轮"隐喻，改为"双向箭头=增强回路" |
| 8 | `yt-decision-canvas` | 案例02 "N/A=认知断裂"→"N/A=无明显成本" |
| 9 | `yt-decision-depth-ladder` | 深度-L2 VA 删除虚构字母 C/D/Y/Z |
| 10 | `yt-decision-depth-ladder` | 深度-L3 VA 补遗漏的 A+B+C+D 描述 |

### 📋 结构性修复（4 处）

| # | 卡片 | 修复内容 |
|:---|:---|:---|
| 11 | `yt-decision-depth-ladder` | source_refs 补缺失的 6 张图（案例02/03/04/06、抽样实验、决策经验值） |
| 12 | `yt-decision-full-process` | source_refs 补缺失的 2 张图（双三角、关键训练清单） |
| 13 | `yt-decision-y-model` | source_refs 补缺失的 2 张图（双三角、ABCD） |
| 14 | `yt-decision-abcd-model` | VA 从正文移至 frontmatter，补 `00_inbox/` source_ref |

### 穿插规则

- 单元模型域每做完 5 张后，顺手修 2-3 条 VA 修复
- 修复完成后跑 `kdo validate --v15 --card <id>` 确认不引入新问题
- 不改动已有 Critique / Synthesis / Reusable Knowledge 内容

---

## 验收

| # | 验收项 | 判定 |
|:--:|------|:--:|
| A1 | 单元模型域 Card Map 提交审批 | 人工 |
| A2 | 全部卡片通过 `kdo validate --v15` | exit 0 |
| A3 | Critique ≥2 攻击者 + 不要用场景 ≥2 + AT ≥3（每卡） | 验证 |
| B1 | 14 条 VA 修复全部到位 | 逐条 grep |
| B2 | 修复不引入 regressions（已有 Critique/Synthesis 不改动） | diff 审查 |

## 不做什么

- **不做** 颜色类修复（洪七公报告里的小修 #5/6/7/8 颜色部分，已作废）
- **不做** A 类脚本化修复（断链/frontmatter/格式）
- **不做** AI学习域

## 进度表

| Part | 目标 | 已完成 | 备注 |
|:--:|:--:|:--:|:---|
| A | 单元模型域全量编译 | 7/7 ✅ | overview/ladder/selection/construction/benchmark/dynamic/ai-assisted 全部 v1.5 |
| B | VA 修复 14 条 | 10/14 | #1-8 ✅，#9 #10 #14 ⚠️ 待修 |

### Part B 剩余 3 条（2026-05-24 审查结论）

**⚠️ 注意**：以下是我（欧阳锋）逐条 grep 验证后的结论——不是估计，是实测。

#### ✅ 已修复（无需再动）

| # | 卡片 | 验证 |
|:--:|:---|:---|
| 7 | `yt-decision-ai-partner` | `grep 齿轮` 返回 0。VA 已改为"双向箭头=增强回路"。✅ |
| 1-6 | canvas/width-method/y-model/full-process | VA 重写到位 ✅ |
| 8 | canvas 案例02 | "N/A=认知断裂"→"N/A=无明显成本" ✅ |

#### ❌ 未完成（需要你做）

| # | 卡片 | 当前状态 | 具体操作 |
|:--:|:---|:---|:---|
| 9 | `yt-decision-depth-ladder` | L3 VA 第137行仍有 `红A+B+C+D=产出分子/定钱终点；绿Y=投入分母/定量过程；黑X/Z=未激活基础项` | 删除该句中 A/B/C/D/Y/X/Z 字母赋值。改为纯空间/结构描述 |
| 10 | `yt-decision-depth-ladder` | L3 VA 缺少 A+B+C+D 四项内容的文字描述 | 补充：A.商业场景/B.决策场景/C.增长场景/D.转化场景 对应的视觉表达（从原图看图写，不用虚构字母） |
| 14 | `yt-decision-abcd-model`（在 `30_wiki/frameworks/`） | VA 仍在正文 `## 视觉结构分析（Visual Analysis）` 节，未移至 frontmatter | 将正文 VA 内容压缩为 `visual_analysis` 字段写入 frontmatter（参考 `yt-decision-ai-partner` 的写法）。正文只留 `## 核心定义` 起的内容 |

### 穿插规则（不变）

- 单元模型域每做完 5 张后，顺手修 2-3 条 VA 修复
- 修复完成后跑 `kdo validate --v15 --card <id>` 确认不引入新问题
- 不改动已有 Critique / Synthesis / Reusable Knowledge 内容

---

*欧阳锋 · 2026-05-24*
*VA 修复清单已剔除颜色类 bug。读后感已交付 ✅（额外任务）。*
