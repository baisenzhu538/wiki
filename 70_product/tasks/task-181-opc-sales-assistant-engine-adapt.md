---
id: task_20260713_wangyuyan-opc-sales-assistant-engine-adapt
assignee: huangyaoshi
status: pending_review
updated_at: '2026-07-13T14:07:02.339632+00:00'
---
# Task #181 · OPC 销售对话助手引擎适配（参谋型裁剪版）

- **状态**：queued
- **负责人**：黄药师
- **优先级**：MEDIUM
- **依赖**：#177 reviewed（引擎协议卡）+ #169 reviewed（D 域 12 阻力卡先行）
- **依据**：`tool-opc-sales-dialogue-assistant`（reviewed，已加载 Y 模型 OS）+ `method-一堂-教练对话引擎协议`（#177）+ 王语嫣裁定：参谋型 agent 不全搬教练型里程碑，注入三件套

## 背景裁定（王语嫣）
YAI 对话引擎=教练型（多轮引导）；OPC 销售对话助手=参谋型（单次输入输出）。全搬 M0-M8 会拖慢参谋响应。适配方案=注入三件套，里程碑流程不搬。

三层架构定位（老朱 7-13 裁定）：D 域=场景无关方法论底座；OPC 销售域=销售场景应用层；销售对话助手=应用层的 1v1 参谋。D 域不只服务销售（运营/市场/产品同为转化率场景）——助手边界条款须声明：非销售转化率问题（私域运营/详情页/投放落地页等）→转介 D 域教练（#172），助手不假装覆盖全域。

## 适配内容（三件套）
1. **盲区库补漏**：System Prompt 的「抗拒点识别规则」升级为对照 D 域 12 阻力清单逐条过筛（觉得贵/没能力/没时间/门槛高/距离远/不靠谱/有风险/折面子/不专业/体验差/怕冲动/还不急），输出标注客户顾虑命中哪几条阻力+对应消除策（挂 `tool-一堂-阻力消除12策小抄`）
2. **硬约束识别**：输出第四段「风险提示」前增加显式宣告——当客户抗拒信号明确时，输出「⛔ 当下不该推：理由+建议等待的信号」（现有原则 3 升级为显式输出项）
3. **深度分级**：Input Format 增加可选字段「分析深度：快速判断（默认）/深度策略」，深度策略档才展开动力三曲线分析（FAB/名利权情/影响力是否用对层级）
4. 加挂 D 域卡到域层 related：12 阻力总表/12 策小抄/动力三曲线（#169/#170 产出后替换占位）

## 不做
- ❌ 不搬 M0-M8 里程碑流程（参谋型不需要多轮引导）
- ❌ 不改四段输出结构（已实测验证，#50）
- ❌ 不动军团其他 7 张 agent-spec（本任务只适配对话助手 MVP）

## 验收口径
- 适配后 spec 可实测：贴一段含明显阻力的客户对话，输出能命中阻力编号+消除策+硬约束宣告
- 预检 PASS，扫窗申报=实动集；待王语嫣审查后 pending_review

## 扫窗申报
改动清单+实测样例输出+术语疑点

---

## 终审记录 · 欧阳锋 · 2026-07-13

**结论：FAIL，返工。**

用户自称 "GATE PASSED"，但独立复验发现三件套未真正落到可执行 System Prompt，且 D 域卡未挂。

### 发现的问题

1. **System Prompt 模板未同步更新（关键）**
   - 源文件 `30_wiki/tools/tool-opc-sales-dialogue-assistant.md` 的正文说明部分已注入：
     - 12 阻力清单输出格式示例（L127）
     - 4. 硬约束宣告（L143）
     - 5. 深度分级（L150）
   - 但同文件内的 **System Prompt 模板（L212–271）** 仍是旧四段结构：
     - `# Output Format` 只要求四部分（1.客户意图与阶段判断 / 2.下一步建议 / 3.回复选项 / 4.风险提示）
     - `# Input Format` 只有 5 项，无「分析深度：快速判断/深度策略」
     - 无「⛔ 当下不该推」显式宣告
   - 运行时加载的是 System Prompt 模板，三件套在此模板中不生效。

2. **D 域卡未加挂（关键）**
   - 任务单要求加挂：12 阻力总表 / 12 策小抄 / 动力三曲线。
   - 实际 frontmatter `related` 只新增 2 项：`method-一堂-教练对话引擎协议`、`case-yitang-yai-conversion-rate-visit-rate`。
   - `domain_sources` 仍为 4 张旧工具卡，未加入 D 域卡。

3. **编译产物未同步**
   - `.agent/prompts/tool-opc-sales-dialogue-assistant.md` 仍是基于旧源文件编译（hash `783a9f6e4be9`），未包含本次正文修改。
   - 重新编译后 token 约 29k，但 domain_sources 仍只有 4 个。

4. **结构口径冲突**
   - 任务单明确「不改四段输出结构」，但正文说明已扩展为 5 段（新增 4.硬约束宣告、5.深度分级）。
   - 若 System Prompt 模板同步更新为五段，则与「不改四段输出结构」矛盾；若保留四段，则三件套需整合进现有四段内。

5. **情绪/抗拒点识别规则表未升级**
   - 表格仍是旧 5 条通用规则（反复问价格 / 已读不回 / 提及竞品 / 强调风险 / 催促快速落地）。
   - 任务单要求「对照 D 域 12 阻力清单逐条过筛」，规则表本身未升级。

### 返工要求

1. 在 System Prompt 模板中同步注入三件套：
   - Input Format 增加「分析深度：快速判断（默认）/深度策略」
   - Output Format 明确输出硬约束宣告「⛔ 当下不该推：理由 + 等待信号」
   - 情绪/抗拒点识别规则表升级为 12 阻力清单逐条映射
2. frontmatter 加挂 D 域卡：
   - `related` 增加：`framework-一堂-12种阻力总表`、`tool-一堂-阻力消除12策小抄`、`framework-一堂-动力三曲线`
   - `domain_sources` 增加上述三张卡的相对路径
3. 重新编译 `.agent/prompts/tool-opc-sales-dialogue-assistant.md`
4. 明确四段/五段结构：要么把新增内容收进现有四段，要么向王语嫣申请修改「不改四段输出结构」的裁定
5. 返工后重新跑 `kdo pre-submit` 并提交编译产物

**状态**：`pending_review` → `in_progress`，退回黄药师返工。

---

## 终审记录 · 欧阳锋 · 2026-07-13（重提复验）

**结论：仍 FAIL，继续返工。**

### 本次复验发现

1. **System Prompt 模板三件套已注入 ✅**
   - Input Format 增加第 6 项「分析深度：快速判断（默认）/ 深度策略」
   - Output Format §1 抗拒点已改为「对照 D 域 12 阻力清单逐条过筛」
   - §4 风险提示已合并硬约束宣告「⛔ 当下不该推：理由 + 建议等待的信号」
   - 四段结构保持，未新增第五段 ✅

2. **frontmatter `related` 已加挂 3 张 D 域卡 ✅**
   - `framework-一堂-12种阻力总表`
   - `tool-一堂-阻力消除12策小抄`
   - `framework-一堂-动力三曲线`

3. **`domain_sources` 格式错误导致编译器崩溃 ❌（关键）**
   - 当前 `domain_sources` 使用 TODO 占位符：
     ```yaml
     - <<<TODO: 30_wiki/frameworks/framework-一堂-12种阻力总表.md #169>>>
     - <<<TODO: 30_wiki/tools/tool-一堂-阻力消除12策小抄.md #170>>>
     - <<<TODO: 30_wiki/frameworks/framework-一堂-动力三曲线.md #169>>>
     ```
   - `<<<` 在 YAML 中是 merge key 语法，被解析为 `dict`，导致 `agent-prompt-compiler.py` 崩溃：
     ```
     TypeError: unsupported operand type(s) for /: 'WindowsPath' and 'dict'
     ```
   - 生产队列显示 #169、#170 已 `reviewed`，D 域卡已存在，不应再以 TODO 占位。

4. **编译产物未真正同步 ❌（关键）**
   - 用户称「.agent/prompts/tool-opc-sales-dialogue-assistant.md 已更新」。
   - 实际文件被删到只剩 86 行（git diff: -2018 行），内容开头直接是「边界与风险提示」，OS 层/域层/System Prompt 模板全部丢失。
   - 我已将 `.agent/prompts/tool-opc-sales-dialogue-assistant.md` 撤销回旧版本（2103 行，基于 7月5日源文件），但仍是旧编译产物，未包含本次三件套更新。

### 返工要求

1. 把 `domain_sources` 中的 3 个 TODO 占位符替换为真实相对路径：
   - `30_wiki/frameworks/framework-一堂-12种阻力总表.md`
   - `30_wiki/tools/tool-一堂-阻力消除12策小抄.md`
   - `30_wiki/frameworks/framework-一堂-动力三曲线.md`
2. 重新运行 `python kdo-tools/agent-prompt-compiler.py tool-opc-sales-dialogue-assistant`
3. 验证 `.agent/prompts/tool-opc-sales-dialogue-assistant.md`：
   - 文件行数应 ≈ 2300 行（不是 86 行）
   - 包含新的 System Prompt 模板（Input Format 有第 6 项、Output Format §1 有 12 阻力清单、§4 有硬约束宣告）
   - `domain_sources` 列出 7 个源文件
4. 重新跑 `kdo pre-submit -f 30_wiki/tools/tool-opc-sales-dialogue-assistant.md .agent/prompts/tool-opc-sales-dialogue-assistant.md`
5. 提交编译产物

**状态**：`pending_review` → `in_progress`，继续返工。
