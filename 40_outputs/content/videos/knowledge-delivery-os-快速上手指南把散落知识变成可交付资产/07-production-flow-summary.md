# Task 7 视频制作全流程 — 7a~7g 工序详解

**项目:** Knowledge Delivery OS 快速上手指南：把散落知识变成可交付资产
**总帧数:** 40 帧 | **总时长:** ~8.3 分钟 | **分辨率:** 1920×1080
**风格:** Amber/Black Bauhaus，终端美学，结构化留白

---

## 流程总览

```
7a 分镜修订 → 7b Seg1 画面 → 7c Seg2 画面 → 7d Seg3 画面 → 7e Seg4 画面 → 7f Seg5 画面 → 7g 音画对位 → Ship
   (审批)        (审批)          (审批)          (审批)          (审批)          (审批)          (审批)
```

**核心原则:** 每道工序完成 → 书面提报 → 欧阳锋审批 → 才能进入下一阶段

---

## 7a — 分镜修订 (Storyboard v2)

| 项目 | 内容 |
|------|------|
| **入参** | `01-script.md` v2（十指讲香版，2219字，5个Segment） |
| **出参** | `02-storyboard.md` v2（40帧，17680字节） |
| **前置条件** | Gate 0（脚本）已通过审批 |
| **核心工作** | 对比旧分镜v1和新脚本v2，识别delta，修订对齐 |

### 具体修订内容
- **烹饪比喻系统**（新增）：生肉→粥→菜 3帧序列（F26-F28）
- **情绪弧线标注**（新增）：每段标注情绪阶段+色调方案+节奏
- **墓碑意象增强**（增强）：裂纹、褪色文字、青草、时间线标记
- **产品经理故事线**（对齐）：左右分屏对比结构
- **金句画面标记**：5个金句帧明确标注（F9, F11, F17, F22, F34, F38）

### 质量门
```bash
kdo video validate --stage storyboard
# 结果: PASS
```

---

## 7b — Seg 1 画面制作 (Hook)

| 项目 | 内容 |
|------|------|
| **入参** | `02-storyboard.md` v2（F001-F010） |
| **出参** | `frames/segment_1_frame_001.png` ~ `010.png`（10帧） |
| **工具** | Pillow (Python) + 中文字体(wqy-zenhei) + 英文字体(DejaVu Sans Bold) |
| **情绪弧线** | 假象→焦虑→狼狈→共情→希望 |

### 10帧清单

| 帧号 | 类型 | 画面内容 | 情绪 |
|------|------|----------|------|
| F001 | Title Card | KDO logo 居中 + "快速上手指南" | 中性 |
| F002 | Text Reveal | 白色大问号放大→缩小移左上 | 好奇 |
| F003 | Text Reveal | "200+" 琥珀闪烁 + "篇文章" | 假象 |
| F004 | Text Reveal | "50+ 篇笔记" + "10+ 个课程" 三行数据 | 假象 |
| F005 | Text Reveal | 时间对比: 一小时收集 vs 一分钟思考 | 假象 |
| F006 | Text Reveal | "713块" "1200+小时" 数字跳动→变暗 | 焦虑 |
| F007 | Text Reveal | "然后呢？" 闪烁（0.5s→0.2s加速） | 焦虑高峰 |
| F008 | Metaphor | 日历+钟表+收藏夹 快闪场景 | 狼狈 |
| F009 | **金句** | "信息过载不是问题。信息变不成资产才是问题。" | 共情/觉醒 |
| F010 | Logo Reveal | KDO 从噪点中显现 | 希望 |

### 质量门
```bash
kdo video validate --stage frames
# 结果: PASS
```

---

## 7c — Seg 2 画面制作 (误区)

| 项目 | 内容 |
|------|------|
| **入参** | `02-storyboard.md` v2（F011-F017） |
| **出参** | `frames/segment_2_frame_011.png` ~ `017.png`（7帧） |
| **情绪弧线** | 揭露→理解→坚定 |

### 7帧清单

| 帧号 | 类型 | 画面内容 | 情绪 |
|------|------|----------|------|
| F011 | **金句** | "你不是不努力。你是努力停在了错误的地方。" | 揭露 |
| F012 | Text Reveal | "收集+分类" 红线划掉 → "=死胡同" | 警示 |
| F013 | Comparison | 印象笔记/Notion/Obsidian 失败卡片 | 自嘲 |
| F014 | Comparison | 消费行为(红) vs 生产行为(琥珀) + 箭头 | 冲突 |
| F015 | Flow Diagram | 闭环循环图: 输入→加工→交付→反馈→改进 | 理解 |
| F016 | Flow Diagram | KDO 九工序流水线（9圆角方框+箭头） | 信服 |
| F017 | **金句** | "不是做得更多。是做得更清晰。" | 坚定 |

### 质量门
```bash
kdo video validate --stage frames
# 结果: PASS
```

---

## 7d — Seg 3 画面制作 (工厂)

| 项目 | 内容 |
|------|------|
| **入参** | `02-storyboard.md` v2（F018-F031） |
| **出参** | `frames/segment_3_frame_018.png` ~ `031.png`（14帧） |
| **情绪弧线** | 否定→展示→教学→比喻→灵活 |
| **特点** | 跨度最大的一段，含6个Terminal Demo + 3个烹饪比喻 |

### 14帧清单

| 帧号 | 类型 | 画面内容 | 情绪 |
|------|------|----------|------|
| F018 | Text Reveal | KDO不是什么: 列表+红叉（笔记软件/知识库/存更多） | 否定 |
| F019 | Flow Diagram | 漏斗动画: 9发光节点+三输出（文章/代码/能力） | 展示 |
| F020 | Flow Diagram | 三种产出方块 + 虚线溯源到"来源" | 归纳 |
| F021 | Terminal Demo | `kdo trace` 返回原始文档/编译记录/交付版本 | 演示 |
| F022 | **金句** | "不是'存得更多'，是'产得更清晰'。" | 强调 |
| F023 | Terminal Demo | `kdo capture <url>` → "已捕获飞书文档" | 教学 |
| F024 | Terminal Demo | `kdo ingest` → wiki_id + domain | 教学 |
| F025 | Terminal Demo | `kdo enrich` 三步编译进度条（浓缩/批判/对标） | 教学 |
| F026 | Metaphor | **烹饪第1帧**: 灰色生肉块 + "原始文档=生肉" | 比喻 |
| F027 | Metaphor | **烹饪第2帧**: 白色粥碗+蒸汽 + "编译=炖成粥" | 比喻 |
| F028 | Metaphor | **烹饪第3帧**: 琥珀色菜肴+光泽 + "产出=端上桌的菜" | 比喻 |
| F029 | Terminal Demo | `kdo route`/`produce`/`validate` + 底部小字 | 教学 |
| F030 | Terminal Demo | `kdo ship`/`feedback`/`improve` + "状态:shipped" | 教学 |
| F031 | **金句** | "可以只用 3 步。也可以用满 9 步。"（数字琥珀放大） | 灵活 |

### 质量门
```bash
kdo video validate --stage frames
# 结果: PASS
```

---

## 7e — Seg 4 画面制作 (对比)

| 项目 | 内容 |
|------|------|
| **入参** | `02-storyboard.md` v2（F032-F034） |
| **出参** | `frames/segment_4_frame_032.png` ~ `034.png`（3帧） |
| **情绪弧线** | 冲突→反转→冲击（最强情绪段） |
| **特点** | 左右分屏，冷灰vs琥珀，墓碑vs流水线 |

### 3帧清单

| 帧号 | 类型 | 画面内容 | 情绪 |
|------|------|----------|------|
| F032 | Comparison | **左右分屏**: 左侧冷灰墓碑（裂纹+"谷歌分析.docx"+青草+Day90） vs 右侧琥珀流水线（7 CLI节点+流光） | 冲突 |
| F033 | Comparison | **延续**: 墓碑青草更多 + 右侧文档图标+绿色✓ + "持续更新" | 反转 |
| F034 | **金句** | "传统做法，文档写完就是墓碑。" / "KDO的做法，文档写完才是开始。" | 冲击 |

### 质量门
```bash
kdo video validate --stage frames
# 结果: PASS
```

---

## 7f — Seg 5 画面制作 (结尾)

| 项目 | 内容 |
|------|------|
| **入参** | `02-storyboard.md` v2（F035-F040） |
| **出参** | `frames/segment_5_frame_035.png` ~ `040.png`（6帧） |
| **情绪弧线** | 温暖→融合→理性→坚定→结束 |

### 6帧清单

| 帧号 | 类型 | 画面内容 | 情绪 |
|------|------|----------|------|
| F035 | Comparison | 花园(Obsidian, 绿) vs 厨房(KDO, 琥珀) + 传送带+果实流动 | 温暖 |
| F036 | Metaphor | 花园插画→传送带→厨房插画，中央箭头融合 | 融合 |
| F037 | Text Reveal | 适合/不适合 两栏对比（绿✓ vs 灰横线） | 理性 |
| F038 | **金句** | "信息变不成资产，才是问题。" | 坚定 |
| F039 | CTA Card | KDO logo + "让你的知识值得被交付。" + 底部小字 | 号召 |
| F040 | End Screen | 淡出至黑 + 官方文档/GitHub/版权信息 | 结束 |

### 质量门
```bash
kdo video validate --stage frames
# 结果: PASS
```

---

## 7g — 音画对位 (Audio-Visual Sync)

| 项目 | 内容 |
|------|------|
| **入参** | `frames/`（40帧）+ `01-script.md`（口播文本） |
| **出参** | `draft/draft.mp4` + `audio/full_audio.mp3` |
| **工具链** | edge-tts（TTS）+ ffmpeg（合成） |
| **前置条件** | 40帧全部就绪 + 脚本通过审批 |

### 三步工序

#### Step 1: 提取口播文本
- 从 `01-script.md` 提取 "Full Text (for TTS / recording)" 部分
- 清理换行，生成 `audio/full_text.txt`（2303字符）

#### Step 2: TTS 音频生成
```bash
edge-tts --file full_text.txt --write-media full_audio.mp3 --voice zh-CN-XiaoxiaoNeural
```
- **实际音频时长**: 487.9秒（~8.1分钟）
- **语速**: 约280字/分钟（正常范围）

#### Step 3: 视频合成
```bash
ffmpeg -f concat -i concat.txt -i full_audio.mp3 -c:v libx264 -c:a aac draft.mp4
```
- **每帧时长**: 487.9s ÷ 40 = **12.2秒**
- **输出参数**: 1920×1080, H.264, AAC, 11.5MB
- **总时长**: 500.1秒（~8.3分钟）

### 音画对位审查

| 检查项 | 结果 | 说明 |
|--------|------|------|
| 音画时长匹配 | ✅ | 500s vs 488s，差异12s（最后一帧延时） |
| 分辨率/编码 | ✅ | 1920×1080 H.264/AAC |
| 音频完整性 | ✅ | 2303字全文，无断点 |
| 帧时长分配 | ⚠️ | **均匀分配** 12.2s/帧，非按 segment 口播动态分配 |
| 帧切换与口播匹配 | ⚠️ | 静态分配，无法精确对位到句子级别 |

### 质量门
```bash
kdo video validate --stage compose
# 结果: PASS
```

---

## 各阶段审批记录

| 阶段 | 完成时间 | 审批状态 | kdo验证 |
|------|---------|---------|---------|
| 7a 分镜修订 | 2026-05-20 | ✅ 已审批 | storyboard PASS |
| 7b Seg1 画面 | 2026-05-20 | ✅ 已审批 | frames PASS |
| 7c Seg2 画面 | 2026-05-20 | ✅ 已审批 (Gate 2) | frames PASS |
| 7d Seg3 画面 | 2026-05-20 | ✅ 已审批 (Gate 2) | frames PASS |
| 7e Seg4 画面 | 2026-05-20 | ✅ 已审批 | frames PASS |
| 7f Seg5 画面 | 2026-05-20 | ✅ 已审批 | frames PASS |
| 7g 音画对位 | 2026-05-20 | 🔴 **待审批** | compose PASS |

---

## 产出物总览

```
40_outputs/content/videos/knowledge-delivery-os-快速上手指南把散落知识变成可交付资产/
├── _spec.md                    # 项目规格
├── 01-script.md                # 口播脚本 (2219字)
├── 02-storyboard.md            # 分镜v2 (40帧)
├── 03-qa-report.md             # QA报告 (全流程)
├── 07-production-flow-summary.md  # 本文件
├── audio/
│   ├── full_audio.mp3          # TTS音频 (487.9s)
│   ├── full_text.txt           # TTS源文本
│   └── segments_backup/        # 5段异常segment音频备份
├── draft/
│   └── draft.mp4               # 合成视频 (500s, 11.5MB)
├── frames/
│   ├── segment_1_frame_001.png ~ 010.png   # Seg 1: 10帧
│   ├── segment_2_frame_011.png ~ 017.png   # Seg 2: 7帧
│   ├── segment_3_frame_018.png ~ 031.png   # Seg 3: 14帧
│   ├── segment_4_frame_032.png ~ 034.png   # Seg 4: 3帧
│   └── segment_5_frame_035.png ~ 040.png   # Seg 5: 6帧
```

---

## 下一阶段

**Ship (交付)** — Gate 5

```bash
kdo video ship <project_dir>
```

- 验证 draft.mp4
- 复制到 final/final.mp4
- 记录交付状态
- 输出到 `50_delivery/`

*按五绝分工，Ship 是段王爷（Publisher）的职责，北丐职责到 7g 为止。*

---

*本文件由洪七公自动生成，供欧阳锋 QA 审查。*
