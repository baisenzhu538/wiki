# Stage 3 作者深度审查报告：老顽童 cases 样本

- **审查样本数**：16 张卡片（15 张 `case` + 1 张 `dark-knowledge`）
- **审查维度**：内容完整性、Source 可验证性、Confidence/Trust 一致性、与其他卡片关系、类型特定检查
- **审查日期**：2026-06-14
- **审查说明**：本报告仅做审查记录，**未修改任何原始文件**

---

## 一、总体结论

本次审查的 16 张卡片整体结构完整，普遍具备 Background / What Happened / 关键证据 / 可迁移场景 / 教训 / 失败模式 / Sources 等模块，Source 均能追溯到 `src_20260614_8269ccdb`（一堂建模能力培训 Truman 口述转录文本），格式较为统一。

主要问题集中在以下几类：

1. **Case  outcome 可验证性偏弱**：大量案例的结果描述为定性判断，缺少量化数据、基线对比或独立第三方验证。
2. **Source 引用格式不一致**：部分卡片 Sources 底部使用 `src_...-一堂-建模能力培训-truman-口述.md:...`，与多数卡片的 `.txt:...` 路径不统一。
3. **卡片间存在冲突/重复**：
   - `case-course-milestone-model`（六步）与 `framework-course-milestone-model`（七步）步骤数冲突。
   - `case-thousand-people-square` 与 `concept-thousand-people-square` 内容高度重叠。
   - “5% after 状态”与“5% 专家”两种表述混用；“千人广场”与“销冠广场”术语不统一。
4. **类型模板不匹配**：`dk-modeling-case-explosion-confidence` 作为 `dark-knowledge`，缺少该类型要求的“误区 / 后果 / 避免方法”。
5. **元数据独立性不足**：16 张卡片 `author` 与 `reviewed_by` 均为“老顽童”，且 `review_date` 与 `created_at` 相同，属于自审。

---

## 二、问题分类统计

| 问题分类 | 涉及卡片数 | 说明 |
|---|---|---|
| Case outcome / 可验证结果不足 | 8 | 结果多为“明显提升”“越来越少犯错”等定性描述，缺量化数据或独立验证 |
| Source 格式/原始性不足 | 6 | Sources 路径 `.md` / `.txt` 混用；部分关键数据仅有口述回忆，无原始材料 |
| Confidence/Trust 与证据强度不匹配 | 3 | 高 confidence 但仅有二手引用或口头回忆，证据支撑偏弱 |
| 卡片关系冲突/重复/术语不一致 | 4 | 步骤数冲突、案例卡与概念卡高度重叠、“5%”定义与广场术语混用 |
| 类型模板不匹配 | 1 | dark-knowledge 卡缺少“误区 / 后果 / 避免方法” |
| 元数据/评审独立性 | 16 | author = reviewed_by，review_date = created_at，自审痕迹明显 |

> 注：一张卡片可能同时落入多个分类，因此总数大于 16。

---

## 三、具体卡片问题清单

### 1. `cases/case-ai-agent-milestone-design.md`
- **问题**：无明显结构性问题。
- **建议**：案例 outcome 数据（3 小时、42 轮、48 个组件）具体，但均为 Truman 自评。如有 AI 产出物或会议记录，可作为附件链接以增强可验证性。

### 2. `cases/case-ai-assisted-review.md`
- **问题**：内容完整，但 outcome 缺少量化数据。
- **建议**：补充例如“AI 辅助复盘后，单条文案迭代时间从 X 小时降到 Y 分钟”或“错误发现率提升 Z%”等数据；若无法获取，可在卡片中标注“暂无量化数据”。

### 3. `cases/case-child-drawing-rhyme.md`
- **问题**：最小建模案例叙事清晰，但效果验证为定性描述。
- **建议**：补充基线（如练习前控笔评分/作品数量）与后续观察记录；无数据时可降低 confidence 或加“家长观察记录”标签。

### 4. `cases/case-course-milestone-model.md` ⚠️ 重点问题
- **问题**：
  - 案例标题为“**六步**生产流程”，而 `framework-course-milestone-model.md` 为“**七步**里程碑”。
  - 案例的六步缺少“预案”，并把“封装与包装打磨”合并为一步；框架则拆分为“封装”与“包装打磨”两步。
  - 两张卡片 Sources 范围接近（案例 `2170-2248`，框架 `2170-2262`），说明来自同一段材料，但提炼结果不一致。
- **建议**：
  - 人工判断：确认当前一堂官方做课流程是六步还是七步。
  - 若框架为最新版，更新案例为七步并说明“案例呈现的是某一次具体落地中的简化路径”。
  - 若两者适用场景不同，应在卡片中明确标注版本/适用范围差异。

### 5. `cases/case-essence-education-strategy.md`
- **问题**：Sources 底部路径格式与多数卡片不一致。
- **建议**：统一为 `00_inbox/建模能力/一堂-建模能力培训-truman-口述.txt:2824-3020` 或 `src_20260614_8269ccdb:2824-3020`，避免 `src_...-一堂-建模能力培训-truman-口述.md` 这种混合写法。

### 6. `cases/case-essence-entrepreneurship.md` ⚠️
- **问题**：
  - Sources 路径格式不一致（同第 5 条）。
  - “创业成功率 3%–10%”为 Truman 引述其早期领导的话，无原始出处或行业数据支撑，属于二手引用。
  - `confidence: 0.85` / `trust_level: high` 对该类无实证支撑的引用略显偏高。
- **建议**：
  - 统一 Source 路径格式。
  - 对“3%–10%”添加注释，说明是“课上引用的经验判断”而非统计数据；或补充相关研究报告链接。
  - 考虑将 confidence 降至 0.75–0.80。

### 7. `cases/case-essence-humanity-trap.md`
- **问题**：无明显问题。
- **建议**：Source 路径格式正确，内容完整。保持即可。

### 8. `cases/case-livestream-sop-modeling.md` ⚠️
- **问题**：
  - outcome 可验证性弱：仅有“主播状态波动明显减小”“新人更快进入稳定状态”等定性描述，无执行率、满意度、开播事故率等数据。
  - Sources 路径使用 `.md` 格式；`source_refs` 中的第二个来源 `src_20260614_623cfbfd` 仅在 Sources 列表出现，未在“关键证据”中具体引用。
  - 与 `case-zhangyang-anchor-sop-three-locks.md` 主题相近，边界需更清晰。
- **建议**：
  - 补充量化结果（如执行前开播事故率 X%，执行后降至 Y%）。
  - 统一 Source 格式，并在关键证据中说明第二个来源支持的结论。
  - 在 related 或卡片开头说明两卡片的区别：本卡聚焦“直播前热身 SOP 建模”，张扬案例聚焦“SOP 三层执行锁”。

### 9. `cases/case-nine-pm-livestream-survey.md` ⚠️
- **问题**：
  - 核心结论“认真做过三次调研，多数人选 21:00”仅来自 Truman 口述，无调研原始数据、样本量、问卷版本、时间范围。
  - 作为 `case` 类型，缺少 outcome/数据支撑。
  - `confidence: 0.85` / `trust_level: high` 与证据强度不匹配。
- **建议**：
  - 若原始调研记录存在，补充样本量、选项设计、统计结果。
  - 若仅有口述回忆，建议将标题或卡片状态标注为“口述回忆版”，并将 `trust_level` 降至 `medium`，`confidence` 降至 0.70–0.75。

### 10. `cases/case-personal-map-modeling.md`
- **问题**：内容详尽，但 Sources 路径使用 `.md` 格式，与多数 `.txt` 不一致。
- **建议**：统一 Source 路径格式；如有地图 1.0/终稿文件，可作为附件链接。

### 11. `cases/case-thousand-people-square.md` ⚠️ 重点问题
- **问题**：
  - 与 `concept-thousand-people-square.md` 内容高度重叠（95% before / 5% after、反例即错误、案例大爆炸等），案例卡未提供独立的时间线、决策冲突或结果数据，价值感弱。
  - 卡片中“5% 是训练过的 after 状态”与 `dk-modeling-expert-consensus-five-percent.md` 的“5% 的专家决定最大公约数”语义不一致。
  - `dk-modeling-case-explosion-confidence.md` 使用“销冠广场”，而本卡与概念卡使用“千人广场”，术语不统一。
- **建议**：
  - 人工判断：要么将本案例卡合并到概念卡，要么为本卡补充一堂内部应用“千人广场”的具体故事、争议与结果数据。
  - 在概念层统一“5%”的定义：是“after 状态的学员”还是“具备实战经验的专家”，或说明两者关系。
  - 统一“销冠广场”与“千人广场”术语，或在卡片中明确两者关系（同义/子集/应用场景不同）。

### 12. `cases/case-truman-ai-skill-engineering-guide.md`
- **问题**：无明显结构性问题。
- **建议**：Sources 路径使用 `.md` 格式，建议统一；交叉验证评分（S / A / B+）为 Truman 自评，可注明“主观评分”。

### 13. `cases/case-yitang-education-supply-chain.md`
- **问题**：无明显问题。
- **建议**：比喻清晰，逻辑自洽。如能提供课程排期实例（如“解放思想”课两年半打磨时间线）会更好。

### 14. `cases/case-yitang-radar-chart-selection.md`
- **问题**：内容完整，但 outcome 缺少量化数据。
- **建议**：补充雷达图数量、应用场次、重大决策错误减少的估算依据；无数据时可在卡片中说明。

### 15. `cases/case-zhangyang-anchor-sop-three-locks.md`
- **问题**：无明显问题。
- **建议**：执行率数据（50–70% → 70–90% → 近 100%）具体，是本批 case 中的良好范例。保持即可。

### 16. `dark-knowledges/dk-modeling-case-explosion-confidence.md` ⚠️
- **问题**：
  - 类型为 `dark-knowledge`，但正文缺少该类型要求的“明确误区、后果、避免方法”结构。
  - 使用“销冠广场”一词，而相关概念卡/案例卡使用“千人广场”，术语不统一。
  - `related` 中 `modeling-capability-for-kdo` 未使用 `[[...]]` 链接格式（其余 related 均使用）。
- **建议**：
  - 若坚持作为 dark-knowledge，补充“误区 / 后果 / 避免方法”章节；否则改为 `concept` 或 `insight` 类型。
  - 统一“销冠广场 / 千人广场”术语或说明关系。
  - 修复 `related` 链接格式为 `[[modeling-capability-for-kdo]]`。

---

## 四、批量处理建议

### 可脚本化批量修复

| 批量任务 | 脚本化方式 | 预期效果 |
|---|---|---|
| Source 路径格式统一 | 正则扫描 `Sources` 区块，统一为 `00_inbox/建模能力/一堂-建模能力培训-truman-口述.txt:line-line` 或 `src_id:line-line` | 消除 `.md` / `.txt` / `src_...-文件名.md` 混用 |
| `related` 链接有效性检查 | 遍历所有 `.md` 的 `related` 与正文 `[[...]]`，检测目标文件是否存在 | 发现断链或格式错误（如 `modeling-capability-for-kdo` 缺括号） |
| Case  outcome 数据缺失检测 | 扫描 `case` 类型卡片的 `# 结果` / `## Results` / `## 关键证据` 区块，判断是否有数字、百分比、时间等量化标记 | 快速定位 outcome 纯定性的卡片 |
| 卡片相似度检测 | 对 `case` 与同名/同主题 `concept`、`framework` 做文本相似度计算 | 发现像 `case-thousand-people-square` 与 `concept-thousand-people-square` 这种高度重叠 |
| Dark-knowledge 模板合规检查 | 检查是否包含“误区 / 后果 / 避免方法”或其同义标题 | 发现模板缺失 |
| `confidence` / `trust_level` 合理性初筛 | 对 `trust_level=high` 但关键证据全为口述回忆、且 confidence≥0.85 的卡片标红 | 提示人工复核 |

### 必须人工判断

| 人工任务 | 原因 |
|---|---|
| 解决 `case-course-milestone-model` 与 `framework-course-milestone-model` 的六步/七步冲突 | 需要确认当前官方流程与两张卡片的定位 |
| 统一“千人广场 / 销冠广场 / 5% after / 5% 专家”等概念关系 | 涉及知识本体设计，需由领域专家决定术语体系 |
| 决定是否合并 `case-thousand-people-square` 与 `concept-thousand-people-square` | 需权衡“案例卡独立叙事价值”与“避免重复” |
| 调整 `case-nine-pm-livestream-survey`、`case-essence-entrepreneurship` 等卡片的 confidence / trust | 需根据实际证据强度与可获取的原始材料综合判断 |
| 处理 `dk-modeling-case-explosion-confidence` 的类型归属 | 需决定是补齐 dark-knowledge 三要素，还是改为 concept/insight |
| 重新指定独立 reviewer | 当前 16 张卡片均为自审，建议由非作者完成 Stage 3 复核并更新 `reviewed_by` |

---

## 五、结论性建议

1. **优先修复冲突项**：`case-course-milestone-model` 与 `framework-course-milestone-model` 的步数冲突是最影响用户信任的问题，应尽快统一。
2. **术语治理**：建立“广场模型”与“5%”相关术语的规范，明确 `千人广场`、`销冠广场`、`5% after`、`5% 专家` 之间的关系。
3. **Outcome 数据补强**：对定性 outcome 较多的 case 卡片，尽量补充量化数据；无法补充时，应诚实标注并相应下调 confidence / trust。
4. **Source 格式标准化**：统一 Sources 底部路径格式，并确保 `source_refs` 与 Sources 区块一致。
5. **评审流程独立化**：建议由非“老顽童”的 reviewer 完成 Stage 3 复核，并更新 `reviewed_by` 与 `review_date`。

---

*报告生成：Kimi Code CLI · 阶段 3 质量审查 · 2026-06-14*
