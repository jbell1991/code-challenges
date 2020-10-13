import unittest

from reverse_words_swap_case import reverse_words_order_and_swap_cases


class TestReverseWordsSwapCase(unittest.TestCase):
    def test_reverse_words_order_and_swap_cases(self):
        self.assertEqual(reverse_words_order_and_swap_cases(
            'rUns dOg'), 'DoG RuNS')
        self.assertEqual(reverse_words_order_and_swap_cases(
            'The Quick Brown Fox Jumps Over the Lazy Dog'), 
            'dOG lAZY THE oVER jUMPS fOX bROWN qUICK tHE')

if __name__ == '__main__':
    unittest.main()
