---
id: task_20260906_laowantong-encapsulation-t1
title: "封装复盘 T1 生产：6 件高频基建 skill 壳（queue-transition/launch/复盘链/口述三件套/transcribe/采集面）"
seq: 658
status: in_progress
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 老朱 09-06 晨令「全库封装复盘+基础设施封装化」；报告=diag_20260906_wangyuyan-encapsulation-gap-review
reviewer: 欧阳锋
instance: laowantong
updated_at: '2026-09-06T04:08:18.395463+00:00'
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

## 执行报告（#658，老顽童 2026-09-06）

**交付物**：6 件基建 skill 壳（`40_outputs/capabilities/skills/shared/queue-transition/SKILL.md`、`40_outputs/capabilities/skills/shared/kimi-headless-launch/SKILL.md`、`40_outputs/capabilities/skills/shared/review-chain/SKILL.md`、`40_outputs/capabilities/skills/shared/oral-transcript-trio/SKILL.md`、`40_outputs/capabilities/skills/shared/transcribe-win/SKILL.md`、`40_outputs/capabilities/skills/shared/intake-registry/SKILL.md`）+ 目录索引刷新（`40_outputs/capabilities/skills/INDEX.md` / `40_outputs/capabilities/skills/MOUNT-MATRIX.md` / `40_outputs/capabilities/skills/SKILL-HEALTH.md`，`python 40_outputs/code/scripts/scan_skills_registry.py` 生成物，79→85）

**完成内容**：按诊断报告 T1 清单逐件封装——①queue-transition：六动作全命令+参数表、task_id vs seq 寻址（#645 坑/#647 修）、--sequence（#655）与 --force 台账（#444）、F-034 五字段锚词与 E040 入仓口径（--evidence 传文件禁内联，#615/#624/#638/#640 四次实证）、complete 后 30 秒回验（L9）；②kimi-headless-launch：通道-真实模型对照表（claude=GLM glm-5.3-flash / codex=relay→deepseek-v4-pro / kimi=k3 / hermes=上游 kimi）、探针形态、fallback 同上游去重、全死 exit 2 不硬派、0 字节日志与 HERMES_PROFILE 坑（#650）；③review-chain：11 章标题清单、A🟢/B🟡/C🔴 判级硬指标、--file 优先姿势、双写落盘路径；④oral-transcript-trio：scan-demo-sections（17 信号词/--compile/怀疑区）+ transcript-index（build/search、`_processed/` 落点）+ W1 逐字读红线（P-31 锚点）；⑤transcribe-win：三档模型选档纪律（tiny 政策类乱码）、--prompt 收益与数字漂移副作用、RTF 实测耗时预算与 #649 动态 timeout 语义、镜像下载；⑥intake-registry：watch_inbox 扫描面/登记段结构/SOFT_CAP/--seed-top-dirs 风险 + conveyor_probe 只登记不流转边界/--dry-run/--json + E059 逐行身份核验划销纪律。每件均含：何时用/怎么调（命令+参数）/边界与红线/常见坑（症状→修复）/失败模式/相关协议锚点；frontmatter 带 `trigger.natural_language` 触发词（检索路由可用面）。全部未改任何脚本本体。

**验证**：狗粮实测 6/6 通过——①`queue_transition.py status`+`myqueue laowantong`：名下 #658 显示「🚧 进行中」（输出见本单下方实测记录）；②`kimi-headless-launch.py laowantong "…" --force-dead kimi,claude,codex,hermes`：exit 2 全死不硬派、hermes 未重复探测（同上游去重生效）、`logs/channel-health.log` 12:21:00 留痕；③`review-check.py --agent laowantong`：🟡 B级 16105B 11/11章「未达A: epiphany_reversal」；④`scan-demo-sections.py` 实测宣讲会口述稿命中 32 处 + `transcript-index.py build`（712 段/4643 关键词）+ `search 封装`（命中 L340/L552）；⑤`transcribe_win.py --model tiny` 真实转写 SAPI 合成中文音频 exit 0，产出 3 段带时间戳+头部指纹（tiny 乱码如「老丸同的专写够凉石测」反证选档纪律）；⑥`watch_inbox.py` 手工一拍 exit 0 静默（无新素材）+ `conveyor_probe.py --dry-run --json` stdout 纯 JSON、登记 friction 线索 +3、通知只打印不发送。6 件 SKILL.md `kdo pre-submit` 全部 ✅ PASS；`scan_skills_registry.py` 复跑 INDEX.md 85 skills 含 6 件新条目（#37/#39/#44/#47/#65/#80）。

**边界**：只写封装层，8 个底层脚本（queue_transition.py/kimi-headless-launch.py/channel_health.py/daily-context-save.py/review-check.py/scan-demo-sections.py/transcript-index.py/transcribe_win.py/watch_inbox.py/conveyor_probe.py）零改动；拉起器未做真实拉起测试（避免无单硬拉一个 agent，用脚本自带的 --force-dead 测试钩验证预检/fallback/全死路径）；transcribe 狗粮用 11 秒合成音频验证调用链与产出格式，非真实长视频质量验收（#634/#649 实测数据引自任务单原文未复跑）；`90_control/channel-model-map.md` 在 kimi-headless-launch.py docstring 与 #656 任务单中被引用但 vault 内不存在（`find . -name "channel-model-map*"` 仅 3 处引用 0 实体，2026-09-06 核查）——skill 内已注明以脚本 TOOLS 表注释+channel_health.TOOL_UPSTREAM 为准，未擅自补文件。

**需要谁动作**：欧阳锋终审本批 6 壳（审查锚点：狗粮实测记录+pre-submit 输出）；黄药师另立微单两件——①补落 `90_control/channel-model-map.md` 认知表（#656 任务单第 3 条验收遗留，relay 与 claude.exe 是否同 GLM 账号需核实）②pre-submit 对 SKILL.md 类文件的 `title`/`tags:audience:scene:` 必填口径未写进任何登记文档（本次靠报错文案摸索，建议入 `90_control/tool-card-excellence-standard.md` 或 skills README）；王语嫣裁量：6 壳是否按 INDEX.md「挂载现状」口径挂进各角色 spec（现均为「无主」，属登记制引用即挂载，待定向）。

## 狗粮实测记录（新 agent 视角：不读 context，仅凭 SKILL.md 命令执行）

| # | skill | 实测命令（照抄 SKILL.md） | 结果 |
|:--|:--|:--|:--|
| 1 | queue-transition | `python 90_control/scripts/queue_transition.py status` / `… myqueue laowantong` | ✅ 队列 251 总数/1 queued/1 claimed/1 pending_review；myqueue 显示 #658 🚧 进行中 |
| 2 | kimi-headless-launch | `python 90_control/scripts/kimi-headless-launch.py laowantong "…" --force-dead kimi,claude,codex,hermes` | ✅ exit=2「全死不硬派」；探测明细 hermes「同上游 kimi 已判定，未重复探测」；logs/channel-health.log 12:21:00 一行 JSON（decision=laowantong->全死不硬派）；todos 落 3 行【通道预检 #656】（已加注记：测试钩非真实故障） |
| 3 | review-chain | `python kdo-tools/review-check.py --agent laowantong` | ✅ 「laowantong 🟡 B级 (16105B) — 11/11章 ✅已检索，未达A: 深度未过: epiphany_reversal」 |
| 4 | oral-transcript-trio | `python kdo-tools/scan-demo-sections.py "00_inbox/AI大航海20260905/宣讲会：一堂-2026下半年AI大航海-口述.txt"`；`…transcript-index.py build <同稿>`；`…search <同稿> 封装` | ✅ 命中 32 处操作演示段（L76/L134/L138…带信号词+上下文）；build 产出 `_processed/…_索引.json`+`_主题索引.md`（712 段/4643 关键词）；search「封装」命中 L340/L552 并加粗高亮 |
| 5 | transcribe-win | `python kdo-tools/transcribe_win.py "_tmp/dogfood_transcribe.wav" "_tmp/dogfood_transcribe_稿.md" --model tiny`（SAPI Huihui 合成 11s 中文音频） | ✅ exit=0，3 段带 [mm:ss] 时间戳+头部指纹（模型/引擎 1.2.1/耗时 2s）；tiny 乱码实证（「老顽童的转写狗粮实测」→「老丸同的专写够凉石测」）反证选档纪律 |
| 6 | intake-registry | `python kdo-tools/watch_inbox.py`；`python kdo-tools/conveyor_probe.py --dry-run --json` | ✅ watch_inbox exit 0 静默（无新素材，与计划任务同命令幂等）；conveyor_probe stdout 纯 JSON（new_queued/registered/near_miss/notified 字段齐全）、friction 线索 +3 登记 PROPOSAL-PENDING、通知仅打印未发送 |

> 狗粮口径：仅凭各 SKILL.md 的「怎么调」节命令执行，未借助 context 文件/源码阅读；实测过程与输出锚点如上，产物 `_tmp/dogfood_transcribe*.wav/md` 与 `_processed/` 索引留档可复跑。
