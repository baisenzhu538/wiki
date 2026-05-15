# Content Quality Gate

A content artifact is ready for ship when ALL of the following pass:

## P0 — 阻塞发布

- [ ] **source_refs 不为空**：每篇内容必须至少引用一个源文件（`src_xxx`）或 wiki 页面
- [ ] **Core Thesis 可验证**：不是模糊观察，而是一个可被证伪的断言
- [ ] **enrich 已完成**：引用的 wiki 页面 status 必须为 `enriched` 或 `reviewed`。`draft` 状态的页面禁止 produce
- [ ] **target_user 明确**：不说"通用"，不说"所有人"
- [ ] **ACTION 锚点**：至少一个读者今晚能执行的动作——5 分钟内可启动、有成功指标。禁止"分享这篇文章""关注我们"等无行为改变的 CTA

## P1 — 发布前修复

- [ ] **Key Findings 含引用**：每条 finding 至少有一个 `src_` 或 `wiki_ref`
- [ ] **500-3000 字**：article 类型在此范围内
- [ ] **Source Lineage 表完整**：所有引用的源文件 trust_level 已标注
- [ ] **Burn line**（可选，framework 卡推荐）：一句话烧到骨髓，牺牲精确换可记忆

## P2 — 建议改进

- [ ] **跨 wiki 链接**：与至少一篇其他 wiki 页面建立关联（Synthesis 段落）
- [ ] **feedback_path 已声明**：读者知道去哪里给反馈
- [ ] **domain 字段已设置**：内容归属的领域标签完整
- [ ] **EVIDENCE 审计**（可选，重要论述推荐）：至少标注一条论据的偏差（选择性举证/作者偏向/简化），引用一个真实外部批评

## 禁止事项（参考 failure-modes.md）

| 禁止 | 原因 | 失败模式 |
|------|------|:--------:|
| 禁止对 draft 状态的 wiki 页面 produce | 骨架内容无实质信息 | F-KDO-001 |
| 禁止 source_refs 为空就发布 | 无法追溯信息来源 | — |
| 禁止 trust_level=low 的内容不经人工审查发布 | 信源不可靠 | — |
| 禁止 CTA 为"分享/关注/点赞"等无行为改变动作 | 知识未转化为行为 | F-KDO-016 |
