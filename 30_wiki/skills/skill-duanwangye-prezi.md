---
id: skill-duanwangye-prezi
updated_at: '2026-08-20'
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
reviewed_by: 待审
review_date: null
created: '2026-07-20'
related:
- '[[skill-duanwangye-feishu-publishing]]'
- '[[skill-duanwangye-kdo-pipeline]]'
- '[[agent-spec-duanwangye-publisher]]'
tags:
  - audience:executor
  - scene:execution
  - skill-level:intermediate
  - 文章
  - 工具
  - 模板
discoverable_by:
- Prezi
- 无限画布
- 空间叙事
- HTML演示
- 段王爷演示
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

---

## 终审记录（#544 批次二 · 2026-08-27 · 欧阳锋）

**结论：退回**——source_refs 唯一条目非仓库路径（P0），两处能力声称失真。

**取证**：source_refs 0/1 有效（`capability/duanwangye/prezi` 磁盘不存在，check-source-refs.py 实证 refs_missing:1）；pre-submit PASS（SOURCE_REACHABILITY 未拦——门禁链缺口，见 lint 盲区建议书追加实证）；声称-来源对照（subagent 取证 + 终审抽核）。

**缺陷**：
- P0：source_refs 唯一条目 `capability/duanwangye/prezi` 非仓库路径。真实出处实存：`10_raw/sources/multimodal-output/王欢：把一个想法，做成一张会移动的无限画布/王欢：把一个想法，做成一张会移动的无限画布.md` + `40_outputs/capabilities/skills/infinite-canvas-prezi/`（adapted_from 所指）。**同主题四张姊妹卡（concept/tool/dk/case，2026-07-21 批次已 PASS A-）均引 10_raw 真路径，本卡是例外**。注意：段王爷系另 4 张 skill 卡（含 2 张已 reviewed）也用同款虚构路径——家族性惯例，已单列建议
- P1：「画布策划（5种：中心辐射/线性/左右/环形/Z字形）」无出处且与源矛盾——源文与已审 concept 卡（concept-spatial-narrative-design.md:61-68）均为**四种**（路径/嵌套/对比/环形）；「Z字形」源文完全不出现；「中心辐射」仅是某案例的结构描述（源文 L287）非分类枚举项
- P1：「独立终审 ✅ delegate_task 起独立子Agent」——delegate_task 在库内无机制定义，且知识状态是**待验证**（diag_20260721_wangyuyan-infinite-canvas-kdo-factory.md:114 原文是疑问句「能否复用 delegate_task？」）；卡标 ✅ 属能力虚标
- P2：卡自称「当前人工核验」比原 skill 红线宽松——infinite-canvas-prezi/SKILL.md:120 要求「闸门脚本未就绪时不得跳过闸门直接交付」
- 证实项（对照留痕）：防晕规则（源文 L161 逐条对应）、聚簇四原则（L115/L119）、impress.js 2.0.0（源文 L377 + manifest.yaml:6）、prezi_gate.py 待迁移（全库无此文件，SKILL.md:120 同口径）、related 3/3 无死链、被 agent-spec-duanwangye-publisher 依赖关系真实

**落点**：段王爷修 source_refs（引 10_raw 真路径 + infinite-canvas-prezi 包）+ 空间结构改四种对齐已审 concept 卡 + delegate_task 降 ⚠️ 注明待验证 + 人工核验口径对齐原 skill 红线后复审。
