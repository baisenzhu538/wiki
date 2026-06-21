---
name: stage-1-diagnose
description: 域诊断——素材验收+置信度标记+盲区识别+任务清单生成（王语嫣模式）
version: 1.0.0
author: 黄药师
license: MIT
platforms: [cli, feishu]
metadata:
  hermes:
    tags: [KDO, 诊断, 素材验收, 把关, 王语嫣]
    related_skills: [domain-iteration, stage-2-skeleton]
---

# Stage 1: 域诊断

将 `00_inbox/<域>/` 下的原始素材验收、分级、识别盲区。

## 触发词

素材验收、标记素材、诊断这个域、把关素材、素材补齐了看看、diagnose domain

## 约束

- 严禁跳过素材盘点直接写诊断
- 每份素材必须标记 L1/L2/L3 置信度
- 必须对照已有卡片避免重复
- 诊断记录必须写入 disk，不得只留在对话中

## 置信度标记

- 🔵 L1 高：≥2 独立来源，或讲师直接经验+具体案例
- 🟡 L2 存疑：单一来源、数字待核实
- 🔴 L3 不建议：来源不明、处理失败、与已有卡片重复

## 执行步骤

### Step 1: 盘点素材
统计文件数量、类型分布、口述稿/笔记/图片清单

### Step 2: 标记置信度
逐份素材 L1/L2/L3 判断

### Step 3: 识别盲区
图片缺OCR？素材不完整？Q&A尾巴有暗知识？

### Step 4: 对照已有卡片
`kdo cards --domain <域>`

### Step 5: 写诊断记录
输出到 `60_feedback/diagnosis/diag_<日期>_<域>素材验收.md`
包含：素材盘点总表 + 置信度表 + 已有卡片对照 + 盲区清单 + 生产建议

### Step 6: 生成任务清单
输出到 `60_feedback/tasks/task_<日期>_<域>生产任务清单.md`
按 Wave 分批，每张卡给 ID/类型/素材来源/验收标准

### Step 7: 跑生产前检查
```bash
python 90_control/scripts/check-source-refs.py --domain <域>
python 90_control/scripts/check-agent-config.py
```
