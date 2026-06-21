---
id: "corr_20260621_管线违规_supplement卡"
type: "correction"
created_at: 2026-06-21
author: "王语嫣"
severity: "medium"
status: "open"
---

# 管线违规：supplement 卡直接写入 30_wiki

## 违规描述

`30_wiki/frameworks/framework-yitang-research-weapon-supplement-2026.md` 由老顽童于 2026-06-21 直接写入 `30_wiki/`，跳过了王语嫣（诊断）→ 欧阳锋（审核）管线。

## 违规详情

| 项目 | 值 |
|:---|:---|
| 违规卡 | `framework-yitang-research-weapon-supplement-2026` |
| 写入位置 | `30_wiki/frameworks/` |
| 写入时间 | 2026-06-21 |
| 写入人 | 老顽童 |
| 正确管线 | 00_inbox → 王语嫣诊断(60_feedback/diagnosis/) → 欧阳锋审核 → 老顽童ingest → 30_wiki/ |
| 实际路径 | 老顽童 → 30_wiki/ （跳过诊断+审核） |

## 附加问题

除了管线违规，该卡还存在 **F-EQG-001（框架合并癖）** 问题：将五个独立知识域（OSINT/Agent原生/替代数据/Google Dorking/媒体验证）合并为一张复合大卡。

## 建议修正

1. 欧阳锋审核 `diag_20260621_调研武器库五大盲区诊断.md` 中的准入清单
2. 老顽童将 supplement 卡从 `30_wiki/` 移除（或标记为 draft）
3. 按 `task_20260621_调研武器库盲区补充.md` 的 Wave 计划重建为 17 张细粒度卡片
4. 重建后经欧阳锋逐卡审核，再由老顽童正式 ingest

## 相关文件

- 诊断报告：`60_feedback/diagnosis/diag_20260621_调研武器库五大盲区诊断.md`
- 生产任务：`60_feedback/tasks/task_20260621_调研武器库盲区补充.md`

---

*这是王语嫣的独立判断——不代表欧阳锋的最终审核结果。*
