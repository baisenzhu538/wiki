---
id: task_20260802_wangyuyan-213-related-supplement
task_id: 213
assignee: laowantong
status: queued
created_at: 2026-08-02
domain: strategy
priority: P1
source: 欧阳锋终审 TODO（验收#7 related<5 违约）
parent: task_20260802_wangyuyan-innovators-dilemma-qinpeng
depends_on:
  - bridge-christensen-reverse-mapping（Wave 0 已完成，四列映射表就绪）
  - 本任务在 P0 结构修复完成后执行
---

# #213 补链任务：9张卡 related 补到 ≥5

## 背景

欧阳锋复审 PASS/A-，但验收#7（related ≥5 且 ≥2 跨域）违约：14张卡中9张 related < 5。结构修复已完成，本次只补链。

## 目标

9张卡每张 related ≥5，且至少2条跨域。

## 补链策略

使用 Wave 0 已完成的 `bridge-christensen-reverse-mapping` 四列映射表（引用文件→引用概念→原著位置→是否回填）作为 related 来源。

**三类链接来源**：

| 来源 | 操作 | 示例 |
|:--|:--|:--|
| **Wave 1-2 内部卡** | 框架卡/应用卡互链 | `concept-qinpeng-ai-as-amplifier` → `tool-qinpeng-ai-intelligent-service`（上下游关系）|
| **bridge 映射表** | 反向补链到已有 wiki 卡 | `dk-disruptive-innovation-insight-vs-survey` → `yt-panproduct-execution-low-cost-mvp`（已引用 Christensen 且概念匹配）|
| **跨域桥接** | 链到其他域的核心卡 | 战略域→产品域/决策域/需求域 |

## 逐卡补链清单

### 1. `concept-qinpeng-ai-as-amplifier` (当前 4 → ≥5)

已有 related：tool-qinpeng-ai-intelligent-service, concept-qinpeng-knowledge-base-conversion, framework-christensen-disruptive-innovation, case-qinpeng-hardware-ai-amplification

需补 ≥1 条：
- → `tool-马易-AI落地场景识别与拆分`（产品域：放大器论是场景识别的底层逻辑）
- → `dk-ai-capability-not-magic`（暗知识域：AI不会创造能力，呼应放大器论）

### 2. `concept-qinpeng-knowledge-base-conversion` (当前 4 → ≥5)

已有 related：concept-qinpeng-ai-as-amplifier, tool-qinpeng-ai-intelligent-service, case-qinpeng-hardware-ai-amplification, case-english-teacher-ai-agent

需补 ≥1 条：
- → `tool-纪浩-Agent技能市场设计法`（Agent域：知识库是Agent技能的底层资产）
- → `concept-cognitive-offloading-in-ai-era`（认知域：知识库转化=认知卸载的前置步骤）

### 3. `dk-qinpeng-three-corrections` (当前 3 → ≥5)

已有 related：framework-christensen-disruptive-innovation, dk-disruptive-innovation-insight-vs-survey, concept-christensen-rpv-model

需补 ≥2 条：
- → `yt-panproduct-execution-roi-analysis`（产品域：纠正①毛利低vs需求不明→ROI卡已深度引用Christensen）
- → `yt-panproduct-execution-low-cost-mvp`（产品域：纠正②小市场≠低毛利→MVP验证卡已引用）
- → `dk-christensen-empirical-criticisms`（本Wave内部：实证批判是三纠正的外部支撑）

### 4. `dk-disruptive-innovation-insight-vs-survey` (当前 3 → ≥5)

已有 related：dk-qinpeng-three-corrections, framework-christensen-disruptive-innovation, dk-christensen-empirical-criticisms

需补 ≥2 条：
- → `yt-panproduct-execution-low-cost-mvp`（产品域：洞察vs调研→MVP验证的"破坏性创新无法被现有客户验证"）
- → `tool-需求挖掘.md`（需求域：需求挖掘工具卡的反例节已引用颠覆创新时需求挖掘无效）

### 5. `case-feishu-disruptive-innovation` (当前 3 → ≥5)

已有 related：framework-christensen-disruptive-innovation, concept-christensen-rpv-model, bridge-christensen-reverse-mapping

需补 ≥2 条：
- → `framework-christensen-value-network`（本Wave内部：飞书开辟新价值网络）
- → `framework-yitang-oscar-research`（调研域：绕开主流而非超越——OSCAR的O可借鉴）

### 6. `case-english-teacher-ai-agent` (当前 4 → ≥5)

已有 related：concept-qinpeng-ai-as-amplifier, concept-qinpeng-knowledge-base-conversion, tool-qinpeng-ai-intelligent-service, framework-christensen-disruptive-innovation

需补 ≥1 条：
- → `tool-纪浩-Agent技能市场设计法`（Agent域：英语老师=个人Agent创建者的典型案例）
- → `case-live81-ai-trademark-design`（跨案：个人专家×AI=新服务品类，与Live81商标设计同模式）

### 7. `case-qinpeng-hardware-ai-amplification` (当前 3 → ≥5)

已有 related：concept-qinpeng-ai-as-amplifier, concept-qinpeng-knowledge-base-conversion, tool-qinpeng-ai-intelligent-service

需补 ≥2 条：
- → `framework-christensen-disruptive-innovation`（本Wave内部：上海合宙是破坏性创新的AI时代实例）
- → `concept-christensen-rpv-model`（本Wave内部：20年积累=Resources，AI放大=Process革新）

### 8. `dk-christensen-empirical-criticisms` (当前 2 → ≥5)

已有 related：framework-christensen-disruptive-innovation, concept-christensen-jtbd-link

需补 ≥3 条：
- → `dk-qinpeng-three-corrections`（本Wave内部：三纠正+实证批判=双重审视）
- → `dk-disruptive-innovation-insight-vs-survey`（本Wave内部）
- → `tool-科学决策关键训练清单`（决策域：实证批判=科学决策中的证据检验）

### 9. `concept-christensen-jtbd-link` (当前 3 → ≥5)

已有 related：dk-christensen-empirical-criticisms, framework-christensen-disruptive-innovation, bridge-christensen-reverse-mapping

需补 ≥2 条：
- → `case-demand-milkshake-jtbd`（需求域：奶昔案例是JTBD经典案例）
- → `yt-panproduct-execution-low-cost-mvp`（产品域：JTBD视角补充MVP验证的盲区）

## 验收标准

- [ ] 9张卡全部 related ≥5
- [ ] 每张卡 ≥2 条跨域链接（strategy/product/decision/demand/agent 域）
- [ ] 链接的卡必须真实存在（先 `search_files` 确认卡ID有效）
- [ ] 不用动正文，只改 frontmatter 的 related 列表

## 边界

- 本任务**只补 related，不改正文**。溯源/攻击者/失败模式已验证通过，不碰。
- Wave 1 三框架卡 + bridge + tool-qinpeng 已 ≥5，不在此次范围内。
- 与 #213 返工工单（P0-1~P0-4 结构修复）互不阻塞，可并行。
- 优先级 P1——不阻塞 #213 关闭，但应在下次复审前完成。
