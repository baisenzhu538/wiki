# KF-020 判罚： enriched/reviewed 卡 source_refs 指向 00_inbox

> 送审：黄药师
> 判罚人：王语嫣（代欧阳锋）
> 日期：2026-06-17
> 规则依据：《KDO 工业化手册》§六：source_refs 不得指向临时路径。enriched/reviewed 卡的所有 source 必须归档到 `10_raw/sources/`。

---

## 一、判罚结论

**KF-020 违规成立。**

全库扫描发现 **46 张** status 为 enriched 或 reviewed 的卡片，其 `source_refs` 仍指向 `00_inbox/` 临时路径。

这是工业化门禁必须修复的问题，不是可忽略的警告。

---

## 二、对 `yt-decision-depth-ladder` 的具体处理

### 2.1 问题

该卡 `source_refs` 原指向 14 条 `00_inbox/科学决策/` 临时路径，但卡 status 为 enriched。

### 2.2 核查结果

- 13 张图片类 source 已归档至 `10_raw/sources/`，对应 OCR md 文件存在。
- 1 个口述稿 txt（`一堂-科学决策-ROI决策深度实操课口述03.txt`）无单独归档，但内容已包含在 `10_raw/sources/src_20260614_8f80cb0f-一堂-课程地图精华串讲.md` 中。

### 2.3 处理

已将该卡 `source_refs` 全部替换为 `10_raw/sources/` 下的归档文件路径（详见本文件编辑历史）。

### 2.4 判罚

- **status 保持 enriched**，不降级。
- 原因：内容已完成精修，source 实际存在且可归档，只是 frontmatter 路径未更新。
- 修复后质量门禁：`total=1193, p0=0, p1=0, clean=1193, yaml_error=0` ✅

---

## 三、全库扫描结果

### 3.1 违规规模

```text
总违规卡数：46 张
- enriched：24 张
- reviewed：22 张
```

完整列表见附录。

### 3.2 重灾区

| 域 | 张数 | 典型问题 |
|---|---|---|
| 一堂五步法/创业 | ~15 | 早期 case/concept 卡 source 仍指 `00_inbox/һ���岽��/` |
| 决策域 | ~10 | `yt-decision-*`、`yt-foresight-*` 系列 |
| 预判/机会判断 | ~8 | 口述稿 txt + 图片未归档 |
| 产品内核 | ~6 | 早期 reviewed 卡 |
| 单元模型/壁垒 | ~4 | 课程 txt 未归档 |

---

## 四、后续处理方案

### 4.1 处理原则

| 情况 | 处理方式 | 是否降级 |
|---|---|---|
| source 已归档到 `10_raw/sources/` | 修正 frontmatter 路径 | 否 |
| source 未归档，但文件仍在 `00_inbox/` | 先归档到 `10_raw/sources/`，再修正路径 | 否 |
| source 未归档，且原始文件已丢失 | 从 source_refs 中移除该引用；若导致 source_refs 为空，降级为 draft | 是 |
| source 是临时笔记/草稿，无归档价值 | 从 source_refs 中移除 | 视情况 |

### 4.2 建议执行顺序

1. **先修重点卡**：决策域、五步法域的核心框架卡（约 15 张）
2. **再修 case 卡**：早期 reviewed 的 case 卡（约 20 张）
3. **最后修 concept/skill 卡**：其余 11 张

### 4.3 建议负责人

- **黄药师**：主导批量归档和路径替换
- **老顽童**：协助核对 content 与 source 的对应关系
- **王语嫣（代欧阳锋）**：抽检 10 张验证

### 4.4 验收标准

```python
import yaml
from pathlib import Path

violations = []
for p in Path('30_wiki').rglob('*.md'):
    if '_archive' in p.parts or 'raw' in p.parts:
        continue
    text = p.read_text(encoding='utf-8', errors='ignore')
    if not text.startswith('---'):
        continue
    try:
        fm = yaml.safe_load(text.split('---', 2)[1])
    except:
        continue
    if not fm:
        continue
    status = fm.get('status', '')
    src_refs = fm.get('source_refs', [])
    if not isinstance(src_refs, list):
        continue
    inbox_refs = [ref for ref in src_refs if isinstance(ref, str) and '00_inbox' in ref]
    if inbox_refs and status in ['enriched', 'reviewed']:
        violations.append(fm.get('id', p.stem))

print(f'Violations: {len(violations)}')
for v in violations[:20]:
    print(v)
```

目标：**violations = 0**

---

## 五、对黄药师「Y 模型哲学根基——王阳明/矛盾论/实践论三角对照」研究的意见

### 5.1 价值判断

**有价值，但需控制风险。**

Y 模型目前的定位是"科学决策工具"。如果能从哲学层面说明：
- 为什么 Y 模型是"知行合一"的操作化版本
- 为什么"发现矛盾 → 抓主要矛盾 → 实践验证"与 Y 模型的"问题 → 本质 → 方案"同构
- 为什么"实践论"的"实践-认识-再实践"循环是 Y 模型迭代的基础

这可以增强 Y 模型的理论深度和说服力。**但前提是：必须落回工具的使用边界和失败模式，不能变成纯哲学阐释。**

### 5.2 建议产出形式

不要写成长篇论文，建议产出为 **1 张 concept 卡或 1 张 dk 卡**：

- **concept 卡**：`concept-yitang-y-model-philosophical-grounding`
  - 用途：解释 Y 模型的哲学来源，增强理论可信度
  - 内容：王阳明/矛盾论/实践论各自对应 Y 模型的哪个环节 + 一个"哲学根基不是替代品"的边界

- **dk 卡**：`dk-yitang-y-model-philosophy-misuse`
  - 用途：反常识——"懂哲学不等于会用 Y 模型"
  - 内容：哲学给的是思维方向，Y 模型给的是操作步骤；混淆两者会导致"说得对但做不出"

### 5.3 注意事项

| 风险 | 控制方法 |
|---|---|
| 过度哲学化，脱离工具 | 每个哲学观点必须对应 Y 模型的一个具体操作步骤 |
| 来源争议 | 王阳明/矛盾论/实践论是公开经典，可直接引用；但与 Y 模型的"映射关系"是推断，需标注为推断 |
| 与宗教/意识形态混淆 | 只谈方法论，不谈立场 |
| 增量不足 | 如果哲学根基只是"换种说法解释 Y 模型"，则不要单独成卡，合并到 `yt-decision-y-model` 的 Critique 或边界说明中 |

### 5.4 建议步骤

1. 先完成 KF-020 修复（更紧急）
2. 用 web search 收集王阳明"知行合一"、矛盾论"主要矛盾"、实践论"认识论"的核心原文
3. 画出三者的映射表：
   | 哲学概念 | Y 模型环节 | 操作化含义 |
4. 写 1 张 concept 卡，包含：原始表述、深度洞察、使用场景、操作方法、适用边界、失败模式、为什么值钱
5. 王语嫣/欧阳锋 review 后入库

---

## 六、附录：46 张违规卡列表

（原始扫描输出中部分中文路径显示为乱码，不影响 id 识别）

### enriched 卡（24 张）

1. `case-five-step-fake-vs-real-barriers`
2. `case-five-step-growth-first-lever`
3. `case-gudong-tea-shop-foresight`
4. `case-jh-yitang-vs-sqlhelper`
5. `case-truman-ai-partner`
6. `case-truman-motivation-map-12-versions`
7. `case-truman-poker-deck-roi`
8. `case-truman-yitang-foresight`
9. `case-unit-model-gashapon`
10. `case-xiaolong-ecommerce-foresight`
11. `case-zhihu-vs-degetao-network-effect`
12. `case-һ��-���˲���-hypothesis-failure`
13. `case-һ��-����������-hypothesis-validation`
14. `case-�ͺ�-skill-market-problem-validation`
15. `concept-five-step-growth-to-barrier-transition`
16. `skill-�ͺ�-AI�Ի������ĸ���`
17. `yt-foresight-15-char-mantra`
18. `yt-foresight-ab-steady-state`
19. `yt-foresight-addition-subtraction`
20. `yt-foresight-deliverables-four-levels`
21. `yt-foresight-probability-engineering`
22. `yt-foresight-ten-fatal-flaws`
23. `yt-research-osl-framework`
24. `yt-three-dimension-opportunity-matrix`

### reviewed 卡（22 张）

1. `case-milktea-five-step`
2. `case-shampoo-product-kernel`
3. `case-toy-cabinet-barrier`
4. `case-toy-cabinet-business-model`
5. `case-treadmill-demand-analysis`
6. `concept-һ��-hypothesis-driven-business-methodology`
7. `concept-һ��-kernel-iteration`
8. `concept-һ��-kernel-validation`
9. `concept-һ��-key-assumptions`
10. `concept-һ��-product-kernel`
11. `yt-barrier-analysis-cheat-sheet`
12. `yt-customer-acquisition-toolkit`
13. `yt-decision-depth-ladder` ✅ 已修复
14. `yt-demand-analysis-hiking-map`
15. `yt-five-step-common-pitfalls`
16. `yt-five-step-implementation`
17. `yt-five-step-method`
18. `yt-growth-cycle-model`
19. `yt-market-size-estimation`
20. `yt-product-kernel-cultivation`
21. `yt-tool-foresight-canvas`
22. `yt-unit-model-three-tools`

---

## 七、最终裁决

1. **KF-020 违规成立**，46 张 enriched/reviewed 卡 source_refs 指向 `00_inbox/`。
2. **`yt-decision-depth-ladder` 已修复**，status 保持 enriched。
3. **剩余 45 张卡需黄药师批量修复**，按"有归档则替换路径、无归档则先归档或降级"原则处理。
4. **黄药师可继续进行 Y 模型哲学根基研究**，但建议产出为 1 张 concept/dk 卡，并先完成 KF-020 修复。

---

*王语嫣（代欧阳锋）· 2026-06-17*
