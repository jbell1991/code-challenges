import unittest
from maximum_wealth import maximum_wealth


class TestHalvesAreAlike(unittest.TestCase):
    def test_maximum_wealth(self):
        self.assertEqual(maximum_wealth([[1, 2, 3], [3, 2, 1]]), 6)
        self.assertEqual(maximum_wealth([[1, 5], [7, 3], [3, 5]]), 10)
        self.assertEqual(maximum_wealth(
            [[2, 8, 7], [7, 1, 3], [1, 9, 5]]), 17)


if __name__ == '__main__':
    unittest.main()
