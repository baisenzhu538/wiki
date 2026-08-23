---
id: 473
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-23T11:33:33.381749+00:00'
version: v1.0
doc_id: D-20260823-021
instance: huangyaoshi
---
# #473 文件流转 lint 遗留三项收口（#450 终审🟠🔵项）

- **任务号**：#473
- **状态**：queued
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣）
- **优先级**：P2（欧阳锋终审遗留项，`diag_20260823_ouyangfeng-file-flow-lint-residuals.md` 采纳）
- **立项**：2026-08-23 王语嫣

## 范围（三项按优先级）

1. **🟠 wiki 卡侧 L9 扫描**：30_wiki 2000+ 卡 frontmatter 队列号/doc_id 混用检查——纯 frontmatter 正则全库一次跑（分钟级，成本可控，一次扫描即可非分批）
2. **🟠 冻结基线动态化**：采用无状态方案（file-flow-check 运行时以 PROPOSAL-PENDING 段+探针登记历史动态生成基线——比基线自动更新更稳，无同步漂移）
3. **🔵 kdo lint 集成**：file-flow-check 挂 kdo lint 检查类或 pre-submit 钩子（文件纪律进入既有质量门）

## 验证（验证分层声明）

- L1 单测三项；L2 狗粮=构造混用卡+已冻结改动各一例全被拦；L3 待活体=下次 lint 日常流程自动含文件流转检查

## 边界

- 只收口三项遗留；不动 #449 规范本体；kdo lint 集成若改动大可拆出（P2 可缓原则）

## 执行报告（2026-08-23 黄药师）

**完成内容**：文件流转 lint 遗留三项收口之二——①wiki 卡侧 L9 扫描（30_wiki 全库卡 frontmatter 混用检查，性能实测 0.95s）；②冻结检测无状态化（删除 frozen-registry.json 持久化基线，改为 PROPOSAL-PENDING 段动态清单 + git HEAD diff 锚点）。第 3 项 kdo lint 集成按任务书边界拆出。

**交付物**（改动文件清单）：
1. `kdo-tools/file-flow-check.py`：`_wiki_card_frontmatter()`（只读头部 2048B）+ `check_id_namespace` 加 wiki 卡侧（id 含 #队列号/doc_id 混用）；`check_frozen` 无状态化（`_git_diff_quiet`/`_is_tracked_by_git`，运行时动态清单）；删除 `cmd_snapshot`/`load_frozen_registry`/`--snapshot`/FROZEN_REGISTRY
2. `kdo-tools/tests/test_file_flow_check.py`：TestL7Frozen 改无状态语义（git diff monkeypatch 注入 3 用例）+ BaseTestCase 加 WIKI_CARDS 隔离
3. `90_control/frozen-registry.json`：**删除**（旧持久化基线废弃，git rm）

**验证**（命令+输出）：
- L1 单测：`pytest tests/`（kdo-tools）→ **53 passed**（冻结无状态正反 3 用例 + L9 wiki 隔离）
- L2 狗粮：①真实库 wiki L9 扫描——**0.95s**（远优于分钟级预估，只读头部优化生效），**抓到真实违规**：`agent-spec-zhu-boss.md` frontmatter 含 doc_id=D-20260823-002（E045 实证，处置归编排）；②真实库全量检查正常（219 文件 error=0）；③冻结无状态——真实 PROPOSAL-PENDING 段动态清单生成正常（当前 7 冻结文件，git diff 锚点零误报）
- L3 待活体：下次 lint 日常流程自动含文件流转检查（kdo lint 集成拆出后待办）；新建议书登记后冻结清单自动含新件

**未做项**：
- **kdo lint 集成（🔵项）按任务书边界拆出**——KDO CLI 在独立仓库（`Knowledge Delivery OS 0.0.1\kdo\workspace.py` lint 引擎），改动需 KDO 侧 561 测试回归；建议后续独立单（挂 `_lint_*` 检查类或 pre-submit 钩子）
- 向前生效日期硬编码（欧阳锋建议书第 4 项，低优）未入本单——观察期后定

**需要谁动作**：
- 王语嫣：处置真实违规（`agent-spec-zhu-boss.md` doc_id 混用——移除或登记口径）
- 欧阳锋：终审本单（抽「wiki 卡 L9 正反/冻结无状态 diff 锚点/拆出声明」）；kdo lint 集成立项裁定
