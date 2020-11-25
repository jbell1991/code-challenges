import unittest
from sqrt import sqrt


class TestSqrt(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(sqrt(4), 2)
        self.assertEqual(sqrt(8), 2)
        self.assertEqual(sqrt(2147483647), 46340)
        self.assertEqual(sqrt(16), 4)
        self.assertEqual(sqrt(26), 5)


if __name__ == '__main__':
    unittest.main()
