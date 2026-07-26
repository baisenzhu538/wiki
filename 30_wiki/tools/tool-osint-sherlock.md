---
id: tool-osint-sherlock
title: Sherlock：用户名跨平台追踪——找到一个人的所有社交账号
type: tool
status: reviewed
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
- proposal-prompt-injection-infrastructure
- business-research-skill-oscar-13-weapon-system
updated_at: '2026-06-29'
tags:
- audience:executor
- scene:execution
- skill-level:advanced
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

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 操作步骤

1. **步骤一**：待补充
2. **步骤二**：待补充
3. **步骤三**：待补充

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

- **具体假设**：该工具假设用户名唯一性能关联不同平台的身份，但同名用户和刻意模仿的用户名会产生大量误报——关联不等于同一身份。
- **边界**：在全新领域或快速变化的环境中，已有数据和经验可能完全失效——工具的有效性高度依赖场景的稳定性。
- **前提**：该工具的前提是使用者能正确理解和执行工具的规则，但执行者的认知偏差和经验限制会影响工具的实际效果。

**Ross Anderson**（剑桥大学安全工程教授）会质疑：工具的价值不在于"有没有"，而在于"用得好不好"。任何工具都是"能力放大器"——如果使用者的判断力不足，工具只会放大错误。真正的风险不是"缺少工具"，而是"有了工具后产生的虚假安全感"——让你以为自己已经覆盖了所有可能性，实际上只是走完了流程。
