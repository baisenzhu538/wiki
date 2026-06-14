# 黄药师第一周任务（2026-06-15）

> 来源：30_wiki 全库深度审查阶段 0–6  
> 协调人：王语嫣  
> 优先级：P0 优先  
> 需要拍板的问题：见 `needs-user-decision-2026-06-15.md`

---

## 本周总目标

在本周内处理 **系统/决策/关系类的 P0 问题**，并建立 source 映射基础设施，让系统卡和决策卡的 P0 清零。

---

## 任务一：为 decision / proposal / system / improvement-plan 卡补充 source（1 人日）

### 需要你处理的卡片

所有 `status=enriched/reviewed/stable/active` 但 `source_refs` 为空或不足的 decision/proposal/system/improvement-plan 卡。

重点文件：

| 文件 | 当前问题 | 建议补充 |
|---|---|---|
| `decisions/kdo-priority-checklist.md` | source_refs 为空 | 补充触发该清单的会议/对话记录或相关任务文件 |
| `decisions/kdo-protocol-implementation-roadmap.md` | source_refs 为空 | 补充 protocol design session 的 source 或相关文档 |
| `decisions/proposal-kdo-flywheel-infrastructure.md` | source_refs 为空 | 补充触发飞轮讨论的反馈来源、相关 sprint 文档 |
| `decisions/proposal-deep-synthesis-infrastructure.md` | 正文已获欧阳锋批准，但 frontmatter 仍为 pending | 更新 reviewed_by、review_date、status，补充 source_refs |
| `decisions/sprint-6-cli-gap-proposal.md` | 正文已获欧阳锋确认，但 frontmatter 仍为 pending | 更新 reviewed_by、review_date、status，补充 source_refs |
| `systems/kdo-protocol.md` | source_refs 为空 | 补充协议设计会议记录或相关文档 |
| `systems/graph-rag-retrieval-layer.md` | type 字段曾被污染，source 缺失 | 确认 type 为 system/concept，补充 LightRAG 相关 source |
| `systems/obsidian-git-sync-protocol.md` | source_refs 为空 | 补充同步协议设计来源 |

### 执行标准

- 在 frontmatter 中补充 `source_refs`，指向具体会议记录、任务文件、对话记录或相关 wiki 页
- 如来源是会议/对话，可用 `source_context` 字段说明日期和参与者
- 对已批准的提案，更新 `reviewed_by` 为批准人、`review_date` 为批准日期、`status` 为 approved 或 reviewed

---

## 任务二：修复 master 域 contradicts 字段误用（0.5 人日）

### 问题

master 域大量 dark-knowledge 卡把 `contradicts` 用于"相关/纠正/补充"关系，污染知识图谱。

涉及卡片（部分）：

- `dark-knowledges/dk-f2-txt-ingest-skip.md`
- `dark-knowledges/dk-c1-cjk-regex-silent-fail.md`
- `dark-knowledges/dk-f6-cjk-skeleton-corruption.md`
- `dark-knowledges/dk-p2-tmux-cache.md`
- `dark-knowledges/dk-p4-batch-format-empty.md`
- `dark-knowledges/dk-p10-oral-ban.md`
- `dark-knowledges/dk-p13-token-burn.md`
- `dark-knowledges/dk-p17-accuracy-gap.md`
- `dark-knowledges/dk-p6-session-resume-fail.md`
- `dark-knowledges/dk-f14-accuracy-measurement-mismatch.md`
- `dark-knowledges/dk-modeling-counterexample-driven.md`

### 执行标准

1. 读取每张卡的 `contradicts` 字段
2. 判断实际关系：
   - 如果是"相关/引用/补充" → 移到 `related`
   - 如果是"纠正/更新" → 移到 `corrects`（如 schema 支持）或 `related` 并加说明
   - 如果确实有逻辑对立 → 保留 `contradicts`
3. 修改 frontmatter
4. 在王语嫣的看板中标记完成

### 需要拍板的问题

- 当前 schema 是否支持 `corrects` 字段？如不支持，是否新增？（王语嫣建议：先用 `related` 加注释说明关系，不新增字段）

---

## 任务三：处理 design 域 3 张高风险卡（0.5 人日）

### 目标卡片

| 文件 | 问题 | 建议动作 |
|---|---|---|
| `concepts/skill-月白-印刷DPI标准设置.md` | DPI 数值疑似与行业常识相反 | 复核数值，修正错误或加"待验证"标注 |
| `concepts/skill-月白-AI电商图人工过审处理.md` | 教授规避平台检测技巧 | 改写为"提升人工精修质感"，加风险提示 |
| `concepts/skill-月白-薅AIGC羊毛资源法.md` | 鼓励绕过平台付费机制 | 改写为"低成本试用/免费额度使用指南" |

### 执行标准

- 事实性错误：修正并补充来源
- 合规风险：改写表述，加显著风险提示
- 完成后更新 frontmatter 的 `confidence` 和 `trust_level`

### 需要拍板的问题

- `AI电商图人工过审处理` 是否保留？如保留，必须显著改写。（王语嫣建议：保留但改写为"AI 出图后人工精修指南"，删除"规避检测"相关内容）
- `薅AIGC羊毛资源法` 是否保留？（王语嫣建议：保留但改写为"AIGC 工具免费额度使用指南"）

---

## 任务四：建立 src_ID 映射索引（0.5 人日）

### 目标

建立 `src_YYYYMMDD_xxxxxxx → 10_raw/sources/...` 的映射脚本，让 `source_refs` 中的 ID 可以解析为实际文件路径。

### 交付物

- `90_control/scripts/source-id-registry.py`
- 输出：`60_feedback/audit/source-id-registry-2026-06-15.json` 或 `.md`

### 功能

1. 扫描 `10_raw/sources/` 下所有文件
2. 提取文件名中的 src_ID 或建立哈希映射
3. 输出 src_ID 到文件路径的索引
4. 可被其他脚本调用

---

## 任务五：维护门禁脚本（剩余时间）

### 目标

根据本周修复经验，增强 `kcard-quality-gate.py`：

1. 增加对 `reviewed_by=pending` 但正文含"批准/采纳"的检测
2. 增加对 `type` 字段污染的检测
3. 增加对 entity/project 卡 source 缺失的检测
4. 输出按 owner 分组的问题清单（方便王语嫣派任务）

---

## 本周交付物

1. decision/proposal/system 卡的 source 补充完成
2. master 域 contradicts 误用修复完成
3. design 域 3 张高风险卡处理完成
4. `source-id-registry.py` 脚本
5. 增强版 `kcard-quality-gate.py`
6. 更新后的问题看板状态

---

## 有问题找王语嫣

- source 找不到原始材料 → 王语嫣汇总给用户
- 与老顽童的工作有重叠 → 王语嫣协调
- 需要用户拍板 → 王语嫣汇总方案
- 脚本实现细节 → 可直接改，但告知王语嫣以便同步看板
