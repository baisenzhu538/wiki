---
id: rust-concurrency-send-sync
title: "Rust 并发安全：Send 与 Sync 的编译期保证"
type: concept
status: draft
domain:
  - rust
created_at: 2026-06-02
---

# Rust 并发安全

## Summary

Rust 通过 `Send` 和 `Sync` 两个 auto trait 在编译期保证线程安全。`Send` 表示所有权可以安全转移到另一个线程，`Sync` 表示共享引用可以安全跨线程访问。编译器自动为大多数类型推导这些 trait，不需要程序员手动标注——除非使用 unsafe 或 FFI。

## Claims

### Send：跨线程所有权转移

```rust
use std::thread;
let data = vec![1, 2, 3];
thread::spawn(move || {
    println!("{:?}", data); // data 的所有权移入新线程
});
```

`Rc<T>` 不是 `Send`：引用计数使用非原子操作，多线程同时 clone/drop 会导致数据竞争。替换为 `Arc<T>`（原子引用计数）。

### Sync：跨线程共享引用

`T: Sync` 等价于 `&T: Send`。`Mutex<T>` 是 `Sync` 因为它用锁保护了内部可变性。`RefCell<T>` 不是 `Sync` 因为运行时借用检查是单线程的。

### 常见陷阱：async 中的 Send 约束

Tokio 等多线程运行时要求 Future 是 `Send`——运行时可能在 `.await` 点将 Future 迁移到另一个线程。在 async 块中捕获 `Rc` 或 `RefCell` 会导致编译错误。

## Constraints & Boundaries

- Send/Sync 是 marker trait，不提供运行时保护——错误标注 unsafe impl 导致 UB
- `MutexGuard` 不是 Send（必须在获取锁的线程释放），这是设计特性不是 bug
- 过度使用 `Arc<Mutex<T>>` 会失去编译期安全检查的优势
