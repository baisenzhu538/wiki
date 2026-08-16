---
reviewed_by: 欧阳锋
review_date: 2026-08-09
id: task_20260806_huangyaoshi-retrospective-moc
task_id: 236
assignee: huangyaoshi
status: reviewed
updated_at: 2026-08-06
domain: system
priority: P1
---

# #236 复盘主题域 MOC 索引卡（横向能力主题导航修复）

## 背景与触发

2026-08-06 用户探针提问暴露知识库使用机制问题：编排"个人深度复盘"课时，王语嫣在编排中后期才通过 grep 发现已有项目复盘卡（美团 16 字诀）——**知识库使用链路（MOC 导航→检索→应用）断在第一环：复盘主题无 MOC，导航靠记忆**。这是"检索架构 v2（MOC 绝对优先）"落地不完整的结构性缺口：横向能力主题（复盘/学习/协作等跨域主题）无域归属、无索引卡。

复盘卡散落现状：concepts/（yt-model-deep-review-iceberg、yt-personal-deep-review）+ frameworks/（framework-yitang-project-retrospective）+ tools/（tool-复盘推演法）+ cases/（case-一堂-优秀转化率复盘合集）+ #233/#234 新产卡。

## 任务目标

建 1 张「复盘主题域 MOC」索引卡，让任何 Agent（含未来王语嫣）回答复盘问题时第一步可导航到完整知识网络，不再靠 grep 碰运气。

## 输入：王语嫣提供的主题域关系图（编排视角）

```
复盘主题域（MOC 根）
├── 底层能力层（#233 新建，queued）
│   ├── framework-一堂-复盘本质与三要素（判定+ROI规律+三原则）
│   ├── framework-一堂-四象限复盘法（场景选择）
│   ├── framework-一堂-团队复盘四阶段12策略（能力培养）
│   ├── tool-复盘浪费九宗罪自检清单
│   └── dk-借假修真与黑盒白盒
├── 深度标尺层（已有，reviewed）
│   └── yt-model-deep-review-iceberg（冰山五层）
├── 应用场景层
│   ├── framework-yitang-project-retrospective（项目复盘 16 字诀，reviewed 已有）
│   ├── tool-复盘推演法 / tool-复盘推演练习（事前推演，已有）
│   └── case-一堂-优秀转化率复盘合集（已有）
├── 案例层（#234 新建，queued）
│   ├── case-一堂-A加社失败归因→一堂诞生
│   ├── case-一堂-迷你访谈五周迭代
│   ├── case-一堂-教材品控事故
│   └── case-莹莹-before-after复盘
├── 桥接层（#233 新建 + 预留）
│   ├── bridge-个人复盘×知识管理W-Z-K-P（#233）
│   └── 预留：复盘×教练式领导力（等素材）
└── 相邻体系（互补，已有）
    └── yt-personal-deep-review（周子敬 IPO/科学学习，元认知层）
```

**核心关系表述（MOC 卡必须回答）**：项目复盘 16 字诀=一个环节（项目收尾流程）；深度复盘=一种能力（一切经验学习的底层方法）；冰山图=深度标尺（挖多深）；四象限=场景选择（挖什么）；12 策略=能力培养（怎么带团队）；IPO 课=学习系统元认知（相邻体系）。

## 卡片规格

- id: `system-retrospective-moc` 或按 KDO digest 惯例（黄药师定，对齐 `business-formula-domain-digest` 格式）
- type: digest/index（对齐已有 domain digest 卡格式）
- 必含：节点清单（全部复盘相关卡+状态）+ 关系图（上表）+ 使用导航（"被问复盘问题先来这"）+ 各卡分工一句话
- related：全部复盘节点（≥10）
- 归属：黄药师按 digest 惯例落盘（30_wiki/ 对应目录）

## 依赖

- #235 补链完成后网络最完整——**可与 #235 并行：先建 MOC 骨架，补链完成填充**
- #233/#234 生产中的卡以任务单规格为准（避免 MOC 与卡规格不一致）

## 🆕 加注（2026-08-06 王语嫣裁定后）

1. **MOC 聚合方式：按王语嫣提供的关系图手工聚合，不依赖 frontmatter domain 字段**——因为 #237 域名标准化（design- design 等 6 个脏域 294 张）尚未执行，domain 字段聚合会分裂。与 #237 互不阻塞
2. #237 完成后，用干净 domain 数据复验 MOC 聚合一致性
3. `90_control/scripts/scaffold-domain-index.py` 可用作脚手架
4. 本卡同时是"横向主题 MOC 模板"的第一个实战验证：design→master→product→kdo 序列将复用本卡模板（#238 design MOC 已排）

## 验收标准

1. MOC 卡落盘，能回答"知识库的复盘知识有哪些/各自什么关系/怎么选"
2. 节点 related 双向闭合（MOC→各卡 + 各卡→MOC），`kdo pre-submit` PASS
3. 实测导航：王语嫣以"项目复盘 vs 深度复盘区别"提问，先命中 MOC 再定位到具体卡（模拟验证）
4. lint 0 新增 ERROR

## 边界说明

- MOC 是结构索引卡，不做内容展开（内容在节点卡）
- 不改变各节点卡正文（#235 已覆盖补链）
- 模式可复制：本次沉淀"横向主题 MOC"模板，后续"学习/协作/供应链"等横向主题可参照（建议黄药师在 MOC 卡或系统卡中记录此模板）
