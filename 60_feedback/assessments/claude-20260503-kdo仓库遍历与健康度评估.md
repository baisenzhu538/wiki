---
title: "Claude KDO仓库遍历与健康度评估"
type: assessment
status: reviewed
assessor: "Claude"
assessment_date: "2026-05-03"
target: "KDO vault overall health"
source_refs: []
---

# Claude KDO 仓库遍历与健康度评估

> **评估日期**：2026-05-03  
> **评估者**：Claude（AI Agent，Arbiter + System Linter 角色）  
> **评估范围**：全仓库遍历（排除 `.git/`, `.obsidian/`）  
> **参考协议**：`90_control/PROTOCOL.md`, `90_control/routing-rules.md`, `CLAUDE.md`  
> **评估方法**：目录结构扫描 + 关键文件读取 + 数据质量交叉验证 + 流水线状态审计

---

## 一、总体健康度

| 层级 | 健康度 | 说明 |
|------|--------|------|
| **协议层** `90_control/` | **A** | PROTOCOL.md、routing-rules.md、7个Schema、3个Skill、3个Workflow、AGENT_TESTS.md 均完整且质量高 |
| **数据层** `30_wiki/` | **C** | 概念卡片两极分化（街顺报告为A+，其余多为骨架或缺失）；断链14处；contradictions.md空置 |
| **产出层** `40_outputs/` | **D** | 10个artifact中8个validation failure，多个draft仅6词或空壳；3个builtin skill为A |
| **记忆层** `20_memory/` | **F** | 全部空壳，跨会话连续性归零 |
| **反馈层** `60_feedback/` | **B-** | 18条记录格式规范，但13条为simulated、5条为eval-results，无真实人类反馈 |
| **流水线** | **D** | ingest跑通12 source，enrich=0，produce=10但空壳率高，ship=3但validate未通过 |

**综合判断**：这是一个 **"设计图比建筑更完整"** 的系统。协议与规则设计达到生产级水准，但核心数据链路（ingest → enrich → produce → validate）出现断裂，导致规则空转。

---

## 二、关键发现（P0 — 阻塞性）

### 2.1 Enrich 阶段完全空置，Wiki 是"伪编译层"

**证据**：
- 首次迭代报告（`iter_20260502_585f1206`）明确记录：`enrich: 0 wiki page(s) enriched`
- 12 个 source 被 ingest，但 `30_wiki/concepts/` 中大量 source 无对应知识卡片
- 多个 artifact（诊所O2O、互联网医院）疑似直接从 raw source 跳过 wiki 层产出

**影响**：KDO 的核心价值主张——"将原始资料编译为可复用知识"——未兑现。wiki 层沦为 raw source 的镜像仓库，而非编译后的知识层。

**根因**：`kdo ingest` 或 `kdo enrich` 未实际执行三步编译法；或 enrich 命令存在功能缺陷（老顽童评估亦指出 "enrich 无 LLM 失效"）。

---

### 2.2 Artifact 空壳率过高，元数据与实质内容严重失真

**证据**（来自 `fb_20260501_2ec33be4-artifact-validation.md`）：

| artifact_id | draft 字数 | TODO 残留 | validate 结果 |
|-------------|-----------|-----------|---------------|
| `art_20260427_16a7c4d7` | 0 | 无 | **FAIL** (draft missing) |
| `art_20260430_cd02f27c` | 6 | **有** | **FAIL** |
| `art_20260430_a947d7a5` | 6 | **有** | **FAIL** |
| `art_20260501_cc0af2d7` | 6 | **有** | **FAIL** |
| `art_20260430_447f2eea` | 19 | 无 | PASS (warn: 短) |
| 3 个 builtin skill | 完整 | 无 | PASS |

**影响**：10 个 artifact 中 4 个为实质性空壳，却被标记为 `ready` 或 `draft`，误导 ship 决策。有 3 个 artifact 已 ship 到 local，但 ship 时并未通过 validate。

**根因**：没有 enrich 的 wiki 作为原料，Delivery Producer 只能生成模板；ship 流程未严格执行 validate 拦截。

---

### 2.3 20_memory/ 完全废弃，跨会话连续性归零

**证据**：
- `project-continuity.md` 仅有一句占位符
- `user-preferences.md`、`corrections.md`、`operating-principles.md` 均为 3~4 行空壳
- `cli-preferences.json` 仅含 target_user 和 channel

**影响**：每次新会话的 AI agent 都是"失忆"状态，需人类重复交代上下文，违背 KDO "跨会话连续性"设计目标。

---

## 三、结构性缺陷（P1）

### 3.1 断链泛滥 — 知识图谱"伪连通"

- Lint 报告 14 个 broken wikilink，全部集中在 Synthesis 章节
- `[[Multi-Agent Orchestration]]`、`[[SaaS定价策略]]`、`[[平台经济中的互补者困境]]` 等链接指向不存在的页面
- Graph RAG index 虽有 23 节点 28 边，但大量概念连接是"悬空"的

### 3.2 Improvement Plan 冗余积压

- 8 个 improvement-plan（`plan_20260501_e1e150b9` 至 `plan_20260501_97170532`）内容几乎完全相同
- 均指向同一批 3 个 failing artifact + 14 个 broken wikilink
- 无关闭/合并/去重机制，反馈闭环"只开不关"

### 3.3 contradictions.md 空置 — Arbiter 无工可做

- 零条目，仅标题行
- 12 个 source 跨医疗/SaaS/组织方法论/研究方法四大领域，必然存在张力（如 YC "去中层" vs 街顺 "百人客服重资产"）
- 矛盾发现机制未运行

---

## 四、质量与一致性（P2）

### 4.1 工具链不同步（源码 vs pip vs 脚本）

- 仓库中 `kdo_validate.py` 检查维度有限，但 CLI eval-results 显示有更细检查（`content_draft_length`、`content_thesis_filled` 等）
- `kdo_lint.py` legacy 日期格式（`+00:00`）仍触发 false positive
- 老顽童评估已指出 "源码与 pip 版本不同步" 为反复出现的问题

### 4.2 Quality Gates 文档与代码未对齐

- `90_control/quality-gates/content.md` 仅 11 行，是 PROTOCOL.md 精简版
- `kdo_validate.py` 的具体 gate 逻辑未在文档中显式映射

### 4.3 source-registry.yaml / artifact-registry.yaml 状态未知

- PROTOCOL.md 和多 skill 引用这两个文件，但遍历中未确认其内容是否与 `.kdo/state.json` 同步

---

## 五、扩展性（P3）

### 5.1 Feedback 以模拟为主，缺乏真实世界输入

- 18 条 feedback 中 13 条 simulated、5 条 eval-results
- `60_feedback/comments/` 下无真实人类评论
- 系统尚未真正对外交付，反馈闭环在"自说自话"

### 5.2 Graph RAG 静态，无查询 API

- `index.json` 存在但 `kdo query` 实际使用 `search_documents()` 关键词搜索
- `SearchIndex` 向量语义搜索未接入（老顽童评估亦指出"两套搜索并存，实际只用一套"）

### 5.3 Context 加载成本高

- PROTOCOL.md 自身承认：AI 每次会话需重读 PROTOCOL.md + AGENTS.md + routing-rules.md
- `90_control/CONTEXT.md` 为静态快照，无自动化更新机制

---

## 六、亮点（应保留和发扬）

1. **协议层设计质量极高**：PROTOCOL.md、routing-rules.md v0.3（修正了角色混淆）、AGENTS.md、feedback-routing-rules.md、7 个 Schema 均达到生产级水准
2. **街顺概念卡片是三步编译法典范**：完整的 Condense / Critique / Synthesis / Open Questions / Output Opportunities
3. **3 个 builtin capability skill 全部通过 validate**：文档规范、边界清晰、eval cases 完整
4. **index.md 升级为知识图谱入口**：Mermaid 关系图、Dataview 查询、domain 分组方向正确
5. **老顽童评估机制**：存在外部评审（虽为模拟），表明系统有"第三方审计"意识
6. **iteration 报告机制**：`iter_20260502_585f1206` 记录了完整的 pipeline flow 和 metrics

---

## 七、核心判断

> **KDO 仓库当前处于 "Phase 1.5" 状态：协议与基础设施（Phase 1）已就绪，但知识编译与交付链路（Phase 0）尚未跑通。**
>
> 最紧迫的任务不是增加新功能（如 LLM 接口、更复杂的模板），而是：**让已有规则咬合真实数据**。
>
> 具体而言：把 0 个 enriched wiki 变成 12 个，把 8 个 failing artifact 变成 0 个，把空白的 20_memory/ 变成跨会话的连续性锚点。

---

## 八、参考文件

- `[[90_control/PROTOCOL.md]]`
- `[[90_control/routing-rules.md]]`
- `[[90_control/AGENTS.md]]`
- `[[30_wiki/log.md]]`
- `[[30_wiki/index.md]]`
- `[[90_control/iterations/2026-05-02-iter-001-kdo-反馈闭环建设---首次迭代.md]]`
- `[[60_feedback/assessments/老顽童对黄药师KDO改造的独立判断.md]]`
- `[[30_wiki/decisions/kdo-protocol-implementation-roadmap.md]]`
- `[[30_wiki/decisions/kdo-priority-checklist.md]]`

---

*评估完成时间：2026-05-03*  
*评估协议版本：KDO Protocol v0.1*
