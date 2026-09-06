---
id: task_20260906_huangyaoshi-channel-health-fallback

title: "拉起器通道健康预检+余额感知 fallback（F-073 落地：kimi 403/codex 余额尽两墙连撞的工具化根治）"

seq: 656

status: reviewed
assignee: huangyaoshi

created_by: wangyuyan

created_at: 2026-09-06

decision_source: 老朱 09-06 晨问（欧阳锋 glm-5.3-flash 怎么会没额度？是否都自动切 kimi 没发现？）——一晚连撞两道额度墙的根治

reviewer: 欧阳锋

instance: huangyaoshi

updated_at: '2026-09-06T04:42:38.858919+00:00'
evidence: logs/channel-health.log
reviewed_by: 欧阳锋
review_date: '2026-09-06'
grade: A-
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
## ????

### ?????? 2026-09-06 12:38????? PASS?A-?

> methodology_version: v2.3 ? verdict: PASS ? grade: A- ? blocking: ????2 ??+TODO?? residual_risks: M1/M2/L1/L2/L3??????????

**????????????**

1. **? ????? ?????**?`channel_health.py` ?????????????????????claude=HTTP POST `{base}/v1/messages` max_tokens=1?`probe_claude`??codex=HTTP POST `relay/v1/responses` max_output_tokens=16?`probe_codex`??kimi=CLI ? `kimi.exe -p`?`probe_kimi`?OAuth ? CLI ???????? HTTP ????? 401 ????????`classify_status` ?? 401/402/403/429=upstream?5xx/???/??=tool?200+DEAD_KEYWORDS=upstream ??????? `TOOL_UPSTREAM` ??? + `probe_chain`??? exit 2 ??? `main()` ? `select_channel?None?notify?return 2` ? spawn?
2. **? fallback ?? ?????**?`logs/channel-health.log` ????????12:07:16 `laowantong->claude`?kimi ?? 403 weekly limit ? ??? GLM?????????12:05:33/12:07:56 `huangyaoshi->claude`?`--force-dead kimi`??12:08:29/12:21:00????????12:23:48 `ouyangfeng->codex`????????????????codex ??????kimi 403 ????`logs/headless-huangyaoshi-20260906-120756.log` ?=`??fallback??OK`??? claude.exe ??????todos ???????`90_control/todos/huangyaoshi.md`/`laowantong.md` ?????? #656?????
3. **? ???????? ????????? + ? 5 ??????????**?
   - ?1 claude=GLM??? `~/.claude/settings.json` env ? base_url=`https://open.bigmodel.cn/api/anthropic`?model=`glm-5.3-flash`?token ???? `1cdfd9b3?uOra` ?????
   - ?2 codex=DeepSeek?relay ?? PID 161248 ????? `codex-relay --port 4444 --upstream "https://api.deepseek.com/v1" --api-key "sk-?b2f0"`?deepseek key ???? `1511248f?b2f0` ???model=`deepseek-v4-pro` ? channel-health.log ????? `"model":"deepseek-v4-pro"` ???
   - ?3 kimi??? `~/.kimi-code/config.toml` managed:kimi-code ? base_url=`https://api.kimi.com/coding/v1`?api_key ??OAuth ??????
   - ?4 hermes=kimi??? `~/.hermes/config.yaml` ? provider=`kimi-coding`?base_url=`https://api.kimi.com/coding/v1`??????
   - ?5 MiniMax?????????????? `POST https://api.minimaxi.com/v1/text/chatcompletion_v2`??? key ? `~/.kdo/config.yaml`?? 200?model=`MiniMax-M3`?usage.total_tokens=186?max_tokens=8??????199 tokens ?? 200?????????? key status 1008?? `60_feedback/session-archives/2026-09-06/hongqigong.md` + ??? `???_20260906_minimax?????????.md` ???
4. **? ???? ?????**???????? `python -m pytest 90_control/scripts/tests/ -q` ? **273 passed????**?37.65s????????????`test_channel_health_656.py` 11 ????? 11 passed?

**??????**

1. **fallback ? claude ?? ? ??**??????????=?1??? ??????09-05 ??????? GLM ?????+ deepseek ?????? + kimi/hermes ?????????????????ouyangfeng ???=codex/deepseek ??? kimi/GLM ????kimi 7 ??? huangyaoshi+laowantong ?? GLM ?????????????????
2. **?? exit 2 ??? ? ?**?????`notify()` ???=stdout???????? DM?+ todos ???exit 2 ? 0 ???? stdout?stdout ??????????todos ??????12:08/12:21 ???????????????=?????? stdout????????????????????
3. **--no-probe ??? ? ?**??????? flag?????????????????????????????? exit 2?????????????? override ?????????

### ??????? + TODO?

- ?? M1?`probe_chain` ??????????????scope???kimi ??? tool ???CLI ???/???scope=tool??hermes ??????`ProbeResult(tool, prev.healthy, prev.scope, "?????????")`??? hermes ?????????? api.kimi.com ????docstring ????????????????????? scope??? `test_tool_level_failure_does_not_condemn_same_upstream` ? codex(deepseek)+kimi(kimi) ??????????? tool ??????????????**??/TODO**????????? `channel_health.py`???? `and upstream_verdict[up].scope == "upstream"` + ???? tool ?????
- ?? M2?`probe_codex` ? scope=upstream ?????????? tool?`if r.scope == "upstream": r.scope = "tool"`???? relay ????? `_post_json` ????????? tool???????? relay ???**??? deepseek ??**?402 ???/401/403/429???????????deepseek ????????????????????????????????????**??/TODO**??????????????relay ?????? classify 5xx/????????
- ?? L1?channel-model-map ?5?MiniMax?key ?????????key ???????????????????=`e0f4018e?oFdc`??**??**????????
- ?? L2??5 ????12:40 ??+?????????`~/.kdo/config.yaml` mtime=12:21:58?`channel-model-map.md` mtime=12:23:23?git commit `86b25e922`=12:25:58???? 12:40??**??**??????????????
- ?? L3?`~/.kdo/config.yaml` minimax base_url=`/v1`?????????? VLM ?? base_url=`https://api.minimaxi.com/anthropic`?Anthropic ?????????? config note ??????????????**??**????/???????????? config ????

### **?????**

- ??5 ????????grep `channel-model-map.md` ?5 key ?=`?? key ? ~/.kdo/config.yaml minimax ??` ? `?` ????????????? `sha256[:8]??4`?
- ?12:40 ?????????`Get-Item ~/.kdo/config.yaml` LastWriteTime=12:21:58?`Get-Item 90_control/channel-model-map.md` LastWriteTime=12:23:23?`git log --format=%h%ad` 86b25e922=12:25:58???? `Get-Date` ??=12:27:24?
- ?M1 tool ???????`channel_health.py` `probe_chain` ???? `if up in upstream_verdict:`?? scope ????`probe_kimi` ?? scope=tool ?????CLI ??/?????
- ?M2 ???????`channel_health.py` `probe_codex` ? `if r.scope == "upstream": r.scope = "tool"`?`_post_json` ??????? scope=tool?URLError/??/??????
- ?????????grep `00_inbox --include=*.py` ?? `base_url="https://api.minimaxi.com/anthropic"` ???`~/.kdo/config.yaml` minimax.base_url=`https://api.minimaxi.com/v1`?

### ??

???????????? / fallback ?? / ?????? / ?? 273 ??????????????? 2 ??tool ??? M1?relay ????? M2??? + ??????????? 3 ??5 ??????????? **PASS??? A-**?

## 终审记录

### 终审（欧阳锋 2026-09-06 12:38）——判定 PASS（A-）

> methodology_version: v2.3 ｜ verdict: PASS ｜ grade: A- ｜ blocking: 无（🟠2 放行+TODO）｜ residual_risks: M1/M2/L1/L2/L3（见「发现问题」节）

**四核裁定（逐条独立核验）**

1. **① 预检真实现 ✅【实证】**：`channel_health.py` 全文逐行核——三探针形态与任务单口径一致：claude=HTTP POST `{base}/v1/messages` max_tokens=1（`probe_claude`）、codex=HTTP POST `relay/v1/responses` max_output_tokens=16（`probe_codex`）、kimi=CLI 级 `kimi.exe -p`（`probe_kimi`，OAuth 由 CLI 自刷，注释交代 HTTP 探针撞过期 401 假阴性原因）；`classify_status` 分 401/402/403/429=upstream、5xx/不可达/超时=tool、200+DEAD_KEYWORDS=upstream 死；同上游去重 `TOOL_UPSTREAM` 四映射 + `probe_chain`；全死 exit 2 分支在 `main()` 内 `select_channel→None→notify→return 2` 不 spawn。
2. **② fallback 实测 ✅【实证】**：`logs/channel-health.log` 七条实账互证——12:07:16 `laowantong->claude`（kimi 真实 403 weekly limit → 自动切 GLM，生产实战首行）、12:05:33/12:07:56 `huangyaoshi->claude`（`--force-dead kimi`）、12:08:29/12:21:00「全死不硬派」、12:23:48 `ouyangfeng->codex`（本次终审会话自身拉起即走预检：codex 主通道健康、kimi 403 判死）；`logs/headless-huangyaoshi-20260906-120756.log` 尾=`通道fallback验收OK`（真实 claude.exe 拉起跑完）；todos 通知落账在场（`90_control/todos/huangyaoshi.md`/`laowantong.md` 的【通道预检 #656】条目）。
3. **③ 台账五行实证质量 ✅（前四行本机回验 + 第 5 行独立探针）【实证】**：
   - 行1 claude=GLM：实读 `~/.claude/settings.json` env → base_url=`https://open.bigmodel.cn/api/anthropic`、model=`glm-5.3-flash`、token 指纹重算 `1cdfd9b3…uOra` 与表吻合。
   - 行2 codex=DeepSeek：relay 进程 PID 161248 命令行实取 `codex-relay --port 4444 --upstream "https://api.deepseek.com/v1" --api-key "sk-…b2f0"`；deepseek key 指纹重算 `1511248f…b2f0` 吻合；model=`deepseek-v4-pro` 由 channel-health.log 探针响应体 `"model":"deepseek-v4-pro"` 实证。
   - 行3 kimi：实读 `~/.kimi-code/config.toml` managed:kimi-code → base_url=`https://api.kimi.com/coding/v1`、api_key 空（OAuth 自刷）佐证。
   - 行4 hermes=kimi：实读 `~/.hermes/config.yaml` → provider=`kimi-coding`、base_url=`https://api.kimi.com/coding/v1`，同墙成立。
   - 行5 MiniMax（王语嫣增补）：本机独立探针 `POST https://api.minimaxi.com/v1/text/chatcompletion_v2`（订阅 key 自 `~/.kdo/config.yaml`）→ 200、model=`MiniMax-M3`、usage.total_tokens=186（max_tokens=8），与行内「199 tokens 实测 200」口径一致；「按量旧 key status 1008」由 `60_feedback/session-archives/2026-09-06/hongqigong.md` + 建议书 `建议书_20260906_minimax额度耗尽多模态管线.md` 佐证。
4. **④ 回归不红 ✅【实证】**：本会话独立复跑 `python -m pytest 90_control/scripts/tests/ -q` → **273 passed，零失败**（37.65s），与执行报告口径一致；`test_channel_health_656.py` 11 用例单独跑 11 passed。

**三条待裁裁决**

1. **fallback 链 claude 优先 → 同意**【推断→实证】：依据=行1「🟢 全夜存活」（09-05 夜全通道连死时 GLM 唯一存活）+ deepseek 充值复活次之 + kimi/hermes 同墙排最后；异构防线在角色层保持（ouyangfeng 主通道=codex/deepseek 独立于 kimi/GLM 两线），kimi 7 天窗内 huangyaoshi+laowantong 收敛 GLM 属可接受降级，已写「需要谁动作」。
2. **全死 exit 2 送达面 → 够**【实证】：`notify()` 双通道=stdout（时钟契约→飞书 DM）+ todos 落账；exit 2 非 0 退出不吞 stdout（stdout 为流与退出码无关）；todos 实账已在场（12:08/12:21 两条「全死不硬派」）。残留依赖=拉起方须捕获 stdout（王语嫣编排侧按契约已覆盖），无需加码。
3. **--no-probe 应急口 → 留**【推断】：显式 flag、默认不触发、文档化；为预检自身故障时的人工逃生门，与「全死 exit 2」不冲突（默认仍拦，仅人显式 override 才直通）。风险低。

### 发现问题（放行 + TODO）

- 🟠 M1：`probe_chain` 同上游去重按「上游名」而非「scope」——kimi 探针若 tool 级死（CLI 起不来/超时，scope=tool），hermes 被连坐判死（`ProbeResult(tool, prev.healthy, prev.scope, "同上游…未重复探测")`），而 hermes 是独立可执行体、上游 api.kimi.com 未必死；docstring 写「上游级死亡的墙不撞第二次」但实现不区分 scope。用例 `test_tool_level_failure_does_not_condemn_same_upstream` 用 codex(deepseek)+kimi(kimi) 不同上游，未覆盖同上游 tool 级场景，用例名与覆盖不一致。**落点/TODO**：黄药师后续微单修 `channel_health.py`（判定加 `and upstream_verdict[up].scope == "upstream"` + 补同上游 tool 级用例）。
- 🟠 M2：`probe_codex` 对 scope=upstream 的死结果无条件降级为 tool（`if r.scope == "upstream": r.scope = "tool"`）——但 relay 挂时走的是 `_post_json` 异常分支，天然已是 tool；该分支只会命中 relay 透传的**真上游 deepseek 错误**（402 余额尽/401/403/429），把本任务要根治的「deepseek 余额墙」误标成工具级，台账语义与认知表目标（报通道连报真实供应商）相抵。**落点/TODO**：黄药师后续微单删该降级块（relay 自身故障已由 classify 5xx/异常路径覆盖）。
- 🔵 L1：channel-model-map 行5（MiniMax）key 未记指纹（表纪律「key 一律只记指纹」，其余四行均记；本机重算=`e0f4018e…oFdc`）。**落点**：王语嫣补指纹。
- 🔵 L2：行5 时间戳「12:40 挂载+实测」与证据矛盾（`~/.kdo/config.yaml` mtime=12:21:58、`channel-model-map.md` mtime=12:23:23、git commit `86b25e922`=12:25:58，均早于 12:40）。**落点**：王语嫣更正为实际挂载时间。
- 🔵 L3：`~/.kdo/config.yaml` minimax base_url=`/v1`（原生）与既有洪七公 VLM 脚本 base_url=`https://api.minimaxi.com/anthropic`（Anthropic 兼容）端点不一致，但 config note 称「洪七公管线统一读此段」。**落点**：王语嫣/洪七公确认规范端点后对齐 config 或脚本。

### **存在性核查**

- 「行5 指纹未记」核查：grep `channel-model-map.md` 行5 key 列=`订阅 key 挂 ~/.kdo/config.yaml minimax 段…` 无 `…` 指纹形态；对比其余四行均有 `sha256[:8]…尾4`。
- 「12:40 与证据矛盾」核查：`Get-Item ~/.kdo/config.yaml` LastWriteTime=12:21:58、`Get-Item 90_control/channel-model-map.md` LastWriteTime=12:23:23、`git log --format=%h%ad` 86b25e922=12:25:58；本会话 `Get-Date` 当时=12:27:24。
- 「M1 tool 级连坐」核查：`channel_health.py` `probe_chain` 判定行为 `if up in upstream_verdict:`（无 scope 条件）；`probe_kimi` 存在 scope=tool 返回分支（CLI 超时/起不来）。
- 「M2 降级块」核查：`channel_health.py` `probe_codex` 含 `if r.scope == "upstream": r.scope = "tool"`；`_post_json` 异常分支已返回 scope=tool（URLError/超时/连接拒绝）。
- 「端点漂移」核查：grep `00_inbox --include=*.py` 命中 `base_url="https://api.minimaxi.com/anthropic"` 多处；`~/.kdo/config.yaml` minimax.base_url=`https://api.minimaxi.com/v1`。

### 结论

核心四核全过（预检真实现 / fallback 实测 / 台账五行实证 / 回归 273 绿），三条待裁裁决均同意；🟠 2 项（tool 级去重 M1、relay 上游误降级 M2）放行 + 黄药师后续微单修，🔵 3 项行5 细节由王语嫣补齐。判定 **PASS，等级 A-**。
