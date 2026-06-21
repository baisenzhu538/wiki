---
name: self-evolution
description: Self-iterating evolution skill — periodic memory/self-check, error-to-skill闭环, user preference auto-learning. Triggered automatically after complex tasks, on user corrections, and via weekly cron.
version: 1.0.0
author: Hermes Agent
tags: [self-management, memory, skills, auto-improvement]
---

# Self-Evolution Skill

## 触发条件

当遇到以下情况时，自动触发自我迭代流程：
- 用户纠正了我的错误或偏好
- 完成任务后发现了更好的方法
- 使用某个skill时遇到未记录的pitfalls
- 用户说"记住"、"以后都这样"等指示
- 完成复杂任务（5+工具调用）后自检
- 每周定期自检（cron: `0 9 * * 1`，周一早上）

## 核心流程

### Phase 1: Memory 自检

检查记忆文件：
- `~/.hermes/memories/MEMORY.md` — 个人笔记（环境、工具、项目）
- `~/.hermes/memories/USER.md` — 用户画像（偏好、习惯、身份）

检查内容：
- 找出过时的条目（已不适用的事实）
- 找出冗余的条目（同一事实重复记录）
- 找出可以压缩的内容（长记录 → 精简摘要）
- 识别用户偏好是否完整捕获

### Phase 2: Skills 自检

对所有 skills 逐一检查：
- 能否正常加载（skill_view）
- 是否有未记录的pitfalls
- 是否有过时的命令/路径/参数
- 是否缺少用户偏好的特殊处理方式

### Phase 3: Error-to-Skill 闭环

遇到任何错误时，强制执行：
1. 立即记录错误根因到 skill 的 pitfalls
2. 如果skill缺失导致的问题，创建/更新skill
3. 如果是记忆偏差，更新memory

### Phase 4: 用户偏好自动学习

当用户表现出偏好时，自动执行 memory 更新：
- 语言风格偏好（简洁/详细/中文/英文）
- 工作流程偏好（一次性完成 vs 分步确认）
- 技术偏好（特定工具、框架、方案）
- 沟通偏好（称呼习惯、语气）

## 关键原则

1. **不打扰原则**: 自检在后台运行，不中断当前任务
2. **增量更新**: 只更新变化的局部，不重写全部
3. **可回滚**: 修改前记录原值，出问题可恢复
4. **用户知情**: 重大更新可询问用户确认

## 自检命令

```bash
# 查看当前记忆状态（优先检查 ~/.hermes/memories/ 目录）
cat ~/.hermes/memories/MEMORY.md 2>/dev/null || echo "MEMORY.md not found"
cat ~/.hermes/memories/USER.md 2>/dev/null || echo "USER.md not found"
# 旧版 memory.json 已废弃，如存在可忽略

# 查看 skills 列表
ls ~/.hermes/skills/

# 统计记忆文件行数
wc -l ~/.hermes/memories/MEMORY.md ~/.hermes/memories/USER.md

# 检查 skill 完整性：只检查叶子目录（排除分类目录和 scripts/references/templates 辅助文件夹）
find ~/.hermes/skills -maxdepth 3 -type d | while read dir; do
  if [ -z "$(find "$dir" -maxdepth 1 -type d | tail -n +2)" ] && [ ! -f "$dir/SKILL.md" ]; then
    echo "MISSING SKILL.md: $dir"
  fi
done

# 检查空的分类目录（无子 skill 的遗留目录）
for dir in ~/.hermes/skills/*/; do
  if [ -z "$(find "$dir" -maxdepth 1 -type d | tail -n +2)" ] && [ -z "$(find "$dir" -maxdepth 1 -type f)" ]; then
    echo "EMPTY DIR: $dir"
  fi
done
```

## 常见记忆问题模式

- **版本号过时**：项目/工具的版本号（如 KDO v0.0.1 → v0.1.0）容易过期，检查时优先关注带版本号的条目
- **架构描述过时**：系统架构、通信机制等描述随部署演进会失效（如"前期用飞书群聊作为总线"→"已部署 Hub：8765"）
- **偏好重复记录**：同一偏好可能在"沟通偏好"标题下和正文段落中各记录一次，需合并到单一位置

## 输出格式

自检完成后，输出简洁报告：
```
[自我迭代] Memory: 3项更新, 1项删除 | Skills: 2项修复 | 偏好: 新增1项
```

如果发现重大问题，主动提示用户确认。
