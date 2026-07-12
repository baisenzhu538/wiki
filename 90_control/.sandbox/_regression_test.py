"""#159 阶段3 三连复验 — 全量基线 + 沙箱人为造债"""
import subprocess, sys, os, shutil

VAULT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(VAULT)

print("=" * 55)
print("#159 Phase 3: 基线回卷 + 三连复验")
print("=" * 55)

# ── 复验 1: 全量增量零返回 ──
print("\n[1/4] Full incremental lint...")
r = subprocess.run([sys.executable, '90_control/scripts/kdo_lint.py', '--incremental'],
    capture_output=True, text=True, timeout=120, encoding='utf-8', errors='replace')
output = r.stdout
new_errors = 0
for line in output.splitlines():
    if line.strip().startswith('New errors:'):
        try:
            new_errors = int(line.split(':')[1].strip())
        except: pass
print(f"  New errors: {new_errors}")
print(f"  PASS" if new_errors == 0 else f"  FAIL — {new_errors} new errors found")

# ── 复验 2: 三 bug 不复发 ──
print("\n[2/4] Bug regression...")
r2 = subprocess.run([sys.executable, '90_control/scripts/kdo_lint.py', '30_wiki/frameworks/framework-一堂-苦练基本功-总纲.md'],
    capture_output=True, text=True, timeout=30, encoding='utf-8', errors='replace')
o2 = r2.stdout + r2.stderr

f2_false = 'F2 BROKEN LINK' in o2 and 'framework-一堂-苦练基本功-总纲' in o2
dead_false = 'source_refs dead file' in o2 and '口述' in o2
crash = 'Traceback' in o2
print(f"  Bug1 (F2 Chinese id): {'PASS' if not f2_false else 'FAIL'}")
print(f"  Bug2 (source_refs :L): {'PASS' if not dead_false else 'FAIL'}")
print(f"  Bug3 (GBK crash): {'PASS' if not crash else 'FAIL'}")

# ── 复验 3: 沙箱人为造反向真债 ──
print("\n[3/4] Sandbox: manually create a reverse true debt...")
sandbox_dir = '90_control/.sandbox'
os.makedirs(sandbox_dir, exist_ok=True)

# Create card A (concept) that claims case B as evidence
card_a = os.path.join(sandbox_dir, 'concept-test-magic-number.md')
with open(card_a, 'w', encoding='utf-8') as f:
    f.write("""---
id: concept-test-magic-number
title: Test Magic Number Concept
type: concept
status: reviewed
created_at: 2026-07-12
updated_at: 2026-07-12
related:
  - '[[case-test-fupanying]]'
---
# Test Magic Number
This concept uses [[case-test-fupanying]] as evidence in the body.
""")

# Create card B (case) — does NOT have backlink to card A
card_b = os.path.join(sandbox_dir, 'case-test-fupanying.md')
with open(card_b, 'w', encoding='utf-8') as f:
    f.write("""---
id: case-test-fupanying
title: Test Case
type: case
status: reviewed
created_at: 2026-07-12
updated_at: 2026-07-12
related:
  - '[[concept-一堂-魔法数字]]'
---
# Test Case
This case demonstrates the magic number concept.
""")

r3 = subprocess.run([sys.executable, '90_control/scripts/kdo_lint.py', sandbox_dir],
    capture_output=True, text=True, timeout=30, encoding='utf-8', errors='replace')
o3 = r3.stdout + r3.stderr
has_reverse_debt = 'F2 MISSING BACKLINK' in o3 and 'concept-test-magic-number' in o3 and 'case-test-fupanying' in o3
print(f"  Reverse true debt caught: {'PASS' if has_reverse_debt else 'FAIL'}")
print(f"  (concept-test-magic-number -> case-test-fupanying: concept claims case as evidence, case must backlink)")

# ── 复验 4: 基线更新 + 签名数 ──
print("\n[4/4] Baseline update...")
r4 = subprocess.run([sys.executable, '90_control/scripts/kdo_lint.py', '--baseline'],
    capture_output=True, text=True, timeout=120, encoding='utf-8', errors='replace')

# Read new baseline count
import json
bl = json.load(open('90_control/.lint_baseline.json', 'r', encoding='utf-8'))
sigs = bl['error_count']
print(f"  Baseline signatures: {sigs}")
print(f"  Previous: 10380, Current: {sigs}, Delta: {sigs - 10380}")

# ── Cleanup sandbox test cards ──
os.remove(card_a)
os.remove(card_b)
shutil.rmtree(os.path.join(sandbox_dir, '__pycache__'), ignore_errors=True)

# ── Final ──
all_pass = (new_errors == 0 and not f2_false and not dead_false and not crash and has_reverse_debt)
print(f"\n{'=' * 55}")
print(f"Verdict: {'ALL PASS' if all_pass else 'SOME FAILED'}")
sys.exit(0 if all_pass else 1)
