import unittest
from uncover_spy import uncover_spy


class TestUncoverSpy(unittest.TestCase):
    def test_uncover_spy(self):
        self.assertEqual(uncover_spy(2, [[1, 2]]), 2)
        self.assertEqual(uncover_spy(3, [[1, 3], [2, 3]]), 3)
        self.assertEqual(uncover_spy(3, [[1, 3], [2, 3], [3, 1]]), -1)
        self.assertEqual(uncover_spy(3, [[1, 2], [2, 3]]), -1)
        self.assertEqual(uncover_spy(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]), 3)


if __name__ == '__main__':
    unittest.main()
