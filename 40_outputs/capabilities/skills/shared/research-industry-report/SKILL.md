---
name: research-industry-report
description: 行业报告调研——Doris四步法+搜索七技，7天快速建立行业认知
version: 1.0.0
author: 黄药师
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [research, 行业报告, 市场研究, 市场规模, 赛道分析, 产业链]
    related_skills: [research, research-cross-validation]
---

# 行业报告调研

基于 Doris 行业报告调研四步法。

## 触发词

行业报告、行业分析、市场研究、市场规模、行业趋势、赛道分析、market research

## 约束

- 报告必须标注来源机构 + 发布时间
- 多信数据少信观点：优先引用数据而非分析师判断
- 可信度：官方统计 > 权威咨询 > 券商研报 > 媒体 > 个人

## 执行步骤

### Step 1: 搜索七技
1. 关键词变形（"药品零售"→"医药流通""连锁药房"）
2. PDF 后缀限定 `filetype:pdf`
3. 来源限定 `site:gov.cn`
4. 英文关键词
5. 报告聚合站（洞见研报、萝卜投研、199it）
6. 券商报告（华创/中信/中金）
7. 咨询公司（麦肯锡/BCG/贝恩）

### Step 2: 筛选（可信度评估）
🔵 官方统计 > 🟡 权威咨询 > 🟠 券商研报 > 🔴 媒体/个人

### Step 3: 速读（30分钟）
先看 executive summary → 看图表 → 看数据来源 → 记录关键数字

### Step 4: 深读
≥2 份不同来源报告交叉验证，关键数字找第三个来源确认

## 参考案例
- `case-doris-grab-industry-cognition` — 7天建立东南亚行业认知
- `case-doris-2014-music-streaming-prediction` — 预判音乐流媒体趋势
