---
id: task_20260714_wangyuyan-badcase-feedback-loop
assignee: hermes
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-07-19
grade: A-
updated_at: '2026-07-19T10:30:00+00:00'
---

# Task #188 · bad case 回流机制与首条记录

- **状态**：reviewed
- **负责人**：老顽童
- **优先级**：P1
- **依赖**：无（四域教练已建成）

## 背景
184 个任务完成，四域+OPC 销售教练 agent 全线可用。下一阶段主线从「建域」转向「用域」：通过真实使用暴露话术/结构/检索缺陷，再回流修正卡片与 agent-spec。需要一条轻量机制把「使用中遇到的问题」变成可追踪、可修复的资产。

## 目标
建立 bad case 记录模板+存储位置+回流流程，并记录首条 bad case。

## 工作清单
1. **机制卡**：`method-工厂-bad-case-回流机制`（30_wiki/methods/ 或 60_feedback/），含：
   - bad case 记录模板（场景/输入/预期输出/实际输出/缺陷分类/责任域/修复动作/验证方式）
   - 存储路径：`60_feedback/bad-cases/YYYY-MM-DD-<简短标签>.md`
   - 缺陷分类：检索失败/话术生硬/深度不够/身份切换失灵/边界错误/事实幻觉/格式不符
2. **首条记录**：老朱使用任意教练 agent 或销售助手时发现的第一个不满意案例，按模板落盘
3. **agent context 补丁**：在 `wangyuyan-context.md` 和老顽童/黄药师任务启动步骤里加「读最近 3 条 bad case」
4. **闭环流程**：每条 bad case 必须关联到具体卡或 agent-spec 修复项，修复后标注 verified

## 验收口径
- 机制卡 1 张+模板 1 份+首条 bad case 记录 1 条
- lint 无新增
- 老朱能按模板自行记录后续 bad case

## 流程
流程A 直通。首条记录可在任务执行过程中等老朱提供，也可由老顽童模拟一条典型问题先跑通模板。

---

## 终审记录（2026-07-19）

**等级：A-**。机制卡结构完整，模板+存储路径+缺陷分类+闭环流程四件套齐全。bad case 回流是从「建域」转向「用域」的关键基础设施。首条真实 bad case 待老朱使用后落盘。

<!-- 手动终审：queue_transition.py 拒绝执行（队列状态已是 reviewed，无法从非 pending_review 状态终审）。手动修复任务单 frontmatter status→reviewed + reviewed_by/review_date/grade。队列状态本身已是 reviewed，无需修改。 -->
