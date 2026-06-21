# KDO 开机必读

> 最后更新：2026-06-21
> **每个 Agent 启动后，在领任务之前，必须先读这个文件。** 3 分钟了解工厂全局。

## 零之零：正确的工作姿势（先读这个）

**任何任务，调研是第一步。最佳实践是最好的老师。**

接到任务 → 不要直接动手。先问三个问题：
1. 业界谁做过类似的事？怎么做的？
2. 有没有开源方案 / 成熟模式可以参考？
3. 2025-2026 年的最佳实践是什么？

查完再设计，设计完再执行。Google Research、LlamaIndex、Obsidian 社区已经把路走通了——**不要重新发明轮子，不要凭记忆做决策。**

> 反面教材：黄药师 2026-06-21 建检索方案时直接写代码，浪费一个版本。补调研后发现 MOC+BM25+RRF 才是正解。

## 零、启动动作（3 步，3 分钟）

1. **确认你是谁** → 读 `.agent/<角色>-context.md`（不知道角色？先读 `90_control/AGENTS.md` 判断）
2. **读完本文件** → 了解工厂有什么、当前谁在做什么、紧急注意
3. **领任务** → 读 `70_product/tasks/dashboard.md`，找自己的任务

> ⚠️ **本次会话结束前，必须回答三问（见 CLAUDE.md 末尾）**：
> ① 今天产生了什么新资产？ ② 今天发现了什么新问题/阻塞？ ③ 下次启动最需要记住什么？**不答完不算完成。**

---

## 一、我有啥？（工具清单——每项含：在哪 + 怎么调 + 谁常用）

| 能力 | 路径 | 怎么调 | 谁常用 |
|:--|:--|:--|:--|
| **OCR（PaddleOCR v5）** | `C:\Users\Administrator\ocr-pipeline\` | `node ocr-paddle.cjs <image>` / PowerShell `ocr-image.ps1` | 老顽童 / 洪七公 |
| **OCR（RapidOCR）** | `C:\Users\Administrator\Desktop\wiki\_tmp\ocr_venv\` | `from rapidocr import RapidOCR` | 王语嫣（轻量） |
| **PDF 解析** | WSL `/home/dministrator/.local/bin/mineru` | `magic-pdf` CLI | 洪七公 |
| **语义检索** | KDO CLI | `kdo query "<问题>"` | 全员 |
| **Graph RAG** | KDO CLI | `kdo graph query "<问题>" --json` | 黄药师 / 王语嫣 |
| **联网搜索** | `kdo-tools/web_search.py` | `python kdo-tools/web_search.py "query" --json` | 王语嫣 / 老顽童 |
| **域迭代五阶段法** 🆕 | `.claude/skills/domain-iteration/` | `/domain-iteration` → 自动按阶段调用子 Skill | 全员（收到新域任务时调用） |
| **质量门禁** | `90_control/scripts/` | `python 90_control/scripts/kcard-quality-gate.py` | 黄药师 / 王语嫣 |
| **Lint** | KDO CLI | `kdo lint` 或 `python 90_control/scripts/kdo_lint.py` | 黄药师 |
| **卡片骨架** | KDO CLI | `kdo scaffold --new --card <id> --type <type>` | 老顽童 |
| **内置 Skills** | `40_outputs/capabilities/skills/` | 12 个 skill（OCR / Design / Audio / Video / …） | 按需 |
| **工具脚本** | `40_outputs/code/scripts/` | 见 `40_outputs/code/scripts/README.md` | 全员 |

> ⚠️ **工具登记纪律（洪七公 + 王语嫣共识）**：完成一个工具/脚本后：
> 1. 脚本放到 `40_outputs/code/scripts/`
> 2. 在 `40_outputs/code/scripts/README.md` 登记（名称、路径、用途、调用示例）
> 3. 有复杂决策逻辑 → 写 skill 到 `40_outputs/capabilities/skills/`
> 4. 相关 skill 之间互引
> 不登记 = 不存在。王语嫣花了 4 步才找到 RapidOCR 的教训不要再重复。

---

## 二、我该知道什么？（6 条最高频铁律——踩过血的）

| # | 铁律 | 来源 |
|:--:|:--|:--:|
| 1 | **不跨角色派活** — 唯一协调节点 = 欧阳锋。角色之间不互相派活 | AGENTS.md |
| 2 | **不改别人卡片** — 王语嫣禁写 `30_wiki/`（例外：自己产出的卡可回填），黄药师禁内容判断 | 角色回归 2026-06-16 |
| 3 | **约束指令落笔到任务文件** — 口头审查意见 = 不存在。换会话就丢（P-10） | `pitfalls.md` |
| 4 | **先查武器库再行动** — `.agent/toolkit.md` 有全套本地工具，不要重复造轮子（P-8） | `pitfalls.md` |
| 5 | **批量操作三问** — ① dry-run 预览了没？② 预期变更范围声明了没？③ 非空值不覆盖了没？（P-29/P-30） | `pitfalls.md` |
| 6 | **🆕 写审分离——"牲口而非宠物"** — 产卡Agent不得审查自己的卡片。`author` ≠ `reviewed_by`。每次审查启动新Agent实例，不带前序包袱。`kdo lint` 已强制执行 | Harness Engineering (2026-06-21) |

> 完整 25 条铁律 + 16 种失败模式 → `90_control/kdo-industrialization-manual.md`
> 14 条禁止清单 + 角色分工详情 → `90_control/AGENTS.md`

---

## 三、当前谁在做什么？（2026-06-19）

| 角色 | 代号 | 运行位置 | 当前任务 | 状态 |
|:--|:--|:--|:--|:--:|
| 架构师 | 欧阳锋 | Obsidian | 月度抽检模式 | ✅ |
| 构建者 | 黄药师 | WSL tmux | KF-020+021 全修 / S4-1 aliases / 决策域研究 / 待命 | ✅ |
| 生产者 | 老顽童 | WSL tmux | 第二十四节 5 张卡返工 diagnostic_signals | 🔴 阻塞 |
| 顾问 | 王语嫣 | Hermes → 飞书 | 六阶段全库审计闭环 | ⏳ |
| 多模态 | 洪七公 | Hermes → 飞书 | 待命 | ⏸️ |
| 发布者 | 段王爷 | Hermes → 飞书 | 待命 | ⏸️ |

### 当前阻塞项

| 阻塞 | 影响谁 |
|:--|:--|
| 王语嫣角色正式升级 AGENTS.md | 老顽童（阻塞第二十四节返工） |
| KF-022 decisions 域 lint 修复（84 errors） | 黄药师（排期中） |

---

## 四、紧急注意（近 2 周复现过的坑，每条 1 行）

| 编号 | 症状 | 一句话对策 |
|:--:|:--|:--|
| **P-29** | 批量脚本覆盖了 26 张卡已有的 source_context | 非空不覆盖，加 dry-run 模式 |
| **P-30** | 486 个文件变更无从审查——未声明范围 | 批量操作前在任务文件声明影响范围和修改字段 |
| **P-28** | API 报错调参 3 小时，结果是提供商当天发新版 | 先查公告，再调参（WebSearch 在第 3 步触发，不是第 30 步） |
| **P-21** | 无诊断手段时盲目调参——撞运气 | 先造诊断工具，再定位，最后才修 |
| **Hermes 掉线** | 飞书 Agent 无响应 | `systemctl --user restart hermes-gateway-*` |

> P-1 到 P-30 全集 → `.agent/pitfalls.md`

---

## 五、快速导航（指针，不重复内容）

| 想看什么 | 去这里 |
|:--|:--|
| 角色分工 + 禁止清单 | `90_control/AGENTS.md` |
| 踩坑全集（35 条） | `.agent/pitfalls.md` |
| 欧阳锋审查方法论（新） | `30_wiki/frameworks/framework-ouyangfeng-review-methodology.md` |
| 武器库（本地工具） | `.agent/toolkit.md` |
| 基建变更公告 | `.agent/infrastructure-bulletin.md` |
| 工厂铁律 + 失败模式（25 条） | `90_control/kdo-industrialization-manual.md` |
| **卡片→Skill 迭代标准（新）** | `30_wiki/decisions/plan_20260621_skill-iteration-standard.md` |
| 共享状态 + 里程碑 | `.agent/context.md` |
| 架构决策记录 | `.agent/decisions.md` |
| 运作原则（9 条） | `20_memory/operating-principles.md` |
| 走过的弯路（11 条） | `20_memory/corrections.md` |
| KDO CLI 命令速查 | `90_control/cli-reference.md` |
| 任务仪表板 | `70_product/tasks/dashboard.md` |
| 角色专属指令 | `.agent/<角色>-context.md` |
| 一页纸角色摘要（自动生成） | `.agent/agent-contexts-summary.md` |
