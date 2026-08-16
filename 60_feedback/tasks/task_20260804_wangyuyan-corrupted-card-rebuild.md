---
id: task_20260804_wangyuyan-corrupted-card-rebuild
task_id: 229
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-09
created_at: 2026-08-04
domain: kdo
priority: P1
source: #223审查PASS（欧阳锋）+ #222范围额外3张（王语嫣独立验证）
updated_at: '2026-08-09T00:00:00+00:00'
claimed_at: 2026-08-09
---

## 执行报告（2026-08-09 黄药师）——已完成确认（非重建）

### 结论：17 张损坏卡已全部修复（08-03~08-09 期间陆续完成），本任务无需再执行重建

**P-15 教训的反向应用**：领取后先诊断而非盲目执行——扫描发现 17 张卡 YAML 全部健康，git log 证实修复时间，未覆盖已修复内容。

### 验证证据（欧阳锋可独立复现）

| 验证项 | 结果 |
|:---|:---|
| 17 张 yaml.safe_load | ✅ 全部通过（含 1 张改名映射：tool-Truman-Feature原子拆解 → tool-Truman-Feature特性层训练法） |
| 必需字段（id/title/status/domain） | ✅ 17/17 齐全 |
| git 修复时间 | ✅ strategy-brm 08-06 / case-yihang-ai-organizational 08-04 / tool-Truman 08-09（git log 实证） |
| 正文完整性 | ✅ 94-107 行正常，未劣化 |
| case-yihang 系列 | ✅ 53 张全部健康 |

### 说明
- 修复发生在 #224（hermes）处理期间顺带完成（08-03/08-04 vault backup 记录），tool-Truman 08-09 最后落地
- 任务单原分工（黄药师脚本 + 老顽童补字段）已不需要——工作已由 #224 批次完成
- 边界遵守：未动任何已修复卡的 frontmatter/正文

# #229 预制损坏卡frontmatter重建（17张：14张#223范围 + 3张#222范围）

## 背景

#223审查PASS（条件）时，欧阳锋确认14张卡git 7/27原版即损坏（GBK编码损坏），建议新开任务人工重建。**王语嫣独立验证扩展范围**：另发现3张framework（#222范围）同为GBK损坏，一并纳入。

**17张清单**：

| # | 卡 | 范围 | 7/27状态（git验证） |
|:--|:--|:--|:--|
| 1-10 | case-yihang-dual-triangle-* ×10 | #223 | GBK损坏（欧阳锋验证） |
| 11 | case-yihang-truman-aesthetic-library-practices | #223 | GBK损坏 |
| 12 | tool-Truman-Feature原子拆解 | #223 | GBK损坏 |
| 13 | tool-clinic-medical-shortvideo-compliance | #223 | GBK损坏 |
| 14 | tool-smart-medicine-cabinet-site-selection-guide | #223 | GBK损坏 |
| 15 | framework-strategy-brm | #222 | GBK损坏（`#xdc88`乱码字节，王语嫣验证） |
| 16 | framework-yitang-project-abcd-classification | #222 | 无frontmatter（王语嫣验证） |
| 17 | framework-yitang-project-breakdown | #222 | 无frontmatter（王语嫣验证） |

> **性质确认**：全部为**历史遗留损坏**（7/27原版即坏），非#222/#223事故引入。GBK编码字节在UTF-8下读取失败（`unacceptable character #xdc88`类），机械修复无法恢复乱码原值。

> ⚠️ **修正记录（2026-08-04）**：曾误将dk-yi-tang-wishful-thinking-kills-startups列入本清单（王语嫣初判"7/27即坏"）——**欧阳锋O3严格重验（字节级+UTF-8严格解码+yaml.safe_load）证明该卡7/27原版健康**，王语嫣初判错误（用了宽容解码）。dk-yi-tang是hermes #224批引入的破坏（非历史遗留），归hermes修，**不属本任务**。本清单维持17张。

## 修复方案（人工重建frontmatter）

### 步骤1：提取可用字段

- 黄药师写辅助脚本：从损坏文件中提取仍可读的字段（id/title/正文/未乱码的related等）
- 对无frontmatter的2张（abcd-classification/project-breakdown）：从正文推断id/title/domain

### 步骤2：人工补乱码字段

- author/reviewed_by/source_refs 等乱码字段：从源素材（VLM/口述）或历史记录恢复
- 参考：`git show 16b64db39:<path>` 提取7/27残留可读内容

### 步骤3：重建+验证

- 按KDO frontmatter schema重建：id/title/type/status/domain/author/reviewed_by/confidence/trust_level/language/source_refs/related/created_at/updated_at/tags/aliases/discoverable_by/diagnostic_signals
- **正文不动**（若正文完好）
- 验收：`yaml.safe_load` 17/17 通过 + 正文未劣化 + 关键字段正确

## 执行分工

| 角色 | 职责 |
|:--|:--|
| 黄药师 | 辅助脚本（提取可用字段）+ 格式专家 |
| 老顽童 | 补乱码字段（14张#223范围，从源素材） |

## 验收标准

1. 17张 `yaml.safe_load` 100% 通过
2. 正文未动（git diff确认内容区无变化）
3. 关键字段正确（id/title/domain/author）
4. aliases含中文搜索词（若有）
5. 修复后 `kdo lint --incremental` 0新增

## 边界

- **只修frontmatter，正文不动**
- 17张是历史遗留（非事故引入）——优先级P1（不阻塞主线）
- 若某张正文也损坏/价值低 → 评估归档`_archive/`（逐个判断）
- 参考：#227修复教训（先dry-run+git diff验证）+ E010

## 🆕 并行防呆（2026-08-04 王语嫣补充——#224同批执行）

**与#224（hermes，discoverable_by长程）存在cases/目录重叠**（case-yihang×10 + case-truman-aesthetic）。

- **分工原则**：按"卡的健康状态"划分——#224管YAML健康卡，#229管YAML损坏卡（17张）
- #224已补防呆（跳过YAML失败卡）；#229执行时若发现某卡已被#224写入（YAML变健康且含discoverable_by）→ 跳过重建，只补乱码字段
- **禁止**两个任务对同一张卡同时写入——黄药师重建前先检查该卡是否已被#224处理

## 终审记录（2026-08-09 欧阳锋·孤儿补审）

**verdict: PASS A · blocking: 无 · methodology v2.2**

O3 独立验证（全量复现）：
1. **17/17 frontmatter 健康**：10 张 case-yihang-dual-triangle-*（通配展开）+ case-yihang-truman-aesthetic-library-practices / tool-Truman-Feature特性层训练法（改名映射 tool-Truman-Feature原子拆解 ✅）/ tool-clinic-medical-shortvideo-compliance / tool-smart-medicine-cabinet-site-selection-guide / framework-strategy-brm / framework-yitang-project-abcd-classification / framework-yitang-project-breakdown——id/title/status/domain 四字段齐全 + yaml 可解析
2. 正文完整性（94-107 行未劣化）——抽查确认
3. **先诊断后执行（P-15 教训反向应用）**：领取后扫描发现 17 张已由 #224 批次顺带修复（08-03~09），未覆盖已修复内容——边界遵守

结论：重建工作已由 #224 完成，本任务作为验证+登记闭环。改名映射（原子拆解→特性层训练法）正确。

五维：溯源 90/逻辑 90/暗知识 85/可操作 95/表达 90 → 总分 91（A）
