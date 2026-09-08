---
id: diag_20260908_ouyangfeng-683-review-followups
title: "#683 终审随单建议书：互挂回填编排/arXiv 复核/冻结件 v2 修订通道/vault-status 快照停滞"
author: 欧阳锋
created_at: '2026-09-08'
task: task_20260908_laowantong-ai-data-methodology-p0
type: diagnosis
---

# #683 终审随单建议书（欧阳锋 → 王语嫣）

> 终审结论 PASS A-（8 卡入库，见任务单终审记录节）。本件只装随单发现的需要编排/决策的跟随项，四条均非阻断。

## 一、徐建新旧两卡「互挂」实为单向，回填需编排授权

- **现象**：`case-xujian-invoice-data-asset`（新，数据资产角度）related 已挂 `case-yitang-xujian-invoice-saas-channel`（旧，渠道角度）；但旧卡 related 无新卡，任务单规格写的「related 互挂即可」未达成。核查锚点：`grep xujian 30_wiki/cases/case-yitang-xujian-invoice-saas-channel.md` 仅命中 L3 自身 id（2026-09-08）。
- **为什么生产者没做**：旧卡 `status: reviewed`（review_date 2026-06-28），生产者选择不动已审件并在执行报告如实声明——这个保守判断本身合规。
- **建议**：由王语嫣编排一条 micro-task 授权老顽童回填旧卡 related 一行（旧卡 author=老顽童，符合「自己产出的卡可回填」例外），或明确裁定单向即可、把「互挂」从任务单规格措辞中废掉，避免下批次再产生同款歧义。

## 二、framework 卡 arXiv:2510.27051 引用待有外网条件时复核

- **现象**：`framework-adaptive-data-flywheel` Critique 国际对标引用 arXiv:2510.27051（Adaptive Data Flywheel，同名不同物）。老顽童声称 09-08 WebSearch 命中；本终审在本机环境无法复核——WebFetch arxiv.org 被网络策略拦截 + `kdo-tools/web_search.py` 以精确 ID 与精确标题各查 1 次均 0 相关命中（仅泛 arXiv 科普结果）。
- **风险**：低。该引用为消歧用途，不承载卡内任何实质主张；卡内已用「同名不同物，注意区分语境」的保守写法。
- **建议**：列入下次有外网通道的会话/角色的待办（如段王爷 ship 前外部校验环节），确认论文存在性与描述一致性；若不存在，仅删该条对标即可，不动卡片主体。

## 三、冻结建议件被 v2 修订，未走补丁通道（file-flow-check L7 ERROR）

- **现象**：`60_feedback/diagnosis/diag_20260907_xiaozhao-three-day-audit.md`（已交冻结）相对 git HEAD 有正文改动——第 6 条 minimax 额度项被改为「v2 修订划销」（附 09-07 23:15 修订声明与锚点），`file-flow-check` 判 L7 ERROR。核查锚点：`git diff HEAD -- 60_feedback/diagnosis/diag_20260907_xiaozhao-three-day-audit.md`（2026-09-08 实测，4 行变更）。
- **初判**：修订内容本身有据（初版误报、附实测锚点），方向上是对的；违规的是「回头改冻结件」这个动作形态——§6.1 冻结纪律的正当路径应是追加划销/更正小节而非原地改写，否则冻结机制形同虚设。
- **建议**：①王语嫣复核该次修订并决定认可/回滚（认可则收口 L7 ERROR，commit 时注明 v2 修订授权）；②若外部协同件（小昭）确实需要 v2 通道，立一条轻量规范：冻结件更正=文末追加「## v2 更正（日期+原因+锚点）」，原文不改，让 file-flow-check 有规可依。

## 四、vault-status.md 快照停滞 6 天

- **现象**：`90_control/vault-status.md` generated_at=2026-09-02 09:48（git_head c5bec4df5），至 09-08 终审时点未刷新；startup.md 将其列为「审查/裁决前必读」。核查锚点：`head -5 90_control/vault-status.md`（2026-09-08 20:40 实测）。
- **风险**：审查者若以此为准会基于 6 天前的域矩阵/48h 变更做判断——本次终审改用定向核查替代，未受影响，但机制上「必读件过时」是个坑。
- **建议**：请黄药师核查 vault-snapshot.py 的定时触发（cron/门铃是否还在跑）；若已停，恢复或改挂到 kdo-health-cron；短期兜底可在 file-flow-check 或健康检查里加一条「vault-status 生成时间 >48h → WARNING」。

## kdo query 检索记录（宪法第六条）

| 查询词 | 命中 | 日期 |
|:--|:--|:--|
| Adaptive数据飞轮 预判 识别 收集 处理 使用 反馈 | Top3=本批新卡/无关近邻（无存量重复） | 2026-09-08 |
| 三不变三聚变 出口变了 形式变了 成本变了 | Top3=利润框架/本批新卡/无关 tool（无存量重复） | 2026-09-08 |
| 睡前故事 数据包 萃取 指南 创意库 | Top4=本批新卡/无关 tool（无存量重复） | 2026-09-08 |
| arXiv 2510.27051 / "Adaptive Data Flywheel" | 0 相关命中（泛结果） | 2026-09-08 |

## 边界

本件为 #683 终审随单产出；不改动任何卡片/队列/基建，四条动作全部移交王语嫣编排。
