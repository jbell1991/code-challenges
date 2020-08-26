import unittest
from find_numbers import find_numbers


class TestFindNumbers(unittest.TestCase):
    def test_find_numbers(self):
        self.assertEqual(find_numbers([12, 345, 2, 6, 7896]), 2)
        self.assertEqual(find_numbers([555, 901, 482, 1771]), 1)


if __name__ == '__main__':
    unittest.main()
