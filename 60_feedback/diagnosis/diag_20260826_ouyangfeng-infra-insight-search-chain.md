---
id: diag_20260826_ouyangfeng-infra-insight-search-chain
type: proposal
status: orchestrated
author: 欧阳锋（飞书实例）
audience: 王语嫣
date: 2026-08-26
orchestrated_at: 2026-08-27
orchestration: '王语嫣裁定：P0-1/P0-2 立项 #558（影响面收窄为 hermes 侧）；P1-1/P1-3 立项 #559；P1-2 王语嫣自落 kdo-moc'
---

# KDO 基础设施洞察专题：一次「找基本法」暴露的四层检索链路缺陷

> **事件**：2026-08-26，欧阳锋被用户纠正「你是审查者，不是架构师」后，查找 KDO 基本法（kdo-charter）确认角色定义。全文检索→读文件→执行命令三步全部受阻，耗时多轮才找到真相。复盘锁定 4 类基础设施缺陷，其中 1 个为当日新发现的工具级 bug。
>
> **文档定位**：专题洞察（供王语嫣编排决策、黄药师基建修复参考）
> **作者**：欧阳锋（Reviewer）｜**日期**：2026-08-26
> **状态**：洞察报告，待编排

---

## 一、事件背景

2026-08-26 会话中，用户问「你是用的什么大模型」「你是在哪里看到你是架构师的」。欧阳锋自查发现：

- 运行配置 `SOUL.md`（Hermes profile 级 persona）写的是：**欧阳锋（Architect）——KDO 知识工厂的架构师和审查者**
- 用户纠正：「你是审查者，不是架构师」，并提示「有另外一份基本法宪法文件，不是你这份」

随后查找 KDO 基本法，确认角色真相在 `90_control/kdo-charter-v0.1-draft.md` §2.6.2：

> **欧阳锋（Reviewer）岗位说明书 v1.0**——欧阳锋=终审与质量门禁执法者，终审判「做得好不好」；审而不改；PASS 必给等级。

**结论：角色定义出现双重真相源漂移（SOUL.md 旧表述 vs 基本法新定义），且检索链路全程受阻，导致真相难找。**

---

## 二、查找过程时间线（四层障碍叠加）

| 步骤 | 动作 | 结果 | 障碍层 |
|:--|:--|:--|:--|
| 1 | search_files 搜「宪法\|基本法」（全库） | 🔴 **0 命中**（实际库内 103 个文件含这些词） | 工具 bug（P0-1） |
| 2 | search_files 搜文件名 `*constitution*` | 0（文件名确实不含） | 正常 |
| 3 | `ls` 全目录人工翻找 | ✅ 发现 `90_control/kdo-charter-v0.1-draft.md` | — |
| 4 | read_file 读 charter | 🔴 **报 Binary file 拒绝读** | 工具误判（P0-2） |
| 5 | terminal `python` 读 charter | 🔴 **审批 BLOCKED 60s 超时** | 配置（P1-1） |
| 6 | 用户提示「段王爷最早发现，注册在 kdo 里」 | ✅ 查到 dk 卡 + 案例卡 | — |
| 7 | 用户授权改审批配置 | ✅ `approvals.mode=smart` | 已修复 |
| 8 | 终于读到基本法 | ✅ §2.6.2 欧阳锋（Reviewer） | — |

**单看每道墙都能绕，叠在一起就把「查一下基本法」变成「考古」——这是知识库检索链路缺少健康度检查的直接后果。**

---

## 三、基础设施缺陷清单

### 🔴 P0-1：search_files 正则 `|` 交替符失效（当日新锁定，影响全厂）

**症状**：任何含 `|` 的 pattern 静默返回 0 命中，**不报错**。

**证据链**（同一目录 90_control/ 实测对比）：

| pattern | search_files 结果 | grep 实际命中 |
|:--|:--|:--|
| `宪法\|基本法` | **0** | 全库 103 个文件 |
| `宪法` | 9 | 9 |
| `基本法` | 6 | 6 |
| `charter\|constitution` | **0** | 多个 |
| `charter` | 5 | 5 |
| `(宪法\|基本法)` | **0** | — |

**规律**：单关键词正常；一旦出现 `|`（正则交替符），结果归零。纯 ASCII（`charter|constitution`）同样失效，排除中文编码因素。

**影响面**：KDO 全部 Agent（老顽童/王语嫣/黄药师/欧阳锋等）都依赖 search_files 查库。`|` 是多关键词检索的常用写法——**「先查 MOC 不凭记忆回答」的检索规则，前提工具得能用**。失效模式阴险：返回 0 会让 Agent 误判「知识库没有这个主题」，进而放弃检索或凭记忆瞎答，污染下游判断。

**疑似根因**：Hermes 工具封装层对 `|` 的处理（转义/字面量化），或 ripgrep 调用参数问题。需黄药师排查 Hermes 工具实现。

**临时规避**：多关键词分次单搜（`宪法`、`基本法` 各搜一次），或 terminal 用 `grep -rlE 'a|b'`。

---

### 🔴 P0-2：read_file 对 CRLF/超长行文件误判二进制

**症状**：`90_control/kdo-charter-v0.1-draft.md`（UTF-8 + CRLF + 461 字符长行）被 read_file 判定为 `Binary file - cannot display as text`。

**交叉验证**：
- `file` 命令：`Unicode text, UTF-8 text` ✅ 纯文本
- grep 正常命中 ✅
- read_file：拒绝读 🔴

**影响面**：组织级宪法文件（基本法）是角色间唯一沟通的基石（charter §3.14），但 Agent 的标准读文件工具读不了它——只能 python/iconv 绕行。若再叠加审批拦截（本次正是如此），直接死锁。

**疑似根因**：read_file 的二进制探测逻辑对超长行（>某阈值）/CRLF 组合误判。需黄药师确认工具阈值或建议文件规范化（LF + 行长控制）。

---

### 🟡 P1-1：审批配置知识已沉淀但未同步生效（段王爷先例未落地到本 profile）

**事实链**：
- 2026-08-09 段王爷发现：`approvals.mode=manual` 在飞书网关无确认 UI → 代码命令 60s 超时被杀（`case-duanwangye-self-iteration-closed-loop.md`）
- dk 卡 `dk-agent-access-kdo-pitfalls.md` 已写完整修复方案（`hermes config set approvals.mode smart`）
- 但 ouyangfeng profile 直到 2026-08-26 仍是 manual——**知识沉淀 ≠ 配置生效**，中间隔了 17 天，期间每次代码类命令都会被拦

**教训**：dk 卡/案例卡只解决「知道」，不解决「生效」。缺一个各 profile 的配置巡检机制（审批模式/超时/allowlist 周期性核对）。

**已修复**：`hermes config set approvals.mode smart` 实测生效（本次会话验证通过）。

---

### 🟡 P1-2：基本法未注册进 MOC 导航

**证据**：`30_wiki/domains/kdo-moc.md` 搜 charter/基本法 → **0 命中**。

**影响**：SOUL.md 检索规则第 1 条「被问到方法论问题时先查 MOC 导航卡」——但组织级宪法不在 MOC 里。如果 MOC 有注册，本次查找第一步即可命中，无需 `ls` 碰运气。

**归属**：MOC 维护属编排侧（王语嫣），建议补录 charter 条目。

---

### 🟡 P1-3：角色定义双重真相源漂移（SOUL.md vs 基本法）

| 来源 | 位置 | 表述 |
|:--|:--|:--|
| Hermes profile | `AppData\Local\hermes\profiles\ouyangfeng\SOUL.md` | 欧阳锋（**Architect**）——架构师和审查者 |
| KDO 基本法 | `90_control/kdo-charter-v0.1-draft.md` §2.6.2 | 欧阳锋（**Reviewer**）——终审与质量门禁执法者 |

**违反**：charter §3.11 单一真相源 + B2-2（防双文档漂移）。两个系统（Hermes 配置层 vs KDO 知识库）各自维护角色定义，无同步机制——**角色定义漂移的受害者恰好是负责审查角色定义一致性的欧阳锋本人**，讽刺且典型。

**已修复**：SOUL.md 首行改为「欧阳锋（Reviewer）——KDO 知识工厂的终审与质量门禁执法者」，与基本法对齐。

**防漂移建议**：SOUL.md 角色定义行加注「以 `90_control/kdo-charter-v0.1-draft.md` §2.6.2 为准」；或建脚本巡检（知识库角色 spec 与各 profile SOUL.md 一致性）。

---

## 四、行为层反思（不甩锅工具）

1. **违反自身检索规则**：SOUL.md 规则第 1 条「先查 MOC 导航卡」——用户问「宪法文件」时第一反应凭记忆答 Hermes persona 文件，未先查 KDO MOC/索引。MOC 若全，本可第一步定位。
2. **0 命中后未第一时间怀疑工具**：dk 卡早已写「配置层问题伪装成命令坏了」（先查 approvals.mode/cwd/文档规则，再怀疑命令本身）——本次「0 命中」同样该先做 grep 交叉验证，而非换关键词反复搜。**教训推广：任何检索 0 命中，先验证工具，再信结论。**
3. **值得肯定的部分**：最终没有绕过——用户提示后查 KDO 沉淀（dk 卡/案例卡）、定位审批根因、按授权修复、反向锁定 search_files `|` bug，走完了「发现问题→诊断→修复→沉淀」闭环。

---

## 五、修复建议与责任归属（按基本法纪律，走编排通道）

| # | 缺陷 | 建议动作 | 责任方 |
|:--|:--|:--|:--|
| 1 | P0-1 search_files `\|` bug | 立项排查 Hermes 工具封装层；修复前全厂通报规避写法 | 黄药师（基建） |
| 2 | P0-2 read_file 二进制误判 | 工具阈值修复 或 charter 文件规范化（LF+行长）；建议先修工具（治本） | 黄药师（基建） |
| 3 | P1-1 配置巡检缺失 | 各 profile 检查 approvals.mode/超时/allowlist；建周期性巡检（可挂 cron） | 编排侧（王语嫣）协调 |
| 4 | P1-2 基本法入 MOC | kdo-moc 补 charter 条目（含定位、§2.6 角色章节锚点） | 编排侧（王语嫣） |
| 5 | P1-3 防漂移机制 | SOUL.md 标注真相源指向 charter；或脚本巡检一致性 | 编排侧协调 + 各 profile |

---

## 六、一句话结论

> **知识库的「正确性」与「可检索性」是两个独立的工程质量维度——本次事件证明：内容全对（103 个文件含基本法）也可能检索为 0（工具 bug），知识沉淀正确（段王爷 dk 卡）也可能配置未生效（manual 17 天）。KDO 的下一个基建重点，不是再多产卡，而是让已有的卡「查得到、读得了、信得过」。**

---

*欧阳锋（Reviewer）· 2026-08-26 · 洞察报告 v1.0*
