---
id: 543
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-26T16:44:59.517035+00:00'
version: v0.2
instance: huangyaoshi
code_files:
- 90_control/scripts/check-source-refs.py
- 90_control/scripts/health-check.py
- 90_control/scripts/tests/test_check_source_refs.py
- 90_control/notification-coverage-matrix.md
- 60_feedback/analysis/source-refs-health-latest.md
- 60_feedback/analysis/source-refs-health-latest.json
- 60_feedback/analysis/source-refs-debt-governance-20260827.md
- Knowledge Delivery OS 0.0.1/kdo/pre_submit.py
- Knowledge Delivery OS 0.0.1/tests/test_pre_submit_source_anchor.py
reviewed_by: 欧阳锋
review_date: '2026-08-26'
grade: A-
---

# #543 source_refs 死引治理：1024 条缺失存量 + 扫描器挂例行 + json 输出修复

- **任务号**：#543
- **状态**：queued
- **assignee**：huangyaoshi（lint 挂载+报告落盘；治理批次方案报王语嫣裁定）
- **优先级**：P1（ADUCIT 事件深挖实证：全库 4224 条路径类 source_refs 中 1024 条文件缺失=24% 死引率，原稿在 inbox 而卡片引虚空——「找不到原稿反复索要的根）
- **立项**：2026-08-26 王语嫣（老朱追问「原稿就在，为什么找不到」）

## 背景

check-source-refs.py 扫描器早已存在，但**没进任何例行**：不跑、不报、不拦。08-26 王语嫣实跑：2877 卡/5908 条 source_refs，1024 条文件缺失+8 条已知污染引用；src_id 类引用（如 src_20260531_ai-data-lecture-02）连 source_id_map.json 都未注册。工具存在≠在回路里——与通知矩阵教训同构。

## 任务

1. **修 json 输出 bug**（--json 输出 line 2245 格式错误，agent 消费面断的）
1.5. **剥 `:行号` 锚（同族双检查器，08-26 王语嫣裁定补入）**：`resolve_path` 直接拼路径不剥 `path:NN` 后缀 → 带行号锚引用全被误判缺失，**1024 条死引数字本身被污染**（ADUCIT 卡 2 条带锚引用实证在内）。本脚本修复 + KDO 仓 `pre_submit.py::_check_source_reachability`（907 行同款 bug，欧阳锋建议书 diag_20260826_ouyangfeng-source-refs-line-anchor-unreachable）同口径修复——先剥锚再判存在，行号正确性不在检查器职责。回归用例：带行号锚卡 0 误报 + 真缺失文件仍报。修复后重跑全量扫描，报「行号锚误报挤占量」（1024 里有多少是误报）
2. **报告落盘+挂例行**：扫描报告落 `60_feedback/analysis/`，挂周例行（或随 daily-audit-digest），缺失数>阈值报警
3. **死引分批治理方案**：1024 条按域/卡片 status 聚类出报告，参照 #426 分批模式提治理方案（reviewed 卡优先——已审卡带死引=终审漏项）；方案报王语嫣裁定后分批执行
4. **inbox 未归档检测**：死引中指向 00_inbox 的（原稿在 inbox 未入 raw 型，ADUCIT 同款）单独聚一类——这类修复成本最低（归档即可，不用补内容）
5. §3.19：新例行信号→同步通知覆盖矩阵

## 边界

- 本单只出报告+挂例行+提方案，不直接批量修卡（治理批次裁定后另立执行单）
- src_id 注册表（source_id_map.json）补登记机制是否在 pre-submit 挂钩，随方案一并报裁

## 验收

- json 输出修复实测；报告落盘+例行挂载证明；分类治理报告交王语嫣；欧阳锋终审


## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：source_refs 死引治理四件套。①**json bug 修复**（`check-source-refs.py`）：根因=`io.TextIOWrapper(sys.stdout.buffer)` 在无 .buffer 的 agent 宿主 stdout 下 AttributeError 崩溃→JSON 零输出；改 `sys.stdout.reconfigure` try/except 兜底；**顺带修真 bug**：`scan()` 忽略 vault_root 参数用模块级 WIKI_DIR（测试/多库场景扫错库）；②**行号锚剥除（双检查器同口径）**：`strip_line_anchor`（`path:NN`/`path:NN-MM` 剥除，Windows 盘符不误伤）挂入本脚本 `resolve_path` + KDO 仓 `pre_submit.py::_check_source_reachability`（re.sub 同口径）；剥锚后重扫：**挤占量仅 2 条（0.2%）**——1024 口径基本未被锚污染，死引是真实缺失；③**报告落盘+挂例行**：`--report-dir` 落 `60_feedback/analysis/source-refs-health-latest.{md,json}`（含治理聚类段），挂 health-check 每日 02:07 例行；`--max-missing 1024/--max-contaminated 8` 阈值制——超基线=新增才 FAIL，存量不扰（治理后王语嫣裁定下调）；④**聚类治理报告**：`60_feedback/analysis/source-refs-debt-governance-20260827.md`——934/1024（91.2%）指向 00_inbox（归档即修，成本最低）、reviewed 卡 441 条（终审漏项优先）、business-formula+conversion-rate 两域占 51%（疑似同源批量入库事故）；⑤§3.19：矩阵事件 14 行。

**交付物**：
- `90_control/scripts/check-source-refs.py`（json 修复+锚剥除+聚类+阈值）
- `90_control/scripts/health-check.py`（例行挂载+阈值参数）
- `90_control/scripts/tests/test_check_source_refs.py`（8 例回归）
- `90_control/notification-coverage-matrix.md`（事件 14 行，§3.19）
- `60_feedback/analysis/source-refs-health-latest.md` + `60_feedback/analysis/source-refs-health-latest.json`（报告落盘）
- `60_feedback/analysis/source-refs-debt-governance-20260827.md`（聚类治理报告→王语嫣）
- `Knowledge Delivery OS 0.0.1/kdo/pre_submit.py` + `Knowledge Delivery OS 0.0.1/tests/test_pre_submit_source_anchor.py`（KDO 仓同款锚修复+3 例，commit 0175a89）

**验证**：
- L1 单测：wiki 侧 8 例全过（锚剥除四态/挤占量统计/StringIO 宿主 json 不崩/阈值三态/落盘含聚类）；KDO 侧 3 例全过（锚定存在零误报/锚定缺失仍报/裸缺失仍报）
- 基线零退步：90_control **167 passed**（159+8）；KDO 仓 **580 passed**（577+3），1 failed=test_cli_smoke 既有 HEAD 遗留（#540 同口径）
- L2 狗粮：真库全扫 2878 卡/5910 条实测——剥锚后缺失 1024、锚引用 2 条全存活、inbox 簇 934 条/319 卡、聚类透视落盘；阈值实跑 exit=0（1024 不超基线）
- L3 待活体：health-check 02:07 例行首跑（本轮已手动全量验证 source_refs 项挂载）
- **预审红项预标注**：本单预审若检「缺失/不得」类词=报告/方案描述文字误报，预标注在此

**边界**：未批量修卡（治理待裁定另立执行单）✅；src_id 注册表挂钩仅报裁未实施 ✅；grep 裸检索不动 ✅。

**需要谁动作**：欧阳锋终审本单；**王语嫣**：治理方案 `60_feedback/analysis/source-refs-debt-governance-20260827.md` 等你裁定（批次 A inbox 归档口径 + src_id 注册表是否挂 pre-submit）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 9 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（缺失）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）

---

## 终审记录（2026-08-27 凌晨 · 欧阳锋 · PASS A-）

**结论：PASS A-——双仓交付全量独立复核通过，1 处口径小遗漏（观察项不阻断）。**

**版本对齐三问**：①入仓 ✅——wiki 仓 404893a9b+9754ce414（00:24）、KDO 仓 0175a89（00:23）双仓在链；②生效 ✅——health-check 为每日 02:07 定时脚本（非长驻进程，fresh load 无 #541 类旧码问题），L3 待活体声明合理；③对齐 ✅——HEAD 81282af65 在交付之后。

**逐项复核（全部亲跑，非采信报告）**：
- 双仓锚剥除同口径 ✅：wiki `strip_line_anchor`（check-source-refs.py L81，regex `^(.*?):\d+(?:-\d+)?$`，盘符安全）× KDO `pre_submit.py`（0175a89 diff 实证，先剥锚再判存在）——我行号锚建议书的诊断被准确修复
- 测试三数全中：90_control **167 passed**（亲跑）✅；KDO 仓 **580 passed + 1 failed**（test_cli_smoke 既有遗留——该测试最后改动 8bc5645 与本单文件不相交，遗留声明成立）✅
- json 输出修复实测 ✅：--json 输出 414KB 合法 JSON（stats/contaminated/missing/clusters 四键），UTF-8 零替换字符——agent 消费面恢复
- 统计口径全对：2878 卡/5910 条/缺失 1024/污染 8/冒号锚 2 条全存活 ✅；inbox 簇 934 条 ✅；聚类三主线与治理报告一致 ✅
- §3.19：矩阵事件 14 行在案（L27）✅；health-check 挂载（L74-76 阈值 1024/8）✅
- 预审 🔴 预标注核验：「缺失」为报告主题词非负向断言，预标注成立 ✅

**观察项（🟠 不阻断，TODO 级）**：`strip_line_anchor` 只剥冒号锚（`path:NN`），**空格锚（`path L14`/`path L946-1278`）未剥**——亲测全库 15 条空格锚被计入缺失（样例 `00_inbox/解放思想探索营/…口述.txt L14` 文件实测存在）。
**存在性核查**：计数方法=json 落盘文件 `missing_source_cards` 逐条 regex `\s+L\d+(-\d+)?$`；文件存在性用 ls 逐一抽验；对照组=kdo_lint.py L186-189 已有④号空格锚剥除模式（两检查器口径不齐）。
**影响**：真实挤占量 17 条（1.7%）而非报告的 2 条（0.2%）——结论方向不变（死引主体仍是真实缺失），但治理清单里有 15 条假死引，批次 A 执行前宜补剥空格锚重扫。已记入观察项，随治理批次裁定一并处理，不另立建议书（单工具缺陷，属本单后续治理范围）。

**等级理由**：交付物全验通过+跨仓同口径+证据链完整，唯挤占量口径小遗漏（2→17）+扫描器残留盲区各计一处，A-。
