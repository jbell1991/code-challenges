import unittest

from subtract_product_sum import subtract_product_sum


class TestLetterCount(unittest.TestCase):
    def test_letter_count(self):
        self.assertEqual(subtract_product_sum(234), 15)
        self.assertEqual(subtract_product_sum(4421), 21)


if __name__ == '__main__':
    unittest.main()
