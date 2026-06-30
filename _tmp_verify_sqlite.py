import sqlite3
db = sqlite3.connect(".kdo/state.sqlite")
sources = db.execute("SELECT COUNT(*) FROM kdo_records WHERE collection='sources'").fetchone()[0]
total = db.execute("SELECT COUNT(*) FROM kdo_records").fetchone()[0]
print(f"Sources: {sources}")
print(f"Total records: {total}")
# Show a sample
row = db.execute("SELECT record_id, data_json FROM kdo_records WHERE collection='sources' LIMIT 1").fetchone()
if row:
    print(f"Sample id: {row[0]}")
    print(f"Sample json (first 200 chars): {row[1][:200]}")
db.close()
