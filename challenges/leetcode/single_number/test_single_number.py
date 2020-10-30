import unittest
from single_number import single_number


class TestSingleNumber(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(single_number([1, 1, 1, 2, 1, 1]), 2)
        self.assertEqual(single_number([2, 2, 1]), 1)
        self.assertEqual(single_number([4, 1, 2, 1, 2]), 4)
        self.assertEqual(single_number([1]), 1)

    def test_single_number_decimal(self):
        self.assertEqual(single_number([0, 0, 0.55, 0, 0]), 0.55)

    def test_single_number_big_array(self):
        arr = [1] * 10000000 + [2]
        self.assertEqual(single_number(arr), 2)


if __name__ == '__main__':
    unittest.main()
