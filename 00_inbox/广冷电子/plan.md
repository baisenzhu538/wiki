# 调研计划：山西省药品零售经营监督管理办法及类似政策全面深度调研

## 目标
全面深度调研山西省《药品零售经营监督管理办法（试行）》，以及中国各省市在药品零售渠道创新、药食同源销售、连锁经营门槛、远程药学服务、药品网络销售等五个维度的类似政策，输出结构化报告（.docx）。

## 研究路线
按 deep-research-swarm **Route B (Focused Search)** 执行：
- 用户提供了一个具体政策（山西省《药品零售经营监督管理办法》），并有明确调研维度（五大政策领域+其他省市对比）
- 不需要超宽搜索，但需要分维度深度调研和跨省市比较
- 无上传文件，仅基于URL获取文章，需大量外部搜索

## 阶段分解

### Stage 1: 景观扫描（Phase 1）
- 由主Agent执行5轮搜索，覆盖宏观政策背景、监管架构、主要趋势
- 搜索层级：国家药品零售监管框架 → 各省份政策概览 → 近期争议与趋势
- 输出：景观扫描笔记

### Stage 2: 维度分解与深度调研（Phase 2-3）
- 分解为10个调研维度，每个维度由独立Agent深度调研
- 维度列表：
  1. **山西省政策核心框架与背景**：政策制定过程、法律依据、适用范围
  2. **售药渠道创新**：多场所药品销售专柜、自助售药机、智慧药房（柜）——山西与甘肃、广东、浙江等省对比
  3. **药食同源中药饮片销售**：不凭处方开架销售政策——山西与各省对比
  4. **连锁经营门槛**：门店数量要求（10家）、跨省连锁、总部管理要求——全国各省对比
  5. **远程药学服务**：远程审方、驻店药师、AI审方限制——各省对比
  6. **药品网络销售**：线上线下一致、实体门店依托——各省与国家法规对比
  7. **国家层面监管框架**：《药品管理法》、NMPA法规、国家药监局对零售创新的态度
  8. **行业影响与实施效果**：药店行业反应、市场规模变化、便民效果
  9. **监管趋势与未来发展**：智慧监管、药品零售改革方向、潜在风险
  10. **法律风险与合规挑战**：政策执行中的争议、企业合规难点、监管处罚案例
- 每个维度Agent执行 ≥10次搜索，输出至 `{workspace}/research/`

### Stage 3: 交叉验证（Phase 4-5）
- 主Agent读取所有维度输出，分类置信度、识别冲突
- 输出 cross_verification.md
- 必要时派遣验证Agent解决冲突

### Stage 4: 洞察提取（Phase 6）
- 从跨维度分析中提取非显而易见的洞察
- 输出 insight.md

### Stage 5: 报告撰写（Phase 7 + report-writing）
- 加载 report-writing 技能
- 执行 Stage 1-4：大纲设计 → 内容撰写 → 审查 → 组装
- 最终输出 `.agent.final.md`

### Stage 6: 转换为 .docx
- 加载 docx 技能，执行 md2docx 转换
- 最终交付 `.docx` 文件

## 输出文件结构
```
{workspace}/
├── research/
│   ├── pharma_policy_dim01.md ~ dim10.md
│   ├── pharma_policy_cross_verification.md
│   ├── pharma_policy_insight.md
│   └── pharma_policy_landscape.md
├── pharma_policy.agent.outline.md
├── pharma_policy_sec01.md ~ sec10.md
├── pharma_policy.agent.final.md
└── pharma_policy.docx
```

## 引用规范
- 所有引用使用 `[^id]` 内联标记 + 脚注定义
- 优先来源：政府网站、NMPA、各省药监局、权威媒体、行业报告
- 禁止使用：匿名博客、内容农场、SEO聚合页

## 技能加载计划
- Stage 1-4：deep-research-swarm（深度调研）
- Stage 5：report-writing（报告撰写）+ outline.md + content.md + review.md + citation.md
- Stage 6：docx（格式转换）
