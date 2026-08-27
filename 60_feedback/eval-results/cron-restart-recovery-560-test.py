# #560 isolated live regression: restart-recovery of a recurring cron job.
# Scenario: job fires once -> scheduler stops -> misses >=2 fire points ->
# scheduler restarts -> job must fire ONCE (catch-up, no burst) and
# next_run_at must be fast-forwarded into the future.
import json
import os
import sys
import threading
import time
from datetime import datetime
from pathlib import Path

BASE = Path(r"C:/Users/Administrator/Desktop/wiki/_tmp/560-cron-recovery")
HOME = BASE / "home"
FIRE_LOG = BASE / "fire.log"
SCRIPT = BASE / "fire_script.py"

os.environ["HERMES_HOME"] = str(HOME)
sys.path.insert(0, r"C:/Users/Administrator/AppData/Local/hermes/hermes-agent")

from cron.jobs import create_job, get_job, load_jobs  # noqa: E402
from cron.scheduler_provider import InProcessCronScheduler  # noqa: E402

def log(msg):
    print(f"[{datetime.now().astimezone().isoformat(timespec='seconds')}] {msg}", flush=True)

def fire_count():
    if not FIRE_LOG.exists():
        return 0
    return len([l for l in FIRE_LOG.read_text().splitlines() if l.strip()])

# 1. create */1min cron job (no_agent: script IS the job, zero LLM)
job = create_job(
    prompt="560-recovery-probe",
    schedule="*/1 * * * *",
    name="560-recovery-probe",
    deliver="local",
    no_agent=True,
    script="probe.py",
)
log(f"job created id={job['id']} next_run_at={job['next_run_at']}")

def run_scheduler():
    stop = threading.Event()
    sched = InProcessCronScheduler()
    t = threading.Thread(target=sched.start, args=(stop,), kwargs={"interval": 10}, daemon=True)
    t.start()
    return stop, t

# 2. first run: wait for first fire (next minute boundary + tick)
stop, t = run_scheduler()
deadline = time.time() + 100
while fire_count() < 1 and time.time() < deadline:
    time.sleep(3)
assert fire_count() >= 1, "first fire never happened"
log(f"FIRST FIRE ok, count={fire_count()}, next_run_at={get_job(job['id'])['next_run_at']}")

# 3. simulate crash: stop scheduler, wait past >=2 fire points
stop.set(); t.join(timeout=20)
log("scheduler stopped (simulated crash); sleeping 130s to miss fire points")
time.sleep(130)
stuck = get_job(job["id"])["next_run_at"]
count_before = fire_count()
log(f"after outage: next_run_at={stuck} (stale), fires={count_before}")

# 4. restart: fresh scheduler instance, same store
stop2, t2 = run_scheduler()
deadline = time.time() + 60
recovered_at = None
while time.time() < deadline:
    if fire_count() > count_before:
        recovered_at = time.time()
        break
    time.sleep(2)
assert recovered_at, "FAIL: job did NOT fire after restart within 60s"
time.sleep(5)  # let mark_job_run persist
after = get_job(job["id"])
nxt = datetime.fromisoformat(after["next_run_at"])
now = datetime.now().astimezone()
log(f"RECOVERY FIRE ok after {recovered_at - (deadline - 60):.0f}s; next_run_at={after['next_run_at']} last_status={after.get('last_status')}")
assert nxt > now, f"FAIL: next_run_at not fast-forwarded: {nxt} <= {now}"

# 5. no burst: wait one more tick window, expect at most +1 normal fire at next boundary
c = fire_count()
time.sleep(25)
burst = fire_count() - c
log(f"post-recovery 25s: extra fires={burst} (0 expected; boundary fire may add 1 legitimately)")
assert burst <= 1, f"FAIL: burst firing detected (+{burst})"

stop2.set(); t2.join(timeout=20)
log("ALL ASSERTIONS PASSED")
print(json.dumps({
    "job_id": job["id"],
    "first_fire": True,
    "stale_next_run_at": stuck,
    "recovery_fire": True,
    "final_next_run_at": after["next_run_at"],
    "last_status": after.get("last_status"),
    "total_fires": fire_count(),
}, ensure_ascii=False, indent=1))
