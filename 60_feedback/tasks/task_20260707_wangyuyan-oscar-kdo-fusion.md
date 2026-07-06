---
id: task_20260707_wangyuyan-oscar-kdo-fusion
type: task
status: queued
assignee: 老顽童
reviewer: 欧阳锋
priority: P0
created_at: 2026-07-07
updated_at: 2026-07-07
source_refs:
- 00_inbox/OSCAR-KDO-外部探索融合方案.md
- 30_wiki/frameworks/framework-yitang-oscar-research.md
- 40_outputs/capabilities/skills/business-research/SKILL.md
related:
- '[[framework-yitang-oscar-research]]'
- '[[method-kdo-external-exploration-sop]]'
---

# 任务 #127：OSCAR-KDO 融合——框架卡补齐 + 桥接卡 + SOP v2

## 来源

飞书 Agent 完整融合方案：KDO SOP 是 R-heavy（后重前轻），OSCAR 是 O/S/C-heavy（前重后轻）。融合 = OSCAR 的前端设计补 KDO 的前三步 + KDO 的后端验证作为增强版 R。

## 产出

### 1. OSCAR 框架卡补齐（原 #124）

- 补齐 `framework-yitang-oscar-research` 和 `business-research-skill-oscar-13-weapon-system` 两张卡的 `src_unknown` 占位
- status: enriched → reviewed

### 2. OSCAR-KDO 桥接卡（Phase 2）

新卡：`tool-oscar-kdo-external-exploration`——一堂 OSCAR 在 KDO 外部探索中的具体落地

核心内容：融合对照表——

| OSCAR | KDO SOP | 注入内容 |
|:---|:---|:---|
| O·锁定目标 | **新增** | 四类型判断（选择/解答/设计/竞争）+ "了解一下"拒绝 |
| S·缩小范围 | 增强 | 四层面标注（宏观/中观/微观/单点）+ 剥离清单 |
| C·罗列清单 | **新增** | 关键词清单 + 来源类型 + 门控条件 |
| A·获取情报 | 增强 | 公开层+半公开层，有条件触发 |
| R·正确归因 | 保留增强 | KDO六层比对+四路Attacker+准入清单（KDO超越OSCAR） |

### 3. SOP v2（原 #125 升级）

`method-kdo-external-exploration-sop` v1 → v2：6 步 OSCAR 注入版

## 验收

- OSCAR 卡 src_unknown 清零，status→reviewed
- 桥接卡含完整融合对照表 + 六步 SOP
- SOP v2 含 O/S/C/A/R/出诊断
- `kdo pre-submit` 全部 PASS
