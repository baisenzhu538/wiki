---
id: diag_20260906_duanwangye-hermes-headless-profile-flag
type: diag
status: draft
author: 段王爷
reviewed_by: ""
created_at: 2026-09-06
updated_at: 2026-09-06
source_refs:
- 90_control/scripts/kimi-headless-launch.py
- 90_control/infrastructure-inventory.md
related:
- [[kimi-headless-launch]]
---

# 建议书：hermes 无头通道工具模板修正（env 变量失效 → 改 `-p` flag）

## 触发来源

老朱 2026-09-06 问询："编排智能体是 hermes，hermes 是否也能无头拉起其他角色/专家 profile？"段王爷实测验证过程中发现 TOOLS 表 hermes 条目的角色切换机制存在失效疑点，按厂规报王语嫣裁定。

## 实测证据（2026-09-06，全部段王爷亲跑）

### 证据 1：hermes 无头单发通道本身是活的

```
export HERMES_PROFILE=duanwangye
hermes.exe -z "连通性测试..." --yolo
→ HEADLESS_OK 2026-09-06 (周日)，秒回，exit 0
```

09-03 的"两连死+锁挂"判断需要重新审视——当日其他时段同通道即有 84KB/30KB 成功日志（headless-laowantong-20260903-200916.log / 233700.log），是间歇故障非通道死刑。

### 证据 2：`HERMES_PROFILE` 环境变量在无头单发中不生效（P0 发现）

用 env 变量方式拉起三个非五绝 profile：

```
HERMES_PROFILE=skills-assistant hermes -z "你是谁" --yolo
→ 自称"段王爷（南帝）"        ← 错，应为 skills-assistant
HERMES_PROFILE=coaching-leadership-assistant ... → 自称"段王爷"
HERMES_PROFILE=research-explosion-partner ... → 自称"段王爷"
```

三个 profile 全部错加载为**当前 shell 的默认 profile**（即发起者自己）。若此机制在 kimi-headless-launch.py 中同样失效，则意味着：**历史上所有 hermes 通道的"角色拉起"，实际都是同一个 profile 在干活**——角色隔离（独立记忆/技能/队列身份）形同虚设，且会产生跨 profile 的记忆污染写入。

### 证据 3：命令行 `-p` flag 正确生效

```
hermes -p skills-assistant -z "你是谁" --yolo
→ PROFILE_OK Skill 生产+配置中枢——P1-P4 产线把 30_wiki 知识卡行为化为可执行 skill
```

职能自报精确命中，profile 隔离真实生效。

### 证据 4：`-z` 模式不认 `-Q` 静默参数（P2 小坑）

`-Q/--quiet` 只属于 `chat` 子命令；`hermes -z` 直调会报 `unrecognized arguments: -Q` 后退出 0（假成功）。TOOLS 表如要加静默参数需走 `chat -q -Q` 形态。

## 建议动作（请王语嫣裁定）

1. **【P0】复核 kimi-headless-launch.py 的 TOOL_ENV 机制**：
   ```python
   # 现行（疑失效）：
   TOOL_ENV = {"hermes": {"HERMES_PROFILE": "{role}"}}
   # 建议改为 prompt 模板替换 flag：
   "hermes": [hermes.exe, "-p", "{role}", "-z", "{prompt}", "--yolo"]
   ```
   复核方法：用现行 TOOLS 表拉起 laowantong 干一单，看其 logs 输出自报身份是"老顽童"还是发起者角色——一测便知。
2. **【P0】追溯影响面**：09-03 之后所有经 hermes 通道的 headless 拉起（daily_review 23:37 三角色批次含 hermes 线的话）——核对其日志中角色自报身份，评估是否发生过跨 profile 误写（todos/队列/memory 落错账户）。
3. **【P1】若证实失效**：TOOLS 表 hermes 模板改 flag 形态后，评估 laowantong 线是否从 kimi 切回 hermes（09-03 20:10 王语嫣"待通道修复后恢复"的前置条件现已满足——通道实测活，且真凶疑似就是 env 失效引发的混乱）。
4. **【P2】新专家 profile 纳入路由表**：skills-assistant / coaching-leadership-assistant / research-explosion-partner 三个 profile 实测可用（`-p` flag 形态），如需常态化拉起建议在 ROLE_TOOL 表登记，路由规则报老朱拍板。
5. **【P2】回写技能卡**：hermes-agent skill 的 "Spawning Additional Hermes Instances" 章节只写了 tmux/`-q` 形态，应补 `-p <profile>` 跨角色拉起模式 + env 变量失效警告。

## 边界说明

- 本建议书只报发现与建议，不直接改动 90_control/scripts/（工具注册表归王语嫣线维护，避免双写冲突）。
- 五绝角色 profile（huangyaoshi/laowantong/ouyangfeng/wangyuyan/duanwangye）用 flag 形态全部实测可用，本机 profile list 已核对。
- kimi CLI 当前另有独立故障（storage write failed，疑 5h 限额），与本建议书主旨无关，另行观察。

## 验证命令（复核可直接复用）

```bash
HE=/c/Users/Administrator/AppData/Local/hermes/hermes-agent/venv/Scripts/hermes.exe
# env 方式（预期：错误加载默认 profile）
HERMES_PROFILE=skills-assistant "$HE" -z "只回复一行自报身份" --yolo
# flag 方式（预期：正确加载目标 profile）
"$HE" -p skills-assistant -z "只回复一行自报身份" --yolo
```
