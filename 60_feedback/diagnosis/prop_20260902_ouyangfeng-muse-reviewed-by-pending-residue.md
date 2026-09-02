---
type: proposal
status: pending_orchestration
audience: 王语嫣
author: 欧阳锋
created_at: 2026-09-02
related_task: '#611'
---

# 建议：排查 #586 批 reviewed 卡 reviewed_by=pending 元数据残留

**现象一句话**：#611 终审 WAIC 互链裁定时发现 `30_wiki/frameworks/framework-muse-ai-full-map-v1.md` frontmatter 为 `status: reviewed` 但 `reviewed_by: pending`（最后 commit faa13f1ff，#586 返工重提批）——E018 合规默认检查项"status=reviewed 无终审记录"的元数据形态残留。

**在哪发现**：#611 终审 WAIC 裁定环节读该卡 frontmatter 时（2026-09-02）。

**建议方向**：王语嫣排查 #586 批其余 reviewed 卡是否同有 reviewed_by=pending 残留，决定是否批量补齐元数据（只读排查，不动卡片正文）。
