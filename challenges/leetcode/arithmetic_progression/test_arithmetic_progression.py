import unittest
from arithmetic_progression import arithmetic_progression


class TestArithmeticProgression(unittest.TestCase):
    def test_arithmetic_progression(self):
        self.assertEqual(arithmetic_progression([3,5,1]), True)
        self.assertEqual(arithmetic_progression([1,2,4]), False)
        self.assertEqual(arithmetic_progression([3,5,1,7,9,11,15,13,19,17,21]), True)
        self.assertEqual(arithmetic_progression([3,5,1,7,9,11,15,13,19,17,21,2]), False)

if __name__ == '__main__':
    unittest.main()
