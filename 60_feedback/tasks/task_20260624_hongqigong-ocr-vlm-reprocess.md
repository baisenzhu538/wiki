---
id: task_20260624_hongqigong-ocr-vlm-reprocess
type: production_task
created_at: 2026-06-24
author: 黄药师
assignee: 洪七公
priority: P0
---

# 洪七公任务：全库 OCR 卡 VLM 结构化重提取

> 184 张 OCR 卡（`30_wiki/raw/ocr/`）仅有 PaddleOCR 文字提取，缺少视觉结构信息（层级/表格/对比/流程）。
> 需要找到对应原图，用 MiniMax-M3 VLM 重新生成结构化描述。

## 背景

PaddleOCR 只提文字，提不出：
- 修炼地图的段位阶梯结构
- ABCD 模型的四象限关系
- TCPR 底层网络协议的节点连接
- 决策深度 L1-L4 的层级对照

这些结构信息在原图里，必须 VLM 才能提取。

## 执行方式

### Step 1: 扫描 OCR 卡目录

OCR 卡全部在 `30_wiki/raw/ocr/` 下（184 张）。每张卡的 frontmatter 含 `source_refs: src_*` 可追溯到原图。

### Step 2: 找原图

每个 `src_*` ID 对应 `10_raw/sources/` 下的文件。优先找 `.png/.jpg/.webp` 图片。找不到原图的跳过，记录到报告。

### Step 3: VLM 重跑

用黄药师已修复的 `describe-images-minimax.py`（支持 json5 + 中文引号清洗 + 字段级兜底）：
```
python 40_outputs/code/scripts/describe-images-minimax.py -i <图片目录> -o <输出目录>
```

### Step 4: 输出

VLM 描述文件输出到 `00_inbox/_vlm_reprocess/<域>/` 下，保持与 OCR 卡的对应关系。

## 优先级

| 优先级 | 域 | 数量 | 理由 |
|:--|:--|:--|:--|
| **P0** | 单元模型 | 36 | 当前单元模型域建设急需，高密度框架图 |
| **P0** | 科学决策 | 28+ | 决策域素材，大量 ROI 画布和决策深度对比图 |
| **P1** | 泛产品设计 | 20+ | 产品内核相关 |
| **P1** | 个人修炼 | 15+ | 个人成长相关 |
| **P2** | 其他（地图/微信图片/萃取等） | 剩余 | 低优先级 |

## 与王语嫣协作

洪七公 VLM 输出 → 王语嫣标注哪些含独立框架价值 → 老顽童编译成成品卡。

## 注意事项

- 使用黄药师修复后的脚本，parse error 应归零
- 找不到原图的 OCR 卡记录到报告，不阻塞整体进度
- P0 两个域优先，完成后立即通知王语嫣
- 与本任务并行：王语嫣 + 老顽童继续精益创业收尾和跨域桥接

---

*黄药师 · 2026-06-24*
