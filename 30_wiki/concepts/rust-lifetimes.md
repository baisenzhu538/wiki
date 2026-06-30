---
id: rust-lifetimes
title: "Rust 生命周期：引用有效性的编译期保证"
type: concept
status: draft
domain:
  - rust
source_refs:
  - pending_archive
created_at: 2026-06-02
updated_at: 2026-06-02
---

# Rust 生命周期

## Summary

生命周期（lifetime）是 Rust 编译器用来追踪引用有效期的机制。大多数情况下生命周期被自动推导（lifetime elision），只有在函数签名涉及多个引用时才需要显式标注 `'a`。生命周期注解不改变代码逻辑——只帮助编译器验证引用的安全性。

## Claims

### 生命周期省略规则

编译器自动推断生命周期的三条规则：每个引用参数获得独立的生命周期、如果只有一个输入生命周期则赋给所有输出、如果 `&self` 存在则其生命周期赋给所有输出。

### 显式标注的使用场景

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

两个输入引用和一个输出引用——编译器无法自动判断返回值与哪个输入关联，需要 `'a` 标注。

### 结构体中的生命周期

当结构体持有引用时，必须标注生命周期以说明引用必须比结构体活得更久。这是 Rust 消除悬垂引用的核心机制。

## Constraints & Boundaries

- 生命周期标注对新手是最难理解的概念之一——它的语法（`'a`）看起来像泛型但含义完全不同
- 在涉及 trait object、闭包、异步代码时，生命周期标注会变得非常复杂
- Rust 2018 NLL 大幅减少了显式标注的需求
