---
title: "黄药师狗粮笔记：AI学习域全管线走通体验"
author: "黄药师"
date: "2026-05-24"
task_ref: "70_product/tasks/task-20260524-huangyaoshi-ai-study-dogfood.md"
---

# 黄药师狗粮笔记：AI学习域全管线走通体验

## 管线执行总结

素材：3份口述稿（~480KB总计）+ 1份书摘 + 11张PNG知识图 + 1份AI Native框架文稿
产出：2张enriched wiki卡 + 2篇完整文章（~1800+1900 words），通过validate质量门
耗时：约3小时（含调试和绕路时间）

---

## 哪个步骤最痛苦？

### 1. `kdo clean-transcript` —— 几乎无效（最痛）

三份口述稿总共约480KB，运行clean-transcript后只减少了2-3%的行数。内容几乎原样保留。

**根因**：clean-transcript的正则规则是针对**讲座式**语音识别稿设计的（去"嗯啊"、去重复句首），但这三份素材是**直播互动式**口述——有观众打招呼、有"评论区同学你好"、有跑题闲聊、有互动问答。正则无法区分"有价值的口语化表达"和"无价值的社交噪音"。

**体感**：跑了命令，等了几秒，看到输出几乎没变化——第一反应是"这东西到底有没有跑？"。最后我直接放弃清理稿，用原始稿继续走后续流程。

### 2. `kdo ocr`（MinerU）—— 完全失败

三张关键知识图（FeatureSet/提问进化路线图/提问工程化）用 `kdo ocr` 调用MinerU，全部返回"parsing failed"。

**根因**：MinerU是为PDF文档设计的解析器，不是为信息图/知识地图设计的。这些PNG是视觉化的框架图，不是有段落文字的文档页面。

**绕路**：切换到PaddleOCR（`ocr-pipeline/ocr-paddle.cjs`），成功提取了文字，但输出很稀疏（3-7行/张），因为图里80%是视觉结构而非文字。

**体感**：`kdo ocr` 的错误信息只说"parsing failed"，没有说"这类图片不适合用MinerU，请尝试PaddleOCR"。新用户会完全不知道该怎么办。

### 3. `kdo ingest` 吃口述稿 —— 产出垃圾标题

三份口述稿ingest后，自动生成的wiki卡片标题是文件首行非空内容——直播开场白。比如"评论区同学们你们有多少人之前认识我或者知道我？"变成了一张wiki卡的标题。

**根因**：ingest的title提取逻辑是`first_non_empty_line`，对结构化markdown（有`# 标题`）很好用，对ASR转录稿完全不适用——因为ASR稿的第一行是说话人开口的第一句话，通常是无意义的寒暄。

**补救**：手动删除3个垃圾source+wiki条目。之前session已经给ingestion.py加了title最小长度和黑名单过滤，但仍然挡不住"看起来是正常句子但实际是垃圾"的情况。

---

## 哪个步骤根本不存在？

### 1. 没有"预标注"步骤

ingest前，我没有任何方式告诉系统"这是一份ASR口述稿，标题应该是X，kind应该是transcript"。只能ingest后手动修复。

**期望**：`kdo ingest --title "AI时代判断力" --kind transcript` 或者一个 `00_inbox/manifest.yaml` 元数据文件，让我在ingest前声明素材属性。

### 2. `kdo produce` 不会从wiki拉内容

`kdo produce content/article --topic "..."` 生成的是一个纯TODO骨架。它知道关联了哪些source_refs，但完全不读wiki卡片内容，也不用source内容填充Draft部分。

**体感**：produce完后，我面对一个全是TODO的文件，所有内容需要100%手写。produce本质上只是`touch`了一个模板文件。如果我每天要做10篇文章，produce这步等于不存在。

**期望**：produce至少能把wiki卡片的Reusable Knowledge预填到Body Structure里，把Source Lineage表自动补好。Draft不需要自动写（那是LLM的活），但结构性信息不该让人手动复制。

### 3. 没有"article→validate"的快捷路径

validate从state.json读artifact元数据。但我在文件frontmatter里已经更新了source_refs和wiki_refs——validator不读文件frontmatter，只读state.json。这意味着我必须同时维护两个地方的数据。

**期望**：validate应该以**文件frontmatter为唯一真相源**，state.json只做缓存/索引用途。或者至少在文件frontmatter和state.json不一致时给warning。

---

## 哪个体感最意外？

### 1. validator的`section_content`有严重regex bug

`section_content(text, "Draft")` 的正则是 `^##\s+Draft\s*\n(.*?)(?=^##|\Z)`。问题：`^##` 不仅匹配 `## Heading`，也匹配 `### Subheading`（因为`###`的前两个字符就是`##`）。

**后果**：一篇有完整1800字内容的文章，validator报"Draft section is empty (0 words)"。因为所有内容都在`### Part 1`/`### Part 2`里，而regex在第一个`###`就停了。

**绕路**：在`## Draft`和第一个`###`之间加一行引导文字（~45 words），让validator至少能检测到"非空"。但word count永远不对。

**严重程度**：P0。这个bug让**所有使用`###`子标题的文章**永远无法通过完整验证。每一篇从produce到validate的content artifact都会命中。

### 2. state.json vs artifact-registry.yaml 双源冗余

artifact的source_refs/wiki_refs同时存在于：
- `.kdo/state.json`（validate读这里）
- `90_control/artifact-registry.yaml`（人工维护）
- 文件自身frontmatter

三个地方可以不一致，validate只看state.json。这是一个"数据分裂"问题——我改了文件frontmatter，以为已经完事，validation照样fail。

### 3. clean-transcript和produce完全不符预期

我作为builder一直在"推理"这些工具应该怎么工作。真正跑一遍发现：
- clean-transcript我以为能把口述稿变得可读——实际几乎无变化
- produce我以为能生成有内容的初稿——实际只是touch了一个模板

这印证了欧阳锋给我这个任务的原因："你靠的是推理而非体感"。推理和体感之间的差距比我以为的大得多。

---

## 如果每天要做10篇文章，先修什么？

按优先级排序：

### P0（不修就完全卡死）

1. **修 `section_content` regex**：改为 `(?=^##\s|\Z)` 或 `(?=^##[^#]|\Z)`——只匹配同级heading，不匹配更深的子heading。不修这个，所有文章validate的word count检查永远无意义。

2. **produce 自动预填结构性信息**：让produce从wiki卡片读Reusable Knowledge填入Body Structure；从state.json填好Source Lineage表；从frontmatter同步wiki_refs。

### P1（不修就效率极低）

3. **ingest支持`--title`和`--kind`参数**：让用户在ingest阶段就能覆盖自动检测的title和kind。对ASR稿、图片、非结构化文本至关重要。

4. **validate以文件frontmatter为准**：消除state.json/registry/frontmatter三源分裂。文件frontmatter是唯一真相源，validate读到不一致时自动同步state.json。

5. **clean-transcript增加"会话式"规则集**：当前规则只适用于讲座稿。需要增加：去直播互动噪音、去观众问答、去跑题闲聊段落。可能需要LLM辅助分段判断而非纯正则。

### P2（不修可以绕路，但磨人）

6. **`kdo ocr` 失败时给出替代方案建议**：当MinerU返回parsing failed时，输出"此图片可能不适合文档解析，请尝试 PaddleOCR: `powershell 40_outputs/.../ocr-image.ps1 <image>`"。

7. **produce→validate快捷循环**：produce完成后自动跑一次validate预检（`--advisory`模式），提前告诉用户哪些字段还没填。省得写完整篇文章后才发现registry没同步。

---

## 一句话总结

管线的"骨架"是完整的——从capture到validate确实可以走通。但每一步之间的**衔接**几乎全靠人脑胶水：ingest后要手动修title，produce后要手动从wiki复制内容，validate前要手动同步state.json。如果把KDO管线比作一条流水线，机器人手臂都在各自的工位上，但工位之间没有传送带——每个半成品都要人手搬运。

下一批基础设施工单的主题应该是：**补传送带**。
