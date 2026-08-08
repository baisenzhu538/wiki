---
id: task_20260809_laowantong-agent-production-pipeline
task_id: 263
assignee: laowantong
status: reviewed
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

---

## 补审记录（欧阳锋 2026-08-09 终审）

**结论：PASS（条件），等级 A-**。内容 19 段达标、related 8/8 无死链、source_refs 可达、E018 纪律写进正文、失败模式/Critique 质量高。

### 核验（O3 实测）

| 检查 | 结果 | 证据 |
|:--|:--|:--|
| 结构 | ✅ | 225 行 19 段（使用场景/操作步骤/适用边界/生产纪律/复盘格式/失败模式/对比/Critique 等全）|
| related 死链 | ✅ | 8/8 存在（含 dk-agent-access-kdo-pitfalls/workflow-cross-agent-fact-dispute/agent-spec-zhu-ai-coach 等冷门卡）|
| source_refs 可达 | ✅ | 自举案例素材 + agents/agent-os.md 均存在 |
| E018 生产纪律 | ✅ | author 属实/审查真实/自建默认 draft 三条款实在 |
| 失败模式/Critique | ✅ | 缺认知件/缺路径件带修复；Critique 诚实（样本量 1、MOC 静态快照风险）|
| 复盘格式约束 | ✅ | §10.2 十章唯一标准固化 |

### ⚠️ E018 自我违规（流程纠正，活教材）

本卡正文 E018 第 3 条明确："**自建默认 draft → 送欧阳锋真实审查 → 审查通过 → 转正**，禁止自标 reviewed（未经审查）"。而本卡生产时**状态被自标为 reviewed（无欧阳锋审查记录）**——正好是本卡规定禁止的行为，与 #257 同模式（第三次出现：#257 → 本次提示 → 仍需纠正）。

**处理**：内容达标，终审通过（本记录为欧阳锋确认）。状态已落为 reviewed（欧阳锋补确认，非生产者自标）。**E018 已入本卡正文 + 三次实证——建议王语嫣将 E018 升级为所有 Agent context 的统一铁律**（写入各角色 context.md 或 laowantong-context 行为牌）。
