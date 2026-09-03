---
id: task_20260904_huangyaoshi-transcribe-quality-model-bump
title: 转写质量升级：tiny→small/medium 模型评估切换（「公刑部/新党区/手购所用」关键名词错转实证）+ faster_whisper 失踪根因
seq: 634
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-04
decision_source: 老朱 09-04 凌晨链路验证：414号文视频转写成功但关键名词全错（tiny 模型中文错字族，同族 09-02 05:47 批「失碎冲鞋」）——王语嫣门禁判定退回重转
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-03T20:43:48.006485+00:00'
evidence: 60_feedback/tasks/task_20260904_huangyaoshi-transcribe-quality-model-bump-workdir/对照实测与校核记录.md
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

---

## 执行报告（2026-09-04 huangyaoshi，提审）

**交付物**
① kdo-tools/transcribe_win.py v2（模型显式化+自检防护，diff 见 git）；② 414 号文重转逐字稿
`10_raw/sources/src_2026-09-04_wechat_bf9ce0b38119ed73.md`（模型 medium，header 校核注；gitignored 的
00_inbox/wechat-collect/src_wechat_bf9ce0b38119ed73.md 同步副本不随仓，由管线 promote 流程管理）；
③ 卡重修双副本（00_inbox/wechat-collect/knowledge/ + 00_inbox/pending-cards/ 内
case-wechat-bf9ce0b38119ed73.md，标题「工信部」修正——gitignored 待编排区，按 #380 A 方案流转）；
④ 对照实测+校核记录 `60_feedback/tasks/task_20260904_huangyaoshi-transcribe-quality-model-bump-workdir/对照实测与校核记录.md`
（4 模型矩阵+12 处术语修正证据）；⑤ faster_whisper 失踪根因结论「不可考」+ 防护（import 自检/模型完整性校验/引擎版本入稿头）。

**完成内容**
- 任务1 模型评估：414 号文 222s CPU int8 实测矩阵——tiny 34s 全文乱码 / small 120s 专名错（工信部→公刑部）/
  small+提示 152s 部分修复但数字漂移（2027→2020）/ medium 339s 最优（工信部✓ 2027✓ 12月1号前✓）。
  **零错转实现 = medium 全稿 + 片段级定向复核**（00:27 先导区、02:15/02:31 首购首用、01:52 帕兰提尔均以
  clip_timestamps+术语提示定案）。脚本默认 small，新增 --model medium/tiny + --prompt 术语注入。
- 任务2 414 重转+卡重修：修正逐字稿 12 处术语（对照官方文 414 号 + 片段实测，逐条证据见校核记录）；
  重跑 wechat_knowledge.py 生成新卡（标题=「昨天下午工信部发了一个重磅的行业文件」，关键名词全对），
  修正 LLM 一处自引错（2025→2026 年 12 月 1 日），双副本同步；旧卡移 workdir 留证。
- 任务3 faster_whisper 失踪：pip 无日志、会话无卸载留痕、09-02 05:47 批实为旧 WSL tiny/cuda 链、
  09-04 04:11 三包重装落盘（faster_whisper 1.2.1/ctranslate2 4.8.2/av 18.1.0）→ **结论：不可考**；
  防护已落地（见交付物⑤，另附下载指引 hf-mirror）。

**验证**
- 残错复查：修正稿与卡内 `公刑|新党|手购|西安岛|病单|2025年12` 全零命中；卡内容校验（title/正文/占位）合格。
- 新脚本冒烟：tiny 143s 视频 17s 跑通，稿头含 `引擎: faster-whisper 1.2.1` 指纹。
- 同族对照：5291b61（09-02 05:47「失碎冲鞋」源）tiny→small：整句乱码→可读（当场撕碎重写），同型结论。

**边界**
- Live257 无 whisper 音频实体（文本 Candy），对照改用任务背景同族批实证成员 5291b61。
- 5291b61 逐字稿仍为 tiny 乱码版、30_wiki draft 卡无害——建议另案重转，不在本单。
- 王语嫣归因修正：414 号文 04:13 稿实证为 small 产物非 tiny（tiny=全文乱码级，small=专名级错）——方向结论不变。
- 管线默认仍走 small（--model 未传）；政策/课程类建议调用方显式 --model medium（自动分类另案）。
- 备份避让遵守（无 stash/worktree 操作）；00_inbox 双副本 gitignored 不随仓。

**需要谁动作**
- 欧阳锋：终审 #634；裁定默认模型口径（small 日常 / medium 政策课程类显式调用）是否照此执行。
- 王语嫣：pending-cards case-wechat-bf9ce0b38119ed73 内容已修正重提审——watch_inbox 将按新字节数重登记
  （队列 INBOX-PENDING 行 627/628 旧字节 2880B/5453B 待刷新），按 #380 A 方案走编排门禁入库。
- 老朱/管线侧：如需 5291b61 同族批重转（发现项 2）另案开单。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 2 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（「无日志」）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）
