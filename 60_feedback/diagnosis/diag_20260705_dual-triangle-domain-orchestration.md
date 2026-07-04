---
id: diag_20260705_dual-triangle-domain-orchestration
title: 双三角域全天编排诊断与 Before-After
type: diagnosis
status: draft
created_at: 2026-07-05
source: 2026-07-04 全天对话对齐
---

# 双三角域全天编排诊断

## Before-After 对照

### Before（对话开始时）

- 双三角域仅有 #64-#75 共 12 个任务
- VLM 37 个文件停在 _processed/ 未入库，kdo query 搜不到
- 没有 Skills/Workflows/Agents 分类
- 看板维护不准确——建任务单忘加入队列
- 诊断流程缺自攻击
- 口述稿操作演示段落（Truman 摊开操作过程的段落）被系统性漏掉

### After（对话结束时）

- 双三角域任务从 #12 → #105，新增 30 个
- 46 张 draft case 卡入库（黄药师批量 ingest），Agent 可搜到
- 36 张 reviewed（老顽童完成，欧阳锋审过）
- Skills/Workflows/Frameworks/Agents 四类资产均有覆盖
- 六场景全部覆盖：X光（#88）、口喷（#87）、画布（#69/#100）、分工（#101）、地图（#70）、底牌（#78）
- 看板管理bug修复：建任务单和入队同步
- 诊断流程加了操作演示信号词扫描规则
- 王语嫣 context 加入三条新铁律

## 关键决策

1. 口述稿优先于笔记——所有暗知识从口述稿叙事流提取
2. 不改已有任务文件——新洞察→新任务单→队尾排队
3. 编排流程标准化——建任务→入队→同步dashboard+kb-evolution-direction，缺一不交付
4. 操作演示=最高优先级——口述稿处理前先扫信号词
5. FDE 工程 + AI 原生组织作为双三角组织落地层
6. AI 自复盘（L2220-2312）作为飞轮引擎的终局形态

## 待办

- 明天蒸馏 YAI Agent 对话→核心词+data pack 两层拆
- #70 已解锁，老顽童可领
- 巨米业务双三角诊断——等老朱提供具体场景后启动
