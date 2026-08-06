---
id: task_20260806_huangyaoshi-master-moc
task_id: 241
assignee: huangyaoshi
status: queued
updated_at: 2026-08-06
domain: system
priority: P2
---

# #241 master 主题域 MOC 索引卡（横向 MOC 序列②）

## 背景

复盘 MOC（#236 ✅）+ design MOC（#238 ✅）双验证模板可复用。横向序列按密度：design → master(104) → product(75) → kdo(51)。本任务为序列第二个。

## 任务目标

建 1 张 master 主题 MOC 索引卡（104 张，master 域）。模板复用 #236/#238 已定稿结构（黄药师定稿版）。

## 执行前置

- **#238 reviewed**（模板迭代点含状态联动，已定稿）
- **#240 完成后**（中文域查重收尾——master 域若含中文域卡，查重后聚合才准确；串行纪律）

## 模板要求（复用清单——#236 终审 + #238 FAIL 教训后定稿版）

1. 结构：定位 + 一句话 + 使用导航表（"你问的是→看这里"）+ 知识网络图（分层）+ 核心关系表 + 域特色
2. **状态联动提醒**（欧阳锋 #236 终审建议）：MOC 节点状态随卡状态变化需同步更新
3. aliases/discoverable_by 中文词齐全（检索入口）
4. diagnostic_signals：写明"无 MOC 时谁受影响、什么牌退化为碰运气"
5. **节点 related 全部真实存在、死链 0**（#238 FAIL 教训：MOC 节点清单从实际文件扫描出发，禁止凭记忆写 related；全库模式 pre-submit 验证）
6. **related 精确匹配目标卡 id**（#238 复审 PASS 验证法，欧阳锋 2026-08-06）：逐张用**全库 id 集合**对照——related 写卡的实际 id（如 `case-live81-ai-trademark-design`），不写描述性名称（如"Live81 AI 设计马拉松全流程"）——#238 初审 2 张死链就是描述性名称与 id 不一致
6. 中文域例外白名单引用（#240 登记后）

## 验收标准

1. 模板结构 6 项齐全；`kdo pre-submit` PASS；lint 0 新增
2. 实测导航：以 master 域代表性提问（按卡分布定）命中 MOC
3. 与 #236/#238 模板一致（三 MOC 可对齐比较）

## 边界

- 后续序列 product(75) → kdo(51) 依此类推（P2 逐个启动）
- MOC 不展开内容，节点卡不动正文

## 🆕 验收记录（2026-08-06）

- ✅ **欧阳锋终审 PASS**：related 15 张 0 死链（全库 id 集合精确匹配——#238 教训已生效，RELATED_DEAD 检查到位）/ 定位声明 ✅ / ds 2 条 ✅ / 增量 0
- **三 MOC 规律确认**：死链检查从"手测发现 7 张"→"RELATED_DEAD 自动 0"——黄药师 MOC 生产流程成熟（全库 id 集合验证成为标准动作）
- 队列登记核查：任务单 + production-queue #241 条目均已存在（欧阳锋审查时视图未见，实际已登记）；状态 reviewed 待 queue_transition 同步
