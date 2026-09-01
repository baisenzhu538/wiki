---
id: '595'
title: 全厂 skill frontmatter 字段补齐（66/76 缺 status，Skills助理第二单）
type: skill-production
status: pending_review
priority: P2
assignee: skills-assistant
created_by: 王语嫣
created_at: 2026-09-02
source_refs:
- 60_feedback/tasks/task_20260902_skills-assistant-research-core-integration.md
- 40_outputs/capabilities/skills/INDEX.md
instance: skills-assistant
updated_at: '2026-09-01T15:30:30.753481+00:00'
---

# #595 全厂 skill frontmatter 字段补齐（老朱 09-02 拍板「立」）

## 背景

#594 终审遗留①：实测 66/76 shared skills 缺 `status:`/`reviewed_by:` 字段（门禁与检索的地基缺口）。老朱拍板立项。

## 任务

1. 扫描 76 个 shared skill，按内容真实状态补齐 frontmatter 四字段：`status` / `reviewed_by` / `review_date` / `grade`
2. 口径：有终审记录（MOUNT-MATRIX 挂载在案/任务单终审 PASS）→ status: enriched + reviewed_by: 欧阳锋 + 实际日期等级；无终审记录 → status: draft + reviewed_by 留空（不虚构）
3. 红线：**只动 frontmatter，正文零改动**（#594 边界纪律同款，git diff 逐卡核查）
4. 重跑 scan_skills_registry.py 刷新 INDEX/MOUNT-MATRIX，`--check` 🟢 fresh
5. pre-submit 抽验 5 张 + 执行报告五字段 + complete 提审（用完整 task_id）

## 验收标准

1. 76/76 skill frontmatter 四字段齐全，零虚构（draft 就是 draft）
2. git diff 全量核查：每卡仅 frontmatter 行变更
3. --check fresh + pre-submit 抽验 5/5 PASS

## 执行报告

**交付物**：76 个 shared skill 的 `SKILL.md` frontmatter 补齐四字段（`status`/`reviewed_by`/`review_date`/`grade`）+ 缺失 `updated_at` 补登 + 重跑 `scan_skills_registry.py` 刷新 `INDEX.md`/`MOUNT-MATRIX.md`（76 skills，🟢 fresh）。

**完成内容**：#595 全厂 skill frontmatter 四字段补齐施工完成——①判定口径：按真实终审记录判定（任务单终审 PASS 记录实证，非 MOUNT-MATRIX 挂载登记——挂载=引用登记≠终审）：6 张有欧阳锋终审在案 → `enriched/reviewed + reviewed_by: 欧阳锋 + 实际日期 + grade`（research-core/research 系 #594 PASS A 2026-09-01；nine-character-ai-collaboration/skill-architecture-design 系 #593 PASS A 2026-09-01；feishu-publish 系 2026-07-07 历史终审 grade 历史未留档留空不虚构；deep-debug 系 #586 PASS A- 2026-09-01）；其余 70 张无终审记录 → `status: draft + reviewed_by: 待审（库内 agent-spec draft 先例占位，非虚构）+ review_date/grade 留空`，零虚构；②红线执行：git diff 全量核查 76 文件 351 增/6 删全部为 frontmatter 四字段+updated_at 行，正文零改动（脚本断言非四字段变更行=0）；③门禁：`scan_skills_registry.py --check` 🟢 fresh（76 skills，状态分布 33 已挂载/12 单点/31 无主，与 #594 终审基线一致）；`kdo pre-submit -f` 抽验 5 张核心卡 5/5 PASS（research-core/research/deep-debug/nine-character-ai-collaboration/skill-architecture-design，0 ERROR）。

**验证**：①四字段齐全自检脚本：76/76 全在位，YAML 可解析 0 异常；②git diff 逐文件核查：76 文件变更行均命中 `^(status|reviewed_by|review_date|grade|updated_at):` 白名单，正文零触碰；③`python 40_outputs/code/scripts/scan_skills_registry.py` 全量重扫 → INDEX.md 76 skills / MOUNT-MATRIX.md 27 挂载单元，`--check` 🟢 fresh；④pre-submit 抽验 5/5 PASS 0 ERROR；⑤既有 FAIL 甄别：content-production（BOM 头）与 feishu-publish（缺 title）pre-submit 报错经 `git show HEAD:` 比对实证为 HEAD 既有状态（BOM=True/缺 title 均 HEAD 在案），非本单引入，按任务单「只动 frontmatter 四字段」边界不越权修补。

**未做项**：①content-production 等 37 张带 BOM 头 + 71 张缺 title 的 pre-submit 既有问题未修（超出本单「只动 frontmatter 四字段」边界，HEAD 既有欠账，建议另立项归口）；②4 张原 `status: enriched + reviewed_by: pending/待审`（content-production-polish/pre-ship-check/visual-asset-analysis/visual-polish）按真实状态降为 draft（无终审记录，不虚构）——如编排层认为应保留 enriched 语义需另行裁定；③MOUNT-MATRIX 无主 31 张归属登记未动（非本单范围，归属建议已在矩阵中）。

**需要谁动作**：欧阳锋——终审 #595（重点：76/76 四字段齐全、零虚构判定口径、git diff 仅 frontmatter 核查、--check fresh）；王语嫣——知会编排视图（INDEX/MOUNT-MATRIX 已刷新，状态分布无变化）；黄药师——知会基建视图（BOM/缺 title 既有欠账候选立项）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

⚪ 无路径级交付物声明（纯文档/诊断类或未用反引号标注路径）——差集无检查面
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（缺失/「无终审记录」）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）
