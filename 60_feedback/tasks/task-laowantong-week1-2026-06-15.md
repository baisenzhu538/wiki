# 老顽童第一周任务（2026-06-15）

> 来源：30_wiki 全库深度审查阶段 0–6  
> 协调人：王语嫣  
> 优先级：P0 优先  
> 需要拍板的问题：见 `needs-user-decision-2026-06-15.md`

---

## 本周总目标

在本周内处理 **yitang 域最影响可信度的 P0 问题**，让 yitang 域 P0 卡片数从约 200 降到 100 以下。

---

## 任务一：OCR 卡片校对或确认删除（3 人日）

### 需要你处理的 5 张优先级最高 OCR 卡

| 文件 | 问题 | 建议动作 |
|---|---|---|
| `concepts/ocr-一堂-科学决策-深度-l4严格财务公式.md` | 公式未闭合、变量未定义、OCR 断裂 | 对照原图校对，补全变量；如无法校对则改为 draft/low trust |
| `concepts/ocr-泛产品设计-审美工具箱指南.md` | 乱码严重（"豆屏""江信合场景"等） | 对照原图校对，重建操作步骤；如无法校对则降级 |
| `concepts/ocr-一堂-地图-个人地图_conv.md` | OCR 未检测到文本，内容几乎为空 | 如原图确实无文字，删除或改为 source 占位卡 |
| `concepts/ocr-一堂-泛产品设计-十年苦练30招.md` | 表格错位、30 招练习标准缺失 | 重建 30 招能力矩阵；如无法完成则降级 |
| `concepts/ocr-一堂-泛产品设计-需求工具箱指南.md` | 乱码、13 张卡片编号混乱 | 重建 13 张卡片列表与使用场景 |

### 执行标准

- 能校对完成的：更新正文、补充 source、将 status 从 draft 提升到 enriched，trust_level 根据质量设为 medium/medium-high
- 无法校对的：保持 draft，trust_level=low，confidence=0.6，在卡片顶部加 `> ⚠️ 本卡为未校对 OCR，内容可靠性低`
- 确定无价值的：直接删除文件，并在看板中记录

### 完成后请做

1. 更新卡片 frontmatter
2. 在看板 `kcard-issues-board-2026-06-15.md` 对应项打勾或删除
3. 告知王语嫣哪些卡删除了，哪些降级了

---

## 任务二：重写 yitang 三张核心工具卡（2–3 人日）

### 目标卡片

| 文件 | 当前问题 | 目标 |
|---|---|---|
| `concepts/yt-entrepreneur-five-step-method.md` | 仅复述五步法名称，缺步骤/工具/判断标准 | 达到 tool/framework 标准：有适用范围、每一步的操作动作、检查清单、失败模式 |
| `concepts/yt-entrepreneur-unit-model.md` | Bill Aulet 批判缺失、操作步骤不突出 | 补全 Bill Aulet 批判，补充单元模型具体操作步骤/模板 |
| `concepts/yt-entrepreneur-259-milestone.md` | 未列出 9 个里程碑具体内容 | 列出 9 个里程碑定义、每个里程碑的进入/退出标准、示例 |

### 执行标准

- 每张卡至少包含：
  - **一句话定义**（这是什么东西）
  - **适用场景**（何时用）
  - **操作步骤**（每一步做什么）
  - **检查清单**（怎么算做对）
  - **失败模式**（常见错误）
  - **至少 1 个案例或示例**
  - **source_refs 精确到具体课程材料或口述行号**
- 完成后 status 设为 `enriched`，trust_level 根据来源设为 medium-high 或 high

### 需要拍板的问题

- `yt-entrepreneur-five-step-method` 的 type 现在是 `tool`，但内容更像 `framework`。是改为 `framework` 还是保持 `tool`？（王语嫣建议：改为 `framework`，因为五步法是一套方法论，不是单一工具）
- `yt-entrepreneur-unit-model` 中 Bill Aulet 批判被截断为 "..."，是删除这段还是补充完整？（王语嫣建议：补充完整，或删除未完成的批判段落）

---

## 任务三：yitang 域 enriched/reviewed/stable 卡补充 source（剩余时间）

### 目标

为 yitang 域约 200 张 `enriched/reviewed/stable` 但 `source_refs` 仅指向"课程地图精华串讲"的卡片，补充更精确的 source。

### 执行标准

- 把 `source_refs` 从 `"一堂-课程地图精华串讲.md"` 改为具体课程逐字稿/口述文件
- 如可能，补充行号范围
- 不用重写正文，只需修正 source 引用
- 完成后 trust_level 可酌情提升

### 优先级顺序

1. `frameworks/yt-*.md`
2. `tools/yt-*.md`
3. `concepts/yt-*.md`（非 OCR）
4. `cases/yt-*.md` / `case-truman-*.md`

---

## 本周交付物

1. 5 张 OCR 卡的处理结果（校对/降级/删除）
2. 3 张核心工具卡的重写版本
3. 至少 30 张 yitang 卡的 source 补充
4. 更新后的问题看板状态

---

## 有问题找王语嫣

- 不确定某张卡是否该删除 → 王语嫣
- source 找不到原始材料 → 王语嫣汇总给用户
- 与黄药师的工作有重叠 → 王语嫣协调
- 需要用户拍板 → 王语嫣汇总方案
