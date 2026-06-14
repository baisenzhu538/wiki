# KDO 30_wiki 问题卡片跟踪看板

> 创建日期：2026-06-15  
> 维护角色：王语嫣  
> 更新频率：月度  
> 来源：阶段 0–6 全库深度审查

---

## 看板统计

| 级别 | 数量 | 状态 |
|---|---|---|
| P0 | 1,234 | 待处理 |
| P1 | 444 | 待处理 |
| P2 | 待统计 | 待处理 |

> 注：P0/P1 数量来自 2026-06-15 质量门禁脚本扫描结果。大量 P0 为 `author=legacy` + `source_refs 为空`，需分批治理。

---

## P0 — 阻塞性问题

### 1. 元数据完整性（大规模）

| 问题 | 影响卡片数 | 说明 | 建议处理 | 负责人 |
|---|---|---|---|---|
| `author=legacy` | 约 1,200+ | 阶段 1 用 legacy 填充无 author 卡片，但 quality gate 要求 author 明确 | 按文件名前缀/内容/domain 推断真实作者；无法推断的暂标 `unknown` 并保持 draft | 王语嫣 + 各 owner |
| `source_refs` 为空 | 大量 | 无法追溯来源 | 优先补充 enriched/reviewed/stable 卡的 source；draft 卡可暂缓 | 老顽童 + 黄药师 |
| `reviewed_by=pending` 但 status=enriched/reviewed/stable | 数十张 | 元数据与实际状态不一致 | 确认 reviewer 后更新；或降级为 draft | 王语嫣 |
| YAML 解析错误 | 32 | 文件损坏 | 逐张修复 frontmatter | 黄药师 |
| `id` 与文件名不一致 | 少量 | 如 `ai时代判断力口述.md` 的 id 为 `ai时代判断力口述-2` | 统一为文件名 | 王语嫣 |

### 2. OCR 卡片高信任误导

| 文件 | 问题 | 建议 | 负责人 |
|---|---|---|---|
| `concepts/ocr-一堂-科学决策-深度-l4严格财务公式.md` | 公式未闭合、变量未定义 | 人工校对或降级 | 老顽童 |
| `concepts/ocr-泛产品设计-审美工具箱指南.md` | 乱码严重 | 人工校对或降级 | 老顽童 |
| `concepts/ocr-一堂-地图-个人地图_conv.md` | 内容几乎为空 | 删除或改为占位卡 | 老顽童 |
| `concepts/ocr-一堂-泛产品设计-十年苦练30招.md` | 表格错位、练习标准缺失 | 人工校对或降级 | 老顽童 |
| `concepts/ocr-泛产品设计-需求工具箱指南.md` | 乱码、13 张卡片编号混乱 | 人工校对或降级 | 老顽童 |
| `concepts/ocr-一堂-个人修炼-表达力火箭模型-执行武器库.md` | 乱码、与正式卡重叠 | 合并或降级 | 老顽童 |
| `concepts/ocr-一堂-科学决策-关键假设abcd模型.md` | 模型名称混用 | 人工校对 | 老顽童 |
| `concepts/ocr-一堂-科学决策-roi决策评估画布-案例04.md` | 数值属性不明、结论"赌一把" | 补充数据或降级 | 老顽童 |
| `concepts/ocr-一堂-管理必修-课程清单.md` | 纯索引、无知识内容 | 改类型或合并 | 黄药师 |
| `concepts/ocr-一堂-案例拆解-课程清单.md` | 纯索引、编号疑点 | 改类型或合并 | 黄药师 |
| `concepts/ocr-萃取总结.md` | 概念关系不明 | 补充定义 | 老顽童 |
| `concepts/ocr-一堂-个人修炼-科学提问刻意练习.md` | 成长地图未展示 | 补充内容 | 老顽童 |
| `concepts/ocr-婚礼规划.md` | OCR 质量差、Markdown 语法错误 | 人工校对 | 洪七公 |

### 3. 核心工具卡空心化

| 文件 | 问题 | 建议 | 负责人 |
|---|---|---|---|
| `concepts/yt-entrepreneur-five-step-method.md` | 仅复述名称、缺步骤/工具/判断标准 | 重写为完整 tool/framework | 老顽童 |
| `concepts/yt-entrepreneur-unit-model.md` | Bill Aulet 批判缺失、操作步骤不突出 | 补全内容 | 老顽童 |
| `concepts/yt-entrepreneur-259-milestone.md` | 未列出 9 个里程碑具体内容 | 补充 9 个里程碑定义与示例 | 老顽童 |

### 4. 高风险事实/合规问题

| 文件 | 问题 | 建议 | 负责人 |
|---|---|---|---|
| `concepts/skill-月白-印刷DPI标准设置.md` | DPI 数值疑似与行业常识相反 | 印刷专业人员复核 | 行业专家 |
| `concepts/skill-月白-AI电商图人工过审处理.md` | 教授规避平台检测技巧 | 合规改写或加显著风险提示 | 法务/合规 |
| `concepts/skill-月白-薅AIGC羊毛资源法.md` | 鼓励绕过平台付费机制 | 改写为低成本试用指南 | 法务/合规 |

### 5. 文件损坏

| 文件 | 问题 | 建议 | 负责人 |
|---|---|---|---|
| `concepts/yt-decision-depth-ladder.md` | 被异常行号前缀污染 | 清理行号、统一变量语义 | 技术编辑 |
| `cases/index.md` | YAML 解析错误 | 修复 frontmatter | 黄药师 |
| `concept-card-index-latest.md` | YAML 解析错误 | 修复 frontmatter | 黄药师 |

### 6. 关系字段误用

| 问题 | 影响卡片 | 建议 | 负责人 |
|---|---|---|---|
| `contradicts` 字段系统性误用 | master 域 10+ 张 dark-knowledge 卡 | 批量审计并修正为 `related`/`corrects` | 欧阳锋 |

---

## P1 — 影响可信度

### 1. Confidence / Trust 不匹配

| 问题 | 影响范围 | 建议 |
|---|---|---|
| confidence≥0.90 但 source<2 | 13 张（已下调 19 张） | 继续监控，确保下调后仍合理 |
| draft 状态 confidence≥0.85 | 部分 | 下调至 0.75 以下 |
| trust_level=high 但 source<2 | 部分 | 补充第二来源或下调 trust |
| OCR 卡 confidence>0.60 | 大量 | 统一降至 ≤0.60 |

### 2. Source 笼统/不可读

| 问题 | 影响范围 | 建议 |
|---|---|---|
| 仅指向"课程地图精华串讲" | yitang 域大量课程衍生卡 | 追踪到具体课程材料 |
| source ID 无路径映射 | 多域 | 建立 src ID → 文件路径索引 |
| 口头来源无行号 | case 卡常见 | 补充口述行号 |

### 3. Dangling 链接

| 问题 | 影响范围 | 建议 |
|---|---|---|
| `[[...]]` 或 `related` 指向不存在的卡片 | 建模域 70%+、yitang 域部分 | 运行死链扫描，修复或删除 |

### 4. 卡片间重复/冲突

| 主题 | 涉及文件 | 建议 |
|---|---|---|
| 千人广场 / 销冠广场 | case-thousand-people-square / concept-thousand-people-square / dk-modeling-case-explosion-confidence | 统一术语或合并 |
| 六步 / 七步里程碑 | case-course-milestone-model / framework-course-milestone-model | 确认官方流程 |
| 精准提示词 | skill-月白-精准提示词撰写法 / 精准共用提示词撰写 | 合并或差异化 |
| PPT AI 工作流 | skill-月白-PPT全AI生成工作流 / PPT风格锁定工作流 | 合并或拆分 |
| 多语言提示词 | skill-月白-多语言提示词降幻觉法 / AI自动生成多语种专业名词提示词 | 合并或互链 |
| 参考图收集 | skill-月白-最佳实践素材收集法 / 灵感画布建立法 / 设计参考图精准定位法 | 明确分工 |

### 5. 内容单薄

| 文件 | 问题 | 建议 |
|---|---|---|
| `concepts/sprint-2-门禁举证验收.md` | 概念卡过薄 | 补充真实运行示例 |
| `concepts/yt-personal-knowledge-management.md` | Framework Gallery 为空 | 填充或删除 |
| `concepts/master-cognitive-bias-checklist.md` | source 不可追溯 | 引用具体文献 |
| `concepts/master-first-principles.md` | source 不可追溯 | 引用具体文本 |

---

## P2 — 优化项

### 1. 格式问题

- 连续空行过多
- 未闭合 `**` 标记
- 转义引号 `"` 残留
- Visual Analysis 章节过长

### 2. 模板残留

- 重复的"不要用的场景"表格
- 重复的 Taleb/Simon 批判段落
- 空 Critique / 空章节

### 3. Domain 标注

- 单元模型工具缺少 `yitang`
- `entrepreneur` / `business-strategy` / `yitang` 边界不清
- design 标签过于宽泛，建议细分为 `ai-design`、`prompt-engineering` 等

### 4. Cross-link 缺失

- 同一主题卡片未互链
- Synthesis 段落缺少具体引用

---

## 最近行动记录

| 日期 | 行动 | 结果 |
|---|---|---|
| 2026-06-14 | 阶段 0：全库基线扫描 | 生成 1,320 张卡片清单和问题报告 |
| 2026-06-14 | 阶段 1：元数据治理 | 修复 YAML 引号错误、补全 author/reviewer/id |
| 2026-06-15 | 阶段 2：高危卡片清理 | 抽样审查高置信低信任/无 source 卡片 |
| 2026-06-15 | 阶段 3：按作者深度审查 | 审查老顽童 54 张、黄药师 13+40 张 |
| 2026-06-15 | 阶段 4：按可信度分层审查 | 填充 confidence 968 张、trust_level 1,095 张、下调 confidence 19 张 |
| 2026-06-15 | 阶段 5：按 Domain 专项审查 | 审查 yitang/design/master 样本；修复 YAML 列表字段 952 张 |
| 2026-06-15 | 阶段 6：建立质量控制机制 | 创建自检清单、门禁脚本、审查机制、问题看板 |

---

## 下月目标

1. 修复 32 张 YAML 解析错误卡片
2. 将 author=legacy 的 enriched/reviewed/stable 卡片降至 0
3. 为 yitang 域 13 张 OCR 卡统一降级或人工校对
4. 处理 design 域 3 张高风险卡片的合规问题
5. 修正 master 域 contradicts 字段误用
