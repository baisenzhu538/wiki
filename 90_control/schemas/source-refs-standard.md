# source_refs 引用格式规范

## 三类来源

KDO 知识卡的 `source_refs` 支持三种引用格式：

### 1. Vault 内文件路径

```yaml
source_refs:
  - "00_inbox/一堂-商业预判课-Truman-口述.txt"
  - "10_raw/sources/src_20260510_4a74b6bf-xxx.md"
```

用于：inbox 原始素材、已 ingest 的 source 文件、OCR 输出文件。

### 2. 出版物（书籍/论文/报告）

```yaml
source_refs:
  - "Rasiel, E. (1999). *The McKinsey Way*. McGraw-Hill."
  - "Minto, B. (2009). *The Pyramid Principle: Logic in Writing, Thinking, & Problem Solving*. 3rd ed. FT Press."
  - "Christensen, C. (1997). *The Innovator's Dilemma*. Harvard Business Review Press."
  - "Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux."
  - "Taleb, N. N. (2007). *The Black Swan*. Random House."
```

格式：`Author, I. (Year). *Title*. Edition. Publisher.`

用于：经典商业文献、学术著作、行业报告。所有出版物引用前，必须在 `10_raw/literature/README.md` 中登记。

### 3. URL

```yaml
source_refs:
  - "https://arxiv.org/abs/2303.08774"
  - "https://www.mckinsey.com/..."
```

用于：网页文章、在线报告、arXiv 论文。URL 引用需标注 `captured_at` 日期（网页可能失效）。

---

## 规则

1. **格式优先**：出版物引用必须使用标准学术格式（Author, Year, Title, Publisher），不要自由发挥
2. **先去重**：引用前检查 `10_raw/literature/README.md` 是否已有同书引用，确保引用格式一致
3. **溯源可查**：卡片正文中引用出版物时，标注具体章节/页码（如 "Minto, Ch.2" 或 "Kahneman, p.109"）
4. **混合引用**：一张卡可以同时引用 vault 文件路径和出版物
5. **`bridges_to` 与 `source_refs` 的区别**：
   - `source_refs` = 这张卡内容的信息来源
   - `bridges_to` = 这张卡连接到的其他知识体系/框架（不是来源，是桥接目标）
