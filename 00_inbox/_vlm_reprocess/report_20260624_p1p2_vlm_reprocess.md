# P1/P2 VLM 重提取报告（已补全）
生成时间: 2026-06-25T22:00:00+08:00
任务: 对 P1/P2 批次 OCR 卡对应原图，使用 MiniMax-M3 VLM 生成结构化描述。

## 更新说明

2026-06-25 晚，洪七公进一步在 `.kdo_lint_baseline_*` 和 `10_raw/assets/yitang/` 中找回了此前标记为 `unknown` 的 12 张原图（3 张地图 + 9 张微信截图），并全部完成 VLM 结构化描述。

## P1/P2 总体概览（最终）

- 计划处理 OCR 卡: 114 张
- 成功找到原图: 114 张
- 找不到原图: 0 张
- VLM 描述生成成功: 114 张
- VLM 描述生成失败: 0 张

## P1 - 泛产品设计

- 优先级: P1
- 计划处理 OCR 卡: 35 张
- 成功找到原图: 35 张
- 成功生成 VLM 描述: 35 张
- VLM 失败: 0 张
- 找不到原图: 0 张

输出目录: `00_inbox/_vlm_reprocess/泛产品设计/`

## P1 - 个人修炼

- 优先级: P1
- 计划处理 OCR 卡: 15 张
- 成功找到原图: 15 张
- 成功生成 VLM 描述: 15 张
- VLM 失败: 0 张
- 找不到原图: 0 张

输出目录: `00_inbox/_vlm_reprocess/个人修炼/`

## P2 - 其他（最终）

- 优先级: P2
- 计划处理 OCR 卡: 64 张
- 成功找到原图: 64 张
- 成功生成 VLM 描述: 64 张
- VLM 失败: 0 张
- 找不到原图: 0 张

### 补全的 12 张原图来源

| OCR 卡 ID | 原图文件名 | 来源位置 |
|:---|:---|:---|
| ocr-一堂-地图-创业地图_conv | 一堂-地图-创业地图_conv.png | `10_raw/assets/yitang/` |
| ocr-一堂-地图-管理地图_conv | 一堂-地图-管理地图_conv.png | `10_raw/assets/yitang/` |
| ocr-一堂进步大地图_compressed | 一堂进步大地图_compressed.jpg | `10_raw/assets/yitang/` |
| ocr-微信图片_20260507004746_32_32 | 微信图片_20260507004746_32_32.jpg | `.kdo_lint_baseline_21000/10_raw/assets/yitang/` |
| ocr-微信图片_20260507004751_33_32 | 微信图片_20260507004751_33_32.jpg | `.kdo_lint_baseline_21000/10_raw/assets/yitang/` |
| ocr-微信图片_20260507004755_34_32 | 微信图片_20260507004755_34_32.jpg | `.kdo_lint_baseline_21000/10_raw/assets/yitang/` |
| ocr-微信图片_20260507004758_35_32 | 微信图片_20260507004758_35_32.jpg | `.kdo_lint_baseline_21000/10_raw/assets/yitang/` |
| ocr-微信图片_20260507004801_37_32 | 微信图片_20260507004801_37_32.jpg | `.kdo_lint_baseline_21000/10_raw/assets/yitang/` |
| ocr-微信图片_20260507004802_38_32 | 微信图片_20260507004802_38_32.png | `.kdo_lint_baseline_21000/10_raw/assets/yitang/` |
| ocr-微信图片_20260507004804_39_32 | 微信图片_20260507004804_39_32.png | `.kdo_lint_baseline_21000/10_raw/assets/yitang/` |
| ocr-微信图片_20260507004806_40_32 | 微信图片_20260507004806_40_32.png | `.kdo_lint_baseline_21000/10_raw/assets/yitang/` |
| ocr-微信图片_20260507004811_41_32 | 微信图片_20260507004811_41_32.jpg | `.kdo_lint_baseline_21000/10_raw/assets/yitang/` |

输出目录: `00_inbox/_vlm_reprocess/其他/`

## VLM 失败清单

无 VLM 生成失败。

## 全量 184 张最终统计

- 总计 OCR 卡: 184 张
- P0（单元模型 + 科学决策）: 70 张，VLM 成功 70 张
- P1/P2: 114 张，VLM 成功 114 张
- **全库 VLM 描述总数: 184 张**
- **全库找不到原图: 0 张**
- **全库 VLM 失败: 0 张**

## 输出目录

- `00_inbox/_vlm_reprocess/单元模型/`
- `00_inbox/_vlm_reprocess/科学决策/`
- `00_inbox/_vlm_reprocess/泛产品设计/`
- `00_inbox/_vlm_reprocess/个人修炼/`
- `00_inbox/_vlm_reprocess/其他/`
- P0 报告: `report_20260624_p0_vlm_reprocess.md`
- 本报告: `report_20260624_p1p2_vlm_reprocess.md`
