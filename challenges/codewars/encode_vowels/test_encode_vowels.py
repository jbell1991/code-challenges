import unittest

from encode_vowels import encode, decode


class TestEncodeVowels(unittest.TestCase):
    def test_encode_vowels(self):
        self.assertEqual(encode('hello'), 'h2ll4')
        self.assertEqual(encode('How are you today?'), 'H4w 1r2 y45 t4d1y?')
        self.assertEqual(encode('This is an encoding test.'),
                         'Th3s 3s 1n 2nc4d3ng t2st.')
    
    def test_decode_vowels(self):
        self.assertEqual(decode('h2ll4'), 'hello')


if __name__ == '__main__':
    unittest.main()
