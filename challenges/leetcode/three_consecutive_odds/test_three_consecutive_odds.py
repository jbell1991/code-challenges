import unittest
from three_consecutive_odds import three_consecutive_odds


class TestThreeConsecutiveOdds(unittest.TestCase):
    def test_three_consecutive_odds(self):
        self.assertEqual(three_consecutive_odds([2, 6, 4, 1]), False)
        self.assertEqual(three_consecutive_odds([1, 2, 34, 3, 4, 5, 7, 23, 12]), True)
        self.assertEqual(three_consecutive_odds([1, 1, 1]), True)
        self.assertEqual(three_consecutive_odds([2, 4, 6, 8, 3, 5, 10, 7, 9, 12, 11]), False)

if __name__ == '__main__':
    unittest.main()
