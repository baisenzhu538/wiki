---
id: 473
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-23T11:37:49.096109+00:00'
version: v1.0
doc_id: D-20260823-021
instance: huangyaoshi
reviewed_by: 欧阳锋
review_date: '2026-08-23'
grade: A-
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

---

## 终审记录（欧阳锋 · 2026-08-23）

**结论：PASS / A-**

**版本对齐三问**（代码类，全绿）：① 入仓：9f194c2a7（19:33）在 HEAD ② 生效：wiki L9 独立实跑 ③ 对齐：审查对象=HEAD

**O0 逐条溯源**：
1. **wiki 卡侧 L9** ✅：`_wiki_card_frontmatter()`（只读头部 2048B）+ `check_id_namespace` 混用检查——独立实跑性能优秀且**抓到真实违规**：`agent-spec-zhu-boss.md` 含 doc_id（E045 实证——**我 #448 终审时漏检的**，工具补上）+ **一批任务单 frontmatter 带 doc_id**（#463/#464/#471/#472/#473 等——#449 规范"任务单沿用队列号"被执行偏差，处置归王语嫣）
2. **冻结无状态化** ✅：删 frozen-registry.json（git rm 实测）+ PROPOSAL-PENDING 段动态清单 + git HEAD diff 锚点（`_git_diff_quiet`/`_is_tracked_by_git`）——无同步漂移（我的建议书方案二采纳）
3. **测试独立复现** ✅：18 passed（冻结无状态正反 3 + L9 wiki 隔离）——报告全量 53
4. **第 3 项拆出** ✅：kdo lint 集成需 KDO 独立仓库（workspace.py lint 引擎 + 561 测试回归）——边界拆出诚实声明，建议独立单
5. **边界** ✅：不动 #449 规范本体；向前生效日期第 4 项（低优）观察期后定

**发现问题**：
- 🟠 **任务单 doc_id 批违规**（工具实证）：#449 规范"三套编号不混用（E045）：任务单沿用 #队列号"——但 13:51 规范生效后的新任务单普遍带 doc_id——执行偏差（四件套惯性全加），处置归王语嫣（移除或登记口径）
- 🔵 我的审查盲区：zhu-boss 卡 doc_id 混用我 #448 终审未检出——**终审时应跑 file-flow-check 作例行检查**（#450 工具上线后），记入审查流程

**魔鬼代言人**：3 个月后最可能出问题——任务单 doc_id 批违规不清（编号体系继续混用）；或冻结动态清单在 PROPOSAL-PENDING 段被王语嫣划行后清单变化误报（git diff 锚点已兜底）

**存在性核查**（本意见书负向断言证据）：
- 「冻结文件已删」→ 核查：ls frozen-registry.json 不存在 + git show HEAD 删除记录
- 「wiki L9 真实违规」→ 核查：独立实跑输出（zhu-boss + 任务单批 doc_id 行）
- 「18 passed」→ 核查：pytest 独立复现输出
- 「拆出声明」→ 核查：执行报告未做项（KDO 侧 561 测试回归成本）

**残余风险**：任务单 doc_id 批处置待王语嫣；kdo lint 集成独立单；审查流程补 file-flow-check 例行。

*欧阳锋 · 2026-08-23 · A-*
