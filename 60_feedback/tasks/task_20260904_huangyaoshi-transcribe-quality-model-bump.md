---
id: task_20260904_huangyaoshi-transcribe-quality-model-bump
title: 转写质量升级：tiny→small/medium 模型评估切换（「公刑部/新党区/手购所用」关键名词错转实证）+ faster_whisper 失踪根因
seq: 634
status: reviewed
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-04
decision_source: 老朱 09-04 凌晨链路验证：414号文视频转写成功但关键名词全错（tiny 模型中文错字族，同族 09-02 05:47 批「失碎冲鞋」）——王语嫣门禁判定退回重转
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-03T21:17:15.161416+00:00'
evidence: 60_feedback/tasks/task_20260904_huangyaoshi-transcribe-quality-model-bump-workdir/对照实测与校核记录.md
reviewed_by: 欧阳锋
review_date: '2026-09-03'
grade: A-
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

## 终审记录

**终审结论**：PASS A-（欧阳锋 · 2026-09-04 · methodology_version v2.3）
**阻断判定**：无 Critical / High 阻断项；机器预审③④ 🔴 已核销（锚点在证据文件 §三，见下）；1 处低优先级改进点（放行）
**五维评分**：溯源完整 24/25 · 逻辑骨架 24/25 · 暗知识密度 18/20 · 可操作性 15/15 · 表达质量 13/15 → 94（A-）

**O0 溯源**：已打开证据文件 `60_feedback/tasks/task_20260904_huangyaoshi-transcribe-quality-model-bump-workdir/对照实测与校核记录.md`，并核验交付物实体——
① `kdo-tools/transcribe_win.py` v2（git 56bc82eda 已入仓）：`--model/--prompt` 参数、`check_import` 前置自检、`resolve_model` 完整性校验（model.bin 尺寸阈值禁静默降级）、引擎版本指纹入稿头——四处与执行报告交付物⑤一致；
② `10_raw/sources/src_2026-09-04_wechat_bf9ce0b38119ed73.md`：基底 medium 全稿 + header 校核注「#634 术语修正 12 处」，12 处修正逐条与校核记录表对位（先导区/90天/供给端/帕兰提尔/首购首用×2/政府侧/区县/千万级/订单/发令枪/硬造〔疑〕），其中 6 处与官方文 414 号对位；
③ 卡双副本（pending-cards + wechat-collect/knowledge）标题「昨天下午工信部发了一个重磅的行业文件」、正文「工信部/首购首用/订单」关键名词全对；
④ 残错复查实测：`公刑|新党|手购|西安岛|2025年12` 在修正稿与两卡副本零命中（「病单」仅出现在订单修正注的括注说明内，属应留的疑注非残错）。

**存在性核查**（负向断言闭环 + 交付物存在性）：
- 机器预审③④ 🔴「无日志」核销：该负向断言的 `**存在性核查**` 锚点位于证据文件 §三，四查闭环——①Windows pip 无日志（%LOCALAPPDATA%/pip 仅 cache、%APPDATA%/pip 不存在、pip config list 无日志配置）；②全部 logs + 09-02/09-03 session-archives grep uninstall 零命中；③site-packages 三包 mtime 全 09-04 04:11（重装时刻）；④pip 轮子缓存无 faster 轮子。→ #433 实质（负向判词必须附核查节）已满足，放行。
- 交付物五件（①脚本②重转稿③卡双副本④校核记录⑤根因结论+防护）全部存在；脚本已 git 跟踪无脏改动，00_inbox 双副本 gitignored 按 #380 A 方案流转（符合声明）。
- 结论「不可考」为诚实口径：四查无果后不臆造归因，且补 import 自检/模型完整性/版本指纹三道防护——正确。

**审查裁定（生产方提出的三边界 + 王语嫣归因修正）**：
1. Live257 无 whisper 音频实体、对照改用同族批 5291b61——**接受**：5291b61 与「失碎冲鞋」同源、143s 可实测，对照样本成立。
2. 5291b61 逐字稿仍为 tiny 乱码版、30_wiki draft 卡无害——**接受**：不引用乱码行即无污染，另案重转（发现项 2）不占本单。
3. 王语嫣归因修正（414 号文 04:13 稿为 small 非 tiny）——**接受**：对照矩阵实证 tiny=全文乱码级、small=专名级错，方向结论（tiny 不可用、需 medium）不变，归因修正如实入档。
4. 默认 small / 政策课程类显式 --model medium 口径——**裁定**：照此执行（脚本默认 small 已落地；自动按内容分类选模另案）。

**改进点（低优先级，放行）**：
1. 执行报告「完成内容」的负向断言「无日志/会话无卸载留痕」未内联 `**存在性核查**` 锚点（锚点在证据文件 §三）——机器预审③④ 因此 🔴。实质已闭环、不构成返工；生产侧后续同类负向断言可顺手把锚点或「见证据文件 §三」指引内联进执行报告节，便于机器预审一次命中。
2. 修正稿 header 以「校核: #634 术语修正 12 处」替代 v2 脚本的「引擎: faster-whisper X.Y.Z」指纹（冒烟稿 smoke-tiny.md 已含指纹）——修正稿为人工定稿，可接受；后续重转定稿可顺手保留引擎指纹行便于漂移对照。

**需要谁动作**：王语嫣——pending-cards case-wechat-bf9ce0b38119ed73 内容已修正，watch_inbox 按新字节重登记后走 #380 A 方案编排门禁入库；老朱/管线侧——5291b61 同族批重转（发现项 2）另案开单；黄药师（可选）——下批顺手修订上述两处低优先级改进点。
