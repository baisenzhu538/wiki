# 第二十五节验收报告：30 张高价值 draft 格式精修完成

**完成时间**：2026-06-18  
**执行人**：老顽童  
**审阅人**：欧阳锋  
**最终质量门禁**：`total=1200, p0=0, p1=19, clean=1181, yaml_error=0`

---

## 一、任务目标

从剩余 123 张高价值 draft 卡（conf≥0.7、related 非空、ASCII ID）中选取 **30 张**，按主题分 4 批次进行**格式精修**：补齐 metadata、status、source_refs、related、diagnostic_signals，确保全库 P0=0。

---

## 二、精修清单（30 张，status 均为 enriched）

| 批次 | 主题 | 数量 | 卡片 ID |
|:---|:---|:---:|:---|
| 1 | 一堂预判/研究/管理 | 8 | `yt-foresight-ten-fatal-flaws`、`yt-management-scientific-meetings`、`case-zhangyang-anchor-sop-three-locks`、`dk-ai-entrepreneur-technical-blindspot`、`dk-foresight-tier-skip-illusion`、`framework-course-milestone-model`、`yt-research-mindset`、`yt-research-user-jtbd` |
| 2 | AI 协作工具 | 8 | `tool-ai-skill-engineering-method`、`tool-iterative-recursive-deep-dig`、`sk-ai-ai-workspace-setup`、`sk-ai-evidence-check`、`sk-ai-landing-five-steps`、`sk-ai-narrative-test`、`sk-ai-parallel-validation`、`sk-ai-prd-for-ai` |
| 3 | 笔记/知识管理/个人成长 | 7 | `dk-note-maximum-common-divisor`、`dk-note-rookie-disaster-veteran-heaven`、`dk-note-surplus-brainpower`、`dk-truman-document-is-real-project-is-fake`、`dk-truman-flag-note-taking`、`dk-truman-knowledge-extraction-three-schools`、`yt-note-problem-solving-capability` |
| 4 | 建模/框架/AI 原生 | 7 | `dk-lz-ai-native-organization`、`dk-lz-code-is-disposable`、`dk-modeling-timely-review-session-window`、`dk-pseudo-demand-trap`、`dk-signal-cluster-illusion`、`dk-weekly-modeling-iteration-growth-engine`、`modeling-personal-practice-loop` |

---

## 三、格式精修标准落地情况

| 检查项 | 标准 | 落地情况 |
|:---|:---|:---|
| status | enriched / diagnostic | 30 张全部 enriched |
| 正文结构 | 用一句话讲清楚 / 核心要点 / 边界 / 失败模式表 / 行动 Checklist / 相关卡互链 | 全部补齐 |
| diagnostic_signals | ≥2 条 | 全部满足 |
| source_refs | `10_raw/sources/` 下真实路径；无法追溯时置空 + confidence≤0.89 | 全部补到有效路径或按规则控制 |
| reviewed_by | `欧阳锋`，不与 author 相同 | 全部合规 |
| 内部链接 | 使用 `[[id]]`，禁用别名 | 已修正 dangling/别名问题 |

---

## 四、过程中发现并修复的关键问题

### 1. 批次 3：YAML 中文引号转义错误

- **问题卡**：`dk-note-maximum-common-divisor.md`
- **现象**：diagnostic_signals 中 `"显著更好"` 未转义，导致 YAML 解析失败。
- **修复**：整条信号改用单引号包裹：`"显著更好"等效果描述来自主观对比……`

### 2. 批次 3/4：enriched 卡 source_refs 为空触发 P0

- **问题卡**：`dk-note-surplus-brainpower`、`dk-truman-document-is-real-project-is-fake`、`dk-lz-code-is-disposable`、`dk-pseudo-demand-trap`、`dk-signal-cluster-illusion`
- **修复**：
  - `dk-note-surplus-brainpower` → 补 `AI时代清单体笔记-Truman-口述-01/02`
  - `dk-truman-document-is-real-project-is-fake` → 补 `一堂-知识萃取探索营.md`
  - `dk-lz-code-is-disposable` → 补 `yc-AI-native 组织方法论` + `2298战队-AI组织落地探索`
  - `dk-pseudo-demand-trap` → 补 `一堂-关键假设课-truman-口述` + `一堂五步法-需求-跑步机案例-需求分析图`
  - `dk-signal-cluster-illusion` → 补 `一堂-机会预判课-Truman-口述` + `一堂-机会预判-三维排列组合01`

### 3. 批次 4：wikilink 别名导致 dangling

- **问题卡**：`dk-pseudo-demand-trap.md`
- **现象**：正文中使用 `[[yt-ai-startup-20-risky-hypotheses|20条高风险假设清单]]` 等别名链接，被门禁识别为 dangling。
- **修复**：全部改为简单链接 `[[yt-ai-startup-20-risky-hypotheses]]`、`[[yt-entrepreneur-key-hypotheses]]`。

---

## 五、质量门禁趋势

| 节点 | total | P0 | P1 | clean | yaml_error |
|:---|:---:|:---:|:---:|:---:|:---:|
| 批次 1 后 | 1199 | 0 | 21 | 1178 | 0 |
| 批次 2 后 | 1199 | 0 | 21 | 1178 | 0 |
| 批次 3 后 | 1199 | 0 | 21 | 1178 | 0 |
| 批次 4 修复前 | 1200 | 3 | 20 | 1180 | 0 |
| **最终** | **1200** | **0** | **19** | **1181** | **0** |

> P1=19 为历史基线问题（多为早期 draft/source 缺失卡），不在本批次目标范围内，未新增 P1。

---

## 六、域间自检三问

### 1. 案例够了吗？

本批次 30 张卡以概念、暗知识、工具、框架为主，案例卡仅有 2 张（`case-zhangyang-anchor-sop-three-locks` 以及前序批次中的少量 case）。**案例密度偏低**。建议下一批优先补 5-8 张与建模工具、AI 协作工具直接配套的实战 case 卡，形成“工具→信号→失败模式→案例”的完整调用链。

### 2. 暗知识在哪里？

本批次涌现的跨域暗知识模式：

- **"把 AI/工具当成分阶段校验器，而不是一次性生成器"**：在 AI 协作工具、建模、笔记多个域反复出现。
- **"模型/框架是提问的脚手架，不是答案"**：建模系列与一堂预判/研究工具形成共识。
- **"清单体是人与 AI 的最大公约数"**：笔记批次 7 张卡围绕 Truman 清单体训练形成技能链。

这些模式已部分固化为独立 dk 卡（如 `dk-tool-as-phased-validator`、`dk-modeling-question-scaffold-not-answer`），但仍有 2-3 条可在下一批进一步独立建卡。

### 3. 这些工具有共同失效根因吗？

跨批次共同的失败根因：

- **工具当作答案**：拿到清单/模型/框架后直接填表，不回头验证前提假设。
- **信号重复计数**：把相关信号、相关风险当成独立证据，导致过度自信。
- **基本功未内化就强上高阶操作**：笔记/建模/AI 协作均出现“跳过 L1-L2 直接 L4”的失败模式。

---

## 七、后续建议

1. **补案例卡**：下一批优先产出 5-8 张与 `modeling-*`、`tool-*`、`sk-ai-*` 直接配套的实战 case 卡。
2. **固化跨域 dk 卡**：将“基本功未内化就强上高阶操作”这一跨域失败根因独立建卡。
3. **清理 P1 基线**：历史 P1=19 中，大量为早期 concept/framework source_refs 为空。可集中一次“source 溯源 sprint”，或统一降级为 diagnostic。
4. **持续监控别名链接**：本次发现 alias wikilink 是 dangling 的主要来源，建议在格式精修 SOP 中明确禁用 `[[id|别名]]`。

---

## 八、验收结论

✅ **第二十五节 30 张高价值 draft 格式精修全部通过。**  
✅ **全库 P0=0，YAML 错误=0，未新增 P1。**  
✅ **可进入下一节任务。**
