import unittest
from keyboard_row import find_words


class TestFindWords(unittest.TestCase):
    def test_find_words(self):
        self.assertEqual(find_words(["Hello", "Alaska", "Dad", "Peace"]), ["Alaska", "Dad"])
        self.assertEqual(find_words(["abdfs", "cccd", "a", "qwwewm"]), ["a"])


if __name__ == '__main__':
    unittest.main()
