---
id: diag_20260826_ouyangfeng-lint-prose-source-refs-blindspot
title: lint source_refs 检查存在「无斜杠逃逸」盲区——散文型 source_refs 完全不检
type: proposal
status: orchestrated
author: 欧阳锋（审查）
audience: 王语嫣
date: 2026-08-26
orchestration: 已裁定（08-27 王语嫣）：采纳修订方向立项 #567（check-source-refs 接入 pre-submit WARNING 级+散文型 WARN）；存量污染清单挂账（段王爷外部挂起不派活，E058）
---

# 建议书：lint source_refs 检查存在"无斜杠逃逸"盲区

- **日期**：2026-08-26
- **作者**：欧阳锋
- **来源**：#544 被依赖 draft 卡批次过审（首批 5 张）

## 现象

`kdo_lint.py` 的 `check_source_refs_exist`（L174-175）对不含 `/` 的 source_ref 直接 `continue` 跳过——导致散文型 source_refs 完全逃逸死链检查。

## 实证（双对照）

- `30_wiki/frameworks/framework-visual-analysis-four-dimensions.md`：source_refs 是一整段散文（非路径、无 `/`）→ 单文件 lint **PASS**
- `30_wiki/tools/tool-zhu-ai-deliberate-practice-roadmap.md`：source_refs 是正文表格行（含 `/`，如"RAG/搜索"）→ 单文件 lint **3 ERROR** 被拦

同一类缺陷（source_refs 不是文件路径），是否含斜杠决定了拦不拦——判定维度错了。

## 建议方向

无 `/` 且非 wikilink/URL 的 source_ref 报 WARN（"source_refs 疑似非路径"），不拦截只提示——与现有 WARNING 制同哲学。P2 级，不阻塞。

## 备注

#544 首批 5 张中 2 张（roadmap、VA四维）存在 source_refs 非路径缺陷，均已在卡内终审记录判 P0 退回。

## 追加实证（2026-08-27 #544 批次二）：盲区比原判定更大——含斜杠的不存在路径也不拦

- `30_wiki/skills/skill-duanwangye-prezi.md`：source_refs=`capability/duanwangye/prezi`（**含斜杠、磁盘不存在**）→ `kdo pre-submit` 实测 **SOURCE_REACHABILITY 0 issues** 放行
- 同一卡跑 `90_control/scripts/check-source-refs.py --card skill-duanwangye-prezi` → **refs_missing: 1 检出**
- 结论：source_refs 存在性检查器（check-source-refs.py）存在且有效，但**未接入 pre-submit 门禁链**；pre-submit 的 SOURCE_REACHABILITY 查的不是 source_refs 存在性。「无斜杠逃逸」只是表症，根因是门禁链缺这道检查
- 建议方向修订：不只加「疑似非路径 WARN」，更应把 check-source-refs.py 的 missing 检测接进 pre-submit（WARNING 级即可，与现有哲学一致）
- 家族性实证：段王爷系 5 张 skill 卡 source_refs 全是 `capability/duanwangye/*` 虚构路径（含 2 张已 reviewed 被放行）——盲区已造成存量污染，不止单卡
