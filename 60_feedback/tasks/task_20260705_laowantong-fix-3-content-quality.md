---
id: task_20260705_laowantong-fix-3-content-quality
type: task
status: pending_review
assignee: claude
reviewer: 欧阳锋
priority: P2
created_at: 2026-07-05
updated_at: '2026-07-05T13:22:00.805476+00:00'
---

# 任务 #110：修复 3 条内容质量问题

黄药师 `--content-only` 从 129 WARNING 中筛出 3 条真问题：

| 卡片 | 问题 |
|:---|:---|
| 武器库卡 | body 结构不全 |
| 四要素卡 | 标题和内容对不上 |
| 开源知识卡 | 标签不匹配 |

3 个文件，修完 `kdo lint` 验证。


## 执行报告

3/3 pre-submit PASS。武器库卡补 section、四要素卡改标题、开源知识卡修标签。
