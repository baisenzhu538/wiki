---
name: pre-ship-check
description: "Pre-publish gate check for content before shipping to any channel. Checks channel-format match, review status, GEO/SEO readiness, and sensitive content — without modifying the content itself. Use when段王爷 or any agent is about to publish — '发布前检查', 'pre-ship check', 'ready to publish?'. Routes through 段王爷."
version: 1.0.0
author: 黄药师
status: enriched
reviewed_by: 待审
updated_at: 2026-07-21
metadata:
  hermes:
    tags: [publishing, gate, quality, ship, check]
    related_skills:
      - feishu-publish
      - content-production-polish
      - kdo-self-attack
    caller: [duanwangye, huangyaoshi, laowantong, wangyuyan]
---

# 发布前检查门禁

> 不润色、不改写、不编辑——只检查"这个内容现在能发吗？发到这个渠道合适吗？"。发布前最后一道门。

## 触发条件

| 场景 | 触发词 |
|------|--------|
| 段王爷准备发布 | "发布前检查""pre-ship check" |
| 其他 Agent 提交发布 | "这个可以发了吗" |
| 批量发布前 | "这批全检查一遍" |

## 五道门禁

### Gate 1: 审查状态

| 检查项 | 通过条件 | 失败动作 |
|------|---------|---------|
| 欧阳锋终审 | `status: reviewed` + `reviewed_by: 欧阳锋` | 🔴 阻断——退回审查 |
| pre-submit | `kdo pre-submit` 通过 | 🔴 阻断——退回生产者 |
| 等级评定 | 有 `grade: A-` 或以上 | 🟡 警告——B+ 及以下建议不优先发 |

### Gate 2: 渠道匹配

| 检查项 | 通过条件 | 失败动作 |
|------|---------|---------|
| 内容类型 vs 渠道 | 匹配 channel-distribution 矩阵 | 🔴 阻断——建议换渠道或改格式 |
| 格式适配 | 内容已按渠道要求格式化 | 🟡 警告——标注需适配的点 |
| 长度适配 | 不超渠道限制（飞书无限制/小红书1000字/公众号2000字推荐） | 🟡 警告——超长建议拆分 |

### Gate 3: 内容质量

| 检查项 | 通过条件 | 失败动作 |
|------|---------|---------|
| AI味检测 | 无明显AI生成痕迹（排比堆砌/概念太密/说教感/无场景） | 🟡 建议跑 content-production-polish |
| 来源可追溯 | `source_refs` 非空，指向真实素材 | 🔴 阻断——补 source_refs |
| 金句/钩子 | 标题/开头有可传播的一句话 | 🟡 建议优化 |
| CTA | 结尾有下一步动作指引 | 🟡 建议加 CTA |

### Gate 4: GEO/SEO

| 检查项 | 通过条件 | 失败动作 |
|------|---------|---------|
| 标题含关键词 | 标题包含 1-2 个目标搜索词 | 🟡 建议优化 |
| 结构化摘要 | 文章前 100 字可独立作为摘要 | 🟡 建议加摘要 |
| 可引用片段 | 有 1-2 句可独立传播的金句 | 🟡 建议标注 |

### Gate 5: 合规

| 检查项 | 通过条件 | 失败动作 |
|------|---------|---------|
| 敏感词 | 无平台敏感词 | 🔴 阻断——标注需修改的词 |
| 外部链接有效 | 所有外链可访问 | 🟡 警告——死链标注 |
| 图片版权 | 图片有来源标注或许可 | 🟡 建议补来源 |

---

## 输出格式

```
🔴 阻断 (N): 必须修复才能发
🟡 建议 (M): 建议修复但不阻断
🟢 通过 (K): 直接可发

结论: GO / NO-GO / GO-WITH-FIXES
```

## When NOT to Use

| 场景 | 原因 |
|------|------|
| 内容还在草稿阶段 | 先写完再检查——这不是写作辅助 |
| 已经在 content-production-polish 流程中 | polish 有自己的质量标准，不需要双重检查 |
| 紧急发布（用户明确说"不管直接发"） | 尊重用户 override，但记录跳过的门禁 |

## 参考

- `workflows/channel-distribution.md` — 渠道选择矩阵
- `shared/content-production-polish/SKILL.md` — 去AI味润色（本 skill 发现 AI 味后建议调用它）
- `agent-spec-duanwangye-publisher` — 段王爷发布前检查清单
