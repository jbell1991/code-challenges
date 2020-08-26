import unittest

from expanded_nums import expanded_form


class TestExpandedNums(unittest.TestCase):
    def test_expanded_form(self):
        self.assertEqual(expanded_form(12), '10 + 2')
        self.assertEqual(expanded_form(42), '40 + 2')
        self.assertEqual(expanded_form(70304), '70000 + 300 + 4')
        self.assertEqual(expanded_form(900000), '900000')
        self.assertEqual(expanded_form(52505006), '50000000 + 2000000 + 500000 + 5000 + 6')


if __name__ == '__main__':
    unittest.main()
