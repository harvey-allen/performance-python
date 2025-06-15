import unittest
import processing


class TestRustFunctions(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(processing.fibonacci(10), 55)
        self.assertEqual(processing.fibonacci(0), 0)
        self.assertEqual(processing.fibonacci(1), 1)

    def test_sieve(self):
        self.assertEqual(processing.sieve(10), [2, 3, 5, 7])
        self.assertEqual(processing.sieve(2), [2])
        self.assertEqual(processing.sieve(1), [])

    def test_matrix_multiplication(self):
        a = [[1.0, 2.0],
             [3.0, 4.0]]
        b = [[5.0, 6.0],
             [7.0, 8.0]]
        expected = [[19.0, 22.0],
                    [43.0, 50.0]]
        result = processing.matrix_multiplication(a, b)
        self.assertEqual(result, expected)

    def test_sort_array(self):
        unsorted_arr = [5, 3, 8, 1, 2]
        sorted_arr = [1, 2, 3, 5, 8]
        self.assertEqual(processing.sort_array(unsorted_arr), sorted_arr)
        self.assertEqual(processing.sort_array([]), [])
        self.assertEqual(processing.sort_array([42]), [42])

    def test_count_words(self):
        text = "Hello, world! This is a test."
        self.assertEqual(processing.count_words(text), 6)
        empty_text = ""
        self.assertEqual(processing.count_words(empty_text), 0)
        self.assertEqual(processing.count_words("One, two; three..."), 3)


if __name__ == "__main__":
    unittest.main()