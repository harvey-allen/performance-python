# Processing: Performance Benchmarking Module in Rust for Python

This Rust crate exposes a set of computationally intensive functions to Python via [PyO3](https://pyo3.rs/). It is designed to serve as a **performance benchmarking toolkit** for testing the speed and efficiency of Python integrations with Rust or for cross-language comparisons.

The module is intended to be built and used from Python with [maturin](https://maturin.rs/), a tool that simplifies building and publishing Rust-based Python extensions.

## Why These Functions?

The chosen functions are classic algorithms that stress different aspects of CPU and memory performance, making them ideal for benchmarking:

### 1. Naive Recursive Fibonacci (`fibonacci`)

- A simple, CPU-heavy recursive algorithm.
- Demonstrates how well the language handles deep recursion and function call overhead.
- Poor performance for large `n` due to exponential time complexity, making it a good stress test.

### 2. Sieve of Eratosthenes (`sieve`)

- An efficient algorithm to generate all prime numbers up to `n`.
- Tests array manipulation, memory access patterns, and loop performance.
- Good to benchmark raw CPU speed and cache efficiency.

### 3. Matrix Multiplication (`matrix_multiplication`)

- Classic `O(n^3)` complexity problem with nested loops.
- Tests multi-dimensional data access, arithmetic performance, and memory bandwidth.
- Widely used in scientific computing and a good proxy for numerical workloads.

### 4. Quicksort (`sort_array`)

- A fundamental sorting algorithm with average `O(n log n)` complexity.
- Tests recursive calls, data partitioning, and array manipulation.
- Sorting performance is critical in many real-world applications.

### 5. Regex-based Word Count (`count_words`)

- Uses regular expressions to parse text and count words.
- Tests string processing, regex engine performance, and memory allocations.
- Represents common tasks in data processing and text analytics.
