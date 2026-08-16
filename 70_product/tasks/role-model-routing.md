---
title: 模型路由成本杠杆方案（建议稿，不改配置）
type: improvement-plan
status: draft
created_at: 2026-08-09
author: 黄药师
source_refs:
  - "https://benchlm.ai/deepseek/api-pricing"
  - "https://www.morphllm.com/deepseek-api"
  - "https://learn.microsoft.com/zh-cn/training/modules/aaai-optimize-multi-agent-performance-cost-azure/2-design-model-route-agent-ecosystems"
  - "https://futureagi.com/blog/what-is-llm-routing-2026/"
---

# 模型路由成本杠杆方案（#277 调研落地 · 建议稿）

> 结论先行：**KDO 当前全员固定单模型，存在 3.1× 的成本杠杆未用**。按任务分级路由，预计月成本降 40-60% 且质量不降（Pro 审查 + Flash 执行混合工作流实测降 60-70%）。
> 本方案只出建议，**不改任何配置**——落地需王语嫣/欧阳锋批准后执行。

## 一、现状盘点（2026-08-09 实测）

| Profile | 当前模型 | 角色 | 主要任务 |
|:--|:--|:--|:--|
| basic-skills-coach | deepseek-v4-flash | 教练 | 问答/点菜/试点 |
| laowantong | deepseek-v4-flash | 老顽童 | **卡片量产/深挖/诊断** |
| wangyuyan | kimi-for-coding | 王语嫣 | 编排/诊断/跨域设计 |
| hongqigong | kimi-for-coding | 洪七公 | 多模态/VLM |
| duanwangye | kimi-for-coding | 段王爷 | 发布/反馈 |
| 欧阳锋（CLI） | kimi | 终审 | 审查/裁决 |

**问题**：老顽童（生产主力）用 Flash 做深度生产（卡片深挖、九层深挖、跨域桥接）——Flash 是 284B/13B active 的量级模型，**单文件编码近 Pro 但深度推理/多步逻辑明显弱**。欧阳锋/王语嫣用 Kimi 订阅（费用固定）。生产用便宜模型 + 审查用昂贵模型，是**倒挂**——应该反过来：深挖生产用强模型，机械/批量用便宜模型。

## 二、模型定价（2026-08 官方，美元/百万 token）

| 模型 | Input（cache miss） | Output | 参数 | 定位 |
|:--|:--:|:--:|:--|:--|
| deepseek-v4-flash | $0.14 | $0.28 | 284B (13B active) | 量级：分类/抽取/摘要/批量 |
| deepseek-v4-pro | $0.435 | $0.87 | 1.6T (49B active) | 旗舰：深度推理/架构/复杂调试 |
| **Pro ÷ Flash** | **3.1×** | **3.1×** | — | — |

> ⚠️ 2026-08-06 DeepSeek 公告：计划整体上调 API 定价（幅度未定）+ 高峰时段（北京 9-12/14-18）2× 计费（生效日期 TBA）。**方案落地前需复核价格。**

## 三、任务分级表（KDO 实际任务 × 模型匹配）

按 Microsoft 三复杂度分级（Tier 1 便宜 / Tier 2 中档 / Tier 3 前沿）适配 KDO：

| 级别 | 任务类型 | KDO 实例 | 建议模型 | 说明 |
|:--|:--|:--|:--|:--|
| **T1 批量/机械** | 批量修复、lint、OCR 文本化、清单生成、状态流转、格式整理 | #271 四类规则、#237 域名迁移、friction-log 整理、pre-submit 检查 | **flash** | 高吞吐低推理，Flash 质量近 Pro |
| **T2 生产/执行** | 卡片深挖、九层深挖、跨域桥接、诊断报告、案例萃取 | #233-#247 生产、王语嫣诊断、双三角深挖 | **pro**（老顽童/王语嫣核心生产） | 多步推理+知识合成，Flash 不够 |
| **T3 审查/裁决** | 终审、架构决策、争议裁决、跨域框架设计 | 欧阳锋终审、D3 战略决策、桥接设计 | **pro/旗舰** | 不可降档——质量地板 |

**KDO 具体路由建议**：
1. **老顽童**：flash → pro（生产主力升级）——卡片深度直接决定知识库质量，是 ROI 最高的升档
2. **黄药师基建任务**：批量机械（lint/迁移/清扫）→ flash；架构/新工具设计 → pro（按任务手动选）
3. **教练**：保持 flash（问答/点菜是 T1）
4. **欧阳锋/王语嫣/洪七公/段王爷**：维持 Kimi（订阅制，成本固定，不折腾）

## 四、成本测算（估算）

假设 KDO 月消耗 ~1.5 亿 token（input 主导，缓存命中率 ~50%），当前全 Flash：

| 场景 | 月成本（估算） |
|:--|:--:|
| 现状全 Flash | ~$600 |
| 老顽童升 Pro + 其他保持 | ~$1,200 |
| **路由混合（Pro 生产/审查 + Flash 批量，质量地板保护）** | **~$750** |
| 对比：全 Pro | ~$1,900 |

**结论**：全 Flash 省了钱但生产深度不够（倒挂）；全 Pro 贵 3 倍。**混合路由 = 质量提升 + 只多花 25%**——如果生产深度提升带来返工率下降（#269 首交率），净成本可能持平甚至更低。

## 五、落地路径（建议，需批准后执行）

### Phase 1（低风险，1 天）：老顽童切 Pro 试点
- 老顽童 profile `model.default: deepseek-v4-flash → deepseek-v4-pro`
- 试点 1 周：观察卡片深度/返工率（#269 首交率 + 欧阳锋审查反馈）
- 成本变化对照（Hermes 日志 token 统计）

### Phase 2（1 天）：批量任务显式降档纪律
- 基建批量任务（lint 修复/迁移/清扫）执行时显式用 flash（手动指定或临时 profile）
- 规则写入黄药师 context：**"批量机械任务默认 flash，架构/设计任务默认 pro"**

### Phase 3（可选，后续）：路由层
- 若 KDO 规模继续增长 → 评估 LiteLLM/nexus-llm-router 类网关做自动路由
- **当前不做**：KDO 角色固定 + 任务类型相对稳定，手动分级已够用；网关是过度工程（YAGNI）

## 六、风险与护栏

| 风险 | 护栏 |
|:--|:--|
| 便宜模型漂移（质量悄悄降） | Phase 1 试点 + #269 首交率 + 欧阳锋审查反馈是天然质量门 |
| Pro 涨价（08-06 公告） | 落地前复核价格；Phase 1 先小规模验证 ROI |
| Kimi vs DeepSeek 双提供商维护 | 维持现状——只有老顽童切 Pro（DeepSeek 内升级，不动 Kimi 侧） |
| Flash 试点质量不达标 | 回滚 = 改一行 config；Hermes profile-guard.py 可快照回滚（P-23 已建） |

## 七、不做的事（明确拒绝）

- ❌ 不建自动路由网关（YAGNI——手动分级已覆盖 KDO 场景）
- ❌ 不让欧阳锋/王语嫣切模型（订阅制成本固定，动了反而乱）
- ❌ 不搞 ensembling/双模型并行（成本 2×，KDO 无此量级需求）

---
*方案：黄药师 2026-08-09 | 待王语嫣/欧阳锋批准后执行 Phase 1*

---

## 用户实测修正（2026-08-10 用户实证——覆盖本文档"倒挂"推断）

**用户实测：deepseek-v4-flash 实际强于当前 pro 预览版**（欧阳锋本人会话亦运行于 flash）。

- 本文档 §一"倒挂"结论基于参数规模（284B vs 1.6T）与第三方定价推断——**实测优先于推断**（O-11 验证方法决定结论）
- §四 成本测算与 §五 Phase 1（老顽童切 Pro 试点）前提重估：flash 作深度生产可能无倒挂，ROI 待涨价新价 + 实测再议
- 仍有效：任务分级思维（T1 批量/T2 生产/T3 审查）、质量门兜底、不做网关 YAGNI
- 识图/视觉任务：kdo 内 minimax API 可调用（勿重复造轮子）
