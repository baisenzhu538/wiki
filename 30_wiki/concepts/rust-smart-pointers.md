---
id: rust-smart-pointers
title: "Rust 智能指针：超越引用的所有权管理"
type: concept
status: draft
domain:
  - rust
aliases:
  - Rust智能指针：超越引用的所有权管理
  - 引用的所有权管理
  - 智能指针
  - 超越引用的所有权管理
source_refs:
  - pending_archive
created_at: 2026-06-02
updated_at: 2026-06-02
---

# Rust 智能指针

## Summary

当所有权和借用规则无法满足需求时，Rust 提供了智能指针作为逃生舱。`Box<T>` 提供堆分配，`Rc<T>` 提供引用计数共享所有权，`RefCell<T>` 将借用检查推迟到运行时。三者组合（`Rc<RefCell<T>>`）可以实现类似 GC 语言的灵活共享可变访问。

## Claims

### Box<T>：堆上分配

最简单的智能指针。当类型大小在编译期未知（如递归类型）、或需要转移大量数据的所有权而不复制时使用。`Box::new(value)` 分配堆内存，离开作用域时自动释放。

### Rc<T>：引用计数

单线程场景下的共享所有权。`Rc::clone(&rc)` 增加引用计数，最后一个 `Rc` 离开作用域时释放数据。不能提供可变访问——需要配合 `RefCell`。

### RefCell<T>：运行时借用检查

将 Rust 的编译期借用检查推迟到运行时。`borrow()` 返回 `Ref<T>`（不可变），`borrow_mut()` 返回 `RefMut<T>`（可变）。违反借用规则时触发 panic 而非编译错误——适合在测试中捕获逻辑错误。

## Constraints & Boundaries

- `Rc<RefCell<T>>` 虽然灵活，但失去了编译期安全检查的优势——过度使用可能掩盖设计问题
- `Arc<T>` 是 `Rc<T>` 的线程安全版本，使用原子操作（有性能开销）
- `Weak<T>` 配合 `Rc` 使用可避免循环引用导致的内存泄漏
