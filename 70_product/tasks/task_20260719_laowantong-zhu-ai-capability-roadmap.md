---
id: task_20260719_laowantong-zhu-ai-capability-roadmap
type: task
status: reviewed
assignee: hermes
priority: P1
estimated_cards: 2
created_at: 2026-07-19
updated_at: '2026-07-19T13:57:58.698458+00:00'
source_refs:
- 30_wiki/personal-os/zhu-future-directions.md
- 30_wiki/personal-os/user-insight-profile.md
- 30_wiki/personal-os/zhu-feedback-patterns.md
- 30_wiki/personal-os/zhu-project-board.md
related:
- '[[zhu-future-directions]]'
- '[[user-insight-profile]]'
- '[[zhu-feedback-patterns]]'
- '[[task_20260719_wangyuyan-profit-pricing-domain]]'
reviewed_by: 欧阳锋
review_date: '2026-07-19'
grade: A-
---

# 老朱 AI 能力建设刻意练习路线图

## 任务目标

基于已确认的个人域策略——**鑫港湾打工解决生存 + 借假修真看清方向 + 全力学习 AI 能力**，为老朱产出一张可执行的 AI 能力刻意练习路线图（tool 卡）和一张个人 AI 教练智能体规格（agent-spec 卡）。

本任务不讨论未来 10 年方向选择，只解决“这一年怎么把 AI 能力真正练出来”的执行问题。

## 背景信息（已写入个人域）

- 当前策略：`zhu-future-directions.md` §当前策略框架
- 时间窗口：2 年以上，但第一年必须出成果
- 性格约束：`zhu-feedback-patterns.md` —— 跳跃性思维、完美主义、取舍困难、个人偏好主导
- 业务场景：`zhu-project-board.md` —— 鑫港湾黑石系统、OPC 控制系统、润心堂品牌重启
- 学习目标：从“工具使用者”进阶到“能独立搭建智能体/工作流并嵌入业务闭环”

## 产出物

### 1. tool-zhu-ai-deliberate-practice-roadmap

一张 tool 卡，内容必须包含：

- **能力模型分层**：
  - L1 工具使用（提示词、多模型协作、RAG/搜索）
  - L2 工作流搭建（低代码/脚本化自动化）
  - L3 智能体设计（agent-spec、system prompt、工具调用）
  - L4 业务嵌入（把 AI 落到鑫港湾/OPC/润心堂的真实场景）
- **24 周路线图**：
  - 第 1-4 周：当前段位诊断 + 工具熟练度基线
  - 第 5-12 周：围绕 1 个真实业务场景搭工作流
  - 第 13-24 周：产出并验证 1 个可用智能体/agent-spec
- **每周最小动作**：具体到“本周练什么工具、完成什么输出、找谁要反馈”
- **与老朱性格约束的防偏机制**：
  - 跳跃性思维 → 每周只允许切换 1 次主题
  - 完美主义 → MVP 验收标准，先跑通再优化
  - 取舍困难 → 每个阶段只保留 1 个主场景
  - 个人偏好主导 → 每个练习必须有业务价值验证
- **里程碑与验收**：
  - 3 个月：能独立搭建 1 个业务工作流
  - 6 个月：产出 1 个通过自测的智能体
  - 12 个月：在真实业务场景中跑通人机协作闭环

### 2. agent-spec-zhu-ai-coach

一张 agent-spec 卡，规格：

- **角色**：老朱的 AI 学习教练 + 决策陪跑者
- **核心功能**：
  - 根据路线图推送本周最小动作
  - 对练习结果给结构化反馈（用 Truman 学习曲线/刻意练习框架）
  - 在老朱提出新方向时，调用 `zhu-future-directions.md` 做优先级提醒
  - 每次对话结束自动记录一条反馈信号到 `zhu-feedback-patterns.md`
- **输入**：老朱的练习输出、问题、新想法
- **输出**：下一步动作 + 反馈等级（🟢/🟡/🔴）+ 是否需要升级到人/专家
- **边界**：不替老朱做商业决策，只负责学习推进和决策框架提醒

## 验收标准

1. 两张卡均通过 `kdo pre-submit`
2. `kdo lint` 0 新增 ERROR/WARNING
3. 路线图必须绑定至少 2 个真实业务场景（从鑫港湾/OPC/润心堂中选）
4. 必须引用个人域文件作为 source_refs
5. 必须包含可量化的 3/6/12 个月里程碑
6. 必须针对老朱的 4 个性格约束设计防偏机制

## 参考文件

- `30_wiki/personal-os/zhu-future-directions.md`
- `30_wiki/personal-os/user-insight-profile.md` §2.1 认知风格
- `30_wiki/personal-os/zhu-feedback-patterns.md`
- `30_wiki/personal-os/zhu-project-board.md`
- `40_outputs/capabilities/skills/shared/nine-layer-deep-dig/SKILL.md`（按需引用）
- `40_outputs/capabilities/skills/shared/deliberate-practice/SKILL.md`（如存在，按需引用）

## 下一步

老顽童领取后，先 Read 个人域相关文件，再开始设计；完成后提交欧阳锋终审。
