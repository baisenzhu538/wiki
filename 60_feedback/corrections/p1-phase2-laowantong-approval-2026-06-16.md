# 第二阶段 P1 精修 — 老顽童 B4-B6 验收批准

## 批准时间

2026-06-16

## 批准人

用户授权王语嫣按建议拍板。

## 待确认事项与决议

### 1. 241 张 `source_unknown` 卡

**决议**：保持 `source_unknown`，不再继续人工认领。

**理由**：
- 这些卡多为 legacy 卡、OCR 卡或早期导入卡，原始来源已不可考；
- 强行推断 source 容易引入错误溯源；
- `source_unknown` 是明确的元数据状态，不影响 P0/P1 基线。

### 2. 37 张保留 high trust 的长文档单 source 卡

**决议**：可接受。

**理由**：
- 37 张卡的单一 source 均为长文档（如 Truman 口述稿 `src_20260614_8269ccdb`，>30KB）；
- 老顽童已在 `source_context` 中加注释说明；
- 长文档内容充分，足以支撑 high trust 判定。

### 3. 74 张 status 降级为 draft 的卡

**决议**：符合流程预期。

**理由**：
- 这些卡原 status 为 enriched/reviewed/stable；
- 因自审问题（author == reviewed_by）改为 `reviewed_by: pending`；
- 在第三方 reviewer 完成审查前，status 保持 `draft` 是合理流程，避免 P0 阻塞。

## 后续行动

- 老顽童 B4-B6 任务验收通过。
- 等待黄药师完成 B1-B3（dangling 链接、tags 格式、domain 复核）。
- 37 张 high trust 单 source 卡纳入正常维护，后续如有更精确 source 可补充。
