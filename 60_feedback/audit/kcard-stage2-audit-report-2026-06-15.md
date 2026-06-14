# 30_wiki 阶段 2 高危卡片抽样审查报告

**报告日期**：2026-06-15  
**审查角色**：王语嫣  
**覆盖范围**：30_wiki 全库 1,320 张卡片  
**本阶段目标**：对阶段 1 元数据治理后仍存疑的两类高危卡片进行抽样审查，给出批量处理建议。

---

## 一、审查对象与抽样方法

阶段 1 完成后，剩余主要问题池如下：

| 问题类型 | 数量 | 抽样数 | Agent |
|---|---|---|---|
| 高置信低信任（confidence ≥ 0.85 但 trust_level 为空/低） | 152 | 30 | Agent 58 |
| 无 source（source_refs 为空） | 219 | 30 | Agent 59 |

抽样原则：
- 覆盖 concept / skill / case / framework / dk / entity 主要类型
- 覆盖不同 status（draft / enriched / reviewed / stable）
- 优先抽取 domain 分布较广、作者多样的卡片
- 仅审查，不直接修改文件

---

## 二、Agent 58：高置信低信任卡片审查结果

### 2.1 样本概况

审查 30 张卡片，发现 **约 40%（12 张）** 存在 confidence 虚高问题。

### 2.2 主要问题类型

| 问题类型 | 数量 | 典型表现 |
|---|---|---|
| draft / pending review 卡片高 confidence | 5 张 | 未审稿的草稿卡 confidence ≥ 0.85 |
| 课件截图/教学示例被标为高置信 | 3 张 | PNG 截图来源无法提供可验证数据 |
| 来源引用过于笼统 | 3 张 | 仅有作者名、空引用或口头来源 |
| trust_level 缺失或错配 | 约 13 张 | 已验证卡片未标 high，draft 卡未标 low |

### 2.3 批量处理建议

1. **draft + reviewed_by=pending 的卡片**：`confidence` 上限设为 **0.75**，`trust_level` 强制设为 `low` 或 `medium-low`。
2. **`source_refs` 仅含 PNG 且无 txt/md 的 case 卡片**：`confidence` 从 ≥0.85 下调至 **0.75**，`trust_level` 保持 `medium`。
3. **`source_refs` 为空或仅有口头/作者名的 concept/framework 卡片**：`confidence` 上限 **0.75**。
4. **有 outcome 验证或 correction 报告支撑的卡片**：补 `trust_level=high`，不调整 confidence。
5. **所有 `trust_level` 为空但 source 充分的 enriched/reviewed 卡片**：批量填为 `medium-high` 或 `high`（按 source 质量）。

---

## 三、Agent 59：无 source 卡片审查结果

### 3.1 核心结论

**无 source 卡不等于低质量卡。** 本次抽样的 24 张 enriched/reviewed/stable 卡片内容均较完整，多为课程体系整理、调研报告提炼或内部系统规格。直接降级会造成大量误伤。

### 3.2 关键发现

| 发现 | 数量 | 说明 |
|---|---|---|
| 来源可补的内部材料 | 多数 | 可对应到 `10_raw/sources/` 中的课程逐字稿、OCR 文件或调研报告源 |
| YAML 格式错误导致「假无 source」 | 2 张 | Kimi / YC 两张 entity 卡片的 `source_refs` 与 `id` 字段存在 YAML 错位 |
| tools 目录无 status | 5 张 | 单元模型工具卡 status 为空，是稳定区高危漏网之鱼 |
| 真正需要降级的空泛卡片 | 极少 | status 为 enriched/reviewed/stable 但内容空泛、无法溯源的样本中占比很低 |

### 3.3 批量处理建议

1. **先跑 source-matching 脚本**：按标题/id/domain 在 `10_raw/sources/`、`10_raw/assets/`、`10_raw/web/` 中匹配潜在源，自动生成 candidate source_refs。
2. **修复 YAML 格式错误**：重点检查 entity 卡片的 `source_refs` 与 `id` 字段是否错位。
3. **对匹配失败的 enriched/reviewed/stable 卡片统一降级为 draft**，而不是一刀切全部降级。
4. **对 tools 目录 status 为空的卡片**：统一降级为 draft 并补 source。
5. **对 1KB 以下 draft skill/OCR 卡片做专项清理**：这类最可能是占位卡，是废弃比例的主要来源。

---

## 四、综合结论

1. **高置信低信任卡片需要立即批量修正**：这类卡片最容易误导用户，规则清晰，适合脚本化处理。
2. **无 source 卡片需要先做 source-matching，再降级**：内容价值不低，优先补来源，避免误伤。
3. **tools 目录和 entity 类型是下一阶段重点**：一个 status 缺失率高，一个存在 YAML 格式错误。
4. **元数据治理（阶段 1）已经显著降低了审查噪音**：author 已全部补全，reviewer 剩余 47 张，为后续按作者/来源追责打下基础。

---

## 五、下阶段计划（阶段 3）

**目标**：按作者进行深度审查，重点清理老顽童和黄药师的高风险卡片。

**理由**：
- 老顽童非药柜专项域审计已显示系统性问题（业务公式/AI 短剧/建模能力域流于形式、案例库缺失）
- 黄药师作为高产作者，需要验证其卡片 source 和 confidence 标注是否一致

**执行方式**：
1. 对老顽童卡片按 domain 分组，逐域审查
2. 对黄药师卡片抽样审查 source 和 trust_level 一致性
3. 输出按作者分类的问题清单和批量处理建议

---

## 附录：相关文件

- 阶段 1 元数据治理报告：`kcard-metadata-fix-report-2026-06-14.md`
- 全库基线报告：`kcard-baseline-report-2026-06-14.md`
- 全库卡片清单：`kcard-inventory-2026-06-14.csv`
- 老顽童非药柜专项审计：`老顽童非药柜专项域深度审计.md`
- 王语嫣今日复盘：`C:/Users/Administrator/Desktop/agent复盘/王语嫣/2026-06-13-王语嫣每日复盘.md`
