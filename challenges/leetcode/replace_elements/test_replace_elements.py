import unittest
from replace_elements import replace_elements


class TestReplaceElements(unittest.TestCase):
    def test_replace_elements(self):
        self.assertEqual(replace_elements(
            [17, 18, 5, 4, 6, 1]), [18, 6, 6, 6, 1, -1])
        self.assertEqual(replace_elements(
            [1, 2, 3, 4, 5, 10, 20, 15]), [20,20,20,20,20,20,15,-1])

if __name__ == '__main__':
    unittest.main()
