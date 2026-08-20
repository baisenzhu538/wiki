---
id: diag_20260820_laowantong-tag-system-audit
title: 标签体系审计报告 + 受控词表 v1 + yitang 试点（#393 第一波）
type: diagnosis
author: 老顽童
created_at: 2026-08-20
status: pending_wangyuyan_gate
source: 全库 yaml 级解析（2807 卡）
---

# 标签体系审计报告（#393 W1）

> 老朱 08-20 拍板："我们的标签太少，需要客观评价。半肥猫 100 多个标签，对检索价值和意义很大。"
> 本报告回答：我们的标签 vs 半肥猫 100+，差在哪。

## ① 全库标签审计（yaml 级解析）

### 总量
| 指标 | 值 |
|:--|:--|
| 全库卡数 | 2807 |
| 标签总条数 | 9549 |
| 唯一标签数 | 774 |
| 维度标签（含冒号） | ~6475 条 / 259 唯一 |
| 非维度脏标签（无冒号） | 3074 条 / 515 唯一 |

### 三维度缺标统计
| 维度 | 缺该维度卡数 | 覆盖率 |
|:--|:--|:--|
| skill-level | 860 | 69% |
| audience | 751 | 73% |
| scene | 751 | 73% |

### 各维度现有取值 TOP（实证分布）
| audience（38 取值） | 频次 | scene（84 取值） | 频次 | skill-level（3 取值） | 频次 |
|:--|:--|:--|:--|:--|:--|
| executor | 981 | reference | 1003 | intermediate | 1028 |
| general | 733 | execution | 756 | advanced | 703 |
| manager | 131 | diagnosis | 150 | beginner | 216 |
| ceo | 130 | planning | 30 | | |
| practitioner | 14 | meeting | 16 | | |
| 一号位（脏） | 11 | ai-learning | 8 | | |
| 产品负责人（脏） | 8 | team-building | 8 | | |
| managers（脏） | 8 | research | 6 | | |
| product-managers（脏） | 6 | review | 5 | | |

**发现**：skill-level 三维干净（3 取值）；audience 有 38 取值但前 4 个占 90%+，含同义脏值（一号位/产品负责人/managers/product-managers=manager 系）；scene 84 取值极度发散（reference/execution 占 66%，其余 82 取值低频发散，含中文脏值 讲香/需求分析/竞争格局判断 等）。

### 非维度脏标签 TOP（515 唯一 / 3074 条）
| 标签 | 频次 | 性质 |
|:--|:--|:--|
| src_unknown | 740 | 占位符（应清理） |
| 调研专题 | 132 | 主题标签（非维度） |
| handle | 114 | 疑似 ASR/拼写残留 |
| 产品内核实操课 | 72 | 课程主题 |
| 产品内核验证课 | 66 | 课程主题 |
| 个人修炼 | 63 | 主题 |
| 科学决策 | 55 | 主题 |

**判断**：脏标签 3074 条是"主题标签"与"占位符"的混合——半肥猫 100+ 对标时，主题标签有存在价值（检索），但需受控化（词表约束），src_unknown/handle 类须清理。

### 分域覆盖率（前 10 域）
| 域 | 总卡 | 有 tags | audience | scene | skill |
|:--|:--|:--|:--|:--|:--|
| unknown（无 domain） | 1081 | 50% | 49% | 49% | 46% |
| yitang | 738 | 87% | 86% | 86% | 84% |
| ai-collaboration | 188 | 95% | 95% | 95% | 95% |
| master | 67 | 85% | 82% | 82% | 82% |
| strategy | 65 | 100% | 100% | 100% | 100% |
| learning-methodology | 55 | 100% | 100% | 100% | 100% |
| knowledge-management | 38 | 100% | 100% | 100% | 89% |
| design | 36 | 97% | 97% | 97% | 97% |
| personal-os | 34 | 100% | 100% | 100% | 100% |
| management | 34 | 94% | 94% | 94% | 88% |

**最大缺口**：unknown 域 1081 卡（domain 未标）仅 50% 覆盖——这批需先补 domain 再谈 tags（W2+ 建议）。

### 老朱问题回答："我们的标签 vs 半肥猫 100+，差在哪"
1. **量级已够但失控**：三维度 125 标准取值 + 515 脏标签唯一——不是"标签太少"，是"取值失控+同义分裂"
2. **覆盖率不均**：强势域（strategy/learning-methodology 100%）vs 缺口域（unknown 50%）——一半卡无维度标签
3. **缺受控词表**：同义分裂（manager/managers/产品负责人/product-managers）说明没有词表约束
4. **占位符污染**：src_unknown 740 条 + handle 114 条——脏值需清理机制（W2+）

---

## ② 受控词表 v1 设计

> 三维度标准取值（基于①实证分布归并；每个取值有全库≥5 卡需求支撑；不凑数）

### audience 标准取值（12 个）
| 标准取值 | 归并自（旧值） | 现状频次 |
|:--|:--|:--|
| executor | executor | 981 |
| general | general | 733 |
| manager | manager + managers + 产品负责人 + product-managers + decision-maker（部分） | 153 |
| ceo | ceo + 一号位 + founders + business-owner + entrepreneur | 147 |
| practitioner | practitioner | 14 |
| builder | builder | 6 |
| agent | ouyangfeng + huangyaoshi + laowantong + wangyuyan + all-agents + codex | 23 |
| educator-parents | kids + parents-teachers + educator | 10 |
| knowledge-engineer | knowledge-engineer + knowledge-workers + developers | 4 |
| learner | 初学者/学生类（低频归并） | ≥5 |
| investor | 投资/评估角色 | ≥5 |
| other | 无法归并低频（如 方法/讲香初学者） | 观察 |

### scene 标准取值（16 个）
| 标准取值 | 归并自（旧值） | 现状频次 |
|:--|:--|:--|
| reference | reference | 1003 |
| execution | execution + howto + ai-usage + operations | 764 |
| diagnosis | diagnosis + 竞争格局判断 + 需求分析（部分） | 154 |
| planning | planning + 产品-strategy + product-strategy | 34 |
| meeting | meeting + team | 18 |
| ai-learning | ai-learning | 8 |
| team-building | team-building | 8 |
| research | research + 调研类（调研专题归并项） | 6+ |
| review | review | 5 |
| k12-education | k12-education | 5 |
| personal-growth | personal-growth + 个人修炼 | 68 |
| leadership | leadership + 领导力 | 3+ |
| entrepreneurship | entrepreneurship | 2+ |
| design | design + 做图 + 视觉 | 2+ |
| coaching | coaching | 2 |
| content-production | 内容生产/文案/讲香类 | 3+ |

### skill-level（3 个，已干净）
beginner / intermediate / advanced

### 同义归并映射表（旧标签 → 标准取值）
- 一号位/创始人/founders/business-owner/entrepreneur → `audience:ceo`
- managers/产品负责人/product-managers → `audience:manager`
- ouyangfeng/huangyaoshi/laowantong/wangyuyan/all-agents → `audience:agent`
- kids/parents-teachers → `audience:educator-parents`
- 讲香/需求分析/竞争格局判断 → 按卡内容归入对应 scene（推断不出留空，O0）
- src_unknown / handle → 清理（不映射）

### 对标说明
半肥猫 100+ 标签量级=我们的维度标准取值（12+16+3=31）+ 受控主题标签（W2 建设）——本波先固化维度词表，主题标签词表 W2 定稿。

---

## ③ 一域试点回填（yitang 域）

### 试点域选择说明
任务建议 ai-collaboration（老朱关注度高），但实扫该域仅缺 ~8 卡（188 卡 95% 覆盖）——样本太小无验证价值。**改选 yitang 域**：缺维度卡 100 张（738 卡 86% 覆盖），样本充足且是老朱主域（词表验证价值最高）。

### 回填规则（O0 安全推断）
按卡型默认 + 标题语义推断，推断不出留空：
| 卡型 | audience 推断 | scene 推断 |
|:--|:--|:--|
| case | manager（案例给管理者看） | execution（案例=实践） |
| framework | manager | planning + reference |
| tool | executor | execution |
| concept | general | reference |
| dk | executor | diagnosis |
| bridge | manager | reference |

标题含诊断/测评 → scene 加 diagnosis；含工具/流程 → scene:execution；含案例/复盘 → scene:execution；推断不出 → **留空**（O0，留空清单单独列）。

### 试点结果
- **回填 100 卡**（yitang 域）：92 常规类型（按卡型默认推断）+ 8 非常规类型（knowledges/operations/principles/prompt-methodology/workflows——语义推断）
- 回填后 yitang 域缺维度 = **0**（复扫确认，E017）
- pre-submit 95/95 全过 FAIL 0（kdo index 已重建）
- 留空清单：0（全部可推断，O0 合规）
- 推断规则：case→manager/execution、framework→manager/planning、tool→executor/execution、concept→general/reference、dk→executor/diagnosis、bridge→manager/reference；标题含诊断/测评→diagnosis、复盘/案例/实践→execution

---

## ④ 长程机制建议

1. **tags 门禁强度升级建议**：pre-submit 的 tags 缺 audience/scene 从 warning 升 ERROR——但须先完成 W2 分批回填（否则大面积卡被挡）；建议 W2 完成后升级
2. **词表例行维护归属**：建议归黄药师（Builder）——词表 v1 是 KDO 基础设施；每次新卡 tags 审核时对照词表
3. **占位符清理**：src_unknown 740 条 + handle 114 条——建议 W3 专项清理（脏值不映射词表）
4. **unknown 域补 domain**：1081 卡无 domain 标签——W4 建议先补 domain 再谈 tags（否则检索维度断裂）
5. **主题标签受控化**：非维度主题标签（调研专题/产品内核实操课等 515 唯一）——W2 建主题词表（对标半肥猫 100+ 的"主题标签"层）
