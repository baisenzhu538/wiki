---
id: task_20260906_laowantong-encapsulation-t1
title: "封装复盘 T1 生产：6 件高频基建 skill 壳（queue-transition/launch/复盘链/口述三件套/transcribe/采集面）"
seq: 658
status: queued
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 老朱 09-06 晨令「全库封装复盘+基础设施封装化」；报告=diag_20260906_wangyuyan-encapsulation-gap-review
reviewer: 欧阳锋
instance: laowantong
updated_at: '2026-09-06T12:35:00+08:00'
---

# #658 T1 封装生产（老顽童）

## 任务
按诊断报告第三节 T1 清单，为 6 件高频基建能力写 SKILL.md 壳（不改脚本本体，只写封装层）：
1. queue-transition（90_control/scripts/queue_transition.py）——状态流转姿势/seq vs task_id 寻址坑（#645 friction）/force 台账纪律（#655 --sequence 新能力）
2. kimi-headless-launch——拉起姿势/通道-真实模型对照（#656 台账联动）/逐单落盘纪律
3. daily-context-save + review-check（并一件「复盘链」壳）——11 章格式/--evidence 传文件禁内联（F-034）/🟢🟡🔴 等级
4. scan-demo-sections + transcript-index（并一件「口述稿处理三件套」壳）——W1 逐字读红线：工具只做索引不替代阅读
5. transcribe-win——用法/timeout 语义（#649 修后）/长视频姿势
6. watch-inbox + conveyor-probe（并一件「采集登记面」壳）——登记段结构/划销纪律/E059 逐行身份核验

## 每件壳验收（硬标准）
- SKILL.md 含：何时用/怎么调（命令+参数）/边界与红线/踩坑→dk 或协议链接
- **狗粮测试：一个未读 context 文件的新 agent，仅凭 skill 检索即可正确调用一次（实测记录附执行报告）**
- 不改脚本本体；发现脚本 bug 不顺手改（另立项）

## 参考
- 封装六层形态：30_wiki/frameworks/framework-encapsulation-methodology.md（昨夜新卡）
- skill 卓越标准：90_control/tool-card-excellence-standard.md
- 挂载：skills/shared/，与 #649 的 kdo 挂载联动口径一致
