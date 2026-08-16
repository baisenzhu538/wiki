---
name: research-financial-report
description: 上市公司财报/招股书深度解读——基于一堂方法论+Doris行业报告体系
version: 1.0.0
author: 黄药师
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [research, 财报, 招股书, 上市公司, 年报, 财务分析]
    related_skills: [research, research-cross-validation]
---

# 财报/招股书深度解读

基于一堂上市公司报告解读方法论。

## 触发词

财报、招股书、年报、上市公司、IPO、营收、利润、毛利率、看懂财报

## 约束

- 数字必须来自原始报告，禁止凭记忆输出
- 标注数据来源：报告名称 + 页码 + 年份
- 对标分析时至少选 3 家可比公司

## 执行步骤

### Step 1: 获取报告
- 巨潮资讯网 (cninfo.com.cn) — A 股官方
- 港交所披露易 — 港股
- SEC EDGAR — 美股

### Step 2: 关键数据提取
- 营收结构（按产品/地区/客户）
- 成本结构（毛利率、费用率）
- 增长驱动（量价拆分）
- 竞争格局（市场份额）
- 风险披露（招股书风险因素章节）

### Step 3: 对标分析
4 种关系选对标：同行/上下游/同模式/同用户

### Step 4: 输出报告
包含：核心财务数据 + 营收拆分 + 对标对比 + 关键风险 + 结论

## 参考案例
- `case-popmart-prospectus-pricing` — 泡泡玛特招股书
- `case-neworiental-prospectus-marketing` — 新东方招股书
- `case-proya-betaine-skincare-benchmark` — 珀莱雅/贝泰妮对标
