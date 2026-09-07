# #677 tags 门禁激活 — 验证证据（2026-09-07 huangyaoshi）

## 交付
- KDO 仓 `kdo/pre_submit.py`：死代码提取为真函数 `_check_tags`（def 行系 8bc5645 批量提交丢失，原困在 `_check_aliases_has_source_name` 的 return 之后不可达）+ 接线 `run_pre_submit` + #498 词量口径 + 两态（`TAGS_HARD_DATE="2026-09-14"`，env `KDO_TAGS_HARD_DATE` 可提前）
- 新增回归 `tests/test_pre_submit_tags_gate.py` 15 例

## 验证记录
1. **TDD 红**：`ImportError: cannot import name 'TAGS_HARD_DATE'`——失败原因正确（函数从未成形）
2. **绿**：新套件 15 passed
3. **全量回归**：KDO 仓 `654 passed, 1 skipped`（修前基线 639+新增 15，零红）
4. **缺陷态复现（活体）**：两 dk 卡 09-06 18:31 前版本（git `4179de376^`，grep `^tags:` 计数 0/0 实锤缺陷态）→ `_check_tags` 双双 `warning | No tags found…（软期至 2026-09-14）`
5. **标杆卡**：`framework-meeting-iceberg-canvas` 走 `run_pre_submit` 接线路径 → tags 门禁 0 issue，passed=1 failed=0（另 3 条 issue 属 quote_verbatim/concept_crosscheck/quality_score 其他门禁，非本单）
6. **两态翻转**：`KDO_TAGS_HARD_DATE=2026-01-01` + `run_pre_submit` → severity=error、failed=2
7. **现行两 dk 卡**（09-06 18:31/18:42 backup 提交已补 tags：维度 4 条+核心词 3 条）→ 0 issue，不误报治理合规态

## kdo query 检索记录
- 本次为代码/配置/任务号类检索（宪法第六条 grep 许可类）：grep 定位 `pre_submit.py`/`tag-registry.yaml`/`tags-vocab-design.md`/`#498` 任务单/三张验收卡，均多命中
- 域知识词表口径直读真相源：`90_control/tags-vocab-design.md` §词量口径分卡型 + `90_control/tags-vocab/modeling.yaml`（#498 裁定原文）
- 未做 kdo query 语义检索：本单无域知识断言，规则依据全部溯源到上列受控文件（kdo query 0 命中风险不存在于本单范围）

## 口径裁定（供欧阳锋终审）
- **词量计数**：普通卡=全部条目（维度标签+内容词，标杆卡 6 条合规）；dk 卡=核心词（非 `:` 条目）1-3——不对称是因 registry 对 dk 另有 source 维度要求，若计入 1-3 上限则数学冲突（audience+scene+source-person+source-context-type ≥4>3）
- **原死代码 framework→method 检查不接线**：registry `method` 维度 `layer: chunk` + `labeling: auto`（chunk 级自动标注非卡作者职责）；实证 309 张 framework 卡仅 19 张带 `method:` 标签，且标杆卡（验收要求通过）无此标签
- **dk source 维度双通道**：tags 标签（registry 原义）或 frontmatter `source_person`/`source_context` 字段（新式卡实证承载，含 09-07 复审的 dk-AI知识库卡）任一满足
