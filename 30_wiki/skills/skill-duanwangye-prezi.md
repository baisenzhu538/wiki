---
id: skill-duanwangye-prezi
title: 段王爷·Prezi无限画布演示发布 — 空间叙事HTML演示生成
type: skill
status: draft
confidence: 0.85
trust_level: medium
domain:
- publishing
- html
- prezi
- agent-capability
source_refs:
- capability/duanwangye/prezi
author: 段王爷（南帝）
adapted_from: infinite-canvas-prezi (王欢, huanwang.org)
reviewed_by: ~
review_date: ~
created: '2026-07-20'
related:
- "[[skill-duanwangye-feishu-publishing]]"
- "[[skill-duanwangye-kdo-pipeline]]"
---

# 段王爷·Prezi 无限画布演示发布

> **一句话**：将 40_outputs/ 中的内容变成 impress.js 驱动的单文件 HTML 无限画布演示——镜头用缩放、平移、旋转运动讲空间叙事。

## 其他 Agent 何时调用我

| 场景 | 触发条件 | 示例 |
|------|---------|------|
| 空间叙事演示 | 内容有总分/层级/时间线/对比等空间结构 | "把这篇做成Prezi风格的无限画布" |
| 单文件可分享演示 | 需要断网可播、浏览器直接打开的交互演示 | "做个浏览器双击就能看的演示" |
| 创始人手册/BP | 创业故事、产品介绍需要视觉冲击力 | "把BP做成会动的画布" |
| 长文可视化 | 把长文章变成可飞行的空间结构 | "把这篇长文做成会缩放平移的演示" |

## 我的核心能力

| 能力 | 状态 | 说明 |
|------|------|------|
| 画布策划 | ✅ | 内容逻辑→空间结构映射（5种：中心辐射/线性/左右/环形/Z字形） |
| HTML构建 | ✅ | impress.js 2.0.0 + 单文件模板，图片base64内联 |
| 聚簇嵌套 | ✅ | 父子scale比≥3，钻入→穿梭→退回镜头序列 |
| 渐进显现 | ✅ | substep逐条出现，保持讲解节奏 |
| 防晕规则 | ✅ | 旋转≤90°、缩放比≤10、运动交替、间距防穿帮 |
| AI生图配图 | ⚠️ | 依赖外部工具（Codex CLI / ComfyUI），非本skill内置 |
| 机械闸门 | ⚠️ | prezi_gate.py 待从原skill迁移 |
| 独立终审 | ✅ | delegate_task 起独立子Agent七维审查 |

## 调用姿势

```
用户 → 段王爷：把这个做成Prezi
段王爷 → skill_view(duanwangye-prezi)
       → Step 1: 通读素材→拆场景→规划坐标→落盘 plan.json
       → Step 2: 按plan配图→降级获取→落盘 media_manifest.json
       → Step 3: 用模板渲染HTML→过闸→截图→独立终审→交付 output.html
```

## 核心设计原则

1. **空间即逻辑**：画布的空间关系 = 内容的逻辑关系。看全景图能读出结构=成功，均匀路径线=失败
2. **真嵌套**：子场景以显著更小的 scale 嵌在父场景的几何包围盒内，有完整的钻入/退回序列
3. **聚簇四原则**：先拆聚簇、簇内紧凑不遮挡、簇间分离承载关系、结构靠空间涌现禁剧透
4. **降级铁律**：按时交付完整演示 > 单个素材的完美。每个素材最多验证2-3个URL

## 已知限制

- 机械闸门脚本（prezi_gate.py）需从原 Claude skill 迁移，当前人工核验
- AI 生图依赖外部管线（Evan-gpt-image / ComfyUI），本 skill 不内置
- impress.js 依赖 CDN（jsDelivr），纯离线需手动内联 JS
- 浏览器兼容：需现代浏览器（Chrome/Firefox/Safari/Edge），不支持 IE
