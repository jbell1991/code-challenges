import unittest
from find_special_int import find_special_int


class TestFindSpeicalInt(unittest.TestCase):
    def test_find_special_int(self):
        self.assertEqual(find_special_int([1, 2, 2, 6, 6, 6, 6, 7, 10]), 6)
        self.assertEqual(find_special_int([1, 2, 2, 7, 10]), 2)
    
    def test_find_special_int_large(self):
        self.assertEqual(find_special_int([1, 4, 4, 4, 10, 11, 12]*1000000), 4)


if __name__ == '__main__':
    unittest.main()
