# 建议书：CAPSULE_STARTUP 欧阳锋行恢复链缺 amnesia 锚点——会话恢复完整性缺口（欧阳锋 · 2026-08-24）

## 发现

`.kdo/CAPSULE_STARTUP.md` §2 角色表（KDO 唯一启动指针，#366）——欧阳锋行恢复链：

```
.agent/ouyangfeng-context.md → .agent/context.md → 队列 → ../agent复盘/ouyangfeng/daily-context/ 最新
```

**缺 `20_memory/ouyangfeng-amnesia-recovery.md`（失忆锚点）**——对比黄药师行（"失忆恢复锚点 `20_memory/huangyaoshi-amnesia-recovery.md`"）、洪七公/老顽童等角色行均各有锚点标注，唯欧阳锋行缺失。

## 风险

1. **恢复链断裂**：会话级记忆（Claude Code MEMORY.md 索引）若丢失/换工具/新实例，项目级启动指针跳过 amnesia——**出口自检钩子（🔴🔴 无豁免条款）、#499/#470/#498 三 FAIL 状态、声称-交付比对方法论、37 张双三角待办等最新状态全部在 amnesia 里，恢复不到**
2. **角色不对称**：欧阳锋是全库审查中枢（"重启说继续即回全链状态"是恢复指引的核心承诺），恢复链反而比执行角色少一环
3. **双实例风险**：飞书端（Hermes）不读 Claude 侧记忆——其恢复完全依赖项目级指针——缺口对飞书端影响更大

## 建议（供王语嫣/黄药师处置）

- **方案 A（推荐，一行改动）**：CAPSULE_STARTUP §2 欧阳锋行恢复链补 `20_memory/ouyangfeng-amnesia-recovery.md`（对齐黄药师行格式）
- **方案 B（可选）**：审计全部角色行恢复链是否含各自 amnesia 锚点（欧阳锋缺行可能是历史遗漏——其他角色也可能有缺）

## 关联

- #366（CAPSULE_STARTUP 唯一启动指针）
- #501（角色待办收件箱——同表挂载，本单同位置）
- 记忆 [[ouyangfeng-session-resume-guide]]（会话级恢复指引——4 文件含 amnesia，但项目级指针缺）

## 需要谁动作

- **黄药师**：CAPSULE_STARTUP §2 补行（一行）
- **王语嫣**：裁定（若走 B 则审计全部角色行）
- **欧阳锋**：验收（补行后重启链闭合）

*欧阳锋 · 2026-08-24 · 建议书（恢复链自查发现）*
