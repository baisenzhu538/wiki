---
plan_id: "plan_20260503_f3e9a2b1"
type: "improvement-plan"
status: "draft"
created_at: "2026-05-03T12:00:00+00:00"
feedback_count: 1
artifact_count: 10
source_count: 12
assessment_ref: "60_feedback/assessments/claude-20260503-kdo仓库遍历与健康度评估.md"
---

# Improvement Plan plan_20260503_f3e9a2b1

## 来源

本计划由 Claude 全仓库遍历评估（`claude-20260503-kdo仓库遍历与健康度评估.md`）触发，替代此前重复生成的 8 个同类计划。

---

## Summary

- **Sources**: 12（已 ingest，待 enrich）
- **Artifacts**: 10（8 failing validate，2 passing）
- **Feedback records**: 18（13 simulated + 5 eval-results）
- **Lint issues**: 14 broken wikilinks
- **Memory layer**: 0% 填充
- **Contradictions**: 0 条记录

---

## Priority 1: 修复基础链路断裂（P0）

### 1.1 跑通 enrich：完成至少 1 个 source 的三步编译法

**目标**：将 1 个未 enrich 的 source 转化为标准知识卡片，验证 enrich 链路可运行。

**推荐 source**：`src_20260501_9962715b`（互联网医院模式深度调研报告）
- 已有对应 artifact `art_20260501_0ac5504f`，说明 source 内容完整
- 但 `30_wiki/concepts/互联网医院模式深度调研报告.md` 尚未执行完整 Condense / Critique / Synthesis

**执行步骤**：
1. 读取 `10_raw/sources/src_20260501_9962715b-互联网医院模式深度调研报告.md`
2. 执行 Condense：提取 3-5 条核心结论
3. 执行 Critique：逐条评估前提假设、边界与反例、可靠性
4. 执行 Synthesis：创建与现有 wiki 页面的 `双向链接`（如 [[诊所O2O外卖平台业务深度调研报告]]、[[鑫港湾his系统分阶段整改报告]]）
5. 补充 Open Questions 和 Output Opportunities
6. 更新 frontmatter：`status: reviewed`，`trust_level: medium/high`
7. 运行 `kdo lint` 确认 0 error

**验收标准**：该 wiki 页面通过 `kdo lint`，且 Critique + Synthesis 非空。

---

### 1.2 清理 artifact 空壳，回退失实 status

**目标**：让所有 artifact 的 `status` 与实质内容一致。

**行动**：

| artifact_id | 当前问题 | 行动 |
|-------------|---------|------|
| `art_20260427_16a7c4d7` | draft missing (0 words) | status → `stub`；补充 draft 或移除 ship 记录 |
| `art_20260430_cd02f27c` | TODO 残留，draft 6 词 | status → `draft`；完成 Core Thesis 和 Draft |
| `art_20260430_a947d7a5` | TODO 残留，draft 6 词 | status → `draft`；完成 Core Thesis 和 Draft |
| `art_20260501_cc0af2d7` | TODO 残留，draft short | status → `draft`；完成 Core Thesis 和 Draft |
| `art_20260430_447f2eea` | draft 19 词（偏短） | status 保持 `ready`，但建议扩充至 500+ 词再 ship |

**新增质量门**：在 `produce-and-ship-flow.md` Step 6 增加硬性规则：
> `content_draft_length < 200 字` 的 artifact **禁止**进入 Ship 阶段。

---

### 1.3 激活 20_memory/ 跨会话记忆

**目标**：让 AI 新会话能加载历史上下文。

**最低填充要求**：
- `20_memory/project-continuity.md`：追加本次 session 摘要（日期、处理 source 数、产生 artifact 数、未决问题）
- `20_memory/user-preferences.md`：写入用户已知偏好（如输出渠道偏好、领域关注优先级）
- `20_memory/operating-principles.md`：写入 3-5 条本仓库的运作原则（如"先 enrich 后 produce"、"ship 前必须通过 validate"）

**机制**：在 `Knowledge Curator Skill` Procedure 中增加 Step 0：
> "会话开始时读取 `20_memory/` 全部文件，加载 continuity 与 preferences。"

---

## Priority 2: 修复结构性缺陷（P1）

### 2.1 修复 14 个 broken wikilink

**来源**：`kdo lint` 报告

**涉及页面**：
- `30_wiki/concepts/紫鲸ai智能体工作流平台.md`：4 个断链
- `30_wiki/concepts/街顺app全面调研报告.md`：6 个断链
- `30_wiki/concepts/鑫港湾his系统分阶段整改报告.md`：4 个断链

**策略**：
- 若链接指向的概念有价值且暂无页面 → 创建 stub 页面（仅 frontmatter + 一句话描述）
- 若链接指向的概念超出当前仓库范围 → 改为纯文本，移除 `[[...]]`
- 修复后运行 `kdo lint` 验证 0 warning

**新增 lint 规则**：broken wikilink 从 **warning** 提升为 **error**。

---

### 2.2 合并/关闭冗余 improvement plan

**行动**：
1. 将本计划（`plan_20260503_f3e9a2b1`）设为当前唯一活跃计划
2. 将此前 8 个 plan（`plan_20260501_*`）的 status 统一改为 `superseded`，并在每个文件头部追加：
   ```markdown
   > **Status**: superseded by `[[plan_20260503_f3e9a2b1]]`
   ```
3. 在 `System Linter Skill` 中增加 "Plan Drift" 检查：若未关闭 plan 数量 > 3，标红告警

---

### 2.3 创建 contradictions.md 示范条目

**推荐矛盾对**：
- **A 方**：YC AI-Native 方法论（"中层管理变 markdown，消除人肉中间层"）
- **B 方**：街顺 APP 实践（"百人真人客服团队是核心竞争壁垒，按营业额 6% 抽成"）
- **张力**：YC 主张用 AI/agent 替代中层与客服人力；街顺用重人力客服构建 SaaS 差异化。两者在"组织设计是否应去人力化"上存在直接冲突。

**格式**：
```markdown
| id | source_a | source_b | description | status | resolution |
|----|----------|----------|-------------|--------|------------|
| c_001 | src_20260430_8cc84e5b | src_20260427_970eb338 | YC主张AI替代中层 vs 街顺依赖百人客服 | open | 待评估 |
```

---

## Priority 3: 对齐工具链与文档（P2）

### 3.1 对齐源码与 pip 安装版

**执行**：
```bash
pip install -e /path/to/kdo/source --force-reinstall
kdo --help | grep -E "lint|validate|enrich|improve"
kdo lint
kdo validate
```

**验证清单**：
- [ ] `kdo lint` 行为与 `90_control/scripts/kdo_lint.py` 源码一致
- [ ] `kdo validate` 的检查维度与 `90_control/scripts/kdo_validate.py` 一致
- [ ] 若 CLI 版更完整，将 CLI 代码覆盖到仓库脚本，确保单一 truth source

---

### 3.2 更新 quality-gates/ 文档

**行动**：将 `kdo_validate.py` 中每个 gate 的通过/失败标准逐条映射到 `quality-gates/*.md`：
- `content.md`：补充 `content_draft_length >= 200` 等量化标准
- `capability.md`：补充 `capability_eval_cases_filled` 等检查点
- 每份文档末尾增加 "Script Reference" 段落，注明对应代码位置

---

### 3.3 确认 registry 文件同步状态

**行动**：
1. 读取 `90_control/source-registry.yaml` 和 `artifact-registry.yaml`
2. 对比 `.kdo/state.json` 中的 source 列表与 artifact 列表
3. 若存在差异，以 `state.json` 为 truth source 修正 yaml，或删除 yaml 并在 PROTOCOL.md 中注明 truth source 位置

---

## Priority 4: 扩展真实反馈与图谱查询（P3）

### 4.1 完成 1 次真实交付并收集人类反馈

**推荐 artifact**：`art_20260430_447f2eea`（AI-Native 公司组织方法论）
- 已有实质内容（非空壳）
- topic 热度高，易获得读者反馈

**行动**：
1. 将 draft 扩充至 1500+ 字
2. 通过 `kdo validate` 全部通过
3. Ship 到真实渠道（微信公众号 / 知乎 / Newsletter）
4. 在文章末尾放置反馈收集方式
5. 收到真实反馈后，格式化为标准 markdown 存入 `60_feedback/comments/`

---

### 4.2 给 `kdo query` 增加 `--graph` 支持

**短期实现**（纯 stdlib，零依赖）：
1. 读取 `30_wiki/.graph/index.json`
2. 当查询命中某节点时，同时返回其 1-hop 邻居节点列表
3. 在 `kdo query` CLI 中增加 `--graph` flag 开关该行为

**中期**：废弃未使用的 `SearchIndex` 向量搜索，降低维护负担，直到有明确需求再重建。

---

## Closure Criteria

本计划关闭需同时满足：

1. [ ] 至少 1 个 source 完成完整 enrich（三步编译法），`kdo lint` 0 error
2. [ ] 所有 artifact 的 `status` 与实质内容一致，无 TODO 残留
3. [ ] `20_memory/` 至少 3 个文件有非空内容
4. [ ] `kdo lint` broken wikilink = 0
5. [ ] 此前 8 个冗余 plan 已标记为 `superseded`
6. [ ] `contradictions.md` 至少有 1 条示范条目
7. [ ] 源码与 pip 版 `kdo lint/validate` 行为一致
8. [ ] `quality-gates/*.md` 与脚本检查点逐条对齐
9. [ ] 完成 1 次真实 ship 并收集到 ≥1 条真实人类 feedback

---

## Recommended Next Single Action

> **立即执行**：挑选 1 个未 enrich 的 source（推荐互联网医院报告），手动完成完整的三步编译法，产出第一张标准知识卡片。这是验证"基础链路可跑通"的最小可行动作。

---

*Plan created: 2026-05-03*  
*Supersedes: plan_20260501_e1e150b9, plan_20260501_05858800, plan_20260501_8001399c, plan_20260501_85a84b92, plan_20260501_8ecb74e3, plan_20260501_97170532, plan_20260501_ca61cdd7, plan_20260501_47264869*
