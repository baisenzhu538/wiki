---
id: rust-borrowing-references
title: "Rust 借用与引用：不转移所有权的访问"
type: concept
status: draft
domain:
  - rust
source_refs:
  - pending_archive
created_at: 2026-06-02
updated_at: 2026-06-02
---

# Rust 借用与引用

## Summary

借用（borrowing）允许在不转移所有权的情况下访问值。`&T` 创建不可变引用（可同时存在多个），`&mut T` 创建可变引用（同一时刻只能存在一个）。借用检查器在编译期验证这些规则，消除悬垂指针和数据竞争。

## Claims

### 不可变借用：共享读取

```rust
fn print_len(s: &String) {
    println!("{}", s.len()); // 只读访问，不获取所有权
}
let s = String::from("hello");
print_len(&s); // 借给函数，s 仍然有效
println!("{}", s); // OK
```

### 可变借用：独占写入

```rust
fn append(s: &mut String) {
    s.push_str(" world");
}
let mut s = String::from("hello");
append(&mut s); // 可变借用
// 在 append 返回后，可变借用的独占性结束
let r = &s;     // 现在可以不可变借用了
```

### 借用规则的工程意义

这些规则不仅防止内存错误——它们从根本上改变了并发编程模型。Rust 的 `Send` 和 `Sync` trait 自动推导类型是否可以在线程间安全传输，不需要程序员手动加锁或标注。

## Constraints & Boundaries

- 借用检查器在复杂数据结构（如图、双向链表）上会变得极难满足——这是 Rust 社区公认的痛点
- NLL（Non-Lexical Lifetimes）从 Rust 2018 开始放宽了部分限制
- `RefCell` 和 `Mutex` 提供了运行时借用检查的逃生舱
