---
name: transcribe-win
title: "transcribe-win——Windows 原生 faster-whisper 转写（模型选档+timeout 语义）"
description: |
  Windows 原生 faster-whisper 转写（CPU int8）：视频/音频 → 带时间戳逐字稿 md。
  模型三档 tiny/small/medium 选档纪律（政策/课程类 tiny 乱码）、--prompt 术语注入的收益与副作用、
  长视频耗时预算（RTF 实测）与 #649 修后的 timeout 语义。
category: kdo-infrastructure
version: 1.0.0
related_skills:
  - oral-transcript-trio
encapsulates: kdo-tools/transcribe_win.py
tags:
  - audience:hongqigong
  - scene:transcription
  - 转写
  - 逐字稿
status: draft
reviewed_by: 待审
review_date:
grade:
updated_at: 2026-09-06
trigger:
  natural_language:
    - 视频/音频转文字
    - 转写逐字稿
    - 转写乱码/专名错转
    - 长视频转写超时
    - faster-whisper 模型下载
    - transcribe_win 怎么用
---

# transcribe-win：Windows 原生转写（faster-whisper CPU int8）

> **一句话**：`python kdo-tools/transcribe_win.py <视频/音频> <输出.md> --model small --prompt "术语1、术语2"` —— 落出带 `[mm:ss]` 时间戳的逐字稿，头部自带环境指纹。

## 何时用

- 微信视频号/B站回放/本地音视频需要出逐字稿（下游走 `oral-transcript-trio` 深挖）
- `wechat_link_monitor` 管线之外的**手工补转写**（管线挂了、漏单、单独素材）
- 转写质量出问题（专名错转/整段乱码）需要换模型档重跑

**不要用于**：已有逐字稿的稿子（先查 `00_inbox/**/knowledge/` 与 transcript-registry）；英文内容（`language="zh"` 写死）。

## 怎么调

```bash
cd C:\Users\Administrator\Desktop\wiki

# 常规（默认 small）
python kdo-tools/transcribe_win.py "60_feedback/wechat-collect/<hash>.mp4" "00_inbox/wechat-collect/src_wechat_<hash>.md"

# 政策/课程/专名密集内容：medium + 术语提示
python kdo-tools/transcribe_win.py <媒体路径> <输出.md> --model medium --prompt "工信部、首购首用、数据要素"

# 快速摸底（低价值/只想知道讲了啥）——tiny 仅限此场景
python kdo-tools/transcribe_win.py <媒体路径> <输出.md> --model tiny
```

### 参数与模型选档

| 参数 | 取值 | 说明 |
|:--|:--|:--|
| `<媒体>` `<输出.md>` | 位置参数，顺序固定 | 输出建议落 `00_inbox/<专题>/`，命名带源 hash 便于溯源 |
| `--model` | `tiny` / `small`（默认）/ `medium` | 见下表；**残缺模型会明确报错，不静默降级** |
| `--prompt` | 顿号分隔的中文专名 | initial_prompt 术语注入：专名大部修复，但**长音频尾段提示衰减 + 可能数字漂移（实测 2027→2020）**——用了必须抽查数字 |

| 模型 | 适用 | 实测（#634 对照，CPU int8） |
|:--|:--|:--|
| `tiny` | 仅快速摸底 | 34s 素材段整段乱码（工信部→公秦部）；**政策/课程类禁用** |
| `small` | 默认；闲聊/访谈 | 裸跑偶发专名错转（工信部→公刑部）；+prompt 大部修复，152s |
| `medium` | 政策/课程/专名密集（验收标准=关键名词零错转） | 模型已在位（`faster-whisper-medium/`） |

### 耗时预算与 timeout 语义（#649 修后）

- 本机实测（65min/148MB 视频，small，CPU int8）：**实际 2475s，RTF≈0.63**——旧管线固定 900s 超时只够实际所需的 36%，这就是当年「每拍重下死循环」的死因。
- 管线内（`wechat_link_monitor.py`）#649 修后：动态 timeout = 媒体时长×1.0 + 300s（下限 900s，上限 4h；ffprobe 缺席按体量 60s/MB 兜底），失败留痕 ledger + 同素材 3 败熔断——**不要再把它改回固定值**。
- 手工直跑长视频：按 `媒体时长 × 0.7` 起步预留时间，放后台跑（不要用 15 分钟前台超时），跑完看输出 md 头部的 `耗时` 字段核对。

### 产出格式

```markdown
# 逐字稿

> 源: <媒体路径> | 模型: small | 设备: cpu | 引擎: faster-whisper 1.x.x | 术语提示: 开 | 时长: 3905s | 耗时: 2475s

[00:00] 第一段文字……
[00:47] 第二段文字……
```

头部指纹（模型/引擎版本/耗时）是排障锚点——「上次能跑这次不行」时先对比它。

## 边界与红线

1. **模型质量红线**：政策/课程/专名密集内容用 tiny = 乱码入库污染检索面（#634 裁定）。拿不准就 medium。
2. **残缺模型明确失败，不许将就**：`model.bin` 缺失或低于最小可信尺寸（tiny 60MB/small 400MB/medium 1200MB）→ 脚本 exit 2 并给下载命令，**不静默降级**。
3. `language="zh"` 写死、CPU int8、单文件单次——批量请循环调用，每完成一个落盘一个。
4. 转写稿是原始素材层：落 `00_inbox/` 或 `60_feedback/wechat-collect/`，不改写不删除；下游深挖走 `oral-transcript-trio`。
5. 环境自检：`import faster_whisper` 失败会明确报错（该包曾无痕失踪）——修复 `python -m pip install faster-whisper==1.2.1`，不要先怀疑脚本。

## 常见坑（症状 → 修复）

| 症状 | 根因 | 修复 |
|:--|:--|:--|
| 整段乱码、专名全错 | 用了 tiny（或残缺 small） | 换 `--model medium`（政策/课程类必选） |
| 专名对了但年份/数字变了 | `--prompt` 注入的数字漂移副作用 | 抽查数字段；或去掉 prompt 重跑对照 |
| ❌ 模型不可用：model.bin 缺失/仅 N 字节 | 下载中断/残缺——残缺模型加载不报错但出烂稿，脚本已硬拦 | 按报错里的命令走镜像下载：`HF_ENDPOINT=https://hf-mirror.com python -m huggingface_hub.commands.huggingface_cli download Systran/faster-whisper-<档> --local-dir <模型目录>`（实测 hf-mirror ≈90MB/s；HF 直连常不通） |
| 转写到一半被杀、无产出 | 前台超时太短（长视频） | 后台跑 + 按 RTF 预算时间；管线场景确认动态 timeout 生效（#649） |
| `faster_whisper` ImportError | 环境漂移（#634：曾无痕失踪，根因不可考） | `python -m pip install faster-whisper==1.2.1`；修复后在产出头部核对引擎版本 |
| 转写完的稿子没人消费 | 只转不读 | 转写完立刻走 `oral-transcript-trio`（扫描+索引+逐字读） |

## 失败模式（本技能特有）

| 失败 | 可识别信号 | 修复 |
|:--|:--|:--|
| 拿 tiny 省时间 | 「先跑一版看看」用了默认 tiny 跑政策课 | 记住 tiny 只做「有没有内容」判断，正式稿重跑 medium |
| 输出路径随手放 | 逐字稿落在 `_tmp/` 或根目录 | 按专题落 `00_inbox/<专题>/`，命名带源 hash，保证可溯源 |
| 只看完成不看指纹 | 不核对 md 头部模型/耗时字段 | 验收第一步读头部指纹，再抽读首中尾三段 |

## 相关协议与卡

- 选档与质量裁定：`#634` 转写质量升级（脚本 `transcribe_win.py` docstring 含对照实测数据）
- timeout 语义与死循环实证：`60_feedback/tasks/task_20260906_huangyaoshi-transcribe-timeout-and-aliases.md`（#649，148MB 视频每拍重下实证）
- 下游：`oral-transcript-trio` skill（扫描高价值段 + 主题索引 + W1 逐字读红线）
