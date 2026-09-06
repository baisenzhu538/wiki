---
id: task_20260906_laowantong-multi-researcher-cross
title: "场景复现一：多研究员交叉研究工作流（老朱拍板第一优先，A60-61 课程口径 KDO 化）"
seq: 664
status: in_progress
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 老朱 09-06 拍板第 4 项「多研究院交叉」；课程金矿 A60-A62+B93（楚门哈佛案例教学法研究）
reviewer: 欧阳锋
instance: laowantong
updated_at: '2026-09-06T07:44:59.468495+00:00'
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

（完工后回填五字段：交付物/完成内容/验证/边界/需要谁动作）
