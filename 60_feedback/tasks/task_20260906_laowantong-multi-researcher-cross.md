---
id: task_20260906_laowantong-multi-researcher-cross
title: "场景复现一：多研究员交叉研究工作流（老朱拍板第一优先，A60-61 课程口径 KDO 化）"
seq: 664
status: pending_review
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 老朱 09-06 拍板第 4 项「多研究院交叉」；课程金矿 A60-A62+B93（楚门哈佛案例教学法研究）
reviewer: 欧阳锋
instance: laowantong
updated_at: '2026-09-06T09:23:09.688697+00:00'
evidence: 60_feedback/diagnosis/working/pilot-multi-researcher-cross-20260906.md
---

# #664 多研究员交叉研究工作流（老顽童）

## 目标（知行合一：能跑，不是卡）
把课程场景做成 KDO 可执行工作流：一个研究课题进来 → 拆 N 个不同立场/背景的研究员视角（A60：10 选 3-5）→ 分头调研 → 合并交叉 → 多视角总报告。

## 交付
1. **workflow 卡**：多研究员交叉研究流程（触发→分视角→任务书翻译→并行调研→合并裁决→报告）
2. **skill**：`multi-researcher-cross`（可执行版：任务书模板/研究员画像池/合并裁决规则——含 A62「不省 Token/信息传清楚」嘱咐）
3. **试金石**：用一个小课题真跑一遍（3 研究员视角），报告入工作流卡作案例

## 边界
- 研究员=同通道多实例（GLM 分工即可，不需多供应商）；"立场/背景不同"用提示词画像实现
- 与 kdo-self-attack（四路攻击）互补不重叠：交叉=多视角并行研究，攻击=对抗性验证

## 建模方案（L1 出牌，2026-09-06 老顽童）

[素材牌] 牌3·先口述稿再笔记 → 已逐字读 `00_inbox/AI大航海20260905/AI实战路径-五个层级全解析-口述.txt:358-410`（A60-A61 案例原文）+ `宣讲会…口述.txt:1040-1075`（B93）——不基于王语嫣台账二手摘要写卡
→ [边界牌] 牌6·先查已有卡再新建 → 存在性核查（三条锚）：①`40_outputs/capabilities/skills/shared/research-multi-agent/SKILL.md`（Supervisor/Swarm/Pipeline/Hybrid 架构分类学，无画像池/任务书/裁决规则）②`30_wiki/workflows/workflow-cross-agent-fact-dispute.md`（事后争议裁决，非并行研究）③`40_outputs/capabilities/skills/shared/kdo-self-attack/SKILL.md`（对抗攻击已有卡，非并行研究）→ 三者互补不重叠【实证】
→ [边界牌] 牌7·先对标准则再建模 → WebSearch 实测（arXiv 2311.17371 MAD benchmark 等）：**无门控的 devil's advocate 降低准确率**、画像须按域相关性策展而非堆数量、MAD 未必优于 Self-Consistency → 写进合并裁决规则做硬约束
→ [结构牌] 牌8·先定总纲再子卡 → workflow 卡=总纲（六节强制：使用场景/操作步骤/适用边界/为什么值钱/与其他知识的关联/Critique + O8 定位块，`90_control/scripts/card_review_checklist.py:111` 实测要求）
→ [结构牌] 牌9·先 framework 再 concept → workflow 卡先行，skill 为其可执行件（互链）
→ [结构牌] 牌10·先骨架再填肉 → 骨架（触发→分视角→任务书翻译→并行调研→合并裁决→报告）先落，再填每步判断标准
→ [过程牌] 牌11·先 dry-run 再 apply → 试金石=小课题真跑 3 研究员（真实子 Agent 并行，非纸面推演）
→ [过程牌] 牌14·先跑脚本确认再下结论 → `python -m kdo pre-submit --files <...>` 实测贴输出（deprecated 脚本已核对：`90_control/scripts/pre_submit.py` 指向同命令）
→ [质量牌] 牌15·先自攻击再提交 → 交付前对 workflow 卡跑四路攻击

## 执行报告

**交付物**（四件，全入仓）：
- `30_wiki/workflows/workflow-multi-researcher-cross.md` — workflow 卡（六节强制 + O8 定位块 + 试金石实录节）
- `40_outputs/capabilities/skills/shared/multi-researcher-cross/SKILL.md` — 可执行版 skill（任务书模板 / 10 张研究员画像池 / 合并裁决规则，含 A62「不省 Token/信息传清楚」嘱咐）
- `60_feedback/diagnosis/working/pilot-multi-researcher-cross-20260906.md` — 试金石存档（3 研究员真跑，三份报告全文存档）
- `30_wiki/index.md` — index 登记（workflows 节，L2874）

**完成内容**：把课程场景（A60-A61 Truman 哈佛案例教学法 6 Agent 并行研究 + B93 技能中心）KDO 化为可执行工作流：触发 → 10 选 3-5 分视角 → 任务书翻译 → 并行调研 → 合并裁决 → 分层报告。试金石真跑 3 研究员（P3 决策心理师 / P7 交付运营工程师 / P5 壁垒审计师，同通道多实例并行互不可见），验证流程能跑通 + 视角确实分歧（三报告对"根因在哪一层"给出三种切法，非同一结论三次复述）+ 裁决规则可执行【实证，workflow 卡试金石节 + 存档全文】。

**验证**：
- pre-submit（三件一起）：`python -m kdo pre-submit --files <workflow卡> <SKILL.md> <存档>` → **3/3 PASS，0 errors**。完整输出：

```
====================================================================
  Pre-Submit Gate Report
====================================================================
  Files checked: 3
  Passed:        3
  Failed:        0

  [YAML]: 0 issues
  [WIKILINK]: 0 issues
  [DOMAIN]: 0 issues
  [DK_SECTION]: 0 issues
  [OUTLINK]: 0 issues
  [ALIASES]: 1 warnings
    🟡 pilot-multi-researcher-cross-20260906.md — Source names not in title/aliases
  [POSITION_DECLARATION]: 0 issues
  [SOURCE_REACHABILITY]: 0 issues
  [QUALITY_SCORE]: 3 info
    📊 workflow-multi-researcher-cross.md      75/100 | pos:25 | src:25 (5) | decomp:25 (3)
    📊 multi-researcher-cross/SKILL.md         25/100 | pos:N/A | src:0 (empty)
    📊 pilot-multi-researcher-cross-20260906.md 60/100 | pos:N/A | src:25 (3) | decomp:10 (1)
  [BODY_SRC_UNKNOWN]: 0 issues
  [VLM_TWO_SECTION]: 0 issues
  [CONCEPT_CROSSCHECK]: 1 warnings
    🟡 workflow-multi-researcher-cross.md — 涉及已有概念 5 个，请人工核对权威定义一致性（#542 提示制不拦截）
  [QINGDANTI_STRUCTURE]: 0 issues
  [QUOTE_VERBATIM]: 0 issues
  [SOURCE_RANGE]: 0 issues

  ✅ Result: PASS（2 条 WARNING 在列——有警在身，非全清，终审前自行掂量）
```

- 收尾修补实证：存档补 frontmatter + 正文 1 处实证 token 截写（`src_unk*` + 可复跑 grep 锚），修前 2 轮 FAIL（缺 frontmatter / 正文占位门禁误伤实证引用）→ 修后 PASS【实证】
- 存档锚点复跑：`grep -c "src_unk" 30_wiki/log.md` → 218（P5 报告"库内污染实证"可独立复跑）【实证】
- 入仓核查：四件 `git log --oneline -1` 各命中（vault backup 062924400）；存档收尾修补另 commit c1471d190【实证】
- L9 双落盘：complete 后实测——`queue_transition.py status` 显示 `pending_review: 1 → #664`，任务单 frontmatter `status: pending_review` + `evidence` 路径留档，双验通过【实证】

**边界**：
- 试金石只验证「流程能跑通 + 视角分歧 + 裁决规则可执行」，**不验证「合并报告优于单角色报告」**——需同课题双跑对照（单角色 vs 三研究员交叉），属后续工作【推断】
- 画像 3/10 抽样（P3/P5/P7），全池未覆盖；画像只改信息源与怀疑点，不背书专业能力
- **600s 后台任务上限事件**：本次真跑曾撞 Claude Code 后台任务 600s 等待上限被掐断，四件交付物已完整落盘后才由后续会话收尾。多研究员真跑的超时约束是本工作流**已知运行限制**——后续可设 `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS=0` 或改异步模式化解，另行立项，不属本单【实证】
- 与 kdo-self-attack 互补不重叠（任务单边界节既定）：交叉=多视角并行研究，攻击=对抗性验证
- skill 质量预分 25/100（src:0）为 skill 类文件常态形态（无 source_refs frontmatter 字段），非缺内容；workflow 卡 75/100

**需要谁动作**：欧阳锋终审（workflow 卡 + skill + 存档三件；pre-submit 输出已附上节，2 条 WARNING 如实在列）。终审通过后如需 `kdo index --rebuild`，按铁律通知黄药师执行（老顽童不自己跑）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 4 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
