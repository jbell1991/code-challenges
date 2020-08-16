import unittest
from string_transformer import string_transformer


class TestStringTransformer(unittest.TestCase):
    def test_string_transformer(self):
        self.assertEqual(string_transformer("Example string"), "STRING eXAMPLE")
        self.assertEqual(string_transformer("Example Input"), "iNPUT eXAMPLE")
        self.assertEqual(string_transformer("To be OR not to be That is the Question"), "qUESTION THE IS tHAT BE TO NOT or BE tO")
        # Should handle empty string
        self.assertEqual(string_transformer(""), "")
        # Should handle multiple spaces
        self.assertEqual(string_transformer("You Know When  THAT  Hotline Bling"), "bLING hOTLINE  that  wHEN kNOW yOU")
        # Should handle leading space
        self.assertEqual(string_transformer(" A b C d E f G "), " g F e D c B a ")


if __name__ == '__main__':
    unittest.main()
