import unittest

from max_consecutive_ones import max_consecutive_ones


class TestMaxConsecutiveOnes(unittest.TestCase):
    def test_max_consecutive_ones(self):
        self.assertEqual(max_consecutive_ones([1, 1, 1, 0, 1, 1, 1, 1]), 4)
        self.assertEqual(max_consecutive_ones([1, 0, 1, 1, 1, 0, 0, 1]), 3)
        self.assertEqual(max_consecutive_ones([1, 1, 0, 1, 0, 1, 0]), 2)
        self.assertEqual(max_consecutive_ones([1] * 10000 + [2] + [1] * 11000), 11000)

if __name__ == '__main__':
    unittest.main()
