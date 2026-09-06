---
id: task_20260906_hongqigong-datapack-vision
title: "DataPack 试点一：识图金标准库（金标准样本+踩坑案例+置信对照，洪七公整理弹药）"
seq: 660
status: queued
assignee: hongqigong
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 老朱 09-06 点名（洪七公把识图整个工作流的踩坑案例、金标准封装成 datapack）
reviewer: 欧阳锋
instance: hongqigong
updated_at: '2026-09-06T12:50:00+08:00'
---

# #660 DataPack 试点一：识图金标准库（洪七公）

## 规格
`40_outputs/capabilities/datapacks/hongqigong-vision-goldstandard/`（规范见该目录 README）：
1. **金标准样本**：≥5 组「原图→正确 OCR/VLM 输出」对照（含今天的 AI组织行为学 PDF 三源校勘案例——现成首件）
2. **踩坑实录**：≥5 个失败案例与原因（丢中文族/表格图/手写体/零宽字符/扫描倾斜…）
3. **对照数据**：置信度判定标准（何时可信/何时必须人工复核/何时多源校勘）
4. **使用说明**：适用问题/挂载时机/更新日期
## 边界
- 弹药是你手里的真实案例，不编造；引用既有病例（如丢中文桩文件）注明来源锚
- 工作流步骤不写这里（那是 Skill，#658 已覆盖 transcribe/采集面；识图 workflow skill 可后续另立）
