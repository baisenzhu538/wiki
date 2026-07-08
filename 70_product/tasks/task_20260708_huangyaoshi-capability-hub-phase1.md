---
id: task_20260708_huangyaoshi-capability-hub-phase1
title: P-23 能力中台 Phase 1：VLM 能力上线 + Agent 共享工具底座
status: queued
priority: P0
assignee: 黄药师
reviewer: 欧阳锋
expected_cards: 0
expected_code_modules: 1
source_refs:
  - 30_wiki/decisions/plan_20260707_capability-hub-architecture.md
  - 70_product/tasks/parking-lot-huangyaoshi.md
related:
  - "[[plan_20260707_capability-hub-architecture]]"
  - "[[framework-yihang-dual-triangle-weapon-library]]"
  - "[[framework-yihang-fde-ai-native-org]]"
created_at: 2026-07-08
updated_at: 2026-07-08
---

# P-23 能力中台 Phase 1：VLM 能力上线 + Agent 共享工具底座

> 来源：黄药师停车场 P-23 + `plan_20260707_capability-hub-architecture.md`
> 王语嫣判断：#139-#143 域 Agent 军团需要统一调用 VLM/OCR/搜索等共享能力，否则每个 Agent 都会重复写工具调用逻辑，形成新一轮碎片化。P-23 Phase 1 是后续所有 Agent 建设的硬前置，应优先入队。

---

## 一、目标产出

### Phase 1（0.5-1 天）

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 1 | 能力中台骨架 | code module | `_capability_hub/registry.py` | 能力注册表：自发现、list、get |
| 2 | 能力基类 | code module | `_capability_hub/base.py` | 所有能力继承的基类 |
| 3 | 统一配置 | code module | `_capability_hub/config.py` | API Keys（MiniMax 等）集中配置 |
| 4 | VLM 能力模块 | code module | `_capability_hub/vlm/__init__.py` + `core.py` | 自注册 VLM 能力；内部封装 MiniMax API |
| 5 | 能力列表 CLI | command | `python -m capability_hub list` | Agent 启动时可见：可用工具、说明书、可实例化 Agent 配置 |
| 6 | 旧脚本兼容迁移 | code update | `run_vlm_*.py` | 改为调用 `_capability_hub/vlm` |
| 7 | Agent 启动序列更新 | doc update | `.agent/startup.md` | 所有 Agent 启动序列加入 `python -m capability_hub list` |

---

## 二、验收标准

- [ ] `_capability_hub/` 目录结构按架构方案落地。
- [ ] `python -m capability_hub list` 可运行，输出至少包含 `vlm` 能力及状态。
- [ ] Agent 调用 VLM 的代码统一为：
  ```python
  from capability_hub.vlm import process
  result = process("00_inbox/test.png")
  ```
- [ ] Windows 绝对路径与 WSL 相对路径跨平台测试通过。
- [ ] 旧 `run_vlm_*.py` 脚本向后兼容或迁移完成。
- [ ] `.agent/startup.md` 武器库清单中加入能力中台。
- [ ] Hermes Agent Python venv 已安装 MiniMax SDK（如适用）。
- [ ] 欧阳锋终审通过。

---

## 三、最终判断

**评级：A（硬前置，必须优先）**

- 没有统一能力层，#139-#143 每个 Agent 都会重复写 VLM/OCR 调用，回到碎片化。
- 工作量小（0.5-1 天），收益大（所有 Agent 共享）。
- 与 P-23  parking lot 描述一致，架构方案已 draft。

**建议入队编号**：`#144`
**优先级**：P0
**Assignee**：黄药师
**Reviewer**：欧阳锋
**预计工时**：0.5-1 天
**依赖**：无
**阻塞**：#143 跨域双三角诊断 Agent、#139-#142 域 Agent 均依赖 P-23 完成后才能稳定调用共享能力

---

*王语嫣 2026-07-08*
