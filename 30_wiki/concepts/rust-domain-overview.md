---
id: rust-domain-overview
title: "Rust 编程语言：零成本抽象与内存安全的系统编程"
type: framework
status: draft
domain:
  - rust
created_at: 2026-06-02
updated_at: 2026-06-02
---

# Rust 编程语言概述

## Summary

Rust 是 Mozilla 开发的系统编程语言，核心卖点是"零成本抽象 + 内存安全 + 无数据竞争的并发"。通过所有权（ownership）、借用（borrowing）、生命周期（lifetime）三大机制，在编译期保证内存安全而不需要垃圾回收器。广泛应用于操作系统、嵌入式、WebAssembly、区块链和 CLI 工具开发。

## Framework Gallery

### 核心概念体系

| 概念 | 解决的问题 | 与 C++ 对比 |
|------|------|------|
| 所有权 | 谁负责释放内存 | C++ 需要手动 delete 或 unique_ptr |
| 借用 | 如何在不转移所有权的前提下访问数据 | C++ 的 const& 和 &，但无编译期借用检查 |
| 生命周期 | 引用在什么范围内有效 | C++ 的悬垂引用是运行时 bug |
| 智能指针 | 需要灵活所有权时怎么办 | C++ 的 shared_ptr/unique_ptr |
| Send/Sync | 能否在线程间安全传递 | C++ 无编译期并发安全检查 |

### Rust 的适用场景

- 需要极致性能 + 安全的场景（替代 C/C++）
- WebAssembly 前端（Rust → WASM 生态成熟）
- 命令行工具（clap、ratatui 等生态丰富）
- 不适合：快速原型、一次性脚本（编译时间 + 学习曲线不值得）

## Constraints & Boundaries

- 学习曲线是系统编程语言中最陡峭的之一——所有权系统没有 GC 语言中的对应概念
- 编译时间较长（尤其是泛型重度使用时）
- 生态不如 Python/JS 丰富，但近年来改善显著
