---
id: 352
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-18T01:27:06.593513+00:00'
title: MCP 文档债清理（kdo_graph 幽灵引用 + help_guide 裁决 + SSE deprecated）
priority: P2
dependency:
- 350
reviewed_by: 欧阳锋
review_date: '2026-08-18'
grade: A
---

# #352 MCP 文档债清理

## 任务目标

清理小昭 MCP 审查（WorkBuddy 外部调用者视角，2026-08-18）发现的 P0 文档债三项——不影响功能正确性，但污染调用方认知。

## 素材/证据

- 小昭审查：`C:\Users\Administrator\WorkBuddy\2026-08-14-15-10-20\KDO-MCP-审查与改进建议.md` §二 P0-1/2/3
- 王语嫣实测验证（2026-08-18）：
  - `tools.py` **8 处** docstring 引用不存在的 `kdo_graph`（L42/L52-53/L83/L311/L357/L411/L428-429/L436）——只有 `_try_graph_query` 内部函数，从未实现为工具
  - `help_guide()`（tools.py:405 起）定义了完整首连引导，但 server.py 从未注册——死代码
  - `server.py` L6/L147 的 `--sse` 选项 + config.yaml sse 块基于已废弃传输（MCP 2025-06-18 规范：SSE → Streamable HTTP）；当前无远程客户端在用 SSE（WorkBuddy/Claude Code/Hermes 均 stdio）

## 精度修正（codex #337 复审 2026-08-18，采纳）

- kdo_graph 幽灵引用真实分布：**4 函数 / 9 行**（search L42/52-53/83、read_card L311、capabilities L357、help_guide L411/428-429/436）——onboard 不引用（小昭原判 onboard L187-188 有误）

## 修改范围

1. **kdo_graph 幽灵引用**：8 处 docstring 改为引用真实工具（`kdo_onboard` 是最接近的替代）或删去——不改功能，只改文档文本
2. **help_guide 裁决**：注册为 `kdo_help` 工具（推荐，首连引导有价值）或删除——裁决后落地
3. **SSE deprecated**：`--sse` 选项与 config sse 块标注 deprecated + 注释指引 Streamable HTTP 迁移（不实现迁移，只标注）

## 边界

- **不动 #350 已交付代码**（pending_review 冻结）
- 须在 **#351 重启前交付**（用户拍板 2026-08-18：与 #351 gateway 重启合并一次生效）
- 不实现 Streamable HTTP（P3 架构另议）

## 验收标准

1. `grep kdo_graph tools.py` → 0 处（或全部指向真实工具）
2. help_guide 有明确裁决结果并落地
3. SSE 标注 deprecated，`--sse --help` 输出含指引
4. 回归：4 工具功能不变（中文 query 抽查 2 例）

## 执行报告（2026-08-18 黄药师）

### 结论
三项 P0 文档债清理完成，验收 4/4 通过。

### 修改
1. **kdo_graph 幽灵引用**：tools.py 9/9 处替换为 `kdo_onboard`（真实工具），`grep kdo_graph` 两文件均 0
2. **help_guide 裁决 → 注册为 kdo_help 工具**：server.py 注册（首连引导有价值），`kdo_help()` 返回完整引导（what_is_kdo/how_to_search/common_patterns/score_guide）
3. **SSE deprecated**：`--sse` help 标注 DEPRECATED（MCP 2025-06-18 规范 SSE→Streamable HTTP，P3 另议）+ config.yaml sse 块注释

### 验收证据
- kdo_graph 残留：tools.py 0 / server.py 0 ✅
- kdo_help 注册：5 处引用 ✅
- SSE deprecated：server.py + config.yaml ✅
- 功能回归：中文 query（偶遇采集 10s 首次/科学决策 0s 缓存）命中 2/2；help_guide 可调用 ✅
- 编译：两文件 py_compile 通过 ✅

### 边界遵守
- 未动 #350 已交付代码（pending_review 冻结）
- 未实现 Streamable HTTP（P3）

*送欧阳锋终审*

## 交付

1. 修改 + 回归证据
2. 送欧阳锋终审
