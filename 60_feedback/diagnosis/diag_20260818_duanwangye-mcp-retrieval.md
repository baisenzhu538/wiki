---
id: diag-20260818-duanwangye-mcp-retrieval
title: "段王爷检索能力诊断：kdo MCP 零使用 + GBK 乱码 + 单一真相源脱轨"
type: diagnosis
status: delivered
created_at: 2026-08-18T09:30:00+00:00
updated_at: 2026-08-18T09:30:00+00:00
domain:
  - infrastructure
  - retrieval
tags:
- mcp
- gbk
- duanwangye
- retrieval
source_refs:
- C:\Users\Administrator\AppData\Local\hermes\profiles\duanwangye\logs\mcp-stderr.log
- C:\Users\Administrator\AppData\Local\hermes\profiles\duanwangye\logs\gateway.log
- C:\Users\Administrator\AppData\Local\hermes\profiles\duanwangye\config.yaml
- C:\Users\Administrator\Desktop\wiki\kdo-tools\mcp\server.py
- C:\Users\Administrator\Desktop\wiki\kdo-tools\mcp\run_kdo_mcp.cmd
---

# 段王爷检索能力诊断

**诊断者**：王语嫣 | **日期**：2026-08-18
**任务来源**：老朱提问「为什么段王爷还是用的旧的，速度好慢，找东西」

## 一、结论摘要

段王爷**已迁 Windows 侧且 gateway 存活**（与队列 #345 挂起状态不符——编排侧记忆滞后），但检索层实际失效，三层根因叠加：

1. **kdo MCP 零调用**——段王爷找东西靠模型硬搜，不用检索层（实测 738 秒 / 11 次 API 调用）
2. **唯一一次 MCP 检索中文查询 GBK 乱码**——server.py 缺 UTF-8 处理（#323 GBK 修复族漏网），用过一次结果差即弃用
3. **MCP 配置未纳入 #326 单一真相源**——duanwangye/beikai 用旧手工 launcher（run_kdo_mcp.cmd），其他 9 profile 均为模板渲染直跑

## 二、事实链（证据）

| # | 事实 | 证据 |
|:--|:--|:--|
| 1 | 段王爷 Windows profile 存在且 gateway 存活 | `AppData\Local\hermes\profiles\duanwangye\gateway_state.json`：running pid=6892 feishu=connected updated=2026-08-17T17:10Z |
| 2 | kdo MCP server 已挂 | config.yaml `mcp_servers: [wechat, kdo]`；gateway 子进程 `cmd.exe /c run_kdo_mcp.cmd` |
| 3 | kdo MCP 零调用（08-16 19:26 后仅 Ping 心跳） | `logs/mcp-stderr.log`：无任何 kdo_search 调用记录 |
| 4 | 唯一一次调用中文查询乱码 | 08-16 19:10 `kdo_search: query='���ָ� ��ȡ...'`（GBK 解码 UTF-8 JSON） |
| 5 | 738 秒硬搜 | gateway.log 08-17 02:10:34 `response ready time=738.4s api_calls=11`（视频号逐字稿调研轮） |
| 6 | 用户 08-17 已质疑检索层 | gateway.log 08-17 02:02:36 用户：「知识库不是有MCP还有moc吗？」 |
| 7 | duanwangye/beikai 用 run_kdo_mcp.cmd，其他 9 profile 模板渲染直跑 | 10 个 Windows profile config.yaml mcp_servers.kdo 对比 |
| 8 | server.py 无 stdin/stdout reconfigure utf-8 | grep server.py：无 PYTHONIOENCODING / reconfigure |
| 9 | WSL 侧段王爷 gateway 已死（08-16 19:02 SIGTERM 后无人复活） | WSL gateway.log / gateway-exit-diag.log——迁移后遗留，需清理 |

## 三、根因分析

### 直接原因：检索行为缺失
段王爷 agent 侧无检索习惯——SOUL 无「知识库问题先 kdo query」指令，找东西依赖模型记忆+API 硬搜。738 秒/11 次调用 vs R 型同任务用 kdo MCP 几分钟全链完成，量级差。

### 催化原因：GBK 乱码打击信心
08-16 19:10 唯一一次 kdo_search 调用中文查询乱码（cp936 解码 UTF-8 JSON）→ 检索结果必然差 → 段王爷从此不用 MCP。#323（08-15）GBK 修复族修了 52 个脚本，MCP server.py 漏网。

### 结构原因：单一真相源脱轨
duanwangye/beikai 的 kdo MCP 入口是清 PYTHONPATH 的手工 launcher（run_kdo_mcp.cmd），未纳入 #326 hermes-mcp-template 单一真相源渲染 → 模板后续更新收不到。注意：run_kdo_mcp.cmd 解决的是 Hermes venv PYTHONPATH 污染（cp313 破坏 pydantic_core），收口时需保留此能力（模板需补 PYTHONPATH 清理或验证新版已隔离）。

### 元根因：编排侧记忆滞后
队列 #345（T3 duanwangye 就绪测试）仍挂起「等老顽童 CLI + 用户命令」，但迁移实际已完成。部署事实与编排记录断层（E021 家族：信队列状态不验证运行态；本次反向——验证了进程才纠正队列认知）。

## 四、任务编排（E025：不修改 #345 挂起单，另开新任务）

| 任务 | 标题 | assignee | 优先级 | 依赖 |
|:--|:--|:--|:--|:--|
| #350 | kdo MCP server.py UTF-8 修复（中文检索乱码根治，全厂 MCP） | huangyaoshi | P1 | 无 |
| #351 | 段王爷检索能力启用（MCP 单一真相源收口 + SOUL 检索指令 + 消费层验证） | huangyaoshi | P1 | #350 |

## 五、验证标准

**#350**：中文 kdo_search 调用 5/5 命中、无乱码、回归 0 破坏。

**#351**：
1. config 与模板对齐（sync-hermes-mcp.py 幂等 SAME）
2. SOUL 检索指令落盘
3. 消费层：段王爷 MCP stderr 出现 kdo_search 中文调用记录（非乱码）
4. 飞书真机：问段王爷「知识库有没有 X」→ 有 kdo_search 调用 + 响应 <60s + 引用卡名真实（对照 738s 基线）

## 六、教训（入错误模式库候选）

1. **E029 家族复发**：判定部署位置前先验证「运行进程读哪个文件/目录」——首次查 `C:\Users\Administrator\.hermes\profiles`（旧目录）误判段王爷在 WSL，用户纠正后才查 `AppData\Local\hermes\profiles`（实际运行目录）。验证到消费层（gateway_state.json 实读）后结论即刻修正。
2. **编排记忆 vs 运行事实**：部署状态以 gateway_state.json/进程/日志为准，队列状态仅作参考；发现不一致以事实为准并登记队列待对齐。
3. **GBK 修复族检查清单补漏**：#323 修了 52 个脚本，MCP server（stdio 管道）是同类风险——后续 GBK 类修复需含 MCP/CLI 管道入口扫描项。

## 七、遗留

- #345 任务单状态与事实不符（实际已迁 Windows）——挂起单不动（E025），由欧阳锋/老朱裁定处置（关闭或标注完成）
- WSL 侧 duanwangye 旧物（profile 目录、崩溃日志 45MB）待清理——是否列入迁移链收尾（T4 归档）待裁定
- beikai 与 duanwangye 同款 launcher 问题——#351 一并收口
