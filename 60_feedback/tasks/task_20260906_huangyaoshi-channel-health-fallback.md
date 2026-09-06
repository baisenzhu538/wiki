---
id: task_20260906_huangyaoshi-channel-health-fallback
title: "拉起器通道健康预检+余额感知 fallback（F-073 落地：kimi 403/codex 余额尽两墙连撞的工具化根治）"
seq: 656
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 老朱 09-06 晨问（欧阳锋 glm-5.3-flash 怎么会没额度？是否都自动切 kimi 没发现？）——一晚连撞两道额度墙的根治
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-06T03:46:11.903701+00:00'
---

# #656 拉起器通道健康预检+fallback（黄药师）

## 实证（09-05 夜→09-06 晨）
- kimi 通道：403 周额度（23:37 起，全员死亡，7 天窗）
- codex 通道（relay:4444→上游）：07:14 "Insufficient Balance" 秒死
- claude.exe 通道：实为智谱 GLM glm-5.3-flash（settings.json ANTHROPIC_BASE_URL=open.bigmodel.cn），全夜存活扛下全部产出
- 根因：拉起器无通道健康预检、无 fallback——死通道每次派工都撞墙才发现（kimi 撞 2 次：02:51/04:16 都是我手动发现手动切）

## 修法
1. **预检**：launch 前对目标通道打最小探针（1-token 或 /models），配额/余额/403 类错误=通道不健康
2. **fallback**：不健康→按 ROLE_TOOL 顺序自动切下一个健康通道，todos+飞书通知「通道 X 不健康（原因），已切 Y」；全不健康→报王语嫣不硬派
3. **认知表**：`90_control/channel-model-map.md`——CLI 名→真实供应商→模型→key 归属（relay 与 claude.exe 是否同 GLM 账号需黄药师核实后落表），以后值守报通道同时报真实模型

## 验收
- 模拟死通道（坏 key）launch → 自动 fallback 成功+通知出现
- 全通道死 → 明确报错不假跑
- 现有回归不红
