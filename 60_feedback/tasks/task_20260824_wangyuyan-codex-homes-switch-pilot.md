---
id: 490
assignee: wangyuyan
status: in_progress
updated_at: '2026-08-23T19:12:14.608879+00:00'
version: v0.1
instance: wangyuyan
---

# #490 codex-homes 切换试点（风清扬先切，先补后切）

- **任务号**：#490
- **状态**：queued（**依赖 #489 采集面补全完成后开工**——先补后切，杜绝「切了就断留痕」）
- **assignee**：wangyuyan（编排切换执行；风清扬试点实测；黄药师配置支持；老朱确认推广）
- **优先级**：P1（F-048 拍板落地 → P1-②）
- **立项**：2026-08-24 王语嫣（老朱 2026-08-24 直达拍板 F-048 → P1-②）

## 背景

codex-homes 7 角色隔离目录（`D:\KDO-memory\codex-homes\<角色拼音>\` 含 config/memory/sessions）已建（08-23 20:10），但 **sessions 全空、尚未切换启用**——「壳在、数据流未接」，当前仍在共享 `.codex` 写。F-048 拍板：codex 定性=工厂共用工具，需按角色分家（CODEX_HOME 隔离），使「每个角色全量上下文独立」。

## 任务

### 步骤 1 · 前置确认（#489 完成后）
- 确认 #489 采集面补全已验收——codex 会话能进 L1 全量库（先补后切，避免切换瞬间留痕断档）

### 步骤 2 · 风清扬先切试点
- 风清扬 CODEX_HOME 指向 `D:\KDO-memory\codex-homes\fengqingyang\`（config/memory/sessions 独立）
- 观察者风险最低，切完即可实测「审计侧全量上下文闭环」

### 步骤 3 · 实测闭环
- 风清扬实测：切换后 codex 会话 → L1 采集 → 审计侧可完整回溯（全量上下文闭环）

### 步骤 4 · 跑通后推广
- 风清扬试点跑通 → 其余角色（黄药师/欧阳锋/王语嫣/老顽童等）按序推广切换

## 验证（验证分层）

- L1：切换前置条件（#489 验收）满足
- L2 狗粮：风清扬切后实测审计侧全量上下文闭环（codex 会话可被 L1 采集+回溯）
- L3 待活体：其余角色推广切换后，各角色 codex 上下文独立且可审计

## 边界

- **先补后切**：#489 采集面补全验收前，不切任何角色（防留痕断档）
- 风清扬只审计+试点实测，不改脚本（配置/脚本支持归黄药师）
- 切换执行归王语嫣编排；推广前老朱确认
- 与 F-048 建议1（CODEX_HOME 分家）同源——本单就是分家的执行落地

## 关联

- F-048（老朱拍板 P1-②：先补后切，风清扬先切试点）
- #489（采集面补全，前置依赖）
- `diag_20260823_fengqingyang-l1-periodic-audit.md` §拍板记录（P1-② 原文）
- `diag_20260823_fengqingyang-codex-instance-isolation.md`（CODEX_HOME 分家建议书）
- #463（L1 采集基建）/ #471（常驻调度）

## 需要谁动作

- **王语嫣**：编排切换顺序 + 前置确认 + 协调
- **风清扬**：试点切换 + 实测审计侧闭环（不实施脚本）
- **黄药师**：CODEX_HOME 配置/脚本支持
- **老朱**：推广前确认
- **欧阳锋**：终审本单

## 执行报告（F-034 五字段，2026-08-24 王语嫣）

**文件清单**：`D:\KDO-memory\codex-homes\` 下新增 7 个角色隔离启动脚本（start-fengqingyang/wangyuyan/ouyangfeng/laowantong/huangyaoshi/hongqigong/duanwangye.sh）+ 通用脚本 switch-codex.sh + README.md 补 bash 启动方式。

**完成内容**：切换机制落地——CODEX_HOME 隔离脚本（设置 `CODEX_HOME` 指向角色目录后 exec codex，隔离 config/memory/sessions）；前置 #489 采集面补全已 reviewed（先补后切条件满足）。

**验证**：`export CODEX_HOME=fengqingyang && codex --version` → 返回 `codex-cli 0.144.1`，且 `fengqingyang/tmp/arg0` 被写入（03:10/03:11 两次），证明 codex 识别 CODEX_HOME 环境变量、数据写角色目录而非共享 .codex。脚本 `./switch-codex.sh fengqingyang --version` exit=0。

**未做项**：①试点实测（L2 审计侧闭环）——风清扬当前用飞书、未实际切 codex，需其切换时实测「codex 会话→L1 采集→审计回溯」闭环；②其余角色推广（L3 待活体）；③各角色 config.toml 如需独立微调（当前复制自共享 .codex，deepseek-v4-pro 配置）。

**需要谁动作**：风清扬（实际切换试点 + 实测审计侧闭环）；老朱（推广前确认）；欧阳锋（终审本单）。
