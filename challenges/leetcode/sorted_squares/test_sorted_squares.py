import unittest

from sorted_squares import sorted_squares


class TestSortedSquares(unittest.TestCase):
    def test_sorted_squares(self):
        self.assertEqual(sorted_squares(
            [-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])
        self.assertEqual(sorted_squares(
            [-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])


if __name__ == '__main__':
    unittest.main()
