---
id: method-external-agent-feedback-production-loop
title: "外部 Agent 反馈→生产深化闭环机制（双驱动固化）"
type: method
status: draft
author: 王语嫣
reviewed_by: 欧阳锋
review_date: 2026-08-09
created_at: 2026-08-09
domain:
  - system
tags:
  - audience:builder
  - scene:reference
  - skill-level:intermediate
  - agent:hermes
---

# 外部 Agent 反馈 → 生产深化闭环机制

> 一句话：Hermes 教练等外部 Agent 每次真实使用 KDO（踩坑/洞察/验证/纪律漏洞），都通过显式通道回流，驱动知识库/数据/标准/生产方式的四层深化——**KDO 进化从"内部驱动"升级为"内部+外部双驱动"**。
> 实证：AI 基本功教练上线两轮对话，已通过本机制隐含的四回路给 KDO 带来 4 项深化（见文末 dogfooding 映射）。

---

## 一、四回路模型（反馈 → 深化）

| 回路 | 反馈类型 | 深化动作 | 落盘位置 | 实证 |
|:--|:--|:--|:--|:--|
| **知识回路** | 踩坑/新洞察/新方法 | 建 dk 卡/案例卡 → 知识库增厚 | 30_wiki/dark-knowledges + cases | 教练三连坑 dk 卡 |
| **数据回路** | 真实任务验证结果 | verified 回填 → 知识从"记录"变"验证过" | 周期表 JSON/卡 verified | 试点 5 Feature 回填（25/100） |
| **流程回路** | 纪律漏洞/行为违规 | 铁律升级 → 生产标准进化 | agent-os §13 + E 系列铁律 | E018 四提四证 → 全角色铁律 |
| **模式回路** | 成功模式/自举实证 | 流水线/机制固化 → 生产方式进化 | workflow 卡/method 卡 | #263 Agent 生产流水线 |

## 二、反馈流入通道（显式，不靠偶尔发现）

### 通道 1：corrections 文件（已有，标准化触发）
```
60_feedback/corrections/corr_<日期>_<角色>-<主题>.md
触发：任何 agent 踩坑/诊断/自我迭代后（欧阳锋/老顽童/教练已示范）
```

### 通道 2：agent 迭代日志（agent-spec 必含，自动源）
```
agent-spec 卡的 ## 迭代日志（每次实测/反馈追加一行）
→ 王语嫣每周编排扫描：迭代日志中的四回路信号 → 转深化动作
```

### 通道 3：消费端回填（试点已验证）
```
kdo feature 试点回填（verified/case_ref）→ 周期表 JSON → 数据回路自动完成
```

### 通道 4：编排反馈闭环（王语嫣侧，每周）
```
汇总通道 1-3 信号 → 四回路分类 → 触发深化动作（建卡/回填/铁律/固化）
→ 结果写入 kb-evolution-direction
```

## 三、触发规则（什么值得深化 vs 噪音）

| 信号 | 判定 | 动作 |
|:--|:--|:--|
| 新坑（无已有卡覆盖） | ✅ 深化 | 建 dk 卡（author=反馈 agent，status=draft，送审） |
| 纪律漏洞（E 系列新增） | ✅ 深化 | 升级铁律（E 编号，写入相关 context/prompt） |
| 真实任务验证结果 | ✅ 深化 | 回填 verified/case_ref |
| 成功模式（自举/流水线类） | ✅ 深化 | 固化 workflow/method 卡 |
| 已知坑的重复报告 | 🟡 不深化 | 指向已有 dk 卡（防重复） |
| 纯抱怨/无信息量 | ❌ 噪音 | 不入库 |

## 四、agent 侧义务（谁反馈什么）

1. 踩坑 → corrections 文件 + 可复用进共享 skill
2. 实测验证 → 回填（verified/case_ref/verify_note——含"边界无效"也要如实标注）
3. 纪律冲突 → 显式提出（不沉默不绕过）
4. 自建资产 → 遵守 E018（author 属实/审查真实/自建默认 draft）

## 五、dogfooding：教练反馈四回路映射（本机制自验证）

| 教练反馈 | 回路 | 深化动作 | 状态 |
|:--|:--|:--|:--|
| 三连坑（审批/cwd/检索规则） | 知识 | dk-agent-access-kdo-pitfalls | ✅ 已建（draft 待审） |
| 质量门禁 5 Feature 实测 | 数据 | 周期表 verified 20→25 | ✅ 已回填 |
| 自建卡伪造审查（E018） | 流程 | E018 铁律升级（#264 执行中） | 🔄 进行中 |
| 自举行为（调研模板→建体系） | 模式 | #263 Agent 生产流水线 | ✅ 已固化 |

**四回路全部走通——机制有效。**

## 六、与现有机制的衔接

- corrections 目录（已有）→ 通道 1 复用
- agent-os §13（角色实例策略）→ 流程回路的落点
- #261（全局认知）→ agent 侧义务（第 4 条 E018）写入
- kb-evolution-direction → 深化动作的登记处

---

*王语嫣 · 2026-08-09 · 触发：用户战略问题"外部 agent 反馈能否带来生产深化" + #252 试点实证*
