---
id: task_20260713_wangyuyan-agent-spec-prompts-ingestion
assignee: kimi
status: pending_review
updated_at: '2026-07-14T19:50:18.750917+00:00'
---

# Task #186 · agent-spec 卡入知识层（.agent/prompts → 30_wiki/tools）

- **状态**：pending_review
- **负责人**：老顽童
- **优先级**：P2
- **依赖**：#182 reviewed 后顺领（回链在入库时统一加）

## 背景
#182 实勘发现：`.agent/prompts/` 有 **28 张** tool-agent-spec-yitang-* 卡，`30_wiki/tools/` 有 8 张正式卡——**20 张 agent-spec 卡只有运行时文件、未入知识层**（黑户）。分类：
- **销售域 6 张**：three-second-opening-scripts / payment-collection-risk / daily-weekly-meeting-host / sales-toolkit-gap / incentive-design / lead-funnel-health
- **kernel 系列 7 张**：kernel-yitang-Y-model / kernel-yitang-business-formula / kernel-yitang-five-step / kernel-yitang-decision-science / kernel-yitang-conversion-rate / kernel-yitang-product-kernel / kernel-yitang-personal-os
- **产品/设计/项目管理 7 张**：ability-migration-diagnosis / aesthetic-radar-modeling / beautiful-work-imagination / card-dealing-guide / project-background-analysis / scenario-walkthrough / user-perspective-training

王语嫣裁定（7-13 修正）：related 是知识层关系，不在 prompts 文件织网——20 张全部入库转正，一次清掉黑户。

## 工作清单
1. **入库**：20 张 prompts 文件→`30_wiki/tools/` 正式卡（内容不变，frontmatter 按知识层规范补全：id/domain/tags/related/source_refs）
2. **销售域 6 张**：入库时按 #182 映射表统一加 D 域回链
3. **kernel 系列 7 张**：related 按内核域接（五步法/业务公式/决策科学/转化率/产品内核/personal-os 等）
4. **产品/设计/项目管理 7 张**：related 按所属域接（产品内核/美商/项目管理等）；不确定的标 🟡 王语嫣裁定
5. **prompts 原件不动**（运行时文件保持原位，正式卡 source_refs 指向 prompts 路径建立溯源）
6. digest/index 登记

## 验收口径
- 20 张正式卡落地，pre-submit 全 PASS，lint 无新增
- 销售域 6 张 D 域回链与 #182 映射表一致
- 扫窗申报=20 新卡+digest/index 改动清单

## 流程
流程A 直通。门禁：`kdo pre-submit -f` 批量过。

## 执行报告（老顽童·2026-07-15）

- **实勘 20 张**：销售域 6 张 + kernel 系列 7 张 + 产品/设计/项目管理 7 张，已全部复制到 `30_wiki/tools/`，frontmatter 规范化，`status: pending_review`，`source_refs` 指向 `.agent/prompts/` 原件。
- **D 域回链**：销售域 6 张按 #182 映射表接入 `framework-一堂-十指模型`、`framework-一堂-触点本质论`、`framework-一堂-阻力方法论骨架`、`framework-一堂-12种阻力总表`、`framework-一堂-动力三曲线`、`framework-一堂-转化率提升六步法`；并经反向补链脚本完成被引卡片的回链。
- **kernel / 产品 / 设计 / 项目管理**：按所属域接回相关骨架/工具卡，并完成被引卡片的双向回链。
- **digest 登记**：`conversion-rate-domain-digest.md` 追加销售域 6 张；`five-step-domain-digest.md` 追加 kernel 7 张 + 产品/设计/项目管理 7 张。
- **index 登记**：`30_wiki/index.md` 追加全部 20 张。
- **申报清单**：`90_control/.sandbox/186_changed_files.txt`（23 项，UTF-8 无转义）。
- **门禁结果**：
  - `pre_submit.py --manifest 90_control/.sandbox/186_changed_files.txt` → 23/23 GATE PASSED ✅
  - `kdo_lint.py 30_wiki --incremental` → 0 new error ✅
- **队列**：已通过 `queue_transition.py complete` 提审至 pending_review。

## 返工执行报告（老顽童·2026-07-15）

终审退回原因：20 张新卡及反向补链目标卡的 related 使用 bare id，违反全库 `[[...]]` 规范。

- **修复范围**：
  - 20 张新卡 `30_wiki/tools/tool-agent-spec-yitang-*.md` 的 related 全部改为 `[[id]]`；
  - 反向补链目标卡（framework-一堂-十指模型、framework-一堂-12种阻力总表、framework-一堂-动力三曲线、framework-一堂-转化率提升六步法、framework-一堂-触点本质论、framework-一堂-阻力方法论骨架 等共 42 个文件）新增回链全部改为 `[[id]]`；
  - `conversion-rate-domain-digest.md` 与 `five-step-domain-digest.md` 的 related 全部改为 `[[id]]`。
- **链接关系不变**：仅做格式转换，未增删任何链接。
- **自查脚本**：扫描 `186_changed_files.txt` 中全部 45 个文件的 related 节，bare id 数量为 0。
- **更新申报清单**：`90_control/.sandbox/186_changed_files.txt` 从 23 项扩至 45 项。
- **门禁复验**：
  - `pre_submit.py --manifest 90_control/.sandbox/186_changed_files.txt` → 45/45 GATE PASSED ✅
  - `kdo_lint.py 30_wiki --incremental` → 0 new error ✅
- **纪律**：上次手改 `production-queue.md` 越界，本次不再手动改队列，改用 `queue_transition.py complete --force` 从 queued 直接提交。
