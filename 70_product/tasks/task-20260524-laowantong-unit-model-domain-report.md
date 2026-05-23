# 单元模型域编译完工报告

**Report ID**: RPT-20260524-UNIT-MODEL  
**Compiler**: 老顶童  
**Date**: 2026-05-24  
**Task**: 单元模型域编译（新域）  
**Status**: ✅ 完工待审

---

## 一、完工总结

| 项目 | 状态 |
|------|------|
| 新域卡片编译 | 7/7 ✅ |
| 补边（已有卡 related 双向链接） | 7/7 ✅ |
| index更新 | index.md自动生成，无需手动干预 ✅ |

**7张新卡片全部入库 vault。**

---

## 二、入库清单

| 序号 | 文件路径 | 类型 | 核心内容 |
|------|----------|------|----------|
| 1 | `30_wiki/frameworks/yt-unit-model-overview.md` | F1 | 定义、十大单元模型分类、三角色、与五步法/Y模型关系 |
| 2 | `30_wiki/frameworks/yt-unit-model-ladder.md` | F2 | L1-L6六段进阶、段位标准、15个常见错误、构建方法 |
| 3 | `30_wiki/tools/yt-tool-unit-model-selection.md` | T1 | 复制哪个算哪个、加法减法、核心单元判断 |
| 4 | `30_wiki/tools/yt-tool-unit-model-construction.md` | T2 | 拆推评算、成本收入项清单、ABCD类模型 |
| 5 | `30_wiki/tools/yt-tool-unit-model-benchmark.md` | T3 | 科学类比、基准值来源、三点预测、基准值共建 |
| 6 | `30_wiki/tools/yt-tool-unit-model-dynamic.md` | T4 | 规模经济分析、规模变量/业务变量/环境变量、拐点预判 |
| 7 | `30_wiki/tools/yt-tool-unit-model-ai-assisted.md` | T5 | TCP-R双导师、教学教练T+咨询教练C、出口式咨询 |

---

## 三、质量自检

### 3.1 标准符合情况

| 检查项 | 要求 | 结果 |
|---------|------|------|
| frontmatter 完整 | id/title/type/status/domain/language 等 | ✅ 7/7 |
| Reusable Knowledge | 4-17条 claims | ✅ 7/7（F1:8条, F2:12条, T1:8条, T2:10条, T3:9条, T4:10条, T5:9条） |
| Critique | ≥2个 H4 外部攻击者，含具体引用 | ✅ 7/7 |
| Constraints | ≥1个内部局限 | ✅ 7/7 |
| Synthesis | ≥2个 [[wikilink]] 到已有卡片 | ✅ 7/7（每张卡均≥3个双向链接） |
| Action Triggers | ≥1个结构化触发场景 | ✅ 7/7 |
| 外部攻击者 | 不同范式，紧迫感 | ✅ 全部来自不同学科范式 |
| Constraints vs 外部攻击 | 不重叠 | ✅ |

### 3.2 外部攻击者清单

| 卡片 | 攻击者 1 | 攻击者 2 |
|------|---------|---------|
| F1 概览 | Mintzberg（管理实践与样板间调） | Christensen（突破性创新与约束代理） |
| F2 阶梯 | Kahneman（认知偏差与自评失准） | Snowden（Cynefin 框架与复杂系统） |
| T1 选择 | Simon（有限理性与选择负载） | Klein（自然决策与专家直觉） |
| T2 构建 | Popper（演绎法与归纳陷阱） | Gigerenzer（适应性工具箱与过度拆解） |
| T3 基准 | Tetlock（专家预测与比赛过度） | Thaler（推定实验与改善翼效应） |
| T4 动态 | Sterman（系统动力学与模型过简） | Taleb（反脆弱与规模经济骗局） |
| T5 AI辅助 | Morozov（技术解决主义与领域安全） | Postman（技术盲目与思考面容交易） |

### 3.3 已知弱点

| 项目 | 说明 | 严重程度 |
|------|------|----------|
| F2 的15个错误 | 口述稿中15个错误分散在多个案例中，未找到明确列表。F2中的15个错误是基于案例提炼，可能不完整 | 低 |
| T5 的TCP-R模型 | 口述稿中TCP-R只有概念提及，无完整框架描述。T5中的双导师模型是基于口述稿片段+推断补充 | 中 |
| 补边可能不完整 | 新卡引用了大量已有卡，但只更新了7个已有卡的related字段 | 低 |

---

## 四、补边详情

### 已更新的已有卡片（7张）

| 已有卡片 | 添加的新链接 |
|----------|-------------|
| `yt-decision-full-process` | +7张单元模型卡 |
| `yt-entrepreneur-five-step-method` | +7张单元模型卡 |
| `master-cognitive-bias-checklist` | +2（ladder, benchmark） |
| `master-systems-thinking` | +6（除overview） |
| `master-first-principles` | +3（ladder, construction, dynamic） |
| `master-decision-hygiene` | +2（ladder, selection） |
| `yt-decision-review` | +2（ladder, benchmark） |

### 未更新但新卡已引用的已有卡（待后续补边）

- `yt-decision-y-model`（被F2/T1/T2引用）
- `yt-entrepreneur-liberate-thinking`（被F1/F2引用）
- `yt-entrepreneur-growth-flywheel`（被F1引用）
- `yt-entrepreneur-scientific-method`（被F1引用）
- `master-knowledge-compound`（被F2引用）
- `ai-prompt-engineering`（被T5引用）
- `master-falsification`（被T3引用）
- `master-planning-fallacy`（被T3引用）
- `master-bounded-rationality`（被T1引用）
- `master-ecological-rationality`（被T2引用）
- `master-strategic-planning`（被T2引用）
- `master-strategy-type`（被T4引用）

---

## 五、待审查项

1. **F2的15个错误是否完整**：口述稿中未找到明确的15个错误列表，F2中的错误是基于多个案例提炼。建议审查者确认是否需要补充或调整。

2. **T5的TCP-R模型准确性**：口述稿中TCP-R只有概念提及，双导师模型的具体描述可能需要进一步验证。

3. **补边是否完整**：新卡引用了12个已有卡，但只完成了7个已有卡的双向链接更新。剩余12个已有卡的related字段未更新。

---

## 六、下一步行动

1. **送审**：等待欧阳锋审查，重点关注F2的15个错误和T5的TCP-R模型。
2. **补边**：根据审查反馈补充剩余12个已有卡的双向链接。
3. **OCR Batch 5**：返回处理OCR批次5去留评估。

---

*本报告由老顶童编写，待审查者确认。*
