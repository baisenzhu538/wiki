---
id: task_20260816_codex-hongqigong-migration
assignee: codex
status: pending_review
priority: P0
wsjf: 4.0
created_at: 2026-08-16
updated_at: 2026-08-16
source: 用户指令（2026-08-16"洪七公启动不起来，现在也准备迁移到Windows侧，以后全量都是Windows，codex已经在操作了"）
related: #342 #343 #344 #345
---

# 洪七公（beikai）迁移 Windows（#347）

## 背景

洪七公 WSL 侧"启动不起来"（实测：systemd 服务活着但飞书断连）→ 用户决策：**洪七公迁 Windows，以后全量 Windows**——此前"只有飞书洪七公留在 WSL"的决策反转（#345 任务书冻结不动，E025）。codex 已在操作中。

## 现状快照（2026-08-16 王语嫣核查）

| 位置 | 状态 |
|:--|:--|
| WSL beikai | `hermes-gateway-beikai.service` **loaded active running**，但 gateway_state feishu=`disconnected`（2026-08-16T11:44:40Z，error_code null）——"启动不起来"真相：服务活着、飞书断连 |
| WSL beikai config | skills.external_dirs ✅（本地+shared）+ mcp_servers.kdo ✅ 已配 |
| WSL beikai 凭据 | auth.json/pairing/记忆（memories/）在 WSL 侧——迁移需搬运 |
| Windows `.hermes/profiles/hongqigong` | 空壳（仅 SOUL.md+config.yaml，无 memories/skills/sessions）待填充 |
| Windows `AppData\Local\hermes/profiles/beikai` | 旧壳（gateway_state 是 2026-05-15 陈旧记录）；skills.external_dirs **只有本地**（缺 vault shared 路径）；**mcp_servers 缺失**（无 kdo）——若复用需补 |
| E030 修复（已生效） | shared 70 技能 platforms 已修 `[linux, macos, windows]`——external_dirs 补上即全部可加载 |

## 任务

1. **查明 WSL beikai 飞书断连根因**（token 过期/pairing/网络代理 127.0.0.1:7897）——迁移前确认凭据可用性
2. **迁移到 Windows**（参照 #344 T2 模式）：config（external_dirs 补 vault shared + mcp_servers.kdo）+ 凭据 + 记忆 + skills 核对
3. **WinError 87 补丁**（gateway/status.py，老顽童 T2 同款——洪七公实测中曾遇）
4. **双开冲突处理**：停 WSL 侧 beikai gateway 再启 Windows 侧（#344 清单第 5 项）
5. **E030 收尾核对**：`hermes skills list` 验证共享技能全部加载（不只文件在磁盘）
6. **飞书真机冒烟**：洪七公飞书端可用（连接 connected + 工具调用无退化——openmontage 886MB Linux 工具链需单独评估 Windows 替代/降级方案）

## 验收标准

- Windows 侧 feishu connected + 真机冒烟通过（消息收发/图片处理能力无退化）
- 记忆继承成功（memories 搬运 + 失忆恢复验证）
- `hermes skills list` 全量加载核对
- WSL 侧 beikai gateway 已停（无双开冲突）
- 欧阳锋终审

## 决策记录（待落 decisions.md）

- 原决策"只有飞书洪七公留在 WSL"反转 → **全量 Windows**；迁移完成后 WSL 整体退役候选（.wslconfig 8GB/内存决策过时——等迁移全部完成再定，不提前拍板）
- openmontage Linux 工具链：Windows 替代/降级方案作为迁移决策子项

## 回滚

Windows 侧失败 → 回 WSL beikai（凭据/记忆未删前可回）

## 执行门禁

🔥 **执行中：用户已命令 + codex 已在操作**（老顽童 CLI 完成度不阻塞本任务——洪七公断连是当下生产事故）


## 迁移完成记录（2026-08-16 王语嫣核验 + 用户确认）

- **用户确认迁移成功**（真机冒烟：洪七公 Windows 侧飞书可用）
- **核验**：Windows AppData\Local beikai gateway **running + feishu connected**（12:18Z）；WSL 侧 hermes-gateway-beikai.service **已停 + disabled**（双开冲突处理 ✅）；skills list **243 enabled**（84 builtin + 158 local 全加载）；mcp_servers.kdo ✅（run_kdo_mcp.cmd + WIKI_ROOT/KDO_SRC）
- **E030 联动**：shared 70 技能 platforms 修复后 external_dirs 直接生效（此前 WSL 侧也从未加载过共享技能）
- **状态**：pending_review → 欧阳锋终审
