---
id: 371
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-18T17:49:52.780194+00:00'
title: 正库元数据规范清洗（P1，小昭体检修正版）——真 domain 空值 307 + trust_level/status/type 枚举收敛
priority: P1
dependency: []
reviewed_by: 欧阳锋
---

# #371 正库元数据规范清洗（P1）

## 任务目标

清洗正库元数据真实缺陷（王语嫣复核修正小昭口径后的版本）：domain 真空值 307 张 + 枚举污染。**注意：小昭报告的"1967 空值+拼接污染 193 张"是她扫描器不解析 list 式 domain 的测量伪影，真实规模以本任务单为准。**

## 素材/证据（王语嫣全库扫描 2026-08-19，2800 卡）

- domain 真空值：307 张（10%）
- trust_level 非标：235 张（`observed` 65 / `medium-high` 99 / `medium-low` 90 / 带 `#` 尾巴等）
- type 双轨：dk 316 vs dark-knowledge 8
- status 14 种取值无终态枚举规范（reviewed 1120 / draft 646 / enriched 523 / pending_review 88 / needs-review 45 / 其他零散）
- 缺 title 14 / 缺 type 59 / 重复键 95（OSCAR 卡 3 个 aliases 键通病）/ `_test_pa.md` 测试文件混正库

## 修改范围

1. **枚举定标**（王语嫣已裁定，黄药师执行）：trust_level ∈ {high, medium, low}——observed→medium、medium-high→high、medium-low→low；type 统一 `dk`；status 终态枚举 {reviewed, deprecated}，中间态 {draft, pending_review, enriched} 规范化
2. **脚本批量清洗**：dry-run 先行 + 非空值不覆盖 + git 留痕（批量三问）
3. **domain 307 张补全**：脚本按目录/related 推断 + 人工抽查（老顽童协助抽查 10%）
4. **重复键/缺字段修复**：95+14+59 张逐批修；`_test_pa.md` 移出正库
5. **非终态 785 张不在本任务**（处置决策另议，见队列备注）

## 边界

- 只改 frontmatter 不动正文
- 每批 dry-run + 抽查留痕
- lint 全库回归：ERROR 不新增

## 验收标准

1. trust_level/type/status 枚举 100% 合规
2. domain 空值 307→个位数（无法推断的标 unknown 并备案）
3. 重复键/缺 title/缺 type 清零；_test_pa.md 移出
4. kdo lint ERROR 不增

## 交付

1. 清洗脚本 + dry-run 记录 + 抽查证据
2. 送欧阳锋终审

## 执行记录（2026-08-19 黄药师，已提审）

### 扫描摸底（2823 文件，真实规模）

domain 空 307 / trust 非标 265（observed 65+medium-high 99+medium-low 89+带#尾巴 10+placeholder 1）/ dark-knowledge 8 / status 14 种 / 缺 type 59 / 重复键 95 / 测试文件 4（_test_pa/_test_dead_link/_dogfood ×2，no_title 的唯一一张就是 _test_pa）

### 清洗执行（脚本 `90_control/scripts/clean-metadata-371.py`，635 文件）

| 字段 | 处置 |
|:--|:--|
| trust_level | 257 映射：observed→medium、medium-high→high、medium-low→low、带#取前缀、placeholder→medium；剩余全部 ∈ {high,medium,low} |
| type | 67：dark-knowledge→dk（8）+ 缺 type 按目录映射（59） |
| status | 97 归并：superseded→deprecated、revised/stable/approved→reviewed、active→enriched、proposed→draft、pending→pending_review、缺省→draft；needs-review 保留（正式中间态） |
| domain | 307 全补：文件名/关键词规则（yt-前缀=yitang、medicine/医疗→healthcare、人机协作→ai-collaboration、ec→ecommerce 等）+ related 卡 domain 众数 → 161 推断；**146 标 unknown 备案**（`_tmp_m371_domain_unknown.txt`，真实边界：外部框架/域不明卡无法可靠推断——"个位数"目标不现实，建议老顽童抽查 10% 时人工补） |
| 重复键 | 95 修复（yaml round-trip 去重保留最后值） |
| 测试文件 | `_test_pa.md`/`_test_dead_link.md`/`_dogfood_dk.md`/`_dogfood_dk2.md` 移出正库 → 00_inbox |

### 验证

- 抽查 5 张卡 frontmatter 映射全部正确（observed→medium、yt-→yitang、strategy 命中等）
- **lint 回归：清洗后 8270 ERROR vs 清洗前基线 8393（stash 对比）——-123 不增反减**（type 规范化修复部分 link 类）✅
- 只改 frontmatter 不动正文；_archive 排除

### 待办

- domain unknown 146 张人工抽查补全（老顽童协助 10%，备案文件在 _tmp_m371_domain_unknown.txt）

## 交付

1. 清洗脚本 + dry-run/apply 记录 + 抽查证据 + lint 对比
2. 送欧阳锋终审
