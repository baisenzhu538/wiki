#!/usr/bin/env python3
"""
Validate artifacts against quality gates before shipping.
Pure stdlib. No external dependencies.
Usage: python 90_control/scripts/kdo_validate.py [artifact_path]
"""

import re
import sys
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


class SimpleYAMLParser:
    def parse(self, text: str) -> dict:
        result = {}
        current_key = None
        current_list = []
        in_list = False

        for line in text.splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue

            if stripped.startswith("-"):
                item = stripped[1:].strip()
                item = self._unquote(item)
                current_list.append(item)
                in_list = True
            else:
                if in_list and current_key:
                    result[current_key] = current_list
                    current_list = []
                    in_list = False

                if ":" in stripped:
                    key, val = stripped.split(":", 1)
                    key = key.strip()
                    val = val.strip()
                    val = self._unquote(val)
                    if val == "":
                        val = None
                    current_key = key
                    result[key] = val

        if in_list and current_key:
            result[current_key] = current_list

        return result

    @staticmethod
    def _unquote(s: str) -> str:
        if s.startswith('"') and s.endswith('"'):
            return s[1:-1]
        if s.startswith("'") and s.endswith("'"):
            return s[1:-1]
        return s


def extract_frontmatter(content: str) -> dict:
    m = FRONTMATTER_RE.match(content)
    if not m:
        return {}
    return SimpleYAMLParser().parse(m.group(1))


def validate_content_artifact(fp: Path, fm: dict, body: str) -> list:
    errors = []
    rel = fp.relative_to(VAULT_ROOT).as_posix()

    # Gate 1: Target audience defined
    target = fm.get("target_user", "")
    if not target or len(target) < 3:
        errors.append(f"{rel}: [Content Gate] target_user too short or missing")

    # Gate 2: Core thesis in first 1000 chars
    if len(body) > 0:
        first_k = body[:1000]
        # Look for bold or heading that states a thesis
        if not re.search(r"(^#{1,2}\s+|\*\*|__)", first_k, re.MULTILINE):
            errors.append(f"{rel}: [Content Gate] No clear thesis in first 1000 chars (no heading or bold)")

    # Gate 3: Structure complete (has at least 2 sections)
    sections = re.findall(r"^#{2,3}\s+", body, re.MULTILINE)
    if len(sections) < 2:
        errors.append(f"{rel}: [Content Gate] Less than 2 sections (structure incomplete)")

    # Gate 4: Claims traceable to source_refs
    sources = fm.get("source_refs", [])
    if not sources:
        errors.append(f"{rel}: [Content Gate] No source_refs (claims not traceable)")

    # Gate 5: Feedback path declared
    if "feedback" not in body.lower() and "comment" not in body.lower():
        errors.append(f"{rel}: [Content Gate] No feedback path declared in body")

    return errors


def validate_code_artifact(fp: Path, fm: dict, body: str) -> list:
    errors = []
    rel = fp.relative_to(VAULT_ROOT).as_posix()

    # Gate 1: Installation path documented
    if "install" not in body.lower() and "setup" not in body.lower():
        errors.append(f"{rel}: [Code Gate] No installation instructions")

    # Gate 2: Usage example exists
    if "```" not in body and "example" not in body.lower():
        errors.append(f"{rel}: [Code Gate] No usage example (code block or 'example' section)")

    # Gate 3: Validation steps exist
    if "test" not in body.lower() and "validate" not in body.lower():
        errors.append(f"{rel}: [Code Gate] No test/validation steps")

    # Gate 4: Failure modes named
    if "error" not in body.lower() and "fail" not in body.lower() and "troubleshoot" not in body.lower():
        errors.append(f"{rel}: [Code Gate] No failure modes or troubleshooting documented")

    # Gate 5: Version/release path
    if "version" not in body.lower() and "release" not in body.lower() and "changelog" not in body.lower():
        errors.append(f"{rel}: [Code Gate] No version or release path documented")

    return errors


def validate_capability_artifact(fp: Path, fm: dict, body: str) -> list:
    errors = []
    rel = fp.relative_to(VAULT_ROOT).as_posix()

    # Gate 1: Task boundary defined
    if "boundary" not in body.lower() and "scope" not in body.lower():
        errors.append(f"{rel}: [Capability Gate] Task boundary not defined")

    # Gate 2: Input/output spec
    if "input" not in body.lower() or "output" not in body.lower():
        errors.append(f"{rel}: [Capability Gate] Input/output spec unclear")

    # Gate 3: Tool permissions declared
    if "permission" not in body.lower() and "access" not in body.lower():
        errors.append(f"{rel}: [Capability Gate] Tool permissions not declared")

    # Gate 4: Failure handling
    if "fail" not in body.lower() and "error" not in body.lower() and "exception" not in body.lower():
        errors.append(f"{rel}: [Capability Gate] Failure handling not documented")

    # Gate 5: Evaluation cases
    if "test" not in body.lower() and "eval" not in body.lower() and "example" not in body.lower():
        errors.append(f"{rel}: [Capability Gate] No evaluation cases or examples")

    return errors


def validate_file(fp: Path) -> list:
    errors = []
    rel = fp.relative_to(VAULT_ROOT).as_posix()
    content = fp.read_text(encoding="utf-8")
    fm = extract_frontmatter(content)
    m = FRONTMATTER_RE.match(content)
    body = content[m.end():] if m else content

    if not fm:
        errors.append(f"{rel}: missing frontmatter")
        return errors

    page_type = fm.get("type", "")
    artifact_type = fm.get("artifact_type", "")

    if page_type == "artifact":
        if artifact_type in ["article", "video", "audio", "tutorial", "report", "course"]:
            errors.extend(validate_content_artifact(fp, fm, body))
        elif artifact_type in ["app", "plugin", "template", "script", "package"]:
            errors.extend(validate_code_artifact(fp, fm, body))
        elif artifact_type in ["skill", "agent", "workflow", "eval", "playbook"]:
            errors.extend(validate_capability_artifact(fp, fm, body))
        else:
            errors.append(f"{rel}: unknown artifact_type '{artifact_type}'")
    elif page_type == "concept":
        # Minimal concept validation
        if "### [Critique]" not in body:
            errors.append(f"{rel}: [Concept Gate] Missing [Critique] section")
        if "### [Synthesis]" not in body:
            errors.append(f"{rel}: [Concept Gate] Missing [Synthesis] section")
    elif page_type in ["decision", "improvement-plan"]:
        # Already covered by schema; add lightweight checks
        pass
    else:
        # Unknown type, skip specific gates
        pass

    return errors


def validate_path(target: Path) -> dict:
    all_errors = []
    file_count = 0

    md_files = list(target.rglob("*.md"))
    for fp in md_files:
        file_count += 1
        errs = validate_file(fp)
        all_errors.extend(errs)

    return {
        "files_checked": file_count,
        "errors": all_errors,
        "passed": len(all_errors) == 0,
    }


def main():
    target = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else VAULT_ROOT / "40_outputs"
    result = validate_path(target)

    print("=" * 50)
    print("KDO Validate Report")
    print("=" * 50)
    print(f"Files checked: {result['files_checked']}")
    print(f"Errors found:  {len(result['errors'])}")
    print(f"Status:        {'PASS' if result['passed'] else 'FAIL'}")
    print()

    if result["errors"]:
        for err in result["errors"]:
            print(f"  [GATE FAIL] {err}")
        sys.exit(1)
    else:
        print("All quality gates passed. Ready to ship.")
        sys.exit(0)


if __name__ == "__main__":
    main()
