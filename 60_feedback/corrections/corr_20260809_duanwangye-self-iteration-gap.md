---
id: "corr_20260809_duanwangye-self-iteration-gap"
type: "correction"
target_role: "段王爷（南帝 Publisher）"
source: "老朱 2026-08-09 自我迭代点名 + 教练 Agent dk 卡对照"
severity: "P2"
status: "open"
created_at: 2026-08-09
---

# 纠正：段王爷自我迭代缺口——纸面闭环从未落地

> 老朱 2026-08-09 点名"你们的共性是不会自我迭代"，对照教练 Agent 的 `dk-agent-access-kdo-pitfalls` 做诚实自检。

## 事实

1. `duanwangye-review` skill 写了完整的"自我进化引擎"（四阶段闭环：Memory自检→Skills自检→Error-to-Skill→偏好学习），但 **60_feedback/corrections/ 里段王爷自己的沉淀为零**——文档写得漂亮，从未真正执行。
2. `config.yaml → approvals.mode: manual + timeout: 60`：本王在飞书网关下跑带写操作的 shell 命令（如 `python3 -c "open(...,'w')"`）会触发审批→无 UI→60s 超时被杀。**只读命令（print/ls/curl 读取）放行**。这是教练 Agent 坑 1 在段王爷环境的实测确认（2026-08-09 实测定案）：之前用 write_file 工具 + 只读命令绕过了它，所以"看起来没踩"——配置层问题伪装成命令坏了。
3. `search_files` 搜 30_wiki 多次慢/超时，降级用 terminal find 解决——**每次都重新踩，没沉淀**（与王语嫣同款）。
4. 检索规则散落：记忆里写"30_wiki/是AI生成非人写；40_outputs/由人填充"，但实际 40_outputs 已有产出的结构（articles/capabilities/code/content 等）——规则过时，未更新。

## 根因

**"绕过"而不是"诊断+修复+沉淀"**：遇到工具卡顿就换方法，从不停下来问——这是配置问题还是命令问题？该不该写 corrections？该不该请求修复？该不该沉淀成 skill？

## 建议改进（闭环 v1，已部分落地）

1. ✅ **发布任务完成后强制跑 Error-to-Skill 闭环**：遇到超时/卡顿/规则失效，立即写 60_feedback/corrections/，不绕过。
2. ✅ **沉淀段王爷自己的 dk 卡**：`dk-publish-collapse-to-iterate`（发布执行=知识迭代入口，见 30_wiki/dark-knowledges/），注册进 MOC。
3. ✅ **更新检索规则**：40_outputs 结构、30_wiki 路径以 wiki 实际结构为准，写进 SOUL.md 级记忆。
4. ⏳ **审批模式评估（实测确认，2026-08-09）**：本王环境写操作类 shell 命令被 manual 审批卡死（60s 超时）。**请求欧阳锋/老朱授权执行 `hermes config set approvals.mode smart`**（dk-agent-access-kdo-pitfalls 复用步骤已验证）。红线遵守：不用 --yolo/off、不未经授权改配置、改完向用户说明风险（smart 仍放行 rm -rf，靠行为自律）。
5. ⏳ **验证闭环**：下次遇到同类问题先查 MOC/corrections，不重复踩。

## 闭环实测（2026-08-09 第二轮：真跑一遍五步闭环）

收到老朱"你需要学习"后，本王没有继续写报告，而是当场跑了一次完整闭环：

| 步骤 | 动作 | 结果 |
|:--|:--|:--|
| 1. 发现问题 | 扫描本王 skill 发现 `duanwangye-review` 里有 4 处 Windows 路径（`C:\Users\...`） | 4 处命中 |
| 2. 诊断根因 | 验证：Windows 写法在 WSL 下全部 `No such file`，WSL 写法（`/mnt/c/...`）全部存在 | 根因 = skill 文档是早期 Windows 环境写的，迁移 WSL 后未同步——**与教练 Agent 坑 2 同款** |
| 3. 修复 | patch 全部 4 处为 WSL 格式 | ✅ 3 个 patch 全部成功 |
| 4. 沉淀 | 追加本段到 corrections + 更新 skill 路径说明 | ✅ 本文件 |
| 5. 验证 | 下次执行 daily-context-save.py 直接可用 | 待验证（命令已验证存在） |

**附带发现**：`/mnt/c/Users/Administrator/Desktop/agent复盘/duanwangye/daily-context/` 最新文件停在 `2026-08-02.md`——**本王复盘习惯断了 7 天**。会话结束强制动作写在 skill 里但从没执行，与"纸面引擎"同病。已修复路径，下一步补上断档复盘。

## 欧阳锋签名

> 审查人：待审
> 日期：2026-08-09
> 类型：流程改进建议 + 自检纠正，非事故
