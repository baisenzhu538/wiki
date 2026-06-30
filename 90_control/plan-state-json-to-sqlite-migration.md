---
id: plan-state-json-to-sqlite-migration
title: "KDO state.json → SQLite 迁移实施规划"
type: improvement-plan
status: draft
author: 王语嫣
target_reviewer: 黄药师 + 欧阳锋
created_at: 2026-06-29
updated_at: 2026-06-29
domain:
  - kdo
  - infrastructure
  - scalability
source_refs:
  - kdo-workspace.py-load-save-state
  - kdo-state.json-structure-audit-2026-06-29
  - kdo-scalability-roadmap-10k-cards
related:
  - [[kdo-scalability-roadmap-10k-cards]]
  - [[kdo-system-manual]]
  - [[kdo-industrialization-manual]]
  - [[plan-kdo-infrastructure-disaster-prevention]]
---

# KDO state.json → SQLite 迁移实施规划

> **目标**：把 `.kdo/state.json` 从 JSON 文件迁移到 SQLite，解决 `kdo enrich`、`pre-submit`、`freeze` 中的多次线性查找问题，为多 Agent 并发读写提供事务支持。
>
> **关键设计**：通过 `workspace.py` 中的 `load_state()` / `save_state()` 作为唯一抽象点，保持所有现有 `state.get("sources", [])` 代码不变。

---

## 一、为什么这是架构上收益最高的改动

### 1.1 当前痛点

当前 `state.json` 是一个 1.8 MB 的 JSON 文件，包含 17 个顶层集合（sources、artifacts、feedback、tasks 等）。每次调用 `load_state()` 都要把整个文件读入内存，每次 `save_state()` 都要把整个文件写回磁盘。

实测调用点：KDO 代码库中 **272 处**引用了 `state.json` 或 `load_state`/`save_state`。

高频慢路径：

| 调用场景 | 当前复杂度 | 问题 |
|:---|:---|:---|
| `kdo enrich --all` | O(enriched × sources) | 对每张需要 enrich 的卡，线性扫描 `state["sources"]` 找原始素材 |
| pre-submit 外链检查 | O(links × wiki_files) | 每个 wikilink 重新 `rglob("30_wiki/*.md")` |
| freeze verify | O(cards × deps × cards) | 嵌套扫描 wiki 目录 |
| dashboard 启动 | O(state_size) | 每次启动都全量加载 state.json |
| 多 Agent 并发 | 无锁，易 corrupt | 同时写 state.json 会丢失数据 |

### 1.2 SQLite 迁移后的收益

| 收益 | 说明 |
|:---|:---|
| **查找从 O(n) 变 O(log n) 或 O(1)** | `SELECT * FROM sources WHERE id = ?` 替代线性扫描 |
| **只读写需要的记录** | 不用每次 load/save 整个 1.8MB JSON |
| **事务支持** | 多 Agent 并发写由 SQLite WAL 模式处理 |
| **索引支持** | 给 `source_id`、`wiki_path`、`artifact_id` 建索引 |
| **查询能力** | 可用 SQL 做聚合、过滤、join，替代 Python 循环 |
| **10k 卡基础** | state.json 到 10k 卡时会到 8MB+，SQLite 不会线性膨胀 |

---

## 二、当前 state.json 结构分析

基于 `.kdo/state.json` 实测（2026-06-29）：

| 顶层键 | 类型 | 当前数量 | 主要字段 |
|:---|:---|---:|:---|
| `version` | int | 1 | 状态文件版本 |
| `sources` | list | 689 | id, title, type, location, trust_level, ingested_at |
| `artifacts` | list | 34 | artifact_id, type, subtype, title, status, path |
| `deliveries` | list | 7 | delivery_id, artifact_id, path, status |
| `feedback` | list | 2,852 | feedback_id, kind, title, path, status |
| `projects` | list | 1 | project_id, name, goal, status |
| `tasks` | list | 14 | task_id, title, project_id, status |
| `connectors` | list | 0 | — |
| `improvement_plans` | list | 8 | plan_id, path, status |
| `briefs` | list | 4 | brief_id, title, topic, path |
| `eval_runs` | list | 0 | — |
| `ingested_inbox_files` | list | 500 | 字符串路径 |
| `wiki_snapshots` | dict | 0 | — |
| `revisions` | list | 2 | revision_id, wiki_page, page_title, diff_hash |
| `artifacts_count` | int | 27 | 计数 |
| `gate_overrides` | list | 1 | stage, reason, timestamp |
| `enrich_evidence` | list | 336 | evidence_id, wiki_path, method, result |

**关键观察**：
- 所有集合都是**同构记录列表**，天然适合关系表。
- 部分字段（如 feedback、evidence）可能包含嵌套 dict，需要 JSON 列存储。
- `version` 和 `artifacts_count` 是标量，可放 `kdo_meta` 表。

---

## 三、兼容性层设计（核心）

### 3.1 设计原则

**不要改 272 处调用代码**。改一处抽象层：`kdo/workspace.py` 中的 `load_state()` 和 `save_state()`。

方案：**SQLite-backed dict-like facade**。

```python
class SQLiteState:
    """Behaves like the old dict[str, Any] state, but backed by SQLite."""

    def __init__(self, db_path: Path):
        self._db = sqlite3.connect(db_path, check_same_thread=False)
        self._db.execute("PRAGMA journal_mode=WAL")
        self._db.execute("PRAGMA synchronous=NORMAL")
        self._db.row_factory = sqlite3.Row
        self._write_lock = threading.Lock()
        self._ensure_tables()

    def get(self, key: str, default=None):
        if key in SCALAR_KEYS:
            return self._get_scalar(key, default)
        return SQLiteCollection(self._db, key)  # list-like

    def __getitem__(self, key: str):
        return self.get(key)

    def __setitem__(self, key: str, value):
        if key in SCALAR_KEYS:
            self._set_scalar(key, value)
        else:
            self._replace_collection(key, value)
```

### 3.2 列表集合的延迟加载

`state.get("sources", [])` 返回一个 `SQLiteCollection`，它：
- 支持 `for source in state.get("sources", [])`（迭代时按需查询）
- 支持 `len(state.get("sources", []))`
- 支持按 id 快速查找：`collection.by_id("src_xxx")`
- **写操作（append、update）立即写入数据库**（受 `_write_lock` 保护），不等待 `save_state()`

这样现有代码几乎不用改：

```python
# 旧代码，继续可用
for source in state.get("sources", []):
    if source["id"] == target_id:
        ...

# 优化后的新代码，可用 but 非必须
source = state["sources"].by_id(target_id)
```

### 3.3 save_state 语义重新定义

黄药师关键补充：SQLite 下 `save_state()` 不再是“全量序列化写文件”，而是“确认持久化 / WAL checkpoint”。

```python
def save_state(root: Path, state: SQLiteState | dict) -> None:
    if isinstance(state, SQLiteState):
        # 写操作已在 append()/update() 时落库；
        # save_state 只做 WAL checkpoint 或 no-op。
        state.checkpoint()
    else:
        # fallback：兼容旧路径/测试
        _legacy_save_state_json(root, state)
```

对应集合操作语义：

| 操作 | JSON 行为 | SQLite 行为 |
|:---|:---|:---|
| `state["sources"].append(record)` | 追加到内存 list | 立即 `INSERT INTO kdo_records` |
| `state["sources"].update(record)` | 修改内存 list | 立即 `UPDATE kdo_records` |
| `save_state(root, state)` | 把整个 dict 写回文件 | WAL checkpoint / no-op |

对调用方透明，但避免“内存累积后 save 失败丢一批数据”的风险。

---

## 四、SQLite Schema 设计

### 4.1 表结构

```sql
-- 元数据标量
CREATE TABLE kdo_meta (
    key TEXT PRIMARY KEY,
    value_json TEXT NOT NULL
);

-- 记录型集合的统一表
CREATE TABLE kdo_records (
    collection TEXT NOT NULL,      -- 'sources' | 'artifacts' | 'feedback' | ...
    record_id TEXT NOT NULL,       -- id / artifact_id / feedback_id / ...
    data_json TEXT NOT NULL,       -- 整条记录序列化为 JSON
    updated_at TEXT NOT NULL,
    PRIMARY KEY (collection, record_id)
);

-- 用于线性遍历时的顺序
CREATE INDEX idx_records_collection ON kdo_records(collection);

-- 常用查询索引
CREATE INDEX idx_records_id ON kdo_records(record_id);

-- ingested_inbox_files 这类简单列表
CREATE TABLE kdo_strings (
    collection TEXT NOT NULL,
    value TEXT NOT NULL,
    inserted_at TEXT NOT NULL,
    PRIMARY KEY (collection, value)
);
```

### 4.2 为什么不一张表一个集合？

考虑过的方案：

| 方案 | 优点 | 缺点 |
|:---|:---|:---|
| **统一表（推荐）** | 迁移简单；新增集合无需改 schema；兼容动态字段 | 无法对单个字段建强类型索引 |
| **每集合一张表** | 字段类型清晰；可单独优化 | 需要 15+ 张表；schema 变更成本高；需要生成模型 |
| **JSON1 扩展 + 虚拟表** | 可对 JSON 字段建索引 | SQLite 版本依赖；复杂度更高 |

**推荐统一表 + JSON 列**，因为：
1. KDO 的集合字段不稳定，经常新增字段。
2. 迁移成本最低，不需要为每个集合写 DDL。
3. 常用查询通过 `record_id` 索引已经够快。
4. 如果需要对某个字段频繁查询，可后续加专门索引或拆出列。

---

## 五、迁移策略（零停机 + 可回滚）

### 5.1 步骤

```
1. 备份 .kdo/state.json → .kdo/state.json.bak.YYYYMMDD
2. 新增 workspace.py 实现 SQLiteState 类
3. load_state() 检测：
   - 若 .kdo/state.sqlite 存在 → 加载 SQLite
   - 否则读取 state.json → 自动迁移 → 生成 state.sqlite
     → 重命名 state.json → state.json.migrated
4. 所有命令继续通过 load_state()/save_state() 工作
5. 观察 1–2 周，确认稳定后删除 state.json.migrated
```

### 5.2 回滚方案

- 保留 `state.json.migrated` 一周。
- 若发现问题，可通过环境变量 `KDO_STATE_BACKEND=json` 强制使用旧 JSON。
- 或提供命令 `kdo migrate --rollback-state` 从 SQLite 导出回 JSON。

### 5.3 双写过渡期（不做）

黄药师评审结论：**双写是过度防御，不做**。

理由：
- 增加 `save_state` 复杂度（两次写入，失败处理更麻烦）
- `state.json.migrated` 备份已经是安全网
- 环境变量 `KDO_STATE_BACKEND=json` 回退已经足够

最终方案：**单写 + 备份 + 回退命令**。

---

## 六、代码变更清单

### 6.1 必须改

| 文件 | 改动 | 说明 |
|:---|:---|:---|
| `kdo/workspace.py` | 新增 `SQLiteState`、`SQLiteCollection` | 核心抽象层 |
| `kdo/workspace.py` | 修改 `load_state()` | 自动检测并迁移 |
| `kdo/workspace.py` | 修改 `save_state()` | 写入 SQLite |
| `kdo/cli.py` | 新增 `kdo migrate state` 命令 | 手动触发/回滚 |

### 6.2 建议改（收益最大化）

| 文件 | 改动 | 收益 |
|:---|:---|:---|
| `kdo/commands/curation.py` | `enrich` 时用 `state["sources"].by_id(...)` | 把 O(n) 查找变 O(1) |
| `kdo/commands/system.py` | lint 时从 SQLite 读取源注册信息 | 减少 JSON 解析 |
| `kdo/commands/delivery.py` | 查询 artifact 时用索引 | 加速 graph query 前置查找 |
| `kdo/dashboard.py` | dashboard 统计用 SQL 聚合 | 启动更快 |

### 6.3 不要改（保持兼容）

- 272 处 `state.get(...)` / `state[...]` 调用**暂时不动**，通过 facade 兼容。
- 所有现有测试**不应失败**。

---

## 七、性能预期（需实测验证）

> 以下数字为方向性估算，MVP 阶段必须跑实际 benchmark——`time kdo enrich --all --dry-run` 迁移前后对比。

| 操作 | 当前 (JSON) | 迁移后 (SQLite) | 备注 |
|:---|---:|---:|:---|
| `load_state()` 首次 | ~50ms | ~10ms + 首次连接 | 连接可复用 |
| `state["sources"].by_id()` | O(n) ~0.5ms@689 | O(log n) ~0.05ms | 10k 时差距更大 |
| `save_state()` 小更新 | ~80ms 写 1.8MB | ~5ms 写单条 | 最大收益（估算） |
| `enrich --all` source 查找 | 主导耗时之一 | 下降 5–10x | 取决于 enriched 数量（估算） |
| dashboard 启动 | 需全量解析 | 按需查询 | 感知明显 |

---

## 八、测试计划

### 8.1 单元测试

- `tests/test_workspace_state.py` 新增：
  - JSON → SQLite 自动迁移正确性
  - SQLiteState dict-like 行为兼容性
  - 并发写不丢失数据
  - 回滚 JSON 一致

### 8.2 集成测试

- 在副本 wiki 上运行：
  - `kdo lint --summary`
  - `kdo enrich --all --regex`
  - `kdo graph rebuild`
  - `kdo pre-submit` 多张卡
  - `kdo dashboard`

### 8.3 性能基准

- 记录迁移前后的 `time kdo enrich --all`。
- 目标：source 查找阶段耗时下降 ≥50%。

---

## 九、风险与缓解

| 风险 | 缓解 |
|:---|:---|
| SQLite 文件损坏 | 启用 WAL 模式；保留 JSON 备份；定期 `.backup` |
| 多线程访问冲突 | WAL 模式 + 单连接池 + 写操作加 `threading.Lock` |
| 迁移后数据不一致 | 迁移后校验 `count(*)` 与 JSON 记录数一致 |
| 某些代码直接读 `.kdo/state.json` | 搜索所有直接路径引用，改为 `load_state()` |
| Python 环境缺少 sqlite3 | Python 标准库自带，无需额外依赖 |

---

## 十、实施优先级与分工（黄药师拍板版）

### 本周做

| # | 工作 | 负责人 | 预计时间 |
|:---:|:---|:---|:---:|
| 1 | 实现 SQLiteState + SQLiteCollection（**只支持 sources 集合**） | 黄药师 | 2–3 天 |
| 2 | `load_state()` 自动检测 + 迁移 | 黄药师 | 1 天 |
| 3 | 跑 `enrich` benchmark 实测性能提升 | 黄药师 | 0.5 天 |

### 下周做

| # | 工作 | 负责人 | 预计时间 |
|:---:|:---|:---|:---:|
| 4 | 扩展其余 16 个集合到 SQLite | 黄药师 | 2–3 天 |
| 5 | 实现 `kdo migrate state --rollback` | 黄药师 | 1 天 |
| 6 | 集成测试 + 并发安全测试 | 黄药师 | 1–2 天 |

### 不做

- ❌ 双写过渡期（过度防御）
- ❌ `check_same_thread=False` 绕过（改用 WAL + Lock）

---

## 十一、验收标准

1. `kdo lint --summary` 在迁移后无新增 ERROR/WARNING。
2. 迁移后 `.kdo/state.sqlite` 存在，`.kdo/state.json` 被重命名为 `.kdo/state.json.migrated`。
3. `kdo enrich --all` 耗时较迁移前下降 ≥30%。
4. 并发运行两个 `kdo` 命令不导致 state 数据丢失或 corrupt。
5. 所有现有测试通过。
6. 提供 `kdo migrate state --rollback` 可回滚到 JSON。

---

## 十二、最小可启动版本（MVP）

如果资源有限，先做这三件事：

1. **只迁移 `sources` 表**（689 条，enrich 最常用），其余集合继续走 JSON。
2. **保持 `load_state()` 返回 dict 兼容对象**，不改任何调用方。
3. **双写一周**：SQLite 主写，JSON 影子写。

这样风险最低，同时解决 enrich 的最大痛点。

---

**关联文档**：
- [[kdo-scalability-roadmap-10k-cards]]
- [[kdo-system-manual]]
- [[plan-kdo-infrastructure-disaster-prevention]]
