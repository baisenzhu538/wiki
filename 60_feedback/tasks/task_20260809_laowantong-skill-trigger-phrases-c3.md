---
id: task_20260809_laowantong-skill-trigger-phrases-c3
assignee: hermes
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-09
updated_at: '2026-08-09T12:00:42.935280+00:00'
priority: P1
wsjf: 2.0
---

# #278 C3 拆分：Skill 触发词补全 13 个（#301 · E026 单角色铁律）

## 任务目标

从 #278（黄药师 Skill 盘点审计）拆出的 C3 条件项——**一个任务一个角色（E026 铁律）**：触发词补全属于内容生产（老顽童），不塞进黄药师的审计任务。

## 规格

1. 补全 13 个 skill 的 `## 触发词` 节（P1 违规清单在 `60_feedback/diagnosis/audit_20260809_huangyaoshi-skill-cleanup.md` 的 P1 表——含 ai-image-prompt-engineering、data-curator 等 13 个明细）
2. 触发词格式参考：已合规 skill（task-orchestration 等）——中文触发场景 + 负面例子防误触发
3. 洪七公相关的 skill（多模态类）可转其归属——本任务先做老顽童归属部分，洪七公部分如清单含多模态 skill 则另拆

## 验收标准

- 13 个 skill 触发词节全部补齐（或按归属拆分完成并注明）
- `kdo skill eval` 触发词命中测试通过（抽查 3 个）
- 与 #278 审计报告 P1 清单逐项对账（13/13）

## 依赖

- #278 reviewed（审计报告就位）——**注意：#278 初审 B+，C1/C2 已修复待欧阳锋复审，本任务依赖审计报告内容即可（不等复审）**

## 边界

- 只补触发词节，不改 skill 其他内容
- 不修改 #278 任务单（E025 铁律：调整另开新任务）

## 终审记录（2026-08-09 欧阳锋）

**verdict: PASS A · blocking: 无 · methodology v2.2**

O3 独立验证：
1. **13/13 触发词节全对账**：#278 审计 P1 清单逐项命中（ai-image-prompt-engineering/audio-production-pipeline/consultant-mode-yai-style/config-cascade-debug/data-curator/delivery-producer/hermes-gateway-revival/image-ocr/image-ocr-easyocr/image-understanding-pipeline/knowledge-curator/long-image-ocr/system-linter——每节 1 个 ## 触发词，无重复）
2. **负面例子防误触发**：抽查 config-cascade-debug（"不要触发：代码逻辑 bug/依赖版本问题/首次配置"）——超出任务要求的质量设计
3. 队列注释修复验证：L304 残留注释已在表格外（parse 281 全可见 + #301 可见）——第二次同型问题（#280 首次），报告建议补强 pre-submit-self-check 技能检查清单 ✅
4. **双轨一致性**：13 个改动的 skill 无漂移（#267 纪律遵守——shared 改后已同步 .claude）✅
5. 归属说明合理：6 个多模态类一并补齐（省流转）

🟢 观察：task-orchestration 双轨漂移 1 个（shared vs .claude 内容不同）——非 #301 引入（#301 未动该 skill），疑似王语嫣改 task-orchestration 未跑 sync——建议跑 `skill_bridge_sync.py sync --apply` 或由黄药师确认

五维：溯源 90/逻辑 90/暗知识 85/可操作 95/表达 90 → 总分 91（A）
