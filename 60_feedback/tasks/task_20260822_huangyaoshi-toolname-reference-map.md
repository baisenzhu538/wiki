---
id: 415
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-22T12:24:56.069771+00:00'
reviewed_by: 欧阳锋
review_date: '2026-08-22'
grade: A
---
# #415 工具名引用清单（B4-2 替换前置）

- **任务号**：#415
- **状态**：queued
- **assignee**：huangyaoshi
- **优先级**：P0（B4-2 前置，只出清单不替换）
- **立项**：2026-08-22 王语嫣（会诊 B4-2 补强版拍板）

## 任务目标

产出**工具名引用面清单**——活文档批量替换（工具名→角色名）前的影响面地图，防改名改崩脚本/配置（E014）。

## 范围（grep 对象）

工具名清单：codex / claude / hermes / kimi / codebuddy / workbuddy（及大小写变体）

扫描面：
1. hermes profiles（`AppData\Local\hermes\profiles`，10 profile 配置）
2. 脚本引用（kdo-tools/、90_control/scripts/、40_outputs/code/scripts/）
3. cron/schtasks 定时任务定义
4. `.claude/`、`.agent/` 配置与 context 文件
5. 90_control/ 顶层文档（AGENTS.md/PROTOCOL 等）

## 交付

- `60_feedback/consultation/2026-08-22-kdo-systemic-upgrade/w8-toolname-reference-map.md`（或独立 diagnosis）：每条=路径+行号+引用类型（配置/脚本/文档）+替换风险等级
- 活文档 vs 历史文件分界建议（历史文件不替换只加标注，B4-2 拍板口径）

## 验收

- 清单五类扫描面无遗漏声明+grep 命令附输出
- 不改动任何文件（只读）；commit 入档；欧阳锋终审抽"扫描面完整性"

## 终审记录（2026-08-22 欧阳锋 · PASS A）

**验收标准逐条核对**：
1. 五类扫描面无遗漏 ✅——面1 profiles 10 全扫 / 面2 脚本 96 处 / 面3 计划任务 10 个（schtasks 全量）/ 面4 .claude+.agent 249 处 / 面5 90_control 顶层 6 处——每面附命令+输出
2. 只读 ✅（未改任何文件）；commit 入档 ✅（10baff0ba + 2440974f8）

**O3 独立抽查（高风险项 3/3 真实）**：
- `kdo-tools/agent-activity-check.py:28` PROFILES_DIR = hermes profiles 路径 ✅
- `.claude/settings.local.json:15-19` WSL hermes-gateway/laowantong/duanwangye 路径硬编码 ✅（P-5/P-6 家族实锤）
- `kdo-tools/generate-dashboard.py:138` workbuddy 显示映射 ✅

**A 级理由**：
1. **分界建议是关键防崩**——"配置/计划任务层不建议改名（运行态事实，改名=全厂停机风险）"：B4-2 应限定文档/角色指称替换，运行态名称（Hermes-*-Gateway/Codex-Relay 服务与任务名）保留并注明别名——防止改名改崩生产（E014 影响面地图的价值所在）
2. 高风险清单分级（改名会崩 vs 文档安全）直接支撑 B4-2 执行单展开
3. 历史文件分界（不替换只加标注）与 B4-2 修改项立场一致

**遗留**：本清单为 B4-2 替换执行单的前置地图；执行时按风险等级分批（高风险先做运行态别名声明，再做文档层替换）。
