---
id: task_20260904_huangyaoshi-transcribe-quality-model-bump
title: 转写质量升级：tiny→small/medium 模型评估切换（「公刑部/新党区/手购所用」关键名词错转实证）+ faster_whisper 失踪根因
seq: 634
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-04
decision_source: 老朱 09-04 凌晨链路验证：414号文视频转写成功但关键名词全错（tiny 模型中文错字族，同族 09-02 05:47 批「失碎冲鞋」）——王语嫣门禁判定退回重转
reviewer: 欧阳锋
---

# #634 转写质量升级（黄药师）

## 背景（实证）

- 09-04 00:19 老朱视频号链接：下载✅转写✅但 tiny 模型把「工信部」转作「公刑部」、「信创区」转作「新党区」、「首购首用」转作「手购所用」——政策关键名词全错，这种卡转正=检索面污染
- 同族：09-02 05:47 批「征留/失碎冲鞋」乱码族
- 附带未解之谜：faster_whisper 在 Windows Python312 里失踪（昨 05:47 还能跑），王语嫣应急 pip 重装 1.2.1 恢复——谁弄没的没查到（环境漂移无留痕）

## 任务

1. **模型评估切换**：transcribe_win.py 默认 tiny→small（或 medium，按显存/速度实测权衡），中文政策/课程类内容验收标准=关键名词零错转；用 414 号文视频和 Live257 片段做前后对照
2. **414 号文重转+卡重修**：重转 `src_wechat_bf9ce0b38119ed73` 对应视频，卡 `case-wechat-bf9ce0b38119ed73` 内容修正重提审
3. **faster_whisper 失踪根因**：查 pip 日志/环境变更记录，给一句话结论（查不到就写「不可考」+加防护：转写前置自检 import 失败即报）

## 交付

- 模型切换 diff+对照实证 + 重转写产物 + 卡重修 + 失踪根因结论 + 执行报告
- claim/complete 走 queue_transition（complete 634）
