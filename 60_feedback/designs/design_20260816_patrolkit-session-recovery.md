---
id: design_20260816_patrolkit-session-recovery
title: "K1 PatrolKit 设计：KDO Session 资产自动回收机制"
type: design
status: draft
author: 黄药师
created_at: 2026-08-16
domain: kdo
related: '#326 #324 #338'
source_refs:
  - 00_inbox/AI知识库/楚门-AI知识管理探索营-口述.txt
  - 60_feedback/diagnosis/diag_20260816_ai-knowledge-management.md
  - 60_feedback/tasks/task_20260816_huangyaoshi-patrolkit-session-recovery.md
---

# K1 PatrolKit 设计：KDO Session 资产自动回收机制

> **定位**：#326 巡检（check-mcp-roaming，配置巡检）的自然升级——**从"配置巡检"到"知识资产巡检"**。
> 楚门课程"知识资产雷达"（PatrolKit）的 KDO 落地版：巡查各 Agent Session → 精华自动抽离 → 沉淀为技能进化日志/错误模式库 → 技能迁移。
> **本设计只出方案不改造**（任务书：挂起待 Hermes 迁移会审，不双线开战）。

---

## 一、现状盘点（2026-08-16 实测）

| 资产 | 现状 | 驱动方式 |
|:---|:---|:---|
| daily-context（5 角色共 62 文件） | `agent复盘/<agent>/daily-context/YYYY-MM-DD.md` | 人肉：Agent 会话结束写 + daily-context-save.py 自检 |
| 技能进化日志（6 处） | `agent复盘/<agent>/技能进化日志.md`（Keep/Improve/Add/Stop） | 人肉：会话结束追加一行 |
| 错误模式库（E 系列） | `agent复盘/<agent>/错误模式库.md` + `30_wiki/dark-knowledges/dk-*.md` | 人肉：踩坑当下记录 |
| 成功模式库 | `agent复盘/<agent>/成功模式库.md` | 人肉：成功实践记录 |
| 失忆恢复锚点 | `wiki/20_memory/*-amnesia-recovery.md` | 人肉：状态变化时更新 |

**核心问题**：全部靠 Agent 自觉 + 会话结束强制动作。**Session 里的精华（对话中的金句/判断/模式）在会话结束时如果没有被人工摘录，就永久丢失**——这正是楚门说的"降低对 Session 的依赖"的 KDO 侧缺口。

## 二、巡查目标（Patrol 什么）

**三层巡查对象**：

| 层 | 对象 | 数据源 | 巡查频率 |
|:---|:---|:---|:---|
| L1 复盘资产 | daily-context 新文件、技能进化日志、错误模式库 | `agent复盘/*/`（文件系统） | 每日（日检） |
| L2 Session 记录 | Hermes gateway 会话日志、sessions/ 目录 | `~/.hermes/profiles/*/sessions/` + gateway 日志 | 每周（周检） |
| L3 产物资产 | 任务单执行报告、60_feedback 反馈、30_wiki 新卡 | `60_feedback/` + `30_wiki/`（git 变更） | 每周（周检） |

**设计原则**：L1 是主战场（低成本高价值——文件已结构化）；L2/L3 是延伸（需解析非结构化内容，成本高，先做 L1 验证价值）。

## 三、抽离规则（抽什么）

**从 Session/复盘文本中抽离 4 类资产**：

| 资产类型 | 特征信号 | 沉淀去向 |
|:---|:---|:---|
| **技能进化**（Keep/Improve/Add/Stop 候选） | 文本含"下次""教训""应该""不再""Keep/Improve" | 技能进化日志（追加行） |
| **错误模式**（E 系列候选） | 文本含"踩坑""报错""失败""返工""被拦" | 错误模式库（E 编号）→ 复发 ≥2 自动升级行为牌 |
| **成功模式** | 文本含"成功""有效""验证通过""全过" | 成功模式库 |
| **暗知识**（dk 候选） | 文本含"本质""其实""发现""原来"——且有新认知 | dk 卡候选（送老顽童生产） |

**抽离触发器**（三选一，按优先级）：
1. **事件驱动**（主）：`daily-context-save.py save` 时顺带扫描（会话结束即抽离，热数据）
2. **定时巡检**（辅）：每日 09:07 跑 review-check.py 时附带扫描（兜底冷数据）
3. **手动触发**：`kdo patrolkit scan --agent <name>`（按需）

## 四、沉淀路径（沉到哪）

```
Session/复盘文本
   │  patrolkit 抽离（规则扫描 + LLM 辅助分类）
   ▼
候选资产池（60_feedback/patrolkit/inbox/<asset-type>/）
   │  人审（黄药师/王语嫣周检，低摩擦：只看建议不看原文）
   ▼
确认资产
   ├── 技能进化日志（追加行，自动）
   ├── 错误模式库（E 编号 + 复发计数，自动）
   ├── 成功模式库（追加行，自动）
   ├── 失忆锚点（更新状态节，自动）
   └── dk 卡候选（送老顽童生产，人工）
```

**关键设计**：抽离是"建议模式"不是"直写模式"（对齐 `kdo tag suggest --write` 教训——自动分类曾被跳过人工选值环节）。**PatrolKit 产出候选池 + 人审确认**，低摩擦（人只审建议，不看原文）。

## 五、与现有机制的关系

| 现有机制 | 关系 |
|:---|:---|
| #326 check-mcp-roaming.py | **同框架升级**：check-mcp-roaming = 配置巡检（17/17 PASS）；PatrolKit = 知识资产巡检（下一层）——同目录 `90_control/scripts/`，可复用报告格式 |
| daily-context-save.py | **事件触发器**：save 时顺带 patrolkit scan（复用其存档时机） |
| review-check.py（A/B/C 级） | **质量输入**：C 级复盘 = 无资产可抽（跳过）；A 级 = 高价值抽离源 |
| friction-log | **互补**：friction-log 是"踩坑当下记"；PatrolKit 是"事后从 Session 捞漏网" |
| 失忆恢复锚点 | **沉淀目标**：抽离出的状态变化自动更新锚点 |

## 六、实施路径（挂起方案，待迁移会审后启动）

| 阶段 | 内容 | 依赖 |
|:---|:---|:---|
| P0（设计，本任务） | 本文档落盘 ✅ | 无 |
| P1（改造） | `kdo patrolkit` 命令（scan/inbox/confirm）+ L1 抽离规则 | Hermes 迁移会审结论（不双线开战） |
| P2（延伸） | L2 Session 解析（gateway 日志）+ L3 产物扫描 | P1 验证价值后 |
| P3（自动化） | 每日 09:07 定时巡检 + 周检报告（对齐 08-14 health-check 模式） | P2 稳定后 |

## 七、风险与边界

1. **隐私/权限**：只扫 `agent复盘/` + `60_feedback/`（工厂资产），不扫个人 Hermes session 原始对话（L2 需明确边界）
2. **误报**：抽离是"建议模式"，人审确认前不写入任何资产文件（写错不删，追加修正）
3. **不抢角色**：dk 卡生产仍归老顽童（PatrolKit 只产出候选池）；编排归王语嫣；终审归欧阳锋
4. **与迁移会审解耦**：设计先行不依赖会审；改造执行等会审结论（避免双线开战）

---

*黄药师 · 2026-08-16*
