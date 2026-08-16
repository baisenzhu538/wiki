---
id: task_20260809_laowantong-scientific-meeting-p1
assignee: kimi
status: reviewed
reviewed_by: 欧阳锋
review_date: '2026-08-09'
updated_at: '2026-08-09T09:33:25.284287+00:00'
priority: P1
wsjf: 2.5
grade: A
---

# 科学开会 P0 深化+补链（#286 · bridge×1 + dk×6 + 补链）

## 建模方案（出牌 · 老顽童 kimi 实例 2026-08-09）

`[#3 先口述稿再笔记] → [#6 先查已有卡再新建] → [#9 先 framework 再 concept（#285 已就位）] → [#10 先骨架再填肉（dk 六节标题机械规范）] → [#15 先自攻击再提交] → [#16 先 lint 再 pre-submit]`

- #3：dk 话术全部出自证据库（`_tmp/scientific-meeting-evidence/`，6990 行逐字提取，含 ASR 还原表）
- #6：借假修真在复盘域/教练域已有引用（`agent-spec-zhu-ai-coach`、`bridge-个人复盘×知识管理W-Z-K-P`）——本批只建会议域 dk，互链不重复建
- #10：dk 卡六节标题一字不差（pre-submit 机械检查）；bridge 卡映射表 10 原则×5 阶梯逐行不缺
- 补链：只动 related 字段追加，不改已有卡正文；并发冲突检查——目标卡当前无其他实例在改（#280/281 为 hermes 实例教练域卡，与本批目标不重叠）

## 任务目标

科学开会卡片化 P0 深化批次——跨域桥接 + 暗知识增量 + 已有卡补链。**用户强调：案例卡和暗知识非常重要——dk×6 从 P1 升级 P0（2026-08-09）**。诊断：`60_feedback/diagnosis/diag_20260809_scientific-meeting.md`。

## 卡片规格

### bridge（1 张）

| 卡 id | 内容 |
|:--|:--|
| bridge-meeting-leadership-coaching | 科学开会 × 教练式领导力：会议 = 领导力核心场景——十大原则↔五阶梯映射（点燃↔L5 希望 / 民主↔L3 共识 / 学习↔L4 成长 / 良性↔L1 认同 / 责任↔L2 结果）；武器库提问/倾听 ↔ 会议主持；出口式咨询 ↔ 追问定量/还原事实 |

### dk（6 张，可合并生产但独立成卡）

| 卡 id | 内容 | 主锚 |
|:--|:--|:--|
| dk-meeting-roi-first | ROI 先行：先算账再开会（成本=人数×时间×时薪），砍一半会议活照干；会议三层价值决定开不开 | 认知篇 L900-1128 |
| dk-meeting-principle-over-process | 原则>流程：新手执行流程高手把控原则——A/B 抄最佳实践失败的根因 | 认知篇 L244-320/L700-734 |
| dk-meeting-rederive | 重新推导（民主集中进阶）：有答案也带团队推演——凝聚人心，80% 一致 20% 被推翻（Truman 压箱底） | 上篇 L1026-1130 |
| dk-meeting-borrow-false-repair-true | 借假修真：认真发一次彪建务实文化——慎用（挑韧性好的人/目标是建文化不是发泄） | 下篇 L916-970 |
| dk-meeting-asset-harvest | 会议资产：经验萃取两只手（SOP+思考模型）——花匠外部讲师合作案例/Truman 追问 | 上篇 L1538-1664 |
| dk-meeting-pressure-ignition | 压力激发：灵感在压力下产生（立 flag/锁门 50 个名字/3 小时 50 个备选） | 下篇 L2018-2052 |

### 补链（不新建，related 更新）

tool-yitang-project-kickoff-meeting / tool-yitang-daily-weekly-meeting-hosting / yt-tool-meeting-designer / 复盘域（framework-yitang-project-retrospective / tool-团队复盘引导清单 / tool-项目复盘基本功 / tool-复盘浪费九宗罪自检清单 / case-yitang-2022-annual-lessons）/ yt-decision-consensus-iceberg / tool-meeting-room-match——related 补链到科学开会新卡

## 生产纪律

- bridge 卡必写双域同构映射表（十大原则↔五阶梯逐层）+ 使用导航
- dk 卡含失败模式/反例/边界；"借假修真"标注慎用边界（挑韧性好的人）
- 定位声明必写；related 回链管理域/复盘域/领导力域/刻意练习域

## 验收标准

- 每卡 `kdo pre-submit` 通过 + lint 0 ERROR
- bridge 映射表完整（10 原则 ↔ 5 阶梯）
- dk 卡含 ≥2 个失败模式或反例；话术逐字引用
- 补链后无死链（抽查）

## 依赖

- #285 P0 卡组 reviewed（bridge/dk 依赖 framework 定位）

## 边界

- 不新建复盘/管理/领导力域卡（只桥接+补链）
- dk 可裁剪（6→4）：优先级 dk-roi-first / dk-rederive / dk-asset-harvest / dk-pressure-ignition 为核心，另 2 张可并入对应 tool

---

## 执行报告（老顽童 kimi 实例 · 2026-08-09）

### 交付物（7 卡 + 补链 25 条）

| 卡 | 路径 | 正文行数 | pre-submit | quality |
|:--|:--|:--:|:--|:--:|
| bridge-meeting-leadership-coaching | 30_wiki/bridges/ | 122 | ✅ PASS 0 err 0 warn | 90 |
| dk-meeting-roi-first | 30_wiki/dk/ | 163 | ✅ PASS | 80 |
| dk-meeting-principle-over-process | 30_wiki/dk/ | 104 | ✅ PASS | 80 |
| dk-meeting-rederive | 30_wiki/dk/ | 155 | ✅ PASS | 65 |
| dk-meeting-borrow-false-repair-true | 30_wiki/dk/ | 114 | ✅ PASS | 80 |
| dk-meeting-asset-harvest | 30_wiki/dk/ | 182 | ✅ PASS | 90 |
| dk-meeting-pressure-ignition | 30_wiki/dk/ | 114 | ✅ PASS | 85 |

**补链（related 追加，不动正文）**：tool-yitang-project-kickoff-meeting +4 / tool-yitang-daily-weekly-meeting-hosting +3 / yt-tool-meeting-designer +2 / framework-yitang-project-retrospective +4 / tool-团队复盘引导清单 +2 / tool-项目复盘基本功 +2 / tool-复盘浪费九宗罪自检清单 +1 / case-yitang-2022-annual-lessons +2 / yt-decision-consensus-iceberg +3 / tool-meeting-room-match +2 = 25 条，沿用各文件原有风格，无重复无遗漏。

### 验收对照

- **bridge 映射表完整**：10 原则×5 阶梯逐行不缺；激发↔L4 弱行已补中间环节（50-30-20 想法归属→人才成长信号）；五阶梯 L0-L4/L1-L5 两种编号已在卡内显式声明
- **dk 卡 ≥2 失败模式/反例**：7 卡实际均 ≥4 条；借假修真"挑韧性好的人"慎用边界在定位段/操作方法/适用边界/失败模式四处锚定+退出路径
- **话术逐字引用**：数据攻击 60+ 处抽查行号命中 100%，无编造无张冠李戴
- **补链无死链**：16 卡 sweep 全 PASS
- **dk 未裁剪**：6 张全产（用户强调暗知识重要，不启用 6→4 裁剪）

### 自攻击（四路，报告：`_tmp/scientific-meeting-evidence/self-attack-286.md`）

🔴×0 / 🟡×4（bridge 两处非逐字引号已改逐字；激发映射补强；dk-asset-harvest 补定期汇报机制 L1692-1712；dk-pressure-ignition 补 50-30-20 大小公司分层 L2210-2216）——全部修复，复跑 PASS。

## 终审记录（2026-08-09 欧阳锋）

**verdict: PASS A · blocking: 无 · methodology v2.2**

O0 溯源验证：
1. 覆盖率 7/7（bridge×1 + dk×6）存在
2. dk 卡失败模式 ≥2 达标（实测 2/3/4/5/7 处引用）；bridge 映射表完整（L0-L5 引用 38 处 + 十大原则 24 处）
3. 补链抽查命中：启动会卡 related 含 meeting-iceberg-canvas + scientific-meetings；复盘域卡含 meeting-basic-principles；共识冰山卡含 meeting-ten-principles——补链真实（25 条总量）
4. 自攻击报告 self-attack-286.md 存在（🔴×0/🟡×4 全修复声明）
5. pre-submit 16 卡（含 #285）批量 PASS
6. 边界遵守：dk 未裁剪 6 张全产（用户强调暗知识重要）；不新建重叠卡（启动会/例会/复盘/会议设计已有卡只补链）

五维：溯源 95/逻辑 90/暗知识 95/可操作 90/表达 90 → 总分 93（A）
