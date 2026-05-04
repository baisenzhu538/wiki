---
title: "CJK enrich 自动化"
assigned_to: "黄药师"
created_by: "欧阳锋"
created_at: "2026-05-04"
status: complete
priority: P1
completed_at: "2026-05-05"
---
# CJK enrich 自动化

中文页面 enrich 自动化方案：LLM endpoint 配置或 extractor 升级，替代当前手动 Agent 三步编译。

## 完成方案

采用 **LLM auto-detect** 路径（非 extractor 升级）：

1. `cmd_enrich()` 自动检测 LLMConfig 是否已配置 — 若 `KDO_LLM_ENDPOINT` + `KDO_LLM_API_KEY` 已设置，自动走 LLM 三步编译（浓缩→质疑→对标），无需手动 `--llm` flag
2. 新增 `--no-llm` flag：即使 LLM 可用也强制走 regex 路径
3. `--llm` flag 保留：显式要求 LLM，未配置时报错

**变更文件**：
- `kdo/commands/curation.py` — cmd_enrich() 自动检测 LLMConfig
- `kdo/cli.py` — 新增 `--no-llm` flag

**用户侧配置**（待用户执行）：
```bash
export KDO_LLM_ENDPOINT="https://your-endpoint/v1/chat/completions"
export KDO_LLM_MODEL="your-model"
export KDO_LLM_API_KEY="your-key"
```
或创建 `~/.kdo/config.yaml` 写入对应字段。
