---
id: task_20260902_laowantong-live257-ten-finger-fragrance-cards
title: Live257 重讲十指讲香模型卡组（十指讲香 framework + 用数字讲故事 method + 发布会文案案例）
seq: 610
status: in_progress
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-02
decision_source: inbox 01:51 批次分诊（diag_20260902_wangyuyan-inbox-batch-42 族A，老朱 0831/0901
  直令高价值素材直接编排产卡）
reviewer: 欧阳锋
source_refs:
- 00_inbox/Live257-重讲十指讲香模型内测Candy-逐字稿.md
related_tasks:
- '#596'
instance: laowantong-kimi
updated_at: '2026-09-01T23:15:12.864641+00:00'
---

# #610 Live257 十指讲香卡组（老顽童）

## 背景

- 素材：`00_inbox/Live257-重讲十指讲香模型内测Candy-逐字稿.md`（131KB/1747 行，水水老师拆书《用数字讲故事》奇普·希思 + 十指讲香模型学员超级案例：华为/苹果/小米发布会文案拆解，案例作者王木匠/柴翔/贾红阳/沈伟杰）
- 入口诊断：域归属=**sales（表达/营销文案）**；库内有 `讲香基本功-李頔-260731/` 同族素材目录，编排前先 grep 查重（E022：主题词「讲香」+来源词「水水/Live257」双查）
- 体量 131KB 属大素材：逐字读全文（W1 硬规则，分多次读完），scan 类工具只做索引定位

## 任务（3-4 卡候选，最终形态按 W6 三方法定夺）

1. **framework**：十指讲香模型（场景化/口语化/数字化…升华化，十要素以素材原文为准）
2. **method**：《用数字讲故事》核心方法（奇普·希思，拆书层增量）
3. **case**：发布会文案拆解超级案例（华为/苹果/小米，学员实战——挑最完整 1-2 个立 case 卡）

## 验证

- pre-submit 全过；O0 溯源锚点=逐字稿路径+行号
- related 与存量讲香族/表达族卡互链双向 0 死链
- **传播声明检查**：内测 Candy 件若含「不要外传/仅限内部」字样，按 #322 先例加传播限制标注（Live260 同族已实证有限制字样）

## 六维标签建议（spec v1.6；sales 域轴缺如——生产者试点提新词，王语嫣审词入轴）

- 专业轴：销售 / 文案 / 表达 / 讲故事
- 对象轴：发布会文案 / 产品卖点 / 客户沟通
- 性质轴：框架 / 方法 / 案例
- 经验轴：实战 / 拆解 / 复盘
- 受众轴：销售 / 市场 / 创业者
- 来源轴：Live / 一堂内测 / 拆书（奇普·希思）

## 边界

- 原素材不动（00_inbox 只增不删）；学员案例署名保留
- 王宁/水水原话引用保持原样不美化

## 交付

- 3-4 张卡 + 执行报告（含三方法记录+互链实证）
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 610 附执行报告路径）
