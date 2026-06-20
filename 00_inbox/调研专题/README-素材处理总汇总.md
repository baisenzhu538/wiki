# 📊 调研专题 — 素材处理汇总

> 处理时间: 2026-06-20 | 引擎: MiniMax M3 (VLM) + pymupdf (PDF) | 调用者: 洪七公（北丐）

---

## 一、整体概况

| 素材类型 | 数量 | 处理方式 | 产出 | 状态 |
|:--|:--:|:--|:--|:--:|
| 🖼️ PNG 图片 | 48 | MiniMax M3 VLM 结构化描述 | `_vlm_desc.md` × 48 | ✅ 全成功 |
| 📄 PDF 文档 | 3 | pymupdf 文字提取 | `_ocr.md` × 3 | ✅ 125页/11.2万字 |
| 📝 TXT 文本 | 18 | 元数据统计 | `_meta.md` × 18 | ✅ 46.7万字 |
| 📄 DOCX 文档 | 1 | python-docx | `_ocr.md` × 1 | ✅ 7.9万字 |
| 📦 ZIP 压缩包 | 2 | 解压 | `_extracted/` 目录 | ✅ 含调研 skill |

---

## 二、🖼️ VLM 图片描述（48张）

**模型**: MiniMax-M3 | **成功率**: 48/48 (100%) | **详情**: [README-VLM描述汇总.md](README-VLM描述汇总.md)

### 高价值图片（confidence ≥ 0.90）

| 图片 | 类型 | 标题 | 置信度 |
|:--|:--|:--|:--:|
| 调研黑客OSCAR模型.png | 框架图 | OSCAR 调研黑客五步法 | 0.95 |
| 调研全景策略图.png | 信息图 | 商业调研全景策略图 | 0.95 |
| 调研超级武器库.png | 信息图 | 调研武器库全景 | 0.95 |
| 系统调研AI教练背后.png | 框架图 | 系统调研 AI 教练底层逻辑 | 0.95 |
| 理想调研三原则.png | 信息图 | 理想调研三原则 | 0.95 |
| AI调研报告价值层级.png | 信息图 | AI调研报告价值层级 | 0.95 |
| 一堂AI调研parter双三角模型.png | 框架图 | 系统式调研Partner探索 | 0.92 |
| 提升AI调研能力的10条关键假设.png | 框架图 | 10条关键假设 | 0.92 |
| 调研雷达图.png | 信息图 | 调研能力雷达图 | 0.94 |
| 调研手段卡 × 8 | 教学示意图 | 各行业调研手段卡 | 0.92-0.95 |

### 低置信度图片（需人工复核）

| 图片 | 置信度 | 可能原因 |
|:--|:--:|:--|
| 一堂DOC-20260406015121~15150 | 0.3 | 纯文字/截图，无视觉结构 |
| 一堂DOC-20260406015307 | 0.3 | 同上 |

---

## 三、📄 PDF 文本提取（3份）

**引擎**: pymupdf | **总页数**: 125 | **总字数**: ~11.2万

| PDF 文件 | 页数 | 字数 | 产出文件 |
|:--|:--:|:--:|:--|
| AI组织研究对话记录开源（Truman）.pdf | 57 | 45,074 | `AI组织研究对话记录开源（Truman）_ocr.md` |
| 一堂网页调研记录（Truman）.pdf | 36 | 31,846 | `一堂网页调研记录（Truman）_ocr.md` |
| 技能Partner对话记录(Truman).pdf | 32 | 35,324 | `技能Partner对话记录(Truman)_ocr.md` |

---

## 四、📝 TXT 文本元数据（5份）

| TXT 文件 | 行数 | 字数 | 类型 |
|:--|:--:|:--:|:--|
| 高阶调研行动营01.txt | 1,848 | 79,815 | 课程口述 |
| 一堂-调研行动营启动_原文润色.txt | 3,697 | 72,323 | 课程口述 |
| 一堂-调研武器库课程_原文润色.txt | 2,487 | 47,104 | 课程口述 |
| 一堂-上市公司报告解读-口述.txt | 1,107 | 19,599 | 课程口述 |
| 一堂-上市公司报告解读-笔记.txt | 187 | 4,250 | 笔记 |
| **合计** | **9,326** | **223,091** | |

---

## 五、📦 ZIP 解压内容

### business-research-skill_extracted/
> Claude skill 文件 — 商业调研方法论

```
SKILL.md                               # 技能定义
references/
  ├── research-principles.md           # 调研原则
  ├── analysis-frameworks.md           # 分析框架
  ├── weapon-action-templates.md       # 武器行动模板
  ├── databases-index.md               # 数据库索引
  ├── ci-platforms.md                  # 竞品情报平台
  ├── market-sizing.md                 # 市场测算
  ├── report-guide.md                  # 报告指南
  ├── ach-methodology.md               # ACH方法论
  ├── bias-checklist.md                # 偏见检查清单
  └── style-guide.md                   # 风格指南
templates/
  ├── fact-card.md                     # 事实卡片模板
  ├── report-structure.md              # 报告结构模板
  └── weapon-checklist.md              # 武器检查清单
```

### deep-research_extracted/
> Claude skill 文件 — 深度调研方法论

```
SKILL.md
assets/
  └── 示例报告-智能电动车市场深度调研.md
references/
  ├── 01-5W2H分析框架.md
  ├── 02-五步搜索法.md
  ├── 03-10维度竞品分析.md
  ├── 04-市场分析框架.md
  └── 05-洞察提炼与报告撰写.md
```

---

## 六、后续建议

1. **图片 OCR 补充**: 当前仅完成 VLM 结构描述，如需逐字提取图中文字，可补跑 `batch-paddleocr-js`
2. **低置信度图片**: 4 张 confidence=0.3 的图片建议人工命名或单独处理
3. **PDF 深度分析**: 3 份 PDF 对话记录含丰富调研案例，可做摘要提取
4. **ZIP Skill 集成**: `business-research-skill` 和 `deep-research` 可提炼为 Hermes 技能
5. **TXT 结构化**: 5 份课程口述可进一步分章节、提取金句、生成知识卡片

---

*生成: 洪七公 · 北丐多模态渲染管线 · 2026-06-20*
