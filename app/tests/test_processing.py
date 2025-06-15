import unittest

import processing

class TestFibonacciFunction(unittest.TestCase):

    def setUp(self):
        pass

    def test_fibonacci(self):
        self.assertEqual(processing.heavy_computation(10), 55)


if __name__ == "__main__":
    unittest.main()