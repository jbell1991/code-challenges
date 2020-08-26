import unittest
from count_characters import count_char


class TestCountCharacters(unittest.TestCase):
    def test_count_char(self):
        self.assertEqual(count_char('aba'), {'a': 2, 'b': 1})
        self.assertEqual(count_char(''), {})

if __name__ == '__main__':
    unittest.main()
