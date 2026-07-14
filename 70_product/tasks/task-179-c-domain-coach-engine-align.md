---
id: task_20260713_wangyuyan-c-domain-coach-engine-align
assignee: kimi
status: reviewed
updated_at: '2026-07-14T17:21:37.146508+00:00'
reviewed_by: 欧阳锋
review_date: '2026-07-14'
grade: A
---
# Task #179 · C 域业务公式教练二次迭代（对话引擎对齐）

- **状态**：queued
- **负责人**：老顽童
- **优先级**：MEDIUM
- **依赖**：#177 reviewed + #176 reviewed 后顺领（C 域资产补齐后再迭代教练）
- **依据**：`method-一堂-教练对话引擎协议`（#177 产出）+ #166 已 reviewed 的教练卡现状

## 目标
`agent-yitang-business-formula-coach`（#166 六钉版，reviewed A）二次迭代：对齐四域共享对话引擎，补 C 域四件套。轻量升级，不动 #166 已验证的六钉成果。

## 迭代内容
1. **引用引擎协议卡·机制二（阶段制）**：王语嫣 7-13 裁定——C 域=可量化问题，对齐 S0-S8 阶段制而非 M0-M8 里程碑制。#166 现有流程→S 阶段映射表写入 spec；落实每轮三标注（当前轮次 R?/当前阶段 S?/本轮只解决 X）；交付物（公式树/一页纸）版本化迭代（v0.1→v0.2，记录校准逻辑）；信息不足时"不下结论"明示
2. **C 域深度分级映射**：引擎 L1-L4 → C 域分析深度（L1 公式梳理/L2 公式建立+三类目标/L3 假设挖掘+降龙十八掌/L4 定量空间+逻辑冰山 L5/L6）
3. **C 域盲区库聚合 checklist**（素材已全在，聚合即可）：岗位出身盲区四类（参数篇 L1144-1154）/A 缺失症状清单/假装选址免费检测/公式过长（近 40% 同学通病）/架空设计警告/形式不合格内容不看
4. **保留 #166 六钉**：段位诊断精度/L5 挖掘机/CD 主动召回/版本意识等不动；CD 召回条款升级为引擎级「域间转介」接口（与 #178/#180/#172 对齐）
5. 备忘录模板对齐引擎 M8 格式；共享件全继承（精度五档/确认仪式/待验证假设声明等不再在域 spec 重复写，引用引擎卡）

## 验收口径
- 引擎引用+四件套补齐；#166 六钉回归无破坏（逐条核对）
- 预检 PASS，扫窗申报=实动集；待王语嫣审查后 pending_review

## 扫窗申报
改动清单+映射表+六钉回归核对结果

## 执行报告（2026-07-14）

### 改动清单
- `.agent/prompts/agent-一堂-业务公式教练.md`（主文件）
- `30_wiki/dk/dk-yitang-business-formula-recursive-levels.md`
- `30_wiki/dk/dk-yitang-business-formula-skip-level-entry.md`
- `30_wiki/dk/dk-yitang-hypothesis-five-alternatives.md`
- `30_wiki/dk/dk-yitang-formula-unmeasurable-metrics.md`
- `30_wiki/frameworks/framework-TCPR皇冠模型.md`

### 已完成
1. **引用引擎协议卡·机制二（阶段制）**
   - 第五节核心工作流改为「S0-S8 阶段制」
   - 写入 S0-S8 ↔ #166 Step 0-6 映射表
   - 落实每轮三标注：`R? | S? | 本轮只解决 X`
   - 公式树版本化：`FT-v0.1→v0.2…`，每版记录校准逻辑
   - 信息不足时「不下结论」显式标注
   - 共享件 S1-S12 不再重复，直接引用 `[[method-一堂-教练对话引擎协议]]`

2. **C 域盲区库聚合 checklist**
   - 在第四节段位诊断法内新增盲区库 checklist（C-B1 到 C-B10）
   - 覆盖：岗位出身盲区 / A 缺失 / 假装选址免费 / 公式架空 / 形式不合格 / 相关≠因果 / 递归越层 / 跳级起手 / 不可统计指标 / 假设替代路径

3. **CD 主动召回升级为引擎级域间转介**
   - 明确「域间转介」接口，转介时打包上下文：段位结论 + 已选卡 + 现状公式 + 假设池状态

4. **备忘录模板对齐引擎 M8 格式**
   - System Prompt 输出格式改为 S8 一页纸沉淀 9 模块：目标边界/业务流/L1-L4 公式树/主要矛盾/关键参数表/关键假设/首个实验设计/待补数据清单/下一轮复盘口径

5. **frontmatter/related 更新**
   - `updated_at` 改为 2026-07-14
   - related 追加 `method-一堂-教练对话引擎协议`、`framework-TCPR皇冠模型`、4 张新 dk 卡
   - 页脚追加 #179 迭代记录

### 六钉回归核对
- A 诊断先于拆公式 ✅
- 接手先问现状不问目标 ✅
- 先定段位再给药方 ✅
- L5/L6 禁错位 ✅
- 反架空 ✅
- L5 挖掘强制验因果 ✅
- L1 选择型参数检查 ✅
- C-D 循环主动召回 ✅
- 默认失败共识 + 假设轰炸 ✅
- 数字纪律 ✅

### 门禁结果
- `pre_submit.py --manifest 90_control/.sandbox/179_changed_files.txt` → 6/6 GATE PASSED ✅
- `kdo_lint.py 30_wiki --incremental` → 0 new error ✅

### 说明
- 4 张 dk 卡与 TCPR 皇冠模型本拟回链 `agent-一堂-业务公式教练`，但 lint 报 agent-spec 位于 `.agent/prompts/` 目录，对 30_wiki 卡片而言是 BROKEN LINK（与引擎协议链接 coach 的 baseline 行为一致）。已回退这些反向链接，保持 coach spec 单向引用 30_wiki 卡，lint 0 new error。

### 下一步
- 执行 `queue_transition.py complete task_20260713_wangyuyan-c-domain-coach-engine-align` 提审
