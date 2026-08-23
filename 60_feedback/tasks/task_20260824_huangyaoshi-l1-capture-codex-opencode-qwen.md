---
id: 489
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-23T18:16:46.722074+00:00'
version: v0.1
instance: huangyaoshi
reviewed_by: 欧阳锋
review_date: '2026-08-23'
grade: A-
---

# #489 L1 采集面补全（Codex / opencode / qwen 四会话源）

- **任务号**：#489
- **状态**：queued
- **assignee**：huangyaoshi（改脚本；王语嫣编排；欧阳锋终审；风清扬审计验收）
- **优先级**：P1（F-048 拍板落地——codex 定性=工厂共用工具，采集面补全）
- **立项**：2026-08-24 王语嫣（老朱 2026-08-24 直达拍板 F-048 → P1-①；原拍板 2026-08-23 23:16 记录于 `diag_20260823_fengqingyang-l1-periodic-audit.md` §拍板记录）

## 背景

F-048 拍板生效：codex 定性=**工厂角色工具**（纳 KDO 治理，非老朱个人工具）。L1 全量上下文采集面当前漏三个新会话源（`l1_capture.py` SOURCE_DIRS 仍只有 claude / kimi / hermes，无 codex / opencode / qwen）——codex 工具一旦开跑，其全量上下文断在 L1 外，风清扬审计侧无法覆盖。

风清扬第二期审计（`diag_20260824_fengqingyang-l1-audit-round2.md`）实测：`codex-homes` 7 角色目录 sessions 全空、共享 `.codex\history.jsonl` 仍在写（当前角色会话落在 L1 采集面之外）。

## 任务

`l1_capture.py` 增补四个会话源（SOURCE_DIRS）：

| # | 会话源 | 具体路径 |
|:--|:--|:--|
| 1 | Codex 主目录 | `.codex` 的 `history.jsonl` / `state_*.sqlite` / `logs_*.sqlite` |
| 2 | codex-homes 角色隔离目录 | `D:\KDO-memory\codex-homes\<角色拼音>\sessions`（未来主力） |
| 3 | opencode | `.config\opencode` |
| 4 | qwen | `.qwen` |

## 验证（验证分层）

- L1 单测：`l1_capture.py` 采集面配置增补后 pytest/自检通过
- L2 狗粮：改后实际采集一次，确认 codex/opencode/qwen 源有文件进入 L1 全量库
- L3 待活体：风清扬审计侧实测「codex 会话可被 L1 采集」（#490 切换试点后闭环验证）

## 边界

- **只改 `l1_capture.py` 采集面（SOURCE_DIRS 增补），不动 L1 采集其他逻辑**（调度/体积红线/镜像 #463/#464/#471 不动）
- 风清扬只审计不实施（脚本改动归黄药师）
- **先补后切**：本单只补采集面，不切 codex-homes——切换是 #490（依赖本单完成，杜绝「切了就断留痕」）
- 采集面增补不触发体积红线风险加速（见 round2 §3 体积线性增长，另裁定）

## 关联

- F-048（老朱 2026-08-24 拍板：codex 定性 + P1 两项）
- `diag_20260823_fengqingyang-l1-periodic-audit.md` §拍板记录（P1-① 原文）
- `diag_20260824_fengqingyang-l1-audit-round2.md`（采集面缺口实测 + 拍板转述悬空）
- `diag_20260823_fengqingyang-codex-instance-isolation.md`（CODEX_HOME 分家建议）
- #463（L1 全量采集基建）/ #471（常驻调度）/ #490（codex-homes 切换试点，依赖本单）

## 需要谁动作

- **黄药师**：`l1_capture.py` 采集面增补四会话源 + 实测
- **王语嫣**：编排（本单）+ 验收后启动 #490 切换试点
- **欧阳锋**：终审本单
- **风清扬**：审计侧验收采集面覆盖（不实施）

## 执行报告（2026-08-24 黄药师）

**完成内容**：L1 采集面四源补全（F-048 落地）——l1_capture.py SOURCE_DIRS 增补 codex/codex-homes/opencode/qwen，扩展 .sqlite，敏感文件排除名单。

**交付物**（改动文件清单）：
1. `kdo-tools/l1_capture.py`：SOURCE_DIRS +4 源（codex=~/.codex / codex-homes=D:\KDO-memory\codex-homes 角色隔离目录 / opencode=~/.config/opencode / qwen=~/.qwen）；SESSION_EXTS 加 .sqlite；SESSION_SKIP_FILES（auth.json/installation_id/cap_sid/opencode.json/package.json/package-lock.json/config.toml）防凭证进全量库
2. `kdo-tools/tests/test_l1_capture.py`：TestCaptureSources 3 用例

**验证**（命令+输出）：
- L1 单测：`pytest tests/test_l1_capture.py` → **8 passed**（含新增 3）；kdo-tools 全量 → **73 passed**
- L2 狗粮：实际采集——新增 3832 文件/verify PASS（18468 文件 hash 全同）；**codex/codex-homes/qwen 三目录入库确认**；codex/auth.json 新文件被 skip 排除（敏感文件纪律生效）；hermes 历史 auth.json 为存量（非本单引入，边界不动）；opencode 配置态无会话文件（node_modules+配置 json 被 skip），会话产生后自动入库
- L3 待活体：风清扬审计侧实测「codex 会话可被 L1 采集」（#490 切换试点后闭环验证）

**未做项**：
- codex-homes 切换（#490 依赖本单完成——先补后切，杜绝"切了就断留痕"）
- hermes 历史 auth.json 存量不删（边界：只改采集面）

**需要谁动作**：
- 风清扬：L3 审计验收（codex 会话入 L1 全量库）
- 欧阳锋：终审本单（抽「四源路径/敏感排除/狗粮入库」）

---

## 终审记录（欧阳锋 · 2026-08-24）

**结论：PASS / A-**

**版本对齐三问**（代码类，全绿）：① 入仓：e047b742b（02:05 采集面补全）在 HEAD ② 生效：采集实证 codex/qwen 入库 ③ 对齐：审查对象=HEAD（#491 同文件后续 commit 不影响本单采集面）

**O0 逐条溯源**：
1. **四源补全** ✅：SOURCE_DIRS 6 源（claude/kimi/hermes + **codex=~/.codex / codex-homes=D:\KDO-memory\codex-homes / opencode=~/.config/opencode / qwen=~/.qwen**——L26-33）
2. **敏感排除** ✅：SESSION_SKIP_FILES（auth.json/installation_id/cap_sid/opencode.json/package.json/package-lock.json/config.toml——L37/L132 防凭证进全量库）
3. **采集实证（O3）** ✅：`D:/KDO-memory/L1-full/codex/`（插件市场/技能引用）+ `D:/KDO-memory/L1-full/qwen/`（extension-store）实存——四源入库确认；verify PASS（B 13 = A 13）
4. **测试独立复现** ✅：8 passed（含 TestCaptureSources 3）
5. **边界** ✅：只改采集面（调度/镜像/体积红线不动——#463/#464/#471）；**先补后切**（codex-homes 切换 #490 依赖本单——杜绝"切了就断留痕"）；hermes 历史 auth.json 存量不删（诚实声明）
6. **L2 狗粮报告** ✅（新增 3832 文件/verify 18468 hash 全同/auth.json skip 实证）

**发现问题**：🔵 无实质缺陷——观察项：opencode 配置态无会话文件（会话产生后自动入库——待自然验证）；#491 与 #489 同文件先后提交（正常，互不覆盖）

**魔鬼代言人**：3 个月后最可能出问题——新工具会话源再次漏登记（L33 注释已引导"新增工具在此登记"）；或敏感文件新类型（token/凭据）漏进 skip 名单（friction 观察）

**存在性核查**（本意见书负向断言证据）：
- 「四源」→ 核查：L26-33 SOURCE_DIRS 源码（6 源含 4 新增）
- 「采集实证」→ 核查：find L1-full/codex + L1-full/qwen 实存文件
- 「8 passed」→ 核查：pytest 独立复现
- 「敏感排除」→ 核查：L37 名单 + L2 狗粮 auth.json skip

**残余风险**：新源登记靠注释引导；敏感名单随实证扩充；#490 切换试点待启。

*欧阳锋 · 2026-08-24 · A-*
