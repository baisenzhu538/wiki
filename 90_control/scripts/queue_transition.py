"""Hard state transition enforcer for the KDO production queue.

All queue status changes MUST go through this script. Manual edits to
`production-queue.md` or task file `status` fields are forbidden.

Usage:
    python queue_transition.py claim <task-id> --instance <name> [--force] [--no-commit]
    python queue_transition.py complete <task-id> --instance <name> [--evidence <path>] [--force --reason '<理由>'] [--no-commit]
    python queue_transition.py release <task-id> --instance <name> [--no-commit]
    python queue_transition.py review <task-id> --verdict pass|fail --reviewer 欧阳锋 [--grade A|A-|B+|B|B-|C] [--no-commit]

Exit codes:
    0 = transition applied
    1 = transition rejected / error

--force claim: 跳过队列前方 pending_review 阻塞（用于不同 assignee 的并行任务）
--force complete: 允许从 queued 直接跳到 pending_review
        （用于生产已完成但未通过脚本领取的场景；#444 起必须配 --reason，例外入台账 90_control/force-exceptions.log）
--no-commit: 跳过流转后的自动 git 收口（#390 逃生门，特殊场景手工控制）

#390：流转成功后自动 commit 本次触碰的文件（任务单+队列+dashboard），
让"状态变更"与"入档"原子化——跨 checkout 协作者任何时候读到的都是最新状态。
红线：path-scoped add，严禁 add -A/.（工作区永远有其他 agent 的在制品）。
git 失败不阻断流转：stderr 醒目报警 + 写 90_control/pending-git-commits.log 待收口。
"""

from __future__ import annotations

import os
import re
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

# Ensure UTF-8 stdout to avoid UnicodeEncodeError on Windows Git Bash
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # #568：补 errors=replace（GBK 遇不可映射字符也不炸）
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Make queue_gate importable from the same directory
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from queue_gate import QUEUE_PATH, can_claim, find_task, parse_queue
from queue_lock import QueueLock

# 看板自动刷新
import importlib.util
_dash_spec = importlib.util.spec_from_file_location(
    "generate_dashboard",
    str(Path(__file__).resolve().parent.parent.parent / "kdo-tools" / "generate-dashboard.py")
)
_gen_dash = importlib.util.module_from_spec(_dash_spec)
_dash_spec.loader.exec_module(_gen_dash)


def _refresh_dashboard():
    """队列变更后自动刷新 dashboard.html。"""
    try:
        _gen_dash.main()
    except Exception:
        pass  # 看板刷新失败不阻塞队列操作

# #389 REVIEW-PENDING 待终审自动登记段（与 INBOX-PENDING 对称；纯日志视图，不动状态机语义）
REVIEW_BEGIN = "<!-- REVIEW-PENDING-BEGIN（queue_transition 自动维护，勿手改） -->"
REVIEW_END = "<!-- REVIEW-PENDING-END -->"
_WIKI_ROOT = Path(__file__).resolve().parent.parent.parent


def _review_board_update(register: dict | None = None, strike: str | None = None,
                         strike_note: str = "") -> None:
    """维护 production-queue.md 的 REVIEW-PENDING 段（#389）。

    - register: {"seq","task_id","assignee","task_file"} → 追加登记行（task_id 级幂等；
      行被手删时下次 complete 会重新登记 = 自纠正）
    - strike: task_id → 对应行划掉并附终审注记
    段不存在则创建（插到 INBOX-PENDING 段前，无则追加文件尾）。
    列表行（非表格行），parse_queue 不会误读。失败不阻断流转，但打印警告让异常可见。
    """
    try:
        if not QUEUE_PATH.exists():
            return
        text = QUEUE_PATH.read_text(encoding="utf-8")
        now = datetime.now().strftime("%m-%d %H:%M")

        items: list[str] = []
        if REVIEW_BEGIN in text and REVIEW_END in text:
            block = text.split(REVIEW_BEGIN)[1].split(REVIEW_END)[0]
            items = [l for l in block.splitlines() if l.startswith("- ")]

        if register:
            tid = register["task_id"]
            # O-3 分批提审修复：幂等判断排除已划掉的行——分批任务二次 complete 时
            # REVIEW-PENDING 段已有该任务的划掉行（含 tid），若不排除则不再登记 = 提审无声
            if not any(tid in l and not l.startswith("- ~~") for l in items):
                items.append(
                    f"- #{register['seq']} {tid}｜{register['assignee']}｜提审 {now}｜{register['task_file']}"
                )
        if strike:
            for i, line in enumerate(items):
                if strike in line and not line.startswith("- ~~"):
                    items[i] = f"- ~~{line[2:]}~~{strike_note}"
        if not register and not strike:
            return

        board = [
            REVIEW_BEGIN, "",
            "## ⚖️ 待终审（提审任务，queue_transition 自动登记）", "",
            "> 欧阳锋开工只看这段：有行就审，终审后自动划掉。历史任务不回填（#389，只向前生效）。",
            "",
        ] + items + ["", REVIEW_END]

        if REVIEW_BEGIN in text:
            new_text = text.split(REVIEW_BEGIN)[0] + "\n".join(board) + text.split(REVIEW_END)[1]
        else:
            inbox_marker = "<!-- INBOX-PENDING-BEGIN"
            if inbox_marker in text:
                new_text = text.replace(inbox_marker, "\n".join(board) + "\n\n" + inbox_marker, 1)
            else:
                new_text = text.rstrip() + "\n\n" + "\n".join(board) + "\n"
        QUEUE_PATH.write_text(new_text, encoding="utf-8")
    except Exception as e:
        print(f"⚠️ REVIEW-PENDING 登记失败（不阻断流转）: {e}", file=sys.stderr)


# #390 流转自带 git 收口：流转成功后自动 commit 本次触碰的文件
DASHBOARD_PATH = _WIKI_ROOT / "70_product" / "tasks" / "dashboard.html"
PENDING_COMMIT_LOG = _WIKI_ROOT / "90_control" / "pending-git-commits.log"


# #460 层 2：门禁拦截自动落盘（机器自报——agent 不报也能上浮给王语嫣）
GATE_BLOCKED_LOG = _WIKI_ROOT / "90_control" / "gate-blocked.log"
GATE_BLOCKED_TEST_LOG = _WIKI_ROOT / "90_control" / "gate-blocked-test.log"  # #483：测试件独立日志（task_9999_*，防第五探针误报）


# F-036 问题落点判定在 queue_gate（共享真相源——门禁+探针第七信号同用，禁副本）
from queue_gate import check_issue_disposition as _check_issue_disposition  # noqa: E402


def _capsule_event(agent: str, event: str, payload: str) -> None:
    """#511：胶囊事件层统一写入钩（queue_transition 侧单写入面）。

    懒加载 memory_capsule.log_event_safe（失败可见不静默、不阻断流转主流程——
    #434 同款口径）。本函数自身也不再吞错：log_event_safe 内部已报警+落待收口。
    """
    try:
        sys.path.insert(0, str(_WIKI_ROOT / "kdo-tools"))
        import memory_capsule as mc
        mc.log_event_safe(agent, event, payload)
    except Exception as e:
        print(f"⛔ 胶囊事件钩异常（流转/台账已成功，不阻断）：agent={agent} event={event}: {e}",
              file=sys.stderr)


def _log_gate_blocked(task_id: str, gate: str, reason: str, instance: str = "") -> None:
    """每次门禁拦截自动 append 一行（时间/任务/门禁名/原因/instance）——探针第五探针扫描面。

    #483：测试件（task_9999_*）走独立 gate-blocked-test.log——记录保留（E028 测试覆盖
    历史），但不进真实日志，防第五探针把测试噪声当真实拦截通知王语嫣。
    #511：真实拦截同步写胶囊事件层（event_type=error；测试件不写——同 #483 噪声分流纪律）。
    """
    try:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        target = GATE_BLOCKED_TEST_LOG if task_id.startswith("task_9999_") else GATE_BLOCKED_LOG
        with target.open("a", encoding="utf-8") as f:
            f.write(f"{ts}｜{task_id}｜{gate}｜{reason[:100]}｜{instance}\n")
        if not task_id.startswith("task_9999_"):
            _capsule_event(instance or "unknown", "error",
                           f"gate-blocked;task={task_id};gate={gate};reason={reason[:200]}")
    except Exception:
        pass


def _record_commit_failure(task_id: str, action: str, reason: str) -> None:
    """git 收口失败 → 追加待收口清单（90_control/pending-git-commits.log）。

    巡检/下轮可据此兜住"流转成功但未入 git"的窗口。清单写入本身失败不再上抛。
    """
    try:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with PENDING_COMMIT_LOG.open("a", encoding="utf-8") as f:
            f.write(f"{ts}\t{action}\t{task_id}\t{reason}\n")
    except Exception:
        pass


def _git_commit_transition(task_id: str, action: str, actor: str) -> None:
    """#390：流转成功后把本次触碰的文件 commit 入 git（path-scoped，禁 add -A）。

    触碰集 = 任务单 + production-queue.md + dashboard.html。
    - 仓外文件（KDO_* 环境变量沙盒测试）自动跳过；无未提交变更时静默返回
    - git 任何失败：stderr 醒目报警 + 待收口清单记录，不阻断已成功的流转
    - `git commit -- <paths>` 部分提交语义：别人已 staged 的在制品不被裹挟
    """
    try:
        if not (_WIKI_ROOT / ".git").exists():
            return
        files = [QUEUE_PATH, DASHBOARD_PATH]
        task_file = _find_task_file_dual(task_id)
        if task_file is not None:
            files.append(task_file)
            # #402：workspace 目录随流转 commit 入档（与 #390 收口兼容）
            ws = task_file.parent / f"{task_file.stem}-workspace"
            if ws.exists():
                files.extend(p for p in ws.rglob("*") if p.is_file())
        rels: list[str] = []
        for f in files:
            try:
                rel = str(Path(f).resolve().relative_to(_WIKI_ROOT)).replace("\\", "/")
            except (ValueError, OSError):
                continue  # 沙盒/多环境指向仓外 → 不属于本仓提交范围
            if rel not in rels:
                rels.append(rel)
        if not rels:
            return
        status = subprocess.run(
            ["git", "-C", str(_WIKI_ROOT), "status", "--porcelain", "--", *rels],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=15,  # #568：GBK 控制台不指定 encoding 即炸
        ).stdout
        if not status.strip():
            return  # 触碰文件均无未提交变更（如重复流转/手工已收口）
        subprocess.run(
            ["git", "-C", str(_WIKI_ROOT), "add", "--", *rels],
            check=True, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=15,  # #568：GBK 控制台不指定 encoding 即炸
        )
        rows = parse_queue()
        task = find_task(task_id, rows)
        ref = f"#{task['seq']}" if task else task_id
        subprocess.run(
            ["git", "-C", str(_WIKI_ROOT), "commit", "-m",
             f"chore(queue): {ref} {action} by {actor}", "--", *rels],
            check=True, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=15,  # #568：GBK 控制台不指定 encoding 即炸
        )
    except Exception as e:
        print(
            f"🚨 [GIT-COMMIT-FAILED] {task_id} {action} 流转已成功但自动 commit 失败: {e}"
            f" —— 已记入 {PENDING_COMMIT_LOG.name} 待收口清单，请手工收口",
            file=sys.stderr,
        )
        _record_commit_failure(task_id, action, str(e))

# KDO_TASK_DIR / KDO_BATCH_DIR 环境变量允许测试/多环境指向替代目录
TASK_DIR = Path(
    os.environ.get("KDO_TASK_DIR")
    or (Path(__file__).resolve().parent.parent.parent / "60_feedback" / "tasks")
)
BATCH_DIR = Path(
    os.environ.get("KDO_BATCH_DIR")
    or (Path(__file__).resolve().parent.parent.parent / "70_product" / "tasks")
)

# Valid transitions. Format: (current_status, action) -> new_status
# instance/reviewer checks are performed separately.
TRANSITIONS: dict[tuple[str, str], str] = {
    ("queued", "claim"): "claimed-{instance}",
    ("claimed-{instance}", "complete"): "pending_review",
    ("claimed-{instance}", "release"): "claimed-{instance}",
    ("pending_review", "review_pass"): "reviewed",
    ("pending_review", "review_fail"): "queued",
    # #429 F-029：等待外部输入态——不占 pending_review 阻塞位（find_blockers 只收 pending_review/claimed）
    ("pending_review", "mark_waiting"): "waiting-external",
    ("waiting-external", "resume"): "pending_review",
    # #461：queued 单取消/被取代（终态，非删除——charter §3.15 上板冻结的出口）
    ("queued", "cancel"): "cancelled",
}


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    """Return (frontmatter_dict, body)."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---"):
        return {}, text
    # Match leading frontmatter block: ---\n<yaml>\n---\n<body>
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", text, re.DOTALL)
    if not match:
        return {}, text
    fm_text, body = match.group(1), match.group(2)
    if yaml is None:
        raise RuntimeError("PyYAML is required to parse frontmatter")
    data = yaml.safe_load(fm_text) or {}
    return data, body


def write_frontmatter(path: Path, fm: dict[str, Any], body: str) -> None:
    """Write file with YAML frontmatter, preserving body."""
    if yaml is None:
        raise RuntimeError("PyYAML is required to write frontmatter")
    fm_text = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, default_flow_style=False)
    path.write_text(f"---\n{fm_text}---\n{body}", encoding="utf-8")


def find_task_file(task_id: str) -> Path | None:
    """Locate task file by exact filename match.

    Searches only by filename in known task directories.  If the filename
    does not match the task id (e.g. queue has one id but the file was
    renamed), the caller should fall back to
    ``find_task_file_by_frontmatter_id()`` which scans frontmatter.
    """
    candidates = [
        TASK_DIR / f"{task_id}.md",
        BATCH_DIR / f"{task_id}.md",
    ]
    for c in candidates:
        if c.exists():
            return c
    return None


def find_task_file_by_frontmatter_id(task_id: str) -> Path | None:
    """Locate task file whose frontmatter ``id`` field equals *task_id*.

    Scans all ``.md`` files in the task directories.  Used as a fallback
    when the filename does not match the queue id.
    """
    for d in (TASK_DIR, BATCH_DIR):
        if not d.exists():
            continue
        for path in d.glob("*.md"):
            fm, _ = parse_frontmatter(path)
            if fm.get("id") == task_id or str(fm.get("task_id", "")) == task_id:
                return path
    return None


def _find_task_file_dual(task_id: str) -> Path | None:
    """Find task file: filename first, then frontmatter id fallback."""
    return find_task_file(task_id) or find_task_file_by_frontmatter_id(task_id)


def update_queue_status(task_id: str, new_status: str) -> None:
    """Atomically update the status cell in production-queue.md."""
    text = QUEUE_PATH.read_text(encoding="utf-8")
    lines = text.splitlines()
    updated = []
    tid = task_id.strip("`").strip("*")
    found = False
    for line in lines:
        if line.startswith("|") and not set(line.strip()) <= {"|", "-", ":", " "}:
            cells = [c for c in line.strip("|").split("|")]
            if len(cells) >= 4 and cells[1].strip().strip("*").strip("`").strip() == tid:
                # Replace only the 4th cell (status), preserving surrounding formatting
                cells[3] = f" {new_status} "
                updated.append("|" + "|".join(cells) + "|")
                found = True
                continue
        updated.append(line)
    if not found:
        raise ValueError(f"任务 {task_id} 未在生产队列中找到")
    QUEUE_PATH.write_text("\n".join(updated) + "\n", encoding="utf-8")


def update_task_frontmatter(task_file: Path, **updates: Any) -> None:
    """Update task file frontmatter keys."""
    fm, body = parse_frontmatter(task_file)
    for key, value in updates.items():
        if value is not None:
            fm[key] = value
    fm["updated_at"] = datetime.now(timezone.utc).isoformat()
    write_frontmatter(task_file, fm, body)


def current_utc_date() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def backup(path: Path) -> str:
    """Return current file content for rollback."""
    return path.read_text(encoding="utf-8")


def restore(path: Path, content: str) -> None:
    """Restore file content on failure."""
    path.write_text(content, encoding="utf-8")


def apply_updates(task_id: str, new_queue_status: str, task_file: Path, **task_updates: Any) -> None:
    """Atomically update queue and task file; rollback both on failure."""
    queue_backup = backup(QUEUE_PATH)
    task_backup = backup(task_file)
    try:
        update_queue_status(task_id, new_queue_status)
        update_task_frontmatter(task_file, **task_updates)
    except Exception as e:
        restore(QUEUE_PATH, queue_backup)
        restore(task_file, task_backup)
        raise RuntimeError(f"状态更新失败，已自动回滚：{e}") from e


def ensure_task_workspace(task_id: str, task_file: Path) -> str | None:
    """#402：claim 长程任务（frontmatter `long_running: true`）时检查 workspace。

    不存在则创建最小三件套 `60_feedback/tasks/<task_id>-workspace/`：
    `in-progress/`（中间产物）、`excluded/`（已排除方向）、`next-pointer.md`（上次停在哪）。
    非长程任务返回 None。文件随 #390 自动 commit 触碰集入档。
    """
    import time
    fm, _ = parse_frontmatter(task_file)
    if not (fm and fm.get("long_running")):
        return None
    ws = task_file.parent / f"{task_file.stem}-workspace"
    rel = ws.relative_to(_WIKI_ROOT).as_posix() if ws.is_relative_to(_WIKI_ROOT) else str(ws)
    if ws.exists():
        return f"workspace 已存在: {rel}"
    (ws / "in-progress").mkdir(parents=True)
    (ws / "excluded").mkdir()
    (ws / "next-pointer.md").write_text(
        f"# {task_id} workspace\n\n"
        f"- 创建: {time.strftime('%Y-%m-%d %H:%M')}（claim 联动自动生成）\n"
        f"- 上次停在哪: 任务刚被领取\n"
        f"- 下一步: 读任务单 `{task_file.name}` 执行范围\n",
        encoding="utf-8",
    )
    return f"长程任务 workspace 已创建: {rel}"


# 处置类任务 claim 门禁（#375）：任务单含处置关键词时强制内容价值判断节。
# 背景：08-19 英文壳目录事件——"删除"选项进入执行链差点毁核心资产（PARA 库）。
# PROTOCOL §7 素材删除禁令是文案，这里落地为 claim 门禁。
DISPOSAL_KEYWORDS = ("删除", "清理", "归档", "废弃", "处置", "移除", "删除类")


def _extract_action_scope(body: str) -> str:
    """#457 方案 1（辅）：只提取「## 动作」节 + 「## 任务目标」节（不含全 body）——正文叙述不触发关键词。"""
    scope = []
    for sec in ("## 动作", "## 任务目标"):
        idx = body.find(sec)
        if idx == -1:
            continue
        nxt = body.find("\n## ", idx + 1)
        scope.append(body[idx:nxt] if nxt > 0 else body[idx:])
    return "\n".join(scope)


def _check_disposal_gate(task_file: Path, fm: dict[str, Any], task_id: str) -> tuple[bool, str]:
    """处置类任务 claim 检查（#457 结构化重构：显式标记优先 + 关键词限定范围降级为提示）。

    - 显式标记 `disposal: true`（编排侧写任务单时标注）→ 硬门禁：必须带「内容价值判断」节
    - 关键词（只扫动作节+任务目标节）→ 降级为提示（不硬拦），引导补标记
    - 意图不变：PROTOCOL §7 素材删除禁令（逐件老朱亲批）；#189/#454 误判根治（术语词不误卡）
    """
    body = task_file.read_text(encoding="utf-8", errors="replace")
    title = str(fm.get("title") or task_file.stem)

    # 豁免声明：frontmatter claim_gate_exempt 写明理由
    if fm.get("claim_gate_exempt"):
        return True, f"（claim_gate_exempt 豁免：{fm['claim_gate_exempt']}）"

    has_value_judgement = "内容价值判断" in body

    # 1. 显式标记 → 硬门禁（方案 2，主）
    if fm.get("disposal") is True:
        if not has_value_judgement:
            # #460 FAIL 退回补插桩：处置硬门禁（最高风险防线）拦截必须落盘——否则拦截静默王语嫣无感
            _log_gate_blocked(task_id, "处置-硬门禁", "disposal:true 缺「内容价值判断」节（PROTOCOL §7）", task_id)
            return False, (
                f"处置类任务 {task_id}（frontmatter disposal: true）缺「内容价值判断」节——禁止领取。\n"
                f"背景：PROTOCOL §7 素材删除禁令（08-19 英文壳事件）。\n"
                f"请在任务单补充节：该任务涉及素材的内容价值判断（读过内容再定去向），"
                f"并声明删除须逐件老朱亲批。"
            )
        return True, (
            f"✅ {task_id} 已领取（处置类 disposal: true，已含内容价值判断节）。\n"
            f"执行前确认清单：\n"
            f"  ① 素材处置默认只有消化/归档原位保留，删除须逐件老朱亲批（PROTOCOL §7）\n"
            f"  ② 批量三问：dry-run 预览 / 变更范围声明 / 非空值不覆盖\n"
            f"  ③ 处置前通读内容（B5 牌：先读完整内容再下结论）"
        )

    # 2. 关键词（限定范围）→ 降级为提示，不硬拦（方案 1，辅——#189/#454 误判根治）
    scope = title + "\n" + _extract_action_scope(body)
    hits = [k for k in DISPOSAL_KEYWORDS if k in scope]
    if hits:
        return True, (
            f"⚠️ {task_id} 疑似处置未标记：动作/目标节命中 {hits}——如含素材处置动作，"
            f"请补 frontmatter `disposal: true` + 「内容价值判断」节（#457；PROTOCOL §7 删除须老朱亲批）"
        )
    return True, ""


# #444 instance→角色名映射：frontmatter assignee 只写角色名，instance 另存。
# 老顽童 Hermes CLI 实例映射 laowantong（#445：hermes=老顽童专属）；其余角色 instance 与角色名同形。
# #503 修正：kimi 是多角色共用实例（王语嫣/欧阳锋/老顽童均用 Kimi CLI，#445）——
# 按 instance 反推角色在 kimi 上是系统性错误（#497 claim 实测：王语嫣单被错写 laowantong），
# 已从映射移除。claim 写侧不再按 instance 反推覆盖 assignee（保持任务单/队列行原值）。
# 存量任务单 assignee=实例名不回改（读侧兼容，历史既往不咎）。
INSTANCE_ROLE_MAP = {"hermes": "laowantong"}


def _role_of(instance: str) -> str:
    return INSTANCE_ROLE_MAP.get(instance, instance)


# ── #546：实例身份登记 + 终审权机器校验（一具两职事件根治，#525 轻量先行版）──
# 登记表是纯本地 json（.kdo/active-instances.json），claim 时无感写入；
# review 校验「当前 cwd 有 ouyangfeng 角色登记实例」才放行 --reviewer 欧阳锋。
# 能力边界（诚实口径）：多实例共享 cwd 时只能证明「该工作目录有 ouyangfeng 上岗登记」，
# 会话级身份绑定（真·一具两职防控）属 #525 正单（心跳/会话绑定），本单不做。
INSTANCE_REGISTRY = _WIKI_ROOT / ".kdo" / "active-instances.json"


def _load_registry() -> dict:
    try:
        data = json.loads(INSTANCE_REGISTRY.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {"instances": {}}
    except Exception:
        return {"instances": {}}


def _save_registry(reg: dict) -> None:
    INSTANCE_REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    tmp = INSTANCE_REGISTRY.with_suffix(".tmp")
    tmp.write_text(json.dumps(reg, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(INSTANCE_REGISTRY)  # 原子替换防半写


def _register_instance(task_id: str, instance: str) -> None:
    """#546：claim/register 时登记/更新实例身份（角色/cwd/工具/会话/时间）。
    登记失败不阻断流转；测试件 task_9999_ 不登记（#483 噪声分流纪律）。"""
    if task_id.startswith("task_9999_"):
        return
    try:
        reg = _load_registry()
        reg.setdefault("instances", {})[instance] = {
            "role": _role_of(instance),
            "cwd": os.getcwd(),
            "tool": os.environ.get("KDO_TOOL", ""),
            "session": os.environ.get("KDO_SESSION_ID", ""),
            "ts": datetime.now().isoformat(timespec="seconds"),
        }
        _save_registry(reg)
    except Exception:
        pass


def _check_review_authority(task_id: str, reviewer: str,
                            force: bool = False, reason: str | None = None) -> tuple[bool, str]:
    """#546：终审权机器校验——当前 cwd 须有 role=ouyangfeng 的登记实例才放行。
    未登记/不符 → 拒止 + 提示 register；--force --reason 逃生门落 #444 台账。"""
    reg = _load_registry()
    cwd = os.path.normcase(os.path.normpath(os.getcwd()))
    for name, e in reg.get("instances", {}).items():
        role = e.get("role") or _role_of(name)
        entry_cwd = os.path.normcase(os.path.normpath(e.get("cwd", "") or "/"))
        if role == "ouyangfeng" and entry_cwd == cwd:
            return True, ""
    if force:
        if not (reason and reason.strip()):
            return False, "终审权校验 force 逃生必须配 --reason '<理由>'（#444：例外留痕——谁/为何/何时）"
        ledger = _log_force_exception(task_id, reviewer,
                                      f"终审权校验绕过：{reason.strip()}",
                                      bypass="#546 终审权校验")
        return True, f"⚠️ 终审权校验 force 例外已留痕: {ledger}"
    return False, (
        "终审权校验拒止（#546 一具两职根治）：当前工作目录无 ouyangfeng 角色登记实例。"
        "欧阳锋上岗先登记：python 90_control/scripts/queue_transition.py register ouyangfeng；"
        "紧急绕过：review 加 --force --reason '<理由>'（落 force-exceptions.log 台账）"
    )


def action_register(instance: str) -> tuple[bool, str]:
    """#546：实例上岗手动登记（claim 之外的登记入口——欧阳锋等纯审查角色不 claim）。"""
    _register_instance("manual-register", instance)
    e = _load_registry().get("instances", {}).get(instance, {})
    if not e:
        return False, f"登记失败（详见 stderr/权限）：{instance}"
    return True, (f"✅ 实例已登记: {instance}（role={e['role']} cwd={e['cwd']} ts={e['ts']}）\n"
                  f"   登记表: {INSTANCE_REGISTRY}")


def action_claim(task_id: str, instance: str, force: bool = False) -> tuple[bool, str]:
    """Claim a queued task for an instance.

    --force: 跳过 pending_review 阻塞检查（用于不同 assignee 的并行任务）。
    #504：--force 放行保留但留痕——绕过任何阻塞都写 force-exceptions.log 台账（例外不得无痕）。
    """
    rows = parse_queue()
    force_note = ""
    if force:
        # #504：显式放行仍可用（并行审批场景），但绕过即留痕（谁/何时/绕过哪条）
        would_ok, would_reason = can_claim(task_id, rows, instance)
        if not would_ok:
            ledger = _log_force_exception(task_id, instance, f"claim 绕过：{would_reason}",
                                          bypass="pending_review 阻塞（#504 审查等待期占位）")
            force_note = f"\n⚠️ force 例外已留痕: {ledger}"
    else:
        ok, reason = can_claim(task_id, rows, instance)
        if not ok:
            return False, reason

    task_file = _find_task_file_dual(task_id)
    if task_file is None:
        return False, f"找不到任务单文件: {task_id}（已按文件名和 frontmatter id 双重查找）"

    # #375 处置类门禁：缺内容价值判断节拒绝领取
    fm, _ = parse_frontmatter(task_file)
    gate_ok, gate_msg = _check_disposal_gate(task_file, fm, task_id)
    if not gate_ok:
        return False, gate_msg

    with QueueLock("production-queue"):
        # Re-check gate inside lock
        rows = parse_queue()
        if not force:
            ok, reason = can_claim(task_id, rows, instance)
            if not ok:
                return False, reason

        new_status = f"claimed-{instance}"
        # #444 frontmatter 口径：assignee=角色名（文档署名单一口径，E020/E045 同病根治）；
        # 实际执行实例另存 instance 字段。存量任务单 assignee=实例名（如 hermes）不回改——
        # 读侧兼容（REVIEW-PENDING 登记显示原值），历史既往不咎。
        # #503 口径修正：claim 不改 assignee（保持任务单/队列行原值）——kimi 是多角色共用
        # 实例，按 instance 反推角色必然错写（#497 实证：王语嫣单被覆盖成 laowantong）。
        # claim 只更新 status=in_progress + instance=<执行实例>。
        apply_updates(task_id, new_status, task_file,
                      instance=instance, status="in_progress")

    ws_note = ensure_task_workspace(task_id, task_file)
    if ws_note:
        gate_msg = f"{gate_msg}\n{ws_note}"

    _register_instance(task_id, instance)  # #546：claim 即上岗登记（无感）

    return True, f"✅ {task_id} 已领取为 {new_status}{force_note}\n{gate_msg}"


# 代码类任务提审门禁：任务单 frontmatter 声明 code_files（相对仓库根的路径列表，
# 支持跨仓：含 "Knowledge Delivery OS" 的路径归 KDO 源码仓，其余归 wiki 仓）。
# 未声明 code_files 的任务视为制卡/文档类，豁免（pre-submit 门禁已管）。
KDO_REPO_ROOT = Path(r"C:\Users\Administrator\Knowledge Delivery OS 0.0.1")


def _git_uncommitted(repo_root: Path, paths: list[str]) -> list[str]:
    """Return paths with uncommitted changes in the given repo.

    Empty on git errors (fail-open: 门禁不因 git 环境异常阻塞流转，但会提示）。
    """
    if not repo_root.exists() or not (repo_root / ".git").exists():
        return []
    try:
        out = subprocess.run(
            ["git", "-C", str(repo_root), "status", "--porcelain", "--", *paths],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=15,  # #568：GBK 控制台不指定 encoding 即炸
        ).stdout
    except Exception as e:
        # #568：fail-open 可见化——E040 脏改动检测被跳过必须留痕（静默=门禁致盲）
        print(f"[warn] E040 门禁组件 _git_dirty_paths 异常跳过（按无脏改动放行）: {e}", file=sys.stderr)
        return []
    dirty = []
    for line in out.splitlines():
        # porcelain line: "XY path" — strip the 2-char status column
        if len(line) >= 3 and line[2] == " ":
            path = line[3:]
        elif line.startswith("??"):
            path = line[3:]
        else:
            continue
        # 构建产物不算脏（#527 实证：__pycache__ 随 pytest 版本变脸，目录级 code_files 被噪声误拦）
        if "__pycache__" in path or path.endswith(".pyc"):
            continue
        dirty.append(path)
    return dirty


def _check_code_gate(task_file: Path, fm: dict[str, Any]) -> tuple[bool, str]:
    """Reject complete when declared code files have uncommitted changes."""
    code_files = fm.get("code_files") or []
    if isinstance(code_files, str):
        code_files = [code_files]
    if not code_files:
        return True, ""

    wiki_root = Path(__file__).resolve().parents[2]
    dirty_all: list[str] = []
    for cf in code_files:
        cf = str(cf)
        repo = KDO_REPO_ROOT if "Knowledge Delivery OS" in cf else wiki_root
        dirty = _git_uncommitted(repo, [cf])
        for d in dirty:
            dirty_all.append(f"{'KDO' if repo == KDO_REPO_ROOT else 'wiki'}: {d}")

    if dirty_all:
        return False, (
            "代码类任务提审门禁：以下改动文件尚未 commit，请先提交再流转\n"
            + "\n".join(f"  - {d}" for d in dirty_all)
        )
    return True, ""


# ---------------------------------------------------------------------------
# #522 complete 门禁：交付物已入仓校验（E040 机器兜底）
# ---------------------------------------------------------------------------

# 豁免声明关键词（任务单执行报告明确声明以下口径 → 跳过校验：编排/诊断类无代码交付物）
DELIVERABLE_EXEMPT_MARKERS = ("纯任务单修改", "纯任务单", "无代码交付物", "零代码改动")
# 自动收口文件不算交付物（complete 流转本身会 commit 它们）
_DELIVERABLE_AUTO_COMMIT = {"production-queue.md", "dashboard.html"}

# 交付物节内容里的反引号路径：含 / 且有扩展名才认（防命令/字段名误识别）
_DELIVERABLE_PATH_RE = re.compile(r"`([^`\n]+)`")


def _extract_deliverable_section(report: str) -> str:
    """提取执行报告「交付物」节文本（锚点=DELIVERY_FIELDS 改动文件清单三写法；
    节边界=下一粗体字段/## 标题）。无该节返回空串。"""
    for anchor in DELIVERY_FIELDS["改动文件清单"]:  # **交付物** / **改动文件** / **文件清单**
        idx = report.find(anchor)
        if idx == -1:
            continue
        rest = report[idx + len(anchor):]
        m_field = re.search(r"\n\s*(?:-\s*)?\*\*", rest)  # #569：`- **` 子弹行也算字段行起始（#551 节延展误吞实证）
        nxt_field = m_field.start() if m_field else -1
        nxt_head = rest.find("\n##")
        stops = [p for p in (nxt_field, nxt_head) if p > 0]
        return rest[:min(stops)] if stops else rest
    return ""


def _extract_deliverable_paths(report: str, task_file_name: str) -> list[str]:
    """从执行报告「交付物」节提取反引号包裹的文件路径（启发式，识别不出=返回空→WARNING 不硬拦）。"""
    section = _extract_deliverable_section(report)
    paths: list[str] = []
    if section:
        for tok in _DELIVERABLE_PATH_RE.findall(section):
            tok = tok.strip()
            if "/" not in tok and "\\" not in tok:
                continue
            if not re.search(r"\.[A-Za-z0-9]{1,10}$", tok):
                continue
            norm = tok.replace("\\", "/")
            # #515 判据 v1.1 校准点 1：`_tmp/` 划痕路径（前缀或路径段）豁免——
            # 中间产物非交付物，三态检查无意义（E040 与 pre_review 同源生效）
            if norm.startswith("_tmp/") or "/_tmp/" in norm:
                continue
            base = norm.rsplit("/", 1)[-1]
            if base in _DELIVERABLE_AUTO_COMMIT or norm == task_file_name or base == task_file_name:
                continue
            if norm not in paths:
                paths.append(norm)
    return paths


def _git_tracked(repo_root: Path, rel: str) -> bool:
    """git ls-files 校验路径已跟踪；git 异常时 fail-open 返回 True（不拦）。"""
    try:
        r = subprocess.run(
            ["git", "-C", str(repo_root), "ls-files", "--error-unmatch", "--", rel],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=15,  # #568：GBK 控制台不指定 encoding 即炸
        )
        return r.returncode == 0
    except Exception as e:
        # #568：fail-open 可见化——E040 已跟踪校验被跳过必须留痕
        print(f"[warn] E040 门禁组件 _git_tracked({rel}) 异常跳过（按已跟踪放行）: {e}", file=sys.stderr)
        return True


def _check_deliverables_committed(task_file: Path, fm: dict[str, Any],
                                  wiki_root: Path | None = None) -> tuple[bool, str, str]:
    """#522：执行报告交付物必须已入仓（已跟踪+无未提交改动），未入仓即拦。

    返回 (ok, block_msg, warn_msg)。识别不出路径/豁免声明 → ok=True + warn（红线 4：
    识别不出=WARNING 不硬拦）。code_files 声明的由 #363 门禁已管，本查报告交付物节。
    """
    wiki_root = wiki_root or _WIKI_ROOT
    try:
        body = task_file.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return True, "", "任务单不可读，交付物校验跳过"
    report = _extract_exec_report(body)
    if not report:
        return True, "", "无执行报告节（F-034 门禁已拦在前）"
    # 豁免判定收窄到「交付物」节内声明（#522 自体应用实证：完成内容/需要谁动作里
    # 引用豁免词作为说明文字也会命中全报告匹配——豁免词出现在交付物节才算声明）
    if any(m in _extract_deliverable_section(report) for m in DELIVERABLE_EXEMPT_MARKERS):
        return True, "", "任务单声明纯任务单修改/无代码交付物——交付物入仓校验豁免"

    paths = _extract_deliverable_paths(report, task_file.name)
    if not paths:
        return True, "", "交付物节未识别出文件路径（启发式覆盖外）——人工自核已入仓"

    problems: list[str] = []
    external: list[str] = []
    for rel in paths:
        # 库外绝对路径（D:/tech-wiki 等其他库/盘）：不属任何已知仓 git 无法核验
        # → WARNING 不拦（红线 4：识别不出不误拦——#534 狗粮实证撞线）
        if len(rel) > 1 and rel[1] == ":" and "Knowledge Delivery OS" not in rel:
            external.append(rel)
            continue
        repo = KDO_REPO_ROOT if "Knowledge Delivery OS" in rel else wiki_root
        # KDO 仓路径给的是绝对/仓外相对——取仓内相对部分
        repo_rel = rel.split("Knowledge Delivery OS 0.0.1/")[-1] if repo == KDO_REPO_ROOT else rel
        if not _git_tracked(repo, repo_rel):
            problems.append(f"untracked: {rel}")
            continue
        dirty = _git_uncommitted(repo, [repo_rel])
        if dirty:
            problems.append(f"未提交改动: {rel}")

    if problems:
        msg = ("E040 交付物入仓门禁（#522）：以下交付物未入仓——未 commit=未发生\n"
               + "\n".join(f"  - {p}" for p in problems)
               + "\n补救：git add <路径> && git commit -m '#<任务号> <交付说明> by <instance>' 后重跑 complete"
               # #569：报错可操作化——节边界规则+期望格式样例
               + "\n期望格式样例：执行报告内 **交付物** 字段节（`- **` 子弹行起也算字段行），"
                 "节内路径用反引号包裹（如 `90_control/x.py`），下一粗体字段/## 标题即节边界；"
                 "命令文本（如 kdo pre-submit -f <路径>）勿放交付物节")
        return False, msg, ""
    warn = f"交付物入仓核验通过（{len(paths) - len(external)} 个路径已跟踪且无脏改动）"
    if external:
        warn += f"；{len(external)} 个库外绝对路径无法 git 核验（WARNING 不拦，人工自核）：{'、'.join(external[:3])}"
    return True, "", warn


def _review_card_mark_reminder(task_file: Path) -> str:
    """#612 任务2：review verdict=pass 时，若执行报告「交付物」节含 30_wiki 卡片
    路径，返回一行「N 张交付卡待 review_mark 转正」提醒；否则返回空串。

    只提醒不自动转正——自动转正=代写卡片 frontmatter，越权限边界，不做。
    识别不出/读取异常=空串（提醒性输出，绝不阻断终审主流程）。
    """
    try:
        body = task_file.read_text(encoding="utf-8", errors="ignore")
        report = _extract_exec_report(body)
        cards = [p for p in _extract_deliverable_paths(report, task_file.name)
                 if p.startswith("30_wiki/") and p.endswith(".md")]
        if not cards:
            return ""
        shown = "、".join(f"`{c}`" for c in cards[:5])
        more = f" 等 {len(cards)} 张" if len(cards) > 5 else ""
        return (f"\n📌 提醒：{len(cards)} 张交付卡待 review_mark 转正：{shown}{more}"
                "（终审通过不自动转正——自动转正涉及代写卡片 frontmatter 权限边界，请生产方手动回填）")
    except Exception:
        return ""



# #429 F-034 交付五字段硬格式（老朱拍板「想犯错也犯不了」，停车场 F-034 收口）
# 机读锚点：执行报告节或 --evidence 文件含以下标记即算该字段存在（只验存在性，不判内容质量——只拦机械项不碰判断）
DELIVERY_FIELDS: dict[str, tuple[str, ...]] = {
    "改动文件清单": ("**交付物**", "**改动文件**", "**文件清单**"),
    "完成内容一句话": ("**完成内容**", "**一句话**", "**概要**"),
    "验证命令+输出": ("**验证**", "**实测**", "**测试**"),
    "未做项/边界": ("**边界**", "**未做项**", "**待定义**", "**遗留**"),
    "需要谁动作": ("**需要谁动作**", "**待办**", "**待用户拍板**", "**待审**"),
}


def _extract_exec_report(body: str) -> str:
    """提取任务单「## 执行报告」节（到下一个 ## 或文件尾）。"""
    idx = body.find("## 执行报告")
    if idx == -1:
        return ""
    nxt = body.find("\n## ", idx + 1)
    return body[idx:nxt] if nxt > 0 else body[idx:]


def _check_delivery_fields(task_file, evidence: str | None) -> tuple[bool, str]:
    """F-034：交付五字段机读检查——缺项=拒收（--force --reason 可声明例外，#444 台账留痕）。

    #444：evidence 不再作为五字段的替代检查面——五字段必须落在任务单「## 执行报告」节
    （evidence 只是佐证附件，防止指向任务单外文件绕过交接语义——#441 实证侧门）。
    """
    if evidence is not None:
        # evidence 仅验证可读性（佐证附件），检查面恒为任务单执行报告节
        try:
            Path(evidence).read_text(encoding="utf-8", errors="ignore")
        except OSError:
            return False, f"--evidence 文件不可读: {evidence}"
    body = task_file.read_text(encoding="utf-8", errors="ignore")
    check_text = _extract_exec_report(body)
    if not check_text:
        return False, "任务单缺少「## 执行报告」节（#429 F-034：交付必须落执行报告，口头完成=未完成；#444：evidence 附件不能替代）"
    # #569：前缀匹配——剥锚词尾部星号做前缀子串判定，`**改动文件清单**` 命中 `**改动文件`（闭合 ** 不再阻断合法后缀）
    missing = [k for k, anchors in DELIVERY_FIELDS.items()
               if not any(a.rstrip("*") in check_text for a in anchors)]
    if missing:
        sample = ("合法写法样例（五字段各起一行，粗体锚词开头即可）：" + "\n"
                  "  **交付物**：`路径/文件` ……" + "\n"
                  "  **完成内容**：一句话……" + "\n"
                  "  **验证**：命令 + 输出……" + "\n"
                  "  **边界**：……" + "\n"
                  "  **需要谁动作**：……")
        return False, (f"执行报告缺 {len(missing)} 个字段（#429 F-034）：{'、'.join(missing)}。请补全后重试，"
                       f"或 --force --reason '<理由>' 声明例外（#444 台账留痕）。" + "\n" + sample)
    return True, ""


# #444 force 例外台账：--force 绕过 F-034 必须留痕（谁/何时/绕过哪条/为何）——「声明例外」不得无痕
FORCE_LEDGER = _WIKI_ROOT / "90_control" / "force-exceptions.log"


def _log_force_exception(task_id: str, instance: str, reason: str,
                         bypass: str = "F-034 交付五字段") -> str:
    """#444：force 例外写入台账，终审可见。返回台账路径供提示。

    #504：bypass 参数化——claim --force 绕过 pending_review 阻塞同样留痕（默认保持 F-034 原口径）。
    """
    line = (f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}｜task={task_id}｜instance={instance}"
            f"｜bypass={bypass}｜reason={reason.strip()}\n")
    FORCE_LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with FORCE_LEDGER.open("a", encoding="utf-8") as f:
        f.write(line)
    # #511：force 例外同步写胶囊事件层（event_type=error——例外即风险事件；测试件同 #483 分流不写）
    if not task_id.startswith("task_9999_"):
        _capsule_event(instance or "unknown", "error",
                       f"force-exception;task={task_id};bypass={bypass};reason={reason.strip()[:200]}")
    return str(FORCE_LEDGER)


def action_complete(task_id: str, instance: str, evidence: str | None, force: bool = False,
                    reason: str | None = None) -> tuple[bool, str]:
    """Mark a claimed task as pending_review.

    --force: 允许从 queued 直接跳到 pending_review（用于生产已完成但未通过脚本领取的场景）
    #444：--force 必须配 --reason（例外留痕，台账 90_control/force-exceptions.log）
    #444：--evidence 路径留档任务单 frontmatter（佐证附件，不替代五字段检查面）
    """
    rows = parse_queue()
    task = find_task(task_id, rows)
    if task is None:
        return False, f"任务 {task_id} 不在队列中"

    expected = f"claimed-{instance}"
    if force and task["status"] == "queued":
        pass  # 跳过 claim，直接提交
    elif task["status"] != expected:
        return False, f"任务 {task_id} 状态为 {task['status']}，不是由 {instance} 领取的 {expected}"

    # #444：force 无理由=拒绝（「声明例外」被当常规通道的根治——#441 实证）
    if force and not (reason and reason.strip()):
        _log_gate_blocked(task_id, "F-034-force无理由", "--force 未配 --reason（#444 例外留痕要求）", instance)
        return False, ("--force 绕过 F-034 交付五字段门禁，必须配 --reason '<理由>'"
                       "（#444：例外留痕——谁/为何/绕过哪条/何时补，台账可溯）")

    task_file = _find_task_file_dual(task_id)
    if task_file is None:
        return False, f"找不到任务单文件: {task_id}（已按文件名和 frontmatter id 双重查找）"

    fm, _ = parse_frontmatter(task_file)
    if not force:
        # #429 F-034：交付五字段硬格式（升级替代原关键词检查：pre-submit/执行报告/验收）
        gate_ok, gate_msg = _check_delivery_fields(task_file, evidence)
        if not gate_ok:
            _log_gate_blocked(task_id, "F-034-五字段", gate_msg, instance)
            return False, gate_msg

    # #444：force 例外入台账（终审可见）
    force_note = ""
    if force:
        ledger = _log_force_exception(task_id, instance, reason or "")
        force_note = f"\n⚠️ force 例外已留痕: {ledger}"

    # #444：evidence 留档任务单 frontmatter（佐证附件可溯）
    fm_evidence = None
    if evidence:
        try:
            fm_evidence = str(Path(evidence).resolve().relative_to(_WIKI_ROOT)).replace("\\", "/")
        except ValueError:
            fm_evidence = evidence

    # 代码类提审门禁（#363）：code_files 未 commit → 拒绝流转
    gate_ok, gate_msg = _check_code_gate(task_file, fm)
    if not gate_ok:
        return False, gate_msg

    # #522：交付物已入仓校验（E040 机器兜底）——识别不出/豁免声明=WARNING 不硬拦（红线 4）
    dlv_ok, dlv_msg, dlv_warn = _check_deliverables_committed(task_file, fm)
    if not dlv_ok:
        _log_gate_blocked(task_id, "E040-交付物未入仓", dlv_msg, instance)
        return False, dlv_msg
    dlv_note = f"\n📦 交付物校验: {dlv_warn}" if dlv_warn else ""

    # #515：机器预审报告随提审附任务单（参考层——不放行不拦截；失败不阻断流转，
    # 预审失败本身写入报告让终审可见）。报告进任务单→随 complete 自动 commit 进冻结版
    try:
        import pre_review
        pre_review.attach_pre_review(task_file, pre_review.run_pre_review(task_file))
    except Exception as e:  # 预审层故障不阻断生产流转（参考层纪律），stderr 留痕
        import sys as _sys
        print(f"⚠️ 机器预审层故障（不阻断提转）: {e}", file=_sys.stderr)

    with QueueLock("production-queue"):
        rows = parse_queue()
        task = find_task(task_id, rows)
        # --force 允许从 queued 直跳：锁内重检必须同样接受该场景
        if task is None or not (
            (force and task["status"] == "queued") or task["status"] == expected
        ):
            return False, "队列状态在加锁期间发生变化，请重试"

        apply_updates(task_id, "pending_review", task_file, status="pending_review",
                      evidence=fm_evidence)

    # #389：门禁通过后登记 REVIEW-PENDING 段（被门禁拦截的 complete 到不了这里）
    try:
        rel_path = str(task_file.relative_to(_WIKI_ROOT)).replace("\\", "/")
    except ValueError:
        rel_path = str(task_file)
    _review_board_update(register={
        "seq": task["seq"], "task_id": task_id,
        "assignee": fm.get("assignee", task.get("assignee", "")),
        "task_file": rel_path,
    })

    return True, f"✅ {task_id} 已提交为 pending_review，等待欧阳锋终审{force_note}{dlv_note}"


# #433 负向判词证据层门禁（风清扬建议书 diag_20260823_fengqingyang-negative-claim-evidence-gate.md 采纳）
# 治标层：意见书含负向断言词必须带 `**存在性核查**` 锚点（只验锚点存在，不判核查质量——F-034 同款原则）。
# 强词=明确断言缺失（硬拦，缺锚点不闭环）；宽词=无/缺/没有（标需人工不硬杀——"无阻断项"等合法短语不误伤）。
EVIDENCE_ANCHOR = "**存在性核查**"
# 强词：明确断言缺失（硬拦）。#442 返工：删「为空/空值」——子串误伤"不为空/非空值"正向声明（#435 审计）；
# 为空/空值改由 PATTERN_DATA 断言句式检测（"grade 为空/值为空"仍拦，"字段不为空"主语不匹配不命中）
NEGATIVE_CLAIM_STRONG = ["不存在", "未备份", "未同步", "确认缺失", "缺失", "卡住", "丢失", "死锁"]
# 模式 1：无/缺/没有/未 + 0-6 字 + 敏感名词（备份/同步/镜像/副本…）——"无远程备份"类强断言（#430 复现用例）
NEGATIVE_CLAIM_PATTERN = re.compile(r"(?:无|缺|没有|未)(?:任何|远程|本地|有效|可用的|同步|备份的)?.{0,6}(?:备份|同步|镜像|副本|记录|存档|归档|历史|日志|留痕)")
# 模式 2（#435）：数据异常断言句式——主语 + 0-3 字 + 异常词。配断言句式防"无截断/确认无损坏"正向声明自伤（无主语匹配）
NEGATIVE_CLAIM_PATTERN_DATA = re.compile(r"(?:grade|字段|值|数据|内容|文件|路径|事件|记录)[ _]{0,3}(?:为空|空值|已损坏|被损坏|已截断|乱码|半写)")
# 宽词：单字级（无阻断项等合法短语只给需人工提示，不硬杀）。#435 扩展：截断/损坏/乱码/半写观察（正向声明"无截断"也会提示，不拦截）
# #515 判据 v1.1（08-28 欧阳锋校准）：「无/缺/没有」删除——组合断言已由 PATTERN 1 硬拦，
# 单字出现只制造 warn 噪音（狼来了效应实证）；「未发现」保留（意见书「我没看到」嫌疑有提示价值）
NEGATIVE_CLAIM_SOFT = ["未发现", "截断", "损坏", "乱码", "半写"]


def _check_negative_claims(text: str) -> tuple[bool, str]:
    """#433：意见书文本含负向断言词时必须含 `**存在性核查**` 锚点。

    返回 (block, msg)：block=True=review 不闭环；False=放行（宽词命中给 warn 提示）。
    """
    if EVIDENCE_ANCHOR in text:
        return True, ""
    hits = [w for w in NEGATIVE_CLAIM_STRONG if w in text]
    m = NEGATIVE_CLAIM_PATTERN.search(text)
    if m:
        hits.append(f"「{m.group(0)}」")
    m2 = NEGATIVE_CLAIM_PATTERN_DATA.search(text)
    if m2:
        hits.append(f"「{m2.group(0)}」")
    if hits:
        return False, (f"意见书含负向断言（{'/'.join(hits[:4])}）但无 `**存在性核查**` 锚点"
                       f"（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）")
    soft = [w for w in NEGATIVE_CLAIM_SOFT if w in text]
    if soft:
        return True, f"⚠️ 意见书含宽负向词（{'/'.join(soft[:3])}）无核查锚点——按需人工确认（#433 不硬杀）"
    return True, ""


def _check_review_record(task_file: Path, review_file: str | None) -> tuple[bool, str]:
    """#429 F-035：审查意见书强制落盘——任务单「## 终审记录」节（≥50 字）或 --review-file 路径，二者必有其一。"""
    if review_file is not None:
        try:
            rf_text = Path(review_file).read_text(encoding="utf-8", errors="ignore")
        except OSError:
            return False, f"--review-file 不可读: {review_file}"
        if len(rf_text.strip()) < 50:
            return False, "审查意见文件内容过短（#429 F-035），不构成审查意见书"
        return True, ""
    body = task_file.read_text(encoding="utf-8", errors="ignore")
    idx = body.find("## 终审记录")
    if idx == -1:
        return False, "任务单缺少「## 终审记录」节（#429 F-035：审查意见必须落盘，口头/群里意见=未审查）"
    nxt = body.find("\n## ", idx + 1)
    section = body[idx:nxt] if nxt > 0 else body[idx:]
    if len(section.strip()) < 50:
        return False, "终审记录节内容过短（#429 F-035），不构成审查意见书"
    return True, ""


# #461：取消台账（谁/为何取消，与 #444 force 台账同款留痕精神）
CANCEL_LEDGER = _WIKI_ROOT / "90_control" / "cancel-ledger.log"


def action_cancel(task_id: str, instance: str, reason: str | None) -> tuple[bool, str]:
    """#461：queued 单取消（被取代/不需要——终态，非删除）。--reason 必填（留痕：谁/为何）。"""
    if not (reason and reason.strip()):
        return False, "cancel 必须配 --reason '<取消理由>'（#461：谁/为何取消，台账可溯）"

    rows = parse_queue()
    task = find_task(task_id, rows)
    if task is None:
        return False, f"任务 {task_id} 不在队列中"
    if task["status"] != "queued":
        return False, f"任务 {task_id} 状态为 {task['status']}，仅 queued 可 cancel（claimed 先 release，pending_review 先退回）"

    task_file = _find_task_file_dual(task_id)
    if task_file is None:
        return False, f"找不到任务单文件: {task_id}"

    with QueueLock("production-queue"):
        rows = parse_queue()
        task = find_task(task_id, rows)
        if task is None or task["status"] != "queued":
            return False, "队列状态在加锁期间发生变化，请重试"
        apply_updates(task_id, "cancelled", task_file,
                      status="cancelled",
                      cancelled_by=instance,
                      cancel_reason=reason,
                      cancelled_at=current_utc_date())
    # 取消台账
    try:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with CANCEL_LEDGER.open("a", encoding="utf-8") as f:
            f.write(f"{ts}｜{task_id}｜{instance}｜{reason[:100]}\n")
    except Exception:
        pass
    return True, f"⏹️ {task_id} 已取消（cancelled，reason: {reason[:50]}）——终态，重新做=新单"


def action_mark_waiting(task_id: str, note: str | None = None) -> tuple[bool, str]:
    """#429 F-029：pending_review → waiting-external（等老朱/外部输入，不占审查位不阻塞领取）。

    #188 是活样本（只读引用）：等老朱真实使用首条记录，标 waiting-external 后不再阻塞不同 assignee 领取。
    """
    rows = parse_queue()
    task = find_task(task_id, rows)
    if task is None:
        return False, f"任务 {task_id} 不在队列中"
    if task["status"] != "pending_review":
        return False, f"任务 {task_id} 状态为 {task['status']}，只有 pending_review 可标 waiting-external"

    task_file = _find_task_file_dual(task_id)
    if task_file is None:
        return False, f"找不到任务单文件: {task_id}"

    with QueueLock("production-queue"):
        rows = parse_queue()
        task = find_task(task_id, rows)
        if task is None or task["status"] != "pending_review":
            return False, "队列状态在加锁期间发生变化，请重试"
        apply_updates(task_id, "waiting-external", task_file,
                      status="waiting-external",
                      waiting_since=current_utc_date(),
                      waiting_note=note or "")
    return True, f"⏸️ {task_id} 已标 waiting-external（等待外部输入，不阻塞队列）"


def action_resume(task_id: str) -> tuple[bool, str]:
    """#429 F-029：waiting-external → pending_review（外部输入到达，恢复待终审）。"""
    rows = parse_queue()
    task = find_task(task_id, rows)
    if task is None:
        return False, f"任务 {task_id} 不在队列中"
    if task["status"] != "waiting-external":
        return False, f"任务 {task_id} 状态为 {task['status']}，只有 waiting-external 可 resume"

    task_file = _find_task_file_dual(task_id)
    if task_file is None:
        return False, f"找不到任务单文件: {task_id}"

    with QueueLock("production-queue"):
        rows = parse_queue()
        task = find_task(task_id, rows)
        if task is None or task["status"] != "waiting-external":
            return False, "队列状态在加锁期间发生变化，请重试"
        apply_updates(task_id, "pending_review", task_file,
                      status="pending_review",
                      resumed_at=current_utc_date())
    return True, f"▶️ {task_id} 已恢复 pending_review（外部输入到达）"


def action_release(task_id: str, instance: str) -> tuple[bool, str]:
    """Release a claimed task back to queued."""
    rows = parse_queue()
    task = find_task(task_id, rows)
    if task is None:
        return False, f"任务 {task_id} 不在队列中"

    expected = f"claimed-{instance}"
    if task["status"] != expected:
        return False, f"任务 {task_id} 状态为 {task['status']}，不是 {expected}"

    task_file = _find_task_file_dual(task_id)
    if task_file is None:
        return False, f"找不到任务单文件: {task_id}（已按文件名和 frontmatter id 双重查找）"

    with QueueLock("production-queue"):
        apply_updates(task_id, "queued", task_file, status="queued")

    return True, f"✅ {task_id} 已释放回 queued"


def _action_review_override(task: dict, task_file: Path, reviewer: str, reason: str) -> tuple[bool, str]:
    """#538 改判通道：reviewed→queued（终审自我纠错机器通道——破窗手改的根治）。

    纪律：--reason 必填；例外落 force-exceptions 台账（#444 同款）；任务单追记
    「## 改判记录」节（时间/原 verdict/理由）；只支持 reviewed→queued 一个方向
    （grade 更正走任务单追记，不动状态机）。改判后探针 new_failback 口径已覆盖
    「曾 reviewed」场景（#538 任务 2，queued ∩ last_reviewed 即改判信号）。
    """
    task_id = task["task_id"]
    fm, _ = parse_frontmatter(task_file)
    orig = f"PASS {fm.get('grade', '')}".strip()
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")

    # 任务单追记改判节（幂等：多次改判逐条追加）
    body = task_file.read_text(encoding="utf-8")
    entry = (f"- [{ts}] **{reviewer}改判**：{orig} → FAIL（返工）｜理由：{reason.strip()}\n")
    if "## 改判记录" in body:
        idx = body.find("## 改判记录")
        nxt = body.find("\n## ", idx + 1)
        insert_at = nxt if nxt > 0 else len(body.rstrip("\n"))
        body = body[:insert_at].rstrip("\n") + "\n\n" + entry + ("\n" + body[insert_at:] if nxt > 0 else "\n")
    else:
        body = body.rstrip("\n") + f"\n\n## 改判记录\n\n{entry}"
    task_file.write_text(body, encoding="utf-8")

    ledger = _log_force_exception(task_id, reviewer, reason,
                                  bypass="reviewed→queued 改判（#538 终审自我纠错通道）")
    # #580（F-064）：改判=FAIL 打回同族——同样自动打 rework:true 标，返工重提豁免 #504
    with QueueLock("production-queue"):
        rows = parse_queue()
        task2 = find_task(task_id, rows)
        if task2 is None or task2["status"] != "reviewed":
            return False, "队列状态在加锁期间发生变化，请重试"
        apply_updates(task_id, "queued", task_file, status="queued", rework=True)
    return True, (f"↩️ {task_id} 已改判：{orig} → FAIL，状态回 queued（返工）\n"
                  f"⚠️ 改判例外已留痕: {ledger}\n任务单已追记「## 改判记录」节"
                  f"（已自动标 rework:true——返工重提不再触发 #504 拦截，#580 F-064）")


def action_review(task_id: str, verdict: str, reviewer: str, grade: str | None = None,
                  review_file: str | None = None, override: bool = False,
                  reason: str | None = None, force: bool = False) -> tuple[bool, str]:
    """Ouyangfeng-only: review a pending_review task."""
    if reviewer != "欧阳锋":
        return False, "只有欧阳锋可以执行 review 操作"
    # #546：终审权机器校验（一具两职根治）——当前 cwd 须有 ouyangfeng 登记实例
    auth_ok, auth_msg = _check_review_authority(task_id, reviewer, force=force, reason=reason)
    if not auth_ok:
        _log_gate_blocked(task_id, "#546-终审权校验", auth_msg, reviewer)
        return False, auth_msg
    if auth_msg:  # force 逃生门留痕提示随成功消息透传
        print(auth_msg, file=sys.stderr)

    rows = parse_queue()
    task = find_task(task_id, rows)
    if task is None:
        return False, f"任务 {task_id} 不在队列中"
    if task["status"] != "pending_review":
        # #538：改判通道——reviewed→queued（verdict=fail + --override + --reason 必填）
        if override and verdict == "fail" and task["status"] == "reviewed":
            if not (reason and reason.strip()):
                return False, ("改判必须配 --reason '<理由>'（#538：例外留痕——"
                               "谁/为何/何时，台账可溯；无正当理由不改判）")
            tf = _find_task_file_dual(task_id)
            if tf is None:
                return False, f"找不到任务单文件: {task_id}"
            return _action_review_override(task, tf, reviewer, reason)
        return False, f"任务 {task_id} 状态为 {task['status']}，不是 pending_review，无法终审"

    task_file = _find_task_file_dual(task_id)
    if task_file is None:
        return False, f"找不到任务单文件: {task_id}（已按文件名和 frontmatter id 双重查找）"

    # #429 F-035：审查意见书强制落盘（老朱校准：口头/群里意见=未审查）
    # 意见载体 = 任务单「## 终审记录」节（非空）或 --review-file 指定路径
    ok, msg = _check_review_record(task_file, review_file)
    if not ok:
        _log_gate_blocked(task_id, "F-035-意见书", msg, reviewer)
        return False, msg

    # #433：负向判词证据层门禁——意见书含负向断言词必须带 `**存在性核查**` 锚点
    opinion_text = ""
    if review_file is not None:
        opinion_text = Path(review_file).read_text(encoding="utf-8", errors="ignore")
    else:
        body = task_file.read_text(encoding="utf-8", errors="ignore")
        idx = body.find("## 终审记录")
        if idx != -1:
            nxt = body.find("\n## ", idx + 1)
            opinion_text = body[idx:nxt] if nxt > 0 else body[idx:]
    gate_ok, gate_msg = _check_negative_claims(opinion_text)
    if not gate_ok:
        _log_gate_blocked(task_id, "F-035-负向判词", gate_msg, reviewer)
        return False, gate_msg

    # F-036（#主动立项 2026-08-24）：审查发现必须给落点——发现问题节含 🟠/🟡
    # 条目时必须注明去向（建议书/停车场 F-xxx/任务单立项），无落点=终审不闭环
    disp_ok, disp_msg = _check_issue_disposition(opinion_text)
    if not disp_ok:
        _log_gate_blocked(task_id, "F-036-问题落点", disp_msg, reviewer)
        return False, disp_msg

    with QueueLock("production-queue"):
        if verdict == "pass":
            updates = {
                "status": "reviewed",
                "reviewed_by": reviewer,
                "review_date": current_utc_date(),
            }
            if grade:
                updates["grade"] = grade
            apply_updates(task_id, "reviewed", task_file, **updates)
            grade_note = f"，等级 {grade}" if grade else ""
            # #389：终审通过 → REVIEW-PENDING 段对应行自动划掉
            _review_board_update(
                strike=task_id,
                strike_note=f" → 已终审 PASS {grade or ''}（{current_utc_date()} 欧阳锋）",
            )
            # #612 任务2：review_mark 漏转正二次复发（#586/#596，E018 家族同源）——
            # 终审通过时交付物含 30_wiki 卡片 → 输出转正提醒（提醒即可，不代写）
            remind = _review_card_mark_reminder(task_file)
            return True, f"✅ {task_id} 终审通过，状态更新为 reviewed{grade_note}{remind}"
        else:
            # #580（F-064）：FAIL 打回时自动打 rework:true 标——返工重提 claim 时
            # _is_rework_task 读到该标即豁免 #504 own-pending 阻塞（重提≠接新单）。
            # 走 apply_updates 写 frontmatter（幂等，多轮返工重复写 true 无副作用）。
            apply_updates(task_id, "queued", task_file, status="queued", rework=True)
            # #389：终审退回 → 同样划掉登记行（任务回 queued，不再待终审）
            _review_board_update(
                strike=task_id,
                strike_note=f" → 终审退回 queued（{current_utc_date()} 欧阳锋）",
            )
            return True, (f"⚠️ {task_id} 终审不通过，状态退回 queued"
                          f"（已自动标 rework:true——返工完成后重提不再触发 #504 拦截，#580 F-064）")


def _task_depends_on(task_id: str) -> list[str]:
    """#472：任务书 frontmatter depends_on → 依赖任务号列表（存量无字段=[]=可领）。"""
    tf = _find_task_file_dual(task_id)
    if tf is None:
        return []
    fm, _ = parse_frontmatter(tf)
    dep = fm.get("depends_on", "")
    if isinstance(dep, list):
        return [str(d).strip().lstrip("#") for d in dep if str(d).strip()]
    if dep:
        return [str(dep).strip().lstrip("#")]
    return []


def _is_active_task(task_id: str, rows: list) -> bool:
    """依赖任务仍在进行（queued/claimed/pending_review/blocked）→ 未满足。"""
    for r in rows:
        if r["task_id"] == task_id:
            return (r["status"] in ("queued", "pending_review", "blocked")
                    or r["status"].startswith("claimed-"))
    return False  # 队列无行=已结束，视为满足


def _consumption_heartbeat(role: str | None) -> None:
    """#562 任务2（方案B 落点）：消费回执=心跳——myqueue/claim/complete/release/review
    都是 agent 真实消费队列的动作时刻，顺手蹭拍注册表心跳。
    时钟活着≠agent 活着，但「消费动作发生」=agent 活着的最硬证据。
    零成本钩；失败不阻断主流程。仅限五个 KDO 角色（拼音），其余 instance 不入注册表。"""
    if not role:
        return
    _CN_TO_PINYIN = {"欧阳锋": "ouyangfeng", "王语嫣": "wangyuyan", "黄药师": "huangyaoshi",
                     "老顽童": "laowantong", "风清扬": "fengqingyang"}
    role = _CN_TO_PINYIN.get(role, role)
    try:
        import role_registry
        if role not in role_registry.ROLE_PACE_MIN:
            return
        role_registry.heartbeat(role, tool=os.environ.get("KDO_TOOL", "cli"),
                                session_scope=os.getcwd())
    except Exception:
        pass


def action_myqueue(role: str) -> int:
    """#472 任务路由：角色视角的队列视图（只读，不动状态机）。

    可领（queued+无依赖或依赖已满足+非冻结）/ 等依赖（depends_on 未满足）/
    冻结（队列行标注勿领/冻结留档——含被取代挂账）/ 进行中（claimed-<role>）/
    待终审（pending_review）。
    """
    # #552：时钟蹭拍——myqueue 是角色时钟每拍必跑的唯一命令，顺手写注册表心跳
    # #562：蹭拍逻辑上提为 _consumption_heartbeat，claim/complete/release/review 共用
    _consumption_heartbeat(role)
    rows = parse_queue()
    mine = [r for r in rows if r["assignee"] == role]
    todo, wait, frozen, doing, reviewing = [], [], [], [], []
    for r in mine:
        status = r["status"]
        if status.startswith("claimed-"):
            doing.append(r)
        elif status == "pending_review":
            reviewing.append(r)
        elif status == "queued":
            if re.search(r"勿领|冻结留档|冻结勿", r["raw"]):
                frozen.append(r)
            else:
                blockers = [d for d in _task_depends_on(r["task_id"]) if _is_active_task(d, rows)]
                if blockers:
                    r["blockers"] = blockers
                    wait.append(r)
                else:
                    todo.append(r)

    def fmt(items):
        if not items:
            return "  (无)"
        lines = []
        for r in items:
            line = f"  #{r['seq']} {r['task_id']} — {r['name'][:45]}"
            if r.get("blockers"):
                line += f"（等 #{','.join(r['blockers'])} 终审）"
            lines.append(line)
        return "\n".join(lines)

    print(f"# role={role} · 任务路由（#472 只读视图，不动状态机）")
    print(f"✅ 可领 {len(todo)}:"); print(fmt(todo))
    print(f"⏸ 等依赖 {len(wait)}:"); print(fmt(wait))
    print(f"🧊 冻结 {len(frozen)}:"); print(fmt(frozen))
    print(f"🚧 进行中 {len(doing)}:"); print(fmt(doing))
    print(f"⏳ 待终审 {len(reviewing)}:"); print(fmt(reviewing))
    _print_recent_reviews(role)
    return 0


# #535 myqueue「最近终审」栏：REVIEW-PENDING 段划掉行里的终审落点（48h 内，本角色）
_REVIEW_DONE_RE = re.compile(
    r"^- ~~#(\d+) (\S+?)｜(\S+?)｜提审 .*?~~ → (已终审 (?:PASS\s*[A-]*|FAIL)|终审退回)"
    r".*?（(\d{4}-\d{2}-\d{2})")


def _print_recent_reviews(role: str, hours: int = 48) -> None:
    """近 48h 我名下终审落点——只读视图顺手查，不把「没有变化」误读为「仍在审」。"""
    from datetime import datetime as _dt, timedelta as _td
    try:
        text = QUEUE_PATH.read_text(encoding="utf-8")
    except OSError:
        text = ""
    block = ""
    if REVIEW_BEGIN in text and REVIEW_END in text:
        block = text.split(REVIEW_BEGIN)[1].split(REVIEW_END)[0]
    cutoff = _dt.now() - _td(hours=hours)
    rows = []
    for line in block.splitlines():
        m = _REVIEW_DONE_RE.match(line.strip())
        if not m or m.group(3) != role:
            continue
        seq, tid, _a, verdict, dstr = m.groups()
        try:
            d = _dt.strptime(dstr, "%Y-%m-%d")
        except ValueError:
            continue
        if d >= cutoff:
            tag = "🔴退回返工" if "退回" in verdict or "FAIL" in verdict else f"✅{verdict.replace('已终审 ', '')}"
            rows.append(f"  #{seq} {tid} — {tag}（{dstr}）")
    print(f"⚖️ 最近终审（{hours}h） {len(rows)}:")
    print("\n".join(rows) if rows else "  (无)")


def main() -> int:
    if yaml is None:
        print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
        return 1

    args = sys.argv[1:]
    if not args:
        print(__doc__, file=sys.stderr)
        return 1

    action = args[0]

    if action == "myqueue":
        if len(args) < 2:
            print("用法: queue_transition.py myqueue <role>（拼音角色名）", file=sys.stderr)
            return 1
        return action_myqueue(args[1])

    if action == "register":
        # #546：实例上岗登记（欧阳锋等纯审查角色不 claim，从这里登记）
        if len(args) < 2:
            print("用法: queue_transition.py register <instance>", file=sys.stderr)
            return 1
        ok, msg = action_register(args[1])
        print(msg)
        return 0 if ok else 1

    if action == "status":
        rows = parse_queue()
        pending = [r for r in rows if r["status"] == "pending_review"]
        claimed = [r for r in rows if r["status"].startswith("claimed-")]
        queued = [r for r in rows if r["status"] == "queued"]
        print(f"队列总任务数: {len(rows)}")
        print(f"queued: {len(queued)}")
        print(f"claimed: {len(claimed)}")
        print(f"pending_review: {len(pending)}")
        for r in pending:
            print(f"  #{r['seq']} {r['task_id']} — {r['name']}")
        return 0

    if len(args) < 2:
        print(__doc__, file=sys.stderr)
        return 1

    task_id = args[1]

    instance = None
    evidence = None
    verdict = None
    reviewer = None
    grade = None
    review_file = None
    note = None
    reason = None
    force = False
    override = False
    no_commit = False

    i = 2
    while i < len(args):
        if args[i] == "--instance" and i + 1 < len(args):
            instance = args[i + 1]
            i += 2
        elif args[i] == "--force":
            force = True
            i += 1
        elif args[i] == "--override":
            override = True  # #538：reviewed→queued 改判通道（需 --verdict fail --reason）
            i += 1
        elif args[i] == "--no-commit":
            no_commit = True
            i += 1
        elif args[i] == "--evidence" and i + 1 < len(args):
            evidence = args[i + 1]
            i += 2
        elif args[i] == "--reason" and i + 1 < len(args):
            reason = args[i + 1]  # #444：--force 例外声明（留痕台账）
            i += 2
        elif args[i] == "--verdict" and i + 1 < len(args):
            verdict = args[i + 1]
            i += 2
        elif args[i] == "--reviewer" and i + 1 < len(args):
            reviewer = args[i + 1]
            i += 2
        elif args[i] == "--grade" and i + 1 < len(args):
            grade = args[i + 1]
            if grade not in ("A", "A-", "B+", "B", "B-", "C"):
                print("--grade 需要 A|A-|B+|B|B-|C", file=sys.stderr)
                return 1
            i += 2
        elif args[i] == "--review-file" and i + 1 < len(args):
            review_file = args[i + 1]
            i += 2
        elif args[i] == "--note" and i + 1 < len(args):
            note = args[i + 1]
            i += 2
        else:
            print(f"未知参数: {args[i]}", file=sys.stderr)
            return 1

    if action == "claim":
        if not instance:
            print("claim 需要 --instance <instance>", file=sys.stderr)
            return 1
        ok, msg = action_claim(task_id, instance, force=force)
    elif action == "complete":
        if not instance:
            print("complete 需要 --instance <instance>", file=sys.stderr)
            return 1
        ok, msg = action_complete(task_id, instance, evidence, force=force, reason=reason)
    elif action == "release":
        if not instance:
            print("release 需要 --instance <instance>", file=sys.stderr)
            return 1
        ok, msg = action_release(task_id, instance)
    elif action == "review":
        if verdict not in ("pass", "fail"):
            print("review 需要 --verdict pass|fail", file=sys.stderr)
            return 1
        if not reviewer:
            reviewer = "欧阳锋"
        ok, msg = action_review(task_id, verdict, reviewer, grade, review_file=review_file,
                                override=override, reason=reason, force=force)
    elif action in ("mark-waiting", "mark_waiting"):
        ok, msg = action_mark_waiting(task_id, note)
    elif action in ("resume",):
        ok, msg = action_resume(task_id)
    elif action == "cancel":
        ok, msg = action_cancel(task_id, instance, reason or note)  # --reason 优先（#461 语义），--note 兼容
    else:
        print(__doc__, file=sys.stderr)
        return 1

    print(msg)
    if ok:
        # #562：流转成功=消费回执，蹭拍心跳（review 归 reviewer，其余归 instance）
        if action in ("claim", "complete", "release", "review"):
            _consumption_heartbeat(reviewer if action == "review" else instance)
        _refresh_dashboard()
        # #390：流转成功（含 dashboard 刷新）后自动 git 收口；门禁拦截的流转到不了这里
        if not no_commit and action in ("claim", "complete", "release", "review", "mark-waiting", "resume", "cancel"):
            actor = reviewer if action == "review" else instance
            _git_commit_transition(task_id, action, actor or "")
        # #511：流转事件层（单写入面=本钩；失败可见不阻断）——测试件（task_9999_）不写胶囊
        if action in ("claim", "complete", "review") and not task_id.startswith("task_9999_"):
            actor = reviewer if action == "review" else (instance or "")
            _capsule_event(actor or "unknown", "queue_transition",
                           f"task={task_id};action={action};actor={actor}")
            if action == "review":
                _capsule_event(reviewer or "ouyangfeng", "decision",
                               f"task={task_id};verdict={verdict};grade={grade or '-'};reviewer={reviewer}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
