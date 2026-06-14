# Stage 3 作者深度审查报告：老顽童 · 建模系列

**审查范围**：30_wiki 中 author = 老顽童 的建模相关卡片（以清单 `laowantong-modeling.txt` 为准）  
**审查时间**：2026-06-14  
**审查样本数**：24 张  
**审查维度**：内容完整性、Source 可验证性、Confidence / Trust 一致性、卡片间关系、类型特定检查  
**审查结论**：整体质量较高，结构完整、来源可追溯；但存在较多跨卡片 dangling 链接、部分卡片内容重叠、个别卡片内部重复，需要批量清理与人工归并。

---

## 一、审查样本清单

| 序号 | 文件路径 | 类型 |
|------|----------|------|
| 1 | `concepts/modeling-capability-system.md` | concept |
| 2 | `concepts/modeling-three-values.md` | concept |
| 3 | `dark-knowledges/dk-modeling-ai-cross-validation.md` | dark-knowledge |
| 4 | `dark-knowledges/dk-modeling-ai-iterative-prompting.md` | dark-knowledge |
| 5 | `dark-knowledges/dk-modeling-ai-judgment-limit.md` | dark-knowledge |
| 6 | `dark-knowledges/dk-modeling-expert-consensus-five-percent.md` | dark-knowledge |
| 7 | `dark-knowledges/dk-modeling-explanatory-vs-predictive-essence.md` | dark-knowledge |
| 8 | `dark-knowledges/dk-weekly-modeling-iteration-growth-engine.md` | dark-knowledge |
| 9 | `frameworks/modeling-personal-practice-loop.md` | framework |
| 10 | `frameworks/modeling-scientific-milestones.md` | framework |
| 11 | `frameworks/modeling-three-stages.md` | framework |
| 12 | `tools/modeling-level-map.md` | tool |
| 13 | `tools/modeling-weapon-library.md` | tool |
| 14 | `tools/process-modeling.md` | tool |
| 15 | `tools/tool-binary-quadrant-modeling.md` | tool |
| 16 | `tools/tool-canvas-weapon-library-modeling.md` | tool |
| 17 | `tools/tool-checklist-cheatsheet-modeling.md` | tool |
| 18 | `tools/tool-essence-nfactor-modeling.md` | tool |
| 19 | `tools/tool-funnel-formula-modeling.md` | tool |
| 20 | `tools/tool-iceberg-triangle-modeling.md` | tool |
| 21 | `tools/tool-radar-chart-modeling.md` | tool |
| 22 | `tools/tool-sabc-tier-modeling.md` | tool |
| 23 | `tools/tool-scenario-selector-modeling.md` | tool |
| 24 | `tools/tool-sop-template-modeling.md` | tool |

---

## 二、问题分类统计

| 问题类别 | 涉及卡片数 | 占比 | 严重等级 |
|----------|-----------|------|----------|
| 跨卡片 dangling 链接（related 指向不存在的卡片） | 17 / 24 | 70.8% | ⚠️ 中 |
| 卡片间内容重叠 / 边界模糊 | 4 / 24 | 16.7% | ⚠️ 中 |
| Source 引用与 frontmatter source_refs 不一致 | 2 / 24 | 8.3% | 🔴 高 |
| 卡片内部重复内容 | 1 / 24 | 4.2% | ⚠️ 中 |
| 无明显问题 | 7 / 24 | 29.2% | ✅ 通过 |

> 注：部分卡片同时存在多类问题，因此各类别“涉及卡片数”之和大于 24。

---

## 三、具体卡片问题清单

### 🔴 高优先级

#### 1. `tools/tool-essence-nfactor-modeling.md` — Source 引用与 frontmatter 不一致
- **问题描述**：Claim C1 引用依据为 `src_20260614_82a28d3f`，但 frontmatter `source_refs` 中仅列出 `src_20260614_73352fa5`、`src_20260614_8269ccdb`、`src_20260614_42f1e977` 三个 source。该 source 既未在 source_refs 中注册，也未在 Sources 列表中出现。
- **处理建议**：
  - 若 `src_20260614_82a28d3f` 确实为有效来源，补充到 frontmatter source_refs 与 Sources 章节；
  - 若该引用为笔误或已被合并，应替换为实际使用的 source ID。

#### 2. `tools/tool-sabc-tier-modeling.md` — Source 引用与 frontmatter 不一致
- **问题描述**：Claim C2 和 C4 引用 `src_20260614_82a28d3f-一堂-高阶建模-能力分层.md`，但 frontmatter `source_refs` 与 Sources 列表均未包含该 source。这会导致来源无法追溯。
- **处理建议**：补充 source 到 frontmatter 与 Sources 章节，或替换为已归档 source。

---

### ⚠️ 中优先级

#### 3. `tools/tool-scenario-selector-modeling.md` — 卡片内部内容重复
- **问题描述**：
  - “Step 2：根据子问题选择工具”表格连续出现两次；
  - “Step 3：检查前提条件”连续出现两次；
  - “Quick Decision Tree”同时以文本表格形式和代码块（` ``` `）形式各出现一次，内容基本相同。
  这种重复会显著降低卡片的信息密度和可维护性。
- **处理建议**：删除重复表格与重复前提条件段落；保留一种“Quick Decision Tree”呈现形式（建议保留代码块，更易被脚本解析）。

#### 4. `concepts/modeling-capability-system.md` 与 `frameworks/modeling-three-stages.md` — 内容高度重叠
- **问题描述**：
  - 两张卡片都详细阐述“流程建模（60 分）→ 抽象建模（75 分）→ 本质提炼（85 分）”三段论；
  - 都包含类似的 Claims、Constraints & Boundaries、Action Triggers、关联卡片；
  - `modeling-capability-system.md` 定位为“高阶建模能力体系”总览，而 `modeling-three-stages.md` 定位为“三段论”拆解，但两者的边界在实际内容中不够清晰，读者容易困惑。
- **处理建议**：
  - 人工判定两张卡片的职责边界：`modeling-capability-system.md` 保留体系总览、L1-L6 段位、武器库概述；`modeling-three-stages.md` 聚焦三段论的定义、递进关系、阶段选择决策树；
  - 删除重复 Claims，用 `[[...]]` 互相引用代替展开。

#### 5. `concepts/modeling-capability-system.md` 与 `tools/modeling-level-map.md` 与 `frameworks/modeling-personal-practice-loop.md` — L1-L6 段位定义重叠
- **问题描述**：
  - `modeling-capability-system.md` 简要列出 L1-L6；
  - `modeling-level-map.md` 将其扩展为自评工具；
  - `modeling-personal-practice-loop.md` 再次用 L1-L6 作为修炼路径。
  三段定义基本一致，但时间尺度的表述略有差异（例如 L5-L6 在 level-map 中为“年/十年”，在 practice-loop 中明确为“年 / 十年”），没有冲突，但存在重复维护风险。
- **处理建议**：将 L1-L6 的“标准定义”收敛到 `modeling-level-map.md`，其他卡片只保留与本主题最相关的段位描述，并通过链接引用 level-map。

#### 6. `tools/process-modeling.md` 与 `tools/tool-checklist-cheatsheet-modeling.md`、`tools/tool-sop-template-modeling.md` — 边界可更清晰
- **问题描述**：
  - `process-modeling.md` 是“流程建模”完整方法论，已经包含清单/SOP 格式、加锁机制、执行率数据；
  - `tool-checklist-cheatsheet-modeling.md` 和 `tool-sop-template-modeling.md` 又把清单、SOP 作为独立工具展开。
  三者内容存在交叉，尤其是“加锁执行率 50-70% / 70-90% / 近 100%”在多个卡片中重复出现。
- **处理建议**：
  - `process-modeling.md` 保留“何时启动流程建模、如何识别建模点、如何趁热复盘”等框架性内容；
  - 清单/SOP 的具体格式与执行锁机制收敛到对应 tool 卡片，process-modeling.md 中只给出摘要和链接。

#### 7. 大量 `related` 链接指向当前知识库中不存在的卡片
- **问题描述**：在 24 张样本中，共有 17 张卡片引用了尚未创建的卡片。典型示例：
  - `dk-modeling-ai-cross-validation.md` → `[[dk-modeling-counterexample-driven]]`
  - `dk-modeling-ai-iterative-prompting.md` → `[[dk-modeling-ai-self-retrospection]]`
  - `dk-modeling-ai-judgment-limit.md` → `[[dk-modeling-ai-without-judgment]]`
  - `dk-modeling-explanatory-vs-predictive-essence.md` → `[[dk-modeling-essence-predictive]]`、`[[case-essence-education-strategy]]`
  - `dk-weekly-modeling-iteration-growth-engine.md` → `[[framework-course-milestone-model]]`、`[[concept-thousand-people-square]]`、`[[case-child-drawing-rhyme]]`
  - `modeling-personal-practice-loop.md` → `[[tool-iterative-recursive-deep-dig]]`
  - `modeling-scientific-milestones.md` → `[[dk-modeling-counterexample-driven]]`、`[[tool-ai-skill-engineering-method]]`
  - `tool-checklist-cheatsheet-modeling.md` → `[[dk-modeling-sop-execution-locks]]`、`[[dk-modeling-timely-review-session-window]]`
  - `tool-essence-nfactor-modeling.md` → `[[dk-modeling-essence-predictive]]`、`[[dk-modeling-counterexample-driven]]`
  - 其他如 `tool-funnel-formula-modeling.md`、`tool-iceberg-triangle-modeling.md`、`tool-radar-chart-modeling.md`、`tool-sabc-tier-modeling.md`、`tool-sop-template-modeling.md` 等均存在 dangling 链接。
- **处理建议**：
  - 先通过脚本批量扫描这 24 张卡片的所有 `[[...]]` 链接，输出“目标文件不存在”的清单；
  - 对明确尚未产出的卡片，保留链接并标记为 `待创建` 或加注释；
  - 对已改名或移动的卡片，人工修正链接。

---

### ✅ 无明显问题

以下卡片在内容完整性、Source 可验证性、Confidence / Trust 一致性、类型特定检查上均表现良好，建议直接通过：

- `concepts/modeling-three-values.md`：定义清晰、例子具体、来源明确，confidence 0.85 / trust high 与内容质量匹配。
- `dark-knowledges/dk-modeling-ai-cross-validation.md`：有原始引用、操作步骤、边界条件，暗知识类型判断准确。
- `dark-knowledges/dk-modeling-ai-iterative-prompting.md`：误区、后果、避免方法完整，操作步骤可执行。
- `dark-knowledges/dk-modeling-ai-judgment-limit.md`：原则型暗知识，有明确使用场景与操作方法。
- `dark-knowledges/dk-modeling-expert-consensus-five-percent.md`：概念明确、步骤具体、边界清晰。
- `dark-knowledges/dk-modeling-explanatory-vs-predictive-essence.md`：误区定义清楚，后果与避免方法完整。
- `dark-knowledges/dk-weekly-modeling-iteration-growth-engine.md`：组织级洞察，有原始引用、操作方法、适用边界。
- `frameworks/modeling-scientific-milestones.md`：框架完整，有 Protocol、When NOT to Use、Critique、反事实测试，质量最高之一。
- `frameworks/modeling-personal-practice-loop.md`：修炼路径表清晰，案例/动作对应明确。
- `tools/tool-binary-quadrant-modeling.md`：使用步骤、边界条件、示例完整。
- `tools/tool-canvas-weapon-library-modeling.md`：画布与武器库两个工具的职责区分清楚。
- `tools/tool-funnel-formula-modeling.md`：漏斗图与公式两种工具的使用步骤、边界、示例均完整。
- `tools/tool-iceberg-triangle-modeling.md`：冰山图分层、三角图三要素关系说明清楚。
- `tools/tool-radar-chart-modeling.md`：维度定义、评分标准、决策规则完整。

---

## 四、批量处理建议

| 批量处理项 | 是否可脚本化 | 处理策略 |
|------------|--------------|----------|
| 扫描并列出所有 dangling `[[...]]` 链接 | ✅ 可脚本化 | 用脚本读取 24 张卡片正文，提取所有 `[[...]]` 链接，与 `30_wiki/**` 实际文件路径比对，输出缺失清单。 |
| 检查 `source_refs` 与 Claims 中引用 source ID 的一致性 | ✅ 可脚本化 | 解析 frontmatter 中的 `source_refs`，再正则匹配 Claims 中的 `src_xxxxxx` 引用，找出未注册的 source ID。 |
| 检测卡片内部重复段落/表格 | ✅ 可脚本化（半自动） | 用相似度算法（如段落哈希）检测同一文件内重复超过阈值的段落，人工确认后删除。 |
| 检测跨卡片重复/重叠内容 | ⚠️ 半自动化 | 可用文本相似度或向量相似度找出高度相似的卡片对，但合并/拆分策略必须由人工判定。 |
| 归并 `modeling-capability-system.md` / `modeling-three-stages.md` / `modeling-level-map.md` | ❌ 必须人工 | 需要重新定义每张卡片的职责边界，删除重复 Claims 与表格，调整交叉引用。 |
| 区分 `process-modeling.md` 与 `tool-checklist-cheatsheet-modeling.md` / `tool-sop-template-modeling.md` | ❌ 必须人工 | 需决定哪些内容保留在框架卡片、哪些收敛到工具卡片，避免多处维护同一机制。 |
| 修正/补充 `tool-essence-nfactor-modeling.md` 与 `tool-sabc-tier-modeling.md` 中缺失的 source | ❌ 必须人工 | 需要核对原始 source 文件是否存在、是否已被合并，再决定补充 ID 或替换引用。 |

---

## 五、总体评价

老顽童的建模系列卡片整体结构规范、Burn line 鲜明、Protocol / Action Triggers / Sources 等模块齐全，符合 30_wiki 的写作标准。主要风险集中在**知识库级别的链接治理**和**部分卡片的内容收敛**：

1. **链接治理**：约 70% 的卡片引用了未创建的卡片，长期会削弱知识网络的可用性。建议作为本阶段批量修复的首要任务。
2. **内容收敛**：体系总览、三段论、段位图三张卡片存在重复维护。建议明确“单点真相”后收敛。
3. **来源一致性**：两张工具卡片的 Claims 引用了未在 frontmatter 注册的 source，需补充或修正。
4. **内部重复**：`tool-scenario-selector-modeling.md` 的重复内容可快速清理。

建议在批量脚本治理之后，由熟悉一堂建模课程内容的编辑对 4 组重叠卡片进行人工归并，确保读者不会在不同卡片中读到重复但略有差异的定义。

---

*审查员：Kimi Code CLI · Stage 3 深度审查 · 仅审查、未修改原文件*
