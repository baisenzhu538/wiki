---
id: 567
assignee: huangyaoshi
status: queued
updated_at: '2026-08-27T23:55:00+00:00'
version: v0.1
instance: huangyaoshi
code_files:
  - kdo/pre_submit.py
  - 90_control/scripts/check-source-refs.py
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
