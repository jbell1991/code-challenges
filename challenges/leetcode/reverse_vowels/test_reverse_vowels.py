import unittest

from reverse_vowels import reverse_vowels


class TestReverseVowels(unittest.TestCase):
    def test_reverse_vowels(self):
        self.assertEqual(reverse_vowels("hello"), "holle")
        self.assertEqual(reverse_vowels("leetcode"), "leotcede")
        self.assertEqual(reverse_vowels("aA"), "Aa")


if __name__ == '__main__':
    unittest.main()
