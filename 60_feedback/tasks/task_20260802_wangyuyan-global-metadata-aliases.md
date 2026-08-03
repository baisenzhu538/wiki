---
id: task_20260802_wangyuyan-global-metadata-aliases
task_id: 223
assignee: hermes
status: queued
created_at: 2026-08-02
domain: kdo
priority: P1
source: 王语嫣全局元数据扫描（2026-08-02）
updated_at: '2026-08-03T06:30:00+00:00'
last_review: "PASS放行 2026-08-03 欧阳锋——#222恢复审查通过，#223串行启动放行（hermes实例）"
---

# 🛑 紧急停手（2026-08-03 03:45）：#223 立即停止执行

> **⚠️ 王语嫣紧急指令——hermes老顽童立即停止所有写入操作！**
>
> **原因**：#223（aliases回填）与 #222（discoverable_by回填）**任务范围重叠**（都包含frameworks/），两个实例并行写入同一批文件导致 **C-10级批量破坏**——243/247张frameworks卡YAML解析失败（aliases块被追加插入diagnostic_signals后面）。
>
> **已确认hermes在持续执行**：git显示2626个文件未提交改动（tools 470/concepts 400/cases 344/frameworks 200...）——**继续写入=继续破坏**。
>
> **立即动作**：
> 1. **停止所有写入**（不保存当前批次，不继续扫描）
> 2. 记录已改文件清单（供#227修复参考）
> 3. 等待 #227（黄药师修复脚本）完成 + 本任务重新开放
>
> **恢复条件**：①#227修复完成（yaml.safe_load 100%通过）②#223与#222改为串行执行（不并行）③目录划分避免重叠（#223只做tools/concepts等，#222只做frameworks等）
>
> **🆕 aliases恢复规则（2026-08-03 04:20 王语嫣补充）**：修复脚本"替换"模式导致原aliases丢失。恢复时：
> 1. **7/27前旧卡**：`git show 16b64db39:<path>` 提取原aliases → 与当前合并（去重，不替换）
> 2. **8/2新建卡**：按discoverable_by/title反向补齐
> 3. 合并规则：原aliases + 新aliases 去重合并

## 📋 恢复方案（2026-08-03 05:10 王语嫣编排——串行+目录划分）

> **事故教训（E010+编排层）**："实例隔离"只防队列领取冲突，不防文件写入冲突。#222/#223并行写入同一批文件导致C-10级破坏。恢复后**必须串行**。

**执行顺序（串行，禁止并行）**：
1. **先 #222 完成并审查**（飞书老顽童）→ 再 #223（hermes）
2. **目录划分（零重叠）**：
   - #222 只管：frameworks/ + domains/ + personal-os/ + systems/ + agent-specs/ + skills/ + methods/ + bridges/（8个高价值目录）
   - #223 只管：tools/ + concepts/ + dark-knowledges/ + dk/ + cases/ + 其他（6个目录）
3. **每批写入前**：dry-run 预览 + `git diff` 验证 + yaml.safe_load 确认
4. **aliases 合并规则**（git 恢复原值 + 去重合并，不替换）
5. **本任务剩余范围调整**：原860张aliases回填 + **原aliases恢复**（git对比7/27恢复~2000张旧卡 + 8/2新建卡反向补齐）+ **131张重复键清理**（王语嫣实测：含双aliases/tags/related/diagnostic_signals——原125双aliases扩展，见#228背景）

## 🆕 17张顽固卡收尾项（2026-08-03 欧阳锋裁决纳入本任务）

> **来源**：#227修复的剩余17张（0.65%）——多层腐败（GBK乱码/author与reviewed_by值融合/双aliases/空related/src_unknown粘连），机械修复无法恢复乱码原值。欧阳锋裁决：**纳入#223恢复范围**（不阻塞#222/#223恢复）。

**清单**（O3扫描）：case-yihang-dual-triangle-* ×10 + framework-strategy-brm + framework-yitang-project-abcd-classification + framework-yitang-project-breakdown + system-yitang-Y-model-os + tool-Truman-Feature原子拆解 + plan_20260531_data-curator（统计差1张）

**处置**：
1. 乱码/值融合字段（author/reviewed_by/source_refs）→ 从源素材（VLM/口述）或 `git show 16b64db39:<path>` 恢复原值
2. 双aliases/空related → 机械合并（可修部分）
3. **验收门槛**：修复后 `yaml.safe_load` 通过 + 内容不劣化 + 原搜索词在位
4. 优先级：**#223收尾项**——不阻塞主恢复，但完成#223时必须清零

**⚠️ 注意**：这17张是#227修复的**剩余顽固卡**（黄药师手修部分转交），不是#222/#223破坏新增。执行时与主恢复分开处理。

# 全局aliases回填：860张卡补中文别名

# #223 全局aliases回填：860张卡补中文别名

## 任务背景

全局扫描发现 **aliases 缺失 860/2632 张（32.7%）**——中文搜索大面积盲区。小昭搜"创新者的窘境"搜不到的直接放大因素之一就是aliases缺书名。

**aliases 缺失分布**（按目录）：
- tools/ 364张、concepts/ 133张、dark-knowledges/ 94张、cases/ 48张、dk/ 42张、frameworks/ 43张
- 其余散落：methods 17 / systems 11 / domains 11 / skills 10 等

## 修复范围

**P1：aliases 回填（优先级按搜索价值）**

| 优先级 | 目录 | 数量 | 说明 |
|:--|:--|:--|:--|
| 1 | tools/ | 364 | 工具卡——"XX怎么做"搜索入口 |
| 2 | concepts/ | 133 | 概念卡——"XX是什么"搜索入口 |
| 3 | dark-knowledges/ + dk/ | 94+42 | 暗知识——"XX有什么坑"搜索入口 |
| 4 | frameworks/ + cases/ | 43+48 | 框架/案例 |

**每张卡 aliases 回填规则**：
1. 至少含1个中文别名（卡片常见中文名/简称/口语叫法）
2. 若卡片源自课程/书籍/人物 → 含来源名（如"创新者的窘境"、"Christensen"）
3. 若卡片ID含英文 → 含中文对应词
4. 参照已有卡 aliases 格式（如 `tool-讲香基本功-十指模型`：["十指模型","十指40策略","个人修炼"]）

## 验收标准

1. 860张缺aliases卡全部补上（至少1个中文别名）
2. 别名是真实搜索词（非占位符/非id复制）
3. 不修改正文内容，只动 frontmatter
4. 批量操作遵守铁律：dry-run预览 + 声明影响范围 + 非空不覆盖
5. 抽查20张用 `kdo query` 验证中文搜索可达

## 边界

- **只补 aliases 字段**——discoverable_by/title/tags 由 #219/#222/#224 覆盖
- 大量机械回填可分批（如按目录每批100张）
- 参考 #219/#222 的格式规范
- 存量卡不返工：只补缺失，不重写已有

## 📋 领取方式（王语嫣编排，2026-08-03 更新）

**🆕 执行人调整为 hermes 老顽童（独立消化存量债）**——用户指示：存量aliases/tags债单列给hermes老顽童，飞书老顽童继续#222主线（不阻塞）。

- **执行人**：hermes 老顽童（`claim 223 --instance hermes`）
- **并行关系**：与 #222（飞书老顽童）并行——两个实例互不阻塞（queue_gate实例隔离规则）
- 本任务860张是最大批量，**务必分批**（每批≤100张，dry-run+声明范围+非空不覆盖三铁律）
- 与 #224 的关系：#224（长程）仍由主实例处理，本任务完成后可并入#224节奏
- 若与其他实例并行：声明各自负责的目录范围，避免重复改同一张卡
