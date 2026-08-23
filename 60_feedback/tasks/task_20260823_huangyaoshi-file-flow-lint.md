---
id: 450
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-23T08:12:38.422223+00:00'
version: v0.1
instance: huangyaoshi
---
# #450 文件流转规范工具支撑（lint 冻结检查 + 编号查重）

- **任务号**：#450
- **状态**：queued（**依赖 #449 规范 v1.0 老朱拍板生效后开工**——工具实现规范条文）
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣）
- **优先级**：P1（「想犯错也犯不了」的文件纪律层——E046/多写事故的工具化根治）
- **立项**：2026-08-23 王语嫣（老朱协作纪律指令编排双轨之基建轨）

## 任务目标

把《KDO 文件流转规范》（#449）落成机器检查：编号查重、冻结检测、命名合规——文件纪律从自觉变门禁。

## 范围（依 #449 定稿条文实现，以下为预期形态）

1. **doc_id 查重**：lint 检查 `60_feedback/diagnosis/` 全部 doc_id 唯一（D-YYYYMMDD-NNN 格式+跨 agent 全局唯一）；重复或缺失=ERROR
2. **冻结检测**：已交冻结清单（探针登记历史/PROPOSAL-PENDING 划行记录导出）比对 git——冻结文件出现在后续 diff 中=报警（E046 同族根治：任务单既有节被改也能被「节级 hash 快照」捕捉——实现方案黄药师定：节标题 hash 或全文件 hash，权衡精度与误报）
3. **命名合规**：`diag_/task_` 模板正则检查；版本号/amends 引用有效性（amends 指向的 doc_id 必须存在）
4. **接入位**：`kdo lint` 新增检查类 or 独立 `kdo file-flow-check`；pre-submit 与探针登记各挂一道（登记时即查编号唯一，重复当场拒绝登记）

## 验证（验证分层声明）

- L1：单测四组（查重/冻结检测/命名/amends 有效性）
- L2 狗粮：构造冻结文件改动+重复 doc_id 两场景，检查器全部拦住
- L3 待活体：规范生效后首个真实订正件（amends 链）走通

## 边界

- 只做检查工具，不自动改文件；误报进 friction-log 观察期调优（只拦机械项原则）
- 不动 queue_transition/探针核心逻辑（只在登记口挂检查）；依赖 #449 定稿条文，条文变则工具跟

## 关联

- 规范：#449（先序）；charter §3.15（总纲）
- 实证：E046 吞节 / 黄药师 592559104 已交增补先例 / 欧阳锋 append-only 建议书

## 执行报告（2026-08-23 黄药师）

**完成内容**：《KDO 文件流转规范》v1.0（#449）落成机器检查——`kdo-tools/file-flow-check.py` 实现规范 §8 L1-L9 九项检查（doc_id 查重/格式、version、时间戳、命名、slug 禁词、冻结检测、amends 引用、三套编号不混用），向前生效口径（§9：created_at/文件名日期 ≥ 2026-08-23 严格判级，存量既往不咎仅 info）；conveyor_probe 登记口挂接 doc_id 查重（撞号当场拒绝登记）。

**交付物**（改动文件清单）：
1. `kdo-tools/file-flow-check.py`（新建）：L1-L9 检查器 + `--snapshot` 冻结基线 + `--json` 输出 + `find_duplicate_doc_ids(diag_dir)` 可注入查重（登记口复用）
2. `kdo-tools/tests/test_file_flow_check.py`（新建）：17 用例（L1-L9 正反 + 向前生效 + 冻结基线 + amends 注释剥离）
3. `kdo-tools/conveyor_probe.py`：`_reject_duplicate_doc_ids` 挂接（复用 find_duplicate_doc_ids 单一真相源；撞号剔除+stderr 报警；模块加载失败降级不阻断登记）
4. `kdo-tools/tests/test_conveyor_probe.py`：挂接 2 用例（撞号全拒/唯一放行）
5. `90_control/frozen-registry.json`：冻结基线快照（首次建立，7 个冻结文件）

**验证**（命令+输出）：
- L1 单测：`pytest tests/`（kdo-tools）→ **47 passed**（file_flow_check 17 + conveyor_probe 含挂接用例 + 既有全部）
- L2 狗粮：①真实库首跑——216 文件 error=0 warning=52（**今日新件缺 version/updated_at 真实合规缺口**，检查器价值实证）info=88（存量按向前生效仅提示）；②L9 报出 **9 条任务单含 doc_id 真实违规**（E045，处置归编排）；③L8 误报消除（amends 带注释值剥离 D-编号前缀比对）；④冻结基线建立后 L7 正常（基线 7 文件，改动即报 error）；⑤`conveyor_probe --dry-run` 真实库冒烟——零登记零拒绝零崩溃
- L3 待活体：下次真实建议书落盘+探针登记走通查重（撞号拒绝实测）；规范生效后首个订正件 amends 链走通

**未做项**：
- `kdo lint` 集成未做——当前为独立 `python kdo-tools/file-flow-check.py`（任务书二选一，选了独立命令；kdo lint 集成可后续挂）
- wiki 卡侧 L9（30_wiki frontmatter 含 #队列号）未扫——扫描面 2000+ 卡成本高，当前只查任务单侧（规范 L9 两半之一），wiki 侧待立项
- 任务单含 doc_id 的 9 条**只报不修**——处置归王语嫣编排（规范 §2 任务单沿用 #队列号，编排侧编号实践需对齐）

**需要谁动作**：
- 王语嫣：①处置 9 条任务单 doc_id 违规（对齐规范 E045 口径或修订规范）②新建议书登记注意 doc_id 唯一（撞号会被探针当场拒绝）
- 欧阳锋：终审本单（抽「L1-L9 实现对照规范 §8/冻结检测正反/登记口挂接」）
