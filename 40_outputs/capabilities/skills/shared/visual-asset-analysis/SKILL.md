---
name: visual-asset-analysis
description: "Unified visual asset analysis pipeline. Routes images through OCR (text extraction), VLM (semantic understanding), and VA四维法 (structural design analysis). Use when any agent needs to analyze images, screenshots, diagrams, or infographics — '分析这张图', '跑视觉分析', 'VA this image'. Routes through 洪七公."
version: 1.0.0
author: 洪七公
status: enriched
reviewed_by: 待审
updated_at: 2026-07-21
metadata:
  hermes:
    tags: [visual-analysis, ocr, vlm, multimodal, va, image]
    related_skills:
      - beikai-multimodal-pipeline
      - vlm-image-describe-pipeline
      - image-ocr
      - deep-image-parser
    caller: [huangyaoshi, laowantong, wangyuyan, ouyangfeng]
---

# 视觉资产统一分析管线

> 图片 → OCR(文字) + VLM(语义) + VA(结构) → 三合一结构化描述。洪七公的对外调用入口。

## 触发条件

| 场景 | 触发词 | 示例 |
|------|--------|------|
| 新素材图片分析 | "分析这张图""这批图跑一下 VA" | "把 00_inbox 里的图全分析一遍" |
| 卡片 VA 节补齐 | "给这张卡补 VA""check VA completeness" | "检查 C 域所有卡的 VA 是否达标" |
| 竞品/参考截图分析 | "拆解这个页面""分析竞品截图" | "把这个落地页的四维分析跑一下" |
| 批量素材预处理 | "素材预处理""inbox scan" | "新素材到了，跑完整图片管线" |

## 三引擎管线

```
输入图片
    │
    ├── 引擎 1: OCR（文字提取）
    │   ├── PaddleOCR v5（主力，本地）
    │   ├── EasyOCR（备选）
    │   └── Deep Image Parser（表格/公式/密集文字专用）
    │   产出: _paddle_ocr.txt
    │
    ├── 引擎 2: VLM（语义理解）
    │   ├── MiniMax M3（主力，4层JSON容错）
    │   └── SiliconFlow Qwen-VL（备选，便宜快速）
    │   产出: _vlm_desc.md（类型/结构/风格/用途）
    │
    └── 引擎 3: VA 四维法（结构分析）
        空间层级 + 分组逻辑 + 阅读路径 + 视觉强调
        产出: ## Visual Analysis 节（≥100字/图）
```

## VA 四维法标准

对每张图执行，缺一不可：

| 维度 | 分析内容 | 示例写法 |
|------|---------|---------|
| **空间层级** | 标题→模块→子项 | "三层嵌套：顶部标题栏→中部四个并列模块→底部注释区" |
| **分组逻辑** | 边框/留白/线框的语义 | "左侧三个模块按功能分组（输入/处理/输出），通过虚线框+小标题区分" |
| **阅读路径** | F型/Z型/中心放射 | "F型路径：左上标题→左列导航→右列主内容区→底部CTA" |
| **视觉强调** | 字号/位置/密度/形状 | "最大字号在顶部标题（2x正文），右上角CTA按钮密度最高" |

**质量门禁**：
- [ ] 四维全覆盖（不跳维度）
- [ ] ≥100字/图（纯分析文字）
- [ ] 零颜色违规（不用颜色做唯一区分）
- [ ] 逻辑形态匹配（描述的结构和实际图一致）
- [ ] 原图优先（先看图片，后对照文字）

## 调用流程

```
其他 Agent → 洪七公：把这批图跑VA
洪七公:
  1. 扫描图片目录，列出清单
  2. 逐图执行三引擎（OCR → VLM → VA）
  3. 产出写入对应位置（OCR文本 + VLM描述 + VA节）
  4. 质量自检（四维门禁）
  5. 返回处理摘要
```

## 产出规范

| 产出 | 路径 | 格式 |
|------|------|------|
| OCR文本 | 源图同目录 | `源文件名_paddle_ocr.txt` |
| VLM描述 | 源图同目录 | `源文件名_vlm_desc.md` |
| VA分析 | 对应卡片的 `## Visual Analysis` 节 | 四维法模板 |

## When NOT to Use

| 场景 | 原因 | 替代 |
|------|------|------|
| 纯文字文档（无图） | 本 skill 只处理图片 | content-production |
| 图片是装饰性的（icon/banner） | VA ROI 为负 | 跳过 |
| 已有 VA 且质量达标（≥100字+四维全+零颜色违规） | 不需要重复分析 | 跳过 |
| 图片嵌在 PDF/PPT 中 | 需先提取为独立图片 | document-parsing-toolkit |

## 参考

- `framework-visual-analysis-four-dimensions` — VA 四维法方法论框架
- `agent-spec-hongqigong-multimodal` — 洪七公完整武器库与决策树
- `beikai-multimodal-pipeline` — 多模态渲染总纲
- `vlm-image-describe-pipeline` — VLM 双引擎识图详情
- `task-20260528-hongqigong-unit-model-va-and-articles.md` — 单元模型域 VA 审查记录（欧阳锋 A-）
