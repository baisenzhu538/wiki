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

---

## 执行报告（#650，黄药师 2026-09-06）

**交付物**
- `90_control/scripts/kimi-headless-launch.py`：TOOLS.hermes 模板加 `-p {role}`（arglist 注入，占位符复用既有 `{role}` 替换链）+ TOOL_ENV 移除 `HERMES_PROFILE` 死配置 + 注释更正
- `90_control/scripts/tests/test_headless_launch_650.py`：+3 回归（flag 机制在位/死配置不回填/`{role}` 注入生效）
- `60_feedback/diagnosis/diag_20260906_huangyaoshi-hermes-profile-impact-audit.md`：历史影响面核查报告（报王语嫣转老朱，含受影响任务清单+污染面三查+段王爷 diag 一处证据更正）

**完成内容**
- 修 launcher：env→flag。源码级核实（hermes `hermes_cli/main.py::_apply_profile_override`）：无头 profile 解析链只认 ①argv `-p` → ②`%LOCALAPPDATA%\hermes\active_profile` sticky 文件（现值 **huangyaoshi**，mtime 09-02 00:09:25）→ ③`HERMES_HOME` 指向 profiles 目录——`HERMES_PROFILE` env **整条链不被读**（仅 kanban worker 拿它当作者标签），故 env 移除而非保留兜底（留死配置=误导后人）
- 历史影响面核查：不用日志抽样，直接查各 profile `state.db` sessions 表做权威 enumeration。09-02~09-03 窗口 hermes cli 会话 17 条：**11 条老顽童意图会话错载 huangyaoshi profile**（09-03 01:09–11:09，涉及 #626/#629/#630/#632 四单施工）+1 条通路探针同错载；huangyaoshi/ouyangfeng/wangyuyan 各自落点正确；09-03 01:01 一条老顽童会话落点正确（疑手动直调带 -p，机制无法回溯）
- 污染面三查：①记忆层无污染（huangyaoshi profile `memories/MEMORY.md` 7 行、mtime 09-01 09:58 早于窗口，无老顽童写入）②11 条老顽童会话混入黄药师 profile 会话库（建议留现状不清洗）③施工期加载了黄药师 SOUL/skills/config 上下文（产出均经独立终审，实务风险低）
- KDO 层身份未串的旁证：错载会话自称抽验全部仍是"老顽童"（`headless-laowantong-20260903-010947.log`："我是谁：老顽童（laowantong）"）——prompt 模板扛住了身份

**验证**
- 狗粮（任务 3）：拉起器 `--tool hermes` 拉 `skills-assistant` → 自称"skills-assistant（Skills 助理…职能是 skill 生产+配置中枢…）"= 目标 profile ✓
- 阴性对照（黄药师今日亲跑）：`HERMES_PROFILE=skills-assistant hermes -z 身份自检` → 自称 **huangyaoshi**——错载机制当场复现，与段王爷三 profile 实测互证
- 回归：`pytest 90_control/scripts/tests/test_headless_launch_650.py` 3 passed；`pytest kdo-tools/tests/` 272 passed（全量不红）
- 引用完整性：`kimi-headless-launch.py` 改动经 `py_compile`；`{role}` 占位符替换链未动（既有调用方零改动）

**边界**
- 本单只修 hermes 通道机制，不扩路由（laowantong 回 kimi 的 09-03 决定不动）；kimi/claude/codex 三模板未触碰
- 历史核查窗口按任务书限定 09-02~09-03；09-01 的 6 条会话（hermes 上线前）在窗口外，仅登记不在清单
- `-p` 指向不存在的 profile 会 exit 1——五绝中 `hongqigong` 在 Windows 原生根（LOCALAPPDATA）无 profile 目录，如需 hermes 通道先补 profile（已写入 diag 建议 3）
- 段王爷 diag 证据 1 所引两条"hermes 成功日志"实为 kimi 通道（首行 `kimi version 0.39.1`）——已在 diag 附带更正，其"间歇故障非通道死刑"结论不受影响
- 「两连死」0 字节日志与 state.db 有会话的矛盾（stdout 丢失 vs 进程死）登记为待立项嫌疑，未在本单展开

**需要谁动作**
- 欧阳锋：终审本单（launcher diff+测试+diag 报告）
- 王语嫣：**转老朱知情**——#626/#629/#630/#632 四单施工上下文错载黄药师 hermes profile（产出与终审不受影响，知情即可）；diag 建议 1-4（会话库留现状/hongqigong profile 伞检查/0 字节日志立项与否）请裁定
- 王语嫣：拉起器模板若有别处副本（非本仓），需同步——本单已 grep vault 确认唯一落点
