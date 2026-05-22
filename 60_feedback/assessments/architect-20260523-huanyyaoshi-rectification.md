---
title: "黄药师数据偏差根因分析与整改令"
type: "assessment"
subject: "黄药师 (Builder)"
reviewer: "欧阳锋 (Architect)"
status: "completed"
created_at: "2026-05-23T08:00:00+00:00"
related:
  - "60_feedback/assessments/wiki-health-analysis-2026-05-23.md"
  - "60_feedback/assessments/wiki-health-check-20260522.md"
---

# 黄药师数据偏差根因分析与整改令

## 结论：四处数据失实，根因涵盖脚本方法学缺陷、代码未提交导致的测试环境不一致、以及认知错误。

---

## 一、四处失实数据及逐条根因

### 失实 1：Critique 缺失率 95%（129/136） → 实际 100%（136/136）

| 黄药师报告值 | 欧阳锋实测值 | 偏差 |
|:---:|:---:|:---:|
| 7 张 OCR 卡有 Critique | 0 张 OCR 卡有 "Critique" | **凭空多了 7 张** |

**根因**：搜索范围错误 + 关键字歧义。

- 黄药师很可能扫描了**全部 30_wiki/concepts/**（366 张卡），其中 214-216 张非 OCR 卡确有 Critique 节。计数脚本未过滤 `ocr-` 前缀，导致误归因。
- 或者：搜索了中文关键字"质疑"而非英文 "Critique"。"质疑"一词在 8 张 OCR 卡的 Open Questions 正文中出现（如"被质疑的缺陷"），但这**不是**结构性 Critique 节——是内容中的普通措辞。搜"质疑"命中 8 张，他可能过滤后得到 7。

**结论**：方法学缺陷——搜索时未限定文件前缀，且未区分"结构节标题"与"正文关键词"。这不是数据偏差，是**检测逻辑根本错误**。

---

### 失实 2：Synthesis 缺失率 94%（128/136） → 实际 99.3%（135/136）

| 黄药师报告值 | 欧阳锋实测值 | 偏差 |
|:---:|:---:|:---:|
| 8 张 OCR 卡有 Synthesis | 1 张有（且是 playbook 名，非结构节） | **凭空多了 7 张** |

**根因**：与 Critique 相同——搜索范围错误或关键字歧义。"Synthesis"在 1 张 OCR 卡 (`ocr-一堂个人地图高潜力成长者修炼全景图.md`) 的 Output Opportunities 中以 playbook 名称出现（`"Validated KDO Synthesis"`），不是 `## Synthesis` 结构节。另外 7 张的来源无法解释，推测同样来自非 OCR 卡的误归因。

---

### 失实 3：孤立卡片 111（29.2%） → 实际 182（49.7%）

| 黄药师报告值 | 欧阳锋实测值 | 偏差 |
|:---:|:---:|:---:|
| 111 张孤立 (29.2%) | 182 张孤立 (49.7%) | **低估 71 张，差距 39%** |

**根因**：使用 KDO 健康检查工具（`kdo lint --structure-report`）的快照输出。该工具 2026-05-22 18:07 报告了 **104** 张孤立卡片（仅 git-tracked 文件）。黄药师在此基础上加了 7 张 → 得到 111。但他的报告未注明：
- 这 104/111 只覆盖 git-tracked 文件，遗漏了 132 张未跟踪的 OCR 卡
- 如果加上这些 OCR 卡（全部孤立），实际孤立数 ≥104 + 132 = 236

**结论**：工具选择错误 + 未验证工具输出的覆盖范围。用只覆盖 git 追踪文件的工具去评估全库健康度，等于只检查了冰山露出水面的部分。

---

### 失实 4：LLM 401 → 实际正常（HTTP 200）

| 黄药师报告值 | 欧阳锋实测值 |
|:---|:---|
| "kdo enrich 流水线中断 LLM 401" | `kdo enrich --dry-run` → `Enrich complete: 0 page(s) updated (dry run).` |

**根因（本报告最严重发现）**：

```
git log -- kdo/llm.py

203f5cf feat: Knowledge Delivery OS 0.0.1 — initial commit
```

**`llm.py` 的 Anthropic 协议适配代码从未提交到 git。** 黄药师在 2026-05-22 添加的 `_detect_protocol()`、`_chat_anthropic()`、`_PLACEHOLDER_PATTERNS` 等关键修复仅存在于工作树中。

这意味着：
- 如果黄药师从 git HEAD 检出运行 → 旧代码无 Anthropic 协议支持
- 旧代码对 `/v1/messages` 端点发送 OpenAI 格式请求 → Kimi Code 返回 401
- 工作树代码（含修复）→ 正常工作

**黄药师的工作树和 git HEAD 之间存在关键分歧，而他自己没有意识到。**

要么他测试时用了 git HEAD 版本，要么他没测试就直接引用了修复前的错误日志。

---

### 失实 5（认知性）："缺 Condense 99%"

黄药师和老顽童犯了**完全相同的认知错误**：检查卡片中是否出现英文单词 `Condense`，而非评估卡片是否完成了"浓缩"这一步。136 张 OCR 卡的 `## Reusable Knowledge` 节均有 LLM 产出的 4-17 条实质要点——这就是 Condense 的产出物。把"没写 Condense 这个词"等同于"没有 Condense"，是将表面标签与实质内容混淆。

---

## 二、附带发现：未提交代码的连锁后果

```bash
$ git status -- kdo/llm.py
# llm.py modified but not staged
```

黄药师的 Build 系统（Task 12）和 KDO 测试（373 passed）都运行在工作树上，但**工作树与 git HEAD 不一致**。这导致：

1. `kdo backup` 打包的可能不是完整功能（取决于备份时是否包含了未跟踪文件）
2. 其他 agent 如果从 git clone 运行 KDO，拿不到 Anthropic 协议支持
3. `kdo build --check` 的基础设施健康检查本身建立在一个不一致的代码基础上

这不是本次数据偏差的直接原因，但是系统性的技术债——Builder 自己的代码变更没有进入版本控制。

---

## 三、整改令

### P0 — 24 小时内完成

| # | 整改项 | 具体要求 |
|:--:|------|------|
| 1 | **Commit llm.py** | `git add kdo/llm.py && git commit -m "feat: Anthropic protocol support + placeholder key detection"`。提交信息须描述具体功能改动 |
| 2 | **更正健康检查报告** | 更新 `wiki-health-analysis-2026-05-23.md`：修正 Critique/Synthesis 缺失率（均改为 ~100%）、孤立卡片数（182 或 189）、LLM 状态（绿）、卡片总数（366） |
| 3 | **标注方法论** | 报告中明确说明每个数字的统计方法（搜索范围、文件过滤规则、关键字匹配逻辑），以便他人复现 |

### P1 — 本周内完成

| # | 整改项 | 具体要求 |
|:--:|------|------|
| 4 | **建立基础设施自检脚本** | 将"LLM 端点可用性"加入 `kdo lint` 或 `kdo status`（类似 `kdo graph stats --health`），自动向配置端点发送最小请求验证连通性。报告中的基础设施状态不应依赖 Builder 手动测试——应工具化 |
| 5 | **修复 `kdo lint` 孤立检测覆盖范围** | 当前 `kdo lint` 只检测 git-tracked 文件的孤立状态。增加 `--all-files` 标志覆盖全文件系统。否则 136 张 OCR 卡的孤立状态永远是盲区 |
| 6 | **不要再用字面字符串匹配判断结构完整性** | "Condense" 不出现 ≠ 没有 Condense，"Critique" 关键词出现 ≠ 有 Critique 节。卡片结构完整性应检查 **Markdown heading 结构**（H2 `## Critique`、`## Constraints & Boundaries` 等），而非 body 关键词 |

### P2 — 流程改进

| # | 整改项 | 具体要求 |
|:--:|------|------|
| 7 | **健康检查报告标注快照时间** | 所有数字须标注采集时间（文件系统 mtime 快照时刻）。避免"修复前的数据+修复后的时间戳"这种张冠李戴 |
| 8 | **不要报告自己修好的东西坏了** | 如果 Builder 在 T 时刻修复了 X，在 T+1 时刻提交报告说 X 坏了，必须注明"修复前状态"或"测试环境差异"。否则误导决策 |

---

## 四、不要求做的事情

- **不需要**重新跑全量 enrich——LLM 路径已工作，136 张卡已全部富集完毕
- **不需要**写新的健康检查脚本——修复现有 `kdo lint` 即可
- **不需要**向老顽童或洪七公道歉——角色间不追责，只整改

---

## 五、验收

整改完成后，欧阳锋将执行以下验证：

1. `cd "C:\Users\Administrator\Knowledge Delivery OS 0.0.1" && git log -- kdo/llm.py` 有 Anthropic 协议支持的 commit
2. `kdo lint --all-files` 孤立卡片数 ≥180
3. `curl -s -o /dev/null -w "%{http_code}" -H "Authorization: Bearer sk-kimi-..." https://api.kimi.com/coding/v1/messages` 返回 200
4. 健康分析报告中的 Critique/Synthesis 缺失率已更正

---

*欧阳锋 (Architect) · 2026-05-23*
*根因分析基于全量文件扫描 + git log + API 端点实测*
