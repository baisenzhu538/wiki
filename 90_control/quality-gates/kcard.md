# KDO 卡片入库自检清单（KCard Quality Gate）

> 适用范围：`30_wiki/` 下的 concept / skill / case / framework / dark-knowledge / tool / decision / proposal / entity 等卡片
> 生效日期：2026-06-15
> 维护角色：王语嫣（QA）+ 欧阳锋（Architect）

---

## P0 — 阻塞入库

卡片必须满足以下全部条件，否则不得从 draft 进入 enriched/reviewed/stable：

- [ ] **id 存在且唯一**：与文件名一致，不含空格或特殊字符
- [ ] **title 非空**：能一句话概括卡片核心内容
- [ ] **type 正确**：卡片类型与正文结构匹配
  - `case`：有背景、事件、结果/数据、可迁移教训
  - `tool`：有使用步骤、边界条件、示例
  - `framework`：有适用范围、操作步骤、案例支撑
  - `concept`：有定义、区别、例子
  - `dark-knowledge`：有误区/后果/避免方法
  - `skill`：有练习方法、验收标准、示例
- [ ] **source_refs 不为空**：至少引用一个可追溯到原始材料的 source（`src_xxx` 或具体文件路径）
- [ ] **author 明确**：不为 `legacy` 或空
- [ ] **reviewed_by 明确**：不为 `pending`（进入 enriched 前必须有独立 reviewer）
- [ ] **status 与内容质量匹配**：
  - `draft`：骨架或待审内容
  - `enriched`：内容完整、来源清晰
  - `reviewed`：经独立 reviewer 确认
  - `stable`：经实践验证
- [ ] **confidence 已填**：0.0–1.0 之间，与来源数量和质量匹配
- [ ] **trust_level 已填**：`low` / `medium-low` / `medium` / `medium-high` / `high`，与验证状态匹配
- [ ] **domain 非空且符合规范**：按内容标注，不是按作者/来源标注（参见 `90_control/schemas/domain-annotation-standard.md`）
- [ ] **无 YAML 语法错误**：frontmatter 可被标准 YAML 解析器解析
- [ ] **无 dangling 链接**：正文 `[[...]]` 和 frontmatter `related` 指向的卡片存在

---

## P1 — 发布前修复

- [ ] **source 精确**：source_refs 包含行号/章节定位，而非仅 source ID
- [ ] **confidence / trust 一致**：
  - `trust_level=high` 至少需 2 个独立来源或实践验证
  - `confidence≥0.90` 至少需 2 个来源
  - `draft` 状态 confidence 不应 ≥0.85
- [ ] **卡片间关系清晰**：`related` / `contradicts` / `corrects` 等字段使用正确
  - `contradicts` 仅用于确有逻辑对立的卡片
  - 不得把“相关/纠正”标为 contradicts
- [ ] **无重复内容**：同一主题不与已有卡片高度重复
- [ ] **案例可验证**：case 卡有 outcome/数据/可验证结果，或明确标注为“教学示意案例”
- [ ] **术语统一**：与同一 domain 内其他卡片使用一致的术语
- [ ] **Open Questions 已处理**：enriched 状态的 concept 卡不应遗留大量未回答的 Open Questions

---

## P2 — 建议改进

- [ ] **跨卡片链接**：Synthesis 段落引用至少 1 个其他 wiki 页面
- [ ] **反馈路径**：卡片底部或 frontmatter 声明反馈方式
- [ ] **外部攻击 / Critique**：重要框架/概念卡包含反面视角或自我批判
- [ ] **Action Triggers**：工具/框架卡说明何时使用、何时不使用
- [ ] **视觉描述适度**：Visual Analysis 章节不超过必要长度，避免纯图像描述堆砌

---

## 特殊类型附加规则

### OCR 卡片

- [ ] **默认 trust_level = low**，直到人工校对完成
- [ ] **默认 confidence ≤ 0.6**，直到人工校对完成
- [ ] 校对后更新 `reviewed_by` 和 `status`

### Decision / Proposal / Improvement-Plan

- [ ] **source_refs 或 source_context 必须存在**：记录触发会议/对话/任务文件
- [ ] **状态与实际一致**：若正文已获批准，frontmatter 不得仍为 `reviewed_by: pending`
- [ ] **推测性内容标注 confidence**：设计草案/逆向分析应明确给出较低 confidence

### 课程衍生卡片

- [ ] **source 指向具体课程材料**：不得仅指向“课程地图精华串讲”等二手索引
- [ ] **内容去课程介绍化**：减少“本课程属于…配有选课口令”等 boilerplate

---

## 禁止事项

| 禁止 | 原因 | 对应失败模式 |
|------|------|:------------:|
| source_refs 为空就进入 enriched | 无法追溯来源 | F-KDO-014 |
| author = legacy | 无法追责 | — |
| reviewed_by = pending 但 status = reviewed/stable | 元数据造假 | — |
| OCR 卡默认 trust=medium | 误导用户引用低质量内容 | — |
| contradicts 字段用于非矛盾关系 | 污染知识图谱 | — |
| 同一主题重复建卡不互链 | 检索噪音 | — |
| confidence≥0.90 但 source<2 | 过度自信 | — |
