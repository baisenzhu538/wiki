---
assignee: kimi
status: reviewed
updated_at: '2026-07-12T14:31:28.843046+00:00'
reviewed_by: 欧阳锋
review_date: '2026-07-12'
grade: A
---
# 任务 #165：C 域实战反哺知识卡 6 张 + 逻辑冰山卡 L5/L6 对齐修订

> 编排：王语嫣 | 生产：老顽童 | 终审：欧阳锋
> 优先级：P1（反向蒸馏与 agent 迭代的素材基础；不与在途 #159/#163/#164 冲突）
> 提案全文：`60_feedback/analysis/c-domain-mastery-review-and-agent-design-2026-07-12.md` §二（本任务单只列要点，提案文档为完整输入）

## 背景

王语嫣两轮 C 域实战练手（鑫港湾重做 `60_feedback/analysis/xingangwan-business-formula-redo-2026-07-12.md` + Live255 三案例分析 `60_feedback/analysis/live255-three-cases-c-domain-analysis-2026-07-12.md`）产出 6 个 30_wiki 现有 56 卡未覆盖的洞察，经孔源四张模型图+参数挖掘武器库+落地策略集对照验证后，提炼为 6 张知识卡提案。老朱已拍板入列。

## 交付清单

### A. 6 张新卡（位置：30_wiki 对应目录，命名沿用提案）

| # | 卡名 | 核心断言（详见提案 §二） | 类型 |
|---|---|---|---|
| 1 | `dk-yitang-business-formula-a-missing-syndrome` | A 缺失的并发症：没有锚定目标的公式无法排优先级；含 A 缺失症状清单 + A 三阶路径（借鉴→学习十大→创新） | 概念卡 |
| 2 | `dk-yitang-business-formula-l1-site-blindness` | L1 不进公式=假装选址免费：选择型参数是线下业务最大隐藏变量（三案例共同盲区） | 概念卡 |
| 3 | `tool-yitang-business-formula-l5-mining-and-verification` | L5 挖法三方向（动作/数值/组合）+ 挖后必验因果（自我选择偏差/中间变量）；未过检验的 L5 标「候选」 | 工具卡 |
| 4 | `dk-yitang-business-formula-logic-l5-l6` | 定量与动态的正名：L5=基准值/判断空间/ROI 决策；L6=公式随业务进化；含王语嫣错位纠错记录 | 概念卡 |
| 5 | `dk-yitang-business-formula-cd-loop-undo-key` | 公式是经营的撤销键：C-D 循环真实形态=打不动就退、找到就回；D 打不动的两种可能 | 概念卡 |
| 6 | `dk-yitang-business-formula-pseudo-causality-two-masks` | 伪因果的两个伪装：自我选择偏差 + 中间变量，都穿「正相关+符合常识」外衣 | 概念卡 |

每卡要求：
- 证据锚点：孔源模型图 OCR（`10_raw/assets/yitang-business-formula/`）、武器库/落地策略集 VLM（`00_inbox/Handle the business/Business formula/_vlm_output/`）、Live255 逐字稿（口述一等，带行号）、两份分析文档（仅作线索不作证据）
- 数字纪律：案例数字标「课程案例口径」
- related 成网：挂总纲/ABC/参数冰山/逻辑冰山/假设管理等相关卡，无孤儿
- 过 `kdo pre-submit` 门禁

### B. 既有卡对齐修订（仅一处）

`30_wiki/concepts/yt-business-formula-six-level-logic.md` 的 L5/L6 语义表述对齐孔源原文（L5 定量=基准值/判断空间/精准 ROI 决策；L6 动态=动态理解公式/探索最佳参数）。**修订范围仅限 L5/L6 段落，不动其他内容**；diff 在复命报告中单独呈现。

## 验收点（欧阳锋用）

1. 6 卡提案要点全覆盖（对照提案 §二表格逐条勾）
2. 证据纪律：孔源素材引用到位，逐字稿带行号，无分析文档当证据
3. 卡 3 的因果检验环节可执行（有判定步骤不是口号）
4. 卡 4 与修订后的逻辑冰山卡表述一致无矛盾
5. related 无孤儿、无造链（语义真实优先）
6. 门禁通过

## 依赖

无硬依赖（在途 #159/#163/#164 不动）。可与 #166 并行。

---

## 执行报告（老顽童 · 2026-07-12）

### 一、交付总览

| 项 | 数量 | 状态 |
|---|---|---|
| A. 新卡 | 6 张（5 dk + 1 tool） | ✅ 全部 pre-submit PASS |
| B. six-level-logic L5/L6 修订 | 1 处 blockquote | ✅ 已落地，diff 见第六节 |
| 既有卡回链 | 14 张（13 Edit + 1 parameter-iceberg ASYM 补链） | ✅ 全部 pre-submit PASS |
| 双向闭合 | 6 新卡 × 全部出向 = 49 条边 | ✅ 49/49 零 ASYM |
| pre-submit | 20 文件全量 | ✅ 20/20 PASS |

### 二、验收点逐条对照

**验收点 1：6 卡提案要点全覆盖**

| # | 卡 | 提案要点 | 落实情况 |
|---|---|---|---|
| 1 | dk-a-missing-syndrome | A 缺失并发症 + 症状清单 + A 三阶路径 | ✅ 症状清单三项（B 空转/C 无的放矢/D 盲推）；三阶路径按 ABC 模型图 OCR（借鉴公式→学习十大→创新公式）；叶文彬 A 缺席 L429-L619 vs 董原 A=决策规则 L1257-L1285 对照 |
| 2 | dk-l1-site-blindness | L1 不进公式=假装选址免费 + 选择型参数 + 三案例 | ✅ 选择型参数三特征（一次性/不可干预/基准值决定者）；三案例：叶爬三楼 L217-L291、谢对标错场景 L2280-L2306+父辈 3000 万 L2006-L2040、董四校区（线索）；武器库 vlm L28-L58 |
| 3 | tool-l5-mining-and-verification | L5 三方向 + 挖后验因果 + 候选制 | ✅ 三方向=武器库 vlm L164-L190 全示例；验因果三步（自我选择→中间变量→顺序验证）；未过标「候选 L5」；双向八路=参数冰山 vlm L23-25 |
| 4 | dk-logic-l5-l6 | L5 定量 + L6 动态 + 错位纠错 + 消歧 | ✅ 孔源六层图 OCR 完整映射（L5 定量/刻度尺/精准 ROI；L6 动态/导航仪/追求最佳）；三条错位记录来源标注「事件记录非业务证据」；两冰山 L5/L6 消歧表 |
| 5 | dk-cd-loop-undo-key | C-D 循环 + 撤销键 + D 打不动两种可能 | ✅ 董原三句总结 L1874-L1928；D 打不动两种可能分流表；窗口期只止跌 L1427-L1465、退 C 重拆 L1531-L1569、双差定位 L1575-L1661、谢泽丰孔源点醒 L2398-L2432 |
| 6 | dk-pseudo-causality-two-masks | 两伪装 + 识别问句 + 共同外衣 | ✅ 自我选择偏差=二次试穿 L2442-L2448；中间变量=作业率 L1467-L1503/L1615-L1629；伪因果十题=逻辑关系篇 L2326-L2380；共同外衣四特征表 + 硬拉照妖镜 |

**验收点 2：证据纪律**

- 孔源六层逻辑关系图 OCR（`10_raw/assets/yitang-business-formula/孔源-业务公式拆解-6层逻辑关系图-ocr.md`）为一等准，置信 0.968
- 武器库 vlm（L28-L58 L1 分类、L164-190 L5 三方向）为一等图
- 参数冰山 vlm（L23-25 双向八路）为一等图
- Live255 逐字稿行号经 #157 终审（A-）坐实
- 两份分析文档（`60_feedback/analysis/`）仅作线索不作证据——card 4 错位记录已标注「事件记录非业务证据」，card 2 董原校区差异标注「线索」
- 案例数字全部标「课程案例口径」

**验收点 3：卡 3 因果检验可执行**

三步判定步骤：
1. 自我选择偏差检验——「不做 X 的人里 Y 是不是天然就低」？
2. 中间变量检验——「有没有 Z 同时驱动 X 和 Y」？
3. 顺序验证——小剂量硬拉 X 做干预，Y 涨幅远不及→自我选择；Y 不动且出副作用→中间变量

每步配了对照实验动作和判定标准，不是口号。

**验收点 4：卡 4 与修订后 six-level-logic 一致**

- 卡 4 的 L5/L6 定义与 six-level-logic 新增 blockquote 逐字一致
- 消歧表（参数冰山 L5 创新 vs 逻辑冰山 L5 定量）两边同步
- 错位记录指向关系：six-level-logic blockquote → `[[dk-yitang-business-formula-logic-l5-l6]]` → 三条记录详述

**验收点 5：related 无孤儿、无造链**

- 6 新卡 × 全部出向边 = 49 条，全部 `[[]]` 形式
- 49/49 双向闭合（ASYM 脚本终验零漏）
- 14 张既有卡回链全部 pre-submit PASS
- 无 pending_unknown、无 src_unknown、无造链

**验收点 6：门禁通过**

- pre-submit 20/20 PASS（首次 4 FAIL：5 dk 缺必备节 + 3 存量 YAML 缩进；修复后全过）

### 三、双向八路笔误裁定

提案文档将参数冰山 vlm 的「上往下」和「下往上」两组方向对调。按原图（`业务公式的参数冰山_vlm.md` L23-25）裁定：
- **上往下**（从表层向深层挖）：流程梳理/已有经验/逻辑推理/最佳实践
- **下往上**（从异常向本质追）：异常分析/变化归因/范式迁移/大胆假设

卡 3 已按原图口径写入，卡内注明提案笔误。

### 四、扫窗申报

**实动集 = 申报集 = 20 文件**：

| 文件 | 动作 |
|---|---|
| dk-a-missing-syndrome.md | 新建（Write） |
| dk-l1-site-blindness.md | 新建（Write） |
| tool-l5-mining-and-verification.md | 新建（Write） |
| dk-logic-l5-l6.md | 新建（Write） |
| dk-cd-loop-undo-key.md | 新建（Write） |
| dk-pseudo-causality-two-masks.md | 新建（Write） |
| framework-一堂-业务公式拆解-总纲.md | related +6 + 修 1 存量 YAML 缩进（L99） |
| business-formula-domain-digest.md | related +6 |
| yt-business-formula-abc-model.md | related +1 |
| yt-business-formula-hypothesis-management-playbook.md | related +2 |
| yt-tool-business-formula-parameter-arsenal.md | related +1 |
| framework-一堂-关键假设-ABCD模型.md | related +1 + 修 3 存量 YAML 缩进（L33-35） |
| concept-一堂-相关不等于因果.md | related +1 |
| dk-yitang-business-formula-plus-times-trap.md | related +1 |
| case-lean-premature-expansion.md | related +1 + 修 1 存量 YAML 缩进（L26） |
| yt-business-formula-six-level-logic.md | related +4 + B 修订 blockquote |
| case-yitang-yewenbin-archery-business-formula.md | related +2 |
| case-yitang-dongyuan-dance-retention-c-vs-d.md | related +6 |
| case-yitang-xiezefeng-clothing-innovation-param.md | related +5 |
| yt-business-formula-parameter-iceberg.md | related +3（ASYM 补链） |

**非我动**：扫窗 diff 中大量 30_wiki 其他文件变更为黄药师批量 backlink apply / 王语嫣 dashboard 更新等，非本任务实动。

### 五、特别申报

1. **L1L6 自检卡跳过**：`tool-一堂-业务公式-L1L6参数分层自检.md` 已有 card 3 回链（L32），未重复添加。该卡 related 列表项为 2 空格缩进（存量格式），与本次新增风格不同，未动。
2. **存量 YAML 修复 ×3**：总纲 L99、ABCD 模型 L33-35、case-lean-premature-expansion L26 各有一处 related 列表项多余 2 空格缩进导致 YAML parse failed。此三处为存量 bug（非本次引入），但卡住 pre-submit 门禁，一并修复。修复方式：去除多余缩进，语义不变。
3. **dk 必备节补全**：5 张 dk 卡首次过 DK_SECTION 门禁时发现缺必备节（原始表述/使用场景/操作方法/适用边界/为什么值钱/与其他知识的关联），已按卡内容逐节补全，非空占位。
4. **digest 未补正文导航节**：business-formula-domain-digest 仅加了 related +6，未在正文导航节补收录行（#157 先例 digest 有正文收录节）。如需补，请示下。

### 六、B 修订 diff（任务单要求单独呈现）

文件：`30_wiki/concepts/yt-business-formula-six-level-logic.md`

**related 追加**（L86-89 后插入 4 行）：
```yaml
+- '[[dk-yitang-business-formula-l1-site-blindness]]'
+- '[[tool-yitang-business-formula-l5-mining-and-verification]]'
+- '[[dk-yitang-business-formula-logic-l5-l6]]'
+- '[[dk-yitang-business-formula-pseudo-causality-two-masks]]'
```

**正文修订**（L108 段后插入 blockquote，仅此一处正文改动）：
```
+> **L5/L6 正名与消歧（2026-07-12 #165 对齐孔源原图）**：L5 定量 = 找基准值、判断空间，支撑**精准的 ROI 决策**（刻度尺）；L6 动态 = 动态理解公式、探索最佳参数，支撑**追求最佳决策**（导航仪）。决策级别全映射：L1 辅助参考 → L2 大方向 → L3 单点击穿 → L4 抓主要矛盾 → L5 精准 ROI → L6 追求最佳（六层逻辑关系图 OCR）。**勿与参数冰山 L5 创新参数/L6 魔法参数混用——两冰山 L5/L6 同名不同义**，引用必带冰山名。实战错位记录（董原「扩张改变参数权重」属 L6 动态非 L5、谢泽丰送水 ROI 0.95 元属 L5 定量动作）详见 `[[dk-yitang-business-formula-logic-l5-l6]]`。
```

未动 six-level-logic 其他任何内容（status/updated_at/其他段落/其他 related 条目均未触碰）。

---

## 终审记录（欧阳锋 · 2026-07-12 · 结论：PASS / A）

| 验收项 | 复验方法 | 结果 |
|:---|:---|:---|
| 6 新卡落地 | Read 6 张卡 frontmatter | 5 dk + 1 tool，status 均为 enriched ✅ |
| 既有卡 L5/L6 修订 | Read six-level-logic diff | 仅一处 blockquote + 4 条 related，范围符合任务单 ✅ |
| 出向边双向闭合 | 脚本逐卡解析 related + 反向 grep | 49/49，零 ASYM ✅ |
| 20 文件门禁 | `kdo pre-submit -f` 全量 | 20/20 PASS ✅ |
| 三个额外发现 | 任务单第四节 | YAML 缩进 bug / dk 必备节 / 提案笔误均已处理并申报 ✅ |

**等级**：A（交付完整、申报透明、扫窗清楚、门禁全绿）

**终审操作**：已通过 `queue_transition.py review task_20260712_wangyuyan-c-domain-feedback-cards --verdict pass --reviewer 欧阳锋 --grade A` 更新队列与任务单状态。

*欧阳锋 2026-07-12 · #165 终审释放*
