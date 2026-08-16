---
name: stage-2-skeleton
description: 域骨架建设——从口述稿提取框架卡+概念卡+域索引入口卡（老顽童模式）
version: 1.0.0
author: 黄药师
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [KDO, 骨架, 框架卡, 索引入口, 老顽童]
    related_skills: [domain-iteration, stage-1-diagnose, stage-3-tooling]
---

# Stage 2: 域骨架建设

从诊断记录和口述稿中提取核心框架。

## 触发词

建框架、写框架卡、域骨架、skeleton、搭架子、建索引入口

## 约束

- 必须先读完诊断记录再动手
- 每张 framework 卡必须有 Critique（≥2 外部攻击者）+ Boundary + Action Triggers
- 框架卡配案例链接；案例卡链回方法卡
- 域索引入口卡必须在骨架阶段就建

## 执行步骤

### Step 1: 读诊断记录
理解王语嫣的置信度标记和盲区提示

### Step 2: 提取核心框架
从每份口述稿提取"核心方法论"→ framework 卡
三步编译法：浓缩→质疑→对标

### Step 3: 提取核心概念
域内关键术语、原则 → concept 卡

### Step 4: 生成域索引入口卡
```bash
python 90_control/scripts/scaffold-domain-index.py --domain <域> --topic <名称>
```
手工填写 TODO 行。四段式：框架/工具/案例/暗知识

### Step 5: 跑质检
```bash
kdo lint
python 90_control/scripts/check-source-refs.py --domain <域>
```

## 完成标准
- [ ] 域内核心方法论已覆盖为 framework 卡
- [ ] 每张 framework 卡有 Critique + Boundary + Action Triggers
- [ ] 域索引入口卡已写入，TODO 行已手工填写
- [ ] `kdo lint` 通过
