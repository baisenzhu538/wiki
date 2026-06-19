# 第二十七节验收报告：清尾 31 张 ASCII 高价值 draft + 2 张跨域 dk 卡完成

**完成时间**：2026-06-19  
**执行人**：老顽童  
**审阅人**：欧阳锋  
**最终质量门禁**：`total=1210, p0=0, p1=0, clean=1210, yaml_error=0`

---

## 一、任务目标

剩余 ASCII 高价值 draft 共 31 张（21 张 master 系统暗知识、9 张 design 视觉/电商暗知识、1 张 parking-lot 索引）。本批次一次性清尾，并按"每 30 张格式精修产出 1-2 张跨域 dk 卡"的标准，额外产出 2 张跨域 dk 卡。

> 注：`session-20260619-xingangwan-business-formula-reconstruction` 位于 `60_feedback/usage-logs/`，不在 `30_wiki` 扫描范围内，故剔除。

---

## 二、精修清单（31 张，status 均为 enriched）

| 批次 | 主题 | 数量 | 卡片 ID |
|:---|:---|:---:|:---|
| 1 | Master P 类暗知识 | 7 | `dk-p1-model-switch-env`、`dk-p2-tmux-cache`、`dk-p3-auth-cache`、`dk-p5-cc-connect-config`、`dk-p6-session-resume-fail`、`dk-p7-ocr-skip`、`dk-p9-glob-miss` |
| 2 | Master P/F 类暗知识 | 8 | `dk-p8-toolkit-forget`、`dk-p10-oral-ban`、`dk-p13-token-burn`、`dk-p14-zombie`、`dk-p17-accuracy-gap`、`dk-p19-quote-yaml`、`dk-p20-bigram-fail`、`dk-f3-state-json-race-condition` |
| 3 | Master F/Design 暗知识 | 8 | `dk-f4-wrong-workdir`、`dk-f5-stale-feedback-ref`、`dk-f7-surface-translation`、`dk-f8-phony-wikilink`、`dk-f9-generic-critique`、`dk-f13-handwritten-yaml-parser`、`dk-yb11-visual-book-reverse`、`dk-yb16-ecommerce-product-image-vs-lucky-draw` |
| 4 | Design / 其他 | 8 | `dk-yb18-small-shop-image-mismatch`、`dk-yb19-visual-strategy-price-match`、`dk-yb22-visual-presentation-scene-match`、`dk-yb23-ai-pre-screen-three-minutes`、`dk-yb27-pseudo-layer-evasion`、`dk-yb30-ecommerce-channel-version`、`yt-tool-ai-ppt-maker`、`parking-lot` |

---

## 三、跨域 dk 卡产出（2 张）

| 卡片 ID | 主题 | 桥接的代表卡 |
|:---|:---|:---|
| `dk-state-residue-is-the-silent-killer` | 状态残留是自动化系统里最隐蔽的 bug | P-1/P-2/P-3/P-6/P-14/F-3（环境、缓存、session、token、僵尸进程、state 竞态） |
| `dk-tool-chain-naming-is-infrastructure` | 命名不规范会让整条工具链"失明" | F-10/F-8/P-11/P-19/F-13（source ID、wikilink、regex、YAML 引号、手写解析器） |

---

## 四、格式精修标准落地情况

| 检查项 | 标准 | 落地情况 |
|:---|:---|:---|
| status | enriched / diagnostic | 31 张目标卡全部 enriched |
| dk 正文结构 | 原始表述/核心洞察、使用场景、操作方法、适用边界、常见失败模式表、为什么值钱、与其他知识的关联（≥2） | 全部补齐 |
| tool/index 正文结构 | 用一句话讲清楚、核心要点、边界、失败模式表、行动 Checklist、相关卡互链（≥2） | 全部补齐 |
| diagnostic_signals | ≥2 条 | 全部满足 |
| source_refs | `10_raw/sources/` 下真实路径；无法精确追溯时允许通用 KDO 源或内部文档占位 | 全部有效 |
| reviewed_by | `欧阳锋`，不与 author 相同 | 全部合规 |
| 内部链接 | 使用 `[[id]]`，禁用非卡片链接/别名 | 已修正 |

---

## 五、过程中发现并修复的关键问题

### 1. 6 个精修代理因连接错误失败

- **影响卡**：`dk-yb19`、`dk-yb23`、`dk-yb27`、`dk-yb30`、`yt-tool-ai-ppt-maker`、`parking-lot`
- **处理**：通过 `Agent(resume=...)` 全部恢复，最终均成功 enriched。

### 2. `yt-tool-ai-ppt-maker` 包含 dangling 链接

- **问题**：related 和正文表格中引用了不存在的 `yt-model-personal-branding`。
- **修复**：从 related 和表格中移除该行。

### 3. `dk-f13-handwritten-yaml-parser` YAML 解析错误

- **问题**：diagnostic_signals 中 framework_lens 值包含未转义的反引号和冒号，被 YAML 误解析为 mapping。
- **修复**：将整个 diagnostic_signals 块所有字符串值用单引号包裹。

### 4. `dk-f8-phony-wikilink` 包含自引用占位链接

- **问题**：失败模式表中出现 `[[当前卡片名]]`，被 gate 识别为 dangling。
- **修复**：改为描述性文本"当前卡片名"，不再使用双括号。

### 5. `dk-p14-zombie` 使用 wikilink 别名

- **问题**：正文中出现 `[[dk-p13-token-burn|P-13]]` 等别名链接。
- **修复**：改为简单链接 `[[dk-p13-token-burn]]`。

---

## 六、质量门禁趋势

| 节点 | total | P0 | P1 | clean | yaml_error |
|:---|:---:|:---:|:---:|:---:|:---:|
| 批次 1 修复前 | 1208 | 0 | 1 | 1207 | 0 |
| 批次 1 修复后 | 1208 | 0 | 0 | 1208 | 0 |
| 批次 2 完成后 | 1208 | 0 | 0 | 1208 | 0 |
| 批次 3 修复前 | 1208 | 1 | 1 | 1206 | 1 |
| 批次 3 修复后 | 1208 | 0 | 0 | 1208 | 0 |
| 批次 4 修复前 | 1208 | 0 | 1 | 1207 | 0 |
| 批次 4 修复后 | 1208 | 0 | 0 | 1208 | 0 |
| **最终（含 2 张 dk）** | **1210** | **0** | **0** | **1210** | **0** |

---

## 七、ASCII 高价值 draft 池清理结果

第 25/26/27 节累计精修：**30 + 30 + 31 = 91 张** ASCII 高价值 draft。  
目前 `30_wiki` 内 status 为 draft/diagnostic、confidence≥0.7、related 非空、ASCII ID 的剩余卡片：

- **0 张**

ASCII 高价值 draft 池已基本清空。

---

## 八、域间自检三问

### 1. 案例够了吗？

本批次 31 张卡中 design 视觉/电商暗知识占 9 张，master 系统暗知识占 21 张，parking-lot 索引 1 张。**案例卡仍然偏少**。后续建议从 design 暗知识中挑选 3-5 张转化为"视觉/电商案例卡"，让暗知识与可复现场景对齐。

### 2. 暗知识在哪里？

本批次最突出的跨域模式已固化为 2 张 dk 卡：

- **状态残留是自动化系统里最隐蔽的 bug**：从 P-1/P-2/P-3/P-6/P-14/F-3 共同抽象。
- **命名不规范会让整条工具链"失明"**：从 F-10/F-8/P-11/P-19/F-13 共同抽象。

### 3. 这些卡有共同失效根因吗？

跨批次共同的根因：

- **人眼与机器对"正确"的判断不一致**：F-8、P-19、F-13 都说明"看起来对"不等于"机器能解析"。
- **状态/缓存/session 没有被纳入基础设施管理**：P-1/P-2/P-3/P-6/P-14/F-3 都是同一根因的不同表现。
- **命名/格式规范没有被 gate 强制执行**：F-10、P-11 说明规范若只是文档，就会断裂。

---

## 九、后续建议

1. **处理非 ASCII ID 高价值 draft**：ASCII 池已清空，但仍有中文/非 ASCII ID 的 draft 卡。建议下一轮用相同标准扫描并处理，或决定统一重命名为 ASCII ID。
2. **将内部文档 source 迁移到 `10_raw/sources/`**：大量 master 卡引用 `.agent/pitfalls.md`、`20_memory/corrections.md`、`90_control/failure-modes.md`。虽然当前不触发 P0/P1，但长期建议把关键陷阱/失败模式原文归档到 `10_raw/sources/`。
3. **给 source_id_map 增加命名校验**：在 `.kdo/source_id_map.json` 注册时强制校验 `src_YYYYMMDD_8hex` 格式，避免再次出现 `src_20260618_xingangwan` 这种不规则命名。
4. **补充 case 卡**：下一阶段优先产出 5-8 张与 design 视觉策略、AI PPT、系统状态残留直接配套的 case 卡。

---

## 十、验收结论

✅ **第二十七节 31 张 ASCII 高价值 draft 格式精修全部通过。**  
✅ **2 张跨域 dk 卡产出完成。**  
✅ **30_wiki 内 ASCII 高价值 draft 池基本清空。**  
✅ **全库 P0=0，P1=0，YAML 错误=0，clean=1210。**  
✅ **可进入下一阶段任务。**
