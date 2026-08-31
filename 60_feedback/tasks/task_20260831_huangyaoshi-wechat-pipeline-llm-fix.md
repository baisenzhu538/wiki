---
id: '584'
title: wechat-collect 管线 DeepSeek 推理模型 max_tokens 修复 + 注册副本路径锚点修复
type: bugfix
status: reviewed
priority: P1
assignee: 黄药师
created_by: 王语嫣
created_at: 2026-08-31
updated_at: '2026-08-31T17:37:37.255447+00:00'
claimed_at: 2026-08-31
source_refs:
- 00_inbox/wechat-collect/_needs_rerun/_done-20260831/case-wechat-68004aecb3d913a5.reason.txt
instance: huangyaoshi
evidence: 60_feedback/tasks/task_20260831_huangyaoshi-wechat-pipeline-llm-fix.md
reviewed_by: 欧阳锋
review_date: '2026-08-31'
grade: A-
---

# #584 wechat-collect 管线 LLM 空总结根因修复（已由王语嫣应急落地，本单做回归+固化）

## 事故经过（2026-08-31 22:09）

老朱视频号采集 2 篇新素材（68004aecb3d913a5 / 346efef2737b383b），自动管线转写✅→骨架✅→**LLM 三层次总结失败**（`<!-- LLM 总结失败，请重试 -->` 占位）→ #380 内容校验正确拦截退回 `_needs_rerun/`。

## 根因（探针实测实锤）

**deepseek-v4-flash 是推理模型**：思考链（reasoning_content）计入 completion_tokens，原脚本 `max_tokens: 1500` 被思考链烧光 → `finish_reason=length, content=''`。02:08 批次能过纯属思考短的运气；22:09 两篇思考长即爆。**不是额度问题**（API 调用成功计费正常）。

## 已应急修复（王语嫣 08-31 晚，git 本 commit）

1. `kdo-tools/wechat_knowledge.py`：max_tokens 1500→8192 + system 提示「直接输出不要思考过程」+ 空 content 显式打印 finish_reason/usage（不再静默落骨架）+ timeout 120→180
2. `40_outputs/code/scripts/wechat_{knowledge,promote}.py` 注册副本：路径锚点 `parent.parent` → 向上搜索 wiki 根（修复产出歪写 `40_outputs/code/00_inbox/` 的 bug），llm_summarize 已同步
3. 5 篇卡（08-31 两篇 + 02:08 遗留 3 篇）重产成功，已补 domain 轴/aliases/discoverable_by 落 `00_inbox/pending-cards/`
4. `_needs_rerun/` 7 件归档至 `_done-20260831/`

## 待黄药师

- [ ] 回归：跑 wechat_knowledge.py --all 全量 15+ 篇，确认无新失败
- [ ] 评估是否需要在管线里对 reasoning 模型换用非推理端点或显式 reasoning_effort 参数
- [ ] 双副本同步机制：kdo-tools/（真身）与 40_outputs/code/scripts/（注册副本）目前手工同步，考虑单一真身+软链或复制时校验
- [ ] 域轴修正（王语嫣 08-31 建议，老朱已批 inbox 自动化）：管线产出 frontmatter 的 `domain: wechat-video` 是来源轴不是知识域轴——建议管线默认写 `domain: pending-domain`，wechat-video 挪进 source_context；真实 domain 由编排层（王语嫣）按内容判定后改写（参照已入库 5 卡先例：strategy/ai-collaboration/kdo）

## 验收标准

- `python kdo-tools/wechat_knowledge.py --all` 0 失败占位
- 40_outputs 注册副本单独调用时产出路径正确

## 执行报告（黄药师 2026-08-31）

- **交付物**
  - `kdo-tools/wechat_knowledge.py`——②参数固化：payload 显式 `thinking: {"type":"disabled"}`（根治）+8192 兜底；skip 判定修复（骨架标记精确匹配替代 `<!--` 泛匹配 + 判定前置到 LLM 调用前）；④域轴：模板 `domain: pending-domain`+`aliases/discoverable_by` 空值占位+来源轴挪 `source_context`
  - `40_outputs/code/scripts/wechat_knowledge.py`——③收口：代码副本→runpy 转发桩（调用即转发 kdo-tools 真身）
  - `40_outputs/code/scripts/wechat_promote.py`——③收口：同上转发桩。旧副本已漂移 3 代（缺 #380 编排门禁/#395 updated_at/#516 隔离区），跑它=绕过王语嫣编排门禁直写 30_wiki/cases/
  - `40_outputs/code/scripts/README.md`——桩语义登记（转发桩非副本、改代码只改真身）
  - `00_inbox/wechat-collect/knowledge/case-wechat-article_1a718b23df7e860b.md`——新管线端到端真跑产出（新 frontmatter 实例）
  - `00_inbox/wechat-collect/knowledge/case-wechat-article_4dd7be7cd82f7e80.md`——同上
  - `00_inbox/pending-cards/case-wechat-article_tt_569e12742cff2c52.md`——管线转正落待编排区（0802 批次遗留卡补转正）

- **完成内容**：四项待办全落地；root cause 文档实锤=DeepSeek 官方 Thinking Mode 指南确认 v4 系默认开思考（effort=high）且烧 completion_tokens。

- **验证**：全部实跑——
  1. 回归：`--all` 17 篇全产 0 失败占位（grep 计数=0）
  2. API 三档实测（68004aec 单篇 3k 字）：baseline reasoning_tokens=69 / **thinking_disabled=0（finish=stop）** / effort_low=519 且不可控 → 禁用思考是唯一根治
  3. 幂等空跑：修复前 97s/白烧 17 次 LLM → 修复后 0.13s/0 次 LLM 调用
  4. 桩转发：双桩分别跑 `--all`/`--dry-run`，转发出真身完整行为（promote 17/17 已流转判定）
  5. 端到端：新管线真跑 2 篇，frontmatter=pending-domain+来源轴入 source_context，yaml.safe_load 全过
  6. 4 个 py 文件 py_compile 通过

- **未做项**（边界说明）：① pending-cards 顶层 23:21 出现 2 张旧模板卡（832f/1a718b，domain=wechat-article）——发现并发写入源在跑同批文件（knowledge/ 23:13-23:25 持续更新），疑似王语嫣侧时钟拍重产。按「在飞不动」纪律未抢写，其 domain 改写走编排层标准流程。② 15 篇已流转旧卡的 domain=wechat-video 未批量改写——canonical 卡在 pending-cards/_processed 已有编排层改写版，管线默认值已修复，存量治理归编排层。③ effort 档位（low/medium/high）对长稿行为未穷举——当前结论只覆盖「机械归纳任务禁用思考」场景。

- **需要谁动作**：欧阳锋按验收标准终审本单；王语嫣侧如有并发时钟拍在跑 wechat 管线，请确认与本次固化版无撞车（其 23:21 产物为旧模板，建议重跑一次 `--all` 用新模板覆盖，或由编排层改写 domain）；后续编排层改写 domain 时可顺手清 `domain: pending-domain` 占位卡。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 7 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）

## 终审记录（欧阳锋 2026-09-01）

**结论：PASS / A-**

### 验收核验（规格对照法，全部欧阳锋独立复跑）

| # | 验收项 | 证据 | 状态 |
|:--|:--|:--|:--|
| 1 | `--all` 0 失败占位 | 亲跑 `python kdo-tools/wechat_knowledge.py --all`：17 篇全部「已知识化，跳过」、0.22s 完成、grep `LLM 总结失败` 0 命中——与执行报告声称的幂等空跑一致 | ✅ |
| 2 | 注册副本单独调用正确 | 双桩亲跑通过（knowledge `--all` 完成 17 个 / promote 转发正常）；runpy 转发路径解析（scripts→code→40_outputs→wiki 根）逐行核对正确 | ✅ |
| 3 | 代码级根因修复 | L94 `thinking: {"type":"disabled"}` 根治 + L92 max_tokens 8192 兜底 + L106-110 空 content 显式报 finish_reason/usage 不静默 + timeout 180 | ✅ |
| 4 | skip 判定前置 | L158-164 判定移到 LLM 调用前 + L52-55 骨架标记精确匹配（SKELETON_MARKERS），`<!--` 泛匹配误判已消除 | ✅ |
| 5 | 域轴修正 | 新管线产出卡 frontmatter 实证：`domain: pending-domain` + `来源轴: wechat-article` 入 source_context（1a718b/4dd7be 双卡抽验） | ✅ |
| 6 | 交付物入仓 | 7 声明路径 git status 全干净，无脏改动（机器预审①差集独立复核通过） | ✅ |
| 7 | git 链路 | bae2b5900 施工 → E040 拦截 → c3d605431 补件 → 3c3424494 预审重挂 → 23:37 重提，链条完整可溯 | ✅ |

### 加分项

- 根治优于止血：待办②原文只要求「评估」，黄药师直接以 API 三档实测（baseline 69 / disabled 0 / effort_low 519）锁定禁用思考为唯一根治并落地
- 转发桩让双副本漂移「结构性不可能」，附旧副本漂移 3 代实证（缺 #380/#395/#516 三代修复）——收口语义准确
- 失败保留旧文件（L177-180）防 `--all` 重跑把好卡降级成骨架，边界考虑周全
- 执行报告「未做项」三条边界如实声明（并发写入不抢写/存量不批量改/effort 档位未穷举）——诚实降级正面样本

### **存在性核查**

| 负向断言 | 核查方法 | 结果 |
|:--|:--|:--|
| 失败占位 0 | `grep -rc "LLM 总结失败" 00_inbox/wechat-collect/knowledge/`，逐文件计数 | 0 命中 |
| `_needs_rerun` 已归档 | `ls 00_inbox/wechat-collect/_needs_rerun/` | 仅 `_done-20260831/` 目录 |
| 交付物无脏改动 | `git status --short` 限定 7 声明路径 | 全部干净 |

### 扣分点（-0.5 → A-）

1. 🟡 同文重复采集未提级：1a718b 与 4dd7be 两卡 title 同为「重构协同：关于AI Native团队的思考」（同文章两次采集、hash 不同）——属采集去重范畴非本单修复引入，但终审发现的相邻问题宜登记。**处置**：记观察项，待王语嫣编排层处置（与执行报告未做项①的并发时钟拍问题同族，一并处理）
2. 🟡 无自动化回归护栏：管线修复验证全靠手工实跑（py_compile 通过但无测试断言），下次改动仍无机器兜底——记停车场（O 系列），另立项最小 smoke 测试单（构造骨架标记样例文件断言 skip 行为）
3. 观察项：用户侧验收指令提及的 `--dry-run` 参数实际不存在（usage 仅 `--all/--output/transcript`）——本终审以 `--all` 幂等空跑达成同等验收语义（0 失败占位核查），不影响结论

### 流转

verdict=pass / grade=A- / reviewed_by=欧阳锋 / review_date=2026-09-01。
