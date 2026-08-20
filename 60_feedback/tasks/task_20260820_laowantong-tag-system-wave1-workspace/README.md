# 长程任务 workspace 规范（#402）

> 长程任务（预计跨 ≥3 会话）配持久 workspace，与任务单同目录：
> `60_feedback/tasks/<task_id>-workspace/`。

## 最小三件套

| 路径 | 内容 |
|:--|:--|
| `next-pointer.md` | **上次停在哪 + 下一步**——换会话续作只读此文件即可接续 |
| `in-progress/` | 中间产物（调研半成品、临时清单、未定稿草稿） |
| `excluded/` | 已排除方向（附排除原因，防止换会话重蹈） |

## 机制

- **自动创建**：任务单 frontmatter 声明 `long_running: true` → claim 时 queue_transition 自动建三件套并写初始指针
- **自动入档**：workspace 文件随 #390 流转自动 commit（path-scoped，不裹挟他人在制品）
- **换会话续作**：新会话只读 `next-pointer.md`（+ in-progress/ 按需）即接续，不依赖失忆恢复锚点
- **只向前**：不强制存量任务补建；试点：#393（本 workspace）

## 试点

#393 标签体系（W1 已终审 PASS A-，本 workspace 回填终审后状态 + W2 指针）。
