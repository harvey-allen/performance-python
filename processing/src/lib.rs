use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use regex::Regex;

//
// 1. Naive recursive Fibonacci
//
fn naive_fibonacci(n: usize) -> usize {
    if n <= 1 {
        n
    } else {
        naive_fibonacci(n - 1) + naive_fibonacci(n - 2)
    }
}

#[pyfunction]
fn fibonacci(n: usize) -> usize {
    naive_fibonacci(n)
}

//
// 2. Sieve of Eratosthenes
//
#[pyfunction]
fn sieve(n: usize) -> Vec<usize> {
    let mut is_prime = vec![true; n + 1];
    let mut primes = vec![];

    for p in 2..=n {
        if is_prime[p] {
            primes.push(p);
            let mut multiple = p * p;
            while multiple <= n {
                is_prime[multiple] = false;
                multiple += p;
            }
        }
    }

    primes
}

//
// 3. Matrix Multiplication
//
#[pyfunction]
fn matrix_multiplication(a: Vec<Vec<f64>>, b: Vec<Vec<f64>>) -> Vec<Vec<f64>> {
    let rows = a.len();
    let cols = b[0].len();
    let inner = b.len();

    let mut result = vec![vec![0.0; cols]; rows];
    for i in 0..rows {
        for j in 0..cols {
            for k in 0..inner {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    result
}

//
// 4. Quicksort (returns a new sorted Vec)
//
fn quicksort(mut arr: Vec<i64>) -> Vec<i64> {
    if arr.len() <= 1 {
        return arr;
    }

    let pivot = arr.remove(0);
    let less: Vec<i64> = arr.iter().cloned().filter(|x| *x < pivot).collect();
    let more: Vec<i64> = arr.iter().cloned().filter(|x| *x >= pivot).collect();

    let mut sorted = quicksort(less);
    sorted.push(pivot);
    sorted.extend(quicksort(more));
    sorted
}

#[pyfunction]
fn sort_array(arr: Vec<i64>) -> Vec<i64> {
    quicksort(arr)
}

//
// 5. Regex-based Word Count
//
#[pyfunction]
fn count_words(text: &str) -> usize {
    let re = Regex::new(r"\w+").unwrap();
    re.find_iter(text).count()
}

//
// PyO3 Module
//
#[pymodule]
fn processing(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fibonacci, m)?)?;
    m.add_function(wrap_pyfunction!(sieve, m)?)?;
    m.add_function(wrap_pyfunction!(matrix_multiplication, m)?)?;
    m.add_function(wrap_pyfunction!(sort_array, m)?)?;
    m.add_function(wrap_pyfunction!(count_words, m)?)?;
    Ok(())
}
