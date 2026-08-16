---
id: task_20260815_wangyuyan-agent-spec-domain-cleanup
assignee: hermes
status: pending_review
priority: P2
wsjf: 2.0
created_at: 2026-08-15
updated_at: '2026-08-15T19:37:50.002651+00:00'
source: 欧阳锋停车场 O-14（2026-08-15 拍板）
related: O-14
---

# agent-spec 类卡 domain 字段系统性清扫（O-14）

## 背景

2026-08-14 健康检查（60_feedback/auto/health-check-2026-08-14.md）实证：全部 agent-spec 卡 `non-list domain: None`（FAIL）+ `type=agent-spec in dir=tools/`（WARN）。非 #304 引入，全类历史债。欧阳锋 2026-08-15 审查确认后拍板：交王语嫣编排清扫。

## 清扫对象（9 张，tools/ 目录）

- agent-spec-meeting-assistant.md
- agent-spec-basic-skills-coach.md
- agent-spec-coaching-leadership-assistant.md
- agent-spec-codex-teammate.md
- agent-spec-dual-triangle-canvas-filler.md
- agent-spec-duanwangye-publisher.md
- agent-spec-hongqigong-multimodal.md
- agent-spec-project-management-assistant.md
- agent-spec-复盘教练.md

## 修复要求

1. **domain 字段补齐**：`non-list domain: None` → 列表形式，按各卡内容域（如 meeting-assistant → management/decision；coaching-leadership → human/management；各卡按实际内容定域）
2. **WARN 评估**：`type=agent-spec in dir=tools/` 是否应改目录（如 `30_wiki/agent-specs/`，参照 agent-spec-zhu-ai-coach 已在 agent-specs/ 目录）——**先给方案再动**（结构变更须建议先行，90_control/AGENTS.md）
3. 补齐后 `kdo lint` 该 9 张零 FAIL

## 验收标准

- 9 张卡 domain 全部为列表且非 None
- 08-14 健康检查同类 FAIL 归零
- 目录迁移若做：index.md/related 无死链 + 建议先行记录

## 边界

- 只改 frontmatter domain + 目录归属，不动正文
- 单角色单任务（E026）：王语嫣编排，生产交老顽童/黄药师
- 审查：欧阳锋终审

## 执行报告（老顽童 hermes 实例，2026-08-16）

### 第一部分：domain 补齐（已完成）
- 9 张卡实测：7 张已有列表 domain，2 张 None 已补：
  - agent-spec-meeting-assistant → [management, decision, yitang]（会议设计/该不该开=决策域）
  - agent-spec-coaching-leadership-assistant → [human, management, yitang]（一对一沟通/领导力）
- 9/9 domain 全列表非 None ✅（脚本验证 ALL_OK）

### 第二部分：目录迁移方案（建议先行，未执行，待裁定）

**现状**：
- `30_wiki/agent-specs/` 已是正式目录（index.md L37-39 含 3 张：duanwangye-publisher/hongqigong-multimodal/zhu-ai-coach）
- tools/ 下 9 张 agent-spec 卡 type 与目录不符（WARN），其中 duanwangye/hongqigong 与 agent-specs/ 重复（内容版本不同：tools 181/229 行 vs agent-specs 173/221 行，frontmatter 均已有 domain）

**方案 A（推荐）**：9 张统一迁入 `30_wiki/agent-specs/`
1. 重复 2 张：以 agent-specs/ 版为准（已入 index、domain 达标），删 tools/ 版
2. 其余 7 张：git mv 到 agent-specs/，frontmatter 不动正文
3. index.md 补 7 张条目（照现有 3 张格式）
4. wikilink 批量更新：9 张共 69 处引用（tools/agent-spec-xxx → agent-specs/agent-spec-xxx），用脚本全库替换后跑死链检查
5. 验证：kdo lint 9 张零 FAIL + 死链检查零 + index 覆盖

**方案 B（保守）**：保持 tools/ 现状，接受 WARN（type 与目录不符仅告警非 FAIL），只保留本次 domain 修复

**风险**：引用面大（codex-teammate 18 处/dual-triangle 15 处），批量替换需死链复验；工具链（cap_hub/agent 部署流程）若按路径引用需同步

**建议**：选方案 A（agent-specs/ 目录已存在且 agent-spec-zhu-ai-coach 已在其中，统一归置降低 type/dir 不一致），由欧阳锋终审时一并裁定；若裁定 A，本任务可续作迁移或另开任务执行。

### 验收对照
- [x] 9 张卡 domain 全部列表非 None（脚本实测）
- [ ] 08-14 健康检查同类 FAIL 归零（lint 验证中）
- [x] 目录迁移方案建议先行记录（本报告）

## 终审记录（2026-08-16 欧阳锋）

**verdict: PASS A- · methodology v2.3**

O3 独立验证：
1. **domain 补齐 9/9 达标** ✅：全部为列表非 None（meeting-assistant→[management,decision,yitang]、coaching-leadership-assistant→[human,management,yitang] 等），正文零改动（边界遵守）
2. **目录迁移方案裁定：❌ 方案 A 前提不成立**——重复文件 hash 实测不同（duanwangye/hongqigong tools/ 版 08-04 更新 > agent-specs/ 版 08-03），**tools/ 版是权威副本**，"以 agent-specs/ 版为准"会丢失 08-04 后的更新
3. **裁定：暂不迁移，记 TODO 另立项**——方案 C：保持 tools/ 现状接受 WARN（WARN 非 ERROR 不阻断），重复文件以 tools/ 版为准、agent-specs/ 版待后续去重；目录统一（agent-spec 归 agent-specs/）另开任务，迁移前先做双份 diff 合并
4. 偶发 state.sqlite disk I/O error 如实记录（drvfs WAL 已知问题，重试即过，与 #327 同家族）

**结论**：PASS A-（domain 补齐达标；目录迁移裁定为另立项，本任务不包含）
