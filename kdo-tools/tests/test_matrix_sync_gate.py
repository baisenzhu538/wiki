"""#537 回归：总账登记机器核查（基础设施单 reviewed 时矩阵未同步→提醒）。

三类用例（任务书第 5 条）：触发（未同步→⛔）/豁免（matrix_exempt→EXEMPT）/已同步→None。

运行：python -m pytest kdo-tools/tests/test_matrix_sync_gate.py -q
沙盒：tmp git 仓+合成任务单，不碰真实库。
"""
import importlib.util
import subprocess
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "conveyor_probe", Path(__file__).resolve().parent.parent / "conveyor_probe.py"
)
probe = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(probe)

MATRIX = "90_control/notification-coverage-matrix.md"


def _git(repo, *args):
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True, timeout=30)


def _repo(tmp_path):
    repo = tmp_path / "wiki"
    (repo / "60_feedback" / "tasks").mkdir(parents=True)
    (repo / "kdo-tools").mkdir(parents=True)
    (repo / "90_control").mkdir(parents=True)
    _git(repo, "init")
    _git(repo, "config", "user.email", "t@t")
    _git(repo, "config", "user.name", "t")
    (repo / "kdo-tools" / "conveyor_probe.py").write_text("x=1\n", encoding="utf-8")
    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "init")
    return repo


def _task(repo, task_id, code_files, exempt=False):
    cf = "".join(f"- {c}\n" for c in code_files)
    ex = "matrix_exempt: true\n" if exempt else ""
    fp = repo / "60_feedback" / "tasks" / f"{task_id}.md"
    fp.write_text(f"---\nid: 1\n{ex}code_files:\n{cf}---\n\n# t\n", encoding="utf-8")
    return fp


def _commit_task(repo, task_id, with_matrix=False):
    paths = [f"60_feedback/tasks/{task_id}.md", "kdo-tools/conveyor_probe.py"]
    (repo / "kdo-tools" / "conveyor_probe.py").write_text("x=2\n", encoding="utf-8")
    if with_matrix:
        (repo / MATRIX).write_text("matrix v2\n", encoding="utf-8")
        paths.append(MATRIX)
    _git(repo, "add", *paths)
    _git(repo, "commit", "-m", f"work {task_id}")


def test_unsynced_infra_task_flagged(tmp_path, monkeypatch):
    repo = _repo(tmp_path)
    _task(repo, "task_a", ["kdo-tools/conveyor_probe.py"])
    _commit_task(repo, "task_a", with_matrix=False)
    monkeypatch.setattr(probe, "TASK_DIR", repo / "60_feedback" / "tasks")
    out = probe._matrix_sync_check("task_a", repo)
    assert out and "总账未同步" in out and "conveyor_probe.py" in out


def test_synced_task_passes(tmp_path, monkeypatch):
    repo = _repo(tmp_path)
    (repo / MATRIX).write_text("matrix v1\n", encoding="utf-8")
    _task(repo, "task_b", ["kdo-tools/conveyor_probe.py"])
    _commit_task(repo, "task_b", with_matrix=True)
    monkeypatch.setattr(probe, "TASK_DIR", repo / "60_feedback" / "tasks")
    assert probe._matrix_sync_check("task_b", repo) is None


def test_exempt_task_skips(tmp_path, monkeypatch):
    repo = _repo(tmp_path)
    _task(repo, "task_c", ["kdo-tools/conveyor_probe.py"], exempt=True)
    _commit_task(repo, "task_c", with_matrix=False)
    monkeypatch.setattr(probe, "TASK_DIR", repo / "60_feedback" / "tasks")
    assert probe._matrix_sync_check("task_c", repo) == "EXEMPT"


def test_non_infra_task_passes(tmp_path, monkeypatch):
    repo = _repo(tmp_path)
    _task(repo, "task_d", ["kdo-tools/quality_metrics.py"])  # 不在 INFRA_WATCH
    _commit_task(repo, "task_d", with_matrix=False)
    monkeypatch.setattr(probe, "TASK_DIR", repo / "60_feedback" / "tasks")
    assert probe._matrix_sync_check("task_d", repo) is None


def test_missing_task_file_passes(tmp_path, monkeypatch):
    repo = _repo(tmp_path)
    monkeypatch.setattr(probe, "TASK_DIR", repo / "60_feedback" / "tasks")
    assert probe._matrix_sync_check("task_ghost", repo) is None
