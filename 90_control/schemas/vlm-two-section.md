# VLM/OCR 卡两段式结构规范（#540）

> 小昭事故根因 1 根治：VLM 臆测与 OCR 原文混在一个 confidence 下被当事实采信。
> 本规范把「哪段能信」变成结构事实——读者（人/Agent）一眼可辨。

## 适用范围

VLM/OCR 提取类卡：frontmatter `author` 含 VLM/OCR（如「洪七公（VLM提取）」），或正文含 VLM 深度解析段。

## 结构要求（两段式）

1. **「OCR 原文」段**：标题 `## OCR 原文`——光学识别原文，可引用（相对可靠层）
2. **「VLM 解析」段**：标题 `## VLM 解析`，**首行必须是警示行**（一字不差）：

   `> ⚠️ 以下为 AI 推断，未经交叉验证，不得作为事实引用`

   解析内容（LLM 推断，含幻觉可能）全部在该段内，不外溢

## frontmatter 置信度拆分

```yaml
ocr_confidence: 0.9            # OCR 原文层置信度（相对可靠）
llm_analysis_confidence: 0.4   # VLM 解析层置信度（推断层）
confidence: 0.4                # 兼容字段=取低者（旧读者不瞎）
```

## lint（kdo pre-submit `_check_vlm_two_section`）

VLM 类卡缺两段式（无警示行）→ WARNING（起步不拦，存量批次治理走王语嫣裁定）。

## 存量批次

扫描清单落 `60_feedback/auto/vlm-two-section/`（json+md）。批量挂警示段只加隔离标记不改内容——批次方案报王语嫣裁定后执行（#540 边界：不逐张审解析内容对错）。
