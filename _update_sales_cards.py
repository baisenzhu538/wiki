# -*- coding: utf-8 -*-
from pathlib import Path

# --- Update diagnosis report ---
diag_path = Path('C:/Users/Administrator/Desktop/wiki/60_feedback/diagnosis/diag_20260702_yitang-scientific-sales-methodology.md')
diag = diag_path.read_text(encoding='utf-8')

old_related = '''related:
  - "[[task_20260702_laowantong-yitang-scientific-sales-methodology-production]]"
  - "[[opc-ai-sales-agent-architecture]]"
  - "[[framework-yitang-channel-exploration-4step]]"
  - "[[yt-five-step-method-complete]]"
  - "[[framework-一堂五步法-泛产品设计]]"
  - "[[yitang-methodology-system]]"
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
---'''
new_related = '''related:
  - "[[task_20260702_laowantong-yitang-scientific-sales-methodology-production]]"
  - "[[opc-ai-sales-agent-architecture]]"
  - "[[framework-yitang-channel-exploration-4step]]"
  - "[[yt-five-step-method-complete]]"
  - "[[framework-一堂五步法-泛产品设计]]"
  - "[[yitang-methodology-system]]"
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
---'''
if old_related in diag:
    diag = diag.replace(old_related, new_related, 1)
    print('diag related updated')
else:
    print('diag related NOT FOUND')

old_row15 = '''| 15 | OPC 智能体军团 | AI 协作 / 个人 OS | `opc-ai-sales-agent-architecture` / `human-ai-collaboration-double-triangle` | 销售能力代码化 | 否，已有 system 文件，需反向更新 related |'''
new_row15 = '''| 15 | OPC 智能体军团 | AI 协作 / 个人 OS | `opc-ai-sales-agent-architecture` / `human-ai-collaboration-double-triangle` | 销售能力代码化 | ✅ 新增 `tool-opc-sales-dialogue-assistant`（MVP 对话助手规格卡）；11 智能体架构总图仍由已有 `opc-ai-sales-agent-architecture.md` 承接，需反向更新 related |'''
if old_row15 in diag:
    diag = diag.replace(old_row15, new_row15, 1)
    print('diag L9 row15 updated')
else:
    print('diag L9 row15 NOT FOUND')

old_sec12 = '''## 十二、建议产出的 10 张卡

基于以上诊断，建议产出 **1 framework + 5 tool + 1 framework + 2 case + 1 dk**。

> 说明：用户分层与卖点提炼拆分为两张独立工具卡，未来咨询「该重点跟进哪些客户」和「怎么写卖点」可分别调用；剧本杀 SaaS 和美容院作为两个完整转型案例独立成卡，覆盖 To B 与 To C 场景；新增一张销售反模式 dk 卡，沉淀最常见陷阱。'''
new_sec12 = '''## 十二、建议产出的 12 张卡

基于以上诊断，建议产出 **1 framework + 5 tool + 1 framework + 3 case + 1 dk + 1 tool（OPC 智能体）**。

> 说明：
> - 用户分层与卖点提炼拆分为两张独立工具卡，未来咨询「该重点跟进哪些客户」和「怎么写卖点」可分别调用。
> - 剧本杀 SaaS、美容院、涂料公司作为三个完整转型案例独立成卡，分别覆盖 To B 初创 SaaS、To C 门店零售、传统工业分销三个场景。
> - 新增一张销售反模式 dk 卡，沉淀最常见陷阱。
> - 在黄药师建议基础上，王语嫣独立判断：智能体层不一次性产出 8-10 张，而是先产出 **1 张 MVP 对话助手智能体规格卡**（读对话 → 想策略 → 给话术），直接解决 OPC 最大痛点；其余智能体待本批卡片终审后，根据使用反馈再分批扩展。'''
if old_sec12 in diag:
    diag = diag.replace(old_sec12, new_sec12, 1)
    print('diag sec12 intro updated')
else:
    print('diag sec12 intro NOT FOUND')

old_before13 = '''### Card 10: `case-yitang-sales-transformation-meirongyuan`

**类型**：case  
**主域**：sales / retail / yitang  
**定位**：To C 门店销售体系改造案例，覆盖总部与门店利益协同。

**必须包含的 section**：
1. **Background**：美容院连锁，年营收上千万，新销售总监目标 2000 万。
2. **Problem**：总部与门店利益冲突、店长不配合数据填报、新渠道响应不及时、目标拆不下去。
3. **Decision**：从用户分层、过程拆解、目标拆解、激励机制、数据表单五方面改造。
4. **Process**：
   - 重新明确进店用户画像，按消费能力/稳定性/尝鲜度分层
   - 梳理美团咨询到转化的 20+ 关键节点
   - 用两家样板店验证，再推广到所有门店
   - 目标拆到门店、技师、客户
   - 调整激励机制统一总部和门店利益
   - 优化数据表单，总部派专人协助填关键数据
5. **Result**：在线咨询响应提升后新客到店转化率从 15-20% 提升至 25%；总部与门店不再打架。
6. **Lessons**：样板店验证、利益统一、数据表单要轻量化、关键节点数据化。
7. **Failure Modes**：总部强压门店、表单太复杂、忽视店长利益、新渠道不维护。
8. **Synthesis**：桥接 `framework-yitang-scientific-sales-five-step`、`tool-yitang-customer-segmentation-4step`、`tool-yitang-sales-process-decomposition`、`tool-yitang-sales-performance-management`、`framework-yitang-sales-incentive-6d`、`tool-yitang-sales-toolkit-radar`、`framework-yitang-channel-exploration-4step`。
9. **Related**：≥5 条。

---

## 十三、已有卡补链建议'''
new_before13 = '''### Card 10: `case-yitang-sales-transformation-meirongyuan`

**类型**：case  
**主域**：sales / retail / yitang  
**定位**：To C 门店销售体系改造案例，覆盖总部与门店利益协同。

**必须包含的 section**：
1. **Background**：美容院连锁，年营收上千万，新销售总监目标 2000 万。
2. **Problem**：总部与门店利益冲突、店长不配合数据填报、新渠道响应不及时、目标拆不下去。
3. **Decision**：从用户分层、过程拆解、目标拆解、激励机制、数据表单五方面改造。
4. **Process**：
   - 重新明确进店用户画像，按消费能力/稳定性/尝鲜度分层
   - 梳理美团咨询到转化的 20+ 关键节点
   - 用两家样板店验证，再推广到所有门店
   - 目标拆到门店、技师、客户
   - 调整激励机制统一总部和门店利益
   - 优化数据表单，总部派专人协助填关键数据
5. **Result**：在线咨询响应提升后新客到店转化率从 15-20% 提升至 25%；总部与门店不再打架。
6. **Lessons**：样板店验证、利益统一、数据表单要轻量化、关键节点数据化。
7. **Failure Modes**：总部强压门店、表单太复杂、忽视店长利益、新渠道不维护。
8. **Synthesis**：桥接 `framework-yitang-scientific-sales-five-step`、`tool-yitang-customer-segmentation-4step`、`tool-yitang-sales-process-decomposition`、`tool-yitang-sales-performance-management`、`framework-yitang-sales-incentive-6d`、`tool-yitang-sales-toolkit-radar`、`framework-yitang-channel-exploration-4step`。
9. **Related**：≥5 条。

### Card 11: `case-yitang-sales-transformation-tuliaogongsi`

**类型**：case  
**主域**：sales / manufacturing-distribution / b2b / yitang  
**定位**：传统工业分销场景下的用户分层与销售资源配置转型案例，带明确数据。

**必须包含的 section**：
1. **Background**：涂料公司，面临海量线索但转化率低，销售精力分散。
2. **Problem**：10 万个注册线索里分不清谁是真客户；销售平均分配精力，S 级客户被淹没；没有基于目标的分层假设。
3. **Decision**：用一堂用户分层四步法重新做 SABC 分级，把有限资源集中到高价值客户。
4. **Process**：
   - 明确阶段目标：短期要利润还是长期要标杆客户？
   - 提出分层假设：根据公司规模、项目类型、采购周期、地域等维度假设 S/A/B/C 标准
   - 验证假设：分析历史成交客户画像，抽样访谈 20 个已成交和 20 个未成交客户
   - 执行分层：从 10 万线索中筛出约 20 条 S 级、200 条 A 级，其余进入自动化培育
5. **Result**：销售团队把 80% 精力放在 Top 220 客户上，S 级客户转化率显著提升；整体线索处理效率提高。
6. **Lessons**：分层必须和目标挂钩；没有验证的分层是拍脑袋；自动化培育可以让 B/C 级线索不浪费。
7. **Failure Modes**：只看线索数量不看质量、分层标准常年不更新、B/C 级线索直接丢弃不用培育、销售抵制"只给少量线索"。
8. **Synthesis**：桥接 `framework-yitang-scientific-sales-five-step`、`tool-yitang-customer-segmentation-4step`、`tool-yitang-sales-performance-management`、`master-decision-hygiene`。
9. **Related**：≥5 条。

### Card 12: `tool-opc-sales-dialogue-assistant`

**类型**：tool  
**主域**：personal-os / ai-sales-agent / yitang  
**定位**：OPC 销售智能体 MVP 规格卡，可直接作为 system prompt 使用。解决一人公司同时聊多个客户时"跟丢、跟乱、跟错节奏"的痛点。

**必须包含的 section**：
1. **When to Use**：一人公司创始人同时跟进多个客户、对话散落在微信/邮件/通话中、容易忘记客户阶段、回复前需要快速判断局势。
2. **核心功能**：读对话 → 想策略 → 给话术。
3. **输入**：客户对话记录（微信/邮件/通话转写/CRM 备注）、当前客户分层标签（可选）、当前销售阶段（可选）。
4. **输出**：
   - 客户意图与阶段判断（接触/购买/付款/履约 + 情绪/抗拒点）
   - 下一步建议（该做什么、不该做什么）
   - 2-3 个回复选项（可直接选用或微调）
5. **工作逻辑**：
   - 用 `tool-yitang-customer-segmentation-4step` 判断客户等级
   - 用 `tool-yitang-sales-process-decomposition` 识别当前阶段和关键决策点
   - 用 `tool-yitang-value-proposition-4step` 选择匹配卖点
   - 用 `tool-yitang-sales-performance-management` 判断是否需要推进/预警
   - 生成 2-3 个不同风格回复（直接型/共情型/提问型）
6. **System Prompt 模板**：提供一份可直接复制到 Claude/GPT 自定义指令的精简模板。
7. **边界与风险提示**：
   - 不替代关键人际信任建立
   - 不自动发送消息，只输出建议
   - 涉及客户隐私数据需本地/合规处理
8. **Checklist**：≥8 项。
9. **Anti-patterns**：完全照搬话术不调整、把AI建议当最终决策、在关键谈判中让AI代写、忽视客户情绪信号。
10. **Critique**：≥3 个外部反对者 + ≥2 个内部局限。
11. **Synthesis**：桥接 `opc-ai-sales-agent-architecture`、`human-ai-collaboration-double-triangle`、`framework-yitang-scientific-sales-five-step`、`tool-yitang-customer-segmentation-4step`、`tool-yitang-value-proposition-4step`、`tool-yitang-sales-process-decomposition`、`tool-yitang-sales-performance-management`。
12. **Related**：≥5 条。

---

## 十三、已有卡补链建议'''
if old_before13 in diag:
    diag = diag.replace(old_before13, new_before13, 1)
    print('diag sec12 cards updated')
else:
    print('diag sec12 cards NOT FOUND')

old_sec13 = '''## 十三、已有卡补链建议

产出 10 张新卡后，反向更新以下已有卡的 `related`：'''
new_sec13 = '''## 十三、已有卡补链建议

产出 12 张新卡后，反向更新以下已有卡的 `related`：'''
if old_sec13 in diag:
    diag = diag.replace(old_sec13, new_sec13, 1)
    print('diag sec13 intro updated')
else:
    print('diag sec13 intro NOT FOUND')

old_list_end = '''24. `human-ai-collaboration-double-triangle`
25. `framework-lean-pivot-decision`
26. `dk-yitang-channel-exploration-traps`'''
new_list_end = '''24. `human-ai-collaboration-double-triangle`
25. `framework-lean-pivot-decision`
26. `dk-yitang-channel-exploration-traps`
27. `case-yitang-sales-transformation-tuliaogongsi`
28. `tool-opc-sales-dialogue-assistant`'''
if old_list_end in diag:
    diag = diag.replace(old_list_end, new_list_end, 1)
    print('diag sec13 list updated')
else:
    print('diag sec13 list NOT FOUND')

old_sec14 = '''## 十四、OPC 智能体落地特别说明

OPC 目标与销售五步法高度匹配，但需做以下改编：

| 原版（带团队） | OPC 版（一人+AI） |
|:---|:---|
| 用户分层四步法 | 用户分层智能体：判断「这个客户值不值得我亲自跟」 |
| 卖点提炼四步法 | 卖点提炼智能体：针对不同客户生成差异化卖点 |
| 客户意图识别 | 客户意图识别智能体：识别决策阶段/抗拒点/情绪 |
| 销售过程拆解 | 销售过程拆解智能体：追踪里程碑、卡点预警 |
| 业绩管理三步法 | 业绩预测 + 跟进编排智能体：周计划 + Gap 提醒 |
| 六维激励团队 | 替换为创始人自我驱动机制（目标-行动-反馈循环） |
| 销售武器库 | 智能体提示词库 + 提案模板库 + 案例库 |

这些改编已在 `opc-ai-sales-agent-architecture.md` 中记录。本次新产出的 10 张 KDO 卡应成为该架构的底层方法论来源，需在 `opc-ai-sales-agent-architecture` 的 related 中回链。'''
new_sec14 = '''## 十四、OPC 智能体落地特别说明

OPC 目标与销售五步法高度匹配，但需做以下改编：

| 原版（带团队） | OPC 版（一人+AI） |
|:---|:---|
| 用户分层四步法 | 用户分层智能体：判断「这个客户值不值得我亲自跟」 |
| 卖点提炼四步法 | 卖点提炼智能体：针对不同客户生成差异化卖点 |
| 客户意图识别 | 客户意图识别智能体：识别决策阶段/抗拒点/情绪 |
| 销售过程拆解 | 销售过程拆解智能体：追踪里程碑、卡点预警 |
| 业绩管理三步法 | 业绩预测 + 跟进编排智能体：周计划 + Gap 提醒 |
| 六维激励团队 | 替换为创始人自我驱动机制（目标-行动-反馈循环） |
| 销售武器库 | 智能体提示词库 + 提案模板库 + 案例库 |
| **MVP 首选** | **对话助手智能体**：读对话 → 想策略 → 给话术（详见 `tool-opc-sales-dialogue-assistant`） |

**为什么先做对话助手？**

基于一人公司"资源少、见效快、能闭环"的原则，第一个 MVP 不是做 8 个智能体，而是做 1 个对话助手。它把三件事合在一起：读对话识别客户意图和阶段、想策略判断下一步该做什么、给话术生成 2-3 个回复选项。这直接解决 OPC 最大痛点——一个人同时聊多个客户时，容易跟丢、跟乱、跟错节奏。这个智能体不改变销售动作，只是每次对话后递一张"小抄"。

这些改编已在 `opc-ai-sales-agent-architecture.md` 中记录。本次新产出的 12 张 KDO 卡应成为该架构的底层方法论来源；其中 `tool-opc-sales-dialogue-assistant` 是首个可直接作为 system prompt 运行的规格卡，需在 `opc-ai-sales-agent-architecture` 的 related 中回链，并在该架构中补充 MVP 启动路径。'''
if old_sec14 in diag:
    diag = diag.replace(old_sec14, new_sec14, 1)
    print('diag sec14 updated')
else:
    print('diag sec14 NOT FOUND')

old_op = '''- 可操作性强：可直接产出 1 framework + 5 tool + 1 framework + 2 case + 1 dk，并反向更新 ≥26 张已有卡 related。'''
new_op = '''- 可操作性强：可直接产出 1 framework + 5 tool + 1 framework + 3 case + 1 dk + 1 tool（OPC 智能体），并反向更新 ≥28 张已有卡 related。'''
if old_op in diag:
    diag = diag.replace(old_op, new_op, 1)
    print('diag op line updated')
else:
    print('diag op line NOT FOUND')

old_final = '''**预计卡数**：10 张（1 framework + 5 tool + 1 framework + 2 case + 1 dk） + 反向更新 ≥26 张已有卡 related'''
new_final = '''**预计卡数**：12 张（1 framework + 5 tool + 1 framework + 3 case + 1 dk + 1 tool（OPC 智能体）） + 反向更新 ≥28 张已有卡 related'''
if old_final in diag:
    diag = diag.replace(old_final, new_final, 1)
    print('diag final updated')
else:
    print('diag final NOT FOUND')

diag_path.write_text(diag, encoding='utf-8', newline='')
print('diagnosis written')
