import unittest

from average import avg


class TestAverage(unittest.TestCase):
    def test_average(self):
        self.assertEqual(avg(1), (2), (3), 2.0)


if __name__ == '__main__':
    unittest.main()
