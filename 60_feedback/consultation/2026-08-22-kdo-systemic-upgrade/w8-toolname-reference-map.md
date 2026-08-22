# W8 工具名引用面清单（#415 · B4-2 替换前置影响面地图）

- **任务**：#415（P0，B4-2 前置——只出清单不替换）
- **执行**：黄药师 · 2026-08-22 · 只读扫描（未改任何文件）
- **工具名清单**：codex / claude / hermes / kimi / codebuddy / workbuddy（含大小写变体）

## 一、五类扫描面汇总

| 面 | 扫描对象 | 引用处数 | 引用类型 |
|:--|:--|:--|:--|
| 面1 | hermes profiles（AppData\Local\hermes\profiles，10 profiles） | 多个 profile 的 config.yaml / models_dev_cache / sessions / skills/.usage.json | **配置（provider/model 参数名——改名会崩）** |
| 面2 | kdo-tools/、90_control/scripts/、40_outputs/code/scripts/（py） | **96 处** | 脚本（路径常量/实例名/进程名判断） |
| 面3 | Windows 计划任务 | **10 个任务**：Codex-Relay / Hermes-Beikai-Gateway / Hermes-Duanwangye-Gateway / Hermes-Gateway-laowantong / Hermes-laowantong-Gateway / hermes-laowantong-backup / KDO-Health-Check / kdo-health-daily / kdo-inbox-watch / wechat-link-monitor | **任务名（改名断计划任务）** |
| 面4 | .claude/ + .agent/ | **249 处** | 配置（settings.local.json 的 WSL 路径引用 hermes 服务/config/SOUL）|
| 面5 | 90_control 顶层文档（AGENTS/PROTOCOL/rules-core/工业化手册） | **6 处** | 文档（角色分工表/禁止清单） |

## 二、高风险清单（改名会改崩——替换前必须处理）

| 位置 | 引用 | 风险 |
|:--|:--|:--|
| AppData\Local\hermes\profiles\beikai\config.yaml:162 | `codex_gpt55_autoraise: true` | provider 参数名，改名直接失效 |
| 各 profile config.yaml / models_dev_cache.json | `kimi-coding` / `deepseek` provider 名 | 配置层改名需同步 SDK 缓存（P-27 教训） |
| 计划任务（10 个） | `Codex-Relay` / `Hermes-*-Gateway` 等任务名 | 改名 = 断计划任务 + 断 NSSM 服务关联 |
| .claude/settings.local.json:15-19 | WSL 路径 `hermes-gateway-laowantong.service` / `.hermes/profiles/*/config.yaml` | 路径硬编码，改名全断（P-5/P-6 家族） |
| kdo-tools/agent-activity-check.py:28 | `PROFILES_DIR = ...hermes\profiles` | 脚本路径常量 |
| kdo-tools/agent-activity-check.py:57 | `hermes-gateway-{agent}` 进程名判断 | 进程名匹配逻辑 |
| kdo-tools/generate-dashboard.py:138 | `"workbuddy": "WorkBuddy"` 映射 | 显示映射 |
| kdo-tools/daily-context-save.py:229 | `--instance` 帮助文本 `hermes/kimi/claude` | 文档/参数语义 |

## 三、中风险（文档引用，替换安全）

- 脚本 docstring / README / skill 文档中的工具名（`kdo-tools/*.py` 头部注释、40_outputs/code/scripts/README.md）
- 90_control 顶层文档 6 处（角色分工表工具列——B4-2 主目标）
- .agent/ 上下文文件 249 处中的文档性引用（角色运行位置表等）

## 四、活文档 vs 历史文件分界建议（B4-2 拍板口径）

- **活文档全替换**：90_control/ 顶层规范、.agent/ 角色上下文、README/skill 文档、脚本 docstring、cap_hub
- **历史文件不替换只加标注**：60_feedback/session-archives/、agent复盘/、20_memory/ 历史记录——改字面=篡改记录（#415 立场 B4-2 修改项）
- **配置/计划任务层**：`hermes` 相关**不建议改名**（服务名/任务名/gateway 是运行态事实，改名=全厂停机风险）——B4-2 应限定"文档/角色指称"替换，运行态名称保留并注明别名

## 五、扫描面完整性声明

- 面1：`ls profiles/` 10 profiles 全扫（yaml/json/toml）
- 面2：`grep -rniE "codex|hermes|codebuddy|workbuddy" kdo-tools/*.py 90_control/scripts/*.py 40_outputs/code/scripts/*.py` → 96 处
- 面3：`schtasks /query /fo CSV` 全量 → 10 个相关任务
- 面4：`grep -rniE ... .claude/ .agent/` → 249 处
- 面5：90_control 4 份顶层文档 → 6 处

*黄药师 · 2026-08-22 · 只读清单，B4-2 替换执行单据此展开*
