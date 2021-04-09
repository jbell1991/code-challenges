import unittest
from reverse_string import reverse_string


class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string(["h","e","l","l","o"]), ["o","l","l","e","h"])
        self.assertEqual(reverse_string(["H","a","n","n","a","h"]), ["h","a","n","n","a","H"])


if __name__ == '__main__':
    unittest.main()
