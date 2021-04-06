import unittest
from height_checker import height_checker


class TestHeightChecker(unittest.TestCase):
    def test_height_checker(self):
        self.assertEqual(height_checker([1,1,4,2,1,3]), 3)
        self.assertEqual(height_checker([5,1,2,3,4]), 5)
        self.assertEqual(height_checker([1,2,3,4,5]), 0)


if __name__ == '__main__':
    unittest.main()
