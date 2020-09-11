import unittest

from move_zeroes import move_zeroes


class TestMoveZeroes(unittest.TestCase):
    def test_move_zeroes(self):
        self.assertEqual(move_zeroes([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
        self.assertEqual(move_zeroes([1, 0, 0, 0, 2, 3, 4]), [1, 2, 3, 4, 0, 0, 0])
        self.assertEqual(move_zeroes([1, 1, 0, 0, 1, 0, 1]), [1, 1, 1, 1, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
