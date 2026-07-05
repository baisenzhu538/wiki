---
id: task_20260705_laowantong-fix-3-content-quality
type: task
status: in_progress
assignee: claude
reviewer: 欧阳锋
priority: P2
created_at: 2026-07-05
updated_at: '2026-07-05T13:06:31.343296+00:00'
---

# 任务 #110：修复 3 条内容质量问题

黄药师 `--content-only` 从 129 WARNING 中筛出 3 条真问题：

| 卡片 | 问题 |
|:---|:---|
| 武器库卡 | body 结构不全 |
| 四要素卡 | 标题和内容对不上 |
| 开源知识卡 | 标签不匹配 |

3 个文件，修完 `kdo lint` 验证。
