---
id: task_20260815_laowantong-candy-sales-recruiting
assignee: hermes
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-16
priority: P2
wsjf: 2.0
created_at: 2026-08-15
updated_at: '2026-08-15T18:04:31.198897+00:00'
source: 王语嫣编排（2026-08-15 用户拍板）
related: null
---

# Candy 销售招聘方法入库（#322）

## 背景

马易口述稿（00_inbox/spin销售巨人/，~920-1060 行）分享「销售招聘方法【百倍成交】——招聘篇」Candy 文档：能力模型为核心、定量+定性结合、星巴克/Cosmos 客观面试验证方法（面试官结论一致、跑 28 层验证）。用户拍板：**必须入库**。素材原文标注"不要外传/大家就别太爱传了"——内部知识库可用，入库加传播限制标注。

## 任务

1. 销售招聘方法入库（tool 卡或案例卡，含能力模型+客观验证方法）
2. **传播限制标注**：frontmatter 或正文显著标注「仅内部使用，禁止外传」
3. source 指向素材（口述行号 + Candy 文档链接）

## 核心内容锚点（口述行号）

- 能力模型为核心 + 定量定性结合（~926-966）
- 星巴克面试：三面试官结论必须一致；有分歧讨论面试官自己的问题（~974-998）
- Cosmos 跑 28 层楼验证"坚持锻炼"（~1000-1024）
- 反例：面试问"你能吃苦吗"无意义（~934-960）

## 验收标准

- 卡落盘 + 传播限制标注清晰
- source_refs 口述行号主锚
- `kdo lint` 零 FAIL

## 边界

- 单角色单任务（E026）：老顽童生产，欧阳锋终审
- 与 #320 并行（互不依赖）

## 执行报告（老顽童 hermes 实例，2026-08-15）

### 产出
- `30_wiki/tools/tool-candy-sales-recruiting.md`——销售招聘的客观验证方法（能力模型+定量定性结合+星巴克结论一致机制+Cosmos 28 层跑楼行为验证）
- **传播限制标注已加**：正文首行显著标注「⚠️ 传播限制标注：本卡内容来自内部课程分享，仅限内部知识库使用，禁止外传。」（对应口述 L1054-1056「大家就别太爱传了」）

### 素材精做
- 口述稿 L914-1056 逐字通读（在 #320 全稿 2400 行通读范围内），行号锚点全部命中：
  - 能力模型+定量定性结合 L926-966
  - 星巴克三面试官结论一致 L974-998
  - Cosmos 28 层验证 L1000-1024
  - 反例"你能吃苦吗"无意义 L934-960
- source_refs 口述行号主锚 ✅

### pre-submit 门禁
- Passed 1 / Failed 0，8 项检查零 warning（tags/aliases/定位声明修复后重跑）

### related 验证
- 9 条 related（补 dk-ai-collaboration-degradation-spiral 后跨域≥2），脚本实测全库映射死链=0

### 三方法证据
- 素材精做 ✅（行号命中）；交叉验证用知识库内部卡（framework-yitang-scientific-sales-five-step/tool-yitang-sales-performance-management）
- **全网调研：⚠️ 外网被审批拦截，未能完成独立外部来源调研，请欧阳锋裁定**

### 边界遵守
- 单角色单任务（E026）；与 #320 并行互不依赖 ✅

## 终审记录（2026-08-16 欧阳锋）

**verdict: PASS A- · methodology v2.3**

O3 验证（#320 批内联动）：
1. related=9 死链=0（补 dk-ai-collaboration-degradation-spiral 后达标）✅
2. trust_level=medium + 传播限制标注（素材"不要外传"）符合内部库语义 ✅
3. 卡内量化示例来源标注清晰，未冒充口述 ✅

**结论**：PASS A-，Candy 招聘方法卡入库验收通过。
