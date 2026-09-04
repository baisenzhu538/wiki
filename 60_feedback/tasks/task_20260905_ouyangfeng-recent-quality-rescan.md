---
id: task_20260905_ouyangfeng-recent-quality-rescan
title: 近期入库卡质量回扫（替代期 08-28 起至今）：抽审暗知识含量+一等证据锚，不只结构合规——老朱「担心入库变垃圾」直令
seq: 644
status: pending_review
assignee: ouyangfeng
created_by: wangyuyan
created_at: 2026-09-05
decision_source: 老朱 09-05 直令：担心这段时间入库内容被处理方式严重影响质量
reviewer: 王语嫣（编排层复核落点）
instance: ouyangfeng
updated_at: '2026-09-04T18:18:54.188459+00:00'
evidence: 60_feedback/tasks/task_20260905_ouyangfeng-recent-quality-rescan.md
---

# #644 近期入库质量回扫（欧阳锋）

## 背景

老朱担心：替代期以来入库内容质量被流水线化处理方式拉低。终审拦得住造假拦不住平庸——本单按「暗知识含量/一等证据锚/方向价值」三轴抽审，不是结构合规复查。

## 任务

1. 抽样框：08-28 至今 reviewed 的新卡（约 #584-#643 族产出，~30 张），按域分层抽 10 张
2. 每张三轴打分+一句话判词：暗知识含量（有新增量/只是重组）/ 证据锚（一等口述 vs 二手整理）/ 方向价值（值得生产吗）
3. 产出：回扫报告（含不合格清单+处置建议：降级/补强/维持）+ 系统性模式判词（如果平庸有共同根因）

## 边界

- 只审不动笔；处置归王语嫣编排
- 你有判定权，我不干预结论

## 交付

- 回扫报告落任务单 + complete 644

---

## 回扫报告（欧阳锋 · 2026-09-05 三轴抽审）

### 抽样框
- 08-28 起至今（09-05）`status: reviewed` 的新卡全库扫描：入窗 52 张（含 re-review 旧卡 14 张，created_at 落窗的新卡 38 张）；剔除 entity / agent-spec 2 张非知识卡后，知识卡抽样框 = 36 张（任务单"~30"为约数，实际框略大）。
- 按域分层抽 10 张：strategy 3 / content·sales 3 / ai-collaboration 3 / decision·strategy 1；类型覆盖 framework 3、case 3、dk 2、method 1、concept 1。

### 三轴评分（暗知识含量 / 证据锚 / 方向价值）

| # | 卡 | 暗知识含量 | 证据锚 | 方向价值 |
|:--|:--|:--|:--|:--|
| 1 | framework-popmart-long-termism-operating-philosophy | 中（原则重组 + "时间投入品记账法"增量） | 弱（转述二等，原书不在库） | 高 |
| 2 | case-popmart-molly-transition | 高（L1-L5 真增量："1/3 甜点位=绑架点"） | 中（二等 + 在线补验） | 高 |
| 3 | concept-satisfaction-vs-existence | 中（两轴提炼 + 理论同构待核） | 弱（转述二等 + 魏布伦/鲍德里亚对标存疑） | 中高 |
| 4 | framework-arui-ai-six-fundamentals | 中（重组 + 角色分层暗知识；2/6 块半成品） | 中（公众号正文直采） | 中高 |
| 5 | case-yitang-jiangxiang-huawei-matext-launch | 高（单场景深挖真增量） | 强（一等逐字稿 + 在线补验） | 高 |
| 6 | method-shizhi-jiangxiang-ten-strategies | 中（课程模型方法论化 + 先定靶再选指） | 强（一等逐字稿） | 高 |
| 7 | framework-course-thought-production-line | 高（"材料工程化"硬增量） | 中（口述 Candy 整理形态，唯一一手源） | 高 |
| 8 | case-wechat-article-workbuddy-selfmedia-pipeline | 中高（流程拆解 + 人工决策点主权） | 弱（二等 self-report，trust low） | 中高 |
| 9 | dk-brooks-cost-of-knowing | 高（三条真暗知识 + 攻击者论证） | 强（中译逐字稿） | 高 |
| 10 | dk-koupen-input-method-loss | 高（机制 + 归因反转增量） | 强（一手亲历） | 高 |

### 不合格清单与处置建议
- **无硬 FAIL / 无降级**——本批 10 张全部有 L 层深挖 + Synthesis/Critique，未见"只重组的平庸卡"。
- **补强（4 项，随王语嫣编排跟进）**：
  1. `framework-arui-ai-six-fundamentals`：半成品框架——AI 三基本中"提示词逻辑设计/分析校正"两块只有概念无细节，confidence 0.85 偏高 → 降 confidence 或挂"待连载补全"。
  2. `case-wechat-article-workbuddy-selfmedia-pipeline`：证据锚最弱（二等 self-report、trust low），核心数字（6h→30min、日更 22 篇+40%）未核实 → 补公开佐证，或明确降为 hypothesis 案例（卡内 quality_labels 已含 hypothesis，属诚实标注但应跟进）。
  3. `concept-satisfaction-vs-existence`：魏布伦/鲍德里亚理论对标为训练记忆内置、在线核实未完成 → 补验证。
  4. popmart 族 + 讲香族数字（356 倍/1000 亿/八九千万/净水器 1200 元/白酒 59000）卡内已自标注"待核实" → 纳入补强观察，不新增拦截。
- **维持（6 项）**：其余卡。

### 系统性模式判词（平庸有无共同根因）
- **暗知识层未平庸化**：本批 10 张普遍做到 L1-L5 深挖 + Synthesis + Critique，增量在线，不是"只重组"。
- **真实系统性风险在证据锚两级分化**：有逐字稿/口述的卡（讲香族、国帅、布鲁克斯、口喷）证据锚强；依赖"拆书提炼件/公众号/二手网络文章"的卡（popmart 族、阿蕊、WorkBuddy）证据锚弱，普遍走"转述二等 + 在线补验"或 self-report。
- **根因候选**：生产侧把"逐字读一等口述"替换为"转述提炼件"后，证据锚整体降级；终审拦得住结构合规、拦不住"数字未核实照录"这类事实层缺陷——数字自标注"待核实"已成默认操作，这是流水线化拉低质量的入口，也是"拦得住造假拦不住平庸"的具体形态。
- **建议方向（归王语嫣，非阻塞）**：对"转述二等/self-report 来源"的新卡，把"关键数字独立核验"从"自标注"提升为入库前必做项或至少终审抽查项。

### 边界
- 只审不动笔；处置归王语嫣编排；本报告为分层抽审判定，非全量终审。

---

## 执行报告（欧阳锋）

**交付物**：本任务单回扫报告 + 10 张三轴评分表 + 不合格清单 + 系统性模式判词。

**完成内容**：全库扫描 08-28 起 reviewed 新卡建立抽样框，按域分层抽 10 张，逐张读正文 + 打开 source_refs 源文件，按暗知识含量/证据锚/方向价值三轴打分并给一句话判词；输出不合格清单（无降级、4 项补强、6 项维持）与系统性模式判词。

**验证**：O0 溯源 10/10——10 张卡全部打开 source_refs 源文件，源文件存在率 10/10，行锚逐字命中（popmart L69-106/L33-37/L121-142、huawei L244-475、koupen L1810-1880、course L9/L215 等）。

**边界**：只审不动笔，处置归王语嫣编排；抽样为分层样本，非全量终审。

**需要谁动作**：王语嫣——接收处置建议，裁定 4 项补强是否立项跟进、是否接受"无降级"判定。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

⚪ 无路径级交付物声明（纯文档/诊断类或未用反引号标注路径）——差集无检查面
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
