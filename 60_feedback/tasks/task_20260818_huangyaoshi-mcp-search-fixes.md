---
id: 357
assignee: huangyaoshi
status: pending_review
updated_at: 2026-08-18
title: "kdo MCP 检索质量 5 项根因修复（search/capabilities）——第三轮核查穿透"
priority: P1
dependency: []
---

# #357 kdo MCP 检索质量 5 项根因修复

## 背景

KDO-MCP 审查第三轮核查穿透 6 个问题到根因（含代码行），本任务修复其中 5 项（MCP 工具链层），1 项（graph score 全 0.00 = chunks_vdb 无向量）属 KDO 核心引擎层，超出本任务范围，另议。

## 修复清单（全部已落地 + 实测验证）

| # | 问题 | 根因 | 修复 | 验证 |
|---|------|------|------|------|
| 1 | search title 双坏 | BM25 snippet 无换行符（search_index.py:220 `replace("\n"," ")`），`_extract_title` 的 `split("\n")` 失效；文件带 BOM 使 `_parse_frontmatter` 失配 | `utf-8-sig` 读取 + CRLF 归一化 + frontmatter `title` 优先；snippet 改从正文取（跳 frontmatter） | 实测 5 条 title 全部正确中文 |
| 2 | score_label 全 low | 阈值 70/40 是 RRF 量纲，BM25-only 分 5-30、graph 分 0.0 | max 归一化百分位后按 70/40 标签 | 实测 high/low 区分（0.433→high，0.149→low） |
| 3 | engine 退化为 BM25（graph 静默失败） | LightRAG `query_data` 在 running loop 内 `run_until_complete` 崩（`RuntimeError: This event loop is already running`），delivery.py:81 `except Exception: return None` 吞错 | ① delivery.py 检测 running loop → 独立线程执行（实测 to_thread 方案可行）② except 打 stderr 失败可见 | 循环内实测 engine=hybrid RRF（5 结果）；CLI 同步路径不受影响（n=5 不变） |
| 4 | capabilities specs 重复 | `agent-spec-*.md` 在 tools/ 和 agent-specs/ 双目录都扫，无去重 | 按 `f.stem` 去重 | 实测 11 条 dupes=0 |
| 5 | workflow title "---" | CRLF 文件 `split("\n")[0]` 拿到 `---\r` | 跳 frontmatter 找 `title:` 行 + `rstrip("\r")`，无则第一个 `# ` 行 | 实测 title=="---" 0 条 |

## 改动文件

- `kdo/commands/delivery.py`（KDO 源码）：`_try_graph_query` 循环内线程隔离 + except 打 stderr
- `kdo-tools/mcp/tools.py`（wiki）：5 项修复 + snippet 取正文
  - ⚠️ 该文件工作区含 #352-#356 历史累积未提交改动（_onboard_cache 进程级缓存等），与本次修复同属 MCP 工具链连续改进，一并 commit（commit message 已注明范围）

## 未修项（另议）

- **graph score 全 0.00**：`WARNING: no vectors retrieved from chunks_vdb`——graph_index 重建时 embedding 未写入向量库，LightRAG 兜底 WEIGHT 方法。属 KDO 核心引擎层（index 重建/embedding 管线），需单独立项。

## 验证记录

- 模拟 MCP 上下文（running loop 内调用 search/capabilities，Python 3.12 + PYTHONPATH 清空，与 run_kdo_mcp.cmd 一致）：5 项全过
- CLI 同步路径回归：`_try_graph_query` n=5、`_try_bm25_query` n=5（线程分支仅 running loop 触发）
