import unittest
from halves_are_alike import halves_are_alike


class TestHalvesAreAlike(unittest.TestCase):
    def test_halves_are_alike(self):
        self.assertEqual(halves_are_alike("book"), True)
        self.assertEqual(halves_are_alike("textbook"), False)
        self.assertEqual(halves_are_alike("MerryChristmas"), False)
        self.assertEqual(halves_are_alike("AbCdEfGh"), True)


if __name__ == '__main__':
    unittest.main()
