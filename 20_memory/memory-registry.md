---
id: memory-registry
type: registry
status: active
updated_at: '2026-08-19'
owner: 王语嫣
audience: 全体 agent
---

# 记忆注册表（memory-registry）

> 全厂唯一回答"我该读哪份、哪份是最新真相"的文件。来源：codex 记忆一致性审计建议书①（2026-08-19），#365 交付。
> 任何 agent 对"真相在哪"有疑问时查本表；本表未覆盖的新资产，先入本表再使用。

## 表 1 · 唯一真相源（每类事实只有一个权威位置）

| 事实类别 | 唯一真相源 | 备注 |
|:--|:--|:--|
| 当前任务/队列状态 | `70_product/tasks/production-queue.md` | 队列尾为最新；dashboard 是派生物 |
| 任务单 | `60_feedback/tasks/task_*.md` | 队列行引用为准 |
| 组织记忆（会话复盘） | `agent复盘/<pinyin>/daily-context/` 内最新日期文件 | Truman 10 章唯一格式（agent-os.md §10）；中文旧轨已冻结（#367，归档于拼音轨 `cn-track-archive-20260819/`） |
| 错误模式 | `agent复盘/<agent>/错误模式库.md` | 复盘时同步更新 |
| 用户反馈/红线 | `agent复盘/<agent>/用户反馈档案.md` | 同上 |
| 技能进化 | `agent复盘/<agent>/技能进化日志.md` | 同上 |
| 角色协议 | `agents/agent-os.md` + `.agent/<role>-context.md` | 改动走任务制 |
| 启动入口 | 现多入口，#366 收敛为 `.kdo/CAPSULE_STARTUP.md` 唯一指针 | 过渡期中 |
| 工具/脚本真相源 | `kdo-tools/`（登记处 `40_outputs/code/scripts/README.md` 只放指针） | #359 裁定：禁止副本 |
| MCP 配置 | `agents/hermes-mcp-template.yaml` + `sync-hermes-mcp.py` 渲染 | #326 单一真相源 |
| Hermes 记忆 | `AppData\Local\hermes\profiles\<role>\memories\` | 迁移后 Windows 为准；WSL 侧已停 |
| 能力注册 | `cap_hub/` | — |
| 失忆恢复锚点 | `20_memory/<role>-amnesia-recovery.md` | 命名规范见表 3 |

## 表 2 · 派生副本（只读，禁手改）

| 派生物 | 生成脚本 | 真相源 |
|:--|:--|:--|
| `70_product/tasks/dashboard.html` | `kdo-tools/generate-dashboard.py` | production-queue.md |
| `70_product/tasks/dashboard.md` | 同上 | 同上 |
| vault-status / agent-contexts-summary | 相关生成脚本（#369 收口带版本标记） | 各自真相源 |

手改派生物 = 违规；发现漂移改真相源后重跑脚本。

## 表 3 · 命名规范

| 资产 | 规范 | 反例（现存待收敛） |
|:--|:--|:--|
| 失忆恢复锚点 | `20_memory/<role>-amnesia-recovery.md`（无日期后缀） | `duanwangye-amnesia-recovery-2026-07-21.md`（带日期）/ `hongqigong-amnesia-recovery-20260613.md`（日期无连字符） |
| 任务单 | `60_feedback/tasks/task_YYYYMMDD_<agent>-<slug>.md` | — |
| daily-context | `agent复盘/<pinyin>/daily-context/YYYY-MM-DD.md` | 中文目录双轨（#367 收敛） |
| 诊断文档 | `60_feedback/diagnosis/diag_YYYYMMDD_<slug>.md` | — |

## 表 4 · 废弃清单（冻结标 DEPRECATED，不真删；观察后归档）

| 废弃项 | 位置 | 处置 |
|:--|:--|:--|
| `新建文件夹`、`新建文件夹 (2)` | `agent复盘/` | #367 批次冻结归档 |
| `laowantong-next-tasks.md` | `70_product/tasks/` | 同上（context.md 已声明废弃） |
| 中文双轨目录（`欧阳锋/`、`黄药师/`、`老顽童/` 等） | `agent复盘/` | #367 冻结 7 天观察后归档 |
| `daily_cognitive_review` 七节式、`.agent/daily-review` 四段式 | 各 agent 目录 | 已废弃格式（#368 定标后统一） |
| 登记副本 tools.py/server.py 等 | `40_outputs/code/scripts/` | 已删除（#359），此处备案防复活 |

---

*#365 · 王语嫣起草 · 黄药师会审 · 欧阳锋终审 · 2026-08-19*
