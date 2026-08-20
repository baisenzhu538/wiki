---
id: 398
assignee: hermes
status: reviewed
title: 图谱孤儿清零小批（P3，老朱 08-20 拍板）：4 张角色 spec 互链 + 7 张 case-wechat 最低入链
priority: P3
dependency: []
updated_at: '2026-08-20T17:02:45.809119+00:00'
reviewed_by: 欧阳锋
review_date: '2026-08-20'
grade: A
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

---

## 执行报告（2026-08-20 老顽童 hermes 实例）

### 完成概要
图谱孤儿清零小批完成：**五绝角色 spec 互链 5 张 + case-wechat 7 张最低入链 + 2 锚卡双向回链**，孤儿归零，pre-submit 16/16 全过，commit 入档（E040）。

### 角色 spec 互链（5 张，按真实协作关系非环形凑数）
| 卡 | 新增 related |
|:--|:--|
| agent-spec-wangyuyan-orchestrator（编排） | +laowantong（生产下游）+hongqigong（多模态）+team-architecture |
| agent-spec-laowantong-producer（生产） | +huangyaoshi（基建）+hongqigong（多模态）+team-architecture |
| agent-spec-huangyaoshi-builder（基建） | +laowantong（生产）+hongqigong（多模态）+team-architecture |
| agent-spec-hongqigong-multimodal（多模态） | +wangyuyan+laowantong+huangyaoshi+ouyangfeng+team-architecture（此前仅链发布域） |
| agent-spec-ouyangfeng-reviewer（审查，锚） | +wangyuyan+laowantong+huangyaoshi+team-architecture |

### case-wechat 7 张最低入链
- 每张 + `dk-best-datasource-is-floor`（偶遇采集脉络卡）
- 主题可推断的 + 主题卡：article（AI Native 团队→team-architecture）/ dy（Skill→tool-skill-packaging-eight-steps）/ tt（代码审查→tool-open-closed-problem-classifier）
- 3 张 title 空（5291b/6725b/AWyG）只加脉络卡——主题待精做时补（#387 模式）

### 双向回链（只增不改）
- framework-truman-agent-team-architecture +5 张 spec
- dk-best-datasource-is-floor +7 张 case-wechat

### 验证
- **复扫：agent-spec + case-wechat related=0 = 0**（E017）
- pre-submit 16/16 全过 FAIL 0（kdo index 已重建）
- frontmatter 插入 yaml 结构感知（E016）；关联按 spec 真实分工（编排↔生产↔基建↔多模态↔审查）

### 待欧阳锋
- 随下批 spot-check 复终审（抽查"链得对"）

---

## 欧阳锋终审（2026-08-21 · 链得对抽查）

**裁定：PASS A。**

**O3 验证**：
- **spec 互链真实性**：wangyuyan（编排）→laowantong（生产下游）+hongqigong（多模态）✓；ouyangfeng（审查锚）→四角色+team-architecture ✓——按真实协作关系非环形凑数 ✓
- **case-wechat 主题推断**：dy→tool-skill-packaging-eight-steps（Skill 主题）✓；脉络卡 dk-best-datasource-is-floor 统一入链 ✓；3 张 title 空只加脉络卡（#387 模式，主题待精做补）✓
- **独立复扫：agent-spec + case-wechat related=0 = 0** ✓（E017 归零真实）
- pre-submit 16/16 + E016 yaml 结构感知 + commit 入档（E040）✓

**观察**（不阻断）：agent-spec-ouyangfeng-reviewer related 混 1 条双括号旧格式（`[[tool-agent-white-paper-five-elements]]`）——格式不统一遗留，随库级格式收口处理。
