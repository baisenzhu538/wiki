---
name: kimi-headless-launch
description: |
  角色无头拉起器：一条命令把任意 KDO 角色拉起在后台干活（自包含 prompt 自动带角色恢复+队列纪律+收尾留痕）。
  内置通道健康预检+fallback（claude/codex/kimi/hermes 四通道，同上游去重），通道全死不硬派。
  工具=可替换变量，角色=资产；新增工具在 TOOLS 表登记一行即可。
category: kdo-infrastructure
version: 1.0.0
related_skills:
  - queue-transition
  - review-chain
encapsulates: 90_control/scripts/kimi-headless-launch.py
status: draft
reviewed_by: 待审
review_date:
grade:
updated_at: 2026-09-06
trigger:
  natural_language:
    - 拉起某个角色干活
    - 无头模式/headless 启动 agent
    - 通道挂了/额度墙/fallback 切通道
    - 拉起后日志 0 字节
    - 被拉起的角色身份错了
    - kimi 403 周额度
---

# kimi-headless-launch：角色无头拉起器（含通道健康预检）

> **一句话**：`python 90_control/scripts/kimi-headless-launch.py <role> "<本次任务指令>"` —— 探针预检选健康通道 → 无头单发自包含 prompt → 被拉角色在后台跑，日志落 `logs/headless-<role>-<时间戳>.log`。

## 何时用

- 编排者（王语嫣=唯一时钟）要把某角色拉起来执行一单具体任务
- 主通道撞额度墙（kimi 403 周额度）/余额尽（codex）时，自动切下一个健康通道
- 需要确认「哪条 CLI 通道背后真实是哪家模型」再报值守

**不要用于**：在自己会话里替角色跑一次性小命令（直接自己做）；拉起后不管（必须看日志收尾留痕）。

## 怎么调

```bash
cd C:\Users\Administrator\Desktop\wiki

# 标准拉起（带通道预检 + fallback）
python 90_control/scripts/kimi-headless-launch.py laowantong "领 70_product/tasks/production-queue.md 第一件 queued 单施工，完工走 queue_transition complete"

# 指定工具（默认路由表见下）
python 90_control/scripts/kimi-headless-launch.py ouyangfeng "<指令>" --tool codex

# 应急直通：跳过预检按主通道硬拉（通道预检本身坏了才用）
python 90_control/scripts/kimi-headless-launch.py <role> "<指令>" --no-probe

# 测试钩：模拟死通道，验证 fallback / 全死不硬派路径（不发包、不真拉起）
python 90_control/scripts/kimi-headless-launch.py <role> "<指令>" --force-dead kimi,claude,codex,hermes
```

退出码：`0`=已拉起（stdout 给 `proc_<role>_<pid> | tool=<tool> | log=<路径>`）；`1`=用法错误；`2`=**全死不硬派**（已通知王语嫣，不要重试硬派）。

### 通道-真实模型对照（值守报通道必须报真实模型）

| CLI | 真实上游 / 模型 | 探针形态 | 备注 |
|:--|:--|:--|:--|
| `claude.exe` | 智谱 GLM `glm-5.3-flash`（settings.json `ANTHROPIC_BASE_URL=open.bigmodel.cn`） | HTTP `/v1/messages` `max_tokens=1`（正 key 200/≈1s，坏 key 401/≈0.1s） | 09-05 夜全通道连死时唯一全夜存活 |
| `codex.exe` | 本地 relay `127.0.0.1:4444` → api.deepseek.com，模型 `deepseek-v4-pro` | HTTP relay `/v1/responses` | relay 不校验调用方 key；**relay 挂≠deepseek 死**（降级为工具级不连坐） |
| `kimi.exe` | kimi-for-coding，显式 `-m kimi-code/k3`（防配置漂移） | CLI 级 `kimi.exe -p 只回复数字1`（OAuth 由 CLI 自刷，HTTP 探针会拿过期 token 假阴性） | 403=周额度墙 |
| `hermes.exe` | 上游=**kimi**（`~/.hermes/config.yaml: provider kimi-coding`） | 无独立探针，随 kimi 探测结果判定 | 角色切换必须 `-p <role>` flag，见坑 #650 |

默认路由（`ROLE_TOOL`，`--tool` 显式指定优先）：`huangyaoshi→kimi`、`laowantong→kimi`、`ouyangfeng→codex`。
fallback 链顺序：主工具 → `claude → codex → kimi → hermes`。**同上游去重**：kimi 403 时 hermes 不再撞同一堵墙。

### 被拉起的角色会自带什么（prompt 模板，不用你拼）

角色恢复（读 `.agent/<role>-context.md`）+ 队列纪律（状态流转只走 queue_transition.py、实例名=裸角色名）+ 完工落账（todos 追加一行）+ 五字段执行报告 + 备份避让 + 本次任务指令。你只需要把**任务指令写成自包含的一段话**（被拉角色没有你这份上下文）。

## 边界与红线

1. **拉起 ≠ 派活的替代**：角色之间不互相派活，唯一协调节点=欧阳锋；时钟唯一=王语嫣。别用本工具绕开编排。
2. **全死不硬派**（exit 2）：四通道都不健康时不许 `--no-probe` 硬拉——假跑必撞墙，白烧 token 零产出。
3. **逐单落盘**：每次拉起的 stdout/stderr 都在 `logs/headless-<role>-<时间戳>.log`；拉起后要回看日志确认角色真的起来了（0 字节日志=没起来，见坑表）。
4. **通道预检留痕**：探测结果一行 JSON 追加到 `logs/channel-health.log`（`decision` 字段=「<role>-><选中工具>」或「<role>->全死不硬派」）；通道切换/全死会同步落一行到 `90_control/todos/<role>.md`（前缀`【通道预检 #656】`）。
5. 新工具上线前必须**先实测其无头模式**（`-p`/`exec` 形态+权限模式），再登记进脚本 `TOOLS` 表——没实测过不要写。

## 常见坑（症状 → 修复）

| 症状 | 根因 | 修复 |
|:--|:--|:--|
| 日志 0 字节，进程即死 | 用了 `.cmd`/`.bat` 壳——DETACHED 无控制台环境下起不来（09-03 三次实证） | 一律用原生 `.exe`（脚本 TOOLS 表已登记正确路径） |
| 被拉角色自称错身份（段王爷实测三 profile 全错载） | 用 `HERMES_PROFILE` env 切 hermes 角色——hermes 解析链根本不读 env（#650） | hermes 角色走 argv `-p <role>` flag（脚本模板已带） |
| kimi 拉起报 403 weekly usage limit | kimi 周额度墙；hermes 同上游连坐 | 不用处理，脚本自动 fallback 到 claude/codex；报值守时带上「真实上游」 |
| 想查「通道↔模型」认知表 `90_control/channel-model-map.md` 找不到 | 该文件在脚本 docstring/#656 任务单里被引用，但 vault 内**未落盘**（2026-09-06 `find` 全库仅 3 处引用、0 处实体） | 以本表 + 脚本 `TOOLS` 表注释 + `channel_health.TOOL_UPSTREAM` 为准；补表另立项 |
| 全部通道报「force_dead（模拟死通道）」 | 你自己传了 `--force-dead`（测试钩，不发包） | 去掉该参数重跑即是真探测 |

## 失败模式（本技能特有）

| 失败 | 可识别信号 | 修复 |
|:--|:--|:--|
| 指令不自包含 | 被拉角色回问「你说的是哪个任务？」 | 指令里写全：任务 id / 文件路径 / 验收标准，别写「继续」「照旧」 |
| 拉起后不确认 | 只看到 stdout 的 proc 行就走了 | 30 秒后 `tail logs/headless-<role>-<时间戳>.log`，确认角色在读 context 而非报错 |
| 把探针当成本 | 为省 1 秒跳过预检 `--no-probe` | 预检是额度墙的疫苗；只有预检本身报错时才跳 |

## 相关协议与卡

- 探针分类与上游去重实现：`90_control/scripts/channel_health.py`（头注含各探针实测数据）
- 立项依据：`60_feedback/tasks/task_20260906_huangyaoshi-channel-health-fallback.md`（#656，F-073 两墙连撞根治）
- 姊妹 skill：`queue-transition`（被拉角色干活时唯一合法的状态流转入口）
