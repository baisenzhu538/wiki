---
id: domain-xiang-jiang-deep-digestion
title: "讲香域深度消化 + 架构重建"
status: active
priority: P0
assigned_to: 黄药师
architect: 欧阳锋
domain: personal
created: 2026-05-13
updated: 2026-05-13
---

---

## ⚠️ 前置任务

完成 [[calibration-understanding-gate-motivation-peakend]]（理解门禁校准）后，再启动本任务。校准任务用两张旧卡建立理解深度标尺。

---

## 三方讨论裁决 (2026-05-13 欧阳锋)

### 黄药师建议书概览

见 [[new-course-讲香十指模型-消化建议书]]。核心结论：

- **旧卡框架错误已确认**：`yt-personal-sales-pitch-model` 的十指模型（价值构建/表达设计）与口述稿（向下具象/向上抽象）完全不同，需重写而非修补
- **推荐方案 B**：1 framework + 10 tool 卡，参照 panproduct 拆分先例
- **五阶段执行**：OCR → 归档 → 核心卡片 → 关联更新 → 质量门禁

### 欧阳锋独立裁决

**一致认同部分：**

1. ✅ 框架错误诊断正确——系统性重写，非补充更新
2. ✅ 方案 B 方向正确——单卡无法承载 40 子策略 + 100+ 案例的密度
3. ✅ 四层修炼路径中的"基础→进阶→增强→奇效"是天然的拆分依据

**补充/修正部分：**

4. **"超级武器库"需独立成卡**。黄药师将其仅视为速查表，但我判断它是一个跨域元概念——调研武器库、表达力执行武器库、讲香超级武器库共享相同结构特征（即查即用、实战验证、自由排列组合的战术集合）。需新建 `yt-concept-weapon-arsenal.md`（concept 类型），不附属于讲香域。

5. **拆分分两批交付**，不是一次性 11 张卡。依据课程自身的四层路径：

| 批次 | 手指 | 卡片数 |
|------|------|:----:|
| Batch 1 | 场景化 + 比喻化（基础）+ 口语化 + 金句化（进阶） | 4 tool |
| Batch 2 | 数字化 + 情绪化（增强）+ 故事化 + 素材化 + 冲突化 + 升华化（奇效） | 6 tool |

6. **关联域需补充三张卡**的 related 边：

| 卡片 | 需补的 related 指向 |
|------|-------------------|
| `yt-panproduct-execution-low-cost-mvp` | 讲香 framework（十指是泛产品落地的表达工具） |
| `yt-model-ipo-learning-strategy` | 讲香 framework（讲香属 IPO 输出环节 L4-L5） |
| `yt-composite-pan-product-methodology` | 讲香 framework（泛产品设计的表达维度） |

7. **Phase 0（OCR）立即执行**，不等后续讨论。OCR 提取的文字是后续卡片建设的原材料。

### 最终裁决

| 决策项 | 裁决 |
|--------|------|
| 架构方案 | **方案 B**：1 framework + 10 tool，分两批交付 |
| 武器库元概念 | **新增** `yt-concept-weapon-arsenal.md`（concept 类型，跨域） |
| 旧卡处置 | **重写** `yt-personal-sales-pitch-model` 为 framework 卡，保留旧 Constraints 三条约 |
| 关联域扩展 | 补充 panproduct execution、IPO、泛产品方法论三张卡 |
| 命名规范 | `yt-model-personal-pitch-toolkit`（framework）+ `yt-pitch-{strategy-en}`（tool），照黄药师提议 |
| OCR | **立即执行**，进入 Phase 0 |

---

## Phase 0：OCR 提取（立即执行，不等批）

```
处理四张图：
- 00_inbox/一堂-个人修炼-讲香十指模型-超级武器库.png → OCR
- 00_inbox/一堂-个人修炼-讲香基本功-十指模型修炼地图.png → OCR
- 00_inbox/一堂-个人修炼-表达力火箭模型.png → OCR
- 00_inbox/一堂-个人修炼-表达力火箭模型-执行武器库.png → OCR
```

命令参考：
```powershell
# 逐张提取
node C:\Users\Administrator\ocr-pipeline\ocr-paddle.cjs "C:\Users\Administrator\Desktop\wiki\00_inbox\一堂-个人修炼-讲香十指模型-超级武器库.png"
node C:\Users\Administrator\ocr-pipeline\ocr-paddle.cjs "C:\Users\Administrator\Desktop\wiki\00_inbox\一堂-个人修炼-讲香基本功-十指模型修炼地图.png"
node C:\Users\Administrator\ocr-pipeline\ocr-paddle.cjs "C:\Users\Administrator\Desktop\wiki\00_inbox\一堂-个人修炼-表达力火箭模型.png"
node C:\Users\Administrator\ocr-pipeline\ocr-paddle.cjs "C:\Users\Administrator\Desktop\wiki\00_inbox\一堂-个人修炼-表达力火箭模型-执行武器库.png"
```

产出：4 个 `*_paddle_ocr.txt` 文件在图片同目录。

---

## Phase 1：文件归档 + 武器库概念卡

### 1a. kdo ingest

```bash
# 口述版归档
kdo ingest --kind source "00_inbox/一堂-个人修炼-讲香十指模型口述版.txt"
```

### 1b. 图片归档

```
00_inbox/*.png + *.webp → 10_raw/assets/yitang/
```

### 1c. 新建武器库元概念卡

```yaml
id: yt-concept-weapon-arsenal
title: 超级武器库（元概念）
type: concept
domain: master
```

Claims 至少覆盖：
- 武器库的定义特征（即查即用、实战验证、排列组合）
- 武器库 vs 框架（framework）vs 工具箱（toolkit）的区分
- 跨域实例列举（讲香、表达、调研、需求）
- 构建武器库的方法论（从"学一个方法"到"建一个武器库"）

### 1d. 验证

```bash
grep -r '"00_inbox' 30_wiki/concepts/yt-*.md  # → 空
```

---

## Phase 2：核心卡片建设（Batch 1）

### 2a. Framework 卡

重写 `yt-personal-sales-pitch-model.md` 为 framework 卡：

```yaml
id: yt-model-personal-pitch-toolkit
title: 十指讲香模型（框架）
type: framework
domain: personal
prerequisites:
  - yt-model-ipo-learning-strategy
component_of:
  - yt-model-personal-map
related:
  - yt-personal-scientific-expression
  - yt-concept-weapon-arsenal
  - yt-panproduct-execution-low-cost-mvp
```

Claims 覆盖：
- 核心问题：价值 vs 价值感
- 双手框架：左手具象化（5指）+ 右手抽象化（5指）
- 三大原则：卖点优先、持续修改、先慢后快
- 四层修炼路径
- 与火箭模型的关系（短表达 vs 长表达）
- 与动力阻力模型的关系（讲香服务于动力阻力，卖点找歪全白费）
- 从旧卡迁移三条 Constraints

### 2b. 四张 Tool 卡（Batch 1：基础+进阶层）

| ID | Title | 域 |
|----|-------|-----|
| `yt-pitch-scenarization` | 讲香·场景化 | personal |
| `yt-pitch-colloquialization` | 讲香·口语化 | personal |
| `yt-pitch-metaphor` | 讲香·比喻化 | personal |
| `yt-pitch-aphorism` | 讲香·金句化 | personal |

每张 tool 卡结构：
- `prerequisites: [yt-model-personal-pitch-toolkit]`
- `component_of: [yt-model-personal-pitch-toolkit]`
- Claims：定义 + 4 子策略 + 2-3 精选案例 + 何时不该用这个手指
- Constraints：1-2 条边界条件

### 2c. 更新受影响卡片

| 卡片 | 操作 |
|------|------|
| `yt-personal-sales-pitch-model` (旧) | 已被 2a 重写覆盖 |
| `yt-personal-scientific-expression` | 补充火箭模型两张新图到 source_refs 和 body（如 OCR 提取了有价值文字则追加） |
| `yt-model-personal-map` | `related` 新增 `yt-model-personal-pitch-toolkit` |
| `yt-panproduct-execution-low-cost-mvp` | `related` 新增 `yt-model-personal-pitch-toolkit` |
| `yt-model-ipo-learning-strategy` | `related` 新增 `yt-model-personal-pitch-toolkit` |
| `yt-composite-pan-product-methodology` | `related` 新增 `yt-model-personal-pitch-toolkit` |

---

## Phase 3：Batch 2 + 质量门禁

### 3a. 六张 Tool 卡（Batch 2：增强+奇效层）

| ID | Title |
|----|-------|
| `yt-pitch-quantification` | 讲香·数字化 |
| `yt-pitch-emotionalization` | 讲香·情绪化 |
| `yt-pitch-storytelling` | 讲香·故事化 |
| `yt-pitch-materialization` | 讲香·素材化 |
| `yt-pitch-conflict` | 讲香·冲突化 |
| `yt-pitch-sublimation` | 讲香·升华化 |

### 3b. 格式门禁（机械检测，kdo lint 可自动覆盖）

- [ ] `kdo lint` → 0 errors
- [ ] 所有讲香域新卡 `source_refs` 指向 `10_raw/` 或 `10_raw/assets/yitang/`
- [ ] 所有新卡 `related` 非空
- [ ] `grep '"00_inbox' 30_wiki/concepts/yt-*.md` → 空
- [ ] 旧卡 `yt-personal-sales-pitch-model` 已不复存在（被 framework 卡替换）
- [ ] `yt-concept-weapon-arsenal.md` 的 Claims 覆盖至少 3 个跨域武器库实例

### 3c. 理解门禁（人工抽检，欧阳锋执行）

格式门禁检测不到"搬运 vs 理解"。讲香域 40 子策略 + 100+ 案例，机械加工的危险是每张卡看起来完整，但 Claims 只是复述口述稿表面文字。

**抽检方法**：

1. 欧阳锋从 10 张 tool 卡中**随机抽 2 张**
2. 只读每张卡的 `## Constraints & Boundaries` 节
3. 对每条 constraint 判断：

| 信号 | 通过 | 不通过 |
|------|------|--------|
| **反例具体性** | 写了具体场景 + 解释为什么这个场景不该用这个手指（如"数字化在情感决策场景下触发理性计算，反而降低转化"） | 笼统空洞（"需要结合具体场景灵活运用""不是所有场景都适用"） |
| **案例筛选** | 从口述稿 100+ 案例中挑了最有区分度的（能说明这个手指独特价值的），而非课程里最早出现的 | 案例选择无筛选痕迹，或者数量多但无区分度 |
| **跨域连接** | Synthesis 表连接到 vault 中已有概念（如"口语化"→"逐字稿"，"冲突化"→"动力阻力"），连接有实质说明 | Synthesis 表是泛泛的"相关工具"标签，无实质连接 |

4. **追问环节**：欧阳锋从抽检卡的 Constraints 中挑 1 条反例，问黄药师："这个反例为什么是这个手指的边界，而不是另一个手指的边界？"（如"为什么'数字化削弱感染力'这个反例属于数字化手指而非情绪化手指？"）

5. **判定**：
   - 2 张全通过 → 理解门禁通过，进入 Phase 3d
   - 1 张不通过 → 该卡返工，其余 9 张自检
   - 2 张不通过 → Batch 2 暂停，黄药师重新消化口述稿，48h 后重检

### 3d. 欧阳锋终审

---

## 完成信号

- 讲香域：1 framework + 10 tool + 1 武器库概念卡，全部通过格式门禁 + 理解门禁
- 旧卡已替换
- 关联域的 6 张卡片图边已更新
- 火箭模型两张新图已归档并补充到 `yt-personal-scientific-expression`
- 原文素材全部归档 `10_raw/`
- 欧阳锋终审通过（格式门禁 + 理解门禁均通过）
