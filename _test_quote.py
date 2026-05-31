import yaml

text = open("30_wiki/concepts/yt-decision-y-model.md", encoding="utf-8").read()
end = text.find("\n---\n", 4)
raw = text[4:end]
lines = raw.split("\n")

# Show hex dump of lines 74-79 (0-indexed: 73-78)
print("Hex dump of lines around error:")
for i in range(73, min(79, len(lines))):
    line = lines[i]
    hex_repr = " ".join(f"{ord(ch):04X}" for ch in line[:20])
    print(f"L{i+1} (indent={len(line)-len(line.lstrip())}): {hex_repr}...")

# Try to parse while skipping line 77 (the problematic - 负形利用 line)
print("\n\nTest: skip line 77...")
test_lines = lines[:76] + lines[78:]
test_fm = "\n".join(test_lines)
try:
    yaml.safe_load(test_fm)
    print("PARSED OK with line 77 skipped!")
except yaml.YAMLError as e:
    print(f"STILL FAILS: {e}")

# Try to parse with line 78 skipped
print("\nTest: skip line 78...")
test_lines = lines[:77] + lines[79:]
test_fm = "\n".join(test_lines)
try:
    yaml.safe_load(test_fm)
    print("PARSED OK with line 78 skipped!")
except yaml.YAMLError as e:
    print(f"STILL FAILS: {e}")
