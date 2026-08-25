---
id: 533
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-25T19:09:03.234006+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- 90_control/schemas/
- 90_control/kdo-seed/
reviewed_by: 欧阳锋
review_date: '2026-08-25'
grade: A
---

# #533 技术域适配包：软硬件库卡片 schema 扩展 + 域骨架模板 + 存量盘点脚本

- **任务号**：#533
- **状态**：queued
- **assignee**：huangyaoshi（schema+脚本；王语嫣提供域设计口径；欧阳锋终审）
- **优先级**：P1（与 #532 配套：种子包管机制搬迁，本单管技术内容怎么进机制）
- **立项**：2026-08-26 王语嫣（老朱补充：新库=软硬件全栈技术资料——后端平台/硬件/通讯协议/Android/Windows/电路图/固件，且已有几个 agent 在跑、质量不佳）

## 背景

本库是「文稿→卡」单一路径；技术库是「工件已存在（EDA 工程/代码仓/固件/协议文档），认知散落」。核心原则（王语嫣定）：**知识卡管认知，不管工件**——工件留原仓，卡只装设计意图/接口契约/版本变更/踩坑/故障案例，卡引用工件路径。

## 任务

1. **技术域卡 schema 扩展**（90_control/schemas/ 新增，不动现有卡型）：
   - `spec` 卡：协议/接口规格（版本、兼容性、变更历史、双方实现状态）
   - `module` 卡：软硬件模块（职责、接口契约、依赖、owner、固件/硬件版本关联）
   - `fault-case` 卡：故障排查案例（现象→定位→根因→修复→预防，技术团队最值钱暗知识）
   - 电路图/PCB/固件二进制不进卡，frontmatter 留 `artifact_path` 引用
2. **域骨架模板**：按系统分层建域——硬件/电路 → 固件 → 通讯协议 → 平台后端 → 端侧（Android/Windows）；层间接口关系=卡间最该建的链接（写进模板说明）
3. **存量盘点脚本**：扫描目标库已有产出，按形态/数量/缺项（frontmatter 有无、来源标注有无、疑似无源规格）出三堆清单：可审/返工/废弃——接管第一步用
4. schema 各配 1 张示例卡（用虚拟示例，不用真实技术资料）

## 边界

- 只做适配包，不去对方机器执行任何操作；不碰现有 concept/case/framework/tool/dk 卡型定义
- 「现有 agent 质量接管五步手册」由王语嫣主笔（随本单背景附口径），黄药师落 seed 时收编进 bootstrap

## 验收

- 三个 schema 过 schema 校验；盘点脚本在本库 60_feedback 上 dry-run 自证可用；示例卡各 1 张
- 欧阳锋终审

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：技术域适配包四件。①**三 schema**（`90_control/schemas/`，JSON Schema draft-07 既有约定，不动现有卡型）：`spec.yaml`（协议/接口规格：spec_version/compatibility/change_history/implementations/artifact_path 必填）/`module.yaml`（模块：responsibility/interface_contract 必填+dependencies/owner/hw_fw_versions/artifact_path）/`fault-case.yaml`（故障案例：symptom/root_cause/fix 必填+location/prevention/severity——五段链条缺段不是资产是流水账）；三卡型统一落「卡管认知不管工件」（artifact_path 引用原仓，二进制不进卡）。②**域骨架模板** `tech-domain-skeleton.md`：五层栈（硬件/电路→固件→通讯协议→平台后端→端侧）+层间接口关系建链规则（层内靠职责、层间靠契约、跨界靠 spec 卡）+接管建卡顺序建议。③**存量盘点脚本** `tech_inventory.py`：三堆分类（可审=frontmatter 齐+来源在位/返工=缺字段或无源或占位/废弃=无卡头空壳），--json 机读清单。④**示例卡 3 张**（schemas/examples/，全虚拟内容仅展示用法）——yaml 裸日期会被解析成 date 对象，示例卡日期一律加引号（实测踩到已修）。

**交付物**：
- `90_control/schemas/spec.yaml` / `module.yaml` / `fault-case.yaml` / `tech-domain-skeleton.md`
- `90_control/schemas/examples/`（spec/module/fault-case 示例卡 3 张）
- `kdo-tools/tech_inventory.py` + `kdo-tools/tests/test_tech_adaptation.py`（新：4 例回归）
- `90_control/infrastructure-inventory.md`（登记）

**验证**：
- L1 单测 4 例全过：三 schema 过 `Draft7Validator.check_schema`（schema 自身合法）+示例卡过 jsonschema 真校验（验收项「schema 过校验」的机械化）；盘点三堆分类（可审/缺源返工/无卡头空壳废弃各归各位）/缺字段理由可读；全量基线 **139 passed**（135+4，零退步）
- L2 狗粮（验收项 dry-run 自证）：`tech_inventory.py --root 60_feedback` 实跑——可审 126/返工 3798 件，数字与 60_feedback 历史流水形态吻合（大量早期记录缺 source_refs）✅
- L3 待活体：技术库接管实跑（对方机器上用盘点脚本出第一批三堆清单）

**边界**：只做适配包不去对方机器操作 ✅；现有 concept/case/framework 等卡型 enum 零改动（三新卡型独立 schema 文件）✅；王语嫣主笔的「现有 agent 质量接管五步手册」她尚未出稿——收编进 bootstrap 的动作等她交付（本单不代笔）✅；示例卡全虚拟无真实技术资料 ✅。

**需要谁动作**：欧阳锋终审本单；王语嫣——①接管五步手册出稿后我收编进 kdo-seed bootstrap；②域骨架模板（层间契约规则）请过目是否符合你的域设计口径；老朱知悉——技术库的内容进机制管道已就绪。

## 终审记录

- **终审**：欧阳锋 08-26 **PASS A**
- **版本对齐**：冻结版=02:57 commit b942bae7d=提审时刻 ✓
- **O0 溯源**：①三 schema 亲自过 `Draft7Validator.check_schema` 全合法 ✓（spec/module/fault-case 必填字段与任务书逐条对：版本/兼容性/变更历史/双方实现状态/artifact_path 等全在）；②三卡型独立新文件，既有卡型（concept/case/framework/tool/dk）零触碰 ✓（schemas/ 目录 diff 只新增）；③fault-case 五段链必填设计核验（symptom/root_cause/fix 必填+location/prevention——"缺段不是资产是流水账"落进 schema 约束）✓；④示例卡 3 张全虚拟 ✓
- **独立复跑**：139 passed（135+4）一致 ✓
- **L2 亲跑**：`tech_inventory.py --root 60_feedback` 实跑——三堆分类出数（可审 126/返工三千余件/废弃 2 件空壳理由可读），与声明形态吻合（我跑时窗多 1 件=3799，方向一致）✓
- **存在性核查**（负向断言附证）：「不去对方机器操作」——本单 diff 全部落在本仓 schemas/kdo-tools/inventory，无对外操作路径 ✓；「王语嫣五步手册未出稿不代笔」——kdo-seed/BOOTSTRAP.md 当前版不含该手册节 ✓ | 核查人：欧阳锋 08-26
- **预审报告判读**：宽负向词系描述文字误报，已判读不计缺陷
- **后续**：L3=技术库接管实跑第一批三堆清单；王语嫣五步手册出稿→黄药师收编 bootstrap

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 6 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（无/缺）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点
