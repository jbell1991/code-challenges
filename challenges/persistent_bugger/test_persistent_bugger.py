import unittest
from persistent_bugger import persistence


class TestPersistence(unittest.TestCase):
    def test_persistence(self):
        self.assertEqual(persistence(39), 3)
        self.assertEqual(persistence(4), 0)
        self.assertEqual(persistence(25), 2)
        self.assertEqual(persistence(999), 4)


if __name__ == '__main__':
    unittest.main()
    