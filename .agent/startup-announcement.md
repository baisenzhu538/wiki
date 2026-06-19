# 全厂通知：启动文件与基建公告已上线

> 发布时间：2026-06-19  
> 面向：欧阳锋、黄药师、老顽童、王语嫣、洪七公、段王爷  
> 发布人：洪七公（按用户要求广播）

## 两件事已生效

1. **`.agent/startup.md` 已上线**
   - 每个 Agent 启动后、领任务前，必须先读此文件。
   - 内容：工厂全局、工具清单、5 条高频铁律、当前谁在做什么、紧急注意、快速导航。

2. **`.agent/infrastructure-bulletin.md` 同步生效**
   - 新增“工具登记四步法”正式写入规则变更。
   - 四步法：
     1. 脚本放入 `40_outputs/code/scripts/`
     2. 登记到 `40_outputs/code/scripts/README.md`
     3. 复杂决策逻辑写 skill 到 `40_outputs/capabilities/skills/`
     4. 相关 skill 之间互相引用
   - 不登记 = 不存在。

## 角色行动

| 角色 | 行动 |
|:--|:--|
| 欧阳锋 | 在架构审查/抽检时确认 Agent 已读取 startup.md |
| 黄药师 | 新增工具/脚本时按四步法登记；在 CLI/基建变更时同步更新 bulletin |
| 老顽童 | 启动后先读 startup.md，再领 dashboard 任务 |
| 王语嫣 | 审计时把“是否登记”作为工具可用性检查项 |
| 洪七公 | 已执行广播；新增视觉/多模态脚本时按四步法登记 |
| 段王爷 | 发布前检查所依赖工具是否已在 README/skill 中登记 |

---

**请各角色在下次启动时确认已阅读：**
- `C:\Users\Administrator\Desktop\wiki\.agent\startup.md`
- `C:\Users\Administrator\Desktop\wiki\.agent\infrastructure-bulletin.md`
