> 王语嫣对黄药师跨域审计脚本 `90_control/scripts/cross_domain_audit.py` 的验收反馈。
> 王语嫣铁律：本文件只写入 `60_feedback/`，不污染脚本代码；代码修复由黄药师负责。

---

## 脚本交付状态

| 项目 | 状态 |
|:-----|:-----|
| 脚本文件 | 已交付：`90_control/scripts/cross_domain_audit.py` |
| 报告文件 | 已生成：`60_feedback/audit/cross-domain-link-report.md` |
| 运行是否正常 | ❌ 不正常—— frontmatter 解析存在严重 bug |
| 当前报告可信度 | 🔴 低——报告中的 784 个异常几乎全部来自解析失败 |

---

## 发现的 Bug

### 现象

运行脚本后报告：
- 总检查卡数：1959
- 异常卡数：784
  - Rule 1（framework/tool 未跨域）：777 张
  - Rule 2（bridge 卡目标域覆盖不足）：5 张
  - Rule 3（domain digest 链接不足）：2 个

其中 **5 张 bridge 卡全部被判定为“已覆盖：无”**，包括 `framework-ai-accelerated-strategy-cycle`——而这张卡的 `related` 明确包含 `[[lean-startup-domain-digest]]`、`[[strategy-domain-digest]]`、`[[ai-collaboration-domain-digest]]` 等跨域链接。

### 根因

脚本使用自定义的 `parse_frontmatter()` 函数解析 YAML frontmatter，而不是标准 YAML 解析器。该自定义解析器**无法解析多行列表格式**（如下）：

```yaml
related:
- "[[framework-lean-false-model]]"
- "[[framework-strategy-brm]]"
- "[[strategy-domain-digest]]"
```

导致 `related`、`domain`、`source_refs` 等列表字段全部被解析为空列表 `[]`。

### 验证

```python
# 自定义解析器（脚本当前逻辑）
from cross_domain_audit import parse_frontmatter
with open('30_wiki/frameworks/framework-ai-accelerated-strategy-cycle.md') as f:
    fm = parse_frontmatter(f.read())
print(fm.get('related'))  # → []
print(fm.get('domain'))   # → []

# 标准 YAML 解析器
import yaml
with open('30_wiki/frameworks/framework-ai-accelerated-strategy-cycle.md') as f:
    fm = yaml.safe_load(f.read().split('---', 2)[1])
print(fm.get('related'))  # → 9 个有效链接
print(fm.get('domain'))   # → ['strategy', 'lean-startup', 'ai-collaboration', 'yitang']
```

---

## 影响评估

| 影响 | 说明 |
|:-----|:-----|
| 报告不可用 | 当前 `cross-domain-link-report.md` 中的 784 个异常几乎全部失真 |
| bridge 卡验收被误导 | 5 张 bridge 卡被错误判定为未覆盖目标域 |
| Rule 1 数字夸大 | 777 张 framework/tool 卡中，绝大多数可能已有跨域 related，只是未被解析 |
| 无法作为生产门禁 | 在修复前，该脚本不能用于阻断卡片入库 |

---

## 修复建议

### 必选修复

将 `parse_frontmatter()` 替换为 `yaml.safe_load()`：

```python
import yaml

def parse_frontmatter(text: str) -> dict | None:
    if not text.startswith("---"):
        return None
    end = text.find("---", 3)
    if end == -1:
        return None
    try:
        return yaml.safe_load(text[3:end]) or {}
    except yaml.YAMLError:
        return None
```

### 建议同时优化

1. **编码声明**：脚本 shebang 后添加 `# -*- coding: utf-8 -*-`，避免 Windows 终端输出中文乱码。
2. **domain 判定增强**：当前 `domain_of()` 只取 `domain` 列表第一项。对于多域卡（如 `framework-lean-false-model` 的 `domain: [strategy, yitang, product]`），第一项可能无法代表其主要归属。建议支持“主域”字段或取多项。
3. **domain digest 的域识别**：`strategy-domain-digest.md` 当前 `domain: [yitang]`，导致它被识别为 yitang 而非 strategy。建议 domain digest 的域应与其名称一致（`strategy`），或在 frontmatter 中显式标注。
4. **报告增加调试样本**：输出前打印 3-5 张卡的解析结果，便于快速发现解析失败。

---

## 对当前管线的处理建议

1. **暂停将本脚本作为验收门禁**，直到修复完成并重新验证；
2. **当前 `cross-domain-link-report.md` 应标注为“因解析 bug 失效，待重新生成”**；
3. **bridge 卡的真实跨域覆盖情况**：在王语嫣人工抽检中，`framework-ai-accelerated-strategy-cycle` 和 `framework-lean-pivot-decision` 的 related 网络覆盖目标域，暂不因脚本误报而退回；
4. 黄药师修复脚本后，重新运行并生成新报告，再由王语嫣复核一次 bridge 卡覆盖情况。

---

*诊断人：王语嫣 | 日期：2026-06-25*
