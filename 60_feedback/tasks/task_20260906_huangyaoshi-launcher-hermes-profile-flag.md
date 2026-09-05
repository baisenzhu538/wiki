---
id: task_20260906_huangyaoshi-launcher-hermes-profile-flag
title: "拉起器 hermes 通道角色机制修正：TOOL_ENV env 变量失效 → 改 -p flag（段王爷 P0 实证）+ 历史影响面核查"
seq: 650
status: reviewed
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 段王爷建议书 diag_20260906_duanwangye-hermes-headless-profile-flag（王语嫣 09-06 裁定采纳，P0 发现）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-05T20:25:34.652856+00:00'
evidence: 60_feedback/tasks/task_20260906_huangyaoshi-launcher-hermes-profile-flag.md
reviewed_by: 欧阳锋
review_date: '2026-09-05'
grade: A-
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

**存在性核查**（#433 负向判词锚点，核查时间 2026-09-06 03:55-04:00）
- 「拉起器模板 vault 内唯一落点」→ 核查：`find . -name "kimi-headless-launch*" -not -path "*/.git/*"` → 仅 `90_control/scripts/kimi-headless-launch.py`（另 `__pycache__` 编译产物，非源副本）；`grep -rln "HERMES_PROFILE" --include=*.py --include=*.md` 全仓 → 其余命中均为描述性文档（两份 diag/本任务单/todos 历史行）与 `kdo-tools/token_meter.py` 的 **`HERMES_PROFILES` 路径常量**（复数、指向 profiles 目录，非 env 变量，无因果）——不存在第二处需同步的模板副本
- 「记忆层无污染」→ 核查：`profiles/huangyaoshi/memories/MEMORY.md` 全文目检（7 行 4 条目：Python3.12 口径/黄药师施工闭环/myqueue 在途单/Windows 基建三坑）——全部为黄药师/基建主题，无任何老顽童内容条目
- 「kimi/claude/codex 三模板未触碰」→ 核查：`git show afff203ef -- 90_control/scripts/kimi-headless-launch.py` diff 全文仅三处变更（TOOLS.hermes 行、hermes 路由注释行、TOOL_ENV 表），kimi/claude/codex 三行模板不在 diff 中

**需要谁动作**
- 欧阳锋：终审本单（launcher diff+测试+diag 报告）
- 王语嫣：**转老朱知情**——#626/#629/#630/#632 四单施工上下文错载黄药师 hermes profile（产出与终审不受影响，知情即可）；diag 建议 1-4（会话库留现状/hongqigong profile 伞检查/0 字节日志立项与否）请裁定
- 王语嫣：拉起器模板若有别处副本（非本仓），需同步——本单已 grep vault 确认唯一落点

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 3 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（不存在/丢失）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）


## 终审记录

**终审人**：欧阳锋（ouyangfeng）｜**判定**：PASS A-｜**methodology_version**：v2.3

**三焦点独立核验（不复述自称，逐条复跑）**

**① 修法是否真修（狗粮自称核验）——真修，通过**
- `git show afff203ef`：`TOOLS.hermes` 模板由 `-z {prompt} --yolo` 改为 `-p {role} -z {prompt} --yolo`；`TOOL_ENV` 由 `{"hermes":{"HERMES_PROFILE":"{role}"}}` 清空为 `{}`。真改非改名。
- 源码核验 `hermes_cli/main.py::_apply_profile_override`：解析链只认 argv `-p` → `active_profile` sticky → `HERMES_HOME` env 三支，均无 `HERMES_PROFILE` 分支。全量 grep main.py：`HERMES_PROFILE` 0 命中；该 env 仅 `kanban.py`/`kanban_db.py` 作 kanban 作者标签（注释明言 "HERMES_PROFILE is the author the kanban_comment tool defaults to"）。故「env 失效→改 flag、移除死配置不留兜底」论断成立。
- 狗粮实跑：`logs/headless-skills-assistant-20260906-034853.log` 自称 "skills-assistant（Skills 助理…）" = 目标 profile，通过。
- 回归亲跑：`pytest 90_control/scripts/tests/test_headless_launch_650.py` → 3 passed（flag 在位/死配置不回填/`{role}` 注入三例）。

**② 历史影响面核查——坐实，受影响清单必须报老朱**
- 权威枚举亲查（各 profile `state.db` sessions 表，非日志抽样）：huangyaoshi profile 09-02~09-03 窗口 13 条 cli 会话，其中 12 条首条 user message 以「你是laowantong…」或「回答两个字：通路」开头却落点 huangyaoshi——11 条老顽童意图 + 1 条通路探针，与报告一致。
- 受影响任务：#626/#629/#630/#632 四单施工上下文错载黄药师 hermes profile。
- 结论坐实。受影响清单已由黄药师 diag 落盘并指名「王语嫣转老朱知情」；本终审确认该知情必须送达老朱（涉角色隔离与记忆污染面）。王语嫣为对老朱唯一沟通通道，本审不越她直报，随本 PASS 抄送王语嫣编排。

**③ 边界守住（不扩路由）——守住，通过**
- 全 commit（afff203ef）仅 3 文件：launcher + test + diag；`git show` diff 全文仅 hermes 行/注释行/TOOL_ENV 三处，kimi/claude/codex 三模板不在 diff。
- `ROLE_TOOL` 未动：laowantong→kimi（09-03 回 kimi 决定不变）、ouyangfeng→codex、huangyaoshi→kimi。只修机制，不扩路由。

**评分**：溯源完整 ✅｜逻辑骨架 ✅｜暗知识密度 ✅｜可操作性 ✅｜表达质量 ✅ → **A-**

**残留风险（非阻断，去向已定）**
- 错载期 hermes token 用量已归因到 huangyaoshi 名下，token 报表按角色读数需带校正 → 去向：随老朱知情一并提示（diag 已列）。
- 「两连死」0 字节日志 vs state.db 有会话的矛盾 → 去向：diag 建议 4 待王语嫣裁定是否立项，本单不展开。

**存在性核查**（终审侧独立锚点）
- 「HERMES_PROFILE 在 main.py 不被读」→ 全量 grep main.py 0 命中（见①）。
- 「kimi/claude/codex 三模板未触碰」→ `git show afff203ef` diff 逐行核，三模板行不在 diff（见③）。
- 「受影响清单坐实」→ 直查 state.db 首条 user message 逐条对意图与落点，12 条全对上（见②）。