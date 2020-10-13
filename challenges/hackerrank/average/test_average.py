import unittest

from average import avg


class TestAverage(unittest.TestCase):
    def test_average(self):
        self.assertEqual(avg(1, 2, 3), 2.0)
        self.assertEqual(avg(-2, -5), -3.5)
        self.assertEqual(avg(50, 100), 75.0)


if __name__ == '__main__':
    unittest.main()
