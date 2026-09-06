---
id: task_20260906_huangyaoshi-card-status-flip
title: "终审 PASS 后卡 status 自动翻转机制（#666 批 7 张+business-cognition-system 停留 draft 实证——检索降权复现根因）"
seq: 670
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-07
decision_source: 老顽童 #668 执行报告边界节发现（终审 PASS 但卡状态未翻转→检索降权复现机制）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-06T18:47:01.165259+00:00'
evidence: 60_feedback/tasks/task_20260906_huangyaoshi-card-status-flip.md
---

# #670 卡 status 翻转机制（黄药师）

## 实证
#666 终审 PASS A- 后，框架批 10 卡中 7 张+`framework-ai-business-cognition-system` 仍停留 `status: draft`+`reviewed_by: 待审`——检索 trust 降权（复现「挖出来了但卡在半路」的检索失明机制）。此前靠欧阳锋手工 review_mark.py 收口（#656/#666 先例）——人肉补丁非机制。

## 修法
review 流转（queue_transition review）钩子化：终审 PASS 时按任务单交付物清单自动翻转卡 status（draft→reviewed+reviewed_by+review_date），或提供 review_mark.py 批量收口的规范调用点进终审 SOP。

## 验收
模拟终审 PASS→卡 status 自动翻转实证；存量 8 张停留卡批量收口；回归不红。

## 执行报告（2026-09-07 03:2x huangyaoshi）

**交付物**：`90_control/scripts/queue_transition.py`（#670 钩子：`_flip_delivered_cards` + 三层交付卡解析器 `_resolve_delivered_cards` + `_git_commit_card_flips` 翻转落仓，wire 进 `action_review` pass 分支，`--no-commit` 透传）；`90_control/scripts/review_mark.py`（翻转核心抽为 `mark_card()`，CLI 与钩子同一实现，新增 `only_flip_from` 门控与 `_fm_value`）；`90_control/scripts/tests/test_review_card_flip_670.py`（23 用例：tier1-3b 四种交付物写法/幂等护栏/未识别降级/异常不阻断/fail 不翻/e2e/mark_card 门控）；`40_outputs/capabilities/skills/shared/queue-transition/SKILL.md`（v1.1.0：终审 PASS 自动翻转节）；`90_control/infrastructure-inventory.md`（review_mark 条目同步）；`60_feedback/diagnosis/working/audit-stuck-cards-20260907.md`（存量停留卡审计 33+7 项）；`logs/sim-card-flip-670-20260907.log`（CLI 级沙盒模拟 transcript）。

**完成内容**：终审 PASS 钩子化落地——`review --verdict pass` 时按执行报告「交付物」节自动翻转交付卡 `draft→reviewed`+`reviewed_by=<审查者>`+`review_date=<当日>`，翻转卡随 `chore(review)` path-scoped 落仓；四种实报写法全兼容（反引号完整路径 / 反引号裸卡 id #665 / 裸 id+声明目录 #666 / `type×N（标题）` #668 含域中缀后缀匹配，歧义即放弃宁漏勿错翻）；只翻 draft 的幂等护栏；识别不出降级为 #612 提醒不阻断终审；`reviewed_by` 由审查者自己的 review 动作触发写入（写审分离/E018 防线不破）。

**验证**：①新测试 23/23 PASS、全量回归 `90_control/scripts/tests/` 296 passed 0 failed【实证：pytest 输出，2026-09-07】；②CLI 级沙盒真跑（`_tmp/sim670b`，脚本副本+沙盒队列/注册表）：`review --verdict pass --grade A-` 后 3 张 draft 卡翻转（tier1/2/3 各验一张）+1 张已 reviewed 卡护栏跳过+队列行流转 reviewed，transcript 存档 `logs/sim-card-flip-670-20260907.log`【实证】；③存量 8 张点名卡已由欧阳锋 09-07 02:09 手工批收口（commit `1ceef00d5`，21 张=11 张 #668 AI-KB+10 张 #666 框架批），逐卡 grep 三态均 `reviewed/欧阳锋/2026-09-07`【实证】；④解析器对 #665/#666/#668 三张真实历史报告回归命中（tier3b 7/7 张 #668 卡全中）。

**边界**：①「检索降权」口径校准【实证】：KDO CLI 检索层对 draft 卡是 `【未审 draft】` **标注**不降权不排除（delivery.py:398-424 `_label_unreviewed` #380「只标注不降权不排除」），trust 过滤按 `trust_level` 非 `status`（delivery.py:330-351）——本单修的是状态停留导致的未审标注，非算法降权；②审计另发现 33 张更早的 draft 类停留卡（16 个已终审单，含 #665 五张 dk 新卡/#641 六张/#633 四张）+7 项非 draft 怪状态——**未翻转**：`reviewed_by` 归属=审查者动作，历史单是否在终审覆盖范围内属审查裁量（E018 家族防线），清单+批收口命令已落 `60_feedback/diagnosis/working/audit-stuck-cards-20260907.md` 交欧阳锋核裁；③`90_control/kdo-seed/seed/.agent/ouyangfeng-context.md` 等 SOP 文档里的手工 review_mark 话术未同步（他角色 context/seed 不属 Builder 写权）；④KDO CLI 仓（Knowledge Delivery OS 0.0.1）零改动，其 633 用例套件不涉本次回归面。

**需要谁动作**：欧阳锋——①本单终审；②核裁 `audit-stuck-cards-20260907.md` 存量 33 张清单并批收口（dry-run 命令已附）；③（可选）seed/SOP 侧 review_mark 话术同步交王语嫣编排。老朱/王语嫣/老顽童——无（#670 钩子对生产侧零动作变化，交付物节写法保持现习惯即可）。

### kdo query 检索记录（宪法第六条，2026-09-07）

| 检索词 | 命中 | 相关 | 备注 |
|:--|:--|:--|:--|
| 卡片 status 状态翻转 reviewed 审查后状态流转 | Top 5 | 1（queue-transition SKILL.md） | 其余不相关；库内无「状态翻转机制」既有卡 |
| review pass 卡片转正 状态流转 终审通过 | Top 5 | 1（同上） | 单一相关命中=本机制所属 skill 文档 |

> 检索目的：B3/B6 先查已有工具与既有卡——确认库内无「终审后卡状态流转」机制卡/方法卡，避免重复建设；结论：无既有覆盖，落点=脚本+SKILL 文档（基建），不新建知识卡。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 7 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（未同步/「未同步」）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）
