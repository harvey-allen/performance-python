use pyo3::prelude::*;

#[pyfunction]
fn add(a: usize, b: usize) -> usize {
    a + b
}

#[pymodule]
fn processing(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add, m)?)?;
    Ok(())
}
