import unittest

from unique_occurrences import unique_occurrences


class TestUnique_Occurrences(unittest.TestCase):
    def test_unique_occurrences(self):
        self.assertEqual(unique_occurrences([1, 2, 2, 1, 1, 3]), True)
        self.assertEqual(unique_occurrences([1, 2]), False)
        self.assertEqual(unique_occurrences(
            [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]), True)


if __name__ == '__main__':
    unittest.main()
