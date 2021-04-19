import unittest
from array_sign import array_sign


class TestReverseInteger(unittest.TestCase):
    def test_array_sign(self):
        self.assertEqual(array_sign([-1,-2,-3,-4,3,2,1]*1000000), 1)
        self.assertEqual(array_sign([1,5,0,2,-3]), 0)
        self.assertEqual(array_sign([-1,1,-1,1,-1]), -1)

    def test_big_array_sign(self):
        self.assertEqual(array_sign([-1,-2,-3,-4,3,2,1]*1000000), 1)


if __name__ == '__main__':
    unittest.main()
