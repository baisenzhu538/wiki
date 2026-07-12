# F2 边分类标准：关系型 vs 引用型

> 草案·黄药师·2026-07-12 · 送欧阳锋审签（#159 阶段 0 gate）
> 通过后写入 `90_control/.lint_exceptions.json` 并制度化归档。

---

## 一、核心定义

wikilink 分为两类边，F2 对称性规则**仅适用于关系型边**。

### 关系型边（Relational）— 应双向

两个节点在知识网络中**对等互嵌**。A→B 意味着"A 和 B 是同一个论证结构里的两个构件"，缺失回链 = 网络有洞。

特征：
- A 和 B 处于同一抽象层（同为 concept / 同为 framework / 同为 tool）
- 或 A 是方法论节点，在正文中**明确声明** B 是其证据/案例/展开

### 引用型边（Citation）— 天然单向

A 将 B 作为**资源/背景/调用对象**引用，B 不需要知道自己被 A 引用了。回链无信息增量，且会污染 B 的 related 列表。

特征：
- A 是内容节点（case/dk/agent-spec），B 是方法论节点
- 或 A 是 hub 节点（合集/digest/index），B 是其成员
- B 的正文中**没有**对 A 的声明性引用

---

## 二、分类矩阵

### 2.1 关系型（F2 必检）

| from 类型 | to 类型 | 条件 | 示例 |
|:----------|:--------|:-----|:-----|
| concept | concept | 无条件 | `concept-一堂-参数耦合 → concept-一堂-魔法数字` |
| framework | framework | 无条件 | `framework-总纲 → framework-九层金字塔` |
| tool | tool | 无条件 | `tool-三环六维 → tool-建模七法` |
| case | case | 无条件 | `case-复盘营 → case-我请客` |
| dk | dk | 无条件 | — |
| concept | framework | 无条件（方法论互嵌） | `concept-基本功定义 → framework-总纲` |
| framework | concept | 无条件 | 反向同上 |
| concept/framework/tool | case | **仅当正文声明 case 为证据** | `concept-魔法数字 → case-复盘营`（当 concept 正文写了"复盘营案例证明了魔法数字"） |

### 2.2 引用型（F2 豁免）

| from 类型 | to 类型 | 豁免理由 |
|:----------|:--------|:---------|
| **case** | **concept** | 案例引用方法论——concept 不应挂 50 个 case 回链 |
| **case** | **framework** | 同上 |
| **case** | **tool** | 同上 |
| **dk** | **concept/framework/tool/case** | 暗知识引用主流卡——dk 是观察者视角 |
| **agent-spec** | **concept/framework/tool** | Agent 调用工具/手册——调用清单不应要求被调用者回链 |
| **合集卡** | **单案卡** | 合集 = digest 同构 hub，出向是目录，入向是引用 |
| ***** | **digest/index** | 导航索引入向不需回链（已有例外规则） |

---

## 三、灰区规则（最难判的边界）

### 3.1 concept/framework → case 的判定标准

这是欧阳锋指出的最易错边界。判定流程：

1. 读 concept/framework 卡正文
2. 搜索 case 卡名是否出现在正文中
3. 如果在正文中作为**证据声明**出现（"如 XX 案例所示""XX 案例验证了这一点"）→ **关系型，必须回链**
4. 如果只在 related 列表中出现、正文未提及 → **引用型，豁免**
5. 如果 concept/framework 卡尚未 enriched（正文未写）→ **暂判引用型，enriched 后重判**

### 3.2 合集卡的 hub 判定

合集卡（如 `case-yitang-false-causality-collection`）→ 单案卡：**引用型豁免**。
判定依据：合集卡的 `related` 是导航目录，功能 = digest 出向。单案卡指向合集视为"属于这个合集"，单案→合集也是引用型豁免（合集不需要知道自己收录了谁）。

---

## 四、豁免规则模板（`.lint_exceptions.json` 格式）

每条规则四字段：

```json
{
  "from": "case-*",
  "to": "concept-*",
  "reason": "引用型：案例引用方法论概念，concept不应维护所有引用案例的回链",
  "audit": "欧阳锋·2026-07-12"
}
```

铁律：
1. **按方向写，不按类型对写**——`case→concept` 豁免，`concept→case` 不豁免
2. **每条例外带 reason 字段**（语义依据，不是「量大」）
3. **audit 字段记录审签人+日期**——历史未来一致生效

---

## 五、反向边数量估计

基于 8411 条的分类分析：

| 类别 | 估计数量 | 处置 |
|:-----|:--------|:-----|
| 同类型真债 | 2769 | 修（先抽 50 确认 >90%） |
| 引用型正向边（case→concept/framework/tool） | ~800 | 进豁免 |
| dk→* | ~700 | 进豁免 |
| *→digest/index | ~900 | 进豁免（已完成） |
| agent-spec→* | ~50 | 进豁免 |
| concept/framework→case（可能含关系型） | ~200 | 需逐条判定（灰区 §3.1） |
| 其他跨类型（需逐类裁定） | ~3000 | 暂挂，不作为第一批 |

---

## 六、审签后行动

1. 欧阳锋审签通过 → 本文件归档 `90_control/edge-classification-standard.md`
2. 将引用型规则写入 `.lint_exceptions.json`（黄药师，阶段 1）
3. 抽 50 条同类型真债确认真债率（黄药师，阶段 2）
4. 放量 + 基线重建 + 三连复验（阶段 3）
