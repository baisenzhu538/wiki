---
id: task_20260902_skills-assistant-legacy53-evaluate-revive
title: 根目录 legacy skill 处置——评估→上架/重造/报废三分法（健康度建议书动作7·老朱0902拍板升级版）
seq: 599
status: in_progress
assignee: skills-assistant
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 老朱 2026-09-02 拍板：「能用的搬回正规货架登记好；认为没用的拉起skills助理评估——全网调研作为工作流重造一轮，看是否达标，确实没必要再放弃」
reviewer: 欧阳锋
instance: skills-assistant
updated_at: '2026-09-01T16:53:44.128307+00:00'
---

# #599 根目录 legacy skill 处置（评估→三分法）

## 背景

skill 健康度建议书（report-20260901-skill-health-audit）动作7：根目录 54 个游离 skill 目录（建议书口径 53 个，以实际盘点为准）不在 INDEX 登记面，Agent 检索不可见=白沉淀。老朱拍板：**能用的迁 shared/ 登记；疑似没用的不直接报废——先全网调研、按现行工作流标准重造评估一轮，能救活救活，确实没救才进报废清单**。

## 任务分两 Phase

### Phase 1（现在执行，只读+评估，不动任何文件）

对根目录每个 legacy skill 逐个盘点，产出处置建议表：

1. **基础盘点**：名称 / manifest 有无 / 内容质量 / 最后修改时间 / 与 shared/ 76 个是否撞车 / 域归属
2. **三分裁决**（每个 skill 一行结论+理由）：
   - **迁 shared/**：内容达标或小修可达标 → 给出迁移后落位路径+需补的 frontmatter/manifest 项
   - **重造**：主题有价值但现状不达标 → **全网调研该主题现行最佳实践**，对照本厂工作流标准（一卡一事/操作步骤可执行/失败模式表/Action Triggers/适用边界），给出「重造成本 vs 价值」判断；达标可行=给重造方案要点，立项建议
   - **报废**：主题过时/与 shared 重复无增量/无消费场景 → 给报废理由（这条只是建议，贴标签前须王语嫣复核，**Phase 1 零执行**）
3. **产出**：`60_feedback/diagnosis/建议书_20260902_legacy53_评估与重造方案.md`——逐个裁决表+分批立项建议（迁移批/重造批/报废批）
4. **验证要求**：重造评估的全网调研每条结论≥2 独立来源；「与 shared 撞车」判断须 grep 库内实证非印象

### Phase 2（物理搬移，本单不执行）

Phase 1 提审通过后，迁移批/重造批由王语嫣编排立项（**#597 收口后错峰执行**，防 INDEX/MOUNT-MATRIX 重生成撞车）；报废批王语嫣复核后才落 legacy 标记。

## 红线

- Phase 1 **只读**：不搬文件、不改 frontmatter、不删任何东西
- 报废零执行：只列清单+理由
- 全程遵守署名铁律（只写角色名）
- 完成后：队列流转（complete→提审）+ todos 留痕
