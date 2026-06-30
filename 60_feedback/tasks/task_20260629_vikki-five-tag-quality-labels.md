---
id: task_20260629_vikki-five-tag-quality-labels
type: task
status: reviewed
assignee: 老顽童(Kimi)
priority: P2
created_at: 2026-06-29
updated_at: 2026-06-30
reviewed_by: 欧阳锋
review_date: 2026-06-30
reviewer: 欧阳锋
source_refs:
- 00_inbox/AI-study/0071Vikki战队-2群 · 认知精华提炼.md
- 00_inbox/AI-study/0017大馨战队 · 短视频内容拆解方法论精华提炼.md
related:
- 30_wiki/frameworks/framework-kdo-quality-gate
- 30_wiki/systems/system-kdo-frontmatter-schema
- framework-brand-three-degree
---

# Vikki 五标签 + 大馨品牌三度 → KDO 卡片质量标签体系

## 目标

把 Vikki 战队的群聊运营标签系统与大馨战队的品牌三度体系融合，建立一套**既描述卡片内容类型、又评估卡片质量层级**的 KDO 卡片质量标签体系，提升 30_wiki 卡片的可检索性、可审核性和跨角色协作效率。

## 输入模型

### Vikki 五标签（内容类型维度）

| 标签 | 含义 | KDO 映射 |
|:---:|:---|:---|
| 💡 洞察 | 有价值的发现 | `insight` |
| 🎯 假设 | 待验证的判断 | `hypothesis` |
| ✅ 实践 | 可落地的方法 | `actionable` |
| 🔥 金句 | 值得记录的话 | `quotable` |
| ❤️ 为什么 | 底层逻辑 | `principle` |

### 大馨品牌三度（质量层级维度）

| 维度 | 品牌含义 | KDO 卡片映射 |
|:---:|:---|:---|
| 知名度 | 让人知道你是谁 | `cited` — 被引用次数 / 入度 |
| 美誉度 | 让人喜欢你、信任你 | `quality` — lint/审查质量评分 |
| 信任度 | 让人愿意为你付费 | `validated` — 实战验证 / source_refs 可信度 |

## 融合后的 KDO 质量标签体系

```yaml
quality_labels:
  # 内容类型（Vikki）
  - insight        # 有新洞察
  - hypothesis     # 待验证判断
  - actionable     # 可执行步骤
  - quotable       # 高传播性表述
  - principle      # 解释因果机制
  # 质量层级（大馨）
  - cited          # 被多次引用
  - quality        # 审查质量高
  - validated      # 有实战验证
```

## 执行方案

### 方案 A：扩展 `tags:` 字段（推荐）

在现有 `tags:` 中允许标准化质量标签，与自由标签共存：

```yaml
tags:
  - insight
  - actionable
  - validated
  - 渠道增长
```

### 方案 B：新增 `quality_labels:` 字段

机器可读的结构化字段：

```yaml
quality_labels:
  - insight
  - actionable
  - validated
```

### 方案 C：双轨制

- `quality_labels` 用于机器识别和过滤
- `tags` 保留自由标签供人阅读

## 执行要求

1. 黄药师评估三种方案对 `kdo lint` / `kdo query` / `kdo pre-submit` 的影响。
2. 若新增字段，同步更新 kdo 源码中的 frontmatter schema。
3. 编写迁移脚本，对现有 30_wiki 卡片按内容自动/半自动打标签（首批 50 张）。
4. 更新 `.agent/laowantong-context.md`，让老顽童生产卡片时主动选择 quality_labels。
5. 在 `30_wiki/index.md` 或 `30_wiki/systems/` 中建立「KDO 卡片质量标签使用指南」。
6. 同步生产一张 `framework-brand-three-degree` 概念卡，作为品牌三度体系在 KDO 中的沉淀。

## 验收标准

- 新增标签体系通过 `kdo pre-submit` 不报错
- 至少 50 张现有卡片完成标签迁移
- `kdo query --label actionable` 或等效命令可过滤出可执行卡片
- 欧阳锋抽查：标签与卡片内容真实匹配，无机器误标

---

## 执行报告（2026-06-30）

**执行者**：老顽童(Kimi)
**状态**：pending_review，待欧阳锋终审

### 完成内容

1. **黄药师基建层（已完成）**
   - `90_control/scripts/label-quality-migrate.py`：自动/半自动 quality_labels 迁移脚本
   - KDO 源码：未在本次任务中新增 `kdo query --label` 命令；当前使用 `rg "^  - actionable$" 30_wiki -g "*.md" -l` 等效过滤

2. **老顽童内容层**
   - **概念卡**：`30_wiki/concepts/framework-brand-three-degree.md`
     - 品牌三度（知名度/美誉度/信任度）在 KDO 中的沉淀
     - 含 Claims / Evidence / Critique / Synthesis / Action Triggers / Open Questions
   - **使用指南**：`30_wiki/systems/system-kdo-quality-labels.md`
     - 8 个受控标签定义（Vikki 五标签 + 大馨三度）
     - 自动判定规则、人工判定场景、frontmatter 写法、使用场景、标签组合示例、常见误用
   - **50 张试点卡片标签迁移**
     - 运行 `python 90_control/scripts/label-quality-migrate.py --apply`
     - 标签分布：validated 50 / cited 30 / actionable 22 / principle 16 / insight 1
     - 修复 40 张卡片缺失 `created_at` / `updated_at` 的问题

3. **生产规范更新**
   - `.agent/laowantong-context.md`：单卡收尾检查清单新增 quality_labels 检查项

### 质量验证

```text
# 新产出卡片
$ kdo pre-submit -f 30_wiki/concepts/framework-brand-three-degree.md 30_wiki/systems/system-kdo-quality-labels.md
All gates passed. Ready for human review. (2/2 PASS)

# 迁移卡片抽查（50 张分 2 批）
$ kdo pre-submit -f <第一批 25 张>
All gates passed. Ready for human review. (25/25 PASS)

$ kdo pre-submit -f <第二批 25 张>
All gates passed. Ready for human review. (23/23 PASS, 2 张重复)
```

### 欧阳锋终审结果（2026-06-30）

**状态：reviewed ✅**

- 新卡 2/2 pre-submit PASS ✅
- 抽查迁移卡 4/4 pre-submit PASS ✅
- 更新后的队列/context/任务单 5 个文件 pre-submit PASS ✅
- 全库含 `quality_labels` 的卡片：227 张

**审查中修复的坑：48 张卡片存在重复 `quality_labels`**

欧阳锋抽查时发现部分卡片 frontmatter 里有两个完全相同的 `quality_labels:` 块，原因是迁移脚本在 apply 阶段缺少“已存在则跳过”的防御性检查。

- 已用脚本清理 48 张卡片的重复字段
- 已给 `label-quality-migrate.py` 增加防御逻辑：
  ```python
  if "quality_labels:" in frontmatter:
      skip
  ```
- 清理后重新跑 pre-submit，相关卡片全部通过

**遗留问题（已拆分为 #36）**

- `kdo query --label` 未实现，当前用 `rg` 临时替代 → 交给黄药师在 [[task_20260630_kdo-query-label-filter]] 中实现

### 欧阳锋审查要点

- `framework-brand-three-degree` 概念卡的内容是否准确反映大馨战队品牌三度框架
- `system-kdo-quality-labels` 指南是否清晰可执行
- 50 张试点卡片的 `quality_labels` 是否与内容真实匹配
- 迁移脚本 `label-quality-migrate.py` 的判定规则是否合理
- 是否需要补充 `kdo query --label` 命令实现
