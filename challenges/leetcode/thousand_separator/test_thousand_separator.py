import unittest

from thousand_separator import thousand_separator


class TestThousandSeparator(unittest.TestCase):
    def test_thousand_separator(self):
        self.assertEqual(thousand_separator(987), "987")
        self.assertEqual(thousand_separator(1234), "1.234")
        self.assertEqual(thousand_separator(123456789), "123.456.789")
        self.assertEqual(thousand_separator(0), "0")


if __name__ == '__main__':
    unittest.main()
