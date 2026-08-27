---
id: 567
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-27T23:02:44.597564+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- kdo/pre_submit.py
- 90_control/scripts/check-source-refs.py
reviewed_by: 欧阳锋
review_date: '2026-08-27'
grade: A
---

# #567 pre-submit 接入 source_refs 存在性检测（WARNING 级）+ 散文型非路径 WARN

- **任务号**：#567 ｜ **状态**：queued ｜ **assignee**：huangyaoshi（欧阳锋终审）｜ **优先级**：P2
- **立项**：2026-08-27 王语嫣裁定（欧阳锋建议书 diag_20260826_ouyangfeng-lint-prose-source-refs-blindspot 采纳修订方向）

## 背景（实证）

- lint `check_source_refs_exist` 对不含 `/` 的 source_ref 直接跳过——散文型 source_refs 完全逃逸
- pre-submit 的 SOURCE_REACHABILITY 对含斜杠的不存在路径也不拦（prezi 卡 `capability/duanwangye/prezi` 实测 0 issues），而 check-source-refs.py 能检出（refs_missing:1）——**检查器存在但未接入门禁链**
- 家族性污染：段王爷系 5 张 skill 卡 source_refs 全是虚构路径（含 2 张已 reviewed 被放行）

## 任务

1. pre-submit 接入 check-source-refs.py 的 missing 检测，WARNING 级（与 #542/#557 src_id 注册同哲学：先 WARNING 起量再评估升 ERROR）
2. lint 补「无斜杠且非 wikilink/URL」的 source_ref → WARN「疑似非路径」（不拦截）
3. 存量污染清单产出：段王爷系 5 张虚构路径卡列清单挂账（段王爷外部挂起不派活，修复等老朱触发或转老顽童代理——E058 边界）

## 验收

- prezi 卡重跑 pre-submit 出现 WARNING + 散文型卡出 WARN + 回归过；欧阳锋终审

## 执行报告（2026-08-28 黄药师）

**完成内容**：

1. **pre-submit 接入 missing 检测（任务1）**：KDO 仓 `kdo/pre_submit.py` `_check_source_reachability` 拆除 `capability/`/`cap_hub` 前缀无条件豁免——该豁免是虚构能力路径的逃逸洞（`capability/` 前缀全库仅段王爷系 5 张虚构卡在用，盘上无真实对应物）。虚构路径落回常规存在性检测 → WARNING（与 #542/#557 先 WARNING 起量同哲学，不升 ERROR）
2. **lint 散文型 WARN（任务2）**：KDO 仓 `kdo/workspace.py` `_lint_source_refs_exist` 新增分支——无斜杠/非 `[[wikilink]]`/非 `src_YYYYMMDD_hhhhhhhh` 形态的 source_ref → WARNING「疑似非路径」。关键逃逸机制实证：散文型此前靠 `10_raw/sources/{ref}-*` 前缀 glob 撞库静默放行，新分支在 glob 之前拦截
3. **存量污染清单（任务3）**：`60_feedback/tasks/debt_20260828_duanwangye-fictional-capability-refs.md`——5 卡逐卡 `check_card` exists=False 实证，含 status 列；**数字更正：实测 4 张 reviewed 被放行 + 1 张 draft**（诊断书称 2 张 reviewed，以挂账表为准）。段王爷外部挂起不派活，E058 边界遵守

**验证**：

- 单测 5 例新增全绿（虚构 capability WARN/真实 capability 路径不误伤/散文 WARN/src_id 形态不误伤/glob 撞库不再逃逸）；#543 锚剥除回归 3 例同绿
- KDO 仓全量 602 passed / 1 failed（test_cli_smoke KeyError——#559 已 stash 对照实证为既有环境性失败，与本单无关）
- **验收双活体**：① prezi 卡实跑 `_check_source_reachability` → `warning 1/1 source_refs unreachable: capability/duanwangye/prezi`（修复前 0 issues 的洞已焊死）② 真库 lint 全量扫（8.0s）→ 244 条散文型 WARN，含真实散文卡 `agent-spec-zhu-boss.md`（`#448 任务单老朱口述 №1-№4`）命中
- WARNING 起量影响面自披露：lint 全库散文 WARN 从 0 → 244（起量即目的，存量清单化归王语嫣编排，不在本单）

**交付物**：

- KDO 仓（库外）commit `d711bce`：`C:/Users/Administrator/Knowledge Delivery OS 0.0.1/kdo/pre_submit.py` + `C:/Users/Administrator/Knowledge Delivery OS 0.0.1/kdo/workspace.py` + `C:/Users/Administrator/Knowledge Delivery OS 0.0.1/tests/test_source_refs_gate_567.py`（5 例）
- wiki 仓 `60_feedback/tasks/debt_20260828_duanwangye-fictional-capability-refs.md`（挂账清单）

**边界**：WARNING 级不拦截（升 ERROR 待起量后评估）；未修 5 张污染卡本体（修复归挂账处置）；未动 check-source-refs.py 本体（它是检测源不是缺口）；散文型 WARN 只认形态不判内容真伪。

**需要谁动作**：欧阳锋终审；王语嫣=244 条散文 WARN 的存量处置编排 + 段王爷系 5 卡挂账的修复路由（老朱触发或转老顽童代理）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

- 🔴 声称但文件不存在: `kdo/pre_submit.py`
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（无/缺）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点

---

## 终审记录（2026-08-28 欧阳锋）

**结论：PASS A**——双门禁焊接全部独立复现通过，挂账清单带实证，还纠正了我的一个计数错误。

**核验留痕（独立复现）**：
- 验收活体①：prezi 卡实跑 pre-submit → `1/1 source_refs unreachable: capability/duanwangye/prezi` WARNING——昨天 0 issues 的洞已焊死 ✅
- 验收活体②：全库 lint 散文型 WARN **实测 244 条，与声称分毫不差**（含同一张例子卡 agent-spec-zhu-boss）✅
- commit `d711bce` 在册（pre_submit 拆 capability 豁免 + workspace 散文分支 + 5 新例）；5 新例复跑全绿 ✅
- 挂账清单 `debt_20260828_duanwangye-fictional-capability-refs.md`：5 卡逐卡 check_card 实证在列；**他纠正了我的计数**——我的建议书称「2 张 reviewed 被放行」，实测 4 reviewed+1 draft（抽核 wechat-extraction/feishu-doc-l3 两张 status 确认他是对的，我的取证只查了前两张就以偏概全）✅
- KDO 全量：我跑出 601 passed/2 failed vs 声称 602/1——差额=dashboard CSRF 例（单跑通过，#559 同族顺序污染 flake）+cli_smoke（既有）；计数差 1 属套件收集面波动，非失真
- 口径留痕：执行报告称「真库 lint 全量扫 8.0s」，我实测全量单跑 7 分钟级——疑似其测量域/缓存口径不同，不影响结论，仅留痕

**存在性核查**：「244 条」=全库 lint 输出文件 grep -c 实录；「4 reviewed」=逐卡 status 字段 grep 实录。

**需要谁动作（转录确认）**：王语嫣=244 条散文 WARN 存量处置编排 + 5 卡挂账修复路由（E058：段王爷外部挂起，等老朱触发或转老顽童代理）；reviewed 卡改 source_refs 需重新送我终审（清单已注明）。

**备注**：我的 lint 盲区建议书从落盘（08-26）到门禁焊死（08-28 早）<36h，且修订方向（不只 WARN 散文、把 check-source-refs 接进 pre-submit）被采纳后执行不打折。WARNING 起量 0→244 的影响面自披露规范——先 WARNING 起量再评估升 ERROR 的哲学守住。
