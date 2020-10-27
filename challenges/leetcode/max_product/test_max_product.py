import unittest

from max_product import max_product


class TestLetterCount(unittest.TestCase):
    def test_max_product(self):
        self.assertEqual(max_product([3, 4, 5, 2]), 12)
        self.assertEqual(max_product([1, 5, 4, 5]), 16)
        self.assertEqual(max_product([3, 7]), 12)


if __name__ == '__main__':
    unittest.main()
