# -*- coding: utf-8 -*-
"""#613 补齐：status=reviewed 但 reviewed_by=pending/待审 的元数据残留修复。
判定与验证一律 yaml.safe_load（E017 禁正则解析 frontmatter）；文本层面只做行级最小改动。
只动 frontmatter 三字段：reviewed_by / review_date / grade（有实证才加）。"""
import io, sys, json
import yaml

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
ROOT = r"C:\Users\Administrator\Desktop\wiki"

# (path, 期望当前reviewed_by, 补review_date(None=已有不动), 补grade(None=不加), 终审佐证)
FIXES = [
    # ── #586 批（PASS A- 2026-09-01 07:45 欧阳锋，task_20260901_laowantong-candy-collection-batch 返工复审）──
    ("30_wiki/cases/case-jovida-ai-life-coach.md", "pending", "2026-09-01", "A-", "#586 PASS A- 2026-09-01（commit 61e755cc5 落盘）"),
    ("30_wiki/concepts/concept-agent-university.md", "pending", "2026-09-01", "A-", "#586 PASS A- 2026-09-01（commit faa13f1ff 返工修复）"),
    ("30_wiki/concepts/concept-brooks-three-lies-culture.md", "pending", "2026-09-01", "A-", "#586 PASS A- 2026-09-01（commit faa13f1ff）"),
    ("30_wiki/dark-knowledges/dk-brooks-cost-of-knowing.md", "pending", "2026-09-01", "A-", "#586 PASS A- 2026-09-01（commit faa13f1ff）"),
    ("30_wiki/dark-knowledges/dk-koupen-decision-tiering-compromise.md", "pending", "2026-09-01", "A-", "#586 PASS A- 2026-09-01（commit 130366e68）"),
    ("30_wiki/frameworks/framework-lobster-opt-one-person-team.md", "pending", "2026-09-01", "A-", "#586 PASS A- 2026-09-01（commit faa13f1ff）"),
    ("30_wiki/frameworks/framework-muse-ai-full-map-v1.md", "pending", "2026-09-01", "A-", "#586 PASS A- 2026-09-01（commit faa13f1ff；#611 终审发现源头卡）"),
    ("30_wiki/methods/method-anthropic-skill-design-patterns.md", "pending", "2026-09-01", "A-", "#586 PASS A- 2026-09-01（commit 130366e68）"),
    ("30_wiki/methods/method-key-assumption-abcd.md", "pending", "2026-09-01", "A-", "#586 PASS A- 2026-09-01（commit 130366e68）"),
    ("30_wiki/methods/method-obsidian-km-camp.md", "pending", "2026-09-01", "A-", "#586 PASS A- 2026-09-01（commit bddee1fa0）"),
    ("30_wiki/methods/method-spin-linking-sales-marketing.md", "pending", "2026-09-01", "A-", "#586 PASS A- 2026-09-01（commit 6ea1f8acc）"),
    ("30_wiki/tools/tool-ai-koupen-training-partner-design.md", "pending", "2026-09-01", "A-", "#586 PASS A- 2026-09-01（commit 130366e68）"),
    # ── 2026-06-28 批（review_date 已在，仅补 reviewed_by；无字母 grade 实证不加）──
    ("30_wiki/tools/tool-yitang-best-practice-as-golden-finger.md", "pending", None, None,
     "task_20260627_laowantong-deliberate-practice-cards 终审 11 卡全过（欧阳锋，review_date 2026-06-28 在任务单）"),
    ("30_wiki/tools/tool-yitang-channel-industrialization-node-design.md", "pending", None, None,
     "review_20260628_ouyangfeng-channel-growth 25 卡 conditional pass，已执行动作含 reviewed_by→欧阳锋/review_date→2026-06-28"),
    ("30_wiki/tools/tool-yitang-channel-scan-cheat-sheet.md", "pending", None, None,
     "review_20260628_ouyangfeng-channel-growth 25 卡 conditional pass，同上"),
    # ── reviewed_by=待审 批（同 E018 缺陷类；均有任务单终审 PASS A- 佐证）──
    ("30_wiki/frameworks/framework-ai-sales-collaboration.md", "待审", "2026-08-16", "A-", "task_20260815_laowantong-spin-ai-sales-cards 终审 PASS A- 2026-08-16（7 卡清单 #1）"),
    ("30_wiki/frameworks/framework-sales-funnel-full.md", "待审", "2026-08-16", "A-", "同上（#2）"),
    ("30_wiki/tools/tool-sales-objection-dilution.md", "待审", "2026-08-16", "A-", "同上（#3）"),
    ("30_wiki/dark-knowledges/dk-sales-demand-mining-is-company-task.md", "待审", "2026-08-16", "A-", "同上（#4）"),
    ("30_wiki/dark-knowledges/dk-sales-big-deal-vs-small-deal.md", "待审", "2026-08-16", "A-", "同上（#5）"),
    ("30_wiki/dark-knowledges/dk-customers-hate-ai.md", "待审", "2026-08-16", "A-", "同上（#6）"),
    ("30_wiki/tools/tool-candy-sales-recruiting.md", "待审", "2026-08-16", "A-", "task_20260815_laowantong-candy-sales-recruiting 终审 PASS A- 2026-08-16"),
    ("30_wiki/agent-specs/agent-spec-fengqingyang-observer.md", "待审", "2026-08-22", "A-", "task_20260822_laowantong-fengqingyang-agent-spec 终审 PASS/A- 2026-08-22（交付物=本卡）"),
]

# ── 返工轮 2（2026-09-02 终审 FAIL P0-1 补扫）：reviewed_by=待审 且 review_date 有值的 40 张逐张排查。
# 33 张有卡级终审佐证 → 补齐 reviewed_by→欧阳锋 + grade（review_date 已在卡且与终审日一致，不动）；
# 7 张无卡级终审佐证（06-19 批 4 + 07-08 批 3，review_date 系生产者创建日自填）→ 不改，并入上报王语嫣清单。
EV_SPIN = "task_20260816_laowantong-baozhashidiaochan-wave1.md §Wave 2/3 终审记录 PASS A- 2026-08-16 欧阳锋（爆炸式调研三波 20 卡收官：Wave1 五卡 A- + Wave2 七卡 + Wave3 八 dk，卡 id 逐一命中）"
EV_HTKP = "task_20260804_wangyuyan-how-to-know-a-person-cards.md §终审记录 PASS A 2026-08-09 欧阳锋（覆盖率 12/12：2 framework+3 tool+4 dk+2 case+1 bridge，卡 id 逐一命中）"
FIXES_R2 = [
    # ── 2026-08-16 批 20 张（爆炸式调研三波，PASS A-）──
    ("30_wiki/concepts/concept-open-a-document.md", "待审", None, "A-", EV_SPIN + "（Wave1）"),
    ("30_wiki/concepts/concept-research-saturation-coverage.md", "待审", None, "A-", EV_SPIN + "（Wave1）"),
    ("30_wiki/frameworks/framework-baozhashidiaochan-five-step.md", "待审", None, "A-", EV_SPIN + "（Wave1）"),
    ("30_wiki/frameworks/framework-r-type-research-partner-five-state.md", "待审", None, "A-", EV_SPIN + "（Wave1）"),
    ("30_wiki/tools/tool-nine-character-mantra-14-strategies.md", "待审", None, "A-", EV_SPIN + "（Wave1）"),
    ("30_wiki/cases/case-4000-titles-ten-strategies.md", "待审", None, "A-", EV_SPIN + "（Wave2）"),
    ("30_wiki/cases/case-ai-learning-series-modeling.md", "待审", None, "A-", EV_SPIN + "（Wave2）"),
    ("30_wiki/cases/case-design-principles-90.md", "待审", None, "A-", EV_SPIN + "（Wave2）"),
    ("30_wiki/cases/case-leo-lubricant-dealer-research.md", "待审", None, "A-", EV_SPIN + "（Wave2）"),
    ("30_wiki/cases/case-opc-128-directions.md", "待审", None, "A-", EV_SPIN + "（Wave2）"),
    ("30_wiki/frameworks/framework-ai-human-70-30-division.md", "待审", None, "A-", EV_SPIN + "（Wave2）"),
    ("30_wiki/frameworks/framework-ai-report-value-ladder-l1-l6.md", "待审", None, "A-", EV_SPIN + "（Wave2）"),
    ("30_wiki/dark-knowledges/dk-research-ai-no-time-concept.md", "待审", None, "A-", EV_SPIN + "（Wave3）"),
    ("30_wiki/dark-knowledges/dk-research-classification-mece-table.md", "待审", None, "A-", EV_SPIN + "（Wave3）"),
    ("30_wiki/dark-knowledges/dk-research-important-things-must-do.md", "待审", None, "A-", EV_SPIN + "（Wave3）"),
    ("30_wiki/dark-knowledges/dk-research-ranklist-replaces-model.md", "待审", None, "A-", EV_SPIN + "（Wave3）"),
    ("30_wiki/dark-knowledges/dk-research-sampling-correction-three-rounds.md", "待审", None, "A-", EV_SPIN + "（Wave3）"),
    ("30_wiki/dark-knowledges/dk-research-saturation-self-proof.md", "待审", None, "A-", EV_SPIN + "（Wave3）"),
    ("30_wiki/dark-knowledges/dk-research-scavenger-vs-architect.md", "待审", None, "A-", EV_SPIN + "（Wave3）"),
    ("30_wiki/dark-knowledges/dk-research-total-anchor-private-library.md", "待审", None, "A-", EV_SPIN + "（Wave3）"),
    # ── 2026-08-09 批 13 张（人域"看见"支柱 12 卡 PASS A + pipeline 卡补审 PASS(条件) A-）──
    ("30_wiki/frameworks/framework-how-to-know-a-person.md", "待审", None, "A", EV_HTKP + "（清单 #1）"),
    ("30_wiki/frameworks/framework-big-five-personality.md", "待审", None, "A", EV_HTKP + "（清单 #2）"),
    ("30_wiki/tools/tool-illuminator-vs-diminisher.md", "待审", None, "A", EV_HTKP + "（清单 #3）"),
    ("30_wiki/tools/tool-narrative-thinking-user-insight.md", "待审", None, "A", EV_HTKP + "（清单 #4）"),
    ("30_wiki/tools/tool-empathy-practice.md", "待审", None, "A", EV_HTKP + "（清单 #5）"),
    ("30_wiki/dark-knowledges/dk-emotional-value-premium.md", "待审", None, "A", EV_HTKP + "（清单 #6）"),
    ("30_wiki/dark-knowledges/dk-agreeableness-double-edged.md", "待审", None, "A", EV_HTKP + "（清单 #7）"),
    ("30_wiki/dark-knowledges/dk-emotional-value-high-bar.md", "待审", None, "A", EV_HTKP + "（清单 #8）"),
    ("30_wiki/dark-knowledges/dk-narrative-choice-theory.md", "待审", None, "A", EV_HTKP + "（清单 #9）"),
    ("30_wiki/cases/case-ai-pet-emotional-product.md", "待审", None, "A", EV_HTKP + "（清单 #10）"),
    ("30_wiki/cases/case-shuishui-business-insight.md", "待审", None, "A", EV_HTKP + "（清单 #11）"),
    ("30_wiki/bridges/bridge-how-to-know-person-to-business.md", "待审", None, "A", EV_HTKP + "（清单 #12）"),
    ("30_wiki/workflows/workflow-kdo-agent-production-pipeline.md", "待审", None, "A-",
     "task_20260809_laowantong-agent-production-pipeline.md §补审记录 PASS(条件) A- 2026-08-09 欧阳锋（O3 实测六项全过，E018 补确认非自标）"),
]

# 轮次选择：轮 1 已应用（2026-09-02 09:2x，见 fix-result.json 首轮记录）；本脚本复跑默认执行轮 2。
ACTIVE_FIXES = FIXES_R2

def load_fm(text):
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return None, None, None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines, i, yaml.safe_load("".join(lines[1:i]))
    return None, None, None

results = []
for rel, expect_rb, new_rd, new_grade, evidence in FIXES:
    path = ROOT + "\\" + rel.replace("/", "\\")
    with open(path, "r", encoding="utf-8", newline="") as f:
        text = f.read()
    lines, end_i, fm = load_fm(text)
    assert fm is not None, f"{rel}: 无 frontmatter"
    cur_rb = fm.get("reviewed_by")
    assert str(cur_rb).strip() == expect_rb, f"{rel}: reviewed_by={cur_rb!r} 不符预期 {expect_rb!r}，跳过"
    assert fm.get("status") == "reviewed", f"{rel}: status 非 reviewed"
    changed = []
    for j in range(1, end_i):
        key = lines[j].split(":", 1)[0].strip()
        if key == "reviewed_by":
            eol = "\r\n" if lines[j].endswith("\r\n") else "\n"
            lines[j] = f"reviewed_by: 欧阳锋{eol}"
            changed.append("reviewed_by→欧阳锋")
            insert_at = j + 1
            break
    if new_rd and not fm.get("review_date"):
        eol = "\r\n" if lines[insert_at - 1].endswith("\r\n") else "\n"
        lines.insert(insert_at, f"review_date: '{new_rd}'{eol}")
        changed.append(f"review_date+={new_rd}")
        insert_at += 1
        end_i += 1
    if new_grade and not fm.get("grade"):
        eol = "\r\n" if lines[insert_at - 1].endswith("\r\n") else "\n"
        lines.insert(insert_at, f"grade: {new_grade}{eol}")
        changed.append(f"grade+={new_grade}")
        end_i += 1
    new_text = "".join(lines)
    # 写后自检：yaml.safe_load 复解析确认字段生效且 YAML 合法
    _l, _e, fm2 = load_fm(new_text)
    assert fm2["reviewed_by"] == "欧阳锋", f"{rel}: 写后自检 reviewed_by 失败"
    if new_rd:
        assert str(fm2.get("review_date")).strip("'") == new_rd, f"{rel}: 写后自检 review_date 失败"
    if new_grade:
        assert fm2.get("grade") == new_grade, f"{rel}: 写后自检 grade 失败"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(new_text)
    results.append({"path": rel, "changed": changed, "evidence": evidence})
    print(f"✅ {rel}: {', '.join(changed)}")

print(f"\n共修复 {len(results)}/{len(FIXES)} 张")
with open(ROOT + r"\_tmp\613-fix-result.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
