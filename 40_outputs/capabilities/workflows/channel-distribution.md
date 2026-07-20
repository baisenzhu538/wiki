# Channel Distribution Workflow

## Purpose

Expand the `kdo ship` step into a full channel decision and distribution pipeline. Don't just ship — choose the right channel, adapt format, publish, and track.

## Design Principle

```
One artifact → N channels, but don't spray blindly.

For each artifact:
  1. What's the primary channel?  (pick ONE)
  2. Can it be adapted to secondary channels?  (only if ROI > cost)
  3. What feedback does each channel generate?  (route back to cards)
```

## Trigger

When:
- An artifact passes validation and is ready to ship
- Content is marked `status: reviewed` by 欧阳锋
- 段王爷 receives a publish request from any agent

## Prerequisites

- Artifact has passed `kdo validate`
- Content reviewed by 欧阳锋 (not just validated, reviewed)
- Target audience is known
- 段王爷 has access to target channel credentials

---

## Steps

### Step 1 — Channel Selection Matrix

Not all content belongs on all channels. Use this matrix:

| Content Type | 飞书 Docx | 公众号 | 小红书 | 视频号 | Prezi | KDO Wiki |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|
| 方法论框架 (framework) | ✅ 主力 | ✅ 长文 | ❌ 太硬 | ❌ | 🟡 课程版 | ✅ 默认 |
| 案例研究 (case) | ✅ | ✅ | 🟡 拆成故事 | ❌ | ❌ | ✅ |
| 操作工具 (tool) | ✅ | ✅ 实操 | ✅ 清单版 | 🟡 口播版 | ❌ | ✅ |
| 暗知识 (dk) | ✅ | 🟡 | ✅ 金句版 | ✅ 口播版 | ❌ | ✅ |
| 视频资产 | ❌ | ❌ | ❌ | ✅ 主力 | ❌ | ❌ |
| 视觉资产 (图/PPT) | ✅ 附件 | 🟡 | ✅ | ❌ | ✅ 主力 | ❌ |

**Decision rules**:
- 飞书 Docx = default channel. If unsure, ship to 飞书 first.
- 小红书 needs format adaptation (short, visual, story-driven) — don't ship raw wiki articles
- 公众号 needs WeChat formatting — de-AI-ification mandatory
- 视频号 only for video assets — 洪七公 is upstream producer
- Prezi only for content with spatial structure (BP, 创始人手册, 长文可视化)

### Step 2 — Pre-Flight Checklist

Before publishing to any channel:

- [ ] Content reviewed by 欧阳锋 (`status: reviewed`)
- [ ] `kdo pre-submit` passed
- [ ] `kdo validate` returned 0
- [ ] `source_refs` traceable to raw sources
- [ ] Target channel is appropriate for this content type (see matrix)
- [ ] Content adapted to channel format (Step 3)

### Step 3 — Format Adaptation per Channel

#### 飞书 Docx
```
Raw Markdown → feishu-publish SKILL
  → Blocks conversion → create doc → batch write → set permissions → return URL
```
**Adaptation**: Minimal. Markdown→Blocks auto-converted. Rich text preserved.
**Skill**: `shared/feishu-publish/SKILL.md`

#### 公众号
```
Raw Markdown → content-production-polish (去AI味) → WeChat format → publish
```
**Adaptation**: Heavy. Must remove AI voice, add口语化转折, break long paragraphs, add CTA.
**Skill**: `shared/content-production-polish/SKILL.md`

#### 小红书
```
Raw content → xiaohongshu-positioning → short-form rewrite → visual pairing → publish
```
**Adaptation**: Heavy. Long-form → short-form. Text-heavy → visual-forward. Add hashtags, emoji, line breaks.
**Skill**: `skills/xiaohongshu-positioning/SKILL.md`

#### 视频号
```
Video asset → format check (MP4/H.264) → caption + description → publish
```
**Adaptation**: Format only. Content adaptation done upstream by 洪七公.
**Workflow**: `workflows/video-production-flow.md`

#### Prezi 无限画布
```
Raw content → spatial structure mapping → impress.js HTML gen → single-file output
```
**Adaptation**: Total. Content must have natural spatial structure (hierarchy/timeline/contrast).
**Skill**: `skill-duanwangye-prezi` (30_wiki card)

### Step 4 — Execute Publish

For each selected channel, in priority order (primary first, secondary if ROI positive):

```bash
# 1. Ship via KDO pipeline
kdo ship <artifact_id> --channel <channel> --url "<published_url>"

# 2. Record in delivery registry
# Auto-updated by kdo ship

# 3. For 飞书 specifically:
# Use shared/feishu-publish SKILL (MCP-based, no CLI dependency)
```

### Step 5 — Record and Track

After publishing:

```bash
kdo feedback "<observations>" --kind comments --artifact-id <artifact_id>
```

Track per channel:
| Channel | Feedback Source | Collection Method |
|------|------|------|
| 飞书 Docx | Comments, views | Manual check or MCP poll |
| 公众号 | Reads, shares, comments | WeChat backend |
| 小红书 | Likes, saves, comments | App analytics |
| 视频号 | Plays, likes, shares | Video backend |

### Step 6 — Route Feedback to Cards

Feedback doesn't stay in publishing — it flows back to knowledge:

```
Channel feedback
  → 段王爷 categorizes (bug/insight/gap/validation)
    → Route to domain owner:
      - 方法论 gap → 王语嫣 (new task)
      - 案例 validation → card related update
      - 表达问题 → content-production-polish iteration
      - 发布 bug → 黄药师 (infra fix)
```

---

## Channel-Specific Gotchas

| Channel | Gotcha | Mitigation |
|------|------|------|
| 飞书 Docx | 图片无法嵌入 | 消息配图替代 |
| 飞书 Docx | Convert API blocks顺序乱 | 手动构建block数组 |
| 公众号 | 外链受限 | 用"阅读原文"跳转 |
| 小红书 | 字数限制1000 | 拆成多篇或图文化 |
| 小红书 | 敏感词过滤 | 发布前跑敏感词检查 |
| Prezi | 单文件太大(>10MB) | 压缩图片，懒加载外部资源 |

---

## Exit Criteria

- [ ] At least primary channel published successfully
- [ ] Published URL recorded in delivery-registry
- [ ] Feedback record created
- [ ] Channel-appropriate format adaptation applied
- [ ] No unreviewed content shipped (欧阳锋 gate respected)

---

## Related

- `workflows/produce-and-ship-flow.md` — upstream: produce → validate
- `workflows/video-production-flow.md` — upstream: 洪七公 video production
- `shared/feishu-publish/SKILL.md` — 飞书 publishing engine
- `shared/content-production-polish/SKILL.md` — de-AI-ification for 公众号/小红书
- `agent-spec-duanwangye-publisher` — 段王爷 role spec
- `skill-duanwangye-kdo-pipeline` — KDO produce→validate→ship pipeline
- `skill-duanwangye-prezi` — Prezi 无限画布演示
