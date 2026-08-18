---
id: 355
assignee: huangyaoshi
status: queued
updated_at: 2026-08-18
title: "kdo MCP 冷加载死循环止血（P0）——预热 + 超时/keepalive 核查"
priority: P0
dependency: [353]
---

# #355 kdo MCP 冷加载死循环止血（P0）

## 执行状态（2026-08-18 核实：已实质交付）

- **#355 三项范围已由 #351 执行中交付**（黄药师执行报告）：keepalive 超时根因（FastMCP 事件循环被同步 search 阻塞）→ 启动主线程同步 warmup 预热 10s + 工具同步执行（LightRAG worker 依赖主线程 get_event_loop）；旧 NSSM 进程残留杀净
- 实证：段王爷 738.4s/11calls → 8.6s/1call；warmup 后 0s 缓存
- **处置：本任务并入 #351 交付，验收随 #351 欧阳锋终审覆盖**；跨进程共享架构归 #356

## 任务目标

打破"冷加载 538MB 索引 → 300s 超时 → keepalive 失败 → gateway 重启 MCP → 缓存清零 → 再冷加载"死循环。**本任务是 #351（段王爷检索启用）的前置**——不先止血，启用检索即死循环。

## 证据链（codex 只读观察，2026-08-18）

段王爷 02:37-02:49 实录（`AppData\Local\hermes\profiles\duanwangye\logs\`）：
1. 02:37:10 kdo MCP server 启动，收到 `kdo_search: query='偶遇采集...'`（mcp-stderr.log）
2. 02:40:41 keepalive 失败 TimeoutError，connected → degraded，触发重连（agent.log/errors.log）
3. 02:40:43 kdo MCP server 被重启（mcp-stderr.log）
4. 02:43:24 gateway 再次重启，同款 query 再发（gateway.log/mcp-stderr.log）
5. 02:49:18 `kdo_search 300.02s 超时：MCP call timed out after 300.0s`（errors.log）
6. 02:49:32 又拉起新 MCP server 进程（PID 3460）

根因三层：
1. tools.search() 首次调用加载 `wiki\.kdo\search_index.json`（563,808,414 字节 ≈ 538MB 整读整解析）+ LightRAG 图/向量库（graph_index 07-04 陈旧）→ 08-16 实测 178s，现 >300s
2. 进程级缓存（_INDEX_CACHE）被重启循环清零——每次重试都重读 538MB
3. 放大：11 个 server.py 进程并存（各 profile 各挂一个），每进程首次检索独立读同一 538MB 文件，磁盘/内存多路争抢

同族建档：O-15（检索引擎缓存）/O-16（300s 超时复发，R 型 Partner 08-16 死循环）/O-17；friction-log 已上浮（codex 2026-08-18）

## 修改范围（止血最小集）

1. **启动预热**：MCP server 启动时即触发 search_index 加载（get_shared_index），避免"首次调用才冷加载"撞上 keepalive 窗口——预热时机/异步方式由黄药师设计（考虑 gateway 启动时序）
2. **超时/keepalive 参数核查**：MCP call timeout（300s）与 keepalive 窗口（02:37→02:40 仅 3.5 分钟即失败）的匹配——加载 178s 在 keepalive 边缘，确认参数并调整到安全余量
3. **防重启清零（最小版）**：加载完成后进程不被 keepalive/超时误杀——验证预热后 keepalive 正常

## 边界

- 不改检索逻辑、不动索引格式（治本归 #356）
- 不实现跨进程共享（治本归 #356）
- 须在 **#351 重启前交付**（合并一次生效）

## 验收标准（消费层）

1. 任一 profile 连续 2 次中文检索：无 300s 超时、无 gateway/MCP 重启（对照段王爷 02:37-02:49 实录）
2. 首次调用耗时记录（预热后应显著 <178s；实际值黄药师实测留档）
3. keepalive 连续正常（≥10 分钟观察）

## 交付

1. 修改 + 验收证据（含预热前后耗时对照）
2. 送欧阳锋终审
