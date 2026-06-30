"""Debug: trace state.json → SQLite migration step by step."""
import json, sqlite3, sys, os
sys.path.insert(0, r"C:\Users\Administrator\Knowledge Delivery OS 0.0.1")
os.chdir(r"C:\Users\Administrator\Knowledge Delivery OS 0.0.1")
from kdo.workspace import SQLiteState, SQLiteCollection, MVP_COLLECTIONS

os.chdir(r"C:\Users\Administrator\Desktop\wiki")

# Simulate what load_state does
state_file = ".kdo/state.json.migrated"
sqlite_file = ".kdo/state.sqlite.debug"

print("1. Load JSON...")
state_data = json.loads(open(state_file, encoding="utf-8").read())
print(f"   sources count in JSON: {len(state_data.get('sources', []))}")
print(f"   first source id: {state_data['sources'][0].get('id', 'NO ID')}")

print("2. Create SQLiteState with legacy_data...")
state = SQLiteState(sqlite_file, state_data)

print("3. Check sources after init...")
sources_col = state["sources"]
print(f"   type: {type(sources_col).__name__}")
print(f"   len: {len(sources_col)}")
first = next(iter(sources_col)) if len(sources_col) > 0 else None
if first:
    print(f"   first: {first.get('id', 'NO ID')[:40]}...")
else:
    print("   EMPTY!")

print("4. Check raw SQLite...")
db = sqlite3.connect(sqlite_file)
count = db.execute("SELECT COUNT(*) FROM kdo_records WHERE collection='sources'").fetchone()[0]
print(f"   SQLite sources count: {count}")
if count > 0:
    row = db.execute("SELECT record_id FROM kdo_records WHERE collection='sources' LIMIT 3").fetchall()
    print(f"   First 3 ids: {[r[0] for r in row]}")
db.close()

state.close()
