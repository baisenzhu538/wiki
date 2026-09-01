---
id: task_20260902_huangyaoshi-tmp-script-cleanup
title: tmp 一次性脚本清理（散点审计 R5，P1）：根目录 59 + kdo-tools 25
seq: 603
status: reviewed
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
priority: P1
updated_at: '2026-09-01T21:18:59.451089+00:00'
instance: huangyaoshi-kimi
evidence: 60_feedback/tasks/task_20260902_huangyaoshi-tmp-script-cleanup.md
reviewed_by: 欧阳锋
review_date: '2026-09-02'
grade: A-
---

# #603 tmp 脚本清理

## 背景

风清扬审计 P1：vault 根目录 59 个 `_tmp_/_debug/_fix/tmp_*` 散落脚本与 txt（`_fix_source_refs_step1/2/3/final.py` 四版并存等），`kdo-tools/tmp_*` 25 个一次性脚本（3 个转写变体、3 个抓视频版本、1 个读凭据的 `tmp_publish_md.py`）。

## 范围

1. **前置（必须先做）**：`_tmp_skill_health.json`（29KB）被 `60_feedback/diagnosis/建议书_20260901_skill健康度勘察与检测方法论.md:146` 引用——先把引用改指归档后位置（或把该文件归档到 `90_control/baseline/` 并同步改引用），再动其余。
2. 根目录 59 个 + `kdo-tools/tmp_*` 25 个：逐个判定——有正式替代品的归档 `_tmp/`（已在 .gitignore 则直接移入），含凭据读取逻辑的 `tmp_publish_md.py` 单独标注随 #600 处置口径。
3. **归档不删除**：移 `_tmp/` 或隔离区，保留 git 历史可追溯。

## 安全栏

- 批量三问（dry-run 全量清单 → 范围声明 → 非空不覆盖）。
- 每个被移动文件先 grep 全库引用（含 .md 引用与脚本 import），有引用的列入「例外保留」清单随执行报告交付，不强行移动。
- 不碰 `_tmp/` 以外任何 30_wiki/40_outputs 正文内容。

## 交付物

归档后目录清单 + 例外保留清单 + 引用对账表 + 执行报告五字段。

## 验收

欧阳锋终审：根目录 `_tmp_/_debug/_fix/tmp_*` 清零（例外清单除外）+ `_tmp_skill_health.json` 引用链不断 + 抽查 5 个归档文件可追溯。

---

## 执行报告（2026-09-02 huangyaoshi-kimi）

**交付物**：`_tmp/603-archive/root/`（44 个）+ `_tmp/603-archive/kdo-tools/`（22 个）归档；`90_control/baseline/_tmp_skill_health.json`（前置项）；`90_control/.sandbox/quarantine-20260902/` 新增 3 个凭据脚本；`_tmp/603-work/`（dry-run 清单/引用正则/commit 路径单）；工作 commit `eac1f1337`（73 文件 path-scoped）。

**完成内容**：
1. 前置：`git mv _tmp_skill_health.json → 90_control/baseline/`，建议书 line146 引用同步改指新位置（链路复核：grep 命中新路径，文件 exists）。
2. 批量三问执行：① dry-run 全量清单 66 条落 `_tmp/603-work/dryrun-manifest.txt`（存在性/tracked 状态/目标冲突全 ok 零冲突）；② 范围声明=仅根目录 44 + kdo-tools 22 + 前置 1 + 凭据 3，不碰 30_wiki/40_outputs 正文；③ 纯移动无覆盖（目标目录新建）。
3. 归档 66 个：root 44 → `_tmp/603-archive/root/`，kdo-tools 22 → `_tmp/603-archive/kdo-tools/`（tracked 走 git mv，untracked 走 mv）。
4. 凭据处置随 #600 口径：`tmp_publish_md.py`（读 .env 取飞书凭据）、`_tmp_douyin_cookie.py`、`_tmp_get_cookie.py`（CDP 抓 cookie）三件 git rm --cached 后移隔离区（更名加 kdo-tools- 前缀防歧义）。
5. 例外保留 2 项（有功能/发布引用，不强行移动）：`tmp_video/`（`50_delivery/published/…manifest.yaml:54` 备份路径指向 `tmp_video/final.mp4`，已发布清单不改）；`_tmp_m371_domain_unknown.txt`（`90_control/scripts/clean-metadata-371.py:280` 写目标 + task_20260819 备案引用）。
6. 派生修复：`kdo-tools/douyin_cookie_extract.py` / `douyin_user_videos.py` docstring 用法行残留 `_tmp_*` 旧名，已更正为本名（正式版与一次性版脱钩）。

**验证**：
- 清零实测：`ls _tmp_* _debug* _fix_* tmp_*` 根目录仅剩 2 例外项；`ls kdo-tools | grep tmp` 仅剩 3 个已转隔离区（处理后复核为空）。
- 引用对账：全库 grep（md/py/cjs/sh/json/toml/bat/ps1/yaml）命中项逐条判定——功能引用 3 处全部处置（建议书改指、两个 docstring 更正、`_tmp_m371_domain_unknown.txt` 保留例外）；其余命中均为叙事性提及（pitfalls.md、taxonomy-migration 报告、任务单、本审计 diag），不构成链路。
- 可追溯抽查 5 个（_fix_source_refs_final.py→9e54f8bad、_debug_label_llm.py→2716626ac、tmp_transcribe.py→f034ae23d、tmp_wx_video2.cjs→f034ae23d、tmp_add_aliases.py→a465099db）git 历史均在。
- 隔离区落位：3 件物理存在于 quarantine-20260902/（ls 双向复核），.gitignore `quarantine-*/` 规则已在（#600 封口）。

**边界**：未动 `_tmp/` 既有存量；未碰 30_wiki/40_outputs 正文；未做 git 历史改写（含凭据脚本历史仍在，随 #600 轮换建议口径）；根目录 59 vs 实测 44+2 例外差异=审计口径含 `_tmp_skill_health.json`（转 baseline）与审计后新增/已清理项；kdo-tools `_tmp_*` 6 个并入本单一并处置（审计 25 个=tmp_* 19 + _tmp_* 6）。

**需要谁动作**：欧阳锋——终审 #603（验收点：根目录清零仅剩 2 例外、baseline 引用链、抽查可追溯，上文均已留证）；老朱——#600 已建议的凭据轮换不变（本次新增 3 个读凭据脚本入隔离区，同源风险）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ①-补 划痕路径提示

- ⚠️ 交付物节含划痕路径 `_tmp/603-archive/kdo-tools/`（中间产物非交付物，按约定豁免三态检查；如属误写请清理交付物节）
- ⚠️ 交付物节含划痕路径 `_tmp/603-archive/root/`（中间产物非交付物，按约定豁免三态检查；如属误写请清理交付物节）
- ⚠️ 交付物节含划痕路径 `_tmp/603-work/`（中间产物非交付物，按约定豁免三态检查；如属误写请清理交付物节）
### ① 声称-交付差集

✅ 1 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（「未做 git 历史」）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）

---

## 终审记录（欧阳锋，2026-09-02 05:16）

**等级：PASS A-**

**通过维度**（全部亲验，非采信报告）：
- 版本对齐：工作 commit `eac1f1337` 在仓（73 文件 path-scoped，3 插入/280 删除，纯移动+引用改指形态吻合），HEAD `185ba7e7d` 晚于交付；审查对象为当前真相源 ✅
- 清零实测：`ls -d _tmp_* _debug* _fix_* tmp_*` 根目录仅剩 2 例外项（`_tmp_m371_domain_unknown.txt`、`tmp_video/`）✅；`kdo-tools` 下 `tmp_*/_tmp_*` 为零 ✅
- 例外合法性：`_tmp_m371_domain_unknown.txt` 被 `90_control/scripts/clean-metadata-371.py:280` 写入引用（活引用，保留正确）✅；`tmp_video/final.mp4` 被已发布 manifest `:54` 引用（不改已发布清单，保留正确）✅
- 前置项：`90_control/baseline/_tmp_skill_health.json` 存在，建议书 L146 引用已改指新路径（亲读该行确认）✅
- 归档计数：`_tmp/603-archive/root/` 44 个、`kdo-tools/` 22 个，与报告一致 ✅
- 凭据处置：隔离区 3 件（`kdo-tools-tmp_publish_md.py`、`kdo-tools-_tmp_douyin_cookie.py`、`kdo-tools-_tmp_get_cookie.py`）物理在位 ✅；`.gitignore` L49 `quarantine-*/` 封口规则已在 ✅
- 可追溯抽查：5 个样本中 4 个 `git log --follow` 直达 `eac1f1337`；`tmp_add_aliases.py` 系 tracked→gitignored 目标（`_tmp/` 免跟踪），历史经 `a465099db`（08-03 首次入库 208 行）可追溯，与报告所引 commit 一致 ✅

**缺陷/记档**：
- 🟡 机器预审 🔴（意见书负向断言「未做 git 历史」无存在性核查锚点）属实但属形式项——终审已代为完成存在性核查（上文逐项 ls/git 实证），不阻断；生产侧后续意见书负向判词应附核查节（#433 口径，记录不另立项）

**残余风险**：git 历史中含凭据脚本旧版本仍在（报告边界节已声明，随 #600 老朱三项轮换口径，不属本单）；隔离区文件 untracked（设计如此，物理隔离+gitignore 封口）。

**溯源要点**：本审以文件系统实测+git log/show 逐项对账，非采信执行报告数字。

**存在性核查**（#433 口径——意见书中负向断言的核查锚点，欧阳锋终审代做）：
- 负向断言「未做 git 历史改写」核查：`git log --oneline -3 eac1f1337` 显示该 commit 为普通提交，`git log --all -- tmp_add_aliases.py` 历史链完整（a465099db→eac1f1337），无 rebase/filter-branch 痕迹 ✅
- 负向断言「未碰 30_wiki/40_outputs 正文」核查：`git show --stat eac1f1337` 73 文件清单中 30_wiki/40_outputs 正文路径命中 = 0（仅移动 tmp 脚本+建议书 1 行引用改指）✅
- 负向断言「未动 _tmp/ 既有存量」核查：归档动作均为新增目录 `_tmp/603-archive/`，`git show eac1f1337` 无 `_tmp/` 下既有文件删除记录 ✅
