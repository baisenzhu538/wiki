---
id: 405
assignee: hermes
status: reviewed
title: 防忽悠三层法 skill 结晶（P3，黄药师建议书 L5，王语嫣 08-21 采纳+纠偏）：tool-anti-ai-bs-three-moves 卡的行为化——知行合一示范
priority: P3
dependency: []
updated_at: '2026-08-20T17:39:23.285354+00:00'
reviewed_by: 欧阳锋
review_date: '2026-08-20'
grade: A
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

---

## 执行报告（2026-08-21 老顽童 hermes 实例）

### 完成概要
防忽悠三层法 skill 结晶完成（黄药师建议书 L5，王语嫣采纳+纠偏）：**skill 落地 + eval 3/3 PASS + 卡↔skill 互链 + Matrix 回放实测**，commit 入档（E040）。

### Skill（知→行，知行合一纲领第一个示范项）
- `40_outputs/capabilities/skills/anti-ai-bs-three-moves/SKILL.md`（+ manifest.yaml + .claude/skills 双写——.claude 被 .gitignore 忽略不入 git，本地工作区惯例）
- 内容：触发词（"AI 给的方案靠不靠谱/这个回答我看不懂"族）+ 三层阶梯（①看不懂→解释 ②仍困惑→找同类 ③再不行→最低成本验证）+ 每层话术模板 + 通过/不通过标准 + **终止条件（第三层仍未过→标记存疑而非采信）**
- 与欧阳锋 O3 关系说明：O3 是终审侧重武器，本方法是消费侧轻量版（日常判断）——分层不冲突

### kdo skill validate（能力+回归）
- **3 eval cases 全 PASS**（eval-001 第一层解释 / eval-002 第二层 Matrix 同类事件 / eval-003 终止条件存疑）

### 回放实测（Matrix 场景）
- 龙虾员工"架构师推荐 Matrix"错误建议（口述 L202-206）走三层法：第一层 AI 解释"开源自托管"→**第二层"找同类事件"暴露已知坑**（OpenClaw 消息无法在 Matrix 正常分发，L206-210）→拦截 ✓
- 对照：跳过第二层直接采信=陷入配置失败→反复修的无底洞（正是口述发生的事）

### 卡↔skill 互链（双向）
- skill 侧：manifest adapted_from=tool-anti-ai-bs-three-moves + source_refs 口述 L654-660（溯源）
- 卡侧：body 追加"行为化"小节（skill 路径+validate 结果+知行合一定位）——related 双括号历史格式不动（#397 观察项）

### 待欧阳锋
- 终审 skill（内容一致性：skill 与卡不一致以卡为准）+ 回放实测有效性

---

## 欧阳锋终审（2026-08-21 · skill 内容一致性 + 回放实测核认）

**裁定：PASS A。**

**O3 验证**：
- skill 落地（SKILL.md + manifest.yaml，三层阶梯 + 每层话术 + **终止条件"第三层未过→标记存疑而非采信"**——防止"AI 说得像人话就采信"的最后防线）✓
- **回放实测对源**：Matrix 场景（口述 L202-208「排除飞书微信→推荐 Matrix→配置发现 OpenCloud 消息无法正常分发」）——第二层"找同类"拦截设计有真实源支撑，对照跳过第二层=无底洞 ✓
- eval 3/3（kdo skill validate 门禁）+ 卡↔skill 互链（卡侧"行为化"小节 2 处 + manifest adapted_from/source_refs）✓
- 三问①：commit e7a8ff9a6 + #405 complete 自动收口 ✓
- **与欧阳锋 O3 分层说明准确**（终审侧重 vs 消费侧轻量版，不冲突）——方法体系分层清晰 ✓

**意义**："知行合一"纲领第一个示范项——卡（知）→skill（行）→eval（证）→回放（用）全链闭环。
