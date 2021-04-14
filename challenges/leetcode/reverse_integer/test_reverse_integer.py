import unittest
from reverse_integer import reverse_integer


class TestReverseInteger(unittest.TestCase):
    def test_reverse_integer(self):
        self.assertEqual(reverse_integer(123), 321)
        self.assertEqual(reverse_integer(-123), -321)
        self.assertEqual(reverse_integer(120), 21)
        self.assertEqual(reverse_integer(0), 0)
    
    def test_reverse_integer_bit(self):
        self.assertEqual(reverse_integer(1534236469), 0)
        

if __name__ == '__main__':
    unittest.main()
