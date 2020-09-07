import unittest
from defang_ip import defang_ip


class TestDefangIP(unittest.TestCase):
    def test_defang_ip(self):
        self.assertEqual(defang_ip("1.1.1.1"), "1[.]1[.]1[.]1")
        self.assertEqual(defang_ip("255.100.50.0"), "255[.]100[.]50[.]0")


if __name__ == '__main__':
    unittest.main()
