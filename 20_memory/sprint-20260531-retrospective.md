---
title: "Sprint 2026-05-31 复盘 — 标注管线 + 萃取器升级"
type: improvement-plan
status: stable
domain:
  - master
created_at: 2026-05-31
updated_at: 2026-05-31
author: 黄药师（Builder）
tags:
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
---

# Sprint 2026-05-31 复盘

## 一、完成的交付

| # | 交付 | 代码量 | 测试 | 状态 |
|:--:|------|:--:|:--:|:--:|
| 1 | `auto_label_chunk()` 三段式标注管线 | `kdo/commands/label.py` (~400行) | 25 tests | ✅ |
| 2 | `tag-registry.yaml` v1.1 | 15维×113值，含includes/excludes | — | ✅ |
| 3 | Data Curator Phase 2 Clean | `clean_cards.py` (修复+重跑) | — | ✅ |
| 4 | parse_frontmatter bug 修复 | 手写→yaml.safe_load，10卡回滚 | — | ✅ |
| 5 | Label prompt 优化 | 26.7% → 88.3% (7轮迭代) | — | ✅ |
| 6 | 萃取器 LLM 升级 | `extract_dark_knowledge.py` +~60行 | — | ✅ |
| **总计** | | **~500行新增** | **388 tests, 0 regression** | |

## 二、Prompt 工程迭代轨迹（核心技术突破）

### 准确率提升曲线

| 版本 | 关键策略 | chunk_type | method_family | audience | perspective | **总** |
|:--:|------|:--:|:--:|:--:|:--:|:--:|
| v1 | 英, 45候选 APPLY/REJECT | 7% | 7% | 40% | 53% | 26.7% |
| v5 | 中, 单选, 5 few-shot | 73% | 47% | 80% | 73% | 68.3% |
| v8 | +裁决规则+eval示例 | 80% | 67% | 73% | 87% | 76.7% |
| v9 | +developer示例 | 87% | 73% | 93% | 87% | 85.0% |
| **v10** | **+card上下文提示** | **93%** | **93%** | **87%** | **80%** | **88.3%** |

### 每个策略的贡献值

| 策略 | 提升幅度 | 关键洞察 |
|------|:--:|------|
| 中文 few-shot | **+41%** | 单次最大跳跃。英文prompt对中文文本几乎无用 |
| 单选>多选 | **+41%** | "四维各选一"远优于"45候选逐判" |
| 对比区分描述 | +8% | "definition ≠ claim：definition 没有可证伪的主张" |
| card上下文提示 | **+12%** | 告诉LLM"这段话来自决策卫生卡（认知思维工具）" → method_family直接命中 |

### 失败的模式

| 尝试 | 结果 | 教训 |
|------|:--:|------|
| 45候选多标签分类 | 26.7% | LLM不擅长大量候选的逐一判断 |
| 英文描述+中文文本 | 0 candidates | 跨语言bigram匹配完全失效 |
| 7+个few-shot示例 | 80% | 示例过多→注意力分散→尾部示例被忽略 |
| self-consistency(3票) | 退步 | 低温(0.01)下3次投票结果相同，无增益 |
| 无card上下文的细粒度分类 | 73.3% | thinking-tool/decision-framework的边界需要card级信息 |

## 三、踩过的坑

### 坑1：手写YAML解析器导致嵌套数据丢失（P-16，F-KDO-022变体）

- **根因**：`clean_cards.py` 的 97 行手写YAML解析器只能处理一层嵌套
- **影响**：visual_analysis 4图→5字符串，related 4链接→level:intermediate。10张卡受损
- **修复**：替换为 `yaml.safe_load()`（~15行），97→15行，正确性大幅提升
- **教训**：**永远不要手写YAML/JSON解析器**。即使"只是简单的前言"，嵌套结构迟早会出现

### 坑2：花引号被YAML误解析（P-17）

- **根因**：`"四套操作系统"` 中的直引号 `"` 被yaml.safe_load解释为YAML字符串定界符，后面的 `=可切换...` 成为非法tail
- **修复**：值含 `"value"=tail` 模式时，用YAML单引号包裹整个值
- **教训**：Chinese content中的引号容易触发YAML流式解析。用单引号包裹含引号的值

### 坑3：pre-screen对中文文本返回0候选

- **根因**：tag-registry的includes是英文，bigram匹配对中文无效
- **修复**：绕过pre-screen，直接送全维度候选给LLM（单选模式不需要pre-screen做过滤）
- **教训**：pre-screen设计时未考虑中英双语场景。未来需要中文includes描述+LLM预筛

## 四、可复用的Skills & 方法论

### Skill 1：LLM Prompt迭代方法论

```
1. 建 Gold Standard（15-30条手工标注）
2. 测基线（最简prompt）→ 记录每维度准确率
3. 改prompt → 跑全量比对 → 看delta
4. 每次只改一个变量（加few-shot/改描述/加上下文）
5. 保存每轮结果，避免回退
6. 达到85%+ 且连续2轮不再提升时停止
```

**关键**：Gold Standard是唯一真相源。没有它，prompt优化就是盲调。欧阳锋的15条Gold Standard是本轮成功的基石。

### Skill 2：Card上下文注入技术

标注chunk时，告诉LLM"这段话来自XX卡片（类型/用途描述）"——这提供了chunk文本本身不具备的card级信息（卡片是thinking-tool还是decision-framework），直接消除method_family的二义性。

**模板**：
```
此 chunk 来自卡片：{card_name}（{card_type_description}，讨论{key_topics}）
```

### Skill 3：安全批量修改协议（C-10强化版）

```
1. 先读代码，理解当前行为
2. dry-run 单卡 → 验证改动正确
3. write 单卡 → 备份原文件 → 验证备份可恢复
4. 5卡批量 → 每批后抽检
5. 全量后跑 kdo lint + pytest 确认无回归
6. git restore 保留为最终回滚手段
```

**本次验证**：发现parse_frontmatter bug后，从git历史恢复10张受损卡的原始版本，证明git是最可靠的保险。

### Skill 4：萃取器LLM升级模式

纯regex提取→regex预筛+LLM精提取的双轨模式：
- regex路径保留为 `--no-llm` 回退
- LLM路径填充6字段（title/use_case/operation/boundary/why_valuable/cross_reference）
- `is_valid=false` 的候选被LLM过滤（减少噪声）
- score从0.5-0.6压缩区间→0.2-0.9分布

**代码模板**见 `extract_dark_knowledge.py` 的 `llm_extract_candidate()` 函数。

## 五、后续建议

1. **全量跑萃取器**：3篇口述稿跑LLM精提取（每篇约5-10分钟），产出~40-60条高质量候选
2. **Pilot 20张卡标注**：用最终prompt（含card上下文）对前20张卡跑auto_label_chunk → 与Gold Standard比对
3. **tag-registry中文增强**：给chunk_type/method_family的includes加中文关键词，使pre-screen对中文有效
4. **萃取器prompt迭代**：复用labeler的prompt工程经验（中文few-shot + card上下文）对萃取器做同样的优化

---

*黄药师 · 2026-05-31*
