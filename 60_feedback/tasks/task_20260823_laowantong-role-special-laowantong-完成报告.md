---
id: task_20260823_laowantong-role-special-laowantong-完成报告
title: "#431 老顽童岗位说明书定稿——完成报告"
type: completion_report
assignee: laowantong
created_at: 2026-08-23
status: pending_review
---

# #431 角色专场第一场：老顽童岗位说明书定稿——完成报告

## 一、产出

升级 `30_wiki/agent-specs/agent-spec-laowantong-producer.md`（1427 → 6822 字节，旧版职责/边界/协作接口升级为五要素可执行卡，只升级不推倒）。

## 执行报告

**文件清单**：
- `30_wiki/agent-specs/agent-spec-laowantong-producer.md`（唯一改动文件，commit 待入档）

**完成内容**：老顽童岗位说明书 v1.0——五要素齐全（内核/职责/边界/工作流/Trigger+Interface）+ G1/G2 两铁律 + 老顽童专属门禁四条（领取前置精做笔记/素材消费率≥80%；产卡状态细分 in_progress；批次验收≠整单终审；审查者不直接编排）。

**验证**：`kdo pre-submit -f 30_wiki/agent-specs/agent-spec-laowantong-producer.md` → Passed 1 / Failed 0 / ✅ PASS（YAML/WIKILINK/DOMAIN/DK_SECTION/OUTLINK/ALIASES/POSITION/SOURCE_REACHABILITY 全 0 issues）。`kdo index` → Indexed 4086。

**未做项**：不改《KDO 基本法》正文（任务边界）；其余角色专场（欧阳锋/黄药师/风清扬/王语嫣/老朱）不提前拆单（一角色一张过）；老朱终稿拍板后才由王语嫣并入角色章。

**需要谁动作**：欧阳锋终审（抽 B2-3 两条血泪 + 老顽童两条补充是否真含）；老朱终稿拍板后开下一场（欧阳锋）。

---

## 二、五要素对照

| 要素 | 内容 |
|:--|:--|
| 内核 | 卡片产能主力（Anthropic worker）；行为牌组 L1-L9；多实例+队列约束（charter §2.5） |
| 职责 | 5 项：卡片生产（KF-024 结构门禁）/ 素材消费纪律（E024 一等证据）/ 生产门禁（pre-submit 0 ERROR）/ 批量纪律（三问）/ 状态纪律（in_progress 细分） |
| 边界 | 5 项：写审分离（§3.13）/ 不改别人卡不跨角色派活 / 一次领一件 / 审查者不直接编排（G2）/ 只从队列领任务 |
| 工作流 | 7 步：领取前置精做笔记 → 出牌建模 → 制卡 → 提审三证验证 → 退回复工（执行前三问）→ 批次验收禁 review 脚本 → 收尾四件套 |
| Trigger+Interface | Trigger：队列派单 + 「继续」恢复口令；上游王语嫣任务单；下游提审欧阳锋；记忆锚点双路径 |

## 三、验收对照

| 验收项 | 结果 |
|:--|:--|
| 五要素齐全 | ✅ 上表 |
| Trigger+Interface 不再是缺口 | ✅ 独立节，Trigger 明确队列派单/恢复口令 |
| 与 charter §2.1 不冲突 | ✅ 老顽童=生产（卡片/内容），多实例+队列约束——逐条对齐 |
| B2-3 欧阳锋两条血泪 | ✅ 批次验收≠整单终审（工作流第 6 步）/ 审查者不直接编排（边界第 4 项） |
| 老顽童两条补充 | ✅ 领取前置=精做笔记落盘（工作流第 1 步）/ claimed→in_progress 中间态（职责第 5 项） |
| G1/G2 两铁律 | ✅ 独立节，原文口径 |
| pre-submit | ✅ 全 0 issues PASS |
| 相关回链只增不改 | ✅ related 去重（truman 重复项移除）+ 增 fengqingyang-observer/white-paper-five-elements；未改其他卡 |

## 四、边界说明

- 底本全消费：diag_20260822_fengqingyang-5role-spec-workflow（角色 3 老顽童建议）/ charter §2.1/§2.2/§2.4/§3.13 / ouyangfeng position B2-3 / laowantong position B2-3 / 旧 spec 全量吸收
- 未推倒重写：保留旧版职责/边界/基线用例精华，扩展为五要素
- 未碰其他角色文件（写审分离 + 一角色一张过）

## 五、遗留

- 待欧阳锋终审；老朱终稿拍板后王语嫣并入《KDO 基本法》角色章 v1.0
