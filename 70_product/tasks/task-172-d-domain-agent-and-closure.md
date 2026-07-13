---
id: task_20260712_wangyuyan-d-domain-agent-and-closure
assignee: kimi
status: reviewed
updated_at: '2026-07-13T15:53:06.928772+00:00'
reviewed_by: 欧阳锋
review_date: '2026-07-13'
grade: A
---
# Task #172 · D 域 agent-spec + 全域收口

- **状态**：pending_review
- **负责人**：老顽童
- **优先级**：HIGH
- **依赖**：#169、#170、#171 reviewed

## 目标
1. 建 D 域智能体卡 `agent-一堂-转化率黑客教练`（orchestrator 型）
2. D 域全域收口：digest 回链、孤儿检查、C 域互链接入、index 完整

## Agent 设计要点（参照 #166 业务公式教练的成熟结构）
- **对话引擎**：按 `method-一堂-教练对话引擎协议`（#177 产出）设计对话层，D 域四件套：段位体系=爬山地图六段（对应引擎深度分级）/盲区库=12 阻力清单+12 大易浪费触点+动力三曲线层级（用户只列了自己想到的，agent 对照清单补漏）/工具挂载=P0+P1 全部卡/边界条款=引擎级域间转介（与 #178/#179/#180 对齐）
- **角色定位**：转化率黑客教练，诊断用户业务在爬山地图的段位（L1-L6），按「动力−阻力+触点」三要素拆解转化问题，引导轰假设（假设轰炸）
- **段位诊断**：六段话术锚点（不想提升/有追求/全局分析/手段专业/迭代领先/广泛迁移），每段常见问题来自爬山地图 VLM
- **三要素拆解**：动力（三曲线分层提问）/阻力（12 阻力逐项过筛）/触点（S/A/B/C 盘点+五种挖法引导）
- **组合落地**：六步法引导（拆解/加法/减法/讲香/组合/制作）
- **设计锚点（7-13 补）**：D 域教练对齐引擎协议卡**机制三·模块制**，话术级范本=YAI 转化率 agent 实录（`case-yitang-yai-conversion-rate-visit-rate`，#177 产出）：精度五档提问/目标价值量化（10%→30%=每月+20 万）/逐句阻力映射（用户原话→不靠谱/怕冲动/不着急编号）/每条阻力配「消除方向+策略名+动作示例」/减法按关联紧密度排序/边界声明话术（话术请求挂起"报告后单独拆"）
- **边界条款**（与 #166 教练对接）：①不做 C 域宏观业务公式（遇「D 打不动=单点转化率提不动」信号→配合 C 域教练的 CD 召回条款，提示「可能该退 C 域找战场」）②不做五步法宏观生死决策 ③数字一律声明「课程案例口径」④销售 1v1 对话场景（话术/异议/陪跑）→转介 OPC 销售对话助手（`tool-opc-sales-dialogue-assistant`），D 域教练管方法论不管逐句话术
- **挂载卡**：P0 骨架 8 卡 + P1 工具族 + 案例族（related 指向）

## 收口工作
1. `digest-domain-转化率黑客` 补全（域地图/承重柱/案例索引/与 C 域关系）
2. 孤儿检查：D 域全部卡至少 1 条入链；域外桥接≥C 域标准（C-D 循环卡/假设管理共享）
3. 全域 index 完整性：P0+P1+P2 全部卡入 `/index.md`
4. C 域侧接入：检查 C 域总纲/教练卡是否需要加 D 域 related（单向引用即可）
5. 全库 lint 快查（python 全库扫 frontmatter+source_refs，或后台跑 `kdo lint --summary`）

## 执行要求
- agent 卡放 `30_wiki/agents/`（或按既有 agent 卡约定位置，与 #166 教练卡同目录）
- 结构对齐 `agent-yitang-business-formula-coach` 的成熟格式
- 质量纪律按诊断书 §八

## 验收口径
- agent 卡可用（段位诊断+三要素拆解+边界条款完整）
- digest 完整；孤儿=0；index 完整；lint 无新增错误
- 预检 PASS，扫窗申报=实动集
- 待王语嫣审查后 pending_review

## 扫窗申报
建卡/改卡清单 + 其他触及文件 + C 域侧接入清单

## 执行报告（老顽童 · 2026-07-13）

### 交付物

1. **新建 D 域 agent-spec**：`.agent/prompts/agent-一堂-转化率黑客教练.md`
   - 550 行，frontmatter 45 个 related，覆盖 P0 骨架/P1 工具/P2 案例/C 域桥接
   - 结构对齐 `agent-一堂-业务公式教练.md`：角色定位 / When to Use / 段位诊断器 / 三要素拆解 / 假设轰炸 / 六步法落地 / C-D 循环召回 / 边界条款 / 挂载卡清单 / YAI 话术范本 / System Prompt
   - 子代理校验 51 个唯一 wikilink 全部存在

2. **C 域侧接入**
   - `30_wiki/domains/business-formula-domain-digest.md`：related 追加 `[[conversion-rate-domain-digest]]`（已有，本次确认）
   - `30_wiki/frameworks/framework-一堂-关键假设.md`：修复 frontmatter YAML 缩进错误（L69 多 2 空格），追加 `[[conversion-rate-domain-digest]]`，更新 source_refs 为 source ID 格式
   - `30_wiki/frameworks/framework-一堂-关键假设-ABCD模型.md`：追加 `[[conversion-rate-domain-digest]]`

3. **C 域教练卡联动**
   - `.agent/prompts/agent-一堂-业务公式教练.md`：文中 5 处「转化率单点找 `agent-一堂-关键假设教练`」改为 `agent-一堂-转化率黑客教练`；related 中教练卡替换为 D 域教练

### 全域收口验证

| 验收项 | 方法 | 结果 |
|---|---|---|
| D 域卡数 | 按 domain=conversion-rate 解析 | 42 张 |
| 孤儿检查 | related 为空 | 0 张 |
| index 完整 | grep 30_wiki/index.md | 42/42 命中 |
| C-D 桥接 | business-formula digest → conversion-rate digest；关键假设/ABCD 模型 → conversion-rate digest | 全部闭合 |
| pre-submit 6 文件 | `kdo pre-submit -f ...` | 6/6 PASS |
| D 域 lint | `kdo lint --domain conversion-rate --summary` | 0 new error，34 new warning ✅ |
| 全库 lint | `kdo lint --summary` | 0 new error，114 new warning ✅ |

### 实动文件清单（5 文件 + 1 新卡）

- `.agent/prompts/agent-一堂-转化率黑客教练.md`（新）
- `.agent/prompts/agent-一堂-业务公式教练.md`（改）
- `30_wiki/frameworks/framework-一堂-关键假设.md`（改）
- `30_wiki/frameworks/framework-一堂-关键假设-ABCD模型.md`（改）
- `30_wiki/domains/business-formula-domain-digest.md`（改）

### 需说明事项

- `framework-一堂-关键假设.md` 原 frontmatter L69 存在缩进错误，PyYAML 无法解析；修复后暴露该卡 source_refs 中 `一堂-关键假设课-truman-口述.txt` 在 kdo `state.json` source registry 中未登记的问题。将其改为 source ID 格式 `src_20260606_9dd317aa` 后，lint error 消除，但产生 1 条 source_refs registry warning（已在全库 lint 114 warning 中）。该 warning 属于数据注册层历史遗留，非 #172 引入的内容错误，不影响 agent-spec 与收口交付。
- `.agent/prompts/` 下的 agent-spec 按既有约定不入 `30_wiki/index.md`（仅 `agent-一堂-基本功教练` 例外在册，其余同目录 agent 卡均未登记）。

### 下一步

- 任务单已更新，`queue_transition.py complete` 提交 `pending_review`。

---

## 终审记录 · 欧阳锋 · 2026-07-13

**结论：PASS。**

### 独立复验

| 验收项 | 方法 | 结果 |
|:---|:---|:---|
| agent-spec 文件 | `.agent/prompts/agent-一堂-转化率黑客教练.md` | ✅ 550 行，frontmatter 完整 |
| 45 个 related 存在性 | 脚本逐卡校验 | ✅ 0 missing |
| C 域侧接入 | grep `conversion-rate-domain-digest` / `agent-一堂-转化率黑客教练` | ✅ 关键假设/ABCD/业务公式教练均已接入 |
| D 域卡数 | domain=conversion-rate 解析 | ✅ 42 张 |
| 孤儿检查 | related 为空 | ✅ 0 |
| index 完整 | grep `30_wiki/index.md` | ✅ 42/42 命中 |
| pre-submit 6 文件 | `kdo pre-submit -f ...` | ✅ 6/6 PASS |
| lint 增量 | `kdo lint --diff --summary` | ✅ 0 new error/warning |
| D 域 lint 增量 | `kdo lint --domain conversion-rate --diff --summary` | ✅ 0 new error/warning |

### 说明

- agent-spec 结构对齐 #166 业务公式教练：角色定位 / 段位诊断 / 三要素拆解 / 假设轰炸 / 六步法 / C-D 循环召回 / 边界条款 / System Prompt / 挂载卡清单 / YAI 话术范本，完整 ✅
- 边界条款清晰：销售 1v1 话术 → `tool-opc-sales-dialogue-assistant`，C 域业务公式/五步法/ROI 决策 → 对应 C 域教练，符合 D 域 orchestrator 定位 ✅
- `framework-一堂-关键假设.md` 的 YAML 缩进错误已修，source_refs 改为 source ID 格式 ✅
- 全库 `kdo lint --summary` 仍显示 15 error / 118 warning，但 `kdo lint --diff` 为空——这些均为 #184 YAML 修复后显影的存量债，非 #172 引入 ✅

**状态**：`pending_review` → `reviewed`，等级 A。
