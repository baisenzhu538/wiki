---
title: "Sprint 6：修复 KDO 数据流转的四个断裂点（黄药师）"
assigned_to: "黄药师（Builder）"
priority: "P0"
created_at: "2026-06-02"
reviewer: "欧阳锋（Architect）"
status: "pending"
depends_on: []
blocks: []
origin: "art_20260602_kdo_data_autopsy_huangyaoshi — 四个死刑"
related:
  - plan_20260531_data-curator-v1.3
  - labeling-final-consolidation
  - sprint-20260531-retrospective
---

# Sprint 6：修复 KDO 数据流转的四个断裂点

> **背景**：黄药师用 Truman 五层模型反照 KDO 后，发现六步管线两步活着、两步残废、两步死亡。四个断裂点全部是"已有零件没装上"——不是重新设计架构。
> **估时**：~11h
> **原则**：每修复一个断裂点 → 跑全量 pytest → 通知欧阳锋抽检。不跳过 C-10 单卡验证。

---

## 断裂点 1：enrich 管线缺少精加工（L2 残废 → 修复）

**现状**：`kdo enrich` 只做粗加工（洗菜：读TODO→填文本），不做精加工（切块装盘：chunk 级标引 + 多维标签）。424 张卡全部 `enriched` 但没有任何一张跑过 `kdo label`。

**目标**：`kdo enrich --all` 完成后自动触发 `kdo label`（对 enriched 的卡逐张标注 chunk_type / method_family / audience / perspective / confidence / platform / expiry / prerequisite_knowledge / usage_depth 9 维标签）。

**技术方案**：
1. `kdo enrich` 新增 `--auto-label` 参数（默认开启）
2. enrich 完成后调 `auto_label_chunk()` → 写入 `60_feedback/data-quality/label-results/{card_id}-labels.json`
3. 卡片 frontmatter 新增 `label_version` 字段，记录标注时使用的 tag-registry 版本
4. 标注结果暂不回写卡片正文（先写 JSON，待欧阳锋确认准确率后再回写）

**验收**：
- `kdo enrich --wiki-path master-decision-hygiene` → `label-results/master-decision-hygiene-labels.json` 存在且含 9 维标签
- `kdo validate --card master-decision-hygiene` 无新增 WARN
- 不破坏现有 388 tests

**估时**：~2h

---

## 断裂点 2：ingest 缺少预判步骤（ADUCIT 的 A 为空 → 修复）

**现状**：424 张卡没有一张在入库前被问过"AI 未来怎么用"。`value_tier` / `expected_usage_frequency` / `uniqueness` / `expiry` 字段全部缺失。

**目标**：`kdo ingest` 完成后弹出 Truman 三问，引导用户/Agent 做价值预判，预填 frontmatter。

**技术方案**：
1. `kdo ingest` 新增 `--assess` 参数（默认开启）
2. ingest 完成后输出三个问题：
   - 这张卡属于微观（教材）/ 中观（燃料）/ 宏观（护城河）？
   - 预期使用频率？独特性？保质期？
   - ROI 是否为正？
3. 答案写入 frontmatter 的 `value_tier` / `uniqueness` / `expiry` 字段
4. 支持 `--assess-skip` 跳过（批量 ingest 时用）
5. 对已有卡片，新增 `kdo assess --card <id>` 单独补预判

**验收**：
- `kdo ingest --assess` → 交互式弹出三问 → 写入 frontmatter
- `kdo assess --card master-decision-hygiene` → 单独补预判
- `kdo validate --v15` 能检测 `value_tier` 缺失 → 报 WARN
- ≥3 new tests

**估时**：~2h

---

## 断裂点 3：feedback 只记录不回流（L5 闭环断裂 → 修复）

**现状**：`kdo feedback` 只写 Markdown 文件，从来不触发 enrich。60_feedback/auto/ 曾有 1770 个自动反馈，没有一条触发过重新标注或 enrich。

**目标**：`kdo feedback` 新增 `--auto-enrich` 模式，当反馈类型为 `corrections` 或 `eval-results` 时，自动触发对应卡片的重新 enrich 或 label。

**技术方案**：
1. `kdo feedback --auto-enrich` → 解析反馈内容 → 匹配 artifact_id / card_id → 触发对应操作
2. 反馈类型路由：
   - `corrections: label` → `kdo label --card <id>` 重新标注
   - `corrections: content` → `kdo enrich --wiki-path <path>`
   - `eval-results: accuracy` → 更新 `benchmark-results.md` + 通知
3. 24h 冷却期防抖（同卡片同类型反馈不重复触发）
4. 30 天自动清理已处理的反馈文件

**验收**：
- `kdo feedback --kind corrections --artifact-id <id> --auto-enrich` → 触发重新 enrich
- 冷却期内重复反馈不重复触发
- `60_feedback/auto/` 文件数不增长
- ≥3 new tests

**估时**：~3h

---

## 断裂点 4：ship 之后没有 Agent 消费层（L4 死亡 → 激活）

**现状**：`kdo ship` 只写 YAML delivery record。shipp 之后的文章/卡片不进入任何 Agent 的工作上下文。知识资产是一次性消耗品。

**目标**：`kdo ship` 完成后，将产出物路径写入 Agent 共享上下文文件，供下游 Agent 加载。

**技术方案**：
1. 新增 `.kdo/agent_context.json` 作为 Agent 共享状态文件
2. `kdo ship` 完成后自动追加：
   ```json
   {"artifact_id": "...", "path": "...", "labels": [...], "shipped_at": "...", "consumed_by": []}
   ```
3. 各 Agent（老顽童/洪七公/段王爷）启动时读取 `agent_context.json`，加载最新 ship 的上下文
4. Agent 消费后标记 `consumed_by: ["hermes-producer"]`

**验收**：
- `kdo ship <artifact>` → `.kdo/agent_context.json` 含新条目
- Agent 启动脚本能读取并加载上下文
- 不破坏现有 ship 逻辑
- ≥2 new tests

**估时**：~4h

---

## 执行顺序

```
断裂点1（enrich + label 串联）  ← 最先。label 管线已就绪，只差一个触发。
    ↓
断裂点2（ingest 预判）          ← 其次。新卡片入库时补齐 A。
    ↓
断裂点3（feedback 回流）        ← 再次。让飞轮真正闭环。
    ↓
断裂点4（ship → Agent 消费）    ← 最后。依赖前三个断裂点修好后数据流才是完整的。
```

---

## 不做

- **不做** ADUCIT 的 D（识别）自动化——识别"隐藏的高价值数据"需要 LLM 辅助判断，当前 label 管线准确率足够但还没经过 Pilot 验证
- **不做** U（湖仓升仓决策）全自动化——inbox→wiki 的升仓规则需要人工判断，先保持手动
- **不做** Truman 三层工序的"注入灵魂"（萃取指南）——这依赖暗知识萃取管线先跑通

---

## 完成标志

| # | 断裂点 | 验收 |
|:--:|------|------|
| 1 | enrich + label 串联 | `kdo enrich --auto-label` 产出 9 维标签 JSON |
| 2 | ingest 预判 | `kdo ingest --assess` 弹出三问 + 写入 frontmatter |
| 3 | feedback 回流 | `kdo feedback --auto-enrich` 触发重新 enrich/label |
| 4 | ship → Agent 消费 | `.kdo/agent_context.json` 存在 + Agent 能读取 |
| **总** | pytest | ≥ 395 passed, 0 regression |

---

*黄药师 · 2026-06-02 · 待欧阳锋审查*
