---
title: TinyFish Cookbook 架构模板（可迁移至 KDO）
type: template
status: draft
created_at: 2026-05-06
updated_at: 2026-05-06
---

# TinyFish Cookbook 架构模板

> 从 TinyFish cookbook 的 recipe 组织方式中提炼，适配到 KDO `40_outputs/capabilities/` 的可复用模板。

---

## 1. Recipe 标准化结构

### 1.1 目录结构

```
40_outputs/capabilities/playbooks/
└── <playbook-name>/                    ← 使用 kebab-case
    ├── README.md                       ← 必备：问题、方案、输出示例
    ├── script.py                       ← 必备：可独立运行的核心脚本
    ├── config.yaml                     ← 可选：配置参数（站点列表、API key 等）
    ├── demo.md                         ← 可选：效果展示（截图、录屏、演示数据）
    ├── integration.md                  ← 可选：如何接入 KDO 流水线
    └── tests/                          ← 可选：测试用例
        ├── test_basic.py
        └── test_edge_cases.py
```

### 1.2 README.md 模板

```markdown
# <Playbook 名称>

## 问题定义

解决什么问题？用一句话描述。

## 解决方案

用什么工具/技术，核心策略是什么。

## 数据流

```
输入 → [工具/处理] → 输出
```

## 输入

- 输入 1 描述
- 输入 2 描述

## 输出

- 输出 1 描述
- 输出 2 描述

## 快速开始

```bash
# 安装依赖
pip install -r requirements.txt

# 配置环境变量
export <API_KEY>=xxx

# 运行
python script.py
```

## 效果展示

见 [demo.md](demo.md)

## KDO 集成

见 [integration.md](integration.md)
```

### 1.3 integration.md 模板

```markdown
# KDO 集成说明

## 接入点

| KDO 阶段 | 接入方式 |
|---------|--------|
| capture | 作为素材收集源，输出到 00_inbox/links/ |
| ingest  | 调用 `kdo ingest` 处理输出 |
| enrich  | 可作为 enrich 步骤的外部数据来源 |
| produce | 可作为 produce 的素材输入 |

## 使用方式

### 方式 A：独立运行
```bash
python script.py --output ../00_inbox/links/
kdo ingest
```

### 方式 B：集成到 workflow
在 workflow 中增加一个 step，调用此 playbook。

## 注意事项
- 需要的 API key / 凭证
- 限速和配额
- 失败处理
```

---

## 2. 针对 KDO 的改进

### TinyFish cookbook vs KDO capabilities 对比

| 维度 | TinyFish | KDO 建议 |
|------|----------|----------|
| 组织单位 | Recipe（独立项目） | Playbook（符合 KDO 术语） |
| 演示方式 | Live Demo（Vercel） | Demo.md（截图/录屏） |
| 代码位置 | 独立 repo | `40_outputs/capabilities/` 下 |
| 集成 | n8n 工作流 | KDO workflow |
| 文档语言 | 英文 | 中文（优先） |

### KDO 增强点

1. **添加 `integration.md`** ← 明确如何接入 KDO 流水线
2. **添加 `config.yaml`** ← 配置与代码分离，方便复用
3. **添加 `tests/`** ← 确保 playbook 可靠性
4. **添加 `source_refs`** ← 每个输出标注数据来源，符合 KDO 双向溯源原则

---

## 3. 参考示例：从 tinyskills 迁移

TinyFish 的 `tinyskills` recipe 自动抓文档生成 SKILL.md，与 KDO 的 skill 系统直接对应。

### 迁移后的结构

```
40_outputs/capabilities/playbooks/
└── auto-skill-generator/
    ├── README.md          # 问题：自动抓取网页生成 KDO Skill
    ├── script.py          # 核心：TinyFish Fetch + LLM 生成 SKILL.md
    ├── config.yaml        # 站点列表、prompt 模板
    ├── demo.md            # 演示：从 GitHub repo 生成 Skill 的过程
    ├── integration.md   # 如何接入 KDO produce 阶段
    └── tests/
        ├── test_basic.py
        └── test_edge_cases.py
```

### 迁移后的输入输出

| | TinyFish 版本 | KDO 适配版本 |
|---|----------------|---------------|
| 输入 | GitHub repo URL + 文档链接 | 同左，或 KDO `00_inbox/links/` 中的 URL |
| 处理 | TinyFish Fetch + 自定义 LLM prompt | TinyFish Fetch + KDO 的统一 LLM 调用 |
| 输出 | 独立 SKILL.md 文件 | `40_outputs/capabilities/skills/<name>/SKILL.md` |
| 源引用 | 无 | `source_refs` 标注原始网站 |

---

## 4. 使用此模板

### 创建新 playbook

1. 复制模板结构
2. 填充 `README.md` 中的 `<占位符>`
3. 实现 `script.py` 核心逻辑
4. 运行测试 `python -m pytest tests/`
5. 记录到 `30_wiki/index.md`

### 审查清单

- [ ] 问题定义是否清晰？
- [ ] 输入/输出是否可量化？
- [ ] 脚本是否可独立运行？
- [ ] 是否有测试用例？
- [ ] 是否有 KDO 集成说明？
- [ ] 是否标注了 source_refs？

---

*模板版本: v0.1.0 | 来源: TinyFish cookbook 架构分析*
