import unittest
from sort_array_by_parity import sort_array_by_parity


class TestReverseInteger(unittest.TestCase):
    def test_sort_array_by_parity(self):
        self.assertEqual(sort_array_by_parity([3,1,2,4]), [2,4,3,1])


if __name__ == '__main__':
    unittest.main()
