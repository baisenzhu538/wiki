---
id: 402
assignee: huangyaoshi
status: reviewed
title: 长程任务项目空间试点（P2，黄药师建议书 L3，王语嫣 08-21 采纳）：跨会话持久 workspace——#393 标签体系试点
priority: P2
dependency: []
code_files:
- 90_control/scripts/queue_transition.py
- 90_control/scripts/tests/test_queue_transition.py
- 90_control/PROTOCOL.md
- 60_feedback/tasks/task_20260820_laowantong-tag-system-wave1-workspace/README.md
- 60_feedback/tasks/task_20260820_laowantong-tag-system-wave1-workspace/next-pointer.md
updated_at: '2026-08-20T18:01:02.071599+00:00'
reviewed_by: 欧阳锋
review_date: '2026-08-20'
grade: A
---

# #402 长程任务项目空间试点

## 来源

- 建议书：`60_feedback/designs/design_20260821_lobster-employee-insights.md` L3（必读原文）
- 王语嫣 08-21 裁定采纳（P2）：龙虾员工实证"项目空间隔离上下文污染"；KDO 长程任务目前单会话驱动，跨会话中间态（调研半成品/已排除方向）不在任何地方——王语嫣自己的会话交接也靠锚点重建，痛点真实

## 任务目标

长程任务（预计跨 ≥3 会话）配持久 workspace：`60_feedback/tasks/<task_id>-workspace/`——中间产物、已排除方向清单、上次停在哪指针。**#393 标签体系试点一轮再推广**。

## 执行范围

1. workspace 目录规范：结构约定（in-progress/ excluded/ next-pointer.md 最小三件套），写入出生/任务单模板
2. claim 门禁联动：claim 长程任务时检查 workspace 存在性，不存在则创建并写入"上次停在哪"（#375 claim 门禁扩展点，注意与 #390 自动收口兼容）
3. **试点**：为 #393 建 workspace 并回填当前状态（退回修复中：12 张待补+词表 <5 取值处置——中间态正好现成）
4. 换会话续作实测：新会话只读 workspace 不接失忆恢复就能接续 #393——这是验收动作

## 边界

- 只加 workspace 机制，不动任务状态机语义
- 与 #390 自动收口、#399 复扫工具共存零冲突（workspace 目录纳入流转 commit 范围）
- 不强制存量任务补建（只向前 + #393 试点）
- 完成后 commit（E040）

## 内容价值判断（#375 claim 门禁合规声明）

- 素材性质：机制建设——新增 workspace 目录结构 + claim 门禁联动逻辑；#393 试点回填的是**任务状态快照**（中间态文本），非素材文件
- 去向：全部现有文件原位保留零改动；workspace 为新增目录（`60_feedback/tasks/<task_id>-workspace/`）
- 删除禁令：本任务无任何删除/移动动作；如需删除须逐件老朱亲批（PROTOCOL §7）

## 验收标准

1. #393 workspace 建成，含退回修复中间态
2. 换会话续作实测通过（新会话仅凭 workspace 接续）
3. claim 长程任务自动建 workspace 实测

## 交付

1. 机制 + #393 试点 + 换会话实测记录
2. 送欧阳锋终审

---

## 执行报告（2026-08-21 黄药师）

### 交付物

| 文件 | 说明 |
|:--|:--|
| `90_control/scripts/queue_transition.py`（改） | `ensure_task_workspace()`：claim 时 frontmatter `long_running: true` → 自动建三件套+初始指针；`_git_commit_transition` 触碰集扩展（workspace 文件随流转 commit，与 #390 兼容） |
| `90_control/scripts/tests/test_queue_transition.py`（改） | +3 单测：长程建/非长程跳过/已存在幂等不覆盖指针 |
| `60_feedback/tasks/task_20260820_laowantong-tag-system-wave1-workspace/`（新） | #393 试点：next-pointer.md（终审后状态+W2 指针）+ excluded/（3 个已排除方向+原因）+ README.md（结构规范） |
| `90_control/PROTOCOL.md`（改） | §9.5 长程任务 workspace 规范（追加新节，未覆盖既有内容） |

### 验收对照

| 验收标准 | 实测 | 结果 |
|:--|:--|:--|
| ① #393 workspace 建成，含退回修复中间态 | 建成；回填**终审后实际状态**（目录内最新原则：W1 已 PASS A- 非退回中）——含 next-pointer/excluded/口径四要素 | ✅ |
| ② 换会话续作实测（仅凭 workspace 接续） | 模拟新会话**只读** next-pointer.md → 输出"状态=PASS A-/下一步=W2 回填 573 张/排除方向+原因/复用口径"完整接续摘要 | ✅ |
| ③ claim 长程任务自动建 workspace | 单测 3 个全过（建/跳过/幂等）；`python -m pytest` 10/10 全过；py_compile 通过 | ✅ |

### 设计决策

1. **判定口径**：frontmatter `long_running: true` 显式声明（王语嫣编排时标），不自动猜——避免误建/漏建
2. **幂等**：workspace 已存在则提示不覆盖（保护续作写下的指针）
3. **#390 兼容**：workspace 文件并入流转触碰集 → claim 自动建后同批 commit；后续续作更新随下次流转入档（path-scoped，不裹挟他人在制品）
4. **试点回填用"目录内最新"**：建议书写的"退回修复中"是 08-20 上午快照，#393 当晚已修复终审 PASS A-——按最新状态回填，避免新会话读到过时中间态
5. **模板落点**：无独立任务单模板文件，规范写入 workspace 自带 README（自包含）+ PROTOCOL §9.5（机制索引）

### 遗留

- 出生模板（#263）加 long_running 字段说明——建议随 #403（出生模板前置闸）一并改，避免重复改同一文件（王语嫣裁决）

---

## 欧阳锋终审（2026-08-21 · 建议书 L 系列批量）

**裁定：PASS A。**

**O3 验证**：交付物存在且与执行报告一致（盘点分类/workspace README 判定口径/出生两问模板/证据面清单）——诚实标注为共同亮点（语义判断类不硬上门禁 / 无痛点不硬造建议关闭 / 拦截结论附真实机制证据）；机制兼容（#390 流转入档/#399 复扫挂载）✓
