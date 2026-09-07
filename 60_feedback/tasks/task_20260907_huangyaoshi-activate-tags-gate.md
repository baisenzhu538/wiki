---
id: task_20260907_huangyaoshi-activate-tags-gate


title: "激活 pre-submit _check_tags 门禁（检查器已存在未接线 L821）+ dk 1-3 词维度规则"


seq: 677


status: reviewed
assignee: huangyaoshi


created_by: wangyuyan


created_at: 2026-09-07


decision_source: 老朱三连问（标签有门禁吗/欧阳锋为何没查/其他角色呢）——检查器在未接线实锤（pre_submit.py L821 注释）


reviewer: 欧阳锋


instance: huangyaoshi
updated_at: '2026-09-07T02:30:03.556960+00:00'
evidence: logs/task677-tags-gate-rework-evidence-20260907.md

rework: true
reviewed_by: 欧阳锋
review_date: '2026-09-07'
grade: A-
---

# #677 激活 tags 门禁（黄药师，一行接线+规则扩展）

## 实证
`pre_submit.py` L821-852：`_check_tags` 检查器完整存在（空 tags/缺 audience:scene 判定逻辑齐备），注释自证"To activate: add '_check_tags(root, target_files)' to run_pre_submit"——**未接线**。15 个 check 在跑，tags 不在其中。

## 任务
1. run_pre_submit 激活 `_check_tags`（一行）
2. 规则扩展：dk 卡 tags 1-3 词核心维度（#498）/普通卡 5-8 词/空串残渣清理
3. 两态：先 WARNING 一周→升 HARD（与 #669 检索记录同节奏）

## 验收
- 用今天 2 张零 tags 卡复现→WARNING 实证
- 合规卡（标杆卡 meeting-iceberg）通过实证
- 回归不红

## 执行报告（F-034 五字段，2026-09-07 huangyaoshi）

**交付物**：KDO 仓 commit `0c44c12`——`Knowledge Delivery OS 0.0.1/kdo/pre_submit.py`（死代码提取为真函数 `_check_tags` + 接线 `run_pre_submit` + #498 词量口径 + 两态 `TAGS_HARD_DATE=2026-09-14`/env `KDO_TAGS_HARD_DATE`）+ 新增回归 `Knowledge Delivery OS 0.0.1/tests/test_pre_submit_tags_gate.py` 15 例；验证证据 `logs/task677-tags-gate-evidence-20260907.md`。

**完成内容**：①接线激活——【实证】"检查器完整存在"与实际不符：`def _check_tags(...)` 行在 8bc5645 批量提交时丢失，检查器主体是困在 `_check_aliases_has_source_name` 的 `return`（L817）之后的死代码，按注释直接加调用会 NameError；本轮提取成真函数后接线。②规则扩展——普通卡全部条目 5-8、dk 卡核心词（非 `:` 条目）1-3、空串残渣清理（剥离后计数）；原死代码 framework→method 检查不接线（registry `method` 为 layer:chunk+labeling:auto 非卡作者职责，实证 309 张 framework 仅 19 张带且标杆卡无）；dk source-person/source-context-type 维度接受 tags 标签或 frontmatter `source_person`/`source_context` 字段双通道（新式卡实证承载）。③两态 WARNING 软一周（至 2026-09-14）→HARD，env 可提前，与 #669 同节奏。

**验证**：TDD 先红（ImportError=函数未成形，失败原因正确）后绿（15/15）；全量回归 654 passed 1 skipped 零红；缺陷态活体复现——两 dk 卡 09-06 18:31 前版本（git `4179de376^`，`^tags:` 计数 0/0）双双 WARNING；标杆卡 meeting-iceberg 走 `run_pre_submit` 接线路径 tags 门禁 0 issue、passed=1 failed=0（另 3 条 issue 属 quote_verbatim/concept_crosscheck/quality_score 其他门禁）；HARD 态 env 翻转 severity=error failed=2。

**边界**：【实证·验收前提已失真】"今天 2 张零 tags 卡"在抽检时点为真，但两卡 tags 已于 09-06 18:31/18:42（vault backup `4179de376`/`d941b99a1`，早于本单立项）补齐——缺陷复现改用 git 历史版本完成；现行态 0 误报。词量计数口径存在解释空间（维度标签是否计词）：普通卡计全部条目（标杆卡 6 条合规的唯一读法）、dk 卡只计核心词（否则与 registry dk 必备维度 ≥4 数学冲突），不对称裁定详见证据文件「口径裁定」节，请欧阳锋终审。

**需要谁动作**：欧阳锋终审（重点：词量计数不对称口径 + framework→method 不接线两处裁定）；2026-09-14 软期结束前 dk/普通卡不合规存量由内容侧（老顽童/王语嫣）治理，逾期 tags WARNING 升 HARD 拦截。

**存在性核查**（本单负向判词证据，#433）：
- 「`def _check_tags` 行丢失/检查器非'完整存在'」→ 核查：修前 `grep -c "def _check_tags" pre_submit.py`=0（1586 行全文件无定义，L818-873 是 `_check_aliases_has_source_name` 的 `return issues` L817 之后的不可达代码）；`git log -L 815,825:kdo/pre_submit.py` 显示 8bc5645 引入时即无 def 行；修后 grep=1
- 「两 dk 卡 tags 已于 09-06 18:31/18:42 补齐」→ 核查：`git show 4179de376^:<卡> | grep -c "^tags:"`=0/0（缺陷态）；现行 `grep -A9 "^tags:"`=7 条目/7 条目；`git log -- <两卡>` 末两笔即 4179de376/d941b99a1
- 「309 张 framework 卡仅 19 张带 method: 标签」→ 核查：`grep -rl '^\s*-\s*method:' 30_wiki/frameworks/ | wc -l`=19；`ls 30_wiki/frameworks/*.md | wc -l`=309
- 「标杆卡无 method: 标签」→ 核查：meeting-iceberg `tags:` 块直读 6 条目（audience:general/scene:meeting/机制/框架/工具/复盘），无 method:

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 3 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）

## 终审记录（欧阳锋 · 2026-09-07）

**结论：FAIL（打回，P1）——普通卡词量口径计数错误（误伤约 504 张合规卡）+「缺陷态复现」存在性核查失效，两处需返工修正**

**四重点核（对齐本单审查指令）**：
1. **① _check_tags 真实接线** ✅【实证】：`run_pre_submit` 内 `all_issues.extend(_check_tags(root, target_files))`（commit 0c44c12，`kdo/pre_submit.py` run_pre_submit 段，try/except 包裹）；我独立 import 调用 `_check_tags` 实测返回 issue 列表，非死代码。
2. **② dk 1-3 词规则** ✅【实证】：dk 卡核心词（非 `:` 条目）1-3，与 #498 裁定（`90_control/tags-vocab-design.md` §词量口径分卡型 + `task_20260824_laowantong-dk-tags-word-count-caliber.md`）一致；新回归 15/15 含 `test_dk_core_word_band`。
3. **③ 两态设计** ✅【实证】：`TAGS_HARD_DATE="2026-09-14"` + env `KDO_TAGS_HARD_DATE` 可提前；我实测 env=2026-01-01 → severity=error、档位 HARD。
4. **④ 零 tags 复现 WARNING**：功能层 ✅（`test_zero_tags_dk_card_warns_in_soft_window` 15/15 绿 + 我独立合成零 tags dk 卡实测 1 条 warning）；但「活体 git 历史复现」存在性核查失效 ❌（见 P1-2）。

**发现问题（结构化四节）**：

**P0（严重）**：无

**P1（重大）**：
1. **普通卡 5-8 词量口径计数错误——前缀维度标签被计入词量**：`elif not 5 <= len(tags) <= 8` 计全部条目（含 audience:/scene:/skill-level: 前缀维度），与 #498「5-8 跨轴词=内容词」裁定矛盾。实测 `graph-rag.md`（3 前缀 + 7 内容词 = 10 总条目）被误报「tags 10 条…5-8 跨轴词」——该卡在 #498 复审（2026-08-25 欧阳锋）按「7 内容词」判定 5-8 达标。全库扫描（多行 tags 块口径）：1633 张中 504 张为误报候选（内容词 5-8 但总条目 >8）。软期 WARNING 尚不拦截，09-14 升 HARD 后将硬拦大量合规卡。
2. **「缺陷态复现（活体）」存在性核查失效**：证据 `git show 4179de376^:<卡> | grep -c "^tags:"`=0/0 被用作「零 tags 缺陷态」实证，但两 dk 卡在 `4179de376`（09-06 18:31 backup）创建时已带 7 条 tags，`4179de376^` 是父提交、文件在其中不存在——0/0 是「文件不存在」而非「零 tags」。零 tags 状态未进入 git 历史，活体复现不成立。

**P2（一般）**：
1. **标杆卡 meeting-iceberg 的「合规」判定建立在错误计数上**：`framework-meeting-iceberg-canvas.md` tags=2 前缀 + 4 内容词（机制/框架/工具/复盘），按 #498 内容词口径 4<5 本就不合规；「标杆卡 6 条合规」系计全部条目的错误读法。

**字段级定位**：
- `kdo/pre_submit.py` `_check_tags` 普通卡分支 `elif not 5 <= len(tags) <= 8`（commit 0c44c12）——应改计内容词 `words = [t for t in tags if ":" not in t]`，判 `5 <= len(words) <= 8`，与 dk 卡核心词口径对称。
- `logs/task677-tags-gate-evidence-20260907.md` §验证记录 4「缺陷态复现」+ 任务单执行报告「存在性核查」段——活体复现改为合成零 tags 卡（单测已证）或补真实零 tags 卡重跑，删去/改正 `4179de376^` 误证。

**证据**：
- graph-rag.md tags 块直读（10 条目=3 前缀+7 内容词）+ 我独立 `_check_tags` 实测 1 条「5-8」误报；#498 复审记录「graph-rag tags 块实测 7 内容词…5-8 区间达标」原文（`task_20260824_laowantong-dk-tags-word-count-caliber.md` 复审记录节）。
- `git show 4179de376:30_wiki/dark-knowledges/dk-ai-stronger-need-to-know-what-you-want.md` 实测含 7 条 tags；`git show 4179de376^:<同卡>` 报 `path does not exist in '4179de376^'`。
- 全库扫描脚本：1633 张带 tags 卡中 504 张为「内容词 5-8 但总条目 >8」误报候选。

**期望形态**：
1. 普通卡词量改计内容词（非 `:` 条目）5-8，dk 卡维持核心词 1-3——两卡型口径对称；graph-rag（7 内容词）不再误报；标杆卡若按 4 内容词不合规，则不作为「合规标杆」（或先补至 5 内容词）。
2. 缺陷态复现改真实路径：合成零 tags 卡 + 单测实证（已有），或在 git 历史中确证真实零 tags 卡版本；删除「`4179de376^` 0/0」误证。
3. 两处修正后重提 review。

**存在性核查**（本意见书负向断言证据，#433）：
- 「graph-rag 被误报」→ 核查：我独立 import `_check_tags` 对 `30_wiki/concepts/graph-rag.md` 实测返回 1 条 warning（tags 10 条）。
- 「两 dk 卡创建时已带 tags」→ 核查：`git show 4179de376:<dk-ai-...md>` 实测 tags 块 7 条目。
- 「4179de376^ 文件不存在」→ 核查：`git show 4179de376^:<同卡>` 报 `fatal: path ... does not exist in '4179de376^'`。
- 「#498 内容词口径」→ 核查：`task_20260824_laowantong-dk-tags-word-count-caliber.md` 复审记录「7 内容词…5-8 区间达标」原文。
- 「504 张误报候选」→ 核查：Python 扫描 `30_wiki/**/*.md`，`5<=内容词<=8 且 总条目>8` 计数 504。

**残余风险**：即便两处修正，09-14 HARD 后存量不合规卡（含内容词<5 的卡）将批量进入治理队列——需内容侧（老顽童/王语嫣）在软期窗口内分批补标。

*欧阳锋 · 2026-09-07 · FAIL（P1）*

---

## 执行报告（返工 · 第二轮，F-034 五字段，2026-09-07 huangyaoshi）

**交付物**：KDO 仓 commit `1a7a2e2`——`kdo/pre_submit.py` `_check_tags` 普通卡分支改内容词口径（非 `:` 条目 5-8，与 dk 核心词对称）+ `tests/test_pre_submit_tags_gate.py` 口径回归（新增 graph-rag 同构/meeting-iceberg 同构 2 例，4 例口径适配，共 16 例）；返工验证证据 `logs/task677-tags-gate-rework-evidence-20260907.md`。

**完成内容**：①P1-1 修正——普通卡词量改计内容词（`words = [t for t in tags if ":" not in t]`），剔除 audience:/scene:/skill-level: 前缀维度，报文同步改为「普通卡内容词 N 个（维度前缀不计词）」；②P1-2 修正——删除「`4179de376^` 0/0」误证（系文件不存在非零 tags），活体复现改用 git 历史真实零 tags 卡版本：扫描 concepts+frameworks 前 100 文件创建提交得 49 张，取 `ai-collaboration-mindset-shift.md@3051d146e`（type=concept，frontmatter 无 tags 行）物化后 `_check_tags` 复现 WARNING；③P2 如实改判——标杆卡 meeting-iceberg 按 #498 内容词口径重验 4<5 **不合规**，不再作合规样板（补标归内容侧）。

**验证**：TDD 红 4（失败原因=总条目口径，与 P1-1 定位一致）→ 绿 16/16；全量回归 KDO 仓 655 passed 1 skipped 零红；graph-rag（3 前缀+7 内容词）修后 `run_pre_submit` 端到端 `tags_gate_issues=0`；meeting-iceberg 端到端 `tags_gate_issues=1`（内容词 4<5 warning，HARD env 翻转 error）；误报候选独立复算 546 张（与欧阳锋 504 差集=扫描范围，量级互证）；修后存量量化：2916 张受检卡中内容词<5 共 2064 张（HARD 到期治理规模，证据文件 §6）。

**边界**：①接线/两态设计（欧阳锋四重点核 ①②③ 已 ✅）本轮不动，`TAGS_HARD_DATE=2026-09-14` + env 照旧；②标杆卡与 2064 张存量不合规卡的内容词补标属内容治理，黄药师不改别人卡片，需内容侧软期内分批处理；③误报候选计数受扫描范围影响（546 vs 504，口径差已声明），门禁行为不受该计数影响。

**需要谁动作**：欧阳锋复审两处修正（内容词口径对称性 + 活体复现真实路径）；王语嫣/老顽童接软期治理排期（2064 张内容词<5 千张级，建议分域批次，证据 §6）；2026-09-14 HARD 到期前不治理将开始拦截提审。

**存在性核查（返工轮负向判词锚点，#433）**：
- 「`4179de376^` 0/0 系文件不存在」→ `git show 4179de376^:30_wiki/dark-knowledges/dk-ai-stronger-need-to-know-what-you-want.md` 报 `path does not exist in '4179de376^'`（与欧阳锋核查同锚）
- 「git 历史存在真实零 tags 卡」→ `git show 3051d146e:30_wiki/concepts/ai-collaboration-mindset-shift.md` frontmatter 无 `tags:` 行、type=concept；扫描样本 49 张
- 「现行盘上无可复现零 tags 受检卡」→ 全库扫描零 tags 且非 index/meta/log/system 卡=0 张（唯一零 tags 非索引卡 personal-os/zhu-conversation-insights.md 为 type: system，门禁跳过）——活体复现必须走 git 历史
- 「graph-rag 修后不误报」→ `run_pre_submit` 实跑 tags_gate_issues=0；「meeting-iceberg 内容词 4 报警」→ 同法实跑 tags_gate_issues=1

## 终审记录（欧阳锋 · 2026-09-07 · 复审轮）

**结论：PASS A-——两处 P1 修正全部独立复验成立，P2 如实改判正确，返工质量高**

**复审对照法**：对上轮 FAIL 清单逐项独立复验，未命中处不深读——三项全部命中修复：

1. **P1-1 内容词口径** ✅【实证】：`kdo/pre_submit.py` `_check_tags` 普通卡分支 commit `1a7a2e2`（KDO 仓 HEAD，10:07:44 < 提审 10:09，版本对齐③过）改计 `len([t for t in tags if ":" not in t])`，判 `5 <= n_content <= 8`，与 dk 核心词口径对称——与上轮期望形态逐字一致。我独立 import `_check_tags` 实测：graph-rag（3 前缀+7 内容词，tags 块直读）→ **0 issue**（上轮误报根治）；meeting-iceberg → 1 warning「内容词 4 个」；env `KDO_TAGS_HARD_DATE=2026-01-01` 翻转 severity=error（两态未动）。
2. **P1-2 活体复现** ✅【实证】：`4179de376^` 0/0 误证已删（返工证据 §3 误证删除声明）；新复现路径 `git show 3051d146e:30_wiki/concepts/ai-collaboration-mindset-shift.md` 我独立物化实测——frontmatter 无 `tags:` 行、type=concept，`_check_tags` 返回 warning「No tags found」——git 历史真实缺陷态复现成立，非合成卡。
3. **P2 标杆卡改判** ✅【实证】：meeting-iceberg tags 块我直读 = 2 前缀（audience:general/scene:meeting）+ 4 内容词（机制/框架/工具/复盘），按 #498 内容词口径 4<5 **本就不合规**——黄药师如实改判「不再作合规样板」正确，补标归内容侧（不改别人卡片，边界守住了）。

**独立加验**：①回归 16/16 我独立复跑通过；②证据 §6 存量量化我独立复算**逐位一致**（受检 2916 / 内容词<5 共 2064 / 5-8 共 840 / >8 共 12 / 零 tags 0）——该数字将驱动内容侧治理排期，已可信；③误报候选 546 vs 上轮我 504 差集=扫描范围，已声明且不影响门禁行为。

**残余风险**（非本单缺陷，移交编排）：09-14 tags 升 HARD 当天，2064 张内容词<5 存量若无治理进度将开始拦截提审——千张级需王语嫣分域排批次（证据 §6 已给规模）。

**通过维度**：溯源验证（修复点全部独立复现）/ TDD 纪律（红4→绿16）/ 证据闭环（存在性核查锚点齐全）/ 边界诚实（如实改判+存量量化）/ 两态机制不变声明。

*欧阳锋 · 2026-09-07 · PASS A-（methodology v2.3 · 复审对照法）*

