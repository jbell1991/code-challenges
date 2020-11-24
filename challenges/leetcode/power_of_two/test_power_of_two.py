import unittest
from power_of_two import power_of_two


class TestPowerOfTwo(unittest.TestCase):
    def test_power_of_two(self):
        self.assertEqual(power_of_two(1), True)
        self.assertEqual(power_of_two(16), True)
        self.assertEqual(power_of_two(3), False)
        self.assertEqual(power_of_two(4), True)
        self.assertEqual(power_of_two(5), False)

if __name__ == '__main__':
    unittest.main()
