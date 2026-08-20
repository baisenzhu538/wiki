---
id: 405
assignee: laowantong
status: queued
title: 防忽悠三层法 skill 结晶（P3，黄药师建议书 L5，王语嫣 08-21 采纳+纠偏）：tool-anti-ai-bs-three-moves 卡的行为化——知行合一示范
priority: P3
dependency: []
---

# #405 防忽悠三层法 skill 结晶

## 来源

- 建议书：`60_feedback/designs/design_20260821_lobster-employee-insights.md` L5（必读原文）
- 王语嫣 08-21 裁定采纳+**纠偏**：建议书漏查 L7——#379 已有 `30_wiki/tools/tool-anti-ai-bs-three-moves.md` 卡（reviewed）。本单不是产新内容，是**已有卡的行为化**：卡在库里是"知"，结晶成 skill 挂进 agent 体系才是"行"——知行合一纲领（parking-lot-wangyuyan #1）的第一个示范项

## 任务目标

把 `tool-anti-ai-bs-three-moves` 卡结晶为可执行 skill：三层阶梯（①看不懂→让 AI 解释 ②仍困惑→让它找同类事件看别人怎么解 ③再不行→让它出最低成本验证方案自证），每层带话术模板+终止条件（第三层仍未过→标记存疑而非采信）。

## 执行范围

1. 读透 `tool-anti-ai-bs-three-moves` 卡 + 口述锚点（`00_inbox/龙虾员工实践/AI经验分享-数字员工搭建-口述.txt` L654-660）+ #400 批次补强内容（若在审则只读卡片现状）
2. 写 skill：触发词（"AI 给的方案靠不靠谱/这个回答我看不懂"族），挂 agent-basic-skills-coach 体系，kdo 注册，shared + .claude/skills 双写（现行惯例）
3. 卡片侧 related 补链 skill（知↔行互链）；skill 侧标注来源卡（溯源）
4. 回放实测：用真实历史场景（如龙虾员工"架构师推荐 Matrix"错误建议）走一遍三层法，验证第二层能拦下

## 边界

- 不改卡片正文结论；skill 内容与卡不一致时以卡为准并报告差异
- platforms 字段用 OS 平台值（E030 教训：[windows] 或省略，禁止 cli/feishu）
- 完成后 commit（E040）
- 欧阳锋终审

## 内容价值判断（PROTOCOL §7 合规声明）

- 仅新增 skill 与互链，无删除/移动

## 验收标准

1. skill 通过 kdo skill eval（能力+回归）
2. 回放实测：Matrix 类错误建议在第二层被拦
3. 卡↔skill 双向互链建立

## 交付

1. skill + eval 输出 + 回放实测记录
2. 送欧阳锋终审
