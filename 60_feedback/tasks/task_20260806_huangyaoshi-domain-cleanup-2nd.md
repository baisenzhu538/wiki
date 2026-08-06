---
id: task_20260806_huangyaoshi-domain-cleanup-2nd
task_id: 239
assignee: huangyaoshi
status: queued
updated_at: 2026-08-06
domain: system
priority: P1
---

# #239 域名清理补充（第二批：粘连/重复/大小写/测试值）

## 背景

#237 迁移后，王语嫣独立重扫发现仍有非标准域名（粘连/重复/大小写/测试值模式）。黄药师建议 #238 之前清理——采纳。

**已知候选（王语嫣扫描，待黄药师 yaml 级全量复核）**：
- 粘连：`learning-methodology- yitang`(9)、`yitang- ai-collaboration`(8)、`learning-methodology- management`(7)、`learning-methodology- design`(7)、`entrepreneurship- management`(5)、`entrepreneurship- product`(5)、`yitang- master`(5)、`ai-saas- yitang`(4)
- 空格粘连：`yitang - ai-saas`(6)
- 重复：`healthcare- healthcare`(7)
- 占位粘连：`yitang- src_unknown`(8)
- 大小写：`SaaS` 等
- 测试值：`[test]`(3)

## ⚠️ 执行前置（黄药师特别注意）

**王语嫣扫描脚本存在系统性误读**：约 250 个"值"（`aliases:` 99 / `status: needs-review` 37 / `source_refs:` 26 / `difficulty:*` 27 / `discoverable_by:` 11 / `source_person:` 等）是**正则跨字段误读**（domain 列表块解析时吃入了后续字段名），不是真实脏域。

**必须：用 `yaml.safe_load` 级解析（或等效可靠解析器）全库 frontmatter 生成权威清单**——以脚本输出为准，不要沿用任何"grep/正则扫描"的中间数据。产出权威清单后再分类处理。

## 分类处理方案（裁定）

| 类别 | 处理 | 示例 |
|:--|:--|:--|
| a. 粘连域（两个域被粘连成一个值） | **拆解**：按卡 title/正文判断主域归属，一卡一判（半自动：脚本列出候选+上下文，人工/LLM 判断） | `learning-methodology- yitang` → 看卡内容归 learning-methodology 或 yitang |
| b. 重复域 | 去重 | `healthcare- healthcare` → `healthcare` |
| c. 大小写 | 小写化 | `SaaS` → `saas` |
| d. 测试值 | 清理（无意义的删或按卡内容归域） | `[test]` |
| e. 占位粘连（含 src_unknown） | 拆开后 src_unknown 部分按 #237 裁定不纳入（单列跟踪） | `yitang- src_unknown` → `yitang` + src_unknown 占位跟踪 |

## 执行纪律（同 #237，硬约束）

1. `yaml.safe_load` 级解析出权威清单（第一步，先交清单再动文件）
2. dry-run 预览 → git diff 逐卡验证 → 全库 yaml 通过率 ≥99% 才 apply
3. 串行 + 目录划分；#228 重复键护栏
4. 粘连拆解涉及判断的卡：清单中标注"需判断"，不允许脚本静默选一个域（宁可不改，不可猜错）

## 🆕 复审 FAIL 补清（2026-08-06 欧阳锋 O3 + 王语嫣对照表检测）

**#239 初审 FAIL（条件）退回**：欧阳锋 O3 实测 61 张残留粘连；王语嫣已知域对照表检测 79 张/26 种（多出的 product-design 5、content-production-management 2、product-management 1、yitang-product 1 等——建议两个口径全量合并，宁多勿漏）。

**残留清单（对照表拆分检测结果，26 种 79 张）**：
yitang-ai-collaboration(8) / yitang-src-unknown(8) / learning-methodology-management(7) / yitang-ai-saas(6) / learning-methodology-design(6) / product-design(5) / entrepreneurship-product(5) / ai-saas-yitang(4) / entrepreneurship-management(4) / learning-methodology-yitang(3) / learning-methodology-ai-saas(3) / yitang-business-strategy(2) / modeling-yitang(2) / learning-methodology-kdo(2) / content-production-design(2) / content-production-management(2) / ai-collaboration-product(1) / product-management(1) / research-healthcare(1) / yitang-product(1) / ai-collaboration-ai-saas(1) / research-design(1) / entrepreneurship-design(1) / content-production-master(1) / content-production-entrepreneurship(1) / design-business-strategy(1)

**检测方法（固化纪律——E017 升级版：格式合法≠值合法）**：
- 粘连检测必须用**已知域对照表**做拆分匹配（值能否拆成 2+ 个已知域），不能只看 kebab-case 格式
- 已知域表 = 全库已确认的合法域清单（从 top 域名聚合 + 本次迁移后新增）
- 裁定标准：**连字符拼接多个域=一律错误格式**，拆成列表项（`- a\n- b`）；交叉语义用列表表达，不用拼接；拆分时看卡内容一卡一判（宁可不改，不可猜错）

**补清动作**：61-79 张全部拆解（yitang-src-unknown 拆后 src-unknown 部分按占位单列跟踪）；`src-unknown` 混入 domain 的卡同步处理；补清后欧阳锋复审。

## 验收标准

1. 权威清单（yaml 级）产出：全部非标准 domain 值列全，标注分类（粘连/重复/大小写/测试/误读排除）
2. 清理后重扫（**对照表拆分检测**，非仅格式检查）：粘连域归零
3. `kdo lint` 0 新增 ERROR；yaml 全库 ≥99%
4. 粘连拆解的卡：git diff 显示 domain 值修改与卡内容匹配（抽检）

## 依赖 / 边界

- #237 reviewed 后启动（串行，避免并发写）
- **#238（design MOC）前置**——完成本任务后 #238 才可启动（MOC 聚合需要 domain 干净）
- src_unknown（733 张占位域）仍不纳入，单列跟踪
