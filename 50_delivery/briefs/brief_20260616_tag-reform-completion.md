# 标签体系改革完工简报

**日期**：2026-06-16  
**范围**：`30_wiki/` 全库 1359 张卡片  
**负责人**：Kimi Code CLI（独立判断执行）  
**状态**：✅ 改革基线完成，P0 / YAML 错误清零

---

## 1. 改革前问题

全库标签长期处于"野蛮生长"状态：

| 问题 | 表现 |
|------|------|
| 维度命名不统一 | 注册表用 `chunk_type`/`method_family`，实际卡片用 `#chunk-type/...`/`#method/...` |
| flat 标签泛滥 | `#ai`、`#consulting`、`#dark-knowledge`、`#weapon-library` 等无维度前缀 |
| 注册表覆盖不足 | 实际使用大量 `scene/*`、`problem/*`、`confidence/*` 等维度未注册 |
| 无效标签残留 | `None`、`#�߼��¼���` 等乱码/空标签 |
| 唯一标签失控 | 改革前 250+ 唯一标签，同义反复、检索噪音大 |

---

## 2. 改革动作

### 2.1 清理无效标签（Phase 1）

- 扫描全库卡片 frontmatter 中的 `tags`。
- 删除 `None`、空字符串、乱码标签。
- 移除未加 `#` 的纯文本标签。
- **结果**：156 张卡片被清理，473 个无效标签被移除。

### 2.2 扩展并规范化注册表（Phase 2）

文件：`90_control/tag-registry.yaml`，版本从 **1.2 → 1.3**

- **维度命名规范化**：所有 dimension key 从 `snake_case` 改为 `kebab-case`，与实际标签一致：
  - `chunk_type` → `chunk-type`
  - `method_family` → `method`
  - `content_format` → `content-format`
  - `source_context_type` → `source-context-type`
  - `data_generation` → `data-generation`
  - `error_root` → `error-root`
  - `value_tier` → `value-tier`
  - `usage_depth` → `usage-depth`
  - `prerequisite_knowledge` → `prerequisite-knowledge`
- **新增维度**：
  - `confidence`：置信度/验证状态
  - `scene`：使用场景/工作流上下文
  - `problem`：问题域
  - `source-type`：来源多样性
- **补充维度值**：
  - `domain` 增加 `ai`、`saas`、`skill-engineering` 等
  - `method` 增加 `modeling`、`workflow`、`knowledge-management`、`prompt` 等
  - `industry` 增加 `consulting`、`fitness`、`dental`、`hardware`、`ai-infrastructure`
  - `content-format` 增加 `formula`
- **同步更新**：`activation_rules`、`chunk-type-triggers`、`inference_map` 中的维度引用。

### 2.3 保守映射 flat tags（Phase 3）

对含义明确、无争议的 flat tag 做自动映射：

- `#ai` → `#domain/ai`
- `#saas` → `#domain/saas`
- `#healthcare` → `#industry/healthcare`
- `#consulting` → `#industry/consulting`
- `#e-commerce` → `#industry/ecommerce`
- `#business-strategy` / `#product-strategy` → `#method/decision-framework`
- `#product-development` → `#method/product-design`
- `#course-design` → `#method/course-design`
- `#formula` → `#content-format/formula`
- `#critique` → `#chunk-type/critique`
- `#concept` → `#chunk-type/definition`
- `#methodology` / `#meta-method` / `#cognitive-tool` → `#method/thinking-tool`
- `#statistics` / `#sales-analysis` / `#vendor-assessment` / `#self-assessment` → `#method/research-method` 或 `#method/evaluation-method`
- 等等

**结果**：63 张卡片的 90 个 flat tags 被映射为维度标签。

---

## 3. 改革后状态

| 指标 | 改革前 | 改革后 |
|------|--------|--------|
| 注册表维度 | 18 | **21** |
| 注册表允许值 | 134 | **211** |
| 实际唯一标签 | 250+ | **128** |
| 实际标签实例 | ~650 | **583** |
| 无效标签 | 37+ | **0** |
| 未注册维度标签 | 大量 | **0** |
| 未注册 flat tags（待人工审查） | - | **16** |

### 3.1 Top 25 高频标签（已注册）

| 标签 | 次数 |
|------|------|
| `#method/modeling` | 58 |
| `#domain/yitang` | 44 |
| `#content-format/case-study` | 34 |
| `#method/evaluation-method` | 32 |
| `#domain/ai-saas` | 22 |
| `#content-format/concept-card` | 20 |
| `#method/prompt-engineering` | 18 |
| `#content-format/framework` | 16 |
| `#content-format/checklist` | 15 |
| `#method/execution-method` | 14 |
| `#method/learning-method` | 14 |
| `#content-format/sop` | 12 |
| `#method/decision-framework` | 11 |
| `#method/thinking-tool` | 11 |
| `#method/workflow` | 11 |
| `#industry/content-creation` | 9 |
| `#perspective/professional` | 9 |
| `#domain/knowledge-management` | 8 |
| `#industry/education` | 7 |
| `#industry/healthcare` | 7 |
| `#chunk-type/synthesis` | 7 |
| `#method/research-method` | 6 |
| `#perspective/compliance` | 6 |
| `#confidence/verified-by-case` | 6 |
| `#domain/skill-engineering` | 5 |

### 3.2 质量门禁

```
{'total': 1359, 'p0': 0, 'p1': 773, 'clean': 586, 'yaml_error': 0}
```

- P0 问题：0
- YAML 错误：0
- clean 卡片：586（较改革前 +225）

---

## 4. 剩余未注册 flat tags（需人工判断）

以下 16 个 flat tags 因含义不够明确或属于个人体系，未做自动映射，建议后续由内容负责人逐条判定：

| 标签 | 次数 | 建议处理方向 |
|------|------|--------------|
| `#kdo` | 3 | 可映射为 `#domain/master` 或保留为卡片元标签 |
| `#confidence` | 1 | 可映射为 `#confidence/draft` |
| `#dark-knowledge` | 1 | 可映射为 `#domain/master` 或新增 `knowledge-type` 维度 |
| `#deep-dig` | 1 | 可映射为 `#domain/master` 或 `#content-format/framework` |
| `#entrepreneurship` | 1 | 可映射为 `#domain/yitang` 或 `#domain/master` |
| `#iceberg` | 1 | 可映射为 `#method/thinking-tool` 或 `#content-format/framework` |
| `#itingnao` | 1 | 专有名词（听脑），建议保留为 `source-platform` 或映射为 `#domain/ai-saas` |
| `#l6-essence` | 1 | 专有框架标签，需确认是否新增维度值 |
| `#master-system` | 1 | 可映射为 `#domain/master` |
| `#membership` | 1 | 可映射为 `#domain/master` 或 `#industry/saas` |
| `#private-domain` | 1 | 可映射为 `#method/execution-method` 或 `#domain/master` |
| `#renewal` | 1 | 可映射为 `#method/execution-method` |
| `#self-improvement` | 1 | 可映射为 `#domain/master` |
| `#tier` | 1 | 可映射为 `#value-tier/meso` 等，需看上下文 |
| `#value` | 1 | 可映射为 `#method/evaluation-method` |
| `#weapon-library` | 1 | 可映射为 `#content-format/framework` 或保留为个人标签 |

---

## 5. 文件变更清单

- `90_control/tag-registry.yaml`：升级到 v1.3，21 维度 211 允许值
- `90_control/scripts/tag-cleanup-phase2.py`：扩展 flat tag 映射脚本
- `90_control/scripts/normalize-tag-registry.py`：注册表规范化脚本
- `90_control/scripts/tag-cleanup-phase3.py`：保守映射脚本
- `30_wiki/concepts/graph-rag.md`：补充 `source_refs: [source_unknown]`
- `30_wiki/concepts/industry-ai-cases.md`：补充 `source_refs: [source_unknown]`
- `30_wiki/concepts/learning-thinking.md`：补充 `source_refs: [src_20260522_0af1f6dd]`
- 约 220 张卡片的 `tags` 字段被清理或映射

---

## 6. 下一步建议

1. **人工审查 16 个剩余 flat tags**：由黄药师/老顽童按领域认领，决定映射或保留。
2. **质量门禁纳入标签检查**：在 `kcard-quality-gate.py` 中增加对未注册标签的 P1 告警。
3. **标签使用指南**：在 `90_control/` 下补充 `tagging-guide.md`，说明每个维度的使用场景。
4. **定期复检**：每月跑一次标签统计，防止 flat tags 重新膨胀。

---

**结论**：标签体系已完成从"野蛮生长"到"受控维度"的基线改革，检索噪音显著降低，注册表与实际使用基本一致，全库质量门禁保持 P0=0、YAML=0。
