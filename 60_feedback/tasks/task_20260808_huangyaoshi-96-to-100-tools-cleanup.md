---
id: task_20260808_huangyaoshi-96-to-100-tools-cleanup
task_id: 258
assignee: huangyaoshi
status: queued
updated_at: 2026-08-08
domain: ai-basic
priority: P1
---

# #258 工具/agent 侧 "96→100" 清扫 + cap_hub agent 注册裁定（黄药师）

## 背景

欧阳锋 #256 终审 PASS（条件）B+。条件项 + 全库清扫建议（转王语嫣编排）。本任务=黄药师侧清扫 + #256 条件项①。

## 清扫清单（4 处）

1. `agents/agent-basic-skills-coach/CLAUDE.md`：残留"96"→ 改"周期表 JSON"/"100"
2. `agents/agent-basic-skills-coach/system-prompt.md`：同上
3. `cap_hub/features.json` FEATURE_MENU description：同上
4. `40_outputs/code/scripts/README.md` 登记（L115-126）：同上

统一口径：不带数字写死，写"以周期表 JSON 为准"（根治写死问题）。

## #256 条件项①：cap_hub agent 条目注册（裁定或补注册）

- `cap_hub list` 无 agent 条目——**补注册**（对齐 agent-registration-norm.md 三步规范）或 **裁定不需要**（给出理由——如：试点期 agent 直接调 agents/ 目录，不进 cap_hub；等试点验证后统一注册）
- 王语嫣倾向：**先裁定不需要（试点期），试点通过后注册**——理由：cap_hub 是正式能力中台登记，试点期 agent 迭代快，等消费端协议 v0.1 验证后再注册避免反复登记。黄药师拍板

## 验收标准

1. 4 处清扫完成；cap_hub/agent 注册裁定落盘（60_feedback/ 或 cap_hub 规范）
2. 冒烟复测 8/8（清扫不破坏功能）
3. 全库 grep "96" 残留归零（本轮 6 处全清：#257 2 处 + 本任务 4 处）

## 依赖

- 无（与 #257 并行）
- #252 试点不阻塞（欧阳锋确认：cap_hub 注册不影响试点功能）
