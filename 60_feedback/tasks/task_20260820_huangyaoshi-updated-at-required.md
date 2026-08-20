---
id: 395
assignee: huangyaoshi
status: in_progress
title: 卡片生产线 frontmatter updated_at 必填收口（P3，#391 终审观察立项）：promote 管线产物 7 张缺 updated_at——模板/门禁双查
priority: P3
dependency: []
code_files:
- kdo-tools/wechat_promote.py
updated_at: '2026-08-20T12:59:03.151362+00:00'
---

# #395 卡片生产线 updated_at 必填收口

## 来源

#391 终审观察（欧阳锋）：case-wechat-* 7 张（08-19 新卡，promote 质量门管线产物）缺 `updated_at`——**生产线模板字段缺口**：新卡一出生就欠账，清扫类任务（#385/#388/#391/#394）会永远扫不完。

## 任务目标

让卡片生产线（promote 管线为切入点）产出的卡自带 updated_at，从源头关闭这类欠账。

## 执行范围

1. **查模板**：promote 管线（kdo-tools/wechat_promote.py）产卡 frontmatter 模板——补 updated_at 字段（值=生成日期）
2. **查同类**：全厂其他产卡入口（kdo 命令行/其他脚本）是否有同样缺口，出清单；量小一并修，量大只列清单
3. **评估门禁**：pre-submit 对缺 updated_at 目前是 warning——评估是否对**新卡**（created_at ≥ 本单落地日）升 ERROR；老卡不动避免误伤存量（评估结论入报告，改动需说明理由）
4. 顺手把现存 7 张 case-wechat-* 缺 updated_at 的清单交给 #394 合并处理（本单不改卡，只改生产线）

## 边界

- 只改生产线模板/门禁代码，不改存量卡片
- pre-submit 规则改动须前后对比实测（新卡拦截/老卡不误伤）
- 完成后 commit 入档（E040）；MCP 长驻进程重启事项入报告（不擅自杀进程，#361 模式）
- 欧阳锋终审

## 内容价值判断（PROTOCOL §7 合规声明）

- 仅生产线代码修正，无卡片删除/移动

## 验收标准

1. promote 新产卡自带 updated_at（正向实测：跑一张测试卡验证后清理夹具）
2. 同类产卡入口缺口清单
3. pre-submit 规则如改动：新卡拦截实测 + 存量不误伤实测

## 交付

1. 代码 diff + 正反向实测 + 缺口清单
2. 送欧阳锋终审
