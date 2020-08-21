import unittest
from round_to_next5 import round_to_next5


class TestRoundToNext5(unittest.TestCase):
    def test_round_to_next5(self):
        self.assertEqual(round_to_next5(0), 0)
        self.assertEqual(round_to_next5(2), 5)
        self.assertEqual(round_to_next5(3), 5)
        self.assertEqual(round_to_next5(12), 15)
        self.assertEqual(round_to_next5(21), 25)
        self.assertEqual(round_to_next5(30), 30)
        self.assertEqual(round_to_next5(-2), 0)
        self.assertEqual(round_to_next5(-5), -5)


if __name__ == '__main__':
    unittest.main()
