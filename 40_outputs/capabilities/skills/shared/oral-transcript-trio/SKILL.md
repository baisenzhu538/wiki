---
name: oral-transcript-trio
title: "oral-transcript-trio——口述稿处理三件套（扫描演示段 + 主题索引 + 逐字读红线）"
description: |
  口述稿处理三件套：scan-demo-sections（高价值演示段定位）+ transcript-index（关键词→段落索引）+ W1 逐字读红线。
  工具只做导航（行号+段落），不替代阅读；跳过逐字读 = P-31 级知识遗漏（250 行 Q&A 闲聊被跳过的实证）。
category: kdo-infrastructure
version: 1.0.0
related_skills:
  - transcribe-win
encapsulates: kdo-tools/scan-demo-sections.py + kdo-tools/transcript-index.py
tags:
  - audience:laowantong
  - scene:material-processing
  - 口述稿
  - 逐字稿索引
status: draft
reviewed_by: 待审
review_date:
grade:
updated_at: 2026-09-06
trigger:
  natural_language:
    - 口述稿/逐字稿怎么处理
    - 找高价值段落/演示段
    - 超长逐字稿读不完
    - transcript-index 怎么用
    - scan-demo-sections 怎么用
    - 主题索引/段落索引
---

# oral-transcript-trio：口述稿处理三件套（扫描 + 索引 + 逐字读红线）

> **一句话**：先 `scan-demo-sections` 圈出高价值段落 → 再 `transcript-index` 按主题词跳段 → **然后逐字精读命中段和全文关键区**。工具给行号，人/agent 出判断。

## 何时用

- 拿到一份新口述稿/逐字稿（`00_inbox/**/*口述*.txt`、`*_transcript*.md` 等），要判断值不值得深挖、从哪读起
- 稿件几万行，不可能一次全读，需要按主题定位
- 产卡前做素材消费检查（确认关键段都被用过）

**不要用于**：结构化数据/表格文件；已经读过并产完卡的旧稿（先查 `kdo query` 有没有同主题卡——L7 牌）。

## 🔴 第一红线：工具只做索引，不替代阅读

- **口述稿 > 笔记 > 摘要**：笔记是人的浓缩（只覆盖 ~40% 内容），口述稿全文是 source of truth（07-04 工厂决策）。
- **逐字读，不跳读**：包括末尾 Q&A、闲聊、扯淡段——松弛状态暗知识浓度最高。P-31 实证：250 行 Q&A 被跳过，SPEC 陷阱/招投标不报满/没有当面答应=拒绝全在笔记外的闲聊里。
- 判断「这个素材值不值得深挖」必须**读完再判**，不凭扫描结果或摘要下结论。
- 扫描/索引产物落在 `_processed/`（素材目录旁），是导航辅助物，**不是知识卡，不入 30_wiki**。

## 怎么调

前置：`cd C:\Users\Administrator\Desktop\wiki`。

### 1. 圈高价值段（Truman 操作演示信号词扫描）

```bash
# 单稿扫描：打印 L 行号 + 命中信号词 + 上下文（只读，不改文件）
python kdo-tools/scan-demo-sections.py "00_inbox/AI大航海20260905/宣讲会：一堂-2026下半年AI大航海-口述.txt"

# 生成高价值段落汇编（推荐）：落 _processed/<稿名>_高价值段落汇编.md，附怀疑区清单
python kdo-tools/scan-demo-sections.py <口述稿路径> --compile

# 扫 00_inbox 全部口述稿（横向摸底）
python kdo-tools/scan-demo-sections.py --all
```

信号词示例：「我给你演示一下」「举个例子」「这是我真实的」「你们感受一下」「试一下啊」「这个建议是最近我用的特别开心的」「后来一次意外」「转折出现了」等 17 个（源码 `SIGNAL_WORDS`）。命中 = 讲者在摊开真实操作过程，**最高优先级精读**。
`--compile` 还会列「怀疑区」：连续 ≥5 行无信号词的叙事段——安静讲的重要内容，建议抽查。

### 2. 建索引 + 按主题跳段

```bash
# 建索引：落 _processed/<稿名>_索引.json + <稿名>_主题索引.md，并自动登记 transcript-registry
python kdo-tools/transcript-index.py build <口述稿路径>

# 查主题词：打印命中段落 L 行号 + 原文（关键词未精确命中时自动给包含它的近似词）
python kdo-tools/transcript-index.py search <口述稿路径> <关键词>
```

### 3. 逐字精读（只有这步产出知识）

按上面拿到的 L 行号，用 Read 带 offset/limit 读原文；读完再决定产卡与深挖（`nine-layer-deep-dig`）。

## 推荐顺序（新素材到手的第一小时）

| 步 | 动作 | 产出 |
|:--|:--|:--|
| 1 | `scan-demo-sections <稿> --compile` | 汇编 md：演示段清单 + 怀疑区 |
| 2 | `transcript-index build <稿>` | 主题索引 md/json |
| 3 | `transcript-index search <稿> <主题词>` 若干轮 | 行号定位 |
| 4 | Read 逐字读：全文骨架 + 命中段精读 + 末尾 Q&A 全读 | 阅读笔记（落盘） |
| 5 | 素材消费检查：稿中每个数字/Critique/Synthesis/Action Trigger 是否被笔记/卡片用到 | 消费率 ≥80% 才交 |

## 边界与红线

1. 产物只落 `_processed/`，不进 `30_wiki/`；不要把「索引里有 XX」当成「我读过 XX」。
2. 中文信号词扫描对英文稿无效（先转写/翻译再扫）。
3. `build` 会调用 `transcript-registry.py` 自动登记——登记失败只静默跳过，不阻断索引生成；不要因为「登记过了」就跳过阅读。
4. 素材本体（`00_inbox/`、`10_raw/`）只读不改；`_processed/` 是脚本产物，重跑会覆盖。
5. 转写稿从哪来：视频/音频先走 `transcribe-win` skill（模型选档与长视频姿势在那边）。

## 常见坑（症状 → 修复）

| 症状 | 根因 | 修复 |
|:--|:--|:--|
| `search` 报「索引不存在。先跑 build」 | 直接 search 没 build | 先 `build` 再 `search` |
| 扫描命中 0 处就判断「稿子没价值」 | 信号词只覆盖演示型讲法 | 看怀疑区清单 + 逐字读骨架，读完再判 |
| 只读汇编 md 就开始产卡 | 把导航物当内容 | 汇编只有行号+截断文本，必须回原文读 |
| 索引关键词太大/太泛命中上百段 | 关键词选了高频通用词 | 换专名/术语级关键词再 search |
| 稿件在子目录带空格/中文，命令报找不到 | 未加引号 | 路径整体加引号 |

## 失败模式（本技能特有）

| 失败 | 可识别信号 | 修复 |
|:--|:--|:--|
| 索引当阅读 | 复盘/卡片里引用的是索引截断文本 | 卡片引用一律带回原文行号核对 |
| 扫完不读 | 会话耗时 5 分钟就开写卡 | 阅读时长与稿件长度挂钩；长稿分段读，读完写笔记 |
| 末尾 Q&A 跳过 | 读完正文就收工 | P-31 红线：末尾 Q&A 必读，松弛段最高价值 |

## 相关协议与卡

- W1 逐字读红线与素材消费率：`.agent/laowantong-context.md`（牌 L2）、`90_control/kdo-industrialization-manual.md`
- 踩坑锚点：`.agent/pitfalls.md` P-7（35 张框架图跳过 OCR）/ P-31（250 行 Q&A 被跳过）
- 上游：`transcribe-win` skill（视频/音频 → 逐字稿）
- 深挖方法：`40_outputs/capabilities/skills/shared/nine-layer-deep-dig/SKILL.md`
