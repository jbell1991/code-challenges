import unittest
from power_of_three import power_of_three


class TestPowerOfThree(unittest.TestCase):
    def test_power_of_three(self):
        self.assertEqual(power_of_three(27), True)
        self.assertEqual(power_of_three(9), True)
        self.assertEqual(power_of_three(0), False)
        self.assertEqual(power_of_three(81), True)
        self.assertEqual(power_of_three(45), False)


if __name__ == '__main__':
    unittest.main()
