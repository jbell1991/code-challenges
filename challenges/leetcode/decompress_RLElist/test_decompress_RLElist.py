import unittest
from decompress_RLElist import decompress_RLElist


class TestHeightChecker(unittest.TestCase):
    def test_decompress_RLElist(self):
        self.assertEqual(decompress_RLElist([1,2,3,4]), [2,4,4,4])
        self.assertEqual(decompress_RLElist([1,1,2,3]), [1,3,3])


if __name__ == '__main__':
    unittest.main()
