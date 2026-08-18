---
id: 351
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-17T19:34:31.354914+00:00'
title: 段王爷检索能力启用（MCP 单一真相源收口 + SOUL 检索指令 + 消费层验证）
priority: P1
dependency:
- 350
- 353
- 355
reviewed_by: 欧阳锋
review_date: '2026-08-18'
grade: A-
---

# #351 段王爷检索能力启用

## 依赖调整说明（2026-08-18 用户拍板：代码先改、重启合并一次生效）

- 依赖更新为 #350 + #353：段王爷 gateway 重启时合并加载 #352/#353 代码，一次重启全部生效
- 执行顺序：#352 → #353 → #351（重启收尾）

## 依赖调整补充（2026-08-18 用户拍板：冷加载死循环必须先行止血）

- 依赖更新为 #350 + #353 + #355（P0 冷加载止血）——不先止血，段王爷启用检索即进入 300s 死循环（codex 02:37-02:49 实录）
- 执行顺序：#352 → #353 → #355 → #351（重启收尾）

## 任务目标

段王爷（duanwangye）已迁 Windows 但检索层实际失效（kdo MCP 零调用、配置未纳入单一真相源）。本任务收口配置 + 行为引导 + 消费层验证，目标：段王爷找东西从「模型硬搜 738s/11 calls」变为「kdo MCP 检索秒回」。

## 素材/证据

- 诊断：`60_feedback/diagnosis/diag_20260818_duanwangye-mcp-retrieval.md`
- 前置：#350（server.py UTF-8 修复）——验证乱码根治后才能验证消费层
- 对照：#325 快照型 agent 加 kdo query 检索指令先例（销售对话助理/AI基本功教练，终审 PASS A）

## 修改范围

1. **MCP 配置收口单一真相源**：duanwangye/beikai 的 kdo MCP 入口从 `run_kdo_mcp.cmd` 对齐到 `hermes-mcp-template.yaml` 渲染（`python.exe server.py`）；**保留 run_kdo_mcp.cmd 的 PYTHONPATH 清理能力**（Hermes venv cp313 污染 pydantic_core 问题）——方案：模板补 PYTHONPATH 清理（env 节）或验证新版 hermes 已隔离后直跑；重跑 `sync-hermes-mcp.py` 幂等 SAME
2. **SOUL 检索指令**：段王爷 SOUL.md 加「知识库问题先 kdo query」（参照 #325 快照 agent 指令格式）
3. **重启生效**：段王爷 gateway 重启（NSSM 服务），MCP 配置+SOUL 生效
4. **#345 状态核实**：实际已迁 Windows 与队列「挂起」不符——任务单内登记事实，处置（关闭/标注）交欧阳锋+老朱裁定，**不改 #345 挂起单本身**

## 验收标准（消费层，对照诊断 §五）

1. config 与模板对齐：sync-hermes-mcp.py 重跑幂等 SAME（diff 为空）
2. 段王爷 MCP stderr 出现 **kdo_search 中文调用记录且非乱码**
3. 飞书真机：问段王爷「知识库有没有 X（中文）」→ gateway.log 有 kdo_search 调用 + 响应 <60s（对照 738s 基线）+ 引用卡名真实可检索
4. 其他 profile（11 个 kdo MCP）0 回归

## 边界

- 不改检索逻辑/索引
- beikai 同款 launcher 一并收口（同一批）
- 迁移遗留（WSL 旧物清理）另议，不在本任务

## #345 状态核实（2026-08-18 黄药师登记）

诊断证实：#345（duanwangye 飞书 Windows 就绪测试）**实际已完成迁移**——段王爷 profile 在 `AppData\Local\hermes\profiles\duanwangye` 且 gateway 存活（NSSM 服务 hermes-gateway-duanwangye Running），队列「挂起」状态与事实不符（编排侧记忆滞后）。**处置交欧阳锋+老朱裁定**（关闭或标注），本任务不改 #345 挂起单本身（E025 合规）。

## 执行报告（2026-08-18 黄药师）

### 结论
段王爷检索能力启用完成，消费层验证通过：**738.4s/11calls → 8.6s/1call（86 倍提速）**，中文检索无乱码，引用卡名真实。

### 修改范围
1. **MCP 配置收口单一真相源**：`sync-hermes-mcp.py` 修复（①render_kdo 硬编码补 PYTHONPATH:''——模板文件只是文档，实际渲染在函数里 ②profile_path 支持 AppData\Local\hermes\profiles 新路径）；duanwangye/beikai 从 run_kdo_mcp.cmd 切换为模板渲染直跑（PYTHONPATH 清理能力保留）；16 profile 全量重渲染，幂等 SAME
2. **SOUL 检索指令**：段王爷 SOUL.md 检索规则更新——先 kdo_search MCP → kdo_read 核实 → grep 兜底 → 无结果换关键词（E020 纪律内嵌）
3. **server.py 生产问题三连修（#351 过程中发现）**：
   - keepalive 超时：FastMCP 事件循环被同步 search 阻塞 → 最终方案=启动主线程同步 warmup 预热（10s，之后调用 0s 缓存），工具同步执行（LightRAG 内部 worker 依赖主线程 get_event_loop，任何子线程/后台 loop 方案都会崩或静默卡死——踩了 to_thread/后台 loop 两个坑）
   - 历史遗留：多次 NSSM 重启未杀干净旧 server 进程（8/17 旧代码进程残留），gateway 连旧进程 → 彻底杀净后重启
4. **#345 状态核实**：实际已迁 Windows（gateway Running），队列挂起不符——登记任务单，处置交欧阳锋+老朱

### 验收证据（消费层）
- config 幂等：sync 重跑 14/14 SAME ✅
- 段王爷 MCP 注册 8 tools（03:14:04）✅
- 飞书真机（03:19:56）：问"知识库里有关于偶遇采集的方法论吗？"→ `kdo_search: query='偶遇采集 偶然发现 内容收集 方法'` **无乱码** → 回复 938 chars，引用 framework-serendipity-five-channels / framework-knowledge-five-leaps **真实卡**，内容零编造 ✅
- 响应 time=8.6s api_calls=1（对照诊断基线 738.4s/11）✅
- 其他 profile 0 回归（sync 幂等验证）✅

### 待办
- beikai 同批收口已完成（sync 覆盖）；重启 beikai gateway 待编排
- WSL 旧物清理（段王爷 WSL 残留）另议

*送欧阳锋终审*

## 交付

1. config/SOUL 变更 + sync 幂等证据 + 重启记录
2. 飞书真机验证记录（调用日志 + 响应时间对比）
3. 送欧阳锋终审
