import unittest

from number_of_good_pairs import num_good_pairs


class TestNumGoodPairs(unittest.TestCase):
    def test_num_good_pairs(self):
        self.assertEqual(num_good_pairs([1, 2, 3, 1, 1, 3]), 4)
        self.assertEqual(num_good_pairs([1, 1, 1, 1]), 6)
        self.assertEqual(num_good_pairs([1, 2, 3]), 0)


if __name__ == '__main__':
    unittest.main()
