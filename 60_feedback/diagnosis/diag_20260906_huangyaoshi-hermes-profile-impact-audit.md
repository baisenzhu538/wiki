---
id: diag_20260906_huangyaoshi-hermes-profile-impact-audit
type: diag
status: draft
author: 黄药师
reviewed_by: ""
created_at: 2026-09-06
updated_at: 2026-09-06
source_refs:
- 90_control/scripts/kimi-headless-launch.py
- 60_feedback/diagnosis/diag_20260906_duanwangye-hermes-headless-profile-flag.md
- logs/headless-laowantong-20260903-010947.log
related:
- "[[kimi-headless-launch]]"
---

# 建议书：hermes 通道历史影响面核查（#650 任务 2，报王语嫣转老朱知情）

## 结论一句话

09-03 01:09–11:09 之间经 hermes 通道拉起的 **11 个会话全部错载黄药师的 hermes profile**（环境变量机制失效所致，fix 见 #650 修一）；KDO 层身份未串（实例自称、队列身份、todos 落款均为老顽童），污染面在 hermes 层——会话记录进了黄药师 profile 的库、加载了黄药师的 SOUL/skills/config 上下文。

## 机制（源码级，非推测）

hermes 无头 profile 解析链（`hermes_cli/main.py::_apply_profile_override`）依次只认：
1. argv `-p/--profile` flag（生效）
2. `%LOCALAPPDATA%\hermes\active_profile` sticky 文件（**当前值=huangyaoshi，mtime 2026-09-02 00:09:25**）
3. `HERMES_HOME` env 且指向 profiles/<name> 目录

`HERMES_PROFILE` 环境变量**整条链都不读**（仅 kanban worker 用它当作者标签）。旧拉起器 `TOOL_ENV={"hermes":{"HERMES_PROFILE":"{role}"}}` 因此是死配置。

**今日双实测**（黄药师复跑）：
- 阴性对照：`HERMES_PROFILE=skills-assistant hermes -z "你加载的profile名"` → 自称 **huangyaoshi**（错载 active_profile）
- 修复后狗粮：拉起器 `-p skills-assistant` 拉起 → 自称 **skills-assistant**（职能自述精确命中）

## 权威清单（09-02~09-03 窗口，来源=各 profile `state.db` sessions 表，非日志抽样）

| 时间 | 意图角色 | 实际落点 profile | 判定 | 对应工作 |
|:--|:--|:--|:--|:--|
| 09-02 00:08/00:09（3 会话） | 王语嫣 | wangyuyan | ✅ | 时钟自巡（非拉起器模板） |
| 09-02 00:57 | 欧阳锋 | ouyangfeng | ✅ | #596/#599 |
| 09-02 01:37 | 探针 | laowantong | ✅ | profile 探针（非模板） |
| 09-02 01:38 | 黄药师 | huangyaoshi | ✅ | 碰巧正确（意图=huangyaoshi） |
| 09-02 02:06 | （交互式） | laowantong | ✅ | 非拉起器会话，不在本审计范围 |
| 09-03 00:56 | 老顽童 | laowantong | ✅ | todos 追加（非模板） |
| 09-03 01:01 | 老顽童 | laowantong | ✅ | 拉起器模板 prompt，落点却正确（疑手动直调带 -p，机制无法回溯） |
| **09-03 01:09** | **老顽童** | **huangyaoshi** | **❌** | 通路自测（自称"老顽童"✓，无施工） |
| **09-03 01:21** | **老顽童** | **huangyaoshi** | **❌** | **#626 claim**（117 msgs） |
| **09-03 02:11** | **老顽童** | **huangyaoshi** | **❌** | **#626/#630 施工报告**（会话到工具上限如实交接） |
| 09-03 02:13 | 探针 | huangyaoshi | ❌ | 通路探针（"回答我一句话"） |
| **09-03 02:14** | **老顽童** | **huangyaoshi** | **❌** | 接续施工 |
| **09-03 02:16** | **老顽童** | **huangyaoshi** | **❌** | 接续施工 |
| **09-03 02:18→02:43** | **老顽童** | **huangyaoshi** | **❌** | **#626/#630**（199 msgs） |
| **09-03 03:41→03:58** | **老顽童** | **huangyaoshi** | **❌** | **#626 收尾** |
| **09-03 04:41→04:56** | **老顽童** | **huangyaoshi** | **❌** | **#629 收尾** |
| **09-03 06:10→06:17** | **老顽童** | **huangyaoshi** | **❌** | 接续 |
| **09-03 10:09→10:24** | **老顽童** | **huangyaoshi** | **❌** | **#632 施工（8 件模板）** |
| **09-03 11:09→11:19** | **老顽童** | **huangyaoshi** | **❌** | **#632 收尾（L9 双重验证）** |

日志侧旁证：错载会话的自称抽验全部仍是"老顽童"（如 `logs/headless-laowantong-20260903-010947.log`："我是谁：老顽童（laowantong）"）——**KDO prompt 模板扛住了身份，错载只发生在 hermes 层**。

## 受影响任务清单（报王语嫣，老朱知情）

**经错载 profile 实例完成的任务**：#626（Live86 素材模版增量）、#629、#630、#632（8 件模板）。四单均已走完各自队列流转并终审（终审对象是产出物本身，产出不受 hermes 层错载影响）；需知情的是**这些会话的运行上下文混入了黄药师 profile**。

**污染面评估（三查）**：
1. **记忆写入**：huangyaoshi profile 的 `memories/MEMORY.md`（7 行，mtime 09-01 09:58，早于窗口）——**无老顽童内容写入**，记忆层污染未发生
2. **会话库混入**：11 个老顽童会话进黄药师 profile `state.db`（167 条历史中的 11 条）——黄药师若基于该库续聊/检索会看到老顽童的施工史（**已发生，不可逆，建议留存现状不清洗**，清洗风险大于收益）
3. **上下文错载**：施工期间加载了黄药师 profile 的 SOUL/skills/config/auth——对产出物的影响无法事后完全排除，但四单产出均经独立终审+回流验证，实务风险低

## 用量归因连带偏差

`kdo-tools/token_meter.py::_scan_hermes` 按 `profiles/<name>/state.db` 做角色归因——错载期老顽童的 hermes token 花销被记到 **huangyaoshi** 名下（09-03 当日 `60_feedback/analytics/` 的 token 报表如按角色读数需带此偏差校正）。

## 附带更正（段王爷 diag 一处证据）



`diag_20260906_duanwangye-hermes-headless-profile-flag.md` 证据 1 称 09-03 `headless-laowantong-20260903-200916.log / 233700.log`（84KB/30KB）为 hermes 通道成功日志——两文件首行均为 **`kimi version 0.39.1`**，实为 kimi 通道。"间歇故障非通道死刑"的结论方向不受影响（通道本身今日双实测存活），但该两条日志不能作为 hermes 成功证据引用。

## 建议（请王语嫣裁定）

1. **知会老朱**：四单（#626/#629/#630/#632）施工上下文错载一事知情即可，产出无需返工
2. **huangyaoshi profile 会话库留现状**：11 条老顽童会话不清洗（清洗风险 > 收益），本单留档即可
3. **profile 伞检查**：五绝若新增 hermes 通道实例，先核 `%LOCALAPPDATA%\hermes\profiles\<role>\` 是否存在（Windows 原生根，直调 hermes.exe 时即此根）——五绝中现缺 `hongqigong`（只存在于 `~/.hermes` 侧另一 home），`-p hongqigong` 在原生根会直接 exit 1
4. 拉 09-03 凌晨 01:00-01:10 的 0 字节日志与 state.db 有会话的对照（"两连死"实为 stdout 捕获丢失而非进程死）——是否立项排查由王语嫣定
