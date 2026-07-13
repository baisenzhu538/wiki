---
id: tool-demand-rat-generator
title: RAT生成器：从L5洞察自动生成最危险假设清单
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-07-08
confidence: 0.85
trust_level: medium
language: zh-CN
created_at: 2026-07-08
updated_at: 2026-07-08
domain:
- yitang
- demand-analysis
source_refs:
- 00_inbox/五步法之需求分析/一堂-需求分析-需求评估-口述.txt L476-L536
- 00_inbox/五步法之需求分析/一堂-需求分析-方法论-口述.txt L2176-L2206
related:
- '[[tool-demand-iceberg-l5-forces]]'
- '[[tool-demand-iceberg-l6-hypothesis]]'
- '[[tool-demand-assessment-triangle]]'
- '[[tool-demand-chai-tui-ping-suan-guide]]'
- '[[framework-demand-ceiling-four-lines]]'
- '[[domain-demand-analysis-index]]'
- '[[yt-decision-y-model]]'
- '[[tool-demand-micro-experience-script]]'
- '[[tool-demand-option-explorer]]'
- '[[tool-demand-report-template]]'
diagnostic_signals:
- signal: 机会假设全是对的没有风险——"我们的假设都很靠谱"
  lens: RAT缺失——没有主动找"最可能错的地方"
  follow-up: 对每条假设追问"如果这条错了会怎样"——只有后果严重的才是RAT
quality_labels:
- actionable
- insight
---

# RAT生成器：从L5洞察自动生成最危险假设清单

> **一句话**：不是验证"你对的地方"，是找"哪里最容易错"。RAT（Riskiest Assumption Test）从L5四种力量的洞察中，提取3-5个一旦错了整个项目就垮的关键假设，并给出验证方法。

---

## 一、什么是RAT

RAT = Riskiest Assumption Test。口述稿 L476-L536，Truman：

> "机会假设必须有RAT——不是验证你对的地方，是找最容易错的地方。假设错了不可怕，可怕的是你不知道哪个假设错了。"

---

## 二、从L5到RAT的映射

| L5洞察类型 | RAT类型 | 典型问题 |
|:---|:---|:---|
| **推力**（用户想改变） | "用户真的想改变吗？" | 用户说痛但其实忍忍也能过 |
| **惯性**（用户不想动） | "惯性比自己想的更强？" | 替代方案比想象中好用 |
| **拉力**（新方案的吸引力） | "新方案真的更好吗？" | 试用期爽但长期留存差 |
| **焦虑**（对改变的担忧） | "用户到底在担心什么？" | 数据安全/学习成本/切换风险 |

---

## 三、RAT生成三步

### Step 1：列出所有假设
从L5机会假设中提取每条"我认为..."

### Step 2：打分排序
| 维度 | 评分标准 |
|:---|:---|
| **如果错了的后果** | 1=无所谓 / 3=方向要调 / 5=项目死了 |
| **现在的信心度** | 1=纯猜 / 3=有间接证据 / 5=已验证 |
| RAT分数 = 后果分 × (6 - 信心度) |

### Step 3：选取Top 3-5
分数最高的3-5条就是RAT——最危险假设。

---

## 四、RAT验证方法速查

| 假设类型 | 验证方法 | 成本 | 时间 |
|:---|:---|:---|:---|
| "用户痛" | 5个深度访谈 | 低 | 1周 |
| "竞品不行" | 竞品体验+用户切换访谈 | 低 | 1周 |
| "用户愿意付" | 预购/MVP付费测试 | 中 | 2-4周 |
| "市场够大" | 天花板测算 | 低 | 1天 |
| "能规模化" | 单元模型验证 | 中 | 2-4周 |

---

## 五、输出模板

```markdown
# RAT清单：[项目名称]

| # | 假设 | 如果错了 | 后果 | 信心度 | RAT分 | 验证方法 | 时间 |
|:--|:---|:---|:--:|:--:|:--:|:---|:--:|
| 1 | [假设] | [后果] | 5 | 2 | 20 | [方法] | 2周 |
| 2 | ... | ... | 4 | 3 | 12 | ... | ... |
| 3 | ... | ... | 3 | 2 | 12 | ... | ... |

## 验证顺序
1. 先验证RAT分最高的——如果这条对了，项目最危险的部分就解了
2. 每验证一条，更新信心度，重新算RAT分
3. RAT分全部降到12以下→进入下一步
```

## 六、常见失败

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| RAT太保守 | 列的假设"错了也无所谓" | 追问"这条错了项目会死吗？"——不会就删 |
| RAT太多 | 列了15条"最危险假设" | 强制只取Top 5 |
| 只列不验 | RAT清单写得很漂亮但不执行 | 每条RAT配deadline+负责人 |
