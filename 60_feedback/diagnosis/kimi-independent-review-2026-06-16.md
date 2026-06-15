# Kimi Code CLI 对欧阳锋抽检结论的独立判断

**日期**：2026-06-16  
**依据**：欧阳锋（Claudian）10 张卡抽检结论 + Kimi Code CLI 全库扫描数据  
**角色**：独立判断，不附和、不盲从

---

## 一、我验证的关键事实

在欧阳锋结论基础上，我用脚本扫描了全库：

| 事实 | 欧阳锋结论 | Kimi 验证结果 |
|:-----|:-----------|:--------------|
| 跨目录重复卡片 | 提到 McKinsey 家族 2-3 组 | **实际 15 组**，涉及 McKinsey、yt-pitch、yt-tool、yt-unit-model |
| diagnostic_signals 覆盖率 | "填充率不高" | **总体 23.5%**，framework 79.7%、tool 76.2%、concept 16.5%、**case 6.5%、skill 1.9%** |
| deprecated 卡 | "归档流程缺位" | **实际仅 1 张**：`concept-一堂-business-prediction.md` |
| 当前 P1 大头 | 未重点提及 | `author=legacy` 712 张、`dangling 链接` 505 张 |

---

## 二、我的独立判断

### ✅ 同意欧阳锋的部分

1. **卡片重复/知识分裂是 P0 级问题**
   - 15 组同 ID 卡片跨目录存放，部分文件内容不同（如 `concept-mckinsey-issue-tree` 在 concepts/ 和 tools/ 内容有差异）。
   - 这是知识库结构层面的腐败，会导致：同一概念多个版本、链接指向不确定、检索重复、AI 混淆。
   - **必须立即处理**。

2. **diagnostic_signals 遗漏是真实缺口**
   - 不是"要不要填"的问题，是"case 和 skill 几乎没填"的问题。
   - framework/tool 已经由黄药师的 K 任务补到 70-80%，但 case 6.5%、skill 1.9% 接近空白。
   - 诊断型知识库缺了 diagnostic_signals，就像武器库缺了扳机。

3. **v1.5 校验器存在格式假阳性**
   - `不适用场景` vs `dont-use`、`外部攻击` vs `external-attacks` 这种字符串匹配确实机械。
   - 校验器应该支持 heading 别名映射，而不是要求作者死记硬背内部字段名。

### ⚠️ 修正欧阳锋的部分

1. **"v1.5 通过率 18.1% 严重低估，实际 40-50%"——我不同意这个修正幅度**
   - 欧阳锋只抽了 10 张卡，样本太小，且 10 张里 5 张 FAILED。
   - "格式"不是假阳性，而是可解析性的一部分。如果 section heading 不统一，AI 在 RAG/system prompt 里读取时也会困惑。
   - 更准确的判断：**18.1% 可能低估，但 40-50% 也可能高估**。真实通过率可能在 25-35% 之间。
   - 正确的动作不是"放宽校验"，而是"校验器支持语义别名 + 作者逐步对齐格式"。

2. **"暗知识卡 source_refs 引用 wiki 链接合理"——我不同意**
   - `source_refs` 的设计目的是**追溯到原始素材**（口述稿、文献、实验记录），不是"相关概念"。
   - 暗知识卡如果 source_refs 只写 wiki 链接，就切断了原始来源，失去了 KDO 的溯源能力。
   - 正确做法：
     - `source_refs` 仍指向原始 source 文件，或标注 `synthesized`
     - 相关概念链接放在 `related` / `Synthesis` 章节 / `bridges_to` 中
   - 这是**工具不该妥协**的边界，不是"工具局限"。

3. **"deprecated 卡是大问题"——我不同意其严重性**
   - 全库只有 1 张 deprecated 卡，不是系统性问题。
   - 归档 SOP 确实需要，但优先级是 **P2**，不是 P0/P1。
   - 不要被单张卡的 ERROR 放大成全局危机。

4. **"卡片质量 6/10"——样本不足以支撑这个结论**
   - 10 张样本里包含了 McKinsey、一堂、暗知识、案例等不同类型，但无法推断全库 1359 张卡。
   - 更客观的表述：**抽检样本中部分 FAILED 卡内容质量不低，但格式和诊断信号存在真实缺口**。

---

## 三、我认为的真正优先级

基于全库数据和内容/工具分工原则：

### 🔴 P0：卡片重复合并（15 组）

- 这是知识分裂，必须立即止血。
- 对每组重复 ID：
  1. 比较两个版本，判断哪个更完整/更新
  2. 合并内容到唯一位置
  3. 删除或归档另一个位置
  4. 更新所有指向该 ID 的链接
- **负责人**：老顽童（内容判断），黄药师提供 diff/合并辅助脚本

### 🟡 P1：diagnostic_signals 补全（聚焦 case/skill）

- framework/tool 覆盖率已够，重点补 **case 6.5%** 和 **skill 1.9%**。
- 不要等 LLM 自动生成——老顽童根据卡片内容手动补 2-3 条 triplet。
- 黄药师优化 scaffold/enrich，让新卡默认带 diagnostic_signals TODO。

### 🟡 P1：author=legacy + dangling 链接

- 这是当前 P1=773 的绝对大头（712 + 505）。
- author=legacy 需要老顽童判断真实作者；dangling 需要判断是 stub/修正/删除。
- 黄药师提供清单和批量辅助，但不参与内容判断。

### 🟡 P1：v1.5 校验器支持 section heading 别名

- 黄药师负责：把 `不适用场景` 映射到 `dont-use`，`外部攻击` 映射到 `external-attacks` 等。
- 目标：减少假阳性，但不放松对内容结构的要求。

### 🟢 P2：deprecated 归档 SOP

- 定义 deprecated 卡处理流程：移入 `_archive/`、保留 redirect、从 validate 范围排除。
- 当前只有 1 张卡，不急。

### 🟢 P2：source_refs 语义澄清

- 明确 `source_refs` 只接受：原始 source 文件路径、文献引用、`source_unknown`、`synthesized`。
- 不接受 wiki 链接作为唯一 source_ref。

---

## 四、对当前任务安排的修正

我之前给老顽童排的 E1-E5 任务基本方向没错，但**优先级需要调整**：

| 原任务 | 修正 |
|:-------|:-----|
| E1 author=legacy | 保持 P1，但让位于 P0 卡片重复 |
| E2 dangling 链接 | 保持 P1，与 E1 并行 |
| E3 status/confidence 不一致 | 降级为 P2，数量少且风险低 |
| E4 source_refs 为空 | 保持 P1，但严格限定 source_refs 语义 |
| E5 flat tags 人工判断 | 保持 P1，可在碎片时间做 |

**新增 P0 任务**：卡片重复合并（15 组）。

**黄药师的任务**：
- 优先做 v1.5 校验器别名支持
- 提供跨目录重复 ID 检测/合并辅助脚本
- 不要碰内容判断

---

## 五、结论

欧阳锋的抽检有价值，但存在两个倾向：
1. **过度强调内容质量被低估**：10 张样本不足以推翻全库数据，且格式统一本身就是质量。
2. **对某些问题严重性放大**：deprecated 卡和 source_refs wiki 链接不是全局危机。

**真正的 P0 是卡片重复/知识分裂**。这是结构性腐败，会随时间指数级恶化。diagnostic_signals、author=legacy、dangling 链接是 P1 重点。其余问题按 P2 处理。

---

Kimi Code CLI
2026-06-16
