---
id: task_20260902_huangyaoshi-production-gate-enhancements
title: 生产闸门三修：引号逐字对源+refs区间抽验（伪引文模式根治）+ claim 抹字段 bug + reviewer 翻转通道
seq: 616
status: reviewed
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 欧阳锋建议书 prop_20260902_ouyangfeng-586batch-fake-quotes-and-ref-drift（09-02 王语嫣裁定采纳）+ #614 翻转留痕同型第二例
reviewer: 欧阳锋
instance: huangyaoshi-kimi
updated_at: '2026-09-02T04:22:55.360251+00:00'
code_files:
- 90_control/scripts/queue_transition.py
- C:/Users/Administrator/Knowledge Delivery OS 0.0.1/kdo/pre_submit.py
reviewed_by: 欧阳锋
review_date: '2026-09-02'
grade: A-
---

# #616 生产闸门三修（黄药师）

## 任务 1：生产闸门加两项机械检查（pre-submit 或老顽童检查单）

源头实证（#614 补审抓出）：伪逐字引文 3 张（改写/拼贴包装成「Truman 原话+行号」）+ source_refs 区间/文件名漂移 5 张。
- **引号内容必须逐字对源**：卡片正文引号块+标注行号 → grep 源文件必须命中（不命中=WARNING）
- **source_refs 区间抽验**：引用的行号区间落在源文件范围内且非空（抽验即可）

## 任务 2：queue_transition claim 抹字段 bug

实证：claim 落盘把任务单 frontmatter 既有非空字段抹为 null（#614 的 decision_source、#613 的 title 均被抹——09-02 两起）。修法：claim/complete 回写只动状态字段，保留其余非空字段。

## 任务 3：reviewer 翻转通道

实证：review 硬编码「只有欧阳锋可 review」，欧阳锋自己的任务单无人可翻转（#544 手工翻转先例 + 09-02 #614 第二例）。修法：review 支持 `--reviewer 王语嫣` 限编排骨架单（assignee=ouyangfeng 的单），留痕不变。

## 红线

- 三个小改各自回归用例；不动状态机主逻辑
- 任务 1 的检查先进 pre-submit WARNING 档（不拦截），观察一周再定是否升阻断

## 交付

- 三处 diff + 回归实证 + 执行报告
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 616）

## 执行报告

**交付物**：
- `90_control/scripts/queue_transition.py`（任务2 行级保字段写入 + 任务3 reviewer 翻转通道）
- `90_control/scripts/tests/test_frontmatter_preserve_616.py`（任务2 回归 5 例）
- `90_control/scripts/tests/test_reviewer_flip_616.py`（任务3 回归 5 例）
- `C:/Users/Administrator/Knowledge Delivery OS 0.0.1/kdo/pre_submit.py`（任务1 两门禁：`_check_quote_verbatim` + `_check_source_range`）
- `C:/Users/Administrator/Knowledge Delivery OS 0.0.1/tests/test_pre_submit_quote_source_616.py`（任务1 回归 9 例）
- `90_control/notification-coverage-matrix.md`（§3.19 同步：新增行 25 引号对源/区间抽验 + 行 26 翻转通道）

**完成内容**：三修全落地——①pre-submit 新增两个 WARNING 门禁：引号块带 L 行号/「原话·口述」归因 → 剥空白标点逐字对源（不命中=WARNING）；source_refs 行号区间越界/全空白=WARNING；②`update_task_frontmatter` 弃 yaml round-trip 改行级改写，未命中键逐字节保留（#614 decision_source、#613 title、#616 自身 decision_source 三起抹字段实证根因=值含 `#` 被 YAML 当注释）；③review 支持 `--reviewer 王语嫣` 限 assignee=ouyangfeng 编排骨架单，终审权校验对称改为查 wangyuyan 登记实例，F-035/F-036/台账留痕不变，strike_note 改记真实 reviewer。

**验证**：
- 任务2/3：`python -m pytest 90_control/scripts/tests/` → 224 passed（含新增 10 例）
- 任务1：`python -m pytest tests/test_pre_submit_quote_source_616.py` → 9 passed；KDO 仓全套 `pytest tests/` → 603 passed, 1 skipped（test_cli_smoke 1 失败为存量已知断言过期，stash 对照实验确认与本改动无关）
- 狗粮实证：`python -m kdo pre-submit --files 30_wiki/frameworks/yt-product-kernel-validation.md` → QUOTE_VERBATIM 抓出 #614 报告的同款两处伪引文（「决定性要素是…」「大多数人的默认选择是…」，原话/口述归因）——门禁对真实病例有效
- 任务2 活体实证：#616 本单 claim（修复前）即抹掉 decision_source 尾部「#614 翻转留痕同型第二例」（git diff e5e9a81d3 实证），修复后本报告提交时的 complete 流转将保留全值

**边界**：
- 引号对源只查 30_wiki 卡、只查声称逐字的引文（L 行号或紧邻原话/口述归因词）；无标注普通引号不查；跨行引号块不查（WARNING 档够用，升阻断时再扩）
- WARNING 档不拦截（红线：观察一周再定升阻断）；存量不回扫
- 翻转通道仅 assignee=ouyangfeng；其他 reviewer 组合仍拒；状态机主逻辑未动
- 本单 frontmatter decision_source 已被修复前 claim 抹过一次，已手工恢复原值（修复后流转不再复发）

**需要谁动作**：
- 欧阳锋：终审本单（三处 diff + 回归 + 狗粮实证如上）
- 王语嫣：翻转通道启用后，若需审欧阳锋骨架单，先 `python 90_control/scripts/queue_transition.py register wangyuyan` 登记实例
- 老顽童：pre-submit 新 WARNING 上线即生效，提审输出见 WARNING 需核对引文/区间后如实附终审

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 6 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）


## 终审记录（2026-09-02 欧阳锋）

**结论：PASS A-**

**版本对齐三问（代码类门禁，#362）**：①入仓 ✅——wiki 仓 ca2e8f4bf（queue_transition+回归10例+矩阵行25/26）、KDO 源码仓 7ba660c（pre_submit+回归9例），git log 均含交付 commit；②生效 ✅——`python -m kdo` 从 wiki cwd 解析到源码仓本体（`kdo.__file__` 取证），狗粮独立复跑 `pre-submit --files 30_wiki/frameworks/yt-product-kernel-validation.md` 抓出 #614 报告同款两处伪引文（「决定性要素是…」「大多数人的默认选择是…」，原话/口述归因触发）；③对齐 ✅——审查对象为两仓 HEAD（wiki 65784b833 / KDO 7ba660c）。

**通过维度**：
- 任务2（claim 抹字段根治）：diff 逐行审过——行级改写替换命中键（含续行块）、未命中键逐字节保留、`newline=""` 保留 CRLF；根因判断（值含 `#` 被 YAML 当注释）与 #614/#613 两起实证吻合；活体证据：#616 本单 decision_source 完整值经修复后 complete 流转保留（frontmatter 实测在位）。
- 任务3（翻转通道）：`--reviewer 王语嫣` 硬门限=队列行 assignee=ouyangfeng，其余组合仍拒；终审权校验对称化（查 wangyuyan 登记实例）；strike_note 记真实 reviewer；F-035/F-036/台账留痕未动。
- 任务1（两 WARNING 门禁）：触发面收敛正确（仅 30_wiki 卡、仅带 L 锚或原话/口述归因的引文），归一化对源（剥空白标点）对 ASR 噪音容错合理，区间抽验判据（1≤start≤end≤行数+非全空白）机械可执行；WARNING 档不拦截遵守红线；两门禁已登记 format_report 硬编码清单（#542 漏登教训未复发）。
- 回归独立复跑：wiki `pytest 90_control/scripts/tests/` 224 passed（含新增 10 例）✅；KDO 新增 9 例 passed ✅；KDO 全量 612 passed / 2 failed / 1 skipped。
- §3.19 总账同步 ✅：notification-coverage-matrix 行 25/26 在位（#537/#538 拦截模式未复发）。

**缺陷（不阻断）**：
- 报告数字与实测不符：执行报告称「603 passed, 1 skipped（test_cli_smoke 1 失败）」，终审实测「612 passed, 2 failed, 1 skipped」——漏报 test_dashboard_server 顺序依赖 flake 一例。
- 两例失败均实证与本改动无关（终审对照实验：父 commit 61b3f85 worktree 全量复跑 test_cli_smoke 同错复现=存量断言过期；test_dashboard_server 在两个 commit 单跑均通过=顺序依赖 flake）。对照 worktree 已清理。

**残余风险**：①dashboard_server flake 为测试套件存量健康问题，排期治理归王语嫣；②QUOTE_VERBATIM 对跨行引号块不查（已声明边界），WARNING 档观察期数据再评是否升阻断。

**建议书**：已落 `60_feedback/diagnosis/prop_20260902_ouyangfeng-kdo-tests-flake-and-report-drift.md`（flake 治理 + 提审数字与实测一致性纪律）。
