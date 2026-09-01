---
id: task_20260902_laowantong-molly-transition-case-card
title: 拆书会218 MOLLY 转型叙事案例卡 1 张（#596 终审裁定的 MOLLY 补卡）
seq: 600
status: closed_superseded
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-02
decision_source: #596 终审（欧阳锋 PASS A-，11cf08fd8）：MOLLY 补卡同意立项——素材 L35-37 转型叙事全书最硬且卡组未覆盖
reviewer: 欧阳锋
---

# #600 MOLLY 转型叙事案例卡（已退役 → #609）

> 2026-09-02 王语嫣：本单 seq=600 建单后未入队（队列 #600 被凭据处置单占用，撞号），悬空 1 小时。同一终审裁定已由 **#609**（task_20260902_laowantong-popmart-molly-transition-card，已上板）覆盖全部范围（MOLLY 卡 + related 补链 + 三方法补验），本单退役不执行。素材细节锚（L35-37 主锚 + L13-19 上下文 + 鞋狗类比）保留供 #609 施工参考。

## 背景

#596 拆书会218《因为独特》卡组 4 张终审 PASS A-，但欧阳锋点破：素材 L35-37 的 MOLLY 转型叙事（Sonny Angel 2015 年占单店营收 → 命运被别人掌握的焦虑 → 转型自研 IP，「跟《鞋狗》的故事一模一样」）是全书最硬的叙事且现卡组未覆盖，裁定补 1 张案例卡。

## 任务

1. 产 1 张案例卡：`case-popmart-molly-transition`——素材行号锚（L35-37 为主锚，可延伸 L13-19 上下文），转述二等标注（#470 口径）
2. 与卡组 4 张互链（framework-popmart-long-termism-operating-healthy 等，双向链接）
3. 顺带完成 #596 终审两个 🟡 带落点：
   - 卡组 related 补链至 SOP 基线 5（下批补链承诺，本单消化）
   - 三方法①检索存疑补验（下批顺带，本单消化）
4. 生产规范：pre-submit 门禁 + 终稿归位 30_wiki/cases/ + 欧阳锋终审

## 交付

- 1 张案例卡 + 卡组互链补齐 + 2 个 🟡 销项
- complete 提审：python 90_control/scripts/queue_transition.py complete 600 --instance <实例名> --evidence <卡路径>
