"""Lightweight file lock for KDO task queue coordination.

Usage:
    from queue_lock import QueueLock

    with QueueLock("production-queue"):
        # safely read/write queue files
        ...

    # Or manual acquire/release
    lock = QueueLock("production-queue")
    if lock.acquire():
        try:
            ...
        finally:
            lock.release()

CLI:
    python queue_lock.py check          # Check if lock is held
    python queue_lock.py acquire <name> # Acquire lock (blocking)
    python queue_lock.py release <name> # Release lock
    python queue_lock.py status         # List all locks and holders
"""

import json
import os
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

LOCK_DIR = Path(__file__).resolve().parent.parent / ".queue-locks"
LOCK_DIR.mkdir(parents=True, exist_ok=True)

TIMEOUT_SECONDS = 300  # 5-minute stale lock auto-expiry


class QueueLock:
    """Exclusive lock for a named KDO queue resource."""

    def __init__(self, name: str):
        self.name = name
        self.lockfile = LOCK_DIR / f"{name}.lock"
        self.holder_id = str(uuid.uuid4())[:8]
        self._held = False

    def acquire(self, timeout: float = 60.0) -> bool:
        """Try to acquire the lock, waiting up to *timeout* seconds."""
        deadline = time.time() + timeout
        while time.time() < deadline:
            if self._try_claim():
                self._held = True
                return True
            time.sleep(0.2)
        return False

    def release(self) -> bool:
        """Release the lock if currently held."""
        if not self._held:
            return False
        try:
            if self.lockfile.exists():
                data = json.loads(self.lockfile.read_text())
                if data.get("holder") == self.holder_id:
                    self.lockfile.unlink()
            self._held = False
            return True
        except Exception:
            return False

    def _try_claim(self) -> bool:
        """Attempt to claim the lock atomically."""
        try:
            # Check if lock exists and is valid
            if self.lockfile.exists():
                try:
                    data = json.loads(self.lockfile.read_text())
                    holder = data.get("holder", "")
                    acquired_at = data.get("acquired_at", "")
                    if acquired_at:
                        age = time.time() - datetime.fromisoformat(acquired_at).timestamp()
                        if age > TIMEOUT_SECONDS:
                            # Stale lock — break it
                            self.lockfile.unlink()
                        elif holder == self.holder_id:
                            return True  # Already held by us
                        else:
                            return False  # Held by someone else
                except (json.JSONDecodeError, KeyError, OSError):
                    self.lockfile.unlink()  # Corrupt lock — break it

            # Try to create lock file (atomic-ish via tmp + rename)
            tmp = self.lockfile.with_suffix(".tmp")
            payload = {
                "holder": self.holder_id,
                "name": self.name,
                "acquired_at": datetime.now(timezone.utc).isoformat(),
            }
            tmp.write_text(json.dumps(payload))
            os.replace(tmp, self.lockfile)  # Atomic on most platforms
            return True
        except OSError:
            return False

    def __enter__(self):
        if not self.acquire():
            raise TimeoutError(f"Could not acquire lock: {self.name}")
        return self

    def __exit__(self, *args):
        self.release()
        return False


def check_lock(name: str) -> dict | None:
    """"Return lock info if held, None if free."""
    lockfile = LOCK_DIR / f"{name}.lock"
    if not lockfile.exists():
        return None
    try:
        data = json.loads(lockfile.read_text())
        age = time.time() - datetime.fromisoformat(data["acquired_at"]).timestamp()
        if age > TIMEOUT_SECONDS:
            return None  # Stale
        return data
    except Exception:
        return None


def list_locks() -> list[dict]:
    """List all active locks."""
    locks = []
    for f in sorted(LOCK_DIR.glob("*.lock")):
        try:
            data = json.loads(f.read_text())
            age = time.time() - datetime.fromisoformat(data["acquired_at"]).timestamp()
            data["age_seconds"] = int(age)
            data["stale"] = age > TIMEOUT_SECONDS
            locks.append(data)
        except Exception:
            pass
    return locks


if __name__ == "__main__":
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"

    if cmd == "check":
        name = sys.argv[2] if len(sys.argv) > 2 else "production-queue"
        info = check_lock(name)
        print("HELD" if info else "FREE")
        if info:
            print(json.dumps(info, indent=2))

    elif cmd == "acquire":
        name = sys.argv[2] if len(sys.argv) > 2 else "production-queue"
        lock = QueueLock(name)
        if lock.acquire():
            print(f"ACQUIRED holder={lock.holder_id}")
        else:
            print("TIMEOUT")
            sys.exit(1)

    elif cmd == "release":
        name = sys.argv[2] if len(sys.argv) > 2 else "production-queue"
        lockfile = LOCK_DIR / f"{name}.lock"
        if lockfile.exists():
            lockfile.unlink()
            print("RELEASED")
        else:
            print("NOT_HELD")

    elif cmd == "status":
        locks = list_locks()
        if not locks:
            print("No active locks")
        for l in locks:
            mark = " [STALE]" if l["stale"] else ""
            print(f"  {l['name']}: holder={l['holder']} age={l['age_seconds']}s{mark}")

    else:
        print("Usage: queue_lock.py [check|acquire|release|status] [name]")
