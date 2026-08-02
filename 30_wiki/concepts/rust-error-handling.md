---
id: rust-error-handling
title: "Rust 错误处理：Result、? 与分层策略"
type: concept
status: draft
domain:
  - rust
aliases:
  - Rust错误处理：Result、?与分层策略
  - 与分层策略
  - 层策略
  - 错误处理
source_refs:
  - pending_archive
created_at: 2026-06-02
---

# Rust 错误处理

## Summary

Rust 没有异常——错误通过 `Result<T, E>` 类型显式传播。`?` 运算符在 `Ok` 时解包，在 `Err` 时提前返回并自动做类型转换。社区收敛到分层策略：库用 `thiserror` 暴露精确可匹配的错误枚举，应用层用 `anyhow` 快速聚合带上下文的错误链。

## Claims

### Result 与 ? 运算符

```rust
fn read_config(path: &str) -> Result<Config, std::io::Error> {
    let content = std::fs::read_to_string(path)?; // 失败时自动传播错误
    let config: Config = serde_json::from_str(&content)?;
    Ok(config)
}
```

`?` 替代了 Go 语言中反复写 `if err != nil { return err }` 的样板代码。

### 分层策略：thiserror + anyhow

**库层**：`thiserror` 派生宏自动生成 `Display`、`Error` trait 和 `From` 转换。调用方可以精确匹配错误类型做不同处理。

**应用层**：`anyhow::Result<T>` 接受任何实现了 `Error` trait 的类型。`.context("...")` 在每层调用栈添加人类可读的错误上下文，出错时打印完整的错误链。

### Option 与 Result 的分工

`Option<T>` 用于"值可能不存在"（不需要错误信息），`Result<T, E>` 用于"操作可能失败"（需要说明原因）。`.ok_or()` 将 Option 转为 Result，`.ok()` 将 Result 转为 Option（丢弃错误信息——谨慎使用）。

## Constraints & Boundaries

- thiserror 和 anyhow 是社区库，不是标准库——但它们已成为事实标准
- `Box<dyn Error>` 适合小项目原型，但在大型应用中丢失了错误类型信息
- 过度使用 `.unwrap()` 或 `.expect()` 等同于写潜在的 panic——应该只在"不可能失败"的场景使用
