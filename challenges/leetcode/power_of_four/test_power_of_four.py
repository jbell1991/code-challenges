import unittest
from power_of_four import power_of_four


class TestPowerOfFour(unittest.TestCase):
    def test_power_of_four(self):
        self.assertEqual(power_of_four(16), True)
        self.assertEqual(power_of_four(1), True)
        self.assertEqual(power_of_four(5), False)
        self.assertEqual(power_of_four(64), True)
        self.assertEqual(power_of_four(100), False)
        

if __name__ == '__main__':
    unittest.main()
