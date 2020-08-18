import unittest
from find_unique_num import find_uniq


class TestFindUniqueNum(unittest.TestCase):
    def test_find_uniq(self):
        self.assertEqual(find_uniq([1, 1, 1, 2, 1, 1]), 2)

    def test_find_uniq_decimal(self):
        self.assertEqual(find_uniq([0, 0, 0.55, 0, 0]), 0.55)

    def test_find_uniq_big_array(self):
        arr = [1] * 10000000 + [2]
        self.assertEqual(find_uniq(arr), 2)


if __name__ == '__main__':
    unittest.main()
