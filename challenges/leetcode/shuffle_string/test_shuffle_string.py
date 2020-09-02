import unittest
from shuffle_string import shuffle_string


class TestShuffleString(unittest.TestCase):
    def test_shuffle_string(self):
        self.assertEqual(shuffle_string(
            "codeleet", [4, 5, 6, 7, 0, 2, 1, 3]), "leetcode")
        self.assertEqual(shuffle_string("abc", [0, 1, 2]), "abc")
        self.assertEqual(shuffle_string("aiohn", [3, 1, 4, 2, 0]), "nihao")
        self.assertEqual(shuffle_string(
            "aaiougrt", [4, 0, 2, 6, 7, 3, 1, 5]), "arigatou")
        self.assertEqual(shuffle_string("art", [1, 0, 2]), "rat")


if __name__ == '__main__':
    unittest.main()
