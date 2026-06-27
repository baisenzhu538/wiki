---

id: dk-ef-004-missing-diagnostic-firmware
title: 没有诊断固件就是盲调：你不知道信号卡在哪一级
type: dk
domain:
- src_unknown
dark_knowledge_type: hardware-failure
source_person: 黄药师
source_context: 复杂信号链路调试（MCU→电平转换→595→MOSFET→LED→接收管→MUX→运放→MCU）——不知道哪一级出了问题
source_refs:
- 90_control/electronics-practice/failure-modes-electronics.md
created_at: 2026-06-07
updated_at: '2026-06-16'
related:
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
pipeline:
- src_unknown
author: 黄药师
reviewed_by: pending
confidence: 0.75
trust_level: medium
---# 没有诊断固件就是盲调：你不知道信号卡在哪一级

## 原始表述

> E-FM-004：复杂信号链路（MCU→电平转换→595→MOSFET→LED→接收管→MUX→运放→MCU）出现故障。不知道哪一级出了问题，只能盲调参数。

**对策**：建一个 `diagnostic/` 目录，里面放"短路"某级链路的诊断固件。例如：强制拉高 QD 信号绕过 595，直接点灯确认发射管和接收管硬件正常。

关联项目：广冷电子 HX-SMJ 红外光栅板。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **建 diagnostic/ 目录**：在你的固件项目根目录下建一个 `diagnostic/` 文件夹，专门放诊断版固件
2. **逐级短路法**：从信号链的起点（MCU GPIO）开始，写一个最小固件只控制这一级——用诊断固件验证这一级正确 → 往下一级 → 找到断点
3. **诊断固件的特征**：
   - src_unknown
   - src_unknown
   - src_unknown
   - src_unknown
4. **示例**：广冷红外板调试时，写了一个诊断固件强制拉高 QD 信号，绕过 595 移位寄存器，直接用 GPIO 控制 LED——两分钟确认发射管和接收管硬件正常，问题定位到 595 时序

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 为什么值钱

P-21（无诊断手段时盲目调参）就是这个模式的通用版本。这里把它落地到了嵌入式硬件的具体操作。

软件工程师默认会用 `printf` 看变量值——这是诊断。但嵌入式硬件工程师的调试习惯往往是"换个参数试试"——因为写一个诊断固件比改一个宏定义的值要麻烦。**方便的东西被优先使用，不管它有没有用。**

"先造诊断工具再造产品"这个原则听起来很对，但在嵌入式领域的具体操作是什么？是 `diagnostic/` 目录。这个目录的存在，比具体某一份诊断固件更重要——它改变了调试的心智模式：从"猜→烧→试"变成"切链路→定位→修复"。

广冷红外板 V2.2 调了 Ir_Delay 从 15→30→100→200→300→500 六个值，零进展。写一份诊断固件花了两小时——但两小时后问题定位完成，修复花五分钟。**诊断固件的 ROI 不是"花了两小时换来五分钟"，而是"两小时换来了从 0 到 1 的突破"。**
