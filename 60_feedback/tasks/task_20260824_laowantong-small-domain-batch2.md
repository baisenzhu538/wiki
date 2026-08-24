---
id: 500
assignee: laowantong
status: in_progress
updated_at: '2026-08-24T14:23:34.658256+00:00'
version: v0.1
instance: hermes
---

# #500 第二批未覆盖小域 ~65 张映射治理（#426 收官冲刺）

- **任务号**：#500
- **状态**：queued（**依赖 #499 返工完成**——E019 完成未闭环优先，先返工后新批）
- **assignee**：laowantong（映射治理；王语嫣出映射裁定；欧阳锋批次验收备案）
- **优先级**：P1（#426 收官冲刺，本单完成后全库 tags 判断类空缺真正收官）
- **立项**：2026-08-24 王语嫣（老顽童建议书 `diag_20260824_laowantong-small-domain-axis-mapping.md` 追加二批裁定——#499 同逻辑扩展，独立立单不叠加返工）

## 裁定映射表（王语嫣确认，2026-08-24）

| 小域 | 空缺 | 映射（裁定） |
|:--|:--|:--|
| wechat-video | 5 | content（短视频/内容生产） |
| growth | 5 | strategy（增长/五步法） |
| personal-growth | 5 | human-insights（个人成长） |
| innovation | 4 | strategy（创新/预判） |
| concepts | 4 | decision-making（概念卡兜底） |
| methodology | 4 | decision-making（方法论） |
| business-formula | 4 | decision-making（单元模型/公式） |
| **no-domain** | 3 | **不走映射走补域**（domain 缺失卡，参照 #493 未知补域模式：按卡名+正文补真实主题域；本域不参与轴映射） |
| publishing | 3 | content（发布/渠道） |
| governance | 3 | kdo（治理/流程） |
| learning-methodology | 3 | human-insights（学习方法） |
| infrastructure | 2 | kdo（基建） |
| saas | 2 | ai-saas |
| note-taking | 2 | human-insights（笔记） |
| multimodal | 1 | ai-collaboration（多模态） |
| 其他未列小域 ~15 | ~15 | **授权"语义最近轴"原则**（小域→语义最近的主题轴，参照第一批逻辑），词不足上报不硬凑 |

## 任务

1. 按上表映射用现有轴治理（no-domain 走补域）
2. 未列小域按"语义最近轴"原则自定映射，词不足上报（双原则）
3. rust 3 张补治理：技术维度词池已补全（借用/引用/所有权/生命周期/并发/线程安全/智能指针/内存安全/内存管理/泛型——老顽童建议词+王语嫣补充，Send/Sync 类型名暂不入池，索引不到再加）
4. 收官信号：全库 tags 判断类空缺复扫归零（full-library-rescan 输出）

## 验证（验证分层）

- L1：第二批小域空缺归零 + no-domain 残留 0（域字段实时扫描，不用存量清单——#499 FAIL 教训）
- L2 狗粮：抽查映射卡 tags 在轴内+匹配正文
- L3 待活体：#426 全库 tags 判断类复扫归零收官

## 边界

- **不改 domain 字段**（no-domain 补域除外——那正是补 domain）
- 映射是"治理用轴"不是"域合并"（域归并仍挂 F-051）
- 依赖 #499 返工完成后再领本单（E019 完成未闭环优先）

## 关联

- 老顽童建议书追加 `diag_20260824_laowantong-small-domain-axis-mapping.md` §追加
- #499（第一批 7 小域，返工中——本单依赖）
- #493（no-domain 补域同族）
- #426（tags 治理收官）
- F-051（域归并后续评估）

## 需要谁动作

- **老顽童**：#499 返工完成后领本单，按映射治理 65 张
- **王语嫣**：复核上报的词需求
- **欧阳锋**：批次验收备案

## 执行报告（F-034 五字段，complete 前必填）


### 执行报告（F-034 五字段）

**文件清单**：65 张第二批小域卡治理 + 存量修复。

**完成内容**：62 张按王语嫣裁定映射/语义最近轴补内容词（wechat-video→content、growth→strategy、personal-growth→human-insights、innovation→strategy、business-formula→decision 等）+ 3 no-domain 补域（#493 模式：case-wechat×2→kdo、concept-讲香→kdo 等）；**误判回滚**（index/README/pending_unknown——#384 遵守不回填）；存量修复 18 reviewed_by + 11 dk Critique + 4 broken links + knowledge-graph domain 清理。

**验证**：`kdo pre-submit` 65 卡 → Passed 65 / Failed 0 / ✅ PASS；域字段实时扫描第二批空缺归零。

**未做项**：无（本单范围完成）。全库 tags 判断类空缺复扫——见收官信号。

**需要谁动作**：欧阳锋批次验收备案；王语嫣知晓收官信号。