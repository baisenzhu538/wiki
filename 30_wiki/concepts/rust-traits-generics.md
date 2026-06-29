---
id: rust-traits-generics
title: "Rust Trait 与泛型：零成本抽象的接口设计"
type: concept
status: draft
domain:
  - rust
created_at: 2026-06-02
---

# Rust Trait 与泛型

## Summary

Trait 是 Rust 的接口抽象机制——定义共享行为，类似于 Haskell 的 typeclass 或 Go 的 interface，但在编译期通过单态化（monomorphization）实现零运行时开销。泛型 + trait bound 实现了静态分发，`dyn Trait` 实现了动态分发。孤儿规则（orphan rule）防止 trait 实现的冲突——只能在 trait 或类型所在的 crate 中实现 trait。

## Claims

### 静态分发（泛型）vs 动态分发（dyn）

```rust
fn static_dispatch<T: Display>(x: T) { println!("{}", x); }
fn dynamic_dispatch(x: &dyn Display) { println!("{}", x); }
```

静态分发为每个具体类型生成独立代码（零开销，但增加编译时间和二进制大小），动态分发通过 vtable 在运行时查找方法（有间接调用开销，但二进制更小）。

### 孤儿规则

不能为外部类型实现外部 trait。这防止了不同 crate 对同一类型实现同一 trait 的冲突，但也导致需要用 newtype 模式包装外部类型来实现外部 trait。

### 常用派生 trait

`Clone`（显式复制）、`Copy`（隐式复制，仅适用于栈上类型）、`Debug`（格式化输出）、`PartialEq`/`Eq`（相等比较）、`PartialOrd`/`Ord`（排序）、`Hash`（哈希）、`Default`（默认值）。Rust 的 `#[derive(...)]` 自动生成这些 trait 的实现。

## Constraints & Boundaries

- 孤儿规则在大型项目中会成为架构约束——需要设计好 trait 的归属
- 泛型过度使用会显著增加编译时间
- `dyn Trait` 不支持关联类型和泛型方法——不是所有 trait 都能做 trait object
