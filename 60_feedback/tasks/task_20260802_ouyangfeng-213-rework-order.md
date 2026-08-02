---
id: task_20260802_ouyangfeng-213-rework-order
type: rework_order
task_id: 213
assignee: laowantong
status: open
created_at: 2026-08-02
priority: P0
source: task_20260802_wangyuyan-innovators-dilemma-qinpeng
---

# #213 结构修复工单

> **来源**：欧阳锋终审 FAIL（2026-08-02，本终端 + 飞书两实例交叉验证一致）
> **优先级**：P0——已等一轮，直接修复
> **修复人**：老顽童
> **修复原则**：✅ **内容一个字不动，只补结构**。溯源/攻击者/失败模式/定位声明已全部达标，不需要碰正文论述。

---

## 一、总览

要修 **4 类结构问题 × 9 张卡**。其余 5 张卡（bridge / 2×framework / rpv / tool-qinpeng）已完全达标，**不用动**。

| 问题类型 | 数量 | 涉及卡 |
|:--|:--|:--|
| P0-1 `## Critque` 拼写错误 | 3 处 | case-feishu / dk-empirical / concept-jtbd |
| P0-2 dk 缺 `## Critique` 节 | 1 | dk-qinpeng-three-corrections |
| P0-3 case 缺可迁移场景/教训段 + 英文标题 | 3 | 全部 case 卡 |
| P0-4 concept 缺 `## Synthesis` 节 | 3 | 2 张秦鹏 concept + concept-jtbd |

---

## 二、逐文件修复清单

### P0-1：`## Critque` → `## Critique`（3 处，改一个字）

| 文件 | 行号 | 改动 |
|:--|:--|:--|
| `30_wiki/cases/case-feishu-disruptive-innovation.md` | L56 | `## Critque` → `## Critique` |
| `30_wiki/dk/dk-christensen-empirical-criticisms.md` | L99 | `## Critque` → `## Critique` |
| `30_wiki/concepts/concept-christensen-jtbd-link.md` | L76 | `## Critque` → `## Critique` |

> 全库 `grep "## Critque"` 应返回 0。

---

### P0-2：`dk-qinpeng-three-corrections.md` 补 `## Critique` 节

dk 卡七段标准（原始表述/使用场景/操作方法/适用边界/为什么值钱/与其他知识的关联/**Critique**），当前缺 Critique。

**做法**：把正文纠正③里已有的"反方视角"（员工/供应商/社区 blockquote，L71-76）升级为独立标准 `## Critique` 节。可补充：
- 内部局限：纠正③（公司死亡不是坏事）是价值判断非商业事实，作为决策依据有伦理风险
- 外部视角：Schumpeter 创造性破坏支持侧 vs 员工/社区受损侧的对立

> 已有内容不要删，只整理进标准节。

---

### P0-3：3 张 case 卡补标准段

case 卡标准四段：**关键证据 / 可迁移场景 / 教训 / 失败模式**。当前缺可迁移场景、教训。

#### `case-feishu-disruptive-innovation.md`
- `## Critque` → `## Critique`（P0-1 已列）
- 补 `## 可迁移场景`：什么条件下其他产品可以用"绕开核心赛道"策略
- 补 `## 教训`：正反观点争议说明——判断破坏性创新要看产品内核而非功能
- 补 `## 失败模式`：把案例判断误用为确定结论的风险

#### `case-english-teacher-ai-agent.md`
- `## Failure Modes` → `## 失败模式`（英文标题改中文）
- 补 `## 可迁移场景`：个人专家 → AI 服务路径可复制到哪些职业
- 补 `## 教训`：可复制性的前提是真实行业积累

#### `case-qinpeng-hardware-ai-amplification.md`
- `## Failure Modes` → `## 失败模式`（英文标题改中文）
- 补 `## 可迁移场景`：硬件/制造业 AI 转型的参考路径
- 补 `## 教训`：单源案例的数字（10倍效率）不可直接照搬

> 内容从现有正文/源素材提取，不要新编数字。

---

### P0-4：3 张 concept 卡补 `## Synthesis` 节

concept 三步编译法（浓缩/质疑/**对标**），当前缺对标（Synthesis）。

#### `concept-qinpeng-ai-as-amplifier.md`
补 `## Synthesis`：AI 放大器论与 `tool-qinpeng-ai-intelligent-service` 四特征的关系——放大器论是前提，四特征是落地；与 Brynjolfsson"AI 创造新能力"的互补/矛盾定位。

#### `concept-qinpeng-knowledge-base-conversion.md`
补 `## Synthesis`：知识库转化 vs 秦鹏放大器论的上下游关系；与 `concept-qinpeng-ai-as-amplifier` 形成"前提→落地"链条；冷启动困境（20年 vs 3-5年）的边界提醒。

#### `concept-christensen-jtbd-link.md`
补 `## Synthesis`：JTBD 是破坏性创新理论的演化而非替代；与 `dk-christensen-empirical-criticisms` 的呼应（JTBD 部分回应实证批判）；与 `case-demand-milkshake-jtbd` 的概念-案例闭环。

> Synthesis = 本卡和其他卡的**关系定位**（互补/矛盾/可迁移），不是重复核心结构。

---

## 三、非阻塞建议（验收 #7 related ≥5）

9/14 卡 related < 5，验收标准 #7 违约。**不阻塞本次复审**，但建议顺手补：
- 用 `bridge-christensen-reverse-mapping` 四列映射表反向补链到已存在 yt-* / 需求域 / 决策域卡（≥2 跨域）
- wave 1 三框架卡入 index 后 related 会自然增长

---

## 四、验收标准（修完自查）

```
1. grep "## Critque" 30_wiki → 0 命中
2. grep "## Failure Modes" 30_wiki/cases/case-english-teacher-ai-agent.md 等 → 0 命中
3. 每张 case 卡：可迁移场景 + 教训 + 失败模式 三段齐全
4. 每张 concept 卡：Synthesis 段存在且非空
5. dk-qinpeng-three-corrections：Critique 段存在且非空
6. 跑 kdo pre-submit，附输出（注意：pre-submit 不查 section 名拼写，以 1-5 人工核对为准）
```

---

## 五、提交要求

1. 修完按上述验收自查，确认 1-5 全绿
2. 重新提交 `pending_review`（更新 production-queue.md 状态列）
3. 欧阳锋快速复审（只看修复点，溯源已通过不再重复）
4. **本次提醒**：上次在结构未修复的情况下直接重新提交，浪费了一轮审查往返。本次修完再提。

*欧阳锋 · 2026-08-02*
