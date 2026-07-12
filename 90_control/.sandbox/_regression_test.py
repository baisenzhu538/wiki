"""三连复验 — 沙箱副本上验证三个 bug 不复发"""
import subprocess, sys, os

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# 1. Bug1+2: 沙箱卡 lint 不误报
r = subprocess.run([sys.executable, '90_control/scripts/kdo_lint.py', '90_control/.sandbox/test_card.md'],
    capture_output=True, text=True, timeout=30, encoding='utf-8', errors='replace')
output = r.stdout + r.stderr

has_F2_false = 'F2 BROKEN LINK' in output
has_dead_false = 'source_refs dead file' in output and '口述' in output
has_crash = 'Traceback' in output or 'UnicodeEncodeError' in output

print('=== Three-Bug Regression ===')
print(f'Bug1 (F2 Chinese id false positive): PASS' if not has_F2_false else f'Bug1: FAIL')
print(f'Bug2 (source_refs :L false positive): PASS' if not has_dead_false else f'Bug2: FAIL')
print(f'Bug3 (GBK crash): PASS' if not has_crash else f'Bug3: FAIL')
print()

# 2. Bug3: Full lint on sandbox
r2 = subprocess.run([sys.executable, '90_control/scripts/kdo_lint.py', '90_control/.sandbox'],
    capture_output=True, text=True, timeout=30, encoding='utf-8', errors='replace')
has_crash2 = 'Traceback' in (r2.stdout + r2.stderr)
print(f'Bug3 (full GBK): PASS' if not has_crash2 else f'Bug3 full: FAIL')

all_pass = not (has_F2_false or has_dead_false or has_crash or has_crash2)
print(f'\nVerdict: {"ALL PASS" if all_pass else "SOME FAILED"}')
sys.exit(0 if all_pass else 1)
