import unittest

import processing

class TestAdditionFunction(unittest.TestCase):

    def setUp(self):
        pass

    def test_add_positive_numbers(self):
        self.assertEqual(processing.add(1, 1), 2)


if __name__ == "__main__":
    unittest.main()