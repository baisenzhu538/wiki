---
id: task_20260713_wangyuyan-decision-coach-engine-upgrade
assignee: huangyaoshi
status: reviewed
updated_at: '2026-07-13T12:52:04.247890+00:00'
reviewed_by: 欧阳锋
review_date: '2026-07-13'
grade: A
---
# Task #178 · B 域科学决策教练 spec 升级（#153 对话引擎化）

- **状态**：queued
- **负责人**：黄药师
- **优先级**：HIGH
- **依赖**：#177 reviewed（引擎协议卡先行）
- **依据**：黄药师建议书 `00_inbox/Handle the business/conversion rate/_vlm_output/任务编排建议书_王语嫣_科学决策agent升级_黄药师.md`（王语嫣已基本采纳）+ YAI 对话实录

## 目标
升级 #153 产出的科学决策教练 agent-spec：从「角色+工具清单」升级为「对话引擎」——引用 `method-一堂-教练对话引擎协议`，补 B 域四件套。

## 升级内容
1. **对话流程章**：引用引擎协议卡 M0-M8，不重抄流程，只写 B 域映射（里程碑 A=决策三角形宽度展开；高度扫描= `yt-decision-height-toolkit` 四维；深度分级= `yt-decision-depth-ladder` L1-L4）
2. **B 域盲区库聚合**（建议书 §3.2 表起步，可扩展）：知识产权/协议盲区（"道理说得通，纸上是空的"）/合作方动机盲区（"对方要的是你的人还是你的底牌"，挂 `dk-yitang-Y-model-pitfalls`）/精力分散盲区/家庭健康盲区——聚合为 agent checklist
3. **三 pattern 注入**：选项合并/底牌资产盘点/硬约束识别（B 域实例：负债压力→爬坡期不可行）
4. **边界条款**：遇效率问题（C/D 域）或生死问题（A 域）转介对应教练；L4 财务公式深度指 `tool-yitang-business-formula-quant-space-3d` 等既有工具卡
5. 保留 #153 既有成果：TCPR 身份声明/Y 模型 OS 底座/三角形+ABCD+ROI+共识曲线挂载不动

## 不做（建议书 §3.3）
- ❌ 不新建 agent spec（升级现有文件）
- ❌ 不改科学决策域方法论卡
- ❌ 不复制 YAI 全部功能

## 验收口径
- spec 升级后具备完整对话流程（可被实测：给一个决策问题能跑完 M0-M8）
- 预检 PASS，扫窗申报=实动集；待王语嫣审查后 pending_review

## 扫窗申报
改动文件清单+盲区库条目清单+未解决疑点

---

## 终审记录（欧阳锋 · 2026-07-13 · 结论：PASS / A）

### 复验结果

| 验收项 | 方法 | 结果 |
|:---|:---|:---|
| 对话流程章 M0-M8 | 读 agent spec §四 | 引用 `method-一堂-教练对话引擎协议`，B 域映射完整（M0-M8 + 挂载卡）✅ |
| B 域盲区库 | 读 agent spec §五 | 7 条盲区（知识产权/合作方动机/精力分散/家庭健康/选项遗漏/时间窗口/退出成本）✅ |
| 三 pattern 注入 | 读 agent spec §四 | 选项合并/底牌资产盘点/硬约束识别均有 YAI 实例 ✅ |
| 域五件套 | 读 System Prompt | 段位体系+盲区库+工具卡清单+边界条款+TCPR 身份子集 ✅ |
| System Prompt 重写 | 读 agent spec §七 | 引用引擎协议 OS 层 + TCPR + B 域铁律 ✅ |
| #153 既有成果保留 | 读 frontmatter + §一/§八 | TCPR 身份声明/Y 模型 OS 底座/决策三角形挂载均保留 ✅ |
| pre-submit | `kdo pre-submit -f .agent/prompts/agent-一堂-科学决策教练.md` | PASS ✅ |
| 全库 lint | `kdo lint --summary` | #178 单文件 0 error 0 warning；全库 8 error / 18 warning 均来自其他进行中的 D 域案例卡，非 #178 引入 ✅ |

### 欧阳锋评语

升级动作干净、scoped：只动 `.agent/prompts/agent-一堂-科学决策教练.md` 一个文件，从「角色+工具清单」升级为「对话引擎」。

亮点：
- M0-M8 映射不抄引擎协议原文，只写 B 域具体动作和挂载卡；
- 盲区库 7 条有来源（YAI 行号 / `dk-yitang-Y-model-pitfalls`）；
- System Prompt 把 OS 层、TCPR、B 域铁律、域五件套四层叠清楚；
- 保留了 #153 的 TCPR/Y 模型/三角形等既有资产。

**等级**：A（单文件、一次成型、接口清晰、pre-submit 干净）

**终审操作**：
- 已通过 `queue_transition.py review task_20260713_wangyuyan-decision-coach-engine-upgrade --verdict pass --reviewer 欧阳锋 --grade A` 更新队列与任务单状态；
- 队列状态：`待领取 9 / 审查中 0 / 进行中 1 / 已完成 171`。

*欧阳锋 2026-07-13 · #178 终审释放*
