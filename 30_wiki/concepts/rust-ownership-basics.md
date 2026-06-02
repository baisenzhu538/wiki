---
id: rust-ownership-basics
title: "Rust 所有权基础：三条核心规则"
type: concept
status: draft
domain:
  - rust
tags:
  - "#domain/rust"
  - "#method/thinking-tool"
created_at: 2026-06-02
updated_at: 2026-06-02
---

# Rust 所有权基础

## Summary

Rust 的所有权系统是语言最独特的特性——在编译期保证内存安全，无需垃圾回收器。三条核心规则：每个值有且仅有一个所有者、值在所有者离开作用域时被释放、所有权可以通过移动（move）转移。

## Claims

### 规则一：每个值有且仅有一个所有者

```rust
let s = String::from("hello"); // s 是 "hello" 的所有者
let t = s;                      // 所有权从 s 移动到 t
// println!("{}", s);           // 编译错误：s 已经失效
```

**与 GC 语言的关键区别**：在 Java/Python 中，`t = s` 只是复制引用。在 Rust 中，这是一个**所有权转移**——原来的变量不再有效。这防止了双重释放（double free）和使用已释放内存（use-after-free）的 bug。

### 规则二：值在所有者离开作用域时被自动释放

```rust
{
    let s = String::from("hello");
    // s 在此作用域内有效
} // s 离开作用域，内存自动释放，无需 free() 或 GC
```

Rust 在编译期插入 drop 调用，类似于 C++ 的 RAII，但由编译器强制执行而不是依赖程序员记得。

### 规则三：同一时刻只能有一个可变引用或多个不可变引用

```rust
let mut s = String::from("hello");
let r1 = &s;     // 不可变引用，OK
let r2 = &s;     // 多个不可变引用，OK
let r3 = &mut s; // 编译错误：不能同时拥有可变和不可变引用
```

这条规则在编译期消除了数据竞争（data race）——Rust 的 borrow checker 保证不会出现一个线程在写、另一个线程在读的并发 bug。

## Constraints & Boundaries

- 所有权规则不适用于实现了 `Copy` trait 的类型（如整数、布尔值），它们使用复制语义而非移动语义
- 学习曲线陡峭：新手在借用检查器（borrow checker）上的挣扎是 Rust 入门的最大障碍
- 不适合快速原型开发——所有权约束增加了前期设计成本
