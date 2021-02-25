import unittest
from merge_alternately import merge_alternately


class TestMergeAlternately(unittest.TestCase):
    def test_merge_alternately(self):
        self.assertEqual(merge_alternately("abc", "pqr"), "apbqcr")
        self.assertEqual(merge_alternately("ab", "pqrs"), "apbqrs")
        self.assertEqual(merge_alternately("abcd", "pq"), "apbqcd")


if __name__ == '__main__':
    unittest.main()
