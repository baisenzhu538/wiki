---
id: diag_20260906_wangyuyan-encapsulation-gap-review
title: 全库封装复盘报告 v1——9 大高频基建裸奔实锤/T1-T3 缺口清单/封装生产单依据（老朱晨令双主线之二）
type: diagnosis
status: orchestrated
audience: 老朱
author: 王语嫣
created_at: '2026-09-06'
---

# 全库封装复盘报告 v1

## 一、复盘标尺（昨天学的封装方法论，今天用来量库）

Truman 判据：**「知识不仅要能被人看懂，还要能被 AI 调用」**；封装去处六层=DataPack/Skill/Role/知识库/Workflow/路由规则。量法：一件能力若「高频使用+多角色需要+固定姿势」，就该有 skill 壳让 agent 检索即用；只活在散文文档和口口相传里=未封装。

## 二、盘点结果

| 库存 | 数 |
|:--|:--|
| skills/shared 现有 | 79 个（内容方法论类为主：five-step 族/research 族/decision 族/task-orchestration 等） |
| kdo-tools 基建脚本 | 67 个 |
| 90_control/scripts | 99 个 |
| **高频基建脚本有 skill 壳的** | **0 个**（9 个每日级脚本全查无壳） |

## 三、缺口清单（T1 立即封装/T2 排队/T3 不封）

**T1（高频×多角色×固定姿势，本批生产）**：
1. `queue-transition`——状态流转（所有角色每天用；错用=领单失败 #645 实证）
2. `kimi-headless-launch`——无头拉起（王语嫣+被拉角色；纪律写死在脚本 docstring 里，agent 不可检索）
3. `daily-context-save`+`review-check`——复盘链（全角色收尾；--evidence 禁内联等教训全靠踩坑传播）
4. `scan-demo-sections`+`transcript-index`——口述稿处理三件套（W1/W2 牌的配套工具，生产者不知道它们存在）
5. `transcribe-win`——转写（#649 修好待挂载 kdo，正好一并封装）
6. `watch-inbox`+`conveyor-probe`——采集登记面（编排者 triage 依赖）

**T2（高频×单角色，第二批）**：role-clock / generate-dashboard / queue-archive / memory-capsule / infra-status / agent-status

**T3（不封）**：一次性/维护类脚本（build_seed/canvas-agent/douyin_*/fix-review-status 等），留脚本+台账即可

**Dimension A（知识遗漏未封装）另查**：9 份协议在 personal-os（我的域，散文形态合规）；E 系错误模式已 dk 化 327 张；gate 知识在 charter/手册——无重大遗漏，T1 封装后复检。

## 四、执行

- T1 六件封装单 → 老顽童生产（SKILL.md 壳：调用姿势+边界+踩坑链接 dk/协议）→ 欧阳锋终审
- 每件壳的验收=「新 agent 不读 context 文件，仅凭 skill 检索即可正确调用」——狗粮实测
- 挂载点：skills/shared/ + #649 的 kdo 挂载联动
