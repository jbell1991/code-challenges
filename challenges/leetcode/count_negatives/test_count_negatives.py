import unittest

from count_negatives import count_negatives


class TestCountNegatives(unittest.TestCase):
    def test_count_negatives(self):
        self.assertEqual(count_negatives(
            [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]), 8)
        self.assertEqual(count_negatives([[3, 2], [1, 0]]), 0)
        self.assertEqual(count_negatives([[1, -1], [-1, -1]]), 3)
        self.assertEqual(count_negatives([[-1]]), 1)


if __name__ == '__main__':
    unittest.main()
