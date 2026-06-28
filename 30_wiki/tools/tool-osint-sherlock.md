---
id: tool-osint-sherlock
title: Sherlock：用户名跨平台追踪——找到一个人的所有社交账号
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.88
trust_level: high
language: zh-CN
domain:
- yitang
- research
source_refs:
- src_unknown
- src_unknown
related:
- '[[yitang-domain-digest]]'
- '[[yitang-research-domain-digest]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
---

# Sherlock：用户名跨平台追踪

> 输入一个用户名，Sherlock自动检查300+社交平台——瞬间找到一个人在全网的数字足迹。

## 核心能力

- src_unknown
- src_unknown
- src_unknown

## Agent执行指令

```bash
# 安装
git clone https://github.com/sherlock-project/sherlock.git
cd sherlock && pip install -r requirements.txt

# 搜索单个用户名
python sherlock.py username --output results/

# 批量搜索
python sherlock.py user1 user2 user3 --output results/ --csv

# 只看找到的（不看未找到的）
python sherlock.py username --print-found
```

## 实战场景

**场景**：背调竞对的创始人/核心员工
1. 知道竞对CEO的名字 → 转化为常见用户名变体
2. Sherlock跑一轮 → 发现他在Reddit活跃讨论行业问题
3. 发现他的GitHub → 看他的技术偏好和开源贡献
4. 发现他在小众论坛的发言 → 了解他未经过PR包装的真实观点

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 重名误判 | 同用户名≠同一个人 | 交叉验证：头像/简介/关联账号是否一致 |
| 旧账号 | 找到的是5年前已废弃的账号 | 看最后活动时间，区分活跃账号和废弃账号 |
| 隐私风险 | 不该看的私人信息被曝光 | 只看公开信息，不进私人账号 |

## 适用边界

- src_unknown
- src_unknown
- src_unknown

---

*卡片类型：tool | 审核状态：待审*
