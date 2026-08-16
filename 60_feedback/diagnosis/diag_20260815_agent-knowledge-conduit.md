# 知识库→Agent 传导机制盘点诊断（#324 · P0）

> 诊断者：王语嫣（2026-08-15）
> 触发：用户要求「知识库的更新能够惠及所有 agent，这是系统性工程」
> 状态：已提审，待欧阳锋终审

---

## 一、背景

用户指出：知识库持续生产新知识（如 #320/321/322 销售卡组），但 agent 消费知识的方式割裂，新知识入库**不会自动传导**到任何 agent。这不是单点问题（销售对话助理要不要接入），是架构级问题：**知识库→agent 的传导管线缺失**。

## 二、现状矩阵（实测，2026-08-15 逐个查部署文件）

### Hermes 端（~/.hermes/profiles/，8 个 profile）

| agent | kdo MCP（kdo-tools/mcp/server.py） | 知识形态 | 增量传导 |
|:--|:--:|:--|:--:|
| basic-skills-coach | ✅ | SOUL/CLAUDE + MCP 检索（#308 模式） | ⚠️ 半自动 |
| coaching-leadership-assistant | ✅ | SOUL 内嵌核心 + MCP 检索 | ⚠️ 半自动 |
| meeting-assistant | ✅ | SOUL 内嵌核心 + MCP 检索 | ⚠️ 半自动 |
| duanwangye / hongqigong / laowantong / wangyuyan | ❌ | config.yaml 检索指令（prompt 级，非 MCP） | ❌ 静态 |
| note-coach | ❌ | 无检索配置 | ❌ 静态 |

### Claude CLI 端（wiki/.agent/ + wiki/agents/）

| agent | 知识形态 | 检索能力 | 增量传导 |
|:--|:--|:--|:--:|
| 销售对话助理（agents/sales-dialogue-assistant/） | **编译快照**（.agent/prompts/sales-dialogue-assistant.md，7-04 编译）+ CLAUDE.md 写死 5 卡路径 | kdo query 指令（CLI） | ❌ 手动重编译 |
| CLI 六角色（wangyuyan/ouyangfeng/huangyaoshi/laowantong/duanwangye/hongqigong） | context 静态文件（.agent/*-context.md，均有 kdo query 指令） | kdo query（依赖自觉+索引） | ❌ 静态 |
| prompts 编译产物（33 个 agent-*/tool-agent-spec-*） | 编译快照（最新 7-04，**卡片更新后需重新编译**——frontmatter 自注） | 无 | ❌ 手动重编译 |

### 检索底座

- `kdo-tools/mcp/server.py`（MCP server，4 工具）——仅 3 个 Hermes profile 挂载
- `search_index.json`（614MB，今日 12:58 刷新）——索引有更新机制，但属**定期批量**，无事件驱动
- 08-14 健康检查（60_feedback/auto/）——健康检查雏形已存在

## 三、机制缺陷定位（系统性，非单点）

1. **知识变更无事件**（最大缺口）：卡入库/更新后无任何机制通知依赖它的 agent——编译快照永远过期；检索索引靠定期刷新（今天 12:58 撞上，不代表总是）；E028 实证过索引滞后
2. **检索接入不均**：MCP 检索只给了 8 月的新助理（#308 推广面 3/8 Hermes profile）；CLI 端全靠 prompt 自觉执行 kdo query；快照型 agent 完全不检索
3. **导航覆盖不全**：digest/MOC 缺失系统性（销售域今天才补 #321；E015 实证"先查 digest"退化成 grep 碰运气）——检索规则的前提是导航完整
4. **新鲜度无监控**：无 freshness 元数据消费、无"新知识使用频率/无效知识比例"指标（行业最佳实践），健康检查是静态快照非持续化

## 四、行业调研（2026-08-15 全网，≥2 独立来源）

**共识：知识传导已是工程问题，不再只是检索问题。**

1. **增量事件驱动同步**取代批量重建（Redis/CDC、Observe.ai context center）："知识库更新 → agent 立即可用，而非等待静态文档上传"——**stale context 是最常见 RAG 生产事故**（FutureAGI）
2. **统一检索层 = MCP 标准**（Microsoft Foundry IQ）：多 agent 连同一知识层，`knowledge_base_retrieve` MCP 工具集中管理——"对知识的改进惠及每个连接的 agent"（**与 #308 kdo MCP 同构，方向被验证**）
3. **变更订阅协议**（ContextSync Protocol）："MCP 解决 agent 连**工具**；ContextSync 解决 agent 连**组织上下文**"——版本化状态 + 变更订阅（毫秒级推送）+ 权限 + 溯源
4. **治理层 + 版本化 + 监控**（Atlan/腾讯云/FutureAGI）：语料版本化（SHA256/快照/回滚）、freshness 测试、召回率/无效知识比例/新知识使用频率持续监控

来源：[Redis](https://redis.io/blog/real-time-context-ai-agents-fresh-inputs.md) · [Observe.ai](https://www.observe.ai/blog/context-center-for-cx-curing-the-stale-knowledge-problem) · [FutureAGI stale context](https://futureagi.com/glossary/stale-context/) · [Microsoft Foundry IQ](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/foundry-iq-connect) · [ContextSync Protocol](https://github.com/metisos/contextsync-protocol) · [Atlan](https://atlan.com/know/context-engineering/context-engineering-for-rag-agents/) · [腾讯云](https://cloud.tencent.com/developer/article/2687069)

## 五、目标架构：三层传导管线（方向与行业共识一致）

```
知识库生产（卡入库）          ┌─ ① 检索层（治本）：kdo MCP 全 agent 标准化挂载
    │                        │   知识库=可检索系统，卡在库就能被找到
    ▼                        ├─ ② 导航层（保障可达）：digest/MOC 制度化
 索引更新（事件驱动化）        │   生产流水线门禁：新卡必挂 digest + 可检索
    │                        └─ ③ 刷新层（淘汰快照）：编译产物→按需生成
    ▼                            快照型 agent 迁移"检索+引用"模式
 agent 消费（统一检索+导航）
```

## 六、P1-P3 落地建议

**P1 统一检索层（收益最大，先做）**
- 3 个 MCP profile 已有 → 推广到剩余 5 个 Hermes profile（duanwangye/hongqigong/laowantong/wangyuyan/note-coach）——复制 config 节即可
- 快照型 agent（销售对话助理/AI 基本功教练）CLAUDE.md 加"先 kdo query 再查路径表"指令
- 索引事件驱动化：kdo 生产流水线（#263）加"终审闭环 → 触发索引增量更新"环节（E028 纪律机制化）

**P2 导航制度化**
- digest 补全（销售域 #321 已立项，其余缺 digest 域排队）
- 生产流水线门禁：#263 加检查项——新卡必须①挂域 digest ②`kdo query` 可检索（E028 闭环入流水线）
- domain-mapping 挂接全部 digest（单一真相源）

**P3 快照型迁移（试点：销售对话助理）**
- 重编译 prompts 纳入新卡（短期止血）+ CLAUDE.md 路径表升级为 digest 导航（中期）
- 长期：编译产物改为"检索+引用"模式，逐步淘汰快照

## 七、边界

- 本诊断只出方案不执行改造（建议先行）
- P1-P3 执行另立项，对齐后拆任务
- 已纳入 #320/321/322 产出（销售域 digest/新卡为 P2 门禁首批试点）

---

## 终审记录（2026-08-16 欧阳锋）

**verdict: PASS A- · methodology v2.3**

O1/O3 独立验证（全部字节级重跑）：
1. **Hermes 3/8 MCP 挂载 ✅ 准确**：Windows 侧 8 profiles 中 3 个（basic-skills-coach/meeting-assistant/coaching-leadership-assistant）config.yaml L90-98 确认挂 `kdo-tools/mcp/server.py`，其余 5 个无 kdo MCP
2. **销售对话助理快照 ✅ 准确**：`.agent/prompts/sales-dialogue-assistant.md` 7-04 01:23，frontmatter 自注"卡片更新后需重新编译"
3. **索引机制 ✅ 准确**：`.kdo/search_index.json` 585.7MB、08-15 12:58:49 刷新；无 Windows 计划任务、WSL cron 仅 health-check 03:07 + watch_inbox 10min——"定期批量、无事件驱动"判断成立
4. **四项机制缺陷定位 ✅ 成立**：知识变更无事件（E028 实证呼应）/检索接入不均/导航覆盖不全（E015 实证）/新鲜度无监控

O1 覆盖率瑕疵（记 TODO，不阻断）：
- **双位置混合部署未入矩阵**：Hermes profiles 实际分 Windows 侧（8 个，本次诊断对象）与 WSL 侧（8 个，beikai/ouyangfeng 等 6 个挂 openmontage MCP 非 kdo）——gateway 服务混合使用两侧，诊断矩阵只覆盖 Windows 侧
- **编译产物数字不准**：报告"33 个/最新 7-04"，实测 prompts 目录 38 个 .md、最新编译 Jul 15 01:33（agent-一堂五步法教练）——"快照全过期"结论方向仍成立（7-04/7-15 均早于 8 月新卡）

**结论**：诊断结论与 P1-P3 建议方向有效，通过。P1 立项时补充：MCP 推广范围按"实际运行 gateway 的 profile"核算（含 WSL 侧 8 个），编译产物按 38 个实际清单核算。
