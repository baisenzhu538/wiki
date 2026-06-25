---
id: task_20260625_laowantong-vlm-to-cards
type: production_task
created_at: 2026-06-25
author: 王语嫣
assignee: 老顽童
priority: P0
---

# 老顽童任务：基于洪七公 VLM 重提取产出成品卡（王语嫣标注版）

> 王语嫣铁律：本指令仅写入 `60_feedback/`，不污染 `30_wiki/`。老顽童负责按此指令在 `30_wiki/` 生产卡片。
> 触发来源：洪七公已完成全库 172 张 OCR 卡片的 VLM 结构化描述；王语嫣完成独立框架价值标注。
> 标注表：`00_inbox/_vlm_reprocess/_triage/vlm_framework_value_triage.md`
> 上游诊断：`60_feedback/diagnosis/diag_20260625_wangyuyan_vlm-reprocess-intake.md`

---

## 0. 元信息

| 项目 | 内容 |
|------|------|
| 任务类型 | 成品卡生产 |
| 输入 | `00_inbox/_vlm_reprocess/` 下的 VLM 描述 + 对应原图 |
| 输出 | `30_wiki/frameworks/`、`30_wiki/tools/`、`30_wiki/concepts/`、`30_wiki/cases/`、`30_wiki/dk/` |
| 优先级 | P0（单元模型域补完 + 科学决策域建设） |
| 质量负责人 | 王语嫣（CLI） |
| 生产方 | 老顽童 |

---

## 1. 王语嫣价值标注结论

| 动作 | 含义 | 数量 |
|:---|:---|:---:|
| `new-*` | 建议新建 framework / tool / concept 卡 | 约 55 |
| `case` | 建议新建案例卡 | 约 15 |
| `dk` | 建议新建暗知识卡 | 约 10 |
| `enrich` | 建议 enrich 已有 wiki 卡片 | 约 25 |
| `skip` | 课程清单 / 大地图 / 截图 / 原图缺失，暂不入库 | 约 50 |

> 精确清单见 `00_inbox/_vlm_reprocess/_triage/vlm_framework_value_triage.md`

---

## 2. 生产优先级

### 2.1 P0-A：单元模型域（优先第一批）

| 建议动作 | 源文件 | 目标卡片 |
|:---|:---|:---|
| new-tool | `一堂-单元模型-单商圈模型.png` | `tool-单元模型-单商圈` |
| new-tool | `一堂-单元模型-单城市模型.png` | `tool-单元模型-单城市` |
| new-tool | `一堂-单元模型-壁垒预判.png` | `tool-单元模型-壁垒预判` |
| new-framework | `一堂-单元模型-外部对抗地图.png` | `framework-单元模型-外部对抗地图` |
| new-tool | `一堂-单元模型-象限分析法.png` | `tool-单元模型-象限分析法` |
| new-framework | `一堂-单元模型-TCPR底层网络协议.png` | `framework-TCPR底层网络协议` |
| new-concept | `一堂-单元模型-学练用.png` | `concept-单元模型-学练用` |
| new-concept | `一堂-单元模型-最简单元模型.png` | `concept-最简单元模型` |
| dk | `一堂-单元模型-对抗小抄01/02/对抗小抄.png` | `dk-单元模型-对抗小抄`（合并 3 张） |
| dk | `一堂-单元模型-找全成本实操难点.png` | `dk-单元模型-找全成本实操难点` |
| dk | `一堂-单元模型-找单元模型实操难点.png` | `dk-单元模型-找单元模型实操难点` |
| dk | `一堂-单元模型-找基准值实操难点.png` | `dk-单元模型-找基准值实操难点` |
| dk | `一堂-单元模型-规模对抗实操难点.png` | `dk-单元模型-规模对抗实操难点` |
| enrich-case | `一堂-单元模型-扭蛋机案例.png` | `case-unit-model-gashapon` |
| case | `一堂-单元模型-示例01.png` / `示例.png` | `case-单元模型-示例01`、`case-单元模型-示例` |
| enrich | `一堂-单元模型-单sku/单客户/单履约/单柜子/单用户/单订单/单销售/单门店.png` | `yt-unit-model-overview` |
| enrich | `一堂-单元模型-基准值.png` | `yt-tool-unit-model-benchmark` |
| enrich | `一堂-单元模型-多模型情况.png` | `yt-tool-unit-model-selection` |
| enrich | `一堂-单元模型-斧子、尺子、梯子.png` / `斧子尺子梯子详解.png` | `yt-unit-model-three-tools` |
| enrich | `一堂-单元模型-段位专家.png` | `yt-unit-model-ladder` |
| enrich | `一堂-单元模型-动态预测.png` | `yt-tool-unit-model-dynamic` |
| enrich | `一堂-单元模型-规模经济对抗武器库.png` | `yt-scale-economy-weapon-library` |
| enrich | `一堂-单元模型-ABCD策略模型.png` | `yt-assumption-abcd-model` |

### 2.2 P0-B：科学决策域（优先第二批）

| 建议动作 | 源文件 | 目标卡片 |
|:---|:---|:---|
| new-tool | `一堂-科学决策-ROI决策评估画布.png` | `tool-ROI决策评估画布` |
| new-tool | `一堂-科学决策-关键训练清单（重要））.png` | `tool-科学决策关键训练清单` |
| new-framework | `一堂-科学决策-决策三角形.png` | `framework-科学决策三角形` |
| new-framework | `一堂-科学决策-高水平共识曲线（重要）.png` | `framework-高水平共识曲线` |
| new-tool | `一堂-科学决策-商业模式-完整财务公式决策.png` | `tool-完整财务公式决策` |
| new-tool | `一堂-科学决策-稀缺资源清单.png` | `tool-稀缺资源清单` |
| new-tool | `一堂-科学决策-项目方案评估三角形.png` | `tool-项目方案评估三角形` |
| new-tool | `一堂-科学决策-深度-L1优先级定性.png` | `tool-决策深度-L1优先级定性` |
| new-tool | `一堂-科学决策-深度-L2部分定量.png` | `tool-决策深度-L2部分定量` |
| new-tool | `一堂-科学决策-深度-L3定量公式.png` | `tool-决策深度-L3定量公式` |
| new-tool | `一堂-科学决策-深度-L4严格财务公式.png` | `tool-决策深度-L4严格财务公式` |
| new-concept | `一堂-科学决策-X型Y型决策习惯对比.png` | `concept-X型Y型决策习惯` |
| new-concept | `一堂-科学决策-发现决策.png` | `concept-发现决策` |
| new-concept | `一堂-科学决策-宽度-个人/企业/团队.png` | `concept-科学决策宽度-个人/企业/团队`（可合并为 1 张） |
| new-concept | `一堂-科学决策-稀缺机会窗口.png` | `concept-稀缺机会窗口` |
| new-concept | `一堂-科学决策-高度-两种典型的思考习惯.png` | `concept-两种典型思考习惯` |
| new-concept | `一堂-科学决策-人机协作决策.png` | `concept-AI时代双三角竞争力` |
| case × 11 | `一堂-科学决策-深度-案例01~06.png`、`ROI决策评估画布-案例01~04.png`、`深度-L4-案例01.png` | 每张独立 case 卡 |
| dk × 2 | `一堂-科学决策-深度-你的业务是一次抽样实验.png`、`深度-决策经验值.png` | `dk-你的业务是一次抽样实验`、`dk-决策经验值` |
| enrich | `一堂-科学决策-关键假设ABCD模型.png` | `yt-assumption-abcd-model` |

### 2.3 P1：泛产品设计 + 个人修炼 + 其他（第三批）

泛产品设计 35 张中，王语嫣标注为 `new-*` 的约 30 张，建议按「用户卡片 / 落地卡片 / 审美卡片」分组批量生产。

个人修炼 15 张中，标注为 `new-*` 的约 9 张，重点生产：
- `concept-AI时代双三角竞争力`
- `tool-提问刻意练习画布`
- `tool-科学学习IPO完整清单`
- `tool-科学提问刻意练习`
- `tool-讲香十指模型-超级武器库`
- `tool-讲香基本功-十指模型`
- `concept-思考深度分级`

其他域重点生产：
- `framework-问题边界与Problem澄清五层结构`
- `framework-个人成长五步法`
- `framework-TCPR皇冠模型`
- `tool-Y模型STEPS策略集`
- `tool-Y模型实操工作流`
- `case-婚礼操盘-用户和场景`、`case-婚礼规划`

---

## 3. 统一生产要求

### 3.1 原料使用规范

老顽童**不能只读 VLM 描述**，必须：
1. 查看原图（`00_inbox/_vlm_reprocess/_batch_<域>/` 或 `_temp_<域>/`）
2. 读取对应 `*_vlm_desc.md`
3. 如有 OCR 文本（`30_wiki/raw/ocr/`），一并参考
4. 对比已有 wiki 卡片，避免重复

### 3.2 案例卡专项：叙事段落扫描（案例挖掘）

按王语嫣最新入口审计规则，**每张 case 卡生产前必须先做叙事段落扫描**：

1. 在原图 / OCR 文本 / VLM 描述中，找出所有 ≥200 字的连续叙事段落。
2. 按完整度 1-5 评分：
   - 5 分 = 有背景 / 冲突 / 决策 / 结果 / 教训五要素
   - 4 分 = 缺一个要素但故事完整
   - ≤3 分 = 暂不立项为独立 case 卡，可并入其他卡作为案例映射
3. **只有 ≥4 分的段落才能立项为独立 case 卡**。
4. 若叙事段落中含讲师随口说的操作心法 / 失败模式 / 判断口诀，额外标注为 `case + dk` 候选。

**输出要求**：在 case 卡正文开头加入「案例来源」节，说明：
- 原图位置
- 叙事段落位置（OCR 行号 / 图片区域）
- 完整度评分
- 为什么值得独立成卡

### 3.3 每张卡必须做 9 层深挖

1. 一句话定义
2. 为什么重要（3 个理由）
3. 核心机制 / 结构
4. 边界与反例
5. 失败模式（≥3 条）
6. 与已有框架的关系
7. 可迁移场景
8. 行动 checklist
9. Critique（至少 2 个攻击者视角）

案例卡 9 层：
1. 核心洞察
2. 事迹/背景
3. 关键数字（带 conf/source）
4. 关键证据表
5. 失败/成功原因
6. 对立面/争议
7. 可迁移场景
8. 教训与预警信号
9. 与王欢/一堂框架的映射

### 3.4 Frontmatter 规范

```yaml
---
id: tool-单元模型-单商圈
title: 单元模型：单商圈模型
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.78
trust_level: medium
language: zh-CN
domain:
- yitang
- decision-science
source_refs:
- 00_inbox/_vlm_reprocess/单元模型/一堂-单元模型-单商圈模型_vlm_desc.md
- 00_inbox/_vlm_reprocess/_batch_单元模型/一堂-单元模型-单商圈模型.png
- 30_wiki/raw/ocr/<对应ocr卡>.md  # 如有
related:
- "[[yt-unit-model-overview]]"
- "[[yt-unit-model-ladder]]"
- "[[yt-tool-unit-model-selection]]"
- "[[ai-collaboration-domain-digest]]"  # 至少 1 条跨域
---
```

### 3.5 可信度标注

- 王欢/一堂原创方法论：`[conf=0.70, source=王欢原创]`
- 图中具体数字：`[conf=0.80, source=原图/ VLM 描述]`
- 外部学术概念：`[conf=0.85, source=...]`
- 案例数字：`[conf=0.80, source=原图]`

### 3.6 防重复 checklist

生产前必须搜索 wiki：

```bash
# 示例：检查是否已有单商圈模型
grep -r "单商圈" 30_wiki/ --include="*.md"
```

如果已有对应卡片，改为 `enrich` 而不是新建。

---

## 4. 质量门禁

每张卡完成后自查：

- [ ] `id` 与文件名一致
- [ ] `status` = `enriched`
- [ ] `author` = `老顽童`
- [ ] `reviewed_by` = `欧阳锋`
- [ ] `source_refs` 包含 VLM 描述文件 + 原图路径
- [ ] `related` ≥ 5，至少 1 条跨域
- [ ] 每个关键声明有 `conf/source` 标注
- [ ] 失败模式 ≥ 3 条（framework/tool/concept/dk）
- [ ] 案例卡已做叙事段落扫描，完整度 ≥4 分
- [ ] 案例卡有具体数字和证据表
- [ ] 无死链
- [ ] 不是已有卡片的简单重复

---

## 5. 验收方式

- 每完成一个 P0 批次（A 或 B），通知王语嫣做 20% 抽样六层交叉验证。
- 发现 ≥2 张不合格 → 整批退回。
- 验收通过后进入下一批次。

---

## 6. 第一批执行顺序建议

单元模型域建议顺序（由浅入深）：

1. `tool-单元模型-单商圈`
2. `tool-单元模型-单城市`
3. `tool-单元模型-象限分析法`
4. `framework-单元模型-外部对抗地图`
5. `tool-单元模型-壁垒预判`
6. `framework-TCPR底层网络协议`
7. `dk-单元模型-找全成本实操难点`
8. `dk-单元模型-找单元模型实操难点`
9. `dk-单元模型-找基准值实操难点`
10. `dk-单元模型-规模对抗实操难点`
11. `dk-单元模型-对抗小抄`
12. `concept-单元模型-学练用`
13. `concept-最简单元模型`
14. `case-unit-model-gashapon`（enrich）
15. `yt-unit-model-overview`（enrich 单*系列）

---

*任务下达：王语嫣 | 日期：2026-06-25*
