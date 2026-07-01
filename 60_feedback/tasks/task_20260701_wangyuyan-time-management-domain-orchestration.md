---
id: task_20260701_wangyuyan-time-management-domain-orchestration
title: 王语嫣任务编排：时间管理域卡片化与升级
type: task
status: reviewed
priority: P2
assignee: kimi
collaborators:
- 王语嫣（域诊断 + 编排）
- 欧阳锋（终审）
- 洪七公（OCR + VLM 预处理已完成）
created_at: 2026-07-01
updated_at: '2026-07-01T16:50:06.708646+00:00'
reviewer: 欧阳锋
dependencies:
- 00_inbox/时间管理/_processed/时间管理_整合笔记.md
source_refs:
- 60_feedback/diagnosis/diag_20260701_time-management-validation.md
- 00_inbox/时间管理/truman-时间管理课程-口述.txt
- 00_inbox/时间管理/truman-时间管理课程-笔记.txt
- 00_inbox/时间管理/_processed/时间管理_整合笔记.md
- 00_inbox/时间管理/_processed/vlm_summary.json
- 30_wiki/concepts/yt-personal-time-management.md
related:
- - - yt-personal-time-management
- - - case-ai-time-management-tiered-growth
- - - yitang-domain-digest
reviewed_by: 欧阳锋
review_date: '2026-07-01'
---

# 王语嫣任务编排：时间管理域卡片化与升级

> 洪七公已完成 OCR + VLM 识别，产出 `00_inbox/时间管理/_processed/时间管理_整合笔记.md` 及 5 张图解的 VLM 解析。
> 本任务由王语嫣基于现有 KDO 覆盖情况编排，不追求一次性拆完所有概念，先补齐最关键缺口。

---

## 一、素材评估（基于 6 层交叉验证 + 9 层深挖）

完整诊断报告见：`60_feedback/diagnosis/diag_20260701_time-management-validation.md`

| 维度 | 判断 | 说明 |
|:---|:---|:---|
| 来源 | 一堂内部课程（Truman） | 与现有 `yt-personal-time-management` 同源，属于 yitang 方法论体系；来源评级 **A-** |
| 质量 | 中-高 | 口述 + 笔记 + 5 张图解 + VLM 整合，结构清晰；核心逻辑自洽 |
| 数据可信度 | B/C | "5-10 倍效率跃迁""500% 差异"等为课程主张/个人估计，非实验数据，卡片中需降级为观点 |
| KDO 域匹配 | 高 | `personal-growth` / `yitang`；与学习方法论、AI 协作、决策域可桥接 |
| 与现有卡重叠 | 中高 | `yt-personal-time-management.md` 已存在，但覆盖不完整、大量 src_unknown 占位；新素材可显著升级 |
| 综合评级 | **A- / B+** | 高价值，值得纳入，但需批判性呈现 |
| 可产出卡数 | 3-5 张 | 建议先做 1 张升级 + 2 张新建，共 3 张；后续视终审结果扩量 |

---

## 二、域诊断

### 2.1 现有覆盖

| 现有卡片 | 状态 | 问题 |
|:---|:---|:---|
| `yt-personal-time-management` | reviewed（黄药师） | 覆盖不完整，大量 `src_unknown` 占位，未覆盖新课程中的 L1-L6 进阶、深度工作冰山、双环矩阵、双峰哲学 |
| `case-ai-time-management-tiered-growth` | enriched | 商业案例，与个人时间管理方法论无关 |

### 2.2 缺口

- **个人时间管理方法论体系化**：现有概念卡只覆盖 L1-L3 三层框架，缺少 L1-L6 进阶地图。
- **任务-时间-匹配三元模型**：新课程提出的底层模型，KDO 中无对应卡片。
- **深度工作冰山模型**：L1-L5 工作深度分层，可与 `deep work`、`flow`、`ai-collaboration` 桥接。
- **双环矩阵 / 四象限 / 双峰哲学**：工具层模型，可作为工具卡或 framework 卡。

**诊断结论**：先升级核心概念卡，再建 2 张高价值新卡（三元模型 + 深度工作冰山）。工具层卡片（双环矩阵、双峰哲学、四象限）暂不新建，待核心卡通过终审后再评估。

---

## 三、建议卡片地图

### 3.1 升级现有卡

| ID | 类型 | 标题 | 核心动作 | 预期行数 |
|:---|:---|:---|:---|:---:|
| `yt-personal-time-management` | concept | 一堂科学时间管理 | 基于新素材重写/扩展，补全 src_unknown，覆盖 L1-L6 进阶、三元模型、冰山模型 | 150+ |

### 3.2 新建卡

| ID | 类型 | 标题 | 核心命题 | 预期行数 |
|:---|:---|:---|:---|:---:|
| `framework-yitang-time-management-triad` | framework | 一堂时间管理三元模型：任务-时间-匹配 | 任务模型 × 时间模型 × 匹配模型，把对的事放在对的时间 | 120+ |
| `concept-yitang-deep-work-iceberg` | concept | 深度工作冰山模型 | L1-L5 工作深度分层；时间投入 ≠ 价值产出；保护深度工作时段 | 100+ |

**首批总计**：1 张升级 + 2 张新建 = **3 张卡**。

---

## 四、域归属与桥接

| 卡片 | 主域 | 桥接到 |
|:---|:---|:---|
| `yt-personal-time-management` | personal-growth / yitang | 学习方法论域、AI 协作域、决策域 |
| `framework-yitang-time-management-triad` | personal-growth / yitang | 决策域（优先级判断）、学习方法论域（学习时段匹配）、AI 协作域（AI 工具与深度工作时段） |
| `concept-yitang-deep-work-iceberg` | personal-growth / learning-methodology | AI 协作域（AI 替代浅层工作，释放深度工作时间）、心流/专注相关卡片 |

---

## 五、生产要求

### 5.1 生产者

- **Assignee**：老顽童(Kimi)
- **审核者**：欧阳锋
- **域诊断者**：王语嫣

### 5.2 输入素材

1. `00_inbox/时间管理/_processed/时间管理_整合笔记.md`
2. `00_inbox/时间管理/_processed/vlm_summary.json`
3. `00_inbox/时间管理/truman-时间管理课程-口述.txt`
4. `00_inbox/时间管理/truman-时间管理课程-笔记.txt`
5. `30_wiki/concepts/yt-personal-time-management.md`

### 5.3 输出

1. 升级后的 `30_wiki/concepts/yt-personal-time-management.md`
2. 新建的 `30_wiki/frameworks/framework-yitang-time-management-triad.md`
3. 新建的 `30_wiki/concepts/concept-yitang-deep-work-iceberg.md`
4. 更新 `30_wiki/index.md` 收录新卡

### 5.4 验收标准

- [ ] 3 张目标卡 `kdo lint` 0 ERROR / 0 新增 WARNING
- [ ] 3 张目标卡 `kdo pre-submit` PASS
- [ ] `yt-personal-time-management` 的 `src_unknown` 全部替换为具体来源或 `pending_archive` 占位
- [ ] 每张卡 Critique 包含 ≥ 2 个外部反对者或边界案例
- [ ] 每张卡 related ≥ 5，且至少 2 条跨域
- [ ] 欧阳锋终审通过

---

## 六、队列位置

- **入队编号**：`#41`
- **入队位置**：紧跟 `#40 task_20260701_wangyuyan-wobeirushen-pilot-orchestration` 之后
- **状态**：`queued`
- **阻塞依赖**：无（可与 #38-#40 并行）

---

## 七、风险与升级条件

### 7.1 主要风险

| 风险 | 等级 | 缓解措施 |
|:---|:---:|:---|
| 与现有卡重叠 | 中 | 先升级现有卡，避免两张薄卡并存；新卡必须显式桥接 |
| 升级后现有卡 status 变化 | 中 | 升级任务完成后由欧阳锋重新 review，status 从 reviewed 改为 reviewed（新日期）或 enriched→reviewed |
| 素材来源为二手整理 | 低 | 来源为一堂内部课程，已在 KDO 中建立信任；但仍需标注 `trust_level: medium` |

### 7.2 扩量条件

1. 首批 3 张卡通过欧阳锋终审
2. 用户确认认可质量
3. 再评估是否新建双环矩阵、双峰哲学、四象限等工具卡

---

*王语嫣 2026-07-01*
