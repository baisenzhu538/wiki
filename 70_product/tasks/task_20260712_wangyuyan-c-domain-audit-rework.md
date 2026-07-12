---
assignee: kimi
status: queued
updated_at: '2026-07-12'
---
# 任务 #167：C 域质量审计返工（欧阳锋审计报告返工清单落地）

> 编排：王语嫣 | 生产：老顽童 | 终审：欧阳锋
> 优先级：P0（溯源铁律受损 + 增量门禁失盲，直接影响反向蒸馏素材可信度）
> 审计报告：`60_feedback/audit/c-domain-quality-audit-20260712.md`（欧阳锋，2026-07-12，本任务唯一权威输入）

## 背景

欧阳锋 C 域整体质量审计发现：双基线口径差异导致增量门禁对 C 域失盲（`.lint_baseline.json` 0 error vs `kdo lint --domain business-formula` 220 new error）——154 条 source_refs 死文件 + 67 条 case 卡 section 缺失 + ~39 条 tool 卡 section 缺失被旧基线吸收成「零新增」假象。审计返工清单（§六）已按 P0-P2 排好，本任务将其落地。

## 交付清单（按审计 §六返工清单，负责人以本任务单为准）

### P0（本任务必做）

1. **修复 154 条 source_refs 死文件**（老顽童）
   - 逐条确认：文件被移动/重命名/未生成？能补则补（改指向正确路径），不能补则改 `pending_unknown` 或 `pending_archive`
   - 重灾区 9 卡见审计 §2.2（six-level-logic 19 条 / digest 10 条 / marathon 10 条 / 总纲 9 条等）
   - 验收：`kdo lint --domain business-formula` source_refs dead 归零

2. **补齐 19 张 case 卡缺失 section**（老顽童）
   - 缺 `## 关键证据` 等结构化段落，按既有 case 卡骨架补齐；内容无据可补的标 `pending_unknown`，不许编造
   - 验收：lint Case card missing section 归零

3. **鑫港湾孤岛卡裁定执行**（王语嫣已裁定，老顽童执行）
   - **裁定**：`frameworks/xingangwan-pharma-business-formulas` **改 domain 移出 C 域**——理由：①EC 线独立域资产（鑫港湾专案），06-19 版拆解早于 C 域建域，未用 C 域体系；②与 C 域课程卡无实质语义关联，补桥接=造链（违反「造链比缺链更坏」原则）；③EC 线激活时归位
   - 执行：frontmatter domain 移除 business-formula（保留 yitang 或其他合适域，无合适则标 `pending_unknown` 待 EC 线归位）+ 过门禁
   - 验收：C 域口径下孤岛卡归零；该卡 lint 无新增 error

### P1（本任务必做）

4. **补齐 Tool 卡缺失 section**（Purpose/When NOT to Use/Critique/Protocol，老顽童）——lint warning 中 Tool card missing section 归零
5. **`tool-一堂-业务公式-L1L6参数分层自检` 入 index**（老顽童）——grep 命中 `30_wiki/index.md`

### P2（本任务必做）

6. **清理 `business-formula-to-kdo-card-quality` 的 4 条 kdo-\* 死链**（老顽童）——目标卡确认不存在则摘链，存在则修正链接

### 不在本任务（审计清单中的其他项）

- 总纲 `framework-一堂-业务公式拆解-总纲` 终审 → 欧阳锋自有节奏（审计 P0-3，非生产任务）
- 51 张 enriched 卡分批终审 → 欧阳锋（审计 P2，建议顺序：framework/concept → tool → case）

## ⚠️ 与 #159 的时序联动（审计 §5.3）

#159（lint 基线回卷）现 pending_review。**本任务 P0-1/P0-2 完成前，#159 阶段 3 不得重建基线**——否则 154 死文件 + 67 section 缺失会再次被新基线吸收，掩耳盗铃。本任务完成后由王语嫣通知黄药师/欧阳锋解锁基线重建。

## 验收点（欧阳锋用）

1. `kdo lint --domain business-formula`：source_refs dead 归零、Case/Tool missing section 归零
2. 修复方式合规：能补则补，无据标 pending_unknown/pending_archive，无编造无删链了事
3. 鑫港湾卡 domain 修改后 C 域孤岛归零、无新增 lint error
4. index 登记 grep 可验证
5. 扫窗申报=实动集（协议 2）

## 依赖

- 与 #166（agent 迭代）可并行；#166 引用本任务修复后的卡更准确
- #159 基线重建被本任务阻塞（见时序联动）
