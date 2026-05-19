import subprocess, json, sys
result = subprocess.run(
    [sys.executable, "-m", "kdo", "validate", "--v15", "--json"],
    capture_output=True, text=True, timeout=120, cwd=r"C:\Users\Administrator\Desktop\wiki"
)
data = json.loads(result.stdout)
print(f"Total: {data.get('total', '?')}")
print(f"Pass: {data.get('pass', '?')}")
print(f"Fail: {data.get('fail', '?')}")
print(f"Warn: {data.get('warn', '?')}")
