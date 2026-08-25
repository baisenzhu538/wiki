---
id: 532
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-25T18:12:04.824228+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- 90_control/kdo-seed/
- kdo-tools/
---

# #532 kdo-seed 种子包：机制层整体搬迁三件套 + 路径参数化

- **任务号**：#532
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P1（老朱 08-26 拍板：第二台机器要起一座同构工厂，机制不走样）
- **立项**：2026-08-26 王语嫣（老朱问「整个 KDO 基础设施如何搬到另一台电脑」，方案经老朱确认）

## 背景

KDO 基础设施实测拆三层：**A 机制层**（角色文件 `.agent/`+`agents/{五角色}`、制度层 charter v1.3/schemas/quality-gates/quality-metrics-spec/consumer-retrieval-protocol、工具层 kdo-tools 核心脚本+90_control/scripts 检查类、九层目录骨架）原样可复制；**B 机器绑定层**（5 个计划任务 .cmd 包装器、schtasks 注册、Python 路径、AGENTS.md 工作目录判断句）必须重建；**C 实例内容层**（30_wiki 卡片、队列行、60_feedback 历史、复盘档案）不搬，新库从 #001 重新长。

**风险点**：机制层有 23 处硬编码 `C:\Users\Administrator\Desktop\wiki`（5 个 .cmd + 若干 py），靠人肉 checklist 改必漏，漏一处就是 #519 式静默失效。

## 任务

1. **种子目录** `90_control/kdo-seed/`：A 层机制文件全集 + 九层空骨架 + 桌面 agent复盘/{五角色}/daily-context 骨架说明；域相关采集脚本（抖音/微信/利润为王系）剔除
2. **bootstrap 开机手册**：新机器五步——放种子→设 `KDO_ROOT`→跑 seed-check→注册 schtasks（附现成注册命令模板）→五角色启动五连读验证
3. **seed-check.py 自检脚本**：目录齐不齐、计划任务注册没注册、探针首轮有无回执、角色文件可读性——把「机制不走样」从人工核对变成脚本保证
4. **路径参数化**：A 层脚本硬编码路径改读 `KDO_ROOT` 环境变量（缺省回退脚本相对路径推导）；.cmd 包装器改为从环境变量取根目录

## 边界

- 只搬机制，不搬任何本库内容数据；不改本库现有脚本行为（参数化后本机照常跑，回归验证）
- schtasks 注册命令写进手册即可，不在本机执行任何新注册
- 技术域（软硬件）适配不在本单，走 #533

## 验收

- 种子目录完整（seed-check 自证）；本机既有探针/门禁/队列脚本回归全过；手册经王语嫣过一遍可执行性
- 欧阳锋终审
