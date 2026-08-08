---
id: task_20260809_laowantong-agent-production-pipeline
task_id: 263
assignee: laowantong
status: queued
updated_at: 2026-08-09
domain: system
priority: P0
---

# #263 Agent 生产流水线 workflow 卡（模式固化）

## 背景

AI 基本功教练（Hermes）上线全过程实证：从零接入 KDO 到自举（两轮对话完成学习闭环）——"三件套配齐后 Agent 行为链自动"。用户拍板：固化为 workflow 卡。实证案例：`00_inbox/Agent生产流水线-案例-AI基本功教练自举-20260809.md`。

## 卡片规格

- id: `workflow-kdo-agent-production-pipeline`（type: workflow/method——黄药师定，对齐 workflow 卡规范）
- 定位声明：属于 agent 建设体系（agent-native-card-design 的流水线化）

### 三步流水线（核心结构）

```
① spec 层（老顽童）：agent-spec 卡——领域 + 能力边界（TCPR/输入输出/依赖资产）
② 注入层（黄药师）：三件套——认知层（KDO 知识地图+生产纪律）+ 检索层（kdo feature/MCP 桥）+ 权限层（smart/WSL cwd）
③ 自举层（Agent 自己）：探索→定位→踩坑→沉淀→迭代（MOC 导航→建 dk→注册→更新 spec→复盘体系）
```

### 必含内容
1. 三件套规范（引用 #260/#261 实现：知识地图段格式/检索规则/权限配置）
2. 自举行为链（实证：教练的两轮对话行为链）
3. **生产纪律（E018 教训）**：自建卡 author 属实/审查真实/自建默认 draft——写进规范正文（不是附录）
4. 复盘格式约束：agent-os §10.2 标准 10 章（⚠️ 教练借鉴了黄药师旧版格式不合规——案例第七节已标注，规范里明确唯一标准）
5. 先例引用：#150 基本功教练 / #246 复盘教练 / #251 coach / #143 跨域诊断 Agent
6. 验收标准：下一个新 Agent 按流水线走通（spec→注入→自举）

## 素材

- `00_inbox/Agent生产流水线-案例-AI基本功教练自举-20260809.md`（实证）
- #260/#261 任务单（三件套规范）
- agent-os §10.2（复盘标准）
- E018（错误模式库——生产纪律）

## 验收标准

1. workflow 卡含三步流水线 + 三件套 + 纪律 + 复盘约束（pre-submit PASS）
2. 与案例/先例一致（可追溯）
3. lint 0 新增；定位声明有

## 边界

- 不重复建卡（agent-native-card-design 是 spec 规范，本卡是流水线流程——互补）
- 王语嫣不直接写卡（编排职责），本任务老顽童生产、欧阳锋审查
