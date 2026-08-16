---
title: Skill 盘点 + 渐进披露审计报告（#278）
type: report
status: draft
created_at: 2026-08-09
author: 黄药师
---

# Skill 盘点 + 渐进披露审计报告（#278）

> 范围：40_outputs/capabilities/skills/ 顶级 39 个（shared 69 + .claude 52 由 #267 双轨同步覆盖，此处审计顶级独立 skill）
> 方法：`skill_lifecycle.py list` + 4 维度人工审计（frontmatter 完整性 / SKILL.md 长度 / 触发词 / 长期记忆混入）
> 标杆：task-orchestration（2026-08-09 新建，已合规）

## 一、生命周期盘点（39 个）

| 状态 | 数量 | 处置 |
|:--|:--:|:--|
| published | **31** | 正常（含本次补标 15 个） |
| draft | **13** | 待内容补齐（含本次补标 1 个 lib-maintainer 58w 极薄） |
| unknown | **0** | 本次从 16 → 0 ✅ |
| deprecated | 0 | 无（本批无废弃候选——#279 结晶候选 8 个待审） |

**16 unknown 补标明细**：15 → published（内容完整有触发词：ai-design-assets 等）/ 1 → draft（lib-maintainer 仅 58w 极薄）

## 二、结构合规审计（Anthropic 官方 4 维度）

### P0 违规（3 个——frontmatter 缺失/非标准，Claude Code 无法识别）

| Skill | 违规 | 建议改造 |
|:--|:--|:--|
| ai-image-generation-setup | 无 `---` 包裹 frontmatter（`# 标题` + 裸键值 `skill_name:`/`status: stable`） | 补标准 YAML 头（name/description/status），原内容保留 |
| ai-short-drama-creation | 同上（`# 标题` + 裸键值） | 同上 |
| design-prompt-iteration | 完全无 frontmatter（`# 标题` + `## Purpose`） | 补标准 YAML 头 + 从正文提炼 description |

### P1 建议（3 个——触发词缺失）

| Skill | 问题 | 建议 |
|:--|:--|:--|
| ai-image-prompt-engineering | 无"触发/Trigger/When to"节 | 补触发词节（正文有 829w 内容） |
| audio-production-pipeline | 无触发词节 | 同上（736w） |
| consultant-mode-yai-style | 无触发词节 | 同上（836w） |
| config-cascade-debug | 无触发词节 | 同上（525w） |
| data-curator | 无触发词节 | 同上（1385w） |
| delivery-producer | 无触发词节 | 同上（914w） |
| hermes-gateway-revival | 无触发词节 | 同上（729w） |
| image-ocr | 无触发词节 | 同上（700w） |
| image-ocr-easyocr | 无触发词节 | 同上（375w） |
| image-understanding-pipeline | 无触发词节 | 同上（492w） |
| knowledge-curator | 无触发词节 | 同上（894w） |
| long-image-ocr | 无触发词节 | 同上（314w） |
| system-linter | 无触发词节 | 同上（759w） |

### P2 可选（长度/记忆混入）

- **>1000 词**：ai-image-generation-setup（1351w）、data-curator（1385w）、llm-prompt-iteration（1139w）——超长 skill 建议下沉模板/示例到 references（渐进披露）
- **长期记忆混入**：business-research / deep-image-parser / diagnosis-quality-gate / xiaohongshu-positioning 已有 references/（合规 ✅）；其余 0 个混入
- **触发词碰撞**：未发现（各 skill 触发词唯一）
- **测试残留**：skill_20260505_9c1b487a-req-024-路由测试-skill（145w draft）——历史测试产物，建议废弃或归档

## 三、处置汇总

| 类别 | 数量 | 状态 |
|:--|:--:|:--|
| unknown 补标 | 16 | ✅ 已完成（15 published + 1 draft） |
| P0 结构违规 | 3 | 📋 改造清单已出（**只审计不改造**——边界遵守，待王语嫣/欧阳锋确认后执行） |
| P1 触发词缺失 | 13 | 📋 清单已出（待确认） |
| P2 超长/残留 | 4 | 📋 清单已出（待确认） |

## 四、建议

1. P0 3 个由我执行改造（补标准 frontmatter，30 分钟）——待确认
2. P1 13 个触发词节：内容需理解 skill 用途，建议老顽童/洪七公按归属补（或我按 description 提炼）
3. skill_20260505 测试残留 → deprecated（#273 机制）
4. 与 #267 双轨同步联动：P0 修复后跑 `skill_bridge_sync.py sync` 保持双轨一致

---
*报告：黄药师 2026-08-09 | 待王语嫣/欧阳锋确认*
