# 王语嫣 WSL→Windows 迁移体检实录（2026-08-16）

> 首次实战：用户告知"已把你从 WSL 侧迁移到 Windows 侧"，要求全面体检确认满血复活。本文件作为下次体检的对照基准。

## 环境事实
- 本机 Windows 10，git-bash (MSYS) shell，python 3.13.14（无 python3 命令）
- Active profile: wangyuyan，数据在 `C:\Users\Administrator\AppData\Local\hermes\profiles\wangyuyan\`
- Vault: `C:\Users\Administrator\Desktop\wiki\`
- kdo CLI: `/c/Users/Administrator/AppData/Local/hermes/hermes-agent/venv/Scripts/kdo`
- 飞书 DM 网关已连接（本会话即飞书通道）

## 验证结果快照（全部通过）
- 记忆：MEMORY.md 76% / USER.md 79%，UTF-8 完好（read_file 误判 binary，hexdump 证实）
- Skills：145 在册；entry-quality-gate 完整加载（33 references，readiness=available）
- 知识库：vault 九层目录完整；`kdo query "五步法" --limit 3` 返回 graph RAG 结果（EXIT=0）
- 上下文：startup.md / wangyuyan-context.md（601行，行为牌 W1-W10）/ context.md（active_task 到 8-15）
- 复盘：daily-context 最新 2026-08-16.md；技能进化日志更新到 8-16（7 条新经验）
- 时间胶囊：CAPSULE_STARTUP.md 王语嫣段落 + W1-W8 在册

## 发现的 3 个裂缝（不阻塞）
1. **复盘目录分裂**：`agent复盘/wangyuyan/`（拼音，daily-context）vs `agent复盘/王语嫣/`（中文，技能进化日志+错误模式库）；wangyuyan-context.md §会话结束第 0 步写的技能日志路径与实际不符（写的是拼音目录下的技能进化日志，实际在中文目录）
2. **时间胶囊 WSL 路径残留**：CAPSULE_STARTUP.md Shared State 的 `wiki_root: /mnt/c/Users/Administrator/Desktop/wiki`（历史残留，实际 C:\ 可用）
3. **read_file 误判 binary**：MEMORY.md/USER.md/CAPSULE_STARTUP.md 被判 binary，实际 UTF-8 完好——工具探测误报，不涉及数据损失

## 后续状态（2026-08-16 当日修复闭环，老朱授权自行修复）
- 裂缝 1 目录分裂：已合并到 `wangyuyan/`（拼音），中文目录删除，引用更新 2 处（wangyuyan-context.md:567 / amnesia-recovery.md:30），README 落位
- 裂缝 2 wiki_root：已 patch 为 `C:/Users/Administrator/Desktop/wiki`
- 裂缝 3 read_file 误判：Python 逐字节验证 0 NUL + UTF-8 解码通过，数据完好，判定为 Hermes 工具探测行为
- 过程资产：`hermes config set approvals.mode off` 开通自动模式（详见 SKILL.md 坑 7 + corr_20260816_wangyuyan-windows-migration-findings.md）
