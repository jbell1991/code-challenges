import unittest
from create_target_array import create_target_array


class TestCreateTargetArray(unittest.TestCase):
    def test_create_target_array(self):
        self.assertEqual(create_target_array(
            [0, 1, 2, 3, 4], [0, 1, 2, 2, 1]), [0, 4, 1, 3, 2])
        self.assertEqual(create_target_array(
            [1, 2, 3, 4, 0], [0, 1, 2, 3, 0]), [0, 1, 2, 3, 4])
        self.assertEqual(create_target_array(
            [1], [0]), [1])


if __name__ == '__main__':
    unittest.main()
