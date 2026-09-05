---
id: task_20260906_huangyaoshi-launcher-hermes-profile-flag
title: "拉起器 hermes 通道角色机制修正：TOOL_ENV env 变量失效 → 改 -p flag（段王爷 P0 实证）+ 历史影响面核查"
seq: 650
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 段王爷建议书 diag_20260906_duanwangye-hermes-headless-profile-flag（王语嫣 09-06 裁定采纳，P0 发现）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-05T19:47:59.831714+00:00'
---

# #650 拉起器 hermes 通道角色机制修正（黄药师）

## 背景（段王爷实测，证据全在建议书）

`diag_20260906_duanwangye-hermes-headless-profile-flag.md`（status: draft，证据三条）：
- `HERMES_PROFILE` **环境变量**在无头单发（`hermes -z ... --yolo`）中**不生效**——三个非五绝 profile 全部错加载为发起者默认 profile（自称"段王爷"）
- 命令行 **`-p <profile>` flag 正确生效**（`hermes -p skills-assistant -z "你是谁"` → PROFILE_OK）
- `kimi-headless-launch.py` 的 `TOOL_ENV = {"hermes": {"HERMES_PROFILE": "{role}"}}` 用的正是失效机制

## 任务

1. **修 launcher**：hermes 条目角色切换从 env 变量改为 `-p {role}` flag（arglist 注入，env 移除或保留兜底需验证后定）。
2. **历史影响面核查（必做）**：09-02~09-03 hermes 通道四实例时代的拉起（logs/headless-*.log），抽验各实例自称/输出特征是否与目标 profile 一致——若历史上全是同一 profile 在干活，产出受影响任务清单报王语嫣（涉角色隔离与记忆污染面，须老朱知情）。
3. **回归**：拉起器狗粮——hermes 通道拉一次测试 profile，自称核验 = 目标角色。

## 边界

- 段王爷对 09-03「两连死+锁挂」的重审（间歇故障非通道死刑）记录在案，但 laowantong 回 kimi 的路由决定不变（kimi 额度恢复后按 ROLE_TOOL 走）；本单只修机制不扩路由。
- 现 ROLE_TOOL 四主力无 hermes 通道（huangyaoshi/laowantong→kimi、ouyangfeng→codex），当前产线不受此 bug 影响——历史核查是本单重心。
