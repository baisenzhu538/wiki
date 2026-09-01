---
id: task_20260902_skills-assistant-legacy53-evaluate-revive
title: 根目录 legacy skill 处置——评估→上架/重造/报废三分法（健康度建议书动作7·老朱0902拍板升级版）
seq: 599
status: reviewed
assignee: skills-assistant
created_by: wangyuyan
created_at: 2026-09-02
reviewed_by: 欧阳锋
review_date: '2026-09-01'
grade: A-
decision_source: 老朱 2026-09-02 拍板：「能用的搬回正规货架登记好；认为没用的拉起skills助理评估——全网调研作为工作流重造一轮，看是否达标，确实没必要再放弃」
reviewer: 欧阳锋
instance: skills-assistant
updated_at: '2026-09-01T17:05:18.246302+00:00'
evidence: 60_feedback/diagnosis/建议书_20260902_legacy53_评估与重造方案.md
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

## 执行报告（2026-09-02 Skills 助理）

**交付物**：`60_feedback/diagnosis/建议书_20260902_legacy53_评估与重造方案.md`（23.5KB，逐目录裁决表 54 项全覆盖 + 三批立项建议 + 待议事项 4 条）；任务单本报告（随单留痕）。

**完成内容**：Phase 1 只读评估全部完成——实际盘点 54 个游离 skill 目录（任务单口径 53，以实际为准），逐个完成基础盘点（manifest/内容质量/mtime/shared 撞车/域归属）与三分裁决：迁 shared/ 27 项、重造 6 项（crystallized-* 8 草稿合成 1 项）、报废建议 9 项（零执行）＋ builtin 四件套转议题。54 项全覆盖脚本验证 0 遗漏 0 重复。

**验证**（实测输出）：
- 54 目录全覆盖脚本校验：covered=54/actual=54，missing=[] extra=[] dup=[]
- 撞车判断 diff 实证 4 对：self-evolution / knowledge-collision-workflow（仅 frontmatter 状态差异，同源已登记）、nine-layer-business-dig（shared 版 71 行精简 vs 根目录 307 行完整）、business-research（shared 已薄壳化 1.1.0，内容并入 research-core）
- 重造评估全网调研每条结论 ≥2 独立来源：Anthropic 官方 Agent Skills 文章（equipping-agents，2025-10-16）+ agentskills.io spec + anthropics/skills README + GitHub 生态 6 源（Toonflow 15k★/CogVideo 12.9k★/HunyuanVideo-1.5 4.5k★/Docling/Coqui TTS/marqo）
- 引用统计：grep -rl 全库扫描（business-research 221、dual-triangle-oral-spray 104、openmontage-video 107、self-evolution 101、cangjie-skill 33 等）
- 队列流转：claim --force（前方 #596 pending_review 阻塞，任务单明确 Phase1 只读可立即跑，force 例外已留痕 90_control/force-exceptions.log）→ complete 成功

**边界**：
- Phase 1 全程只读：未搬文件、未改任何 skill frontmatter、未删任何内容、未贴标签
- 报废批零执行：9 项仅为建议，须王语嫣复核后才落 legacy 标记
- 撞车判断以 grep/diff 库内实证为准；「最后修改时间」因 2026-08-31 批量同步参考价值有限，未作为裁决主依据
- web_search 后端（DuckDuckGo）本会话不可用，全网调研改用 curl 直抓权威页面 + GitHub API 实证，均落 /tmp/research599/ 留证

**需要谁动作**：
- 欧阳锋：终审建议书（P1-P3 门禁：pre-submit 0 ERROR、路由面自检、五字段提审）
- 王语嫣：编排 Phase 2 立项（迁移批 27 项 + 重造批 6 项，#597 收口后错峰）；复核报废批 9 项；裁定待议 4 条（builtin 登记规则/九字诀口喷去重/design 域挂载/多模态解析层整合）
- 黄药师：重造批 R1/R3 审核（crystallized 结晶证据补全、lib-maintainer 引擎接入）；builtin 登记规则裁定参与

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 1 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）

## 终审记录（2026-09-02 欧阳锋）

**Verdict: PASS / Grade: A-**

审的是建议书本身质量（编排层复核意见不在我审裁范围，不推翻）。

**三项审查独立复核（全部亲跑，非采信 self-report）：**

| 审查点 | 验证方法 | 结果 |
|:--|:--|:--|
| ① 54 全覆盖 0 遗漏 0 重复 | 终审者独立清点 `ls -d */ | grep -v shared` = 54 个目录，逐一映射裁决表 | A 27 目录 + B 14 目录（crystallized-* 8 + openmontage + lib-maintainer + distill-own + audio-production + document-parsing + image-understanding-pipeline）+ C 9 目录 + builtin 4 = 54，0 遗漏 0 重复 ✅ |
| ② 撞车/报废判断有 grep/diff 实证 | 抽验 4 对撞车声明中的 3 对 + 行数/manifest/待填声明 | business-research：shared/research/SKILL.md=32 行 1.1.0 薄壳（frontmatter 实读「已并入 research-core，本卡为兼容薄壳」）vs 根目录 99 行完整版——声明吻合；knowledge-collision diff=17 行、self-evolution diff=12 行，均仅 frontmatter 状态/description 前缀差异——「100% 同源」判断成立；nine-layer 307 vs 71 行行数声明精确吻合；manifest 仅 3 个独立复点吻合；crystallized-* 37 行「待填」grep 命中 ✅ |
| ③ 红线遵守（Phase 1 只读） | git log 全量提交链 + git status | #599 提交链 4 笔（b8109ba30 立项/c4b3cb653 claim/3942c7f5b 建议书/304033e36 complete）触碰面=任务单+建议书+队列/dashboard 流转文件；skills 区非 shared 改动仅 3 个生成物（INDEX/MOUNT-MATRIX diff=各 2 行纯时间戳刷新属 #595 重扫残留、SKILL-HEALTH 属 #598），54 个 legacy 目录 git status 零触碰 ✅ |

**建议书质量加分项**：口径诚实（主动报「任务单 53 实际 54 以实际为准」）；裁决理由全部带 grep/diff 实证而非印象；重造评估全网调研每条 ≥2 独立来源且留证 /tmp/research599/；待议事项 4 条主动识别不越界（builtin 登记规则/九字诀去重/design 挂载/多模态解析整合）；分批方案含挂载建议+优先级+错峰时序。

**🟡 记档 1 项（带落点）**：建议书盘点方法表声明引用统计含 90_control，但报废 C-40（image-ocr-easyocr）漏检了 90_control/AGENTS.md 图片纪律段的首选路径引用——该断链风险由王语嫣编排层复核兜住（3 项缓报废+R6 先行时序），零实际损害。落点：不降级主体质量（被复核层兜住+报废批本有「复核后才落标」双保险）；此教训（引用统计须含 AGENTS.md 等基建声明文件）建议 skills-assistant 记入家法盘点清单，下批评估单执行。

**存在性核查**：①「54 个目录」核查=终审者亲跑 ls 独立清点输出 54 行（清单留存会话）；②「薄壳化」核查=head shared/research/SKILL.md 亲读 frontmatter version: 1.1.0+标题「本卡为兼容薄壳」；③「仅 frontmatter 差异」核查=diff 两对文件输出 17/12 行且逐行为 frontmatter/description；④「legacy 零触碰」核查=git status --porcelain 40_outputs/capabilities/skills/ 非 shared 计数=3（全为 #588/#598 生成物）+54 目录名逐一不在任何 #599 提交的 name-only 清单。
