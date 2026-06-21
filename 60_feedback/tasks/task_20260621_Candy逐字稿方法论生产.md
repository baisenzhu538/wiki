---
id: "task_20260621_Candy逐字稿方法论生产"
type: "production_task_list"
created_at: 2026-06-21
author: "王语嫣（综合欧阳锋裁决）"
executor: "老顽童"
source_path: "缓存 → 00_inbox/拆书会Candy_ProblemOS是如何诞生的.md（老顽童搬运）"
---

# 生产任务：Candy 逐字稿方法论（4 框架 + 1 案例 + 1 附录）

> 欧阳锋裁决：4 🟢 通过 + 1 case 独立 + 1 并入附录。

---

## 源文件

| 状态 | 说明 |
|:---|:---|
| ⏳ 待老顽童搬运 | 缓存 → `00_inbox/拆书会Candy_ProblemOS是如何诞生的.md` |
| 搬运后归档 | → `10_raw/sources/src_20260621_candy-transcript-workflow.md` |

---

## 任务 1：四张核心卡

### C-1：framework-candy-transcript-workflow

- **路径**：`30_wiki/frameworks/framework-candy-transcript-workflow.md`
- **类型**：framework
- **核心内容**：
  - 9 步逐字稿生产流程（搭参考系→差异化定位→框架先成立→案例激活→案例服务结构→标题校准→配图是结构→口语化润色→AI是协作者）
  - 每一步：输入/动作/产出/自检问题
  - 关键原则（单独列出）：不急着写、差异化优先、骨架>文采、案例逼出观点、配图是结构
  - §参考案例：C-6 Problem OS 构建过程摘要（2-3 段简述 9 步在 Problem OS 中的对应）
- **Agent 执行指令**：9 步 Prompt 链（每一步的 Agent 输入模板）
- **失败模式**：跳过参考系直接写/案例堆砌不服务结构/润色太早/主语漂移
- **关联链接**：
  - → `concept-candy-ai-as-collaborator`
  - → `tool-candy-positioning-canvas`
  - → `tool-candy-oral-polish`
  - → `case-candy-problem-os-vpn`
- **素材来源**：`src_20260621_candy-transcript-workflow.md`（归档后路径）

### C-2：tool-candy-positioning-canvas

- **路径**：`30_wiki/tools/tool-candy-positioning-canvas.md`
- **类型**：tool
- **核心内容**：
  - 差异化定位画布——回答"这篇东西凭什么存在"
  - 四象限：已有内容（左）→ 我的内容（右）/ 相同点（上）→ 差异点（下）
  - 核心命名：不要只讲材料，给它一个课程级概念（如"Problem OS"而非"ESR聪明提问"）
  - 自检问题：如果听众只记住一句话，应该是哪句？
- **Agent 执行指令**：定位画布 Prompt 模板
- **失败模式**：差异是伪差异/定位太窄/命名太大
- **关联链接**：
  - → `framework-candy-transcript-workflow`（Step 2）
- **素材来源**：同上

### C-3：concept-candy-ai-as-collaborator

- **路径**：`30_wiki/concepts/concept-candy-ai-as-collaborator.md`
- **类型**：concept
- **核心内容**：
  - AI 是协作对象而非代写工具——人机分工表

    | 人负责 | AI 负责 |
    |:---|:---|
    | 方向判断 | 整理、抽象、扩写 |
    | 真实案例 | 归位、润色 |
    | 指出"哪里不像我" | 生成不同版本 |
    | 决定保留/删除 | 学习已有风格 |

  - 关键原则：方向感必须是人的，AI 可以跑很快但不知道往哪跑
  - 与王欢 Harness 的同构：Generator 执行/Evaluator 评审/人做方向判断
- **关联链接**：
  - → `framework-wanghuan-gan-three-roles`（同构——AI 协作哲学）
  - → `concept-harness-cattle-not-pets`（共同原则：方向感在人的判断）
  - → `framework-candy-transcript-workflow`（Step 9）
- **素材来源**：同上

### C-4：tool-candy-oral-polish

- **路径**：`30_wiki/tools/tool-candy-oral-polish.md`
- **类型**：tool
- **核心内容**：
  - 口语化润色指令集（从 Candy 总结的 7 条原则）
  - 每条的对比示例（原文 → 润色后）
  - 原则：短句有呼吸感 / 口语连接词 / 场景先于道理 / 术语后人话 / 保留人设 / 不改有力量的原句 / 结构稳定后才润色
- **Agent 执行指令**：口语化润色 Prompt 模板（带对比示例）
- **失败模式**：润色变重写/磨平人设/术语全删导致不专业
- **关联链接**：
  - → `framework-candy-transcript-workflow`（Step 8）
- **素材来源**：同上

---

## 任务 2：案例卡

### C-5：case-candy-problem-os-vpn

- **路径**：`30_wiki/cases/case-candy-problem-os-vpn.md`
- **类型**：case
- **核心内容**：
  - 场景：同事问"线下数据库同步线上主库，怎么在家访问"
  - 问题链：回答 VPN → 面露难色（担心冲突但不直说）→ 追问安全性和数据风险 → 暴露其实不理解"线下"和"同步"的含义
  - 映射到方法论：Problem OS 的核心痛感——提问者没定义清楚问题、回答者预判了顾虑但对方不信任、一次低质量提问消耗双方关系
- **关联链接**：
  - → `framework-candy-transcript-workflow`（Step 4 案例激活）
  - → `concept-candy-ai-as-collaborator`（共同原则）
- **素材来源**：同上 + 原文 §第四步

---

## 任务 3：已有卡更新（C-6 并入 C-1）

### 更新：framework-candy-transcript-workflow

在 C-1 末尾追加 §参考案例：

```markdown
## 参考案例：Problem OS 的诞生

Candy 用 9 步法完成了《Problem OS——用 ESR 的提问智慧，构建你的问题操作系统》逐字稿：

| 步骤 | 在 Problem OS 中的对应 |
|:---|:---|
| 1 搭参考系 | 整理 ESR 原文+译本+《学会提问》拆书会+情报调研课+MBA 提问课 |
| 2 差异化定位 | 从"ESR 聪明提问拆书会"→"Problem OS 问题操作系统" |
| 3 框架先成立 | 四层能力栈（L1 提问基础→L2 注意力交易→L3 问题工程化→L4 信用管理） |
| 4 案例激活 | VPN 与线下数据库——详见 `case-candy-problem-os-vpn` |
| 5 案例服务结构 | X-Y Problem / 假设池 / 菜鸡互啄 / LLM 迎合偏见——每个案例落在一个论证位置 |
| 6 标题主语校准 | 从"ESR 很厉害"→"Problem OS 对你有用" |
| 7 配图是结构 | 路线图/四层能力栈/注意力交易图/问题工程化图——每张图承担认知导航 |
| 8 口语化润色 | 学习一堂逐字稿口语特征，短句+连接词+场景先行 |
| 9 AI 是协作者 | 人负责方向/案例/判断/删改，AI 负责整理/抽象/润色 |
```

---

## 任务 4：跨域桥接

新卡创建后补反向链接：

| 操作 | 文件 |
|:---|:---|
| `framework-wanghuan-gan-three-roles` related → 链 `concept-candy-ai-as-collaborator` | 已有王欢卡 |
| `concept-harness-cattle-not-pets` related → 链 `concept-candy-ai-as-collaborator` | 已有 Harness 卡 |

---

## 卡片质量标准

每张卡必须包含：
- [ ] 一段话讲清楚
- [ ] Agent 执行指令（Prompt 模板或步骤链）
- [ ] 失败模式表
- [ ] 适用边界
- [ ] 跨域桥接（related 链接到另一域）
- [ ] source_refs 用 `10_raw/sources/` 路径

---

*王语嫣综合欧阳锋裁决 | 2026-06-21 | 黄药师可选后续 Skill 化*
