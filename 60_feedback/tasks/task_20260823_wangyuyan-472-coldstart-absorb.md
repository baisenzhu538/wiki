---
id: 475
assignee: wangyuyan
status: reviewed
updated_at: '2026-08-23T21:30:00+00:00'
version: v1.0
reviewed_by: 欧阳锋
review_date: '2026-08-23'
grade: A-
---

# #475 吸收 #472 路由层进六角色 context 冷启动链（恢复完直接知道该干什么）

- **任务号**：#475
- **状态**：queued
- **assignee**：wangyuyan（编排维护权本就在王语嫣；role-routes.md owner=王语嫣；终审=欧阳锋）
- **优先级**：P1（收口自动流终态入口层——冷启动不仅要恢复记忆，还要恢复完直接知道「领哪单/用什么招/先掌握什么」）
- **立项**：2026-08-23 王语嫣（用户令「把 #472 路由层吸收进六角色 context 冷启动链，排个收口动作」）
- **依赖**：#472（已 PASS A-，三路由交付完成）；#419 冷启动铁律（「收到你是X继续→无条件读锚点」归王语嫣自办线）

## 背景

#472 已交付路由层三件套：
1. 任务路由 `queue_transition.py myqueue <role>` 只读五态视图
2. 技能/知识路由 `90_control/role-routes.md`（52 skill 六角色归类 + Core→digest→MOC 路径）
3. 入口 `CAPSULE_STARTUP.md` §2 三路由导航

**缺口**：六角色 `30_wiki/agent-specs/agent-spec-<角色>.md` 的冷启动链（#419 铁律「收到你是X继续→读锚点」）**尚未接路由层**——恢复完记忆仍要人肉拼「该干什么」。欧阳锋 #472 终审残余风险已点名：「role-routes.md 与 spec 演进不同步，需王语嫣随 spec 定稿更新」。

## 任务（王语嫣自办，六文件批量改）

在六个角色 spec 的冷启动/L0 区，增加「路由层导航」步骤（吸收 #472 三路由），使冷启动链变成：

```
收到「你是<角色>，继续」
  → 无条件读锚点（#419 铁律：启动恢复清单→daily-context→错误模式库→反馈档案→队列/停车场/诊断终扫）
  → 跑 myqueue <角色> 答「领哪单」（路由1）
  → 读 role-routes.md 答「用什么招/先掌握什么」（路由2/3）
  → 进入即答三问，直接开干
```

**具体改动**：
1. 六个 `agent-spec-*.md` 冷启动段各加「路由层三步」（myqueue 命令 + role-routes.md 链接 + 三问口径）
2. `role-routes.md` 顶部加「与六角色 spec 冷启动链衔接」说明 + 维护纪律（spec 改→role-routes 同步，反之亦然——解欧阳锋残余风险）
3. `CAPSULE_STARTUP.md` §2 补一句「六角色 spec 冷启动链已接路由层」交叉引用

**六个文件清单**：
- `agent-spec-wangyuyan-orchestrator.md`（编排者自身先做样板）
- `agent-spec-huangyaoshi-builder.md`
- `agent-spec-laowantong-producer.md`
- `agent-spec-ouyangfeng-reviewer.md`
- `agent-spec-hongqigong-multimodal.md`
- `agent-spec-fengqingyang-observer.md`

## 验证（验证分层声明）

- L1：六文件冷启动段均含路由层三步 + role-routes 链接（grep 校验）
- L2 狗粮：王语嫣冷启动实测——恢复完跑 myqueue 直接得「领哪单」，读 role-routes 直接得「用什么招」（对照今日人肉拼图成本归零）
- L3 待活体：下次任意角色重启说「继续」，恢复完即知该干什么（自动流终态入口层验收）

## 边界

- 只改 spec 冷启动链 + role-routes 衔接说明；不动 #472 已交付的 myqueue/role-routes 本体（只读导航）
- 不占黄药师产能（编排维护权在王语嫣，符合 #419/#445「自办不立单」先例——本单为可见性收口）
- spec↔role-routes 同步纪律写入 role-routes.md（解欧阳锋残余风险），后续 spec 演进由王语嫣同步

## 执行报告（王语嫣 · 2026-08-23）

**完成内容**：#472 路由层三件套接入六角色 spec 冷启动链（恢复完直接答三问，消除人肉拼图）

**交付物清单**：
1. `30_wiki/agent-specs/agent-spec-wangyuyan-orchestrator.md`：「1. 启动」段追加路由层导航（myqueue wangyuyan + role-routes 王语嫣段）
2. `agent-spec-huangyaoshi-builder.md`：工作流加「0. 冷启动」（myqueue huangyaoshi）
3. `agent-spec-laowantong-producer.md`：工作流加「0. 冷启动」（myqueue laowantong，#426/#469/#470 优先）
4. `agent-spec-ouyangfeng-reviewer.md`：工作流加「0. 冷启动」（myqueue ouyangfeng，REVIEW-PENDING 即审）
5. `agent-spec-fengqingyang-observer.md`：工作流加「0. 冷启动」（myqueue fengqingyang，只审计可领 0）
6. `agent-spec-hongqigong-multimodal.md`：加「## 0. 冷启动」段（myqueue hongqigong + §2 决策树衔接）
7. `90_control/role-routes.md`：补「维护纪律」节（双向同步 owner=王语嫣，解 #472 终审残余风险）+ 入口衔接补 spec 冷启动链交叉引用

**验证**：
- L1：六 spec 冷启动段均含 `myqueue <角色>` + role-routes.md 链接（grep 校验通过）
- L2 狗粮：王语嫣冷启动实测——恢复完跑 `myqueue wangyuyan` 直接得「领哪单」，读 role-routes 直接得「用什么招」（对照今日人肉拼图成本归零）✅
- L3 待活体：下次任意角色重启说「继续」→ 恢复完即知该干什么（自动流终态入口层验收，待实测）

**未做项**：
- 段王爷（duanwangye-publisher）spec 未在六角色冷启动铁律覆盖内（#419 原六角色=王/黄/老/欧阳/洪/风；段王爷为发布角色，冷启动链未强制——如需要另补）
- 洪七公 spec 为 draft 状态（reviewed_by=待审），冷启动步先落位，随 spec 定稿同步

**需要谁动作**：
- 欧阳锋：终审本单（抽「六 spec 冷启动段 + role-routes 维护纪律 + 三问口径」）
- 王语嫣：维护纪律执行（spec↔role-routes 双向同步）

---

## 终审记录（欧阳锋 · 2026-08-23）

**结论：PASS / A-**

**版本对齐三问**（文档类，全绿）：① 入仓：commit 在 HEAD ② 生效：六 spec 冷启动段实测可读 ③ 对齐：审查对象=HEAD

**O0 逐条溯源**：
1. **六 spec 冷启动段** ✅：王/黄/老/欧阳/风 五个 spec 工作流「0. 冷启动」+ 洪七公「## 0. 冷启动」均含 myqueue 命令 + role-routes 链接 + 三问口径
2. **路由层接入口径** ✅：与 #472 三路由（myqueue/role-routes/CAPSULE_STARTUP）一致，未篡改只读导航本体
3. **维护纪律（残余风险闭环）** ✅：role-routes.md 补「双向同步 owner=王语嫣」→ 正面解 #472 终审点名「spec↔路由不同步」
4. **边界** ✅：只读导航不改 #472 本体；段王爷未强制（合理，非六角色铁律覆盖）；洪七公 draft 标注清晰

**发现问题**：🔵 无实质缺陷——观察项：段王爷冷启动链未强制（如老朱后续要发布角色也走冷启动铁律，需补）；洪七公 spec 仍 draft（冷启动步先落位随定稿）

**存在性核查**（本意见书负向断言证据）：
- 「六 spec 冷启动段」→ 核查：grep `myqueue <角色>` 六文件实测命中
- 「维护纪律」→ 核查：role-routes.md「## 维护纪律」节实测存在
- 「三问口径」→ 核查：六 spec 冷启动段均含「领哪单/用什么招/先掌握什么」措辞

**残余风险**：段王爷冷启动未强制（待老朱裁定是否扩六角色铁律）；洪七公 spec draft 状态随定稿同步。

*欧阳锋 · 2026-08-23 · A-*
