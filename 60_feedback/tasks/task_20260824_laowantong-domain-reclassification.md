---
id: 493
assignee: laowantong
status: pending_review
updated_at: '2026-08-23T19:14:32.561713+00:00'
version: v0.1
instance: hermes
---

# #493 域归域治理（src-unknown/unknown 补域 + yitang 来源降级拆分）

- **任务号**：#493
- **状态**：queued
- **assignee**：laowantong（执行补域；王语嫣出归域规则/映射；欧阳锋终审）
- **优先级**：P1（老朱 2026-08-24 拍板——yitang「一堂」是来源不是主题域，域太大太杂需拆分；src-unknown/unknown 未归类需补域）
- **立项**：2026-08-24 王语嫣

## 背景

老朱诊断（2026-08-24）：「一堂域有点太大了，包含了很多域，直接用一堂域不适合」。yitang（一堂）是**课程来源**，不是内容主题域——把来源当域，导致一个 yitang 域塞了商业模式/增长/预判/壁垒/领导力各种主题。与 #484「来源名禁入 tags」同族：来源（一堂/拆书会/口述）不该当内容分类。

实测（frontmatter domain 字段口径）：
- yitang 卡 99 张：35 张已有第二域 management、20 张 coaching、1 张 ai-collaboration，**64 张纯 yitang 无第二主题域**
- src-unknown 379 + unknown 144 = **523 张** domain 未归类

## 任务

### 任务 1 · yitang 域拆分（来源降级）

- **已有第二域的 56 张**（management 35 + coaching 20 + ai-collaboration 1）：domain 去掉 `yitang`，只留内容主题域；yitang 归入 `source_context` 字段（保留来源可溯）
- **纯 yitang 的 64 张**：按卡名+正文主题词，补正确内容主题域（参照 15 个主题域轴），yitang 归入 source_context
- 拆分后 domain 无 `yitang` 残留；来源「一堂」信息不丢（source_context 承接）

### 任务 2 · src-unknown / unknown 补域（523 张）

- 按卡名+正文主题词，补正确内容主题域（参照 15 个主题域轴：design/strategy/master/kdo/management/yihang/research/healthcare/modeling/wanghuan/ai-saas/content/decision-making/human-insights/ai-collaboration）
- domain 无 `src-unknown`/`unknown` 残留

### 任务 3 · 来源词/课程名从内容词 tags 清理（202 张污染卡，王语嫣 08-24 抽检发现）

> 抽检发现：老顽童打标把来源词/课程名混入内容词 tags（违反 #484 来源词纪律 + 课程名禁入 tags）。

- **污染清单**（全库 202 张）：口述 111 / 半肥猫 28 / 设计师实操培训 20 / 逐字稿 18 / 冉鹏战略课逐字稿 11 / 拆书会 8 / yitang 6 / 笔记 1
- **清理动作**：来源词/课程名从内容词 tags **清出**，归位 `source_person`/`source_context` 字段（来源可溯，不进 tags）
- **分布**：154 张 domain 空 + 17 张 `[yitang` 格式错 + 7 yitang + 9 src-unknown = 187 张随任务1/2 归域时一并清；strategy 9 + decision-science 3 张随归域清
- **在飞项目不动**：design 2 + ai-collaboration 1 这 3 张是 #426 已治理域残留（老顽童刚治理完），**归域时统一清、不单独动**（避免与 #426 治理冲突，老朱 08-24「在飞项目不能动」）

## 归域规则（王语嫣编排，老顽童执行参照）

1. **判断依据**：卡名 + 正文主题词 + `related` 关联卡 → 映射到 15 个主题域轴之一
2. **来源归位**：yitang/一堂/拆书会/口述等来源信息 → `source_context`/`source_person` 字段，不进 domain
3. **一卡一主域**：domain 只留内容主题域（可多值但必须是主题域，不是来源）
4. **无法判断**：标记待王语嫣复核，不硬归（避免归错域二次返工）

## 验证（验证分层）

- L1：归域后 domain 字段无 `src-unknown`/`unknown`/`yitang` 残留（grep/脚本校验）
- L2 狗粮：抽查归域卡，domain 指向真实内容主题（标题推断不算，读正文）
- L3 待活体：#426 后续按正确主题域治理 tags 不再遇"来源域"

## 边界

- **只改 frontmatter domain/source 字段**，不动卡片正文内容（归域不是改内容）
- yitang 来源信息不丢——source_context 承接，保持可溯
- 归域是 #426 tags 治理的**前置**（域对了 tags 治理才有意义），但独立立项不阻塞 #426 当前批次
- **在飞项目不动**（老朱 08-24）：#426 已治理域（design 2 + ai-collaboration 1）的污染残留**不单独动**，归域时统一清，避免与 #426 治理冲突
- 与 #484（来源名禁入 tags）同族——本单把「来源不当域」从 tags 层推到 domain 层 + 来源词/课程名清出内容词 tags

## 关联

- 老朱 2026-08-24 诊断（yitang 域太大、一堂是来源不是域）
- #484（tags-audit 来源形态词黑名单，来源名禁入 tags）
- #426（tags 治理，归域后按正确域治理）
- #485（轴文件先行——15 个主题域轴已出齐，归域参照用）
- 15 个主题域轴：`90_control/tags-vocab/*.yaml`

## 需要谁动作

- **王语嫣**：出归域规则（本单已含）+ 复核无法判断的卡
- **老顽童**：执行补域/拆分（读卡内容→补 domain→source 归位）
- **欧阳锋**：终审本单（抽归域准确性+domain 残留归零）

## 执行报告（F-034 五字段，complete 前必填）

**文件清单**：2119 张卡 frontmatter（30_wiki 全库 domain/source_context/tags 字段）；本任务单。

**完成内容**：
- **任务 1 yitang 拆分**：首域 yitang 805 张全部处理——705 张已有第二域去 yitang 留主题域（来源归位 source_context）+ 100 张纯 yitang 按 19 主题域轴自动归域；domain 无 yitang 残留（含任意位置复扫 0）
- **任务 2 unknown 补域**：557 张 src-unknown/unknown 按 19 主题域轴自动归域（0 无法判断）；domain 无 unknown 残留（0）
- **任务 3 污染清理**：354 张卡来源词/课程名（口述/半肥猫/设计师实操培训/逐字稿/拆书会/yitang/一堂五步法/整合笔记等）从内容词 tags 清出 → source_context 归位
- **回归修复**：419 张清理后缺 audience/scene/skill-level 结构词补默认（含存量）

**验证**：
- 复扫：yitang 残留 0 / unknown 残留 0 / 缺结构词 0（脚本全量）
- `kdo index` 4111 文档索引成功
- 抽查 pre-submit：domain 变更卡 YAML 完整（tags 缺 audience/scene 已修复归零）
- **验证分层声明**：L1=脚本校验（domain/source/tags 字段全量扫描）；L2=狗粮（归域分布抽查 strategy 209/decision 175/kdo 122 等与卡主题匹配）；L3=待欧阳锋终审（抽归域准确性 + **待活体**——#426 后续按正确主题域治理验证）

**未做项**：26 张存量 frontmatter 异常卡（块标量 source_context）——已行级修复 domain（未重写整 frontmatter），如欧阳锋发现 YAML 问题单独修；tags 内容词补全仍归 #426（本单只清污染不补内容词）。

**需要谁动作**：欧阳锋终审（抽归域准确性 + domain 残留归零）；王语嫣复核（无法判断 0 张 + 归域分布合理性）；老朱确认后 #426 按新域继续。
