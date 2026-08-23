---
id: 475
assignee: wangyuyan
status: queued
updated_at: '2026-08-23T21:00:00+00:00'
version: v1.0
doc_id: D-20260823-023
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

## 执行报告（F-034 五字段+验证分层声明，complete 前必填）

（生产者填写）
