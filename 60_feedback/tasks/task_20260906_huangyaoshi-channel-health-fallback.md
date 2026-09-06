---
id: task_20260906_huangyaoshi-channel-health-fallback
title: "拉起器通道健康预检+余额感知 fallback（F-073 落地：kimi 403/codex 余额尽两墙连撞的工具化根治）"
seq: 656
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 老朱 09-06 晨问（欧阳锋 glm-5.3-flash 怎么会没额度？是否都自动切 kimi 没发现？）——一晚连撞两道额度墙的根治
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-06T04:16:09.107349+00:00'
evidence: logs/channel-health.log
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

## 执行报告（黄药师 2026-09-06 12:15）

**交付物**
- `90_control/scripts/channel_health.py`（新增，探针引擎：claude/codex HTTP 探针 + kimi CLI 探针 + hermes 同上游连坐判定 + 状态码分类 + `logs/channel-health.log` JSONL 台账）
- `90_control/scripts/kimi-headless-launch.py`（改造：预检→fallback→全死不硬派；新增 `--no-probe`/`--force-dead` 测试钩；stdout 钉 UTF-8 对齐 clock_watchdog 飞书契约；notify 失败降级告警不静默）
- `90_control/scripts/tests/test_channel_health_656.py`（新增 11 用例）
- `90_control/channel-model-map.md`（新增，认知表：CLI→真实供应商→模型→key 指纹→探针→核对命令）
- `.agent/infrastructure-bulletin.md`（新增 09-06 基建变更公告节）

**完成内容**
- 修法①预检：launch 前对 fallback 链逐通道打最小探针，401/402/403/429=上游级不健康（同上游连坐）、5xx/不可达/超时=工具级不健康（不连坐）；探针形态全部实弹验证：GLM 正 key 200/1.2s、坏 key 401/0.1s，relay `/v1/responses` 200/0.9s，kimi CLI 403 快败 2.7s
- 修法②fallback：首个健康通道拉起；主通道死→自动切+todos/stdout 双通知；全死→exit 2 不 spawn+报王语嫣+给 `--no-probe` 应急出口；fallback 链 claude→codex→kimi→hermes，**按上游去重**（新发现：hermes 上游=kimi 同一堵墙，`~/.hermes/config.yaml` 实证，kimi 403 时 hermes 同死，不撞二遍墙）
- 修法③认知表：四条给定事实全落表；任务单遗留核实项闭环——**relay 不是 GLM、与 claude.exe 不同供应商不同账号**【实证：relay 进程命令行 `--upstream https://api.deepseek.com/v1 --api-key sk-…b2f0`（PID 161248）】；指纹约定破案=`sha256(key)[:8]+'…'+key[-4:]`（两条 key 均重算吻合：GLM `1cdfd9b3`、deepseek `1511248f`）
- 附带生产实证：12:07:16 王语嫣拉 laowantong 时预检已实战生效——kimi 真实撞 `403 weekly usage limit`→自动切 claude（`logs/channel-health.log` 首行）

**验证**
- 单测：`pytest 90_control/scripts/tests/ -q` → **273 passed**（含新增 11 + #650 回归 3），现有回归不红
- 验收①实测：`launch huangyaoshi --force-dead kimi` → rc=0、通知「kimi 不健康→已切 claude（上游 zhipu-glm）」、真实拉起 claude.exe 会话跑完（`logs/headless-huangyaoshi-20260906-120756.log` 尾=`通道fallback验收OK`）
- 验收②实测：`--force-dead claude,codex,kimi,hermes` → rc=2、零进程 spawn、todos+stdout 落「不硬派——报王语嫣处置」+应急出口
- 验收③（坏 key 路径）：GLM 端点+假 key 实弹 401 判死（单测 `test_bad_key_real_endpoint_classified_unhealthy`）

**边界**
- relay 不校验调用方 key（坏 Bearer 仍 200，实测）——codex 通道的坏 key 模拟只能走 `--force-dead` 钩子或上游 key 死，无法从本地伪造 401
- kimi 通道只能 CLI 级探针：OAuth token 15min 一换，HTTP 探针必撞过期 401 假阴性（已实测）；代价是 kimi 探针 ~3s（快败）/健康时更久
- 探针每次 launch 都实发（无缓存）：单次成本 1-token 级（GLM/DeepSeek 各一次 ≈ 可忽略）；daily_review 的 60s 子进程超时预算内（实测预检+决策 <10s）
- todos 通知是 best-effort：12:07:16 laowantong 那条生产通知未落账（写失败被吞或被并发会话全文件重写冲掉，无法回溯判定【推断】）——已把写失败从静默改为 stdout 告警；**台账以 `logs/channel-health.log` 为准**
- hermes 无独立探针（上游=kimi 按 dedup 判定）；未登记角色默认回落 kimi 链（沿用原行为）

**需要谁动作**
- 欧阳锋：终审本单（重点裁三处：①fallback 链顺序 claude 优先是否符合你的异构防线口径；②全死时 exit 2 报你/王语嫣的送达面是否够；③`--no-probe` 应急口子留不留）
- 王语嫣：认知表 `90_control/channel-model-map.md` 收入值守口径——**报通道连报真实供应商+模型**；hermes 在 kimi 周额度窗内不要再排为 fallback
- 老朱：无（信息知悉即可：两堵墙互相独立，deepseek 复活≠kimi 复活，kimi 7 天窗内黄药师/老顽童线自动走 GLM）

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 6 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
