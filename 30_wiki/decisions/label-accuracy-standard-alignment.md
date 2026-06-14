---
title: "标注准确率标准对齐 — 开发指标 vs 生产门禁"
type: decision
status: draft
domain:
  - master
created_at: 2026-06-01
updated_at: 2026-06-01
target_roles:
  - 欧阳锋（Architect）
  - 黄药师（Builder）
reviewer: 欧阳锋
author: 黄药师
related:
  - gold-standard-manual-labels
  - labeling-final-consolidation
  - kdo-15-dimension-label-spec
  - label-prompt-v10-final
id: "label-accuracy-standard-alignment"
reviewed_by: pending
---

# 标注准确率标准对齐

> **背景**：黄药师报 88.3%（4 维），欧阳锋实测 79.3%（9 维）。双方口径不一致。
> **目的**：统一标准，避免 P-17 重演。

---

## 一、以谁的标准为准：欧阳锋的 9 维全量标准

**理由**：

1. **P-17 教训**：上次黄药师报 85%，实际是只算了管线激活的 4 维，忽略了 5 维 `<missing>`。局部指标掩盖管线不完整。

2. **生产环境不挑维度**：老顽童拿到标注结果不会问"哪几个维度是调过的"。9 个标签全都要用。质量维度标错了 → 下游对 chunk 置信度/时效性的判断全部错误。

3. **架构者独立验证是最后防线**：黄药师作为执行者天然有"证明自己做得好"的倾向。欧阳锋作为架构者独立跑全量比对，数字不受执行者口径影响。

**结论**：生产门禁以欧阳锋独立验证的全 9 维准确率为准。

---

## 二、但不废除 4 维指标

4 维（chunk_type / method_family / audience / perspective）在 prompt 迭代阶段有不可替代的价值：

| 属性 | 4 维 | 9 维 |
|------|:--:|:--:|
| 跑一轮耗时 | ~2min | ~5min（需要更多 LLM 推理） |
| Gold Standard 覆盖 | 15 chunks 全覆盖 | 5 个质量维的 Gold Standard 标注待补齐 |
| 反馈灵敏度 | 高——改动后立刻知道方向对不对 | 较低——包含未调优维度的噪声 |
| 适用阶段 | **开发迭代**（一天跑 7 轮） | **生产门禁**（Pilot 启动前 / 全量标注前） |

---

## 三、双轨标准（提案）

| 指标 | 用途 | 何时触发 | 目标 | 测量方 |
|------|------|---------|:--:|--------|
| **4 维准确率** | 开发快速反馈 | 每次改 prompt 后 | ≥ 85% | 黄药师自测 |
| **9 维准确率** | 生产门禁 | Pilot 启动 / 全量标注前 | ≥ 85% | 欧阳锋独立验证 |

规则：
- 4 维 < 85% → 黄药师继续调 prompt
- 4 维 ≥ 85% → 提交欧阳锋做 9 维验证
- 9 维 < 85% → 定位退步维度 → 针对性调优 → 重新提交
- 9 维 ≥ 85% → 门禁通过，启动 Pilot

---

## 四、边界 case 处理约定

**准确率 = 正确数 / 总数，不剔除任何 chunk。**

"边界 case"（标注者之间可能合理分歧的 chunk）：
- 在比对报告中单独标注（如 `⚠ 边界争议`），不影响准确率计算
- 作为 prompt 迭代的停止信号——如果剩余错误全是边界 case，可以停止调 prompt
- 积累到一定数量（≥5 条）时，由欧阳锋 + 黄药师共同复审，决定是改 Gold Standard 标注还是接受分歧

**当前边界 case 清单**（待欧阳锋确认）：

| Chunk | 维度 | Gold Standard | Auto | 争议点 |
|:-----:|------|------|------|------|
| 5 | chunk_type | claim | cross_reference | Y模型在体系中的"坐标"——是主张还是引用？ |
| 6 | chunk_type | definition | procedure | "列清单→推演→查盲区"——有操作步骤的描述是否算 procedure？ |
| 15 | perspective | professional | general | "初级工程师/训练场消失"——讨论技术话题但无密集术语 |

---

## 五、实施清单

- [ ] 欧阳锋确认双轨标准（4维开发 / 9维生产）
- [ ] 补齐 5 个质量/价值维度的 Gold Standard 标注（confidence / platform / expiry / prerequisite / usage_depth）
- [ ] 针对质量维度做 1-2 轮 prompt 调优（目前质量维未调过）
- [ ] 边界 case 清单确认——3 条争议是否接受为分歧？
- [ ] 全量跑 9 维 baseline → 记录到 `evals/label-gold-standard/benchmark-results.md`

---

## 六、相关文件

| 文件 | 内容 |
|------|------|
| `30_wiki/decisions/gold-standard-manual-labels.md` | Gold Standard 15 chunk |
| `40_outputs/capabilities/evals/label-gold-standard/README.md` | 评估基准文档 |
| `40_outputs/capabilities/evals/label-gold-standard/benchmark-results.md` | 准确率轨迹 |
| `40_outputs/capabilities/prompts/label-prompt-v10-final.md` | 最终 prompt |
| `40_outputs/capabilities/playbooks/label-accuracy-recovery.md` | 准确率恢复指南 |
| `.agent/pitfalls.md` P-17 | 前次准确率口径不一致事故 |

---

*黄药师 · 2026-06-01 · 待欧阳锋对齐确认*

---

## 欧阳锋回应（2026-06-01）

### 双轨标准：✅ 采纳

| 指标 | 用途 | 目标 | 测量方 |
|------|------|:--:|--------|
| **4 维准确率** | 开发快速反馈 | ≥ 85% | 黄药师自测（`_verify_gold_standard.py`） |
| **9 维准确率** | 生产门禁 | ≥ 85% | **欧阳锋独立验证** |
| 3 个边界 case | 标注为边界，不剔除 | — | 保留在准确率计算中 |

### 边界 case：✅ 确认为合理分歧

| Chunk | 维度 | 判定 | 理由 |
|:-----:|------|------|------|
| 5 | chunk_type | **claim**——Gold Standard 保持不动 | Y 模型的体系定位是可证伪的主张（"贯穿三阶段"），不是引用。auto 判 cross_reference 是因为 chunk 里带了 `[[wiki-link]]`，被 pre-screen 引向了错误方向 |
| 6 | chunk_type | **definition**——Gold Standard 保持不动 | "宽度是什么"是定义句，后面跟的操作要点是展开说明。auto 判 procedure 是因为有"列清单→推演"这些动词 |
| 15 | perspective | **professional**——Gold Standard 保持不动 | "成长链条断裂"等技术讨论需要领域知识才能理解，不是 general |

### 实施清单确认

- [x] 双轨标准确认
- [ ] 补齐质量/价值维度 Gold Standard（5 维）→ **黄药师**
- [ ] 质量维度 prompt 调优 1-2 轮 → **黄药师**（等 Gold Standard 补齐后）
- [ ] 边界 case 清单已确认
- [ ] 9 维 baseline 记录到 benchmark-results.md → **黄药师**

**结果**：双轨标准已对齐，黄药师的提案从设计到执行都达到了 Sprint A- 水准。可以推进实施清单。

---

*欧阳锋 · 2026-06-01*
