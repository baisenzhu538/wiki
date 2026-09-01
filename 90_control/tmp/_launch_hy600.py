import subprocess, time
prompt = open(r'C:\Users\Administrator\Desktop\wiki\90_control\tmp\_prompt_hy600_601.txt', encoding='utf-8').read()
DETACHED = 0x00000008 | 0x00000200  # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP
log = open(r'C:\Users\Administrator\Desktop\wiki\logs\hy-600-601-headless.log', 'ab')
p = subprocess.Popen(
    [r'C:\Users\Administrator\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe',
     '-m', 'hermes_cli.main', '-p', 'huangyaoshi', '-z', prompt],
    cwd=r'C:\Users\Administrator\Desktop\wiki',
    stdout=log, stderr=log,
    creationflags=DETACHED,
)
print(f"proc_hy600_{p.pid} started {time.strftime('%H:%M:%S')}")
