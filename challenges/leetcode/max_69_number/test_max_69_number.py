import unittest
from max_69_number import max_69_number


class TestHalvesAreAlike(unittest.TestCase):
    def test_max_69_number(self):
        self.assertEqual(max_69_number(9669), 9969)
        self.assertEqual(max_69_number(9996), 9999)
        self.assertEqual(max_69_number(9999), 9999)


if __name__ == '__main__':
    unittest.main()
