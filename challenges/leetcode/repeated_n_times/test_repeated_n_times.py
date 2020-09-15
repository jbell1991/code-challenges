import unittest

from repeated_n_times import repeated_n_times


class TestRepeatedNTimes(unittest.TestCase):
    def test_repeated_n_times(self):
        self.assertEqual(repeated_n_times([1, 2, 3, 3]), 3)
        self.assertEqual(repeated_n_times([2, 1, 2, 5, 3, 2]), 2)
        self.assertEqual(repeated_n_times([5, 1, 5, 2, 5, 3, 5, 4]), 5)

    def test_repeated_n_times_large(self):
        self.assertEqual(repeated_n_times(list(range(0, 10000000)) + [9999999]), 9999999)


if __name__ == '__main__':
    unittest.main()
