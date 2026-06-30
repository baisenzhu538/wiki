---
id: task_20260629_vikki-info-emotion-skill-upgrade
type: task
status: reviewed
assignee: 老顽童(Kimi)
priority: P2
created_at: 2026-06-29
updated_at: 2026-06-30
reviewed_by: 欧阳锋
review_date: 2026-06-30
reviewer: 欧阳锋
source_refs:
- 00_inbox/AI-study/0071Vikki战队-2群 · 认知精华提炼.md
- 00_inbox/AI-study/0017大馨战队 · 短视频内容拆解方法论精华提炼.md
related:
- 40_outputs/capabilities/skills/shared/content-production-polish
- framework-kdo-content-standards
- tool-shortvideo-six-dimension-deconstruction
---

# Vikki + 大馨：content-production-polish skill 2.0 升级

## 目标

将 Vikki 战队的「讲人话」方法论与大馨战队的「短视频爆款拆解」方法论有机融合，把 `40_outputs/capabilities/skills/shared/content-production-polish/SKILL.md` 从通用文案润色工具升级为**覆盖口播稿、短视频脚本、公众号文章、小红书文案、销售文案、直播话术**的多平台内容生产 skill。

## 融合逻辑

| 来源 | 核心贡献 | 在 skill 中的位置 |
|:---|:---|:---|
| **Vikki 战队** | 信息×情绪二元模型、信息密度、口语化转折、抽象词落地 | Core Standard + human-speech-rules 方法 #13-#15 |
| **大馨战队** | 短视频 6 维度拆解框架、4 个脚本模板、钩子-结构-转化设计 | Platform Notes 扩展 + 新增「短视频脚本」专节 |

## 第一阶段：Vikki 内容融入

1. **信息 × 情绪 二元模型**
   - 信息是弹头，情绪是制导系统
   - 核弹（纯信息）+ 导弹（纯情绪）搭配效果最大

2. **信息密度控制**
   - 信息密度太高 → 认知负荷 → 紧张
   - 像酒精浓度，唠嗑聊天 > 书面语

3. **口语化转折词库**
   - 说白了 / 我举个例子 / 你看 / 问题来了 / 这就麻烦了

4. **抽象词落地法**
   - 每个抽象概念必须配「说白了就是 + 具体场景」

## 第二阶段：大馨内容融入

1. **短视频 6 维度拆解框架**（作为检查清单反向使用）
   - 定位与受众：一句话 IP 定位 + 受众痛点
   - 选题与钩子：工具型 + 痛点型，前 3 秒钩子
   - 文案结构：反常识开场 → 痛点共鸣 → 方法论 → 案例证明 → 转化
   - 表现力与情绪：亢奋型 + 行动派，屏幕录制 + 字幕高亮
   - 转化设计：公域 → 私信 → 资料 → 付费
   - 数据特征：互动设计、争议点、播放量估算

2. **4 个可复用脚本模板**
   - 实体获客教学型口播填空模板
   - 痛点纠偏型万能脚本公式
   - 创始人 IP 故事型公式
   - 通用可移植公式

3. **5 个人性开关**
   - 贪婪、恐惧、归属、好奇、行动

## 执行要求

1. 在 `SKILL.md` 中把 Core Standard 扩展为：
   - 听得懂 / 听得下去 / 信得过 / 用得上 / **记得住 / 愿意传**
2. 在 `human-speech-rules.md` 中新增方法 #13-#15：
   - #13 信息 × 情绪配比法（Vikki）
   - #14 短视频 6 维度检查法（大馨）
   - #15 人性开关植入法（大馨 + Vikki）
3. 在 Platform Notes 中为「短视频口播」「直播话术」「小红书文案」「公众号文章」「销售文案」分别补充大馨模板。
4. 提供至少 5 个跨域示例（AI/商业、亲子教育、销售、健康、知识付费）。
5. 更新 skill 后跑 `kdo pre-submit -f <skill文件>` 验证。

## 验收标准

- `SKILL.md` 和 `human-speech-rules.md` 通过 `kdo pre-submit`
- 新增内容不破坏原有 12 条方法编号，新增为 #13-#15
- 欧阳锋抽查：每个新增方法必须有具体场景 + 可执行 Pattern + 跨域示例
- 短视频脚本模板必须可直接填空使用

---

## 执行报告（2026-06-30）

**执行者**：老顽童(Kimi)
**状态**：pending_review，待欧阳锋终审

### 完成内容

1. **SKILL.md 升级**（`40_outputs/capabilities/skills/shared/content-production-polish/SKILL.md`）
   - Core Standard 从 4 条扩展为 6 条：听得懂 / 听得下去 / 信得过 / 用得上 / **记得住 / 愿意传**
   - Step 5.5 验证门同步扩展为 6 项检查
   - Mini Scoring Rubric 同步扩展为 6 维
   - Platform Notes 扩展为 5 个平台专节：短视频口播 / 直播话术 / 小红书文案 / 公众号文章 / 销售文案
   - 短视频口播节补充大馨 6 维度检查清单 + 4 个可复用脚本模板
   - 销售文案节补充 5 个人性开关

2. **human-speech-rules.md 升级**（`40_outputs/capabilities/skills/shared/content-production-polish/human-speech-rules.md`）
   - 新增方法 #13：信息 × 情绪配比法（Vikki）
   - 新增方法 #14：短视频 6 维度检查法（大馨）
   - 新增方法 #15：人性开关植入法（大馨 + Vikki）
   - 每个方法均按 5-part 结构编写（Problem → Fix → Pattern → Hard vs Human → Why it works）
   - 每个方法均提供 5 个跨域示例（AI/商业、亲子教育、销售、健康、知识付费）
   - 文件开头说明从「12 条方法」更新为「15 条方法」

3. **桥接同步**
   - 将更新后的 `SKILL.md` 和 `human-speech-rules.md` 同步复制到 `.claude/skills/content-production-polish/`
   - 确保 Hermes/Claude Code 两端技能一致

### 质量验证

```text
$ kdo pre-submit -f 40_outputs/capabilities/skills/shared/content-production-polish/SKILL.md
All gates passed. Ready for human review.

$ kdo pre-submit -f 40_outputs/capabilities/skills/shared/content-production-polish/human-speech-rules.md
All gates passed. Ready for human review.
```

### 欧阳锋审查要点

- Core Standard 新增 #5「记得住」、#6「愿意传」的阈值是否可执行
- Platform Notes 中 4 个短视频脚本模板是否可直接填空
- 方法 #13-#15 的跨域示例是否覆盖足够、无 AI 味
- `.claude/skills/content-production-polish/` 桥接版本是否与 shared 版本一致
