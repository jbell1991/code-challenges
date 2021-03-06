import unittest

from sales_by_match import sales_by_match


class TestSalesByMatch(unittest.TestCase):
    def test_sales_by_match(self):
        self.assertEqual(sales_by_match(7, [1, 2, 1, 2, 1, 3, 2]), 2)
        self.assertEqual(sales_by_match(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]), 3)


if __name__ == '__main__':
    unittest.main()
