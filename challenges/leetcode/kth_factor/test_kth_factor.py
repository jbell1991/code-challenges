import unittest
from kth_factor import kth_factor


class TestKthFactor(unittest.TestCase):
    def test_kth_factor(self):
        self.assertEqual(kth_factor(12, 3), 3)
        self.assertEqual(kth_factor(7, 2), 7)
        self.assertEqual(kth_factor(4, 4), -1)
        self.assertEqual(kth_factor(1, 1), 1)
        self.assertEqual(kth_factor(1000, 3), 4)


if __name__ == '__main__':
    unittest.main()
