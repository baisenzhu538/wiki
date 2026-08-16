---
name: research-cross-validation
description: 调研交叉验证——六层验证框架+多重身份验证，每条核心结论≥2个独立来源
version: 1.0.0
author: 黄药师
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [research, 验证, 核实, fact-check, 信源可信度]
    related_skills: [research, research-financial-report, research-industry-report]
---

# 调研交叉验证

六层验证框架 + 多重身份验证。每条核心结论必须 ≥2 个独立来源确认。

## 触发词

交叉验证、核实、验证、confirm、verify、fact check、数据不一致

## 六层验证

| 层级 | 验证方式 | 可信度 |
|:--|:--|:--|
| L1 | 官方文件（财报/监管/政府公告） | 🔵 最高 |
| L2 | 权威第三方（审计/咨询/学术） | 🔵 高 |
| L3 | 多源交叉（≥3 独立来源一致） | 🟡 中 |
| L4 | 推理验证（逻辑自洽） | 🟡 中 |
| L5 | 单源参考 | 🟠 低 |
| L6 | 传闻/推测 | 🔴 不可用 |

## 多重身份验证

一条情报 ≥2 个独立身份/视角交叉确认：
- 大表哥刘涛：boss直聘+评论区照片+面试 → 7-8轮验证
- 张兰：假扮店长卧底15天 → 多重身份确认运营数据

## 执行步骤

1. 列出所有核心结论
2. 逐条标注 L1-L6 层级
3. L5/L6 结论 → 追加搜索 → 找不到则降级标注
4. 矛盾处理：标注分歧，不做推测
5. 输出验证矩阵（结论 + 来源1 + 来源2 + 层级 + 可信度）
