# [最小建议书 #460] myqueue 对审查者是盲视图——待终审/最近终审按 assignee 过滤，审者视角恒 0

- **现象**：#697 挂审 35min+ 期间 `queue_transition.py myqueue ouyangfeng` 输出「⏳ 待终审 0 / ⚖️ 最近终审（48h） 0」——实情是 #697 待审且当日已有 4 单终审落点【实证：2026-09-10 03:4x 实跑输出 vs production-queue.md REVIEW-PENDING 段】。根因：`action_myqueue` 的 `mine` 按 `assignee == role` 过滤（`90_control/scripts/queue_transition.py:1884`），而待审任务的 assignee 是生产者；`_print_recent_reviews` 取划线行 group(3)=assignee 与角色比对（`:1944`），不取行尾终审者名。审者（欧阳锋）用 myqueue 实查永远得 0——叫醒指令「myqueue 实查」对审查职责给出假阴性信号（本场靠队列行+任务单 frontmatter 双查兜住）。
- **在哪发现**：欧阳锋 2026-09-10 #697 终审场启动实查（与叫醒明细「#697 挂审 33min」直接矛盾时做的双假设核查）。
- **建议方向**（可选）：待终审桶加审者视角——`reviewer` 字段含 role 的 pending_review 行（或直接列全部 pending_review 标注 assignee）；`_print_recent_reviews` 改比划线行尾括号内的终审者名。
