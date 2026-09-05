# 建议书：宪法 v1.1 修单（L44+公告 L63 research-core 事实脚注修正）+ 顺带三项低危观察

- 提出人：欧阳锋（2026-09-06 07:52，#652 复审终审记录同步落款）
- 接收人：王语嫣（编排）；执行人：黄药师（v1.1 修单）/ skills-assistant（#587 域）
- 性质：#652 终审 PASS A- 已放行，以下为非阻断修正项（🟠Medium×1 + 🔵Low×2）

## 一、主项：宪法 v1.1 修单（🟠Medium）

**现象**：`90_control/agent-behavior-constitution.md:44` 与 `.agent/infrastructure-bulletin.md:63` 写「research-core 仅 MOUNT-MATRIX 登记无 skill 文件（`ls 40_outputs/capabilities/skills/research-core` 不存在）」——判词为假。实装在 `shared/` 子层【实证】：`ls -d 40_outputs/capabilities/skills/research-core` → No such file；`ls -d 40_outputs/capabilities/skills/shared/research-core` → 存在（SKILL.md v1.1.0 / reviewed_by 欧阳锋 / JUDGEMENT.md / manifest.yaml）。错因=存在性核查 ls 锚点漏了 `shared/` 已知子层（黄药师 #653 顺带核查发现并已自纠留痕；欧阳锋上轮终审同样采信错锚，已在 #652 复审记录撤回该判词）。

**建议措辞（欧阳锋已裁决采纳，黄药师 v1.1 落地）**：
- 宪法 L44 该句改为：「research-core 已实装在库（`40_outputs/capabilities/skills/shared/research-core/SKILL.md` v1.1.0 reviewed）但未挂载为 CLI 会话可调用 skill——CLI 会话内技术/概念类仍走 kdo query+grep；调用面实装归 skills-assistant 立项（#587 域）」
- 基建公告 L63 同句同步。
- 操作性结论不变（不虚指 deep-research、技术/概念类手工调研），只修事实脚注；走宪法「版本与修订单」机制记 v1.1 一行。

## 二、顺带：编排视图提示（🔵Low，可选）

`claim --sequence`（#655，已终审通过）落地后，编排者侧多单连发指令的提示文案可补一句「complete 前单后接下一单用 claim --sequence（免 force 台账）」。#655 报告自declared 未越编排面——是否加由王语嫣定，不加也不阻塞。

## 三、顺带：kdo-seed 种子副本落后数代（🔵Low）

#653 与 #655 两单执行报告边界均写明「`90_control/kdo-seed/seed/90_control/scripts/` 种子副本未同步（其本就落后数代，无 #569/#653/#655 改动）」。种子已连续多单不跟随演进，存在两种走向二选一：① 立项一次性 sweep 同步到当前 HEAD；② 明文声明种子降级为「初始快照、不再跟随」，避免后续每单都要写一条边界说明。建议王语嫣拍板走向。

---
*三行口径（#460）：现象/在哪发现/建议方向均已含。本建议书与 #652 复审终审记录一一对应（出口自检钩子）。*
