import unittest

from counting_duplicates import duplicate_count


class TestCountDuplicates(unittest.TestCase):
    def test_duplicate_count(self):
        self.assertEqual(duplicate_count('abcde'), 0)
        self.assertEqual(duplicate_count('aabbcde'), 2)
        self.assertEqual(duplicate_count('aabBcde'), 2)
        self.assertEqual(duplicate_count('indivisibility'), 1)
        self.assertEqual(duplicate_count('Indivisibilities'), 2)
        self.assertEqual(duplicate_count('aA11'), 2)
        self.assertEqual(duplicate_count('ABBA'), 2)


if __name__ == '__main__':
    unittest.main()
