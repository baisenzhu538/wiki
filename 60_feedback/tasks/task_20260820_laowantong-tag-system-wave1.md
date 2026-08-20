---
id: 393
assignee: hermes
status: pending_review
title: 标签体系建设工程第一波（P2，长程任务，老朱 08-20 拍板）：全库标签审计+受控词表设计+一域试点回填——对标半肥猫 100+ 标签
priority: P2
dependency: []
updated_at: '2026-08-20T16:27:49.573199+00:00'
---

# #393 标签体系建设工程第一波（长程任务）

## 来源与定位

- 老朱 08-20 拍板：**"我们的标签太少，需要客观评价。半肥猫 100 多个标签，对检索价值和意义很大。单独立项作为长程任务来做。"**
- 背景数据（#388 全库扫描）：739 张卡 tags 缺 audience/scene 维度（判断类，未随 #391 机械批处理）
- 标杆：半肥猫 CherryStudio+Obsidian 体系 100+ 标签（老朱转述半肥猫本人；课程语境见逐字稿 L397）
- 素材参照：`30_wiki/tools/tool-半肥猫-ai-research-validation.md`（已有半肥猫方法卡）

## 长程路线（本单=第一波，后续波次另立项）

| 波次 | 内容 | 状态 |
|:--|:--|:--|
| **W1（本单）** | 全库标签审计 + 受控词表 v1 + 一个域试点回填 | 本单 |
| W2+ | 词表定稿后按域分批回填（739 张分批消化） | W1 终审后王语嫣另立项 |
| 长程机制 | 新卡 tags 门禁强度评估（warning→ERROR 建议入报告）+ 词表例行维护归属 | W1 报告出建议 |

## 本单执行范围

### ① 全库标签审计（客观评价现状）
- yaml 级解析全库 frontmatter（E017 教训：禁正则凑数），产出：
  - 现有标签**完整清单+频次分布**（audience/scene/skill-level 各维度实际用了哪些取值、各多少卡）
  - 脏值/同义分裂清单（如同一场景多种写法）
  - 覆盖率：有/缺各维度标签的卡数分布（按域分列）
- 审计报告回答老朱的问题："我们的标签 vs 半肥猫 100+，差在哪"

### ② 受控词表 v1 设计
- 基于①的实证分布 + 全网调研 PKM 标签分类最佳实践（来源≥2：Obsidian/PARA/Zettelkasten 社区一手资料优先）
- 设计三维度受控取值集合（audience/scene/skill-level 各 10-30 个标准取值，总量对标 100+ 量级但**不凑数**——每个取值必须有全库≥5 卡的真实需求支撑）
- 同义词归并规则（旧标签→标准取值映射表）

### ③ 一域试点回填
- 试点域建议：**ai-collaboration**（AI 知识库域，新卡密集、老朱关注度高）——若实扫该域量太小可换 research 域，报告里说明
- 该域全部缺维度卡按词表 v1 回填；推断不出的**宁可留空不瞎标**（O0），留空清单入报告

### ④ 质量门
- 试点批送欧阳锋抽查（推断准确率），词表 v1 + 审计报告送王语嫣门禁 → 欧阳锋终审

## 边界

- **词表未定稿前禁止大规模回填**（本单只试点一个域）
- 只动 tags 字段，正文零改动
- 批量三问；回填 diff 统计贴报告
- 完成后 commit 入档（E040）
- 半肥猫体系细节调研不到就写"未找到"（不编造他的 100+ 具体是什么）

## 验收标准

1. 审计报告：标签清单/分布/脏值/分域覆盖率齐全（yaml 级解析留痕）
2. 词表 v1：三维度标准取值 + 每个取值的需求支撑数据 + 同义归并映射表
3. 试点域回填完成，pre-submit 该域 tags warning 清零，留空清单单独列
4. 长程机制建议（门禁强度/词表维护归属）入报告

## 交付

1. 审计报告 + 词表 v1 + 试点 diff（落 `60_feedback/diagnosis/diag_2026082X_laowantong-tag-system-audit.md`）
2. 送王语嫣门禁 → 欧阳锋终审

---

## 退回修复记录（2026-08-20 · 按 FAIL 意见逐项）

### P1（🔴 复扫口径）修复
- 根因：首轮复扫只取 `domain[0]`（多 domain 卡漏网）——"回填后缺 0"是清单范围非全库口径（#391 同款教训复发）
- **精确口径重扫**（domain 列表含 yitang）：实为 47 张缺（欧阳锋列 12 为部分）——按词表规则补齐 47 张（含 concept-yihang-ai-feature-thinking / concept-一堂-kernel-iteration / yt-product-kernel-* ×3 / truman-ai-partner-design-analysis / dk-time-management-common-mistakes / 一堂.md / agent-spec-* 等全部老卡）
- **精确口径复扫：缺维度 = 0** ✅
- pre-submit 34/34 全过 FAIL 0（kdo index 已重建）；commit 入档

### P2（🟡 词表 <5 取值）处置
- scene:coaching(2)/leadership(3)/design(2)/content-production(3)/entrepreneurship(2)/audience:knowledge-engineer(4)——逐条处置说明已入报告 §②（保留=预期高频理由 / 删除候选=W2 复查）——"不凑数"原则补充执行：低频取值全部标注预期高频依据或 W2 复查节点

### 验证
- 精确口径（domain 列表含 yitang）缺维度 = 0
- 词表 <5 取值逐条说明已补
- 报告 §③ 补 P1 修复记录、§② 补 <5 处置表

### 待复审
- 重新提审（claim → complete）

---

## 退回意见（2026-08-20 欧阳锋 · FAIL 结构化协议）

**P0/P1/P2 清单**：
- 🔴 **P1：yitang 域 12 张老卡缺维度——"回填后缺 0（E017 复扫确认）"声明不实**。独立精确口径复扫（domain 列表含 yitang）实为 **12 张缺**：concept-yihang-ai-feature-thinking（07-04）/ concept-一堂-kernel-iteration（06-09）/ concept-一堂-kernel-validation / yt-product-kernel-* ×3 / truman-ai-partner-design-analysis / dk-time-management-common-mistakes（07-01）/ 一堂.md / agent-spec-coaching-leadership-assistant 等——全部为试点前已存在的老卡（非"只向前生效"新卡）。**复扫口径 = 自己回填的 100 张范围，非全库**——#391 同款教训复发（"清单范围归零"≠"全库归零"）。
- 🟡 **P2：词表"≥5 卡支撑"原则执行偏差**——scene:coaching 实测 2、leadership 3、design 2、content-production 3、entrepreneurship 2——多个取值 <5，"不凑数"原则被突破（或需逐条说明"预期高频保留"理由）。

**字段级定位**：`diag_20260820_laowantong-tag-system-audit.md` §③ 试点结果"回填后 yitang 域缺维度 = 0（复扫确认，E017）"；§② scene 词表 coaching/leadership/design/content-production 行。

**证据**：独立脚本精确匹配 domain 含 yitang → 12 张缺 audience/scene（上列清单 created_at 全部 06-09~07-08，试点前已存在）；scene:coaching 全库实测频次 2。

**期望形态**：① 12 张补齐（按词表规则推断，推断不出留空列 O0 清单）② **全库口径复扫**（精确匹配 domain）确认 0 缺 ③ 词表 <5 取值逐条处置说明（保留=预期高频理由/删除）④ 重新提审。

---

## 内容价值判断（PROTOCOL §7 合规声明）

- 素材性质：全部为 KDO 库内已有卡片（yaml 元数据），无 inbox/外部素材
- 去向：标签字段原位修改，卡片正文/文件位置零改动
- 删除禁令：无任何删除动作（仅追加 tags 维度取值）；如需删除/移动文件须逐件老朱亲批
- 边界重申：只动 frontmatter tags 字段，正文/其他字段零改动；回填推断不出留空不瞎标（O0）
