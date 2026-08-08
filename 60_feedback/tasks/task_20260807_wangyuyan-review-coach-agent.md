---
id: task_20260807_wangyuyan-review-coach-agent
task_id: 246
assignee: laowantong
status: queued
updated_at: 2026-08-07
domain: personal
priority: P1
---

# #246 复盘教练 agent-spec（复盘域 agent 补缺）

> ⏳ **编排提审（2026-08-07）**：本任务单规格已提交欧阳锋生产前审查——审查通过后老顽童方可领取生产（写审分离：老顽童不替审）。

## 背景

复盘域 16 节点无 agent-spec。#233 编排时暂缓条件（"12 策略→未来可解压复盘教练 agent-spec，等核心卡入库"）已解除——framework×3 已 reviewed、案例卡已入库、团队引导清单（#245）生产后即可支撑 agent 的引导能力。

## 卡片规格

- id: `agent-spec-复盘教练`（对齐 agent-native-card-design 规范）
- TCPR 身份：**Coach**（教练型——参考 #153 决策教练/#177 教练对话引擎协议的对齐）
- System Prompt 必含：
  1. 定位声明（属于 framework-团队复盘四阶段12策略 的引导者落地）
  2. 输入门：复盘场景（个人/团队/项目）+ 素材（事实清单/口述/记录）+ 参与者结构
  3. 核心能力：冰山五层归类（把答案标记归类到 L1-L5）/ 四象限定位（决策执行×成败）/ 三件套产出（go-no-go+规范+分阶段清单）/ 心理安全维护（拦截"下定义"式回应、保护说真话者）/ 追根到底（"哪方面不行？具体在哪？有什么事实？"）
  4. 输出：引导问题清单（核查类+深挖类分类）/ 冰山穿透报告 / 三件套 / 案例沉淀建议
  5. 边界：不替用户决策（go/no-go 归用户）；不跑全库 lint/index；不写 30_wiki 卡片
- 迭代日志：千惠复盘实战反馈（团队版修正：员工先表态/心理安全三段式/批斗会顾虑）
- 暗知识沉淀：追根到底三原则/信息流动管道修复
- 数据源：[[tool-团队复盘引导清单]]、[[framework-一堂-四象限复盘法]]、[[framework-一堂-复盘本质与三要素]]、[[framework-一堂-团队复盘四阶段12策略]]、[[yt-model-deep-review-iceberg]]

## 验收标准

1. System Prompt 可直接注入 Claude/Kimi/DeepSeek 运行
2. 用千惠案例实测：输入 30 问标记版 → 输出冰山归类+三件套（模拟验证）
3. pre-submit PASS；lint 0 新增

## 边界

- 只做 agent-spec 卡（不建可运行代码——agent 运行层是黄药师能力中台的事，本任务只落规格）
- 与 #177 教练对话引擎协议对齐，不重复建协议
