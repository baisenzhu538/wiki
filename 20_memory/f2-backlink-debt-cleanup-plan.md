# F2 历史回链债务清理方案

> 创建：黄药师 · 2026-07-12 · 状态：parking（C域#157完工后启动）

---

## 一、现状

全量 lint（非增量）F2 MISSING BACKLINK：**8411 条**，涉及 1968 张 from 卡、1485 张 to 卡。

---

## 二、分类分析

| 类别 | 数量 | 占比 | 处理策略 |
|:-----|:----|:-----|:---------|
| **同类型间**（concept↔concept, tool↔tool, framework↔framework, case↔case, dk↔dk） | 2769 | 32.9% | 真债，`backlink_fixer` 分批修 |
| **→digest/index**（卡片引用导航页但 digest 不回链） | ~900 | 10.7% | 扩例外规则：`* → *-domain-digest` |
| **跨类型引用**（case→tool, tool→framework, dk→tool 等 70+ 组合） | ~4700 | 55.9% | 需王语嫣逐类裁定哪些该回链、哪些豁免 |
| **不可修复**（non-card目标，如旧 ocr-* 引用） | 47 | 0.6% | 断链非缺回链，不在此方案范围 |

---

## 三、执行阶段

### Phase 1：扩例外（0 成本，立刻）

新增一条例外规则到 `.lint_exceptions.json`：

```json
{"from": "*", "to": "*-domain-digest", "reason": "digest为导航索引，任何卡引用digest不需digest回链到该卡"}
```

预期消除：~900 条。剩余：~7500 条。

### Phase 2：同类型真债（C域完工后）

按类型分批，用 `backlink_fixer --apply` 修：

| 批次 | 类型对 | 数量 | 备注 |
|:-----|:------|:----|:-----|
| 2a | concept↔concept | 77 | 数量最少，先打样验证流程 |
| 2b | framework↔framework | 132 | |
| 2c | case↔case | 386 | |
| 2d | dk↔dk | 275 | |
| 2e | tool↔tool | 1878 | 数量最大，最后修 |
| **小计** | | **2748** | |

每批流程：dry-run 出 diff → 人工确认 → apply → 更新基线。

### Phase 3：跨类型裁定（需王语嫣）

70+ 种跨类型组合（case→tool 372, tool→framework 212, case→framework 179...），需要王语嫣逐类裁定：
- 该回链的 → 进 backlink_fixer 队列
- 豁免的 → 进 exceptions
- 不做决定的 → 保持 lint 红，不阻塞

### Phase 4：定期基线更新

每批修完后 `kdo_lint --baseline` → 新基线。历史债逐步消，增量零容忍（pre_submit + backlink_fixer 已就位）。

---

## 四、前置依赖

- [ ] Phase 1 例外扩：无依赖，随时可做
- [ ] Phase 2-3：#157 案例族完工后、老顽童产能空档时启动
- [ ] Phase 3 王语嫣裁定：需要她的独立判断时间窗口

---

## 五、不在此方案范围的

- 47 条 non-card 目标断链（ocr-* 旧卡引用等）→ 属于 BROKEN LINK 清理，另案处理
- 跨域桥接卡的回链标准（双三角↔Y模型↔基本功↔业务公式）→ 已是 P0 桥接卡，按既有标准
