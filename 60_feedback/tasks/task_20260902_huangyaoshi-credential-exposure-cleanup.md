---
id: task_20260902_huangyaoshi-credential-exposure-cleanup
title: 凭据三件套处置（散点审计 R1，P0 安全项）
seq: 600
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
priority: P0
updated_at: '2026-09-01T17:37:09.924943+00:00'
instance: huangyaoshi
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

## token 轮换建议（老朱动作，agent 不代办）

以下凭据曾在 vault 内裸露且**曾入 git 历史**（本次仅做索引清除+物理隔离，未改写历史）——按泄露处置惯例建议轮换：

1. **douyin.com 会话 cookie**（原 `./--help`）：建议重新登录抖音网页版使旧 cookie 失效
2. **飞书 user token**（原 `duanzhixing/feishu_user_token.json`）：建议在飞书开放平台重新签发
3. `_sg_cookie.txt`（curl 残留，未入 git 历史）：风险较低，如对应服务重要建议一并轮换

## 执行报告

**交付物**：
- `90_control/.sandbox/quarantine-20260902/`（隔离区，含 douyin-cookie--help.txt / _sg_cookie.txt / feishu_user_token.json 三件，物理保留零删除）
- `.gitignore`（新增 `90_control/.sandbox/quarantine-*/` 封口规则）
- git 索引清除 commit：`--help` + `duanzhixing/feishu_user_token.json` 从索引移除（delete mode，工作树经隔离区物理保留）

**完成内容**：P0 凭据三件套处置完毕——①`./--help`（douyin 会话 cookie，git 已跟踪）：git rm --cached 清索引 → 移隔离区（更名 douyin-cookie--help.txt 消除 `--` 选项解析风险）；②`60_feedback/_sg_cookie.txt`（未跟踪）：直接移隔离区；③`duanzhixing/feishu_user_token.json`（git 已跟踪）：git rm --cached → 移隔离区；④.gitignore 补 quarantine-*/ 规则防再入库。全程未打印/未复制任何凭据内容；移动用 Python shutil（中文路径纪律），逐件 exists() 双向复核。

**验证**：①原位三件 Path.exists() 全 False、隔离区三件全 True（含字节数对账 473B/420B）；②`git ls-files` 对两 tracked 件返回 0 行；③`git check-ignore` 验证隔离区命中忽略规则；④索引清除+gitignore 已 commit。

**未做项**：①git 历史改写（按任务单安全栏第 2 条不做，历史含凭据已标注轮换建议）；②实际 token 轮换（归老朱）；③vault 全库凭据模式复扫（本单只管审计点名的三件，全库扫可另立项）。

**需要谁动作**：欧阳锋——终审 #600（重点：三文件 vault 原位不可见+隔离区在位+git 索引零凭据+轮换建议已写）；老朱——执行三项 token 轮换（见上节）。
