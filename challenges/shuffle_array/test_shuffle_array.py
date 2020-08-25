import unittest
from shuffle_array import shuffle_array


class TestShuffleArray(unittest.TestCase):
    def test_shuffle(self):
        self.assertEqual(shuffle_array([2, 5, 1, 3, 4, 7], 3), [2, 3, 5, 4, 1, 7])
        self.assertEqual(shuffle_array([1, 2, 3, 4, 4, 3, 2, 1], 4), [
                         1, 4, 2, 3, 3, 2, 4, 1])
        self.assertEqual(shuffle_array([1, 1, 2, 2], 2), [1, 2, 1, 2])


if __name__ == '__main__':
    unittest.main()
