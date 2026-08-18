---
id: dk-mcp-pythonpath-pollution
title: PYTHONPATH 跨版本污染：cp313 venv 注入 Python312 子进程导致 MCP 崩溃
type: dk
status: draft
reviewed_by: 待审（欧阳锋）
confidence: 0.9
trust_level: medium
language: zh-CN
created_at: 2026-08-16
updated_at: 2026-08-16
domain:
- hermes
- mcp
- infrastructure
aliases:
- KDO MCP 断连
- pydantic_core 加载失败
- PYTHONPATH 污染
- MCP Connection closed
- 跨版本 venv 注入
source_person: 段王爷（南帝）实战
source_context: 2026-08-16 Windows 侧迁移后 KDO MCP 调用报 Connection closed，诊断定位为 PYTHONPATH
  环境污染
source_refs:
- capability/hermes/hermes-mcp-server-ops
related:
- '[[framework-kdo-mcp-server]]'
- '[[tool-mcp-reachability-check]]'
- '[[skill-feishu-doc-l3-extraction]]'
- '[[case-feishu-live259-l3-extraction]]'
tags:
- method:debugging
- scene:infrastructure
- audience:executor
- source-person:agent
- evidence:observed
discoverable_by:
- MCP 调用失败
- Connection closed
- pydantic_core 模块缺失
- 迁移后 MCP 不可用
- 多 Python 版本环境
---

# PYTHONPATH 跨版本污染：MCP server 崩溃的隐蔽根因

> 一句话：Hermes 会话会把 hermes-agent 的 **cp313 venv** 路径注入 PYTHONPATH，KDO MCP server 若用 **Python312** 启动，就会加载 cp313 编译的 `pydantic_core` 二进制直接崩溃——server.py 代码没变，是**环境变量污染**杀死了它。

## 症状

| 现象 | 细节 |
|:--|:--|
| MCP 工具调用 | `MCPError: Connection closed` 或 `AttributeError: 'CallToolResult' object has no attribute 'isError'` |
| 直接跑 server.py | `No module named 'pydantic_core._pydantic_core'` |
| 但 pip show | pydantic 2.13.4 / pydantic_core 2.46.4 都在（在**另一个** venv 里） |

## 根因链

```
Hermes 会话导出 PYTHONPATH = C:\...\hermes-agent;C:\...\hermes-agent\venv\Lib\site-packages
    ↓ MCP server 子进程继承
Python312 启动 server.py → sys.path 含 cp313 venv 的 site-packages
    ↓ import pydantic
pydantic 加载成功（纯 Python）→ pydantic_core 加载失败（二进制 _pydantic_core.cp313-win_amd64.pyd 是 cp313 编译，Python312 跑不了）
    ↓
MCP stdio 通道崩溃 → 客户端报 Connection closed
```

**关键判据**：`python.exe -c "import sys; print(sys.path)"` 看到 `hermes-agent\venv\Lib\site-packages` 混在 Python312 的路径里 = 污染确认。

## 修复（三件套，缺一不可）

### 1. 启动包装脚本（治本）

`wiki/kdo-tools/mcp/run_kdo_mcp.cmd`：
```bat
@echo off
set PYTHONPATH=
"C:\Program Files\Python312\python.exe" "C:\Users\Administrator\Desktop\wiki\kdo-tools\mcp\server.py" %*
```

### 2. 重配 MCP server（走 CLI，不走 patch）

```bash
hermes mcp remove kdo
echo Y | hermes mcp add kdo --command "C:\...\run_kdo_mcp.cmd" --env WIKI_ROOT="..." KDO_SRC="..." PYTHONPATH= --connect-timeout 30
```

⚠️ **交互陷阱**：`hermes mcp add` 有交互确认（"Enable all 4 tools? [Y/n]"），**必须 `echo Y |` 管道**，否则显示"✓ Connected"但实际没保存 config。

⚠️ **config.yaml 受保护**：Hermes 拒绝 agent 直接 patch config.yaml（"Refusing to write to Hermes config file"），必须走 `hermes mcp` / `hermes config` CLI。

### 3. 重启 gateway 生效（易漏）

CLI `hermes mcp test kdo` 成功 ≠ 当前会话能用。会话内 MCP client 是启动时建的旧连接，需 `hermes gateway restart` 或 `/reload-mcp`。

## 验证

```bash
hermes mcp test kdo   # ✓ Connected (864ms) + Tools discovered: 4
```

## 失败模式

| 失败模式 | 症状 | 修复 |
|:--|:--|:--|
| 只改 command 不改 env | PYTHONPATH 仍注入 | 包装脚本或 env 里显式 `PYTHONPATH: ''` |
| 直接 patch config.yaml | Refusing to write | 走 `hermes mcp add/remove` CLI |
| mcp add 不带 echo Y | 显示连接成功但 config 没保存 | `echo Y | hermes mcp add ...` |
| 修完不重启 gateway | CLI test 通过但会话内仍报错 | 重启 gateway 或 /reload-mcp |

## 通用原则

- **基础设施故障优先查环境层**：server 代码没变却突然崩 → 先查 PYTHONPATH / PATH / 工作目录，再怀疑代码
- **多 Python 版本并存时**：子进程必须隔离，显式清空或固定 PYTHONPATH
- **配置修复 ≠ 运行时生效**：改完配置要区分"CLI 验证 OK"与"当前进程连接刷新"两件事
