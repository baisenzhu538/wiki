---
title: Obsidian Git Multi-Device Sync Protocol
type: system
domain:
- kdo
status: draft
id: obsidian-git-sync-protocol
created_at: '2026-05-03'
updated_at: '2026-06-16'
related: null
tags:
- audience:manager
- scene:reference
- skill-level:intermediate
trust_level: medium
reviewed_by: Claude
review_date: '2026-05-03'
author: unknown
source_context: KDO internal record （原 legacy，已从 title/context/filename 推断为 src_20260501_58b6edef）
source_refs:
- pending_archive:src_20260501_58b6edef-obsidian-kdo-内容产出工作流-产品设计大纲
---
# Obsidian Git Multi-Device Sync Protocol

## Core Points

1. **Multi-device sync conflicts are caused by machine-specific files** (`.obsidian/workspace.json`, `.kdo/state.json`, plugin caches) being committed by Obsidian Git's auto-backup feature.
2. **The root solution is `.gitignore` + device reset**, not force-push cleanup after the fact. Prevention is cheaper than cure.
3. **Obsidian Git's default settings are dangerous for multi-device setups**: the "Stage untracked files" option causes `.gitignore` to be bypassed, and auto-push on multiple devices creates a conflict spiral.
4. **This protocol defines the standard operating procedure** for adding a new device to the KDO vault without introducing sync conflicts.
5. **If a conflict occurs, the recovery path is**: isolate the offending device → reset its local state → reconfigure Obsidian Git → resume sync.

### [Critique]

- src_unknown
- src_unknown
- src_unknown
- src_unknown

### [Synthesis]

- src_unknown
- src_unknown
- src_unknown
- src_unknown



## Standard Operating Procedure

### For New Devices

```
Step 1: Clone repository
    git clone <repo-url>

Step 2: Verify .gitignore includes machine configs
    cat .gitignore
    # Must contain:
    # .obsidian/
    # .claude/
    # .claudian/
    # .kdo/

Step 3: Open vault in Obsidian
    → .obsidian/ directory auto-generated with default settings
    → Git ignores it automatically

Step 4: Configure Obsidian Git (CRITICAL)
    Settings → Obsidian Git:
    [ ] Stage untracked files          ← MUST BE UNCHECKED
    [✓] Pull on startup                ← Recommended
    [✓] Auto backup                    ← OK
    [ ] Auto push                      ← OPTIONAL (see below)

Step 5: Test
    Edit a note → Trigger manual backup
    git show --stat HEAD
    # Should show ONLY the note file, NO .obsidian/ files
```

### For Existing Devices (Recovery)

If a device has already committed machine configs:

```
Step 1: Close Obsidian (stops auto-backup)

Step 2: Reset local git state
    git fetch origin
    git reset --hard origin/main

Step 3: Reopen Obsidian
    → .obsidian/ files regenerate from local cache
    → They remain untracked (ignored by .gitignore)

Step 4: Verify Obsidian Git settings
    [ ] Stage untracked files          ← MUST BE UNCHECKED
```

---

## Configuration Reference

### Obsidian Git Settings Checklist

| Setting | Recommended | Reason |
|---------|-------------|--------|
| **Auto backup** | ✅ On | Normal operation |
| **Auto push** | ⚠️ One device only | Prevents multi-device push conflicts |
| **Pull on startup** | ✅ On | Reduces divergence |
| **Stage untracked files** | ❌ Off | **CRITICAL**: Prevents `.gitignore` bypass |
| **Force push** | ❌ Off | Prevents history destruction |
| **Commit message template** | `vault backup: {{date}}` | Standardize |

### Git Config (Per-Device)

```bash
# Recommended: use a device-specific name for clarity
git config user.name "Name (DeviceName)"
git config user.email "email@example.com"
```

---

## Conflict Scenarios & Resolution

### Scenario A: Device pushes `.obsidian/` files

**Symptom**: `git log` shows commits with `.obsidian/workspace.json`, `.obsidian/plugins/...`

**Root Cause**: "Stage untracked files" is ON, or `.gitignore` missing `.obsidian/`

**Fix**:
1. On offending device: Uncheck "Stage untracked files"
2. On any device: `git rm --cached -r .obsidian/ .claude/ .claudian/ .kdo/`
3. Commit: "Remove machine configs from tracking"
4. All devices: `git pull` then `git reset --hard origin/main`

### Scenario B: History divergence (force-push loop)

**Symptom**: Device A force-pushes, Device B's auto-backup re-commits old files

**Fix**:
1. Stop all auto-backup temporarily
2. One authoritative device cleans remote: `git rm --cached -r .obsidian/ ...` + force-push
3. All other devices: `git fetch origin && git reset --hard origin/main`
4. Re-enable auto-backup ONLY on devices with correct settings

### Scenario C: New device clones and gets old machine configs

**Symptom**: Fresh clone contains `.obsidian/workspace-冲突-xxx.json`

**Fix**:
1. After clone: `git rm --cached -r .obsidian/ .claude/ .claudian/ .kdo/`
2. Commit + push
3. `.gitignore` ensures they won't return

---

## Verification Commands

```bash
# Check if any machine configs are still tracked
git ls-files | grep -E "^\.(obsidian|claude|claudian|kdo)/"
# Expected: no output

# Check latest commit contents
git show --stat HEAD
# Expected: NO .obsidian/ files

# Check .gitignore
cat .gitignore | grep -E "^\.(obsidian|claude|claudian|kdo)/"
# Expected: 4 lines
```

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-03 | v0.1 — Documented protocol after resolving multi-device conflict cycle |
