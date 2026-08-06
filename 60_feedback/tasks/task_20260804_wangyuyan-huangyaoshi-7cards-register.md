---
id: task_20260804_wangyuyan-huangyaoshi-7cards-register
task_id: 230
assignee: huangyaoshi
status: queued
created_at: 2026-08-04
domain: kdo
priority: P1
source: review_20260804_huangyaoshi-7cards.md（欧阳锋审查）
updated_at: '2026-08-04T02:30:00+00:00'
---

# #230 黄药师基建经验资产化7张卡：补结构+复审登记

## 背景

黄药师自主产出7张基建经验资产化卡（E010重复键检测/P-42核查缺位/delivery bug/争议裁决协议/可发现性自查等经验沉淀）。欧阳锋审查：**FAIL（条件）**——方向对（#229前把教训沉淀为知识是正确动作），质量欠（1重复卡+7/7结构缺口）。

## 7张卡清单与修复要求

| # | 卡 | 类型 | 🔴/🟡问题 | 修复 |
|:--|:--|:--|:--|:--|
| 1 | framework-讲香十指模型 | framework | 🔴 **重复卡**——与#215 `tool-讲香基本功-十指模型`（reviewed A-）同素材同内容 | **✅ 已删除（2026-08-04 用户确认）**——探索铁证：全库0引用/2条死链related/aliases与tool卡撞车；`git rm`等效（文件从未被git跟踪，python os.remove移除，磁盘已消失）；第三张同主题卡`framework-一堂-十指模型`（老顽童pending_review）不在本次范围 |
| 2 | dk-E010-duplicate-key-detection | dk | 🟡 ds缺/定位缺/related 4 | 补ds+定位+related≥5 |
| 3 | dk-P42-agent-fact-check-gap | dk | 🟡 ds缺/定位缺/related 2/缺关联段 | 补ds+定位+related+**"与其他知识的关联"段** |
| 4 | dk-delivery-path-type-bug | dk | 🟡 ds缺/定位缺/related 2/缺关联段 | 补ds+定位+related+**"与其他知识的关联"段** |
| 5 | workflow-cross-agent-fact-dispute | workflow | 🟡 ds缺/定位缺/related 2 | 补ds+定位+related≥5 |
| 6 | tool-mcp-reachability-check | tool | 🟡 ds缺/定位缺/related 2/缺失败模式 | 补ds+定位+related+**失败模式段**（注：此卡=O-10自查脚本，与#221相关） |
| 7 | tool-kdo-help | tool | 🟡 ds缺/定位缺/related 2/缺失败模式 | 补ds+定位+related+**失败模式段**（注：此卡=#221的kdo_help，已交付） |

## 修复要求（欧阳锋+王语嫣对齐）

1. **🔴 framework-讲香十指模型**：删除（与#215重复）——删除前确认无其他卡引用它；若有引用先改链
2. **6张补结构**：
   - 补ds（每条带signal+影响）
   - 补定位声明（O8：正文开头"属于XX框架第Y步"）
   - related补到≥5（含跨域）
   - dk补"与其他知识的关联"段；tool补失败模式段
3. 修复后重新提交pending_review → 欧阳锋复审

## 验收标准

1. framework-讲香十指模型已删除（或确认并入且无死链）
2. 6张卡：ds/定位/related≥5/dk段/tool段全部补齐
3. `kdo pre-submit --files <6张>` 通过
4. 修复后欧阳锋复审PASS

---

## 🔍 王语嫣验收核查（2026-08-04）—— **部分未达标，需补2项**

> 黄药师报告"6张全补齐"，王语嫣独立验证后确认**大部分达标，但2项未完成**：

### ✅ 已达标（6/6）

| 项 | 状态 |
|:--|:--|
| YAML解析 | ✅ 6/6 通过 |
| ds（diagnostic_signals） | ✅ 6/6 补上 |
| related≥5 | ✅ 6/6（都是6条） |
| 定位声明（O8） | ✅ 6/6 |
| dk三张段 | ✅ 7/8（E010/P42/delivery，基本完整） |

### ❌ 未完成（2项）

**1. workflow/tool 三张缺标准段（欧阳锋审查要求的6段）**
- `workflow-cross-agent-fact-dispute`：只有触发条件/证据效力/裁决流程/验收标准/失败模式——**缺使用场景/操作步骤/适用边界/为什么值钱/与其他知识的关联/Critique**
- `tool-mcp-reachability-check`：只有一句话/用法/输出示例/何时用/失败模式——**缺操作步骤/使用场景/适用边界/为什么值钱/与其他知识的关联/Critique**
- `tool-kdo-help`：只有一句话/返回内容/何时调用/失败模式——**同上缺6段**

**2. review_date 6/6 全缺**（计划明确要求补，探索发现7张卡都缺）

### 结论

黄药师只补了"ds/related/定位声明"三项共性问题，**没有按计划补标准段和review_date**。需退回补完：
- workflow/tool×3：补6个标准段（使用场景/操作步骤/适用边界/为什么值钱/与其他知识的关联/Critique）
- 6张：补review_date
- 补完后重新提报 → 欧阳锋复审

## 边界

- 内容方向正确（基建经验资产化）——只补结构，不改内容
- 与#221/#228的关联卡（tool-mcp-reachability/tool-kdo-help/dk-E010）修复时保持与既有实现的对应
- 归入 kdo 域（基建经验资产）
