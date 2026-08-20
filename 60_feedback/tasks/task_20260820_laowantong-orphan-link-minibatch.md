---
id: 398
assignee: laowantong
status: queued
title: 图谱孤儿清零小批（P3，老朱 08-20 拍板）：4 张角色 spec 互链 + 7 张 case-wechat 最低入链
priority: P3
dependency: []
---

# #398 图谱孤儿清零小批

## 来源

- 老朱 08-20 拍板："4 张角色 spec 也需要做"
- 王语嫣全库实测（08-20 图谱诊断）：
  - **agent-spec 15 张中 6 张孤儿（40%）**——含我们自己：`agent-spec-wangyuyan-orchestrator`、`agent-spec-laowantong-producer`、`agent-spec-huangyaoshi-builder`、`agent-spec-hongqigong-multimodal`（实扫另 2 张以报告为准）
  - **case-wechat-* 7 张全孤儿**——promote 管线产物，入管时零链接（#395 生产线收口前的存量）

## 任务目标

两批孤儿清零，互链真实。

## 执行范围

1. **角色 spec 互链（6 张）**：
   - 互链：五绝 spec 之间按协作关系互链（编排↔生产↔审查↔基建↔多模态）
   - 上链：`framework-truman-agent-team-architecture`（团队架构卡）+ `agent-spec-ouyangfeng-reviewer`（已非孤儿，作为锚）+ 各自域 MOC
   - 读了 spec 内容按真实分工关系链，不环形互链凑数
2. **case-wechat 7 张最低入链**：
   - 每张 related 补：偶遇采集脉络相关卡（如 `dk-best-datasource-is-floor` 或偶遇管线相关 framework——读卡判断）+ 对应主题域已有卡 ≥1
   - 这 7 张是 draft 待精做卡，本单只做**最低入链**（不当孤儿），精做仍走 #387 模式另议
3. 双向回链：被链卡侧 related 追加，只增不改（#384 模式，全量复扫）

## 边界

- 只动 related/frontmatter，正文零改动
- 关联真实（O0）；pre-submit 0 ERROR；完成后 commit（E040）
- 欧阳锋随下批 spot-check 复终审

## 内容价值判断（PROTOCOL §7 合规声明）

- 仅新增链接，无删除/移动

## 验收标准

1. agent-spec 孤儿 = 0、case-wechat 孤儿 = 0（全库复扫）
2. 互链关系经欧阳锋抽查"链得对"

## 交付

1. diff + 复扫证据
2. 送欧阳锋终审（随下批 spot-check）
