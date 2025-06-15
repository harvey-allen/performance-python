use pyo3::prelude::*;
use std::thread;
use std::time::Duration;

/// A naive, CPU-heavy recursive Fibonacci implementation
fn fibonacci(n: usize) -> usize {
    if n <= 1 {
        n
    } else {
        fibonacci(n - 1) + fibonacci(n - 2)
    }
}

#[pyfunction]
fn heavy_computation(n: usize) -> usize {
    // Use a reasonably high `n` to make it take ~1 second (depending on system)
    fibonacci(n)
}

#[pymodule]
fn processing(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(heavy_computation, m)?)?;
    Ok(())
}