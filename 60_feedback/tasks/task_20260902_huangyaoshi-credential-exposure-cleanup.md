---
id: task_20260902_huangyaoshi-credential-exposure-cleanup
title: 凭据三件套处置（散点审计 R1，P0 安全项）
seq: 600
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
priority: P0
updated_at: '2026-09-02T01:25:00+08:00'
---

# #600 凭据三件套处置

## 背景

风清扬替代期散点审计（`60_feedback/diagnosis/diag_20260902_fengqingyang-substitute-scatter-audit.md` P0-A）发现 3 个凭据类文件裸露在 vault 内。老朱 09-02 拍板「全部编排修复」，已知情。

## 处置对象

| 文件 | 说明 | 动作 |
|---|---|---|
| `./--help`（根目录，5409B，08-31 02:08 事故产物） | Netscape cookie 文件，含 douyin.com 会话凭据 | **移出 vault** 到 `90_control/.sandbox/quarantine-20260902/`，不直接删 |
| `60_feedback/_sg_cookie.txt`（473B，08-31 02:03） | curl cookie 残留 | 同上，移隔离区 |
| `duanzhixing/feishu_user_token.json` | 飞书 user token 裸露在非编号目录 | 移 `90_control/.sandbox/quarantine-20260902/` + 检查是否被 git 跟踪，若跟踪则从索引移除并补 .gitignore |

## 安全栏（不可协商）

1. **不打印、不复制凭据内容**到任何输出/日志/任务单。
2. **凭据一律不入 git**：若已在 git 历史，任务单执行报告标注「历史含凭据，建议轮换」，不做历史改写。
3. `./--help` 文件名会被 git/命令行解析为选项，**一切引用必须写 `./--help`**（相对路径带 ./ 前缀）。
4. 移动用 `git mv`（若被跟踪）或 `mv`（未跟踪），移动后 `Path.exists()` 复核。

## 交付物

- 三件套落隔离区 + 执行报告（五字段）
- 任务单末尾追加「token 轮换建议」一节，明确提示老朱：douyin cookie 与飞书 user token 建议轮换（实际轮换操作归老朱，agent 不代办）

## 验收

欧阳锋终审：三文件 vault 内不可见 + 隔离区存在 + git 索引无凭据 + 轮换建议已写。
