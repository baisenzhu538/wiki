---

id: atk_20260702_yitang-scientific-sales-methodology-suite
title: 自攻击报告：一堂科学销售方法论 12 张新卡
type: report
status: reviewed
author: 老顽童
reviewed_by: 欧阳锋
created_at: 2026-07-02
updated_at: '2026-07-02'
related:
  - "[[framework-yitang-scientific-sales-five-step]]"
  - "[[tool-yitang-customer-segmentation-4step]]"
  - "[[tool-yitang-value-proposition-4step]]"
  - "[[tool-yitang-sales-process-decomposition]]"
  - "[[tool-yitang-sales-performance-management]]"
  - "[[framework-yitang-sales-incentive-6d]]"
  - "[[tool-yitang-sales-toolkit-radar]]"
  - "[[dk-yitang-sales-common-pitfalls]]"
  - "[[case-yitang-sales-transformation-jubensha-saas]]"
  - "[[case-yitang-sales-transformation-meirongyuan]]"
  - "[[case-yitang-sales-transformation-tuliaogongsi]]"
  - "[[tool-opc-sales-dialogue-assistant]]"
  - "[[framework-kdo-self-attack]]"

---

# 自攻击报告：一堂科学销售方法论 12 张新卡

> 依据 [[framework-kdo-self-attack]]，在提交欧阳锋终审前对 #44 任务产出的 12 张新卡进行四路对抗检查。本报告记录攻击发现的问题、修复动作和未修复事项的说明。

---

## 一、攻击范围

| 卡片 | 类型 | 主要主张 |
|:---|:---|:---|
| [[framework-yitang-scientific-sales-five-step]] | framework | 科学销售五步法是一堂方法论在销售管理场景的实例化 |
| [[tool-yitang-customer-segmentation-4step]] | tool | 四步 SABC 分层把销售资源集中到高价值客户 |
| [[tool-yitang-value-proposition-4step]] | tool | 四步卖点提炼统一销售语言 |
| [[tool-yitang-sales-process-decomposition]] | tool | 拆路径→划阶段→配动作，把销售过程从黑盒变地图 |
| [[tool-yitang-sales-performance-management]] | tool | 拆目标→定策略→追过程，让业绩可预测 |
| [[framework-yitang-sales-incentive-6d]] | framework | 六维激励模型替代单一金钱激励 |
| [[tool-yitang-sales-toolkit-radar]] | tool | 六维雷达图评估销售工具箱成熟度 |
| [[dk-yitang-sales-common-pitfalls]] | dark-knowledge | 六大销售管理反模式与修复动作 |
| [[case-yitang-sales-transformation-jubensha-saas]] | case | 剧本杀 SaaS 五步法改造 |
| [[case-yitang-sales-transformation-meirongyuan]] | case | 美容院连锁五步法改造 |
| [[case-yitang-sales-transformation-tuliaogongsi]] | case | 涂料公司 10 万线索 SABC 分层改造 |
| [[tool-opc-sales-dialogue-assistant]] | tool | OPC 销售对话助手智能体 MVP 规格卡 |

---

## 二、四路攻击发现

### 2.1 逻辑攻击（Attacker A）

| 卡片 | 问题 | 级别 | 修复 |
|:---|:---|:---:|:---|
| `framework-yitang-scientific-sales-five-step` | 五步法总图把销售管理抽象为线性五步，可能掩盖步骤间迭代关系 | 🟡 | 在「与一堂五步法的关系」中说明是内环迭代而非一次性瀑布 |
| `tool-opc-sales-dialogue-assistant` | 把销售五步法压缩为对话助手，可能让人误以为所有销售动作都能被 AI 替代 | 🟡 | 在边界与风险中强调「不替代关键信任建立、不自动发送消息」 |
| `framework-yitang-sales-incentive-6d` | 六维模型覆盖物质+精神，但精神激励难以量化，落地易被简化成口号 | 🟡 | 在 Critique 内部局限中说明「精神激励需动态 A/B 测试」 |
| `case-*` | 三个案例都来自同一课程，样本单一，无法做对照验证 | 🟡 | 所有数字降级为经验值，confidence 0.80-0.82 / trust_level medium |

### 2.2 证据攻击（Attacker B）

| 卡片 | 问题 | 级别 | 修复 |
|:---|:---|:---:|:---|
| 全部 case 卡 | 关键数据（转化率、完成率、营收）来自李蕊口述，无第三方审计 | 🟡 | 全部数字加「约」并标注 `[conf=0.82, source=李蕊口述]` |
| `tool-yitang-sales-performance-management` | 快钱支付、手机配件电商案例细节较少，可能依赖推断 | 🟡 | 用「课程中提及」而非「已验证」表述，避免过度声称 |
| `tool-yitang-value-proposition-4step` | iPhone 充电器、儿童记忆力培训案例被多次课程引用，可能存在幸存者偏差 | 🟡 | 在 Critique 中作为外部质疑之一回应 |
| `dk-yitang-sales-common-pitfalls` | 失败模式全部来自同一课程，跨行业验证不足 | 🟡 | 在内部局限中说明「其他行业（如电商、直播）可能有不同陷阱」 |

### 2.3 完整性攻击（Attacker C）

| 卡片 | 问题 | 级别 | 修复 |
|:---|:---|:---:|:---|
| `dk-yitang-sales-common-pitfalls` | 任务单要求 `dark_knowledge_type: pattern`，但 schema 枚举无该值 | 🔴 | 改为 schema 允许的 `failure`，并在本报告记录 |
| `dk-yitang-sales-common-pitfalls` | domain 包含 `business-strategy` / `management`，但 dark-knowledge schema domain 枚举只允许 `master / ai-saas / healthcare / yitang` | 🔴 | 保留 `domain: [yitang]`，用 tags 标记 #sales #management 表达跨域 |
| 多张 tool/framework 卡 | 正文末尾重复出现「Related」section，与 frontmatter `related` 重复 | 🟡 | 未删除，因为不违反 lint，但后续可统一为仅 frontmatter 出链 |
| `tool-opc-sales-dialogue-assistant` | System Prompt 模板中的回复示例为通用占位，需用户替换 | 🟡 | 在模板注释中明确「替换为具体产品卖点与周期数据」 |

### 2.4 时效性攻击（Attacker D）

| 卡片 | 问题 | 级别 | 修复 |
|:---|:---|:---:|:---|
| `tool-opc-sales-dialogue-assistant` | 模型能力（Claude/GPT）和隐私法规半年后可能变化 | 🟡 | 在 Critique 内部局限中声明模型与合规时效性 |
| 全部工具卡 | 课程案例中的 CRM、数据表单、协作工具具体产品会迭代 | 🟢 | 按能力类型描述（CRM、数据看板），不绑定具体厂商 |
| `framework-yitang-sales-incentive-6d` | 劳动法规、社保个税政策会变化 | 🟡 | 在多处标注「薪酬/劳动合规需专业机构复核」 |

---

## 三、已修复问题汇总

1. **dk 类型合规**：`dark_knowledge_type` 从任务单不可枚举值 `pattern` 改为 `failure`。
2. **dk domain 合规**：`domain` 缩至 `[yitang]`，跨域通过 tags 表达。
3. **数字降级**：所有 case 和工具卡中的营收、转化率、完成率等数字均加「约」并标注来源与置信度。
4. **法律/合规边界显性化**：涉及薪酬、劳动、提成、客户数据、合同等场景均提示需专业机构复核。
5. **OPC 边界明确**：`tool-opc-sales-dialogue-assistant` 强调不替代关键信任建立、不自动发送消息。
6. **反向 related 补全**：12 张新卡之间互相链接，28 张已有卡 + `opc-ai-sales-agent-architecture.md` 已反向更新 related。

---

## 四、未修复问题及理由

| 问题 | 理由 |
|:---|:---|
| 样本全部来自一堂课程，无外部独立来源 | 任务定位即为「一堂科学销售方法论」实例化；跨行业验证可作为后续 wave 任务 |
| 部分工具卡正文末尾保留 body「Related」section | 不违反 lint，且便于正文阅读；可在后续统一格式任务中清理 |
| OPC 智能体 System Prompt 示例为通用占位 |  intentionally 留出用户替换空间，避免过拟合特定产品 |
| 课程中部分案例细节不足（如手机配件电商） | 已按「课程经验值」处理，未上升为普适结论 |

---

## 五、修复后验证

- `python 90_control/scripts/kdo_lint.py 30_wiki` 在 12 张新卡和 28 张反向更新卡上均未报错（目标文件在完整 lint 输出中无 ERROR）。
- 28 张已有卡 + `opc-ai-sales-agent-architecture.md` 的 `related` 均通过 YAML 解析检查，无语法错误。
- 12 张新卡的 `source_refs` 均指向真实存在的整合笔记、诊断报告或原始素材。

---

## 六、结论

本次自攻击未发现致命逻辑错误或证据造假。主要风险集中在「单一样本来源」「精神激励难量化」「OPC 边界被误用」「劳动合规」四个层面，均已通过标注 confidence/trust_level、补充 Critique/局限、明确 OPC 边界、法律声明等手段降级。建议提交欧阳锋终审。

---

*攻击框架：[[framework-kdo-self-attack]] | 攻击日期：2026-07-02*
