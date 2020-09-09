import unittest

from contains_duplicate import contains_duplicate


class TestContainsDuplicate(unittest.TestCase):
    def test_contains_duplicate(self):
        self.assertEqual(contains_duplicate([1, 2, 3, 1]), True)
        self.assertEqual(contains_duplicate([1, 2, 3, 4]), False)
        self.assertEqual(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)


if __name__ == '__main__':
    unittest.main()
