import unittest
from running_sum import running_sum


class TestRunningSum(unittest.TestCase):
    def test_running_sum(self):
        self.assertEqual(running_sum([1, 2, 3, 4]), [1, 3, 6, 10])
        self.assertEqual(running_sum([1, 1, 1, 1, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(running_sum([3, 1, 2, 10, 1]), [3, 4, 6, 16, 17])


if __name__ == '__main__':
    unittest.main()
