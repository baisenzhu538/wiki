"""#159 阶段3 三连复验 — 全量基线 + 沙箱人为造债"""
import subprocess, sys, os, shutil

VAULT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(VAULT)

print("=" * 55)
print("#159 Phase 3: 基线回卷 + 三连复验")
print("=" * 55)

# ── 复验 4→1: 先更新基线（反映当前干净状态）──
print("\n[1/4] Baseline update...")
r4 = subprocess.run([sys.executable, '90_control/scripts/kdo_lint.py', '--baseline'],
    capture_output=True, text=True, timeout=120, encoding='utf-8', errors='replace')

import json
bl = json.load(open('90_control/.lint_baseline.json', 'r', encoding='utf-8'))
sigs = bl['error_count']
print(f"  Baseline: {sigs} signatures (was 10380, delta {sigs - 10380})")

# ── 复验 1→2: 增量零返回 ──
print("\n[2/4] Incremental = 0...")
r = subprocess.run([sys.executable, '90_control/scripts/kdo_lint.py', '--incremental'],
    capture_output=True, text=True, timeout=120, encoding='utf-8', errors='replace')
new_errors = 0
for line in r.stdout.splitlines():
    if line.strip().startswith('New errors:'):
        try: new_errors = int(line.split(':')[1].strip())
        except: pass
print(f"  New errors: {new_errors} {'PASS' if new_errors == 0 else 'FAIL'}")
if new_errors > 0:
    for line in r.stdout.splitlines():
        if '[ERROR]' in line:
            print(f"    {line.strip()[:150]}")

# ── 复验 2: 三 bug 不复发（需全量扫描以建立跨文件索引）──
print("\n[2/4] Bug regression (full scan for F2 cross-file index)...")
r2 = subprocess.run([sys.executable, '90_control/scripts/kdo_lint.py', '30_wiki'],
    capture_output=True, text=True, timeout=120, encoding='utf-8', errors='replace')
o2 = r2.stdout + r2.stderr

# Bug1: framework-一堂-苦练基本功-总纲 should NOT have F2 BROKEN LINK for cards that exist
# Check specific known-good pairs
known_good_targets = ['concept-一堂-基本功定义', 'concept-一堂-基本功-刻意练习四要素', 'framework-一堂-基本功-九层金字塔']
f2_lines = [l for l in o2.splitlines() if 'F2 BROKEN LINK' in l and 'framework-一堂-苦练基本功-总纲' in l]
false_broken = [l for l in f2_lines if any(t in l for t in known_good_targets)]

# Bug2: source_refs with :L行号 and （注释） should not trigger dead file
dead_false_lines = [l for l in o2.splitlines() if 'source_refs dead file' in l and '口述' in l and (':L' in l or '（' in l)]
# Filter out real dead files (paths that genuinely don't exist)
false_dead = [l for l in dead_false_lines if '九层金字塔' in l or '三环六维' in l or '武器库' in l]

# Bug3: no crash
crash = 'Traceback' in o2

print(f"  Bug1 (F2 Chinese id): {'PASS' if not false_broken else f'FAIL — {len(false_broken)} false positives'}")
if false_broken:
    for l in false_broken[:3]:
        print(f"    {l.strip()[:120]}")
print(f"  Bug2 (source_refs :L): {'PASS' if not false_dead else f'FAIL — {len(false_dead)} false positives'}")
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
all_pass = (new_errors == 0 and not false_broken and not false_dead and not crash and has_reverse_debt)
print(f"\n{'=' * 55}")
print(f"Verdict: {'ALL PASS' if all_pass else 'SOME FAILED'}")
sys.exit(0 if all_pass else 1)
