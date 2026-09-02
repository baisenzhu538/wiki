"""#616 任务2 回归：update_task_frontmatter 行级保字段（claim 抹字段 bug 根治）。

实证根因（09-02 两起）：旧实现 yaml.safe_load→safe_dump round-trip，把 YAML 语法上
解析为 null 的字段抹成真 null——#614 `decision_source: #613 ...`（# 开头被当注释）、
#613 `title: #586批...` 同型。修法=行级改写：未命中键逐字节保留，命中键整行替换。

用例：# 开头值保留 / 多行折叠值保留 / 命中键替换含续行块 / 新键追加 / CRLF 保留。

运行：python -m pytest 90_control/scripts/tests/test_frontmatter_preserve_616.py -q
"""
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

from queue_transition import update_task_frontmatter


class TestFrontmatterPreserve(unittest.TestCase):
    def _run(self, content: str, **updates) -> str:
        td = tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        fp = Path(td.name) / "task_9999_x.md"
        with fp.open("w", encoding="utf-8", newline="") as f:
            f.write(content)  # newline="" 防 Windows 文本写入 \n→\r\n 翻译
        update_task_frontmatter(fp, **updates)
        with fp.open("r", encoding="utf-8", newline="") as f:
            return f.read()  # newline="" 读回原文（CRLF 用例不断言归一化）

    def test_hash_prefixed_value_preserved(self):
        """#614 实证型：`decision_source: #613 ...`（YAML 视角是注释）不得被抹为 null。"""
        out = self._run(
            "---\n"
            "id: task_9999_x\n"
            "decision_source: #613 上报王语嫣的清单——裁定补审\n"
            "reviewer: 欧阳锋\n"
            "---\n\n# 正文\n",
            status="in_progress", instance="huangyaoshi-kimi",
        )
        self.assertIn("decision_source: #613 上报王语嫣的清单——裁定", out)
        self.assertIn("reviewer: 欧阳锋", out)
        self.assertIn("status: in_progress", out)
        self.assertIn("instance: huangyaoshi-kimi", out)
        self.assertIn("updated_at:", out)
        self.assertIn("# 正文", out)

    def test_multiline_folded_value_preserved(self):
        """#613 实证型：多行折叠值（续行缩进）原样保留。"""
        out = self._run(
            "---\n"
            "id: task_9999_x\n"
            "title: 排查补齐\n"
            "decision_source: 欧阳锋建议书 prop_xxx（#611\n"
            "  终审发现）09-02 王语嫣裁定立项\n"
            "reviewer: 欧阳锋\n"
            "---\n\n# 正文\n",
            status="queued",
        )
        self.assertIn("decision_source: 欧阳锋建议书 prop_xxx（#611\n  终审发现）09-02 王语嫣裁定立项", out)
        self.assertIn("title: 排查补齐", out)

    def test_updated_key_multiline_block_replaced(self):
        """命中键旧值是多行块时，续行块随旧值一并换下，不留孤儿行。"""
        out = self._run(
            "---\n"
            "id: task_9999_x\n"
            "code_files:\n"
            "  - a.py\n"
            "  - b.py\n"
            "status: queued\n"
            "---\n\n# 正文\n",
            code_files=["c.py"],
        )
        self.assertIn("code_files:\n- c.py", out)
        self.assertNotIn("a.py", out)
        self.assertNotIn("b.py", out)
        self.assertIn("status: queued", out)

    def test_none_update_means_untouched(self):
        """updates 里 None = 不动该字段（原语义保留）。"""
        out = self._run(
            "---\nid: task_9999_x\nevidence: old.md\n---\n\n# 正文\n",
            evidence=None, status="queued",
        )
        self.assertIn("evidence: old.md", out)

    def test_crlf_preserved(self):
        out = self._run(
            "---\r\nid: task_9999_x\r\ndecision_source: #613 清单\r\n---\r\n\r\n# 正文\r\n",
            status="queued",
        )
        self.assertIn("decision_source: #613 清单\r\n", out)
        self.assertIn("status: queued\r\n", out)


if __name__ == "__main__":
    unittest.main()
