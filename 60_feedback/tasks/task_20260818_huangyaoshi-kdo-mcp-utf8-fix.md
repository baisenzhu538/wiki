---
id: 350
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-17T18:42:08.308714+00:00'
title: kdo MCP server.py UTF-8 修复（中文检索乱码根治，全厂 MCP）
priority: P1
dependency: []
reviewed_by: 欧阳锋
review_date: '2026-08-18'
grade: A-
---

## 执行报告（2026-08-18 黄药师）

### 结论
kdo MCP server.py UTF-8 乱码修复完成：stdin/stderr reconfigure utf-8（#323 同款），**stdout 不动**（MCP 传输通道，FastMCP 管理缓冲，reconfigure 会破坏响应 flush——实测踩坑）。

### 修改范围（3 个文件）
1. `kdo-tools/mcp/server.py` — stdin/stderr reconfigure utf-8（stdout 明确不动）
2. `kdo-tools/mcp/feishu_doc_server.py` — 同款修复
3. `kdo-tools/mcp/openmontage_compact_server.py` — 同款修复（全库扫描同类入口，均补齐）

### 回归证据
1. **输入侧（乱码根因）**：server stderr 日志 `kdo_search: query='偶遇'` 无乱码（修复前实证 `query='���ָ�...'`，diag §三）✅
2. **检索层**：直接调 tools.search 中文 6 例（偶遇自动采集/视频号逐字稿/科学决策/知识库检索/Y模型）+ 英文 1 例——全部命中、无乱码；首次 10s（索引加载），同进程缓存后 0s ✅
3. **协议层**：Windows 上 Python 客户端（FastMCP/anyio 管道）连接 Python server 卡死——非修复引入（连接阶段即卡，与 server 代码无关）；生产客户端是 Hermes（Go），#325 已实测 kdo_search HIT；**协议级验证归 #351 gateway 重启后执行**
4. **编译**：3 文件 py_compile 通过

### 注意（friction-log 已记）
- **不能动 sys.stdout**——MCP 传输通道由 FastMCP 管理缓冲，reconfigure 导致响应无法 flush（第一次修复加了 stdout 后协议完全卡死，移除后恢复连接）
- Windows Python 客户端测 MCP server 不可靠——协议验证走 Hermes（Go 客户端）

### 待办
- #351 消费层验证：gateway 重启后 kdo_search 中文 HIT（依赖本修复）

*送欧阳锋终审*

# #350 kdo MCP server.py UTF-8 修复

## 任务目标

修复 `kdo-tools/mcp/server.py` 中文查询乱码——Windows 中文环境下 stdio 管道默认 cp936 解码 UTF-8 JSON，导致 kdo_search 中文 query 乱码、检索结果差（实测 08-16 19:10 段王爷唯一一次调用乱码，随后弃用 MCP）。

## 素材/证据

- 诊断：`60_feedback/diagnosis/diag_20260818_duanwangye-mcp-retrieval.md`（§三催化原因）
- 先例：#323 GBK 终端崩溃族统一修复（52 脚本 `sys.stdout.reconfigure(utf-8)`，2026-08-15 终审 PASS A-）
- 乱码实证：`AppData\Local\hermes\profiles\duanwangye\logs\mcp-stderr.log` 08-16 19:10 `kdo_search: query='���ָ�...'`

## 修改范围

- `kdo-tools/mcp/server.py`：入口处统一 `sys.stdin`/`sys.stdout`/`sys.stderr` reconfigure(encoding='utf-8')（与 #323 同款 6 行块）
- 全库扫描同类 MCP/CLI 管道入口（mcp/ 目录其他 server、research_adapter.py 等）一并检查，同类风险一并修

## 验收标准

1. 中文 kdo_search 调用 5 例（不同中文 query）全部命中、无乱码（stderr 记录可读）
2. 回归：已有英文 query、工具列表、既有用例 0 破坏
3. 修复后全厂 MCP 生效需 gateway 重启——**重启由 #351 或单独验证执行，本任务只落代码+本地回归**（不擅动运行中 gateway）

## 边界

- 不改检索逻辑、不改索引、不动模板（模板收口归 #351）
- 本任务是 #351 的前置（#351 的消费层验证依赖乱码修复）

## 交付

1. 代码修复 + 回归证据（脚本输出）
2. 更新 `20_memory/corrections.md` 或 friction-log 一行（GBK 家族补漏）
3. 送欧阳锋终审
