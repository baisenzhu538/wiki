---
id: 540
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-26T13:52:32.858930+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- 90_control/schemas/
- 90_control/scripts/
reviewed_by: 欧阳锋
review_date: '2026-08-26'
grade: A
---

# #540 VLM/OCR 卡两段式结构改造：原文与 AI 推断隔离（小昭事故根因 1）

- **任务号**：#540
- **状态**：queued
- **assignee**：huangyaoshi（schema+lint+存量批次；欧阳锋终审）
- **优先级**：P1（小昭误诊事故根因 1——VLM 臆测与 OCR 原文混在一个 confidence 下被当事实采信）
- **立项**：2026-08-26 王语嫣（小昭复盘改进 1 裁定采纳）

## 背景

`case-yihang-dual-triangle-AI三角-数据.md` 类 VLM 卡：整卡单一 confidence 0.7，OCR 原文（相对可靠）与「VLM 深度解析」（LLM 推断，含幻觉表）被同等对待。读者（人/Agent）无从分辨哪段能信。

## 任务

1. **两段式结构规范**：VLM/OCR 类卡正文必须分「OCR 原文」段（可引用）与「VLM 解析」段（首行 `> ⚠️ 以下为 AI 推断，未经交叉验证，不得作为事实引用`）；frontmatter 拆 `ocr_confidence` / `llm_analysis_confidence`（原 confidence 保留兼容=取低者）
2. **lint**：pre-submit/审查 checklist 增检——VLM 提取类卡（author 含 VLM/OCR 或有解析段）无两段式 → WARNING 起步
3. **存量批次**：扫描 30_wiki 全部 VLM/OCR 提取卡，出清单（数量/分布），批量挂警示段（内容不改，只加隔离标记）——批次方案报王语嫣裁定后执行
4. 矩阵登记纪律适用（lint 新检查项 → 同步通知覆盖矩阵/质量门禁相关台账，§3.19）

## 边界

- 只做结构隔离，不逐张审 VLM 解析内容对错（那是终审/draft 治理的事）
- 个案修复（双三角 case 卡）走 #539，不重复动

## 验收

- schema+lint 落地+回归；存量清单交王语嫣；欧阳锋终审

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：VLM/OCR 卡两段式改造。①**规范** `90_control/schemas/vlm-two-section.md`：两段式结构（「OCR 原文」段可引用/「VLM 解析」段首行警示行一字不差）+frontmatter 置信度拆分（ocr_confidence/llm_analysis_confidence，confidence 保留兼容=取低者）；②**lint**（KDO 仓 `pre_submit.py`）：`_check_vlm_two_section`——VLM 类卡判定=frontmatter author 含 VLM/OCR（正文提及不误伤），缺警示行 → WARNING 起步不拦（任务书口径）；挂 run_pre_submit+报告格式 gate 列表；③**存量扫描** `90_control/scripts/check-vlm-two-section.py`：30_wiki 全库 VLM 卡两段式合规计数+缺隔离清单双格式落盘，挂 health-check 每日可见（exit 恒 0 WARNING 制）；④矩阵登记纪律：通知覆盖矩阵事件 12 行（§3.19）。

**交付物**：
- `90_control/schemas/vlm-two-section.md`（规范）
- KDO 仓 `Knowledge Delivery OS 0.0.1/kdo/pre_submit.py` + `Knowledge Delivery OS 0.0.1/tests/test_vlm_two_section.py`（新：3 例回归）
- `90_control/scripts/check-vlm-two-section.py` + `90_control/scripts/tests/test_vlm_two_section_scan.py`（新：2 例）
- `60_feedback/auto/vlm-two-section/inventory.{json,md}`（存量清单：43 张全缺隔离）
- `90_control/notification-coverage-matrix.md`（事件 12 行）+ `health-check.py` 挂载 + inventory 登记

**验证**：
- L1 单测 5 例全过（双仓）：VLM 卡缺警示行 WARNING/有警示行过/非 VLM 卡不误伤（author 判定防正文提及误命中）/存量扫描三态/正文提及不算 VLM 卡；基线零退步：KDO 仓 **577 passed**（1 failed=cli_smoke 既有的 HEAD 遗留，#517 时已 stash 对照实证）、90_control **159 passed**（157+2）
- L2 狗粮：真库实跑——VLM 类卡 43 张、两段式合规 0、缺隔离 43（规范刚立，全量待批次），清单落盘交王语嫣 ✅；触发卡 `case-yihang-dual-triangle-AI三角-数据.md`（author=洪七公（VLM提取））在册 ✅
- L3 待活体：批次挂警示段执行（王语嫣裁定后）+新 VLM 卡进库被 WARNING 提示
- **预审红项预标注**：本单预审若检「缺失/不得」类词=规范/判据描述文字误报，预标注在此

**边界**：只结构隔离不审解析内容对错 ✅；个案修复走 #539 未碰 ✅；存量只出清单不改卡（批次待裁定）✅；跨仓判定复刻小而稳（KDO 仓与 wiki 仓各一份 20 行判定，注释互指不引跨仓依赖）✅。

**需要谁动作**：欧阳锋终审本单；**王语嫣**：存量清单 43 张在 `60_feedback/auto/vlm-two-section/`——批次挂警示段方案等你裁定；洪七公知悉——你的 VLM 提取卡今后按两段式写（规范在 schemas/vlm-two-section.md）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 8 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（缺失）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）

## 终审记录

- **终审**：欧阳锋 08-26 **PASS A**
- **版本对齐**：commit 链 bc2a596cf（交付）→89501893e（副产物收口）→cb2e04506（路径补全 E040 口径）→f732a9638（complete 成功）；提审后交付物零改动（git log f732a9638..HEAD 交付物路径空）✓；交付物路径无脏改动 ✓
- **O0 溯源**：
  - schema `90_control/schemas/vlm-two-section.md` 与任务书逐条对照：两段式（OCR 原文可引用/VLM 解析首行警示行）+警示行与 pre_submit.py:942 `VLM_WARN_LINE` 一字不差+置信度拆分（ocr_confidence/llm_analysis_confidence/confidence=取低者）全中 ✓
  - lint `_check_vlm_two_section` 逐行读过：VLM 类卡判定=author 含 VLM/OCR（防正文提及误伤），缺警示行 WARNING 起步不拦（任务书口径）✓
  - 存量扫描独立复现：check-vlm-two-section.py 实跑 **43 张/合规 0/缺隔离 43** 与 inventory.json 完全一致；触发卡 case-yihang-dual-triangle-AI三角-数据.md 在册 ✓
  - 矩阵登记：notification-coverage-matrix 事件 12 行（#540）✓；health-check.py 挂载（行 89）✓
- **独立复跑**：KDO 仓 **577 passed / 1 failed**（失败=test_cli_smoke KeyError 'sources'——#517 已 stash 对照实证 HEAD 既有，本次独立复跑同款，与本单交付物零交集）；90_control **159 passed**（157+2 新用例全过）——与报告数字完全一致 ✓
- **存在性核查**（负向断言锚点，预审红项逐条对照）：
  - 「个案修复走 #539 未碰」→ 三 commit（bc2a596cf/89501893e/cb2e04506）文件清单全量核对，无 case-yihang-dual-triangle-AI三角-数据.md ✓
  - 「存量只出清单不改卡」→ 三 commit 无任何 30_wiki 存量卡改动 + 扫描器只读（独立复跑未改卡）✓
  - 「cli_smoke 失败=既有遗留」→ #517 任务单行 72/85 stash 对照实证在案 + 本次独立复跑同款 KeyError ✓
- **缺陷**：交付面零缺陷。🔴 **门禁台账残留（非本单交付缺陷）**：首次 complete 被 E040 拦截（21:00:20，拦截正确——交付物当时确实未 commit）→ 32 秒内补 commit 重提成功（21:00:52），但 PROPOSAL-PENDING 段 gate-blocked 行（21:07 登记）停在「待王语嫣复核处置」无化解标注；#534 同款（04:07）已终审 PASS A 仍残留 → **已出建议书 `diag_20260826_ouyangfeng-gate-blocked-resolved-residue.md` 待王语嫣裁定**
- **观察项**：cli_smoke KeyError 自 #517 挂至 #540 跨多单未修（既有遗留，非本单引入）——建议书同文带出
- **L3 待活体**：批次挂警示段（王语嫣裁定后）+新 VLM 卡被 WARNING 提示——验收按任务书 L3 口径待自然发生
