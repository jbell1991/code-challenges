import unittest
from count_odds import count_odds

class TestCountOdds(unittest.TestCase):
    def test_count_odds(self):
        self.assertEqual(count_odds(3,7), 3)
        self.assertEqual(count_odds(8, 10), 1)
        self.assertEqual(count_odds(0, 13), 7)
        self.assertEqual(count_odds(5, 17), 7)
        self.assertEqual(count_odds(646546546, 841641656), 97547555)


if __name__ == '__main__':
    unittest.main()
