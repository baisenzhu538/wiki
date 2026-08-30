# 自攻击报告：#572 第 2 批（2 张卡）

**攻击时间**：2026-08-30
**攻击者**：老顽童（KDO Self-Attack GAN 四路）
**被攻击卡**：
- `case-truman-spring-festival-1000`（春节闭关 1000 条 case）
- `dk-koupen-input-method-loss`（输入法压缩丢稿 dk）

## 攻击摘要
🔴 致命: 0 | 🟡 严重: 0 | 🟢 轻微: 3（3 已就地处理）

## Attacker A: 逻辑
- [🟢] case 卡定位写「第二次飞跃 L2→L3」而 #572 候选描述写「L2 实证」——源稿 L1932 明示「第二次飞跃」=被动→主动=L2→L3，卡内按源稿修正为「L2→L3 实证」，执行报告说明此修正，非漂移。
- [🟢] dk 卡标题「不是工具的错」有绝对化风险——已在「适用边界」第 4 条 + Critique 外部挑战「工具决定论派」双向平衡（工具确实烂时该换就换），逻辑闭环。

## Attacker B: 证据
- [🟢] 两张卡数字（1000 条/10 天/占比 80%、3000 字→两三百字→三句话）均为讲师自述，frontmatter confidence 分级（case 0.75 单案例自述 / dk 0.85 一手亲历）+ source_context 标注「待独立核实」。
- [🟢] dk 卡「质谱输入法」为 STT 误识别（应为「智谱」），引文保留原文 + 加注规范记法，正文统一「智谱」——不擅改源稿、不硬猜（F-061 口径）。

## Attacker C: 完整性
- [🟢] case 卡含 Before-After + 教训×4 + Critique×2（外部攻击者 2 + 内部局限 1）+ 失败模式×3 + When NOT×3 + Action Triggers×4 + Synthesis——对齐 360 case 结构（因系「习惯养成」非「高压交付」，省去隐性成本/事故预演两节，风险已由失败模式×3 覆盖）。
- [🟢] dk 卡 6 标准 section（原始表述/使用场景/操作方法/适用边界/为什么值钱/与其他知识的关联）+ Synthesis + Critique（外部挑战 + 内部局限 + 修复已采纳）——对齐 500vs5000 dk 结构。

## Attacker D: 时效性
- (无发现) 素材为 2026 年春节口述，无过期数据。

## 建议改进（已采纳）
1. case 卡段位标注从候选「L2 实证」修正为「L2→L3 第二次飞跃实证」——以源稿 L1932 为准。
2. dk 卡「质谱→智谱」STT 噪声：引文保留原文 + 加注，正文规范记法。
3. Confidence 分级：case 0.75（单案例自述）/ dk 0.85（一手亲历事故）——按证据层级，不统一虚高。

## 修复确认
两张卡 `kdo pre-submit` 全部 ✅ PASS（WARNING 仅 SOURCE_REACHABILITY=00_inbox 索引外误报 + CONCEPT_CROSSCHECK 提示制，均不拦截）；`kdo index --incremental` → +2（4288 总数）；related 链接（case 7 条 / dk 5 条）grep 实测全部存在（零死链）。
