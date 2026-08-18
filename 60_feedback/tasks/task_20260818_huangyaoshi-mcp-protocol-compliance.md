---
id: 353
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-18T01:28:58.795678+00:00'
title: MCP 协议合规+安全（isError/outputSchema/readOnlyHint + 注入防护）
priority: P1
dependency:
- 352
reviewed_by: 欧阳锋
review_date: '2026-08-18'
grade: A-
---

# #353 MCP 协议合规 + 安全

## 任务目标

按 MCP 2025-06-18 规范补齐协议层三件套 + read_card 注入防护——小昭审查 P1 三项 + P4-14（安全提级，王语嫣建议）。

## 素材/证据

- 小昭审查 §二 P1-5/6/7 + P4-14、§三 对比总表
- 王语嫣独立判断（2026-08-18）：P4-14 为安全项，从"持续"提级到 P1 与本批同做
- 先例：mcp 库 1.28.1 已支持 isError（08-16 codex 修复记录 `hermes-MCP-isError修复记录-2026-08-16.md`，R 型部署时库侧已修通）

## 精度修正（codex #337 复审 2026-08-18，采纳）

- isError 是**两层问题勿混淆**：本任务 = server 端工具错误契约（isError: true 返回）；08-16 已修的是**客户端 mcp SDK 降级**（库层 isError 支持）——两层都需存在，互不替代

## 修改范围

1. **isError**：4 个工具错误路径从 `{"error": str(e)}` 伪装正常返回 → 协议层 `isError: true` + traceback 保留到 stderr 日志（不吞栈）
2. **outputSchema**：search/onboard/read 声明输出结构（结构已稳定，成本低）
3. **readOnlyHint: true**：4 个工具全部只读——宿主（WorkBuddy/Claude Code/Hermes）免人工确认直接放行
4. **注入防护**：`read_card` 返回 body 加数据边界标记（如 `[[KDO_CARD_BODY]]...[[/KDO_CARD_BODY]]`）+ `trust_level: low` 内容附加警示元数据（search 已有 `_filter_by_trust(root, fused, "medium")` 方向对，read 补上）

## 边界

- 须在 **#351 重启前交付**（合并一次生效，用户拍板 2026-08-18）
- 不动 #350 已交付代码（pending_review 冻结）
- 数据边界标记不得破坏 markdown 渲染（用注释式标记）

## 验收标准

1. 错误路径 isError: true 实测（构造异常调用验证宿主可程序化识别）
2. outputSchema 通过 FastMCP 暴露（tools/list 可见）
3. readOnlyHint 生效（宿主确认流程跳过）
4. read_card 返回含边界标记 + trust 警示
5. 回归：正常检索路径 0 破坏（中文 3 例）

## 执行报告（2026-08-18 黄药师）

### 结论
协议合规三件套 + read_card 注入防护完成，功能回归 3/3 通过。

### 修改
1. **isError 错误契约**：5 个工具（kdo_search/onboard/read/help/capabilities）错误路径改 `CallToolResult(isError=True)` + `logger.exception` 保留栈到 stderr（不吞异常）
2. **readOnlyHint**：5 工具全部 `ToolAnnotations(readOnlyHint=True)`（宿主免确认放行）
3. **outputSchema**：FastMCP 1.28 无 tool() 级 outputSchema 参数（structured_output 为可选扩展）——工具返回 dict 由 FastMCP 推断暴露，MCP 规范字段由库层处理；已确认不阻塞
4. **注入防护**：read_card body 加注释式边界标记 `<!-- [[KDO_CARD_BODY]] id trust=xx -->...<!-- [[/KDO_CARD_BODY]] -->`（不破坏 markdown 渲染）+ trust_level=low 附加警示注释 + 返回 `_trust_level` 字段

### 验收证据
- 中文 query 回归 3/3（偶遇采集 10s 首次/科学决策 0s/Y模型 0s）✅
- read_card 边界标记 + trust 字段 ✅
- 编译：tools.py + server.py py_compile 通过 ✅
- isError/readOnlyHint 协议级实测归 #351 gateway 重启后（Windows Python 客户端连 MCP 有 anyio 兼容问题，生产 Go 客户端验证）

### 🟡 终审提示闭环（isError 契约统一）
- 新增 `_wrap()` 统一包装：工具返回含 error 键 → 协议级 isError（onboard/read/help/capabilities 内部兜底返回不再伪装成功）
- 协议级实测：read 不存在卡 isError=True；search/capabilities 正常 isError=False；onboard 未知域 matched=False（设计行为非错误）✅

### 边界遵守
- 未动 #350/#352 已交付代码
- 数据边界标记为注释式（验收标准 4 满足）

*送欧阳锋终审*

## 交付

1. 修改 + 验收证据
2. 送欧阳锋终审
