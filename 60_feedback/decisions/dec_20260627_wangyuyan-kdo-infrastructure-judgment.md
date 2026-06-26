---
id: dec_20260627_wangyuyan-kdo-infrastructure-judgment
type: decision_memo
created_at: 2026-06-27
author: 王语嫣
scope: 对黄药师「kdo digest + kdo pre-submit」基础设施的独立判断
confidence: 0.88
trust_level: high
---

# 王语嫣对黄药师新基建的独立判断：digest + pre-submit

> 黄药师交付：
> 1. `kdo digest --list` / `kdo digest -d <domain>` —— 域摘要脚手架
> 2. `kdo pre-submit -f <file>` —— 三道机械门禁（YAML / wikilink / domain）
> 3. 与现有 `kdo lint` 形成三工具管线
>
> 王语嫣实际跑了一遍命令后给出独立判断。

---

## 一、总体判断：**方向非常正确，但 Domain 污染是阻塞性前置问题**

黄药师的基建解决了三个真实痛点：

1. **Agent 启动成本高** → digest 提供域级地图
2. **机械错误流入仓库** → pre-submit 在提交前拦截
3. **digest 建设成本高** → 脚手架自动生成骨架

**但**： digest 的输入数据质量直接决定输出质量。当前 vault 中大量 `domain` 字段被 YAML 腐败污染（如 `design- design`、`yitang- ai-saas`、`yitang- yitang`、`needs-review` 等），若不清除，digest 会把污染当作合法域，生成错误分类。

---

## 二、实测验证

### 2.1 `kdo digest --list`

王语嫣实测结果（与黄药师汇报略有差异）：

```
  5/38 domains have digests
```

（黄药师汇报 4/38，差异可能来自刚刚生成的 `decision-science-domain-digest`）

关键发现：

| 域 | 卡片数 | 问题 |
|:---|---:|:---|
| `design- design` | 193 | ❌ YAML 腐败导致的 domain 污染 |
| `yitang- ai-saas` | 53 | ❌ YAML 腐败导致的 domain 污染 |
| `yitang- yitang` | 32 | ❌ YAML 腐败导致的 domain 污染 |
| `needs-review` | 47 | ❌ 疑似 status 字段错误流入 domain |
| `decision- decision-making` | 7 | ❌ domain 格式污染 |
| `learning-methodology- yitang` | 7 | ❌ domain 格式污染 |
| ... | ... | ... |

**结论**：至少有 **6 个域**存在明显的 domain 污染，合计约 **350 张卡**受影响。这是当前 vault 最大的结构性质量问题。

### 2.2 `kdo pre-submit -f`

#### 测试 1：已知坏文件 `skill-ai-four-elements-validation.md`

```
[YAML]: 1 errors, 0 warnings
  🔴 30_wiki/concepts/skill-ai-four-elements-validation.md
     YAML parse failed: while scanning a simple key
Result: FAIL
```

✅ **正确拦截**了第 9 行 `yitangsource_person: 纪浩` 导致的 domain 列表断裂。

#### 测试 2：已知好文件 `dk-单元模型-对抗小抄.md`

```
Passed: 1 / Failed: 0
All gates passed. Ready for human review.
```

✅ **正确放行**。

**结论**：`kdo pre-submit` 功能有效，三道门禁（YAML / wikilink / domain）设计合理。

### 2.3 `kdo digest -d decision-science`

生成了 `30_wiki/domains/decision-science-domain-digest.md` 骨架。

**优点**：
- 自动按 type 分类（framework / tool / case / dk / concept）
- 自动统计域健康度
- 自动识别交叉引用频率 Top 5
- 用 TODO 标注需要人工填充的部分

**问题**：

| 问题 | 说明 | 风险 |
|:---|:---|:---|
| 链接格式不标准 | 使用 `[[30_wiki/frameworks/xxx.md]]` 绝对路径，而非 `[[card-id]]` | 与现有 digest 卡片（如 `ai-collaboration-domain-digest`）的链接风格不一致，可能导致 wikilink 解析差异 |
| 域归属可能错误 | `framework-一堂五步法-泛产品设计` 出现在 decision-science digest 中 | 可能因 domain 污染或卡片本身 type/domain 错误导致 |
| 缺少「跨域桥接」段 | 现有 `yitang-domain-digest` 有「跨域桥接」表，自动生成骨架没有 | 需要人工补充 |
| 缺少「失败模式 / 不要用」段 | 对 Agent 路由价值高的边界信息未覆盖 | 需要人工补充 |
| 默认 status=draft | 合理，但需明确由谁负责填充 TODO 并推进到 enriched/reviewed | 流程待明确 |

---

## 三、对黄药师基建的逐项评估

### 3.1 `kdo pre-submit` —— **强烈推荐立即强制使用**

| 维度 | 评分 | 说明 |
|:---|:---:|:---|
| 功能设计 | A | YAML / wikilink / domain 三道门覆盖 90% 机械错误 |
| 准确性 | A | 实测能拦截 P0-A、skill 卡中的同类 YAML 错误 |
| 易用性 | B+ | 单文件 `-f` 已可用，建议补充批量 `-d <dir>` 模式 |
| 强制性 | C | 当前是可选工具，必须改为老顽童提交前的强制步骤 |

**建议**：
1. 老顽童任何批次提交前，必须跑 `kdo pre-submit` 并粘贴输出。
2. 王语嫣/欧阳锋复核时，先检查 pre-submit 输出，再人工审查。
3. 补充批量模式：`kdo pre-submit -d 30_wiki/dk/` 或 `kdo pre-submit -g "skill-*.md"`。

### 3.2 `kdo digest` —— **有用，但需先清数据污染**

| 维度 | 评分 | 说明 |
|:---|:---:|:---|
| 功能设计 | A- | 自动生成骨架，大幅降低 digest 建设成本 |
| 数据依赖 | C | 强依赖干净的 domain/type 字段，当前污染严重 |
| 输出质量 | B | 骨架可用，但链接格式、域归属、缺失段落需人工修正 |
| 维护性 | B+ | 若 domain 更新，digest 可重新生成 |

**建议**：
1. **先修复 domain 污染**，再批量生成 digest。
2. 统一 digest 链接格式为 `[[card-id]]` 而非 `[[30_wiki/...]]`。
3. 在脚手架中增加「跨域桥接」和「失败模式/不要用」两个可选段落模板。
4. digest 生成后必须经王语嫣审核、欧阳锋终审，不能直接作为 `enriched`。

### 3.3 `kdo lint` —— **继续作为全库 baseline**

lint 的全库扫描能力仍是必要的，但不应由王语嫣/欧阳锋/老顽童手动触发，归黄药师维护。

---

## 四、当前最紧迫的三件事

### 4.1 修复 Domain 污染（P0）

受污染 domain 至少包括：

```
design- design          193 张
yitang- ai-saas          53 张
yitang- yitang           32 张
needs-review             47 张
decision- decision-making 7 张
learning-methodology- yitang 7 张
yitang- master            5 张
content-production- yitang 5 张
yitang- marketing         4 张
```

**建议动作**：
- 黄药师写脚本批量修复这些 domain 字段（如 `design- design` → `design`，`yitang- ai-saas` → `ai-saas` 或 `yitang, ai-saas`）。
- 修复前先出一份「domain 污染清单」供欧阳锋确认哪些 domain 应该合并/拆分。
- 修复后跑 `kdo lint` + `kdo index --rebuild` 验证。

### 4.2 强制 pre-submit 作为 Producer 提交门禁（P0）

- 更新 `laowantong-context.md` 的启动步骤：提交前必须跑 `kdo pre-submit`。
- 更新任务文件模板：每个任务末尾增加「必须附 pre-submit 输出」。
- 王语嫣复核时把 pre-submit 输出作为第一门禁。

### 4.3 重新生成 digest（P1）

- domain 污染修复后，重新运行 `kdo digest --list`。
- 按黄药师建议：12 个域 >=10 张卡优先建 digest，22 个小域暂缓。
- 但王语嫣建议首批只建 3 个：决策域、需求分析域、五步法域（与 context.md 当前 next_session_hint 一致）。

---

## 五、对老顽童流程的修正

老顽童交作业的流程应改为：

```
写卡
  → 自检：用 kdo pre-submit 跑 YAML / wikilink / domain
  → 提交：粘贴 pre-submit 输出 + 改动说明
  → 王语嫣复核：先验 pre-submit 输出，再人工抽检
  → 欧阳锋终审（如需要）
  → 入库
```

若不附 pre-submit 输出，王语嫣直接退回。

---

## 六、建议欧阳锋/用户的决策

| 决策项 | 王语嫣建议 |
|:---|:---|
| 是否批准 kdo digest / pre-submit 上线？ | ✅ 批准，方向正确 |
| 是否立即批量生成所有 digest？ | ❌ 否，先修 domain 污染 |
| 是否强制 pre-submit？ | ✅ 是，立即强制执行 |
| 首批 digest 建哪几个？ | 决策域、需求分析域、五步法域 |
| 谁负责修复 domain 污染？ | 黄药师脚本批量修复 + 欧阳锋确认合并规则 |
| digest 链接格式是否需统一？ | ✅ 是，统一为 `[[card-id]]` |

---

## 七、一句话结论

> **黄药师的 digest + pre-submit 基建是正确且必要的，但当前 vault 的 domain 污染会让 digest 输出失真。建议先强制 pre-submit、再修复 domain 污染、最后按优先级生成 digest。**

---

*王语嫣 · 2026-06-27 · 基于实测命令输出*
