---
name: review-chain
description: |
  Agent 收尾复盘链：daily-context-save（双写复盘 + 自动自检）+ review-check（11 章格式与深度判级 🟢A/🟡B/🔴C）。
  会话不跑这条链 = 会话未完成。含 11 章标题清单、判级硬指标、🔴 C 级重写路径、--file 传文件姿势。
category: kdo-infrastructure
version: 1.0.0
related_skills:
  - queue-transition
encapsulates: kdo-tools/daily-context-save.py + kdo-tools/review-check.py
status: draft
reviewed_by: 待审
review_date:
grade:
updated_at: 2026-09-06
trigger:
  natural_language:
    - 会话收尾/下班前写复盘
    - Truman 11章复盘怎么写
    - 复盘被判 C 级/🔴
    - daily-context-save 怎么用
    - review-check 等级怎么看
    - 差异栏空白
---

# review-chain：收尾复盘链（daily-context-save + review-check）

> **一句话**：把 11 章复盘写成文件 → `daily-context-save save --truman --file <路径>` 双写落盘 → 脚本自动判级；🔴 C 级 = 重写，不是交差。

## 何时用

- 每次会话结束前（不跑 = 会话未完成，各角色 context 里有硬性条款）
- 想知道自己昨天的复盘被判了什么等级（`review-check`）
- 换实例/多实例并行时，复盘要按实例分文件不互相覆盖

**不要用于**：任务提审证据（那是 `queue-transition complete --evidence`，两件事）；给人看的交付文档。

## 怎么调

### 第 1 步：把复盘写成文件（先写文件，再调脚本）

路径惯例：`C:\Users\Administrator\Desktop\agent复盘\<角色>\daily-context\YYYY-MM-DD.md`

必须含 **11 章标题**（缺章降级；`差异栏` 空白 = 直接 🔴 C 级红线）：

```
## 差异栏        # 本次 vs 上次复盘哪里不同：新视角/复发模式/被打破的假设
## 概要
## 关键决策      # 表：决策|理由|结果
## 思维盲点      # ≥2 条且每条追问"为什么漏掉"（A 级硬指标）
## 顿悟
## 过程资产      # 表：新增/更新|路径
## 元反思
## Truman复盘
### 逐轮映射     # 表：轮次|人做了什么|双三角|AI做了什么|双三角
### 飞轮效应
### 对照实验
### 下次改进
## 本会话发现的问题   # #458 强制兜底节；有则列，无则写「无」
```

### 第 2 步：保存 + 自动判级（一条命令）

```bash
cd C:\Users\Administrator\Desktop\wiki
python kdo-tools/daily-context-save.py save --agent laowantong --truman --file "C:/Users/Administrator/Desktop/agent复盘/laowantong/daily-context/2026-09-06.md"
```

| 参数 | 用途 | 备注 |
|:--|:--|:--|
| `--agent <id>` | 拼音角色名（必填） | `huangyaoshi/wangyuyan/laowantong/ouyangfeng/hongqigong/duanwangye/sales-dialogue-assistant` |
| `--file <路径>` | 从文件读复盘（**推荐**，长内容） | 先用 Write 工具把 11 章写进去，再传路径 |
| `--stdin` | 管道输入（推荐替代） | `cat 复盘.md \| python kdo-tools/daily-context-save.py save --agent x --truman --stdin` |
| `--text "<摘要>"` | 短内容直接内联 | 长复盘别用，会被截断成低分 |
| `--instance <标识>` | 多实例分文件 | 如 `--instance kimi`，避免同日多实例互相覆盖 |
| `list --agent <id>` | 列历史上下文 | 查断档 |

**双写落盘**（脚本自动，不用手动复制）：
1. `桌面/agent复盘/<agent>/daily-context/YYYY-MM-DD.md`（人看）
2. `60_feedback/session-archives/YYYY-MM-DD/<agent>.md`（agent 检索，`kdo query` 可查）

### 第 3 步：看等级，🔴 就重写

```bash
python kdo-tools/review-check.py --agent laowantong   # 单人；不带 --agent=全量审计日报；--json=机读
```

| 等级 | 硬指标（全要满足） |
|:--|:--|
| 🟢 A | ≥3000B + 11 章 + 差异栏非空 + 盲点≥2 且有追问 + **检索 wiki 有发现** + 深度四条全过 + 「本会话发现的问题」节必填 |
| 🟡 B | ≥1500B + ≥8 章 + 盲点≥1 + 至少提及检索（§10.4.1） |
| 🔴 C | 差异栏空白（#268 重复自审红线）/ 章节数或字数不达标 |

`daily-context-save` 收尾会自动打印 `📋 自检：<emoji> <等级>` 并写 L0 事件（时间胶囊）；🔴 时脚本会直接回显重跑命令——**改完文件重跑同一条 save 命令即可，不换路径**。

## 边界与红线

1. **复盘内容自己写**，脚本只管格式校验与落盘——模板纯保存（`--truman` 不带 `--file/--stdin`）= 存一份空模板，必 🔴。
2. **等级是机制不是观感**：差一个硬指标就降级；别在报告里写「自评 A」，以 `review-check` 输出为准。
3. **`检索 wiki 有发现` 是 A 级硬指标**：会话里确实用过 `kdo query` 且复盘里写了发现，才不是「未检索wiki」。
4. 提审任务的证据走 `queue-transition complete --evidence <文件路径>`——**--evidence 永远传文件路径，禁内联文本**（F-034/#444；#615/#624/#638/#640 四次踩坑），与本 skill 的 `--file` 是同一条肌肉记忆。
5. 复盘里的数字/结论遵守行为宪法：逐条标【实证】（附锚点）/【推断】/【猜测】。

## 常见坑（症状 → 修复）

| 症状 | 根因 | 修复 |
|:--|:--|:--|
| 自检显示 🔴 差异栏空白 | 复盘里 `## 差异栏` 下没写字 | 补写「本次 vs 上次哪里不同」，重跑 save |
| 明明写了 11 章却判 C | 标题写法不一致（如「### 差异栏」「## 一、概要」） | 章名按上文清单逐字写（脚本按标题字符串匹配） |
| 显示「⚠️未检索wiki」降级 | 会话没用过 `kdo query` / 复盘没写检索发现 | 下次会话先检索再下结论（行为宪法第三条），复盘里如实写检索到的内容 |
| 两个实例同日复盘互相覆盖 | 没传 `--instance` | 加 `--instance <标识>` 分文件 |
| 复盘写完忘了跑 save | 收尾流程断在最后一步 | 把 save 命令写进 todos 收尾动作；跑完必须看到 🟢/🟡 |

## 失败模式（本技能特有）

| 失败 | 可识别信号 | 修复 |
|:--|:--|:--|
| 复盘写成工作日志流水账 | 「今天做了 A、B、C」无差异栏无盲点 | 按第 1 步清单逐章填，盲点必须答「为什么漏掉」 |
| 刷字数凑 A | 复制粘贴任务单原文充字数 | 深度四条会拦；写真实的新信息增量 |
| 只在本机桌面留档 | 桌面路径写了但没跑 save | 没跑 save = 没进 session-archives = agent 检索不到 = 等于没写 |

## 相关协议与卡

- 复盘格式权威定义：`agents/agent-os.md` §10.2（11 章）；等级口径源码：`kdo-tools/review-check.py`（`TEN_CHAPTERS`/判级函数）
- 事件留痕：`kdo-tools/daily-context-save.py`（L0 胶囊事件；写失败会落 `20_memory/` 报警行）
- 姊妹 skill：`queue-transition`（收尾提审的门禁与 --evidence 口径）
