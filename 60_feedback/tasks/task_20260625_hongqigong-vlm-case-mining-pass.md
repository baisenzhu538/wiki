---
id: task_20260625_hongqigong-vlm-case-mining-pass
type: production_task
created_at: 2026-06-25
author: 王语嫣
assignee: 洪七公
priority: P0
---

# 洪七公任务：VLM 二轮知识挖掘提取（case-mining pass）

> 王语嫣铁律：本指令仅写入 `60_feedback/`，不污染 `30_wiki/`。
> 触发来源：`60_feedback/diagnosis/diag_20260625_wangyuyan_vlm-reprocess-intake.md`
> 上游任务：`60_feedback/tasks/task_20260624_hongqigong-ocr-vlm-reprocess.md`

---

## 0. 元信息

| 项目 | 内容 |
|------|------|
| 任务类型 | VLM 二轮提取 / 视觉原料深加工 |
| 输入 | `00_inbox/_vlm_reprocess/` 下已生成的 172 张 VLM 描述及对应原图 |
| 输出 | `00_inbox/_vlm_reprocess/_case_mining/` 下每图对应的 `*_case_mining.md` |
| 优先级 | P0（阻塞单元模型域补完与科学决策域卡片生产） |
| 质量负责人 | 王语嫣 |
| 生产方 | 洪七公 |

---

## 1. 为什么需要二轮提取

王语嫣入口审计发现：

- 一轮 VLM prompt（`describe-images-minimax.py`）只要求「描述图片」，导致输出是**视觉摘要**，不是**可入库的知识原料**。
- 单元模型域尤其吃亏：框架图被压缩成「表格有几行、颜色分区」，丢失了操作细节、失败模式、案例数字、适用边界。
- 科学决策域的 ROI 案例、深度 L1-L4 案例，VLM 只描述了「这是一张 ROI 分析表」，没有提取具体数字和决策教训。

因此需要对 **单元模型 35 张 + 科学决策 35 张** 做二轮提取，prompt 从「看图说话」升级为「知识挖掘」。

---

## 2. 处理范围

### 2.1 必做（P0）：单元模型 + 科学决策

| 域 | 图片数 | 输入目录 | 输出目录 |
|:---|:---:|:---|:---|
| 单元模型 | 35 | `00_inbox/_vlm_reprocess/单元模型/` | `00_inbox/_vlm_reprocess/_case_mining/单元模型/` |
| 科学决策 | 35 | `00_inbox/_vlm_reprocess/科学决策/` | `00_inbox/_vlm_reprocess/_case_mining/科学决策/` |

### 2.2 选做（P1/P2）：泛产品设计 + 个人修炼 + 其他

| 域 | 图片数 | 处理建议 |
|:---|:---:|:---|
| 泛产品设计 | 35 | 只做「用户卡片」「落地卡片」「审美卡片」中的高价值图；课程清单类跳过 |
| 个人修炼 | 15 | 重点做「双三角模型」「MUSE 模型」「科学学习 IPO」「表达力火箭模型」 |
| 其他 | 52 | 重点做「婚礼操盘/婚礼规划」「地图类关键节点」「十大单元模型」；找不到原图的 12 张跳过 |

---

## 3. 新的 VLM Prompt（case-mining 版）

建议另存脚本或临时修改 `describe-images-minimax.py` 的 `SYSTEM_PROMPT`。

```text
你是一位商业知识库整理专家。这张图片来自一堂商业课程，是课件截图/框架图/案例图。
请不仅描述图片内容，更要挖掘其中可独立成卡片的商业知识。

请按以下 JSON 格式输出：
{
  "knowledge_type": "framework | tool | concept | case | dk | skip",
  "title": "图片表达的核心标题",
  "one_sentence_definition": "一句话定义",
  "when_to_use": ["适用场景1", "适用场景2"],
  "when_not_to_use": ["不适用场景1"],
  "procedure": ["步骤1", "步骤2", "步骤3"],
  "failure_modes": [
    {"mode": "失败模式名称", "symptom": "表现", "fix": "纠偏动作"}
  ],
  "key_numbers_and_cases": [
    {"claim": "具体数字/案例", "number": "数字", "context": "上下文"}
  ],
  "relations": ["与XX框架的关系"],
  "transferable_scenarios": ["可迁移场景1"],
  "dark_knowledge": "反直觉点或讲师随口说的心法",
  "confidence": 0.85,
  "source_note": "原图文件名"
}

要求：
1. 如果图片只是目录/课程清单/大地图，没有独立框架价值，knowledge_type 填 skip。
2. 如果图片是案例，必须提取具体数字、时间线、决策点、教训。
3. 如果图片是框架/工具，必须提取操作步骤和至少 3 条失败模式。
4. 如果图片含讲师操作心法/判断口诀/失败教训，knowledge_type 填 dk。
5. 所有数字必须保留原图口径；不确定时标注 [conf=low]。
```

---

## 4. 输出格式

每个输出文件：`00_inbox/_vlm_reprocess/_case_mining/<域>/<原图stem>_case_mining.md`

内容模板：

```markdown
# Case Mining：一堂-单元模型-找全成本实操难点

**原图**: `...`
**上游 VLM 描述**: `00_inbox/_vlm_reprocess/单元模型/一堂-单元模型-找全成本实操难点_vlm_desc.md`
**模型**: MiniMax-M3

## 知识类型
dk

## 一句话定义
...

## 适用条件 / 不适用条件
...

## 操作步骤 / 使用流程
...

## 失败模式
...

## 关键数字与案例
...

## 与其他知识的关系
...

## 可迁移场景
...

## 暗知识 / 反直觉点
...

## 置信度
0.78
```

---

## 5. 质量门禁

每张输出文件自查：

- [ ] `knowledge_type` 已判断（framework / tool / concept / case / dk / skip）
- [ ] 非 skip 的图有 `one_sentence_definition`
- [ ] framework/tool/concept 有 ≥3 条失败模式或边界
- [ ] case 有具体数字或时间线
- [ ] dk 有反直觉点和行动建议
- [ ] 所有数字有来源或不确定标注
- [ ] 输出目录与输入目录一一对应

---

## 6. 与王语嫣/老顽童的交接

- 洪七公完成二轮提取后，更新 `00_inbox/_vlm_reprocess/_case_mining/README-案例挖掘汇总.md`。
- 王语嫣对 `_case_mining/` 输出做 20% 抽样验收，重点检查 case 数字与 dk 反直觉点。
- 验收通过后，王语嫣输出卡片生产任务给老顽童，明确「新建 / enrich / 跳过」清单。

---

## 7. 注意事项

1. **不要修改 `00_inbox/_vlm_reprocess/` 下一轮已有输出**，二轮输出放在新目录 `_case_mining/`。
2. **找不到原图的 12 张其他域图片直接跳过**，在 README 中标记为「原图缺失」。
3. **如果某张图二轮输出仍为视觉描述而非知识挖掘，需要重跑 prompt 或人工补充**。
4. **单元模型域必须 35/35 全部完成**，这是当前用户最关注的缺口。

---

*任务下达：王语嫣 | 日期：2026-06-25*
