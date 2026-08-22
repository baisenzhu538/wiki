---
id: 428
assignee: hermes
status: pending_review
updated_at: '2026-08-22T14:38:38.488676+00:00'
---
# #428 补建 agent-spec 卡：风清扬（观察者）

- **任务号**：#428
- **状态**：pending_review（2026-08-22 已提审）
- **assignee**：laowantong（制卡；王语嫣编排；欧阳锋终审）
- **优先级**：P2（其余 4 角色均有 spec 卡，观察者独缺；B2-3 角色专场前补齐）
- **立项**：2026-08-22 王语嫣（风清扬五角色建议书裁定采纳项）

## 任务目标

新建 `30_wiki/agent-specs/agent-spec-fengqingyang-observer.md`，内容底本=`60_feedback/diagnosis/diag_20260822_fengqingyang-5role-spec-workflow.md` §角色 5（特性/规范/工作流/Trigger/Interface 五要素齐全，不新造）。

## 口径（以拍板为准，建议书只是底本）

- 职责按 B2-2 入宪三条：①审计与建议书**只交王语嫣** ②记忆维护（时间/记忆胶囊及摘要洞察，不直接产 KB 卡）③Agent 部署（飞书等平台）+自身迭代
- 边界：不产卡、不终审、不流转队列；与段王爷（内容经销商）零重叠
- 写入全厂通用规范两条（老朱 08-22 补充）：G1 每日自进化（daily-context 落盘+长期资产 commit 为准）/ G2 洞察第一时间上浮（报王语嫣裁定，不口头带过）

## 验收

- 五要素齐全（内核/职责/边界/工作流/Trigger+Interface）+ G1/G2 两铁律
- pre-submit 0 ERROR；双向回链（链 B2-2 拍板所在 decisions.md 与记忆胶囊四层方案）
- 欧阳锋终审；commit 入档（E040）

---

## 提审记录（2026-08-22 老顽童）

产出物：`30_wiki/agent-specs/agent-spec-fengqingyang-observer.md`（95 行，五要素 + G1/G2 + 双向回链 source_refs 4 条）

**pre-submit 输出（kdo pre-submit -f 30_wiki/agent-specs/agent-spec-fengqingyang-observer.md）：**

```
Files checked: 1 | Passed: 1 | Failed: 0
[YAML]: 0 issues
[WIKILINK]: 0 issues
[DOMAIN]: 0 issues
[DK_SECTION]: 0 issues
[OUTLINK]: 0 issues
[ALIASES]: 0 issues
[POSITION_DECLARATION]: 0 issues
[SOURCE_REACHABILITY]: 0 issues
[QUALITY_SCORE]: 1 info
  Quality pre-score: 75/100 | pos:25 | tacit:0 (no section) | src:25 (4) | decomp:25 (7)
✅ Result: PASS — 一次通过！
```

- 门禁修复过程：初次 FAIL 因检索索引新鲜度门禁（卡片 22:21 更新 > .kdo/search_index.json 21:54）→ 跑 `kdo index --incremental` 刷新（+1）→ 复跑 PASS
- 索引已刷新，kdo query 可检索到本卡
