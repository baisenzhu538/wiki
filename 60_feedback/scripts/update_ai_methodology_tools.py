#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update ai-methodology-tools.md with second-round assertion verification results.
"""

from pathlib import Path
import re

CARD_PATH = Path("C:/Users/Administrator/Desktop/wiki/30_wiki/frameworks/ai-methodology-tools.md")

# Read original content
content = CARD_PATH.read_text(encoding="utf-8")

# 1. Update the pending assertions table: mark 300% as unsupported, remove Muse row
old_pending_table = """| 断言 | 来源文件 | 状态 |
|------|---------|------|
| 效率提升 300% | `src_20260614_144d986e-多人-Open-Cloud培训.md` | ⚠️ 未找到原文直接支持（主题摘要提及，来源口述） |
| 4288010 Muse 模型与部分案例细节 | `src_20260614_4b226b4f-一堂-AI方法论探索.md` | ⏳ 已定位 211,336,356,365，待细化到具体案例 |"""

new_pending_table = """| 断言 | 来源文件 | 状态 |
|------|---------|------|
| 效率提升 300% | `src_20260614_144d986e-多人-Open-Cloud培训.md` | ❌ 无原文支持（可能来自 theme summary 加工） |"""

assert old_pending_table in content, "Pending table not found in card"
content = content.replace(old_pending_table, new_pending_table)

# 2. Add Muse assertion to verified table
old_verified_end = """| 200 美元替代 2 万美元人工 | `src_20260614_144d986e-多人-Open-Cloud培训.md` | 181-184 | ✅ 已核对 |

### 仍待精确行号或原文支持的断言"""

new_verified_end = """| 200 美元替代 2 万美元人工 | `src_20260614_144d986e-多人-Open-Cloud培训.md` | 181-184 | ✅ 已核对 |
| 4288010 Muse 模型：四层框架、公司及个人知识库整理、知识体系构建 | `src_20260614_4b226b4f-一堂-AI方法论探索.md` | 204-228（Muse 模型四层及公司/个人知识库应用）, 336（人生点→能力项→Muse 模型→IPO 循环→知识树）, 356（建议用 Muse 模型作为个人知识体系）, 365（Muse 模型与双三角模型为两大核心模型） | ✅ 已核对 |

### 仍待精确行号或原文支持的断言"""

assert old_verified_end in content, "Verified table end not found"
content = content.replace(old_verified_end, new_verified_end)

# 3. Append second-round deep-dive section before the final separator
old_footer = """### 置信度更新

- 原综合可信度：0.56（🟡 中可信度，偏向中低）
- 更新后：核心方法论（五步流程、双三角模型、Feature 思维）已在原文中找到明确对应；关键数字（90%、73.2%、40%→80%、200 美元替代 2 万美元）已核对原文位置。
- 但所有数字仍为项目方/主讲人口述，未经过独立审计，样本量、测量方法、统计口径待复核。
- 因此将 confidence 从默认值调整为 `0.65`，标注 `trust_level: medium`，不过度提升。"""

new_footer = old_footer + """

### 第二轮深挖结果（2026-06-14）

本轮由王语嫣（Kimi Code CLI 子代理）针对本卡片第二批复合卡中仍待处理的 2 条断言进行深挖：

| 断言 | 来源文件 | 原文行号 | 处理结果 |
|------|---------|---------|----------|
| 效率提升 300% | `src_20260614_144d986e-多人-Open-Cloud培训.md` | 无 | ❌ 无原文支持（可能来自 theme summary 加工） |
| 4288010 Muse 模型与部分案例细节 | `src_20260614_4b226b4f-一堂-AI方法论探索.md` | 204-228, 336, 356, 365 | ✅ 已核对 |

**详细说明：**

1. **效率提升 300%**
   - 在原始 source 文件 `src_20260614_144d986e-多人-Open-Cloud培训.md` 中全文搜索「300%」「三百」「3百」「300」「效率提升」等关键词，均未找到直接对应表述。
   - 来源文件第 181-184 行仅提及「200 美元替代 2 万美元」的成本对比，未出现「效率提升 300%」的具体说法。
   - 该表述出现在主题摘要 `theme-ai-methodology-tools-summary.md` 的「个人效率提升案例」小节（"成本降低 99%，效率提升 300%"），属于主题摘要层面的加工整合，无法追溯到录音原文的直接支持。
   - **处理结论**：从卡片中移除或改写为「主题摘要加工表述，未获原文直接支持」；如保留，需明确标注为未验证的摘要推断。

2. **4288010 Muse 模型与部分案例细节**
   - 原文中「Muse 模型」因 ASR 转写存在多种形式：music 模型（211）、miles 模型（212）、MUS 模型（228）、muse 模型（336、356、365）。结合上下文，可确认均指同一「Muse 模型」。
   - 第 204-228 行：主讲人提出 Muse 模型是一个四层框架，并用其整理一堂公司 AI 知识库及个人私有知识库，形成公司和个人两棵知识树。
   - 第 336 行：描述 Muse 模型在个人工作流中的位置——「从最上层的人生点到必备能力里面的能力项，然后再到我的 muse 模型，再到我个人的 IPO 的循环，再到我的知识树」。
   - 第 356 行：建议听众「拿 muse 模型当做你们个人的知识体系」。
   - 第 365 行：明确将「muse 模型」与「双三角模型」并列为本课反复出现的两个核心模型。
   - 关于案例细节：Muse 模型对应的具体案例主要为「公司 AI 知识库整理」和「个人知识库整理」，以及后续基于该知识树展开的 web coding、agent、数据等目录归类。卡片中仅概括性提及「Muse 模型」，未深入具体数字或效果数据，因此可认为已核对。
   - **处理结论**：已核对，补充精确行号；案例中未出现需要额外复核的量化断言。

**本轮发现的新问题：**
- 主题摘要 `theme-ai-methodology-tools-summary.md` 对 Open Cloud 培训案例的概括存在夸大/加工风险（如「效率提升 300%」），建议后续对主题摘要中的数字类断言逐条回查原文。
- 录音 ASR 对「Muse」的转写不一致，后续引用时建议在行号后补充说明同词异写现象，避免检索遗漏。
"""

assert old_footer in content, "Footer section not found"
content = content.replace(old_footer, new_footer)

# Update frontmatter timestamps
content = re.sub(r"updated_at: '[^']+'", "updated_at: '2026-06-14T15:32:09+00:00'", content)

# Write back
CARD_PATH.write_text(content, encoding="utf-8")
print(f"Updated {CARD_PATH}")
