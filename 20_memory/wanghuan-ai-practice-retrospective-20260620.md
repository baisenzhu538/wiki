# 复盘：王欢 AI 实践心法卡片化项目

**时间**：2026-06-19 ~ 2026-06-20  
**执行角色**：老顽童（主产）+ 欧阳锋（审）  
**项目目标**：把 `00_inbox/王欢AI实践心法` 的授课素材系统化地沉淀为 KDO 卡片库

---

## 1. 最终产出

### 卡片规模

- **王欢相关卡总数**：28 张
- **状态分布**：`enriched` 22 张，`draft` 6 张
- **类型分布**：
  - framework：10 张
  - dark-knowledge：7 张
  - concept：5 张
  - case：4 张
  - tool：2 张

### 关键卡片

| 类型 | 代表卡片 |
|:---|:---|
| 框架 | `framework-wanghuan-actor-director-mode`、`framework-wanghuan-ai-five-level-ladder`、`framework-wanghuan-harness-seven-stages`、`framework-wanghuan-five-criteria-first-product` |
| 暗知识 | `dk-wanghuan-magic-defeats-magic`、`dk-wanghuan-spec-trap`、`dk-wanghuan-paced-sales-decision` |
| 概念 | `concept-wanghuan-power-of-standards`、`concept-wanghuan-tacit-knowledge-examples`、`concept-wanghuan-ai-native-definition` |
| 案例 | `case-wanghuan-education-sales-paced`、`case-wanghuan-education-sales-capability-extraction`、`case-wanghuan-yiyu-qingji-medical-notes` |
| 工具 | `tool-wanghuan-ai-business-profile`、`tool-wanghuan-ai-dual-role-coach` |

### 素材归档

- 18 个原始文件（逐字稿、口述、笔记、15 张图 OCR + VLM 描述）已归档到 `10_raw/sources/`
- 全部在 `.kdo/source_id_map.json` 注册
- 12 张既有王欢 draft 卡的 `source_refs` 已从 `00_inbox/` 迁移到 `10_raw/sources/`

---

## 2. 质量门禁

**最终状态**：

```text
total=1304, p0=0, p1=12, clean=1292, yaml_error=0
```

- **P0 已清零**：顺手修复了 2 张 `yt-*` 卡的 YAML 解析错误。
- **P1 剩余 12 张**：其中 11 张是 `yt-*` 卡片的 `trust_level=high` 但单 source / dangling 链接问题；1 张是王欢旧 draft `dk-wanghuan-ai-lifts-personal-ceiling.md`（source 未注册 + trust_level 不匹配）。
- **王欢本次新增/深化的卡片全部干净**。

---

## 3. 做得好的地方

1. **OCR 预解析前置**  
   在王语嫣正式入库标记前，先用 RapidOCR 把 16 张示意图转写成可搜索文本，为后续批量生产提供了可审计、可引用的 source。

2. **source 先归档、后引用**  
   没有把 `00_inbox/` 路径直接写入 enriched 卡，而是统一复制到 `10_raw/sources/` 并注册，符合 KDO 长期可审计要求。

3. **批量 enrichment 效率较高**  
   用 AgentSwarm 把 9 张既有王欢 draft 卡和 7 张新建框架/案例/工具卡并行处理，在较短时间内完成了大量结构化工作。

4. **深挖暗知识与案例联动**  
   不止于框架罗列，还从 Q&A 中挖出了 `dk-wanghuan-magic-defeats-magic`、`dk-wanghuan-spec-trap` 等反直觉暗知识，并把招聘/招投标例子沉淀为 `concept-wanghuan-tacit-knowledge-examples`。

5. **九层/深度结构统一**  
   所有 enriched 卡统一包含：用一句话讲清楚、核心要点、边界表、失败模式表、行动 Checklist、相关卡互链、Critique（外部攻击者 + 不要用）、Synthesis、diagnostic_signals。

---

## 4. 踩过的坑

### 4.1 AgentSwarm 并发覆盖问题

**现象**：第二批 AgentSwarm 的 3 个任务都完成了，但事后发现 `dk-wanghuan-magic-defeats-magic.md` 和 `dk-wanghuan-spec-trap.md` 被还原成了旧 draft。

**根因**：第二批 AgentSwarm 的 prompt 没有使用 `{{item}}` 来限定每个 subagent 只处理一个目标，导致 3 个 subagent 都执行了全部 3 个任务。并发写入同一文件时，后完成的 agent 覆盖了之前的内容。

**修复**：
- 重新用 `Write` 写回两张 dk 卡的 enriched 版本。
- 后续使用 AgentSwarm 时，prompt 必须用 `{{item}}` 限定单任务范围，或改用单个 agent 串行处理。

### 4.2 旧 draft 与新 enriched 卡同名冲突

王欢系列里已经有 6 张 dark-knowledge 旧 draft（如 `dk-wanghuan-ai-lifts-personal-ceiling.md`），它们与新需求中的卡片名称部分重叠，但内容深度、source_refs、frontmatter 都不达标。如果不先清理，容易误判状态。

### 4.3 `related` 字段里的非卡片链接

部分早期生成的王欢卡片在 `related` 中放了类似 `[[human-ai-collaboration-double-triangle]]` 这样的 domain 名称，实际对应的是 `30_wiki/domains/` 下的文件，不是单张卡片，可能成为 dangling 链接隐患。

---

## 5. 关键决策

1. **reviewed_by 统一用欧阳锋**  
   王欢卡片的 author 为王语嫣/老顽童，按规则由欧阳锋审核。

2. **教育机构销售拆成两张 case 卡**  
   一张聚焦 PACED 决策链（`case-wanghuan-education-sales-paced`），一张聚焦完整的销冠能力萃取系统（`case-wanghuan-education-sales-capability-extraction`），避免单张卡信息过载。

3. **暗规则既建 concept 也回注工具**  
   `concept-wanghuan-tacit-knowledge-examples` 作为独立概念卡存在，同时在 `tool-wanghuan-ai-business-profile` 的"行业暗规则"字段和模板中引用，保证抽象与落地兼顾。

4. **yt 卡片的 P1 暂时不动**  
   剩余 P1 问题全部属于 `yt-*` 系列（trust_level/source 不匹配、dangling 链接），与王欢项目无关，未在本次处理。

---

## 6. 下一步建议

### 高优先级

1. **处理 5 张剩余王欢旧 draft dk 卡**
   - `dk-wanghuan-ai-lifts-personal-ceiling.md`
   - `dk-wanghuan-creativity-in-description-and-taste.md`
   - `dk-wanghuan-output-equals-standard-times-iteration.md`
   - `dk-wanghuan-standard-by-iteration.md`
   - `dk-wanghuan-ai-lifts-personal-ceiling.md`
   
   决策：要么 enrich 后并入现有体系，要么降级为 `draft`/`archive`，避免拖住全库 P1。

2. **修复 `dk-wanghuan-ai-lifts-personal-ceiling.md` 的 P1**
   - `trust_level` 与单 source 不匹配
   - `source_refs` 中使用了未注册的 `src_20260618_wanghuan`

3. **统一检查王欢卡片的 `related`**
   - 把指向 domain 的链接改成具体卡片，或移除。
   - 确保没有 dangling 链接。

### 中优先级

4. **做一张王欢 AI 实践心法的 domain digest 或索引卡**  
   28 张卡已经够多，需要一张顶层导航卡或 domain digest，把 actor-director、五层跃迁、 harness、飞轮、PACED/PECED、暗知识、案例串成一张地图。

5. **把最精炼的框架做成可复用模板**  
   例如 `framework-wanghuan-five-criteria-first-product` 的打分卡、`tool-wanghuan-ai-business-profile` 的 5 字段模板，可以落到 `90_control/templates/` 供后续直接使用。

### 低优先级 / 观察

6. **王欢内容是否进入视频/文章交付管道**  
   目前以卡片库形态沉淀，若段王爷/老顽童后续要做短视频或文章，可直接从现有 case/dk/framework 取材。

---

## 7. 核心 takeaway

王欢 AI 实践心法从"一 inbox 原始素材"到"28 张结构化卡片"的转化，验证了 KDO "素材 → source → 卡片 → 互链 → 暗知识" 的飞轮是可以跑通的。最大瓶颈不是内容本身，而是**并发 agent 写入冲突**和**旧 draft 与新 enriched 卡的同名混淆**。下一轮应优先清理 5 张旧 draft，把 P1 降到 0，再考虑做 domain digest 或对外交付。
