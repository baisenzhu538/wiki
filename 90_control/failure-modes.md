---
title: "KDO 失败模式库"
type: "control"
status: "draft"
created_at: "2026-05-03"
source: "EC工业化规范手册 第十三章 — 失败模式库方法论"
---

# KDO 失败模式库

> 每踩一次坑，入库一种模式。目标是下一个 Agent session 启动时读一遍，执行前就知道哪里会摔。

---

## 模式索引

| 编号 | 名称 | 严重度 | 状态 |
|------|------|:------:|:----:|
| F-KDO-001 | CJK regex 静默零返回 | 🔴 | 已知，无自动化防御 |
| F-KDO-002 | 非 .md 文件 ingest 静默跳过 | 🟠 | 已知，无自动化防御 |
| F-KDO-003 | state.json 覆盖写竞态 | 🔴 | 已修复代码，未入库 |
| F-KDO-004 | 错误工作目录执行 pipeline 命令 | 🟠 | 已知，无自动化防御 |
| F-KDO-005 | 过期 feedback 引用残留 | 🟡 | 已知，手动清理 |
| F-KDO-006 | 骨架页面 CJK 内容损毁 | 🟠 | 设计约束，手动绕过 |

---

## F-KDO-001: CJK regex 静默零返回

| 属性 | 内容 |
|------|------|
| **触发命令** | `kdo enrich --all` |
| **表现** | 输出 "0 pages enriched"，无报错，无任何页面被更新 |
| **根因** | `extractors.py` 中的 `extract_open_questions()` 使用 `\b` 词边界匹配——`\b` 不识别中文字符边界，对全中文页面永远返回空列表 |
| **触发信号** | `kdo enrich --all` 输出 "0 pages enriched" 但 wiki 目录下有未 enrich 的中文页面 |
| **防御措施** | ① `kdo self-check` 的 unenriched-wiki-page 检查会在事后发现（已生效）② 事前防御：ingest 时检测内容语言，CJK 内容跳过 regex enrich 并提示走 Agent 三步编译 |
| **临时绕过** | Agent 直接编辑 wiki 页面文件，执行三步 CJK 编译（浓缩→质疑→对标），手动更新 frontmatter status=enriched |
| **永久修复** | 配置 `KDO_LLM_ENDPOINT` 环境变量启用 LLM-based CJK enrich 路径（`curation.py:enrich_wiki_page_llm`），或等待 `extractors.py` 增加 CJK-aware 分词器 |
| **关联文件** | `kdo/extractors.py`, `kdo/commands/curation.py` lines 142-336 |

---

## F-KDO-002: 非 .md 文件 ingest 静默跳过

| 属性 | 内容 |
|------|------|
| **触发命令** | `kdo ingest` |
| **表现** | 对 `.txt` 文件：无输出、无报错、state.json 无变化、无源文件创建。用户以为 ingest 成功了。 |
| **根因** | `kdo ingest` 只扫描 `00_inbox/*.md`，其他扩展名被静默忽略 |
| **触发信号** | `ls 10_raw/sources/` 没有新文件产生；state.json 的 `ingested_inbox_files` 列表无新增 |
| **防御措施** | ingest 完成后：① 打印实际处理的文件数量 ② 对 `00_inbox/` 中剩余的非 .md 文件给出 warning ③ 建议在 ingest 前跑 `find 00_inbox -type f` 确认所有文件都是 .md |
| **临时绕过** | `cp file.txt file.md && rm file.txt` 后重新 ingest |
| **关联文件** | `kdo/commands/ingestion.py` |

---

## F-KDO-003: state.json 覆盖写竞态

| 属性 | 内容 |
|------|------|
| **触发命令** | `kdo improve --apply` |
| **表现** | improve 执行后 wiki_snapshots 为空，revision 记录丢失。无报错。 |
| **根因** | `snapshot_wiki_page()` 内部独立调用 `load_state()` + `save_state()`，但调用方 `cmd_improve()` 之后也用自己持有的旧 state dict 写回磁盘，覆盖了 snapshot 的写入 |
| **触发信号** | `kdo improve --apply` 成功但 `.kdo/state.json` 中 `wiki_snapshots` 为空 |
| **防御措施** | ① 代码修复：`snapshot_wiki_page()` 接受调用方的 state dict 参数，不独立读写 ② 所有写 state.json 的函数统一走一个 save 入口 |
| **状态** | 代码已修复（2026-05-01），但问题模式未记录入库 |
| **关联文件** | `kdo/commands/feedback.py`, `kdo/workspace.py` |

---

## F-KDO-004: 错误工作目录执行 pipeline 命令

| 属性 | 内容 |
|------|------|
| **触发命令** | `kdo revise --scan`, `kdo improve --apply` 等 |
| **表现** | 命令静默失败——不报错、不更新文件、不改变 state.json |
| **根因** | 命令依赖 `find_workspace()` 定位 wiki 根目录。从非 wiki 目录（如 `~/.claude/plugins/`）执行时，`find_workspace()` 要么找不到要么找到错误的目录 |
| **触发信号** | 命令返回 0 但无任何文件变化 |
| **防御措施** | ① 命令启动时打印当前识别的 workspace root ② `find_workspace()` 失败时 exit(1) 并给出明确信息而非静默降级 ③ 在 AGENTS.md 禁止清单中列出 |
| **禁止行为** | **不准在 `~/.claude/plugins/` 或任何非 wiki 根目录下执行 KDO pipeline 命令** |
| **正确做法** | 始终 `cd /mnt/c/Users/Administrator/Desktop/wiki` 后执行 |

---

## F-KDO-005: 过期 feedback 引用残留

| 属性 | 内容 |
|------|------|
| **触发命令** | `kdo lint` |
| **表现** | `ERROR: Feedback 'fb_xxx' path does not exist` —— lint 报告一个磁盘上已不存在的文件 |
| **根因** | feedback 的 .md 文件被删除（如 Obsidian 清理），但 state.json 的 `feedback` 列表中仍保留该文件路径 |
| **触发信号** | `kdo lint` 输出 "Feedback path does not exist" |
| **防御措施** | ① `kdo lint` 自动检测并清理 stale feedback 引用（当前只报错不修复）② 定期运行 `kdo self-check` ③ 删除 feedback 文件时同时从 state.json 移除 |
| **清理方法** | `python3 -c "import json; state=json.load(open('.kdo/state.json')); state['feedback']=[f for f in state['feedback'] if 'DEAD_ID' not in str(f)]; json.dump(state, open('.kdo/state.json','w'), indent=2)"` |
| **关联文件** | `.kdo/state.json` → `feedback` 列表 |

---

## F-KDO-006: 骨架页面 CJK 内容损毁

| 属性 | 内容 |
|------|------|
| **触发命令** | `kdo ingest` |
| **表现** | 自动生成的 `30_wiki/concepts/<page>.md` 骨架中，Summary 和 Reusable Knowledge 段落是随机断裂的中文碎片，不可读 |
| **根因** | `kdo ingest` 的 extractor 用 regex 提取段落摘要——`\b` 不识别中文词边界，在随机位置断句。与 F-KDO-001 同一根因。 |
| **触发信号** | 读自动生成的 wiki 页面骨架，中文内容为无意义的碎片拼接 |
| **防御措施** | 这是设计约束而非 bug——CJK extractor 未实现。当前所有 CJK 内容的骨架都是垃圾，需由 Agent 重写 |
| **临时绕过** | ingest 后立即读 wiki 页面，用三步 CJK 编译（浓缩→质疑→对标）完整重写 |
| **关联** | 与 F-KDO-001 共享根因，但触发阶段不同（ingest vs enrich） |

---

## 执行前自检清单

每个 Agent session 启动时，对照此清单：

```
□ F-KDO-001: 处理的页面是中文内容？→ 跳过 kdo enrich，走 Agent 三步编译
□ F-KDO-002: 00_inbox/ 有非 .md 文件？→ 先转换再 ingest
□ F-KDO-003: 即将执行 improve --apply？→ 确认 state.json 可写且无其他进程持有
□ F-KDO-004: 当前工作目录是 wiki 根目录？→ pwd 确认
□ F-KDO-005: 删除过 feedback 文件？→ 同步清理 state.json
□ F-KDO-006: ingest 中文源文件后？→ 立即读骨架页面，准备重写
```

---

> 更新规则：每次发现新模式 → 追加到此文件 → 更新索引表 → 更新执行前自检清单。
> 退役规则：当防御措施已自动化（如代码修复 + CI 门禁），将状态改为"已退役"而非删除。
