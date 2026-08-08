---
id: task_20260808_wangyuyan-feature-consumption-pilot
task_id: 252
assignee: wangyuyan
status: queued
updated_at: 2026-08-08
domain: ai-basic
priority: P0
---

# #252 消费端协议试点（防死清单机制——王语嫣独立补充）

## 背景

欧阳锋洞察 1（KDO 有生产端协议无消费端协议）+ 洞察 4（"不是学会的是用会的"= 只卡片化不绑使用场景=技巧派）。**防死清单的唯一机制是消费端试点**——本任务把消费端协议从"理念"变成"实测"。

## 任务目标

选 1 个**真实任务**做"点菜式"验证（消费端协议全流程跑通）：

```
真实任务（用户实际要做的 AI 工作）
  → 点菜：从 #248 周期表 JSON 点 5-10 个 Feature 作为关键假设
  → 测试：按 Feature 逐个叠加验证（记录每个 Feature 的增量效果）
  → 复盘：哪些 Feature 有效/无效/边界在哪
  → 回填：验证结果写回周期表 JSON（verified 字段更新 + 案例引用）
  → 沉淀：消费端协议 v0.1（点菜→调优→沉淀的标准流程）
```

## 试点任务选择（王语嫣裁定）

**候选**：
- A. 老朱真实业务任务（如：药店 O2O 的 AI 客服/内容生产）
- B. KDO 内部任务（如：用 Feature 思维拆解一次素材诊断）
- C. 用户现有 AI 工作流升级（如：作图/日报类——用课程案例同款场景）

**裁定**：优先 A（真实业务，验证"用会的"最彻底）；用户确认后定。

## 执行方式（用户裁定 B 后调整）：试点由 agent-basic-skills-coach 执行

试点任务 = **agent 的第一个真实用例**（#251 W4 部署完成后启动）：
- 用户给 agent 一个真实任务 → agent 用 kdo feature 点菜 5-10 Feature 作为关键假设 → 逐 Feature 测试 → 复盘 → 回填周期表 JSON
- **试点通过 = 消费端协议验证 + agent 实测验证，一步两得**

## 产出

1. 消费端协议 v0.1（tool 卡：点菜式查询→组合调优→复盘沉淀 三步流程 + 与生产端协议的接口）
2. 周期表 JSON 回填（试点 Feature 的 verified/case_ref 更新——agent 实测数据）
3. agent 实测记录（agent-basic-skills-coach 的迭代日志——实测反馈进 agent-spec）
4. 试点复盘记录（60_feedback/，进编排反馈闭环）

## 验收标准

1. 试点跑通：agent 完成 点菜→测试→复盘→回填 全流程有记录
2. 周期表 JSON 至少 5 个 Feature 的 verified 状态被真实任务验证更新
3. 消费端协议 v0.1 可被后续任务复用（欧阳锋审查）
4. agent 实测反馈写入 agent-spec 迭代日志（部署→实测闭环）

## 依赖

- **#256 reviewed（agent 部署完成——试点由 agent 执行，黄药师独立任务）**
- #251 规格层 reviewed（agent-spec 定稿）+ #248 reviewed（周期表 JSON）+ #254 reviewed（kdo feature 工具）
- 试点任务由用户拍板（真实业务 vs 内部任务）

## 🆕 试点启动（2026-08-09 用户拍板：先跑 A——内部任务）

### 试点指令（转达飞书 AI 基本功教练）

```
【#252 消费端协议试点 · 任务 A】
任务：用 Feature 思维分析 KDO 的卡片质量门禁体系
流程（消费端协议闭环五步）：
① 点菜：kdo feature pick --n 5（周期表点 5 个 Feature 作为分析的关键假设）
② 分析：用这 5 个 Feature 分析 KDO 质量门禁体系（cap_hub 13 个 lint Feature + 双轨区分）
③ 复盘：哪些 Feature 有效/无效/边界在哪（对照你 08-09 已做过的质量门禁分析）
④ 回填：验证结果写回周期表 JSON（verified 状态更新 + case_ref 引用"质量门禁分析"）
⑤ 沉淀：消费端协议 v0.1（点菜→调优→沉淀 三步流程 + 与生产端协议接口）
```

### 试点验收（消费端协议 v0.1 定稿的条件）
1. 点菜→分析→复盘→回填全流程有记录（60_feedback/）
2. 周期表 JSON 至少 5 个 Feature 的 verified 被真实任务更新（附 case_ref）
3. 消费端协议 v0.1 产出（欧阳锋审查）
4. 试点通过后触发：cap_hub 注册（黄药师裁定已落盘）+ agent 迭代日志更新

## 边界

- 不扩大试点范围（1 个任务，跑通后 v0.2 再扩）
- agent 只给路径建议，不替用户执行任务本身
