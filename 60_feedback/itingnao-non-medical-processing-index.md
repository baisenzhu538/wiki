# 听脑非药柜主题处理索引

生成时间：2026-06-14

## 处理范围

- **总录音数**：406 条
- **药柜/医疗相关**：约 72 条（已单独处理）
- **非药柜主题**：334 条
- **本次处理**：102 条被识别为「与 30_wiki 知识库未明显重叠」的录音

## 处理流程

1. 扫描 334 条非药柜录音与 `30_wiki` 知识库的重叠
2. 识别出 102 条未覆盖录音
3. 拉取这 102 条录音的详情与纪要
4. 二次主题分类为 10 个主题
5. 剔除 13 条无效/低价值录音
6. 发现 12 条实质药柜/医疗相关录音混入非药柜主题
7. 对 9 个有效非药柜主题生成综合知识卡草稿
8. 生成药柜混入清单

## 产出物清单

### 知识卡草稿（9 张）

| 文件 | 主题 | 录音数 | 核心定位 |
|------|------|--------|----------|
| `kcard-yitang-methodology-draft.md` | 一堂方法论体系 | 26 | Y模型、IPO、TCPR、业务公式、知识萃取等方法论整合 |
| `kcard-ai-methodology-tools-draft.md` | AI 方法论与工具栈 | 11 | 双三角、Feature 训练、Skill→Agent→AI 原生组织 |
| `kcard-ai-hackathon-pitches-draft.md` | AI 大航海项目路演 | 11 | 项目路演样本群、MVP 验证、商业化路径 |
| `kcard-industry-ai-cases-draft.md` | 产业 AI 落地案例集 | 9 | 酒店审核、贝壳外呼、自动选品、GEO/AIO 营销等 |
| `kcard-other-draft.md` | 跨域业务验证与组织协作 | 10 | 精益验证、FD 模式、智能设备对接、假设驱动 |
| `kcard-personal-growth-draft.md` | 个人成长与组织 | 5 | 复杂系统、超级个体、消除模糊、终身学习 |
| `kcard-finance-legal-business-draft.md` | 财务-法务-商务运营 | 5 | B2B 履约、税务、支付分账、资质申报 |
| `kcard-product-business-draft.md` | 产品-商业战略 | 3 | 设备运营、战略取舍、食品饮料开发 |
| `kcard-supply-chain-beverage-draft.md` | 餐饮渠道饮料供应链 | 4 | 成本-口感张力、渠道定价、供应链优化 |

### 辅助文件

- `medical-contamination-in-nonmed-report.md` —— 非药柜主题中的药柜/医疗混入清单（12 条）

### 工作文件（不入 60_feedback，仅作参考）

- `90_control/itingnao-kit/work/non-med-uncovered.json`
- `90_control/itingnao-kit/work/non-med-regrouped.json`
- `90_control/itingnao-kit/work/medical-contamination-in-nonmed.json`
- `90_control/itingnao-kit/work/theme-*.md`

## 药柜混入清单（需复核）

| 录音 ID | 标题 | 原主题 | 处理建议 |
|---------|------|--------|----------|
| 4226418 | 药店-选址选品运营讨论 | internal-tech | 移入药柜/药店运营队列 |
| 4092592 | 多人-药店数字化改造讨论 | ai-tech | 移入药柜/药店数字化队列 |
| 3424604 | 云聚米-私有化部署与开发沟通 | internal-tech | 移入药柜/医疗系统队列 |
| 3166977 | 润馨堂-品牌运营讨论 | internal-tech | 移入药柜/品牌运营队列 |
| 2247045 | 瑞心堂-集采与品牌升级讨论 | internal-tech | 移入药柜/供应链队列 |
| 6269640 | 货柜-结构与电子方案讨论 | supply-chain-beverage | 移入药柜/硬件开发队列 |
| 1483043 | 项目分账与支付对接方案 | finance-legal-business | 移入药柜/支付合规队列 |
| 6272697 | 外卖平台-智能分单系统沟通 | other | 复核是否涉及医药即时零售 |
| 2694971 | 多人-AI与行业发展讨论 | industry-ai-cases | 移入药柜/AI应用队列 |
| 1486162 | 智慧城市AI应用交流 | ai-methodology-tools | 移入药柜/医疗AI队列 |
| 6311449 | 一堂-商业项目宣讲会 | yitang-methodology | 仅医疗片段移入复核 |
| 4231073 | 多人-项目问题沟通 | product-business | 复核原文后决定 |

## 后续建议

1. **药柜长期关注**：将混入的 12 条录音归入药柜处理队列，与原有 72 条合并分析
2. **知识卡升级**：9 张草稿需经原文复核后，再决定是否迁移至 `30_wiki/concepts/`
3. **无效录音归档**：13 条无效/低价值录音记录原因后归档，不进入处理流程
4. **主题再拆分**：「other」主题跨度较大，建议后续拆分为更细主题
5. **数据验证**：所有量化数据均来自口述摘要，需回听原文或补充外部证据

## 王语嫣铁律确认

- 所有诊断输出仅写入 `60_feedback/`
- 未污染 `30_wiki/`
- 药柜相关录音已单独标注，不强行混入非药柜主题
