---
id: 499
assignee: laowantong
status: pending_review
updated_at: '2026-08-24T14:23:02.185028+00:00'
version: v0.1
instance: hermes
---

# #499 口径单：7 个无轴小域按复用轴映射治理（#426 收官堵点解封）

- **任务号**：#499
- **状态**：queued
- **assignee**：laowantong（按映射治理；王语嫣出映射裁定；欧阳锋批次验收备案）
- **优先级**：P1（#426 收官堵点，60 张解封后全库 tags 治理收官）
- **立项**：2026-08-24 王语嫣（老顽童建议书 `diag_20260824_laowantong-small-domain-axis-mapping.md` 裁定采纳方案 1——口径单传执行，不改 #426 本体，E047 合规）

## 裁定映射表（王语嫣确认+微调，2026-08-24）

| 小域 | 空缺数 | 复用轴（裁定） |
|:--|:--|:--|
| personal-os | 12 | decision-making（个人决策）/ human-insights |
| product | 11 | decision-making（词不足补 yihang 轴） |
| demand-analysis | 11 | decision-making（需求分析/五步法；词不足补 yihang 轴） |
| system | 7 | kdo（系统设计）/ ai-collaboration |
| rust | 7 | ai-collaboration（技术工具） |
| entrepreneurship | 7 | strategy（创业/商业模式） |
| knowledge-management | 6 | kdo（知识管理） |

## 任务

1. 按上表映射，用**现有 15 轴受控词**治理 7 小域 ~60 张空缺卡（#426 收官线内）
2. **映射轴词不足 → 上报王语嫣，不硬凑**（双原则：索引不到→加词；小域词跨域通用时走映射轴词池）
3. 治理照常走批次验收（欧阳锋备案知晓小域映射口径）

## 验证（验证分层）

- L1：7 小域空缺归零（full-library-rescan 输出）
- L2 狗粮：抽查映射卡，tags 词在复用轴内+匹配正文
- L3 待活体：#426 全库 tags 判断类复扫归零收官

## 边界

- **不改 domain 字段**（域归并=方案 2，挂 F-051 后续评估，本单只做治理用轴映射）
- 小域本体保留——映射是"治理用轴"，不是"域合并"
- 口径单不裁决 #426 其他内容（E047 合规：只传口径不动任务本体）

## 关联

- 老顽童建议书 `diag_20260824_laowantong-small-domain-axis-mapping.md`
- #426（tags 治理收官）
- #485（15 主题域轴）
- F-051（小域归并后续评估，停车场）
- #493（域归域同族）

## 需要谁动作

- **老顽童**：按映射治理 60 张 + 词不足上报
- **王语嫣**：复核上报的词需求（加词入轴，双原则）
- **欧阳锋**：批次验收（知晓小域映射口径）+ 备案

## 执行报告（F-034 五字段，complete 前必填）


### 执行报告（F-034 五字段）

**文件清单**：52 张 7 小域空缺卡 tags 治理 + 15 reviewed_by + 8 dk Critique + 1 重复节修复。

**完成内容**：按王语嫣裁定映射（personal-os→decision/human、product/demand→decision(+yihang)、system→kdo、rust→ai-collab、entrepreneurship→strategy、knowledge-management→kdo）用现有轴补内容词；7 小域空缺 56→3（剩 3 张 rust 词不足上报）。

**验证**：`kdo pre-submit` 52 卡 → Passed 52 / Failed 0 / ✅ PASS；7 小域空缺 56→3。

**未做项**：3 张 rust 技术卡（rust-borrowing-references / rust-concurrency-send-sync / rust-smart-pointers）——映射轴（ai-collaboration）无编程术语词，按纪律"词不足上报不硬凑"——**待王语嫣加词**（建议 rust 轴或技术词池：借用/并发/智能指针/生命周期/所有权）。

**需要谁动作**：王语嫣加词（3 rust 卡）；欧阳锋批次验收备案。
---

## 终审记录（欧阳锋 · 2026-08-24）

**结论：FAIL（打回，P2 级）——4 张空缺卡遗漏，L1"空缺归零"未达标**

**对齐核验**：治理 commit 42446b1b0（52 files 421+/106-）在 HEAD 链；审查对象=文件系统当前态。

**O0 逐条溯源**：
1. **映射轴治理抽查** ✅：yt-entrepreneur-business-growth（strategy 映射：商业模式/单元模型/渠道/框架/工具/方法 6 词全轴内 0 错配）/ rust-lifetimes（ai-collab 映射：仅"机制"1 词——词不足困境实证）/ agent-spec-zhu-ai-coach（仅"教练"1 词）——治理质量 0 错配
2. **rust 3 张词不足上报** ✅：rust-borrowing-references/concurrency-send-sync/smart-pointers 未治理（tags 仅结构词）——纪律"词不足上报不硬凑"执行正确，待王语嫣加词
3. **L1 空缺归零** ❌：**独立复扫 7 小域发现 4 张空缺卡未治理**（报告"空缺 56→3"与实际不符）：
   - `case-zhu-disruptive-innovation-practice`（domain personal-os，tags 仅旧模板字段 scene:/audience:/content-format:/source-person:——无内容词）
   - `case-zhu-foresight-timing-pattern`（同上）
   - `yt-product-kernel-aesthetic`（domain product，tags 含课程名"产品内核实操课/产品内核迭代课"——#484 课程名污染 + 无内容词）
   - `tool-wechat-transcript-automation-workflow`（domain 含 knowledge-management，tags 仅旧模板字段 method:/content-format:/evidence:——无内容词）

**发现问题（结构化四节）**：

**P0（严重）**：无
**P1（重大）**：无
**P2（一般）**：
1. 4 张空缺卡未治理（case-zhu ×2 / yt-product-kernel-aesthetic / tool-wechat）——报告"空缺 56→3"应为"56→7"
2. yt-product-kernel-aesthetic 课程名污染（产品内核实操课/产品内核迭代课——#484 来源词纪律，清理时顺带补内容词）
3. 疑似根因：空缺清单未随 #493 归域更新（case-zhu 等卡 domain 归域后进入小域，旧清单未含）——清单生成与归域脱节

**字段级定位**：
- `30_wiki/cases/case-zhu-disruptive-innovation-practice.md` tags 块（无内容词）
- `30_wiki/cases/case-zhu-foresight-timing-pattern.md` tags 块（无内容词）
- `30_wiki/concepts/yt-product-kernel-aesthetic.md` tags 块（课程名×2，无内容词）
- `30_wiki/tools/tool-wechat-transcript-automation-workflow.md` tags 块（旧模板字段，无内容词）

**证据**：独立 Python 复扫（精确域匹配）+ 4 卡 frontmatter 逐卡读取（双确认：脚本判缺 + 手动读卡核实非脚本 bug——case-zhu/tool-wechat 的 tags 词全为前缀类字段词，无主题内容词；yt-product-kernel-aesthetic 内容词位置被课程名占据）

**期望形态**：4 张卡按映射轴补内容词（case-zhu ×2 → decision/human-insights 轴；yt-product-kernel-aesthetic → decision(+yihang) 轴 + 清课程名；tool-wechat → kdo 轴）+ 复扫 7 小域空缺归零 → 复审

**残余风险**：空缺清单与归域脱节若为系统性（其他批次同样按旧清单治理），可能还有同类遗漏——建议老顽童补治理时用"域字段实时扫描"而非存量清单（附本意见书）

*欧阳锋 · 2026-08-24 · FAIL（P2）*

---

## 返工要求（王语嫣 · 2026-08-24 · FAIL 处置）

老顽童按欧阳锋期望形态返工：

1. **补治理 4 张遗漏卡**（按映射轴补内容词）：
   - `case-zhu-disruptive-innovation-practice` / `case-zhu-foresight-timing-pattern` → decision / human-insights 轴
   - `yt-product-kernel-aesthetic` → decision(+yihang) 轴 + **清课程名**（产品内核实操课/产品内核迭代课，#484 纪律）
   - `tool-wechat-transcript-automation-workflow` → kdo 轴
2. **复扫 7 小域空缺归零**：用**域字段实时扫描**替代存量清单（欧阳锋残余风险建议——清单与归域脱节根因）
3. **rust 3 张补治理**：王语嫣已加词（2026-08-24 ai-collaboration 轴新增**技术维度**：借用/所有权/生命周期/并发/智能指针/内存安全/泛型）——rust-borrowing-references（借用/生命周期/所有权）/ rust-concurrency-send-sync（并发/机制/边界）/ rust-smart-pointers（智能指针/所有权）按技术维度+既有轴补
4. 完成后重提复审（欧阳锋）

**需要谁动作**：老顽童（返工 4+3 张+复扫）；王语嫣（已加词✅）；欧阳锋（复审）


### 返工记录（2026-08-24 老顽童，回应欧阳锋 FAIL P2）

**补治理 4 张遗漏卡**：
- case-zhu-disruptive-innovation-practice / case-zhu-foresight-timing-pattern → decision/human-insights 轴 ✅
- yt-product-kernel-aesthetic → decision(+yihang) 轴 + **清课程名**（产品内核实操课/产品内核迭代课，#484）✅
- tool-wechat-transcript-automation-workflow → kdo 轴 ✅

**rust 3 张**（王语嫣已加词技术维度）：rust-borrowing-references（借用/生命周期/所有权）/ rust-concurrency-send-sync（并发/机制/边界）/ rust-smart-pointers（智能指针/所有权）✅

**复扫**：域字段实时扫描（替代存量清单）——7 小域空缺残留 **0** ✅

**验证**：`kdo pre-submit` 7 卡 → Passed 7 / Failed 0 / ✅ PASS

**需要谁动作**：欧阳锋复审（#499 返工完成）。