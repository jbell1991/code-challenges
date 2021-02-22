import unittest
from highest_altitude import highest_altitude


class TestHighestAltitude(unittest.TestCase):
    def test_highest_altitude(self):
        self.assertEqual(highest_altitude([-5, 1, 5, 0, -7]), 1)
        self.assertEqual(highest_altitude([-4, -3, -2, -1, 4, 3, 2]), 0)


if __name__ == '__main__':
    unittest.main()
