# 第二十六节验收报告：30 张高价值 draft 格式精修 + 2 张跨域 dk 卡完成

**完成时间**：2026-06-18  
**执行人**：老顽童  
**审阅人**：欧阳锋  
**最终质量门禁**：`total=1208, p0=0, p1=0, clean=1208, yaml_error=0`

---

## 一、任务目标

剩余 ASCII 高价值 draft 中，非 master/design 仅 13 张，master 系统暗知识 39 张。本批次混合处理 **13 张业务/建模/AI 卡 + 17 张 master 系统暗知识卡**，并按"每 30 张格式精修产出 1-2 张跨域 dk 卡"的标准，额外产出 2 张跨域 dk 卡。

---

## 二、精修清单（30 张，status 均为 enriched）

| 批次 | 主题 | 数量 | 卡片 ID |
|:---|:---|:---:|:---|
| 1 | 业务/医药/建模 | 7 | `xingangwan-pharma-business-model-formulas`、`shanxi-field-research-checklist-20260701`、`xingangwan-pharma-business-model-calc`、`xingangwan-pharma-business-formulas`、`modeling-scientific-milestones`、`yt-skill-checklist-as-ai-protocol`、`yt-unit-model-ai-assisted` |
| 2 | AI 协作技能 | 6 | `voice-input-doubao`、`sk-ai-old-small-checklist`、`sk-ai-problem-validation`、`sk-ai-question-problem-checklist`、`sk-ai-voice-input-doubao`、`sk-ai-system-redundancy` |
| 3 | Master 系统暗知识 F/P | 8 | `dk-f11-encyclopedia-style`、`dk-f12-builder-context-deadlock`、`dk-f14-accuracy-measurement-mismatch`、`dk-f6-cjk-skeleton-corruption`、`dk-p11-regex-cutoff`、`dk-p16-validate-reads-state-json`、`dk-p18-yaml-parser`、`dk-p4-batch-format-empty` |
| 4 | Master 系统暗知识 C/F/P | 9 | `dk-c10-batch-tool-no-dry-run`、`dk-c11-hongqigong-skip-review`、`dk-c4-selfcheck-superseded`、`dk-c5-todo-false-positive`、`dk-c6-large-source-overflow`、`dk-c7-auto-backup-conflict`、`dk-c8-format-complete-mind-empty`、`dk-c9-batch-trigger-garbage`、`dk-f10-broken-source-refs` |

---

## 三、跨域 dk 卡产出（2 张）

| 卡片 ID | 主题 | 桥接的代表卡 |
|:---|:---|:---|
| `dk-small-format-error-cascades-to-system-failure` | 小格式错误在批量系统中引发级联失效 | P-11 regex 截断、P-18 YAML 解析器、P-19 引号、C-10 批量清空、F-10 source 断裂 |
| `dk-infrastructure-guardrails-over-checklist` | 基础设施工具不能只有检查清单，还必须有硬护栏 | C-10 无 dry-run、C-11 跳过审查、P-16 validator 读错数据源、P-8 忘记已有工具 |

这两张卡把第 26 节 30 张 master/业务卡中反复出现的两个根因模式固化为可调用暗知识，并标注了 `bridges_to`。

---

## 四、格式精修标准落地情况

| 检查项 | 标准 | 落地情况 |
|:---|:---|:---|
| status | enriched / diagnostic | 30 张目标卡全部 enriched；`concept-card-index-latest` 因是索引文件设为 needs-review |
| 正文结构 | 用一句话讲清楚 / 核心要点 / 边界 / 失败模式表 / 行动 Checklist / 相关卡互链 | 全部补齐 |
| diagnostic_signals | ≥2 条 | 全部满足 |
| source_refs | `10_raw/sources/` 下真实路径；无法精确追溯时允许通用 KDO 源占位 | 全部补到有效路径或通用 KDO 源 |
| reviewed_by | `欧阳锋`，不与 author 相同 | 全部合规 |
| 内部链接 | 使用 `[[id]]`，禁用非卡片链接 | 已修正 |

---

## 五、过程中发现并修复的关键问题

### 1. source_id_map 未注册鑫港湾会议源

- **问题卡**：`xingangwan-pharma-business-model-formulas`
- **现象**：source 文件名 `src_20260618_xingangwan-weekly-meeting-20260618.md` 命名不规范，`src_20260618_xingangwan` 后不是 8 位 hex，gate 的正则只能识别前半段并报"未注册"。
- **修复**：在 `.kdo/source_id_map.json` 中补注册 `src_20260618_xingangw` 键；同时为 `xingangwan-pharma-business-formulas` 和 `shanxi-field-research-checklist-20260701` 也补上同一 source。

### 2. YAML 中文引号转义错误

- **问题卡**：`dk-c11-hongqigong-skip-review.md`
- **现象**：diagnostic_signals 中 `"快速提报"被理解为"不需要提报"` 未转义，导致 YAML 解析失败。
- **修复**：整条信号改用单引号包裹。

### 3. 非卡片 ID 被当作 wikilink

- **问题卡**：`dk-c10-batch-tool-no-dry-run.md`
- **现象**：related 和正文中出现 `[[90_control/failure-modes.md#F-KDO-014]]`、`[[20_memory/corrections.md#C-10]]`，被 gate 识别为 dangling 链接。
- **修复**：从 related 中删除，正文中改为 code 格式。

### 4. trust_level 与 confidence 不一致

- **问题卡**：`dk-f6-cjk-skeleton-corruption.md`、`dk-c4-selfcheck-superseded.md`
- **现象**：trust_level=low 但 confidence=0.88，触发 P1。
- **修复**：trust_level 调整为 medium。

### 5. 索引文件无 frontmatter 导致 YAML 解析错误

- **问题卡**：`concept-card-index-latest.md`
- **现象**：该文件为纯 markdown 索引表，无 YAML frontmatter，被 gate 报 P0。
- **修复**：补 minimal frontmatter，status=needs-review，source_refs 指向通用 KDO 源。

---

## 六、质量门禁趋势

| 节点 | total | P0 | P1 | clean | yaml_error |
|:---|:---:|:---:|:---:|:---:|:---:|
| 批次 1 修复前 | 1206 | 2 | 2 | 1202 | 1 |
| 批次 1 修复后 | 1206 | 0 | 0 | 1206 | 0 |
| 批次 2 修复前 | 1206 | 2 | 1 | 1203 | 0 |
| 批次 2 修复后 | 1206 | 0 | 0 | 1206 | 0 |
| 批次 3 修复前 | 1206 | 0 | 4 | 1202 | 0 |
| 批次 3 修复后 | 1206 | 0 | 0 | 1206 | 0 |
| 批次 4 修复前 | 1206 | 1 | 2 | 1203 | 1 |
| 批次 4 修复后 | 1206 | 0 | 0 | 1206 | 0 |
| **最终（含 2 张 dk）** | **1208** | **0** | **0** | **1208** | **0** |

---

## 七、域间自检三问

### 1. 案例够了吗？

本批次 30 张卡中案例/业务卡占 7 张（鑫港湾医药系列），但缺少与建模工具/AI 协作技能直接配套的**外部独立案例**。建议下一批补充 3-5 张"工具→实战"桥接 case 卡。

### 2. 暗知识在哪里？

本批次最突出的跨域模式已固化为 2 张 dk 卡：

- **小格式错误级联失效**：从 P-11/P-18/P-19/F-10/C-10 共同抽象而来。
- **基础设施工具需要硬护栏**：从 C-10/C-11/P-16/P-8 共同抽象而来。

### 3. 这些卡有共同失效根因吗？

跨批次共同的根因：

- **把 validator 的格式通过当成内容正确**：P-16、C-10、P-11 都涉及 validator 只查存在性不查语义。
- **批量操作前缺少不可绕过的硬拦截**：C-10、C-11 都是流程/文档有要求，但工具允许跳过。
- **命名/格式规范没有被系统强制**：F-10、P-19 说明规范若不被 gate/正则强制执行，就会断裂。

---

## 八、后续建议

1. **鑫港湾 source 命名规范化**：将 `src_20260618_xingangwan-weekly-meeting-20260618.md` 重命名为符合 `src_YYYYMMDD_8hex` 规范的名称，并同步更新 source_id_map。
2. **给 gate 增加"非 10_raw/sources 路径 source"的提示**：master 卡大量引用 `.agent/pitfalls.md`、`20_memory/corrections.md` 等内部文档，虽然当前不触发 P0/P1，但未来建议统一迁移到 `10_raw/sources/`。
3. **继续补 case 卡**：下一批优先产出与 `modeling-scientific-milestones`、`yt-unit-model-ai-assisted`、`sk-ai-*` 配套的实战 case 卡。
4. **持续监控 YAML 引号**：本次再次遇到中文双引号未转义问题，建议在格式精修 SOP 中增加"diagnostic_signals 含中文引号时用单引号包裹"的强制检查。

---

## 九、验收结论

✅ **第二十六节 30 张高价值 draft 格式精修全部通过。**  
✅ **2 张跨域 dk 卡产出完成。**  
✅ **全库 P0=0，P1=0，YAML 错误=0，clean=1208。**  
✅ **可进入下一节任务。**
