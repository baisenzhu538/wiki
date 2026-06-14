---
id: dk-yitang-business-formula-plus-times-trap
title: "业务公式拆解：先切分再拆转化，+ 与 × 写错会误导决策"
type: dark-knowledge
dark_knowledge_type: insight
status: reviewed
domain:
  - yitang
  - master
source_person: "孔阳"
source_context: "一堂 2026-06-13 业务公式拆解培训，逻辑关系与运算符号章节"
source_refs:
  - src_20260613_6b939d2b
  - src_20260613_6edbf0af
  - src_20260613_a8bcfd38
created_at: 2026-06-15
updated_at: 2026-06-15
reviewed_by: "老顽童"
review_date: 2026-06-15
trust_level: high
related:
  - yt-business-formula-abc-model
  - yt-business-formula-six-level-logic
  - yt-business-formula-parameter-iceberg
  - case-gym-membership-formula
tags:
  - #source_type/insight
  - #domain/yitang
  - #method/business-formula
author: "欧阳锋"
confidence: 0.85
---

# 业务公式拆解：先切分再拆转化，+ 与 × 写错会误导决策

## 原始表述

> “拆解参数关系的正确顺序：先切分（+），再拆转化（×）。”
> “+ 关系 = 有一个就够了，多了更好，但不要平均用力。”
> “× 关系 = 漏斗关系，缺一不可，必须逐个提升。”
> “相关不是因果。L2 只能看趋势，L3 才能找到抓手。”

——孔阳，一堂 2026-06-13 业务公式拆解培训

---

## 使用场景

- 你把业务拆成 `GMV = 流量 × 转化率 × 客单价 × 复购率` 后，团队仍然不知道先动哪个。
- 你发现公式里某个参数由多个子参数组成，但不确定写“+”还是“×”。
- 你把两个相关变量当成因果，结果干预后 ROI 崩盘。

---

## 操作方法

### 1. 拆解顺序：先切分（+），再拆转化（×）

```
GMV = A 渠道 GMV + B 渠道 GMV + C 渠道 GMV
A 渠道 GMV = 曝光量 × 点击率 × 转化率 × 客单价
```

或者按用户类型切分：

```
GMV = 新用户 GMV + 复购用户 GMV + 转介绍 GMV
```

**为什么**：不同渠道、不同用户类型的转化逻辑不同，混在一起拆出来的参数关系对谁都不准。

### 2. 判断运算符号

| 符号 | 业务含义 | 管理启示 | 反例 |
|---|---|---|---|
| + | 叠加关系 | 有一个就够了，不要平均用力 | 把满意度写成 ×，要求环境、教练、前台都完美 |
| × | 漏斗关系 | 缺一不可，逐个提升 | 把续卡率写成 +，忽略某个致命短板 |

### 3. 区分相关与因果

- **相关**：两个变量同向变化。只能监控，不能作为抓手。
- **因果**：A 变化导致 B 变化，控制其他变量后依然成立。

跨越 L2 → L3 的方法：做控制变量实验，或画完整因果链。

---

## 适用边界

- 业务数据量太小、样本不够时，难以验证因果关系，只能先用相关关系监控。
- 创新型业务没有历史范式时，运算符号只能靠假设，需要快速实验迭代。
- 不要为拆而拆：如果某个参数提不出可验证假设，停在这一层即可。

---

## 为什么值钱

这不是教科书里的数学表达，而是讲师在大量真实案例中提炼出的**决策防错口诀**。大多数业务公式失效，不是因为变量错了，而是运算符号错了、因果判断错了。知道“先切分再拆转化”和“+ 与 × 的业务含义”，能直接避免平均用力、资源错配和 ROI 崩盘。

---

## 与其他知识的关联

- [[yt-business-formula-abc-model]]：四种逻辑关系的官方定义
- [[yt-business-formula-six-level-logic]]：L2 相关 vs L3 因果
- [[yt-business-formula-parameter-iceberg]]：L1-L2 科目 vs L3-L4 抓手
- [[case-gym-membership-formula]]：满意度作为“因的因”的具体案例
