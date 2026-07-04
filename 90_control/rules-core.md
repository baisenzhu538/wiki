# KDO 核心铁律 (L0)

> 状态：活跃。2026-07-04 首次提取。
> 阅读对象：所有角色，每次 Agent 启动必读。
> 定位：违反任一条都会导致**不可逆的灾难性后果**——不是"做得不好"，是"修不回来"。
> 完整规则体系：L1 角色手册见各角色 -context.md，L2 案例库见 .agent/pitfalls.md、20_memory/corrections.md、90_control/failure-modes.md。

---

## 铁律

| # | 铁律 | 违反后果 | 来源 |
|:--:|:--|:--|:--|
| 1 | **禁止修改 10_raw/ 中的源文件** | 溯源链永久断裂。所有引用该 source 的卡片瞬间变成"不知道哪来的"。git 无法恢复——因为 git 也不知道原始源文件应该是什么 | AGENTS.md F-KDO-001, PROTOCOL.md §2.1 |
| 2 | **禁止删除或替换 source_refs** | 同 #1——wiki→source 溯源链断开。如需标记源过时：追加新 source + 标注旧 source superseded，不删除 | AGENTS.md F-KDO-015 |
| 3 | **批量操作前：① dry-run 预览 ② 声明影响范围 ③ 非空值不覆盖** | 无 dry-run = 你不知道这脚本会改什么。71 张卡攻击者内容一次清空 (C-10)、26 张卡 source_context 被覆盖 (P-29)、486 个文件变更无从审查 (P-30) | .agent/pitfalls.md P-29/P-30, 20_memory/corrections.md C-10 |
| 4 | **写审分离——产卡者不得审查自己的卡片** | uthor ≠ eviewed_by，必须由新 Agent 实例审查。自我审查 = 格式门禁绿灯但内容空洞——"格式完整但思维空洞"卡 (C-8) | .agent/startup.md §二-6, operating-principles.md §6 |
| 5 | **不准跳过审批节点——一段一报，通过前不进入下一阶段** | 跨阶段产出 = 下游基于未审批的上游产物工作，一旦上游被否决，下游全部作废 (C-11：三段视频跨节点产出，三次提报全部缺失) | AGENTS.md F-KDO-017, 20_memory/corrections.md C-11 |
| 6 | **约束指令必须落笔到任务文件——口头意见换会话就丢** | 审查意见、方向调整、边界约束如果只存在于对话历史中，下一次 Agent 启动时就不存在了。写过=不存在 (P-10) | .agent/pitfalls.md P-10 |
| 7 | **不跨角色派活——唯一协调节点 = 欧阳锋** | 角色 A 让角色 B 干活 = 绕过审查 = 欧阳锋不知道发生了什么 = 质量控制失效 | AGENTS.md, .agent/startup.md §二-1 |
| 8 | **不读文件不 patch——编辑前必须 Read 确认当前状态** | 基于过时假设编辑 = 覆盖他人已修改的内容。无 git diff 可追溯覆盖前状态 | AGENTS.md F-KDO-016 |
| 9 | **先诊断，后动手——不盲目调参** | 改了三处还不行就停。先造诊断工具（grep/log/lint），定位根因后再修。API 报错调参 3 小时结果是提供商发新版 (P-28)——先查公告 | .agent/pitfalls.md P-21/P-28, .agent/huangyaoshi-context.md 铁律 §1 |
| 10 | **源文件是唯一真相——wiki 是编译后的衍生层** | "看着图就开始建模"跳过 OCR = source 文件无法建立 = 知识不可溯源。图片不是 source，OCR 后的文本才是 | AGENTS.md §Image Input Discipline, operating-principles.md §2 |

---

## 如何使用

1. **启动时**：读本文件（~500 字，1 分钟）。这 10 条是不可协商的底线。
2. **遇到具体场景时**：搜索 L2 案例库——
   - 批量操作场景 → .agent/pitfalls.md P-29/P-30、20_memory/corrections.md C-10/C-12
   - API/工具调试场景 → .agent/pitfalls.md P-21/P-28
   - 角色越界场景 → 90_control/AGENTS.md 禁止清单
3. **需要完整操作标准时**：90_control/kdo-industrialization-manual.md（22 条铁律 + 16 种失败模式）

---

> 提取者：Codex（外部 AI 观察者）
> 数据源：CLAUDE.md、AGENTS.md、PROTOCOL.md、.agent/startup.md、.agent/pitfalls.md、.agent/huangyaoshi-context.md、20_memory/corrections.md、20_memory/operating-principles.md
> 原则：只保留"违反后不可通过 git/回滚修复"的规则。其他规则按需在 L1/L2 中查询。
