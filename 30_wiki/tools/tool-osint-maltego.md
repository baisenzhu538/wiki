---

id: tool-osint-maltego
title: Maltego：实体关系图谱——画出目标公司的隐藏网络
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.88
trust_level: high
language: zh-CN
domain: [yitang, research]
source_refs:
- src_unknown
- src_unknown
related:
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
---

# Maltego：实体关系图谱

> 输入一个域名、人名、公司名或邮箱，Maltego自动搜索并绘制关联网络——谁控股谁、谁认识谁、谁和谁有共同利益。

## 核心能力

| 输入 | 能画出什么 |
|:---|:---|
| 公司域名 | 子公司/母公司、关联域名、DNS记录、SSL证书 |
| 人名+公司 | 社交媒体账号、关联公司、共事过的人 |
| 邮箱地址 | 绑定的社交账号、出现过的数据泄露 |
| IP地址 | 托管了什么服务、地理位置、关联域名 |

## Agent执行指令

```bash
# Maltego 需要桌面客户端（Community版免费）
# 安装后通过 Transform Hub 安装需要的数据转换器
# CLI 自动化可选 maltego-trx (Python库)
pip install maltego-trx
# 编写自定义 Transform 后通过 Maltego 客户端调用
```

## 实战场景

**场景**：调研一家公司的真实背景
1. 输入公司域名 → 发现3个未公开的关联域名
2. 通过关联域名的WHOIS → 发现同一个注册人
3. 该注册人还注册了另一家公司 → 发现潜在竞品或子公司
4. 通过SSL证书 → 发现他们最近部署的新服务（新业务线）

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 关联过度解读 | 两个人出现在同一个活动就推断"有关系" | 区分"已知关联"和"推断关联"，标注置信度 |
| 数据过时 | WHOIS/SSL信息未更新 | 标注每条数据的时间戳 |
| 被图形误导 | 图太复杂反而看不清核心关系 | 先聚焦1-2个关键节点，再逐步展开 |

## 适用边界

- src_unknown
- src_unknown
- src_unknown

---

*卡片类型：tool | 审核状态：待审*
