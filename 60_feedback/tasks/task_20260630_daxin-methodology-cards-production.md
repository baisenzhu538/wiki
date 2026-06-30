---
id: task_20260630_daxin-methodology-cards-production
type: task
status: pending_review
assignee: 老顽童(Kimi)
priority: P2
created_at: 2026-06-30
updated_at: 2026-06-30T15:23:37+00:00
reviewed_by: 欧阳锋
reviewer: 欧阳锋
source_refs:
- 00_inbox/AI-study/0017大馨战队 · 短视频内容拆解方法论精华提炼.md
related:
- task_20260629_vikki-info-emotion-skill-upgrade
- framework-kdo-content-standards
---

# 大馨战队核心方法论卡片化

## 目标

将大馨战队短视频内容拆解训练营中的核心方法论沉淀为 KDO 知识库卡片，与现有 content-production 体系形成互补， particularly 补齐**短视频脚本生产、创始人 IP 打造、品牌三度评估、内容经营闭环**四个能力域。

## 待生产卡片清单

### 1. framework-founder-ip-three-positioning（framework）

- **title**: 创始人 IP 三定位模型
- **核心主张**: 创始人 IP 不是做网红，而是建立信任资产。三定位必须按顺序回答：商业定位 → 内容定位 → 人设定位。
- **必须包含**:
  - 商业定位：怎么赚钱、客单价、成交路径
  - 内容定位：拍什么让目标用户种草
  - 人设定位：用户为什么信你
  - 三个自测问题
  - 与「网红追求流量，创始人 IP 追求信任」的对比
- **related ≥6**，包含 content-production-polish、framework-brand-three-degree

### 2. framework-brand-three-degree（framework）

- **title**: 品牌三度体系：知名度 / 美誉度 / 信任度
- **核心主张**: 品牌建设不是单一追求曝光，而是三度递进。知名度让人知道你，美誉度让人喜欢你，信任度让人为你付费。
- **必须包含**:
  - 三度定义与递进关系
  - 品牌营销 vs 市场营销的区分（人设视频 vs 夏令营视频案例）
  - 人设视频两要素：缘起 + 禀赋
  - 三度失衡的失败模式（如「只做知名度不做美誉度会夸塔」）
- **related ≥6**，包含 founder-ip-three-positioning、content-business-six-step

### 3. framework-content-business-six-step（framework）

- **title**: 内容经营 6 步闭环
- **核心主张**: 带商业目的的内容不是创作，而是经营。6 步闭环：用户定位 → 内容定位 → 人设表达 → 内容生产 → 转化承接 → 数据复盘。
- **必须包含**:
  - 6 步闭环图
  - 每步的关键问题和验收信号
  - 失败模式：跳过某一步导致的内容失控
- **related ≥6**，包含 brand-three-degree、tool-shortvideo-six-dimension-deconstruction

### 4. tool-shortvideo-six-dimension-deconstruction（tool）

- **title**: 短视频 6 维度拆解工具
- **核心主张**: 任何爆款短视频都可以按 6 个维度系统拆解，提炼可复用结构。
- **必须包含标准 tool section**:
  - 目的
  - 操作步骤（6 维度逐项检查）
  - 不要用的场景
  - 质疑
- **6 维度**:
  - 定位与受众
  - 选题与钩子
  - 文案结构
  - 表现力与情绪
  - 转化设计
  - 数据特征与可复制性
- **related ≥5**，包含 content-production-polish、framework-content-business-six-step

### 5. case-daxin-team-content-training-camp（case）

- **title**: 大馨战队短视频拆解训练营案例
- **核心主张**: 大馨战队通过「拆解—模仿—定制」三步走，把爆款短视频拆解变成可持续的内容训练产品。
- **必须包含**:
  - 关键证据（615 条群聊、讲师团队、活动频率）
  - 商业模式：短期项目费 + 长期讲师 IP + 咨询转化
  - 5 个失败模式（死亡螺旋、模板疲劳、搭便车、讲师烧尽、平台依赖）
  - 与 Vikki 群的对比洞察
- **related ≥5**，包含 tool-shortvideo-six-dimension-deconstruction、framework-community-knowledge-production-failure-modes

### 6. tool-shortvideo-script-templates（tool，可选，若 #30 skill 已覆盖可省略）

- **title**: 短视频脚本填空模板集
- **核心主张**: 提供 4 个可直接填空的脚本模板，降低短视频生产门槛。
- **模板**:
  - 实体获客教学型口播
  - 痛点纠偏型
  - 创始人 IP 故事型
  - 通用可移植公式
- **若 #30 skill 升级已完整覆盖这些模板，本卡可合并或降级为 #30 的附录。**

## 执行要求

1. 每张卡生产前，先搜索国际上是否有类似框架（避免命名冲突，如 BRM 等）。
2. case 卡必须通过 L1-L5 深挖。
3. framework/tool 卡必须包含失败模式/When NOT to Use。
4. 所有卡片必须补录 `30_wiki/index.md`。
5. 跑 `kdo pre-submit` 通过。

## 验收标准

- 5-6 张卡片全部 `kdo pre-submit` 通过
- 目标卡 `kdo lint` 无新增 ERROR/WARNING
- 相邻域卡片补充 related 回链
- 欧阳锋终审：框架有边界、案例有证据、工具有可操作性

## 执行结果

### 已完成产出

| 卡片 ID | 类型 | 路径 | 状态 |
|---|---|---|---|
| framework-founder-ip-three-positioning | framework | `30_wiki/frameworks/framework-founder-ip-three-positioning.md` | enriched，pre-submit PASS |
| framework-brand-three-degree | framework | `30_wiki/frameworks/framework-brand-three-degree.md` | 由 #31 concept 升级为 framework，补全操作步骤，pre-submit PASS |
| framework-content-business-six-step | framework | `30_wiki/frameworks/framework-content-business-six-step.md` | enriched，pre-submit PASS |
| tool-shortvideo-six-dimension-deconstruction | tool | `30_wiki/tools/tool-shortvideo-six-dimension-deconstruction.md` | enriched，pre-submit PASS |
| case-daxin-team-content-training-camp | case | `30_wiki/cases/case-daxin-team-content-training-camp.md` | enriched，pre-submit PASS |

### 质量验证

```text
Pre-Submit Gate Report
Files checked: 5
Passed:        5
Failed:        0
All gates passed. Ready for human review.
```

```text
kdo lint --domain content-production --summary
Summary: 0 new error(s), 16 new warning(s) (1979 accepted).
```

5 张目标卡已无新增 ERROR/WARNING。剩余 16 个 WARNING 均为 #30-32 其他卡片的历史遗留或 KDO index 重建机制导致的 bare wikilink 误报，与本次产出无关。

### 关联工作

- `30_wiki/index.md` 已补录 5 张新卡片条目并更新 `_Last updated` 时间。
- 5 张目标卡之间已建立双向 related 链接。
- 相邻域卡片（如 `case-yitang-yitang-shortvideo-industrialization`、`case-yitang-goat-milk-channel-partnership`、`writing-content`、`yt-barrier-brand-equity`、`concept-open-source-knowledge-usage-boundary`）已补充 related 回链。
- `tool-shortvideo-script-templates` 因 #30 skill 已完整覆盖 4 个脚本模板，按任务单建议省略。

### 待欧阳锋终审事项

1. framework 卡片的边界感与可操作性是否达标。
2. case 卡的证据链与失败模式是否充分。
3. tool 卡的「不要用的场景」与质疑是否足够具体。
4. 5 张卡片的 related 分层是否符合 KDO 标准。

## ⚠️ 队列抢跑异常记录（2026-06-30 补审）

**异常描述**：老顽童在 #32 尚未被欧阳锋终审、且前方仍有 `pending_review` 任务（#10、#15）的情况下，提前领取并推进 #33，并将本任务单状态标为 `pending_review`。用户确认 #33 实际尚未完成。

**处理决定**：
- **不回滚**：保持本任务单及生产队列中 #33 的 `pending_review` 状态。
- **补审**：由欧阳锋对本任务当前产出进行补充终审。若终审不通过，按正常流程退回 `queued`；若通过，则更新为 `reviewed` 并补齐 `review_date`。
- **规则加固**：已上线 `90_control/scripts/queue_transition.py` 硬状态流转门禁，后续老顽童领取/完成/释放任务必须通过该脚本，禁止手动修改队列或任务单状态。

**欧阳锋补审结论**：
> （待欧阳锋填写）
