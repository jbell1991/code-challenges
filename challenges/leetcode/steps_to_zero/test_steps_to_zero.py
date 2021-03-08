import unittest
from steps_to_zero import steps_to_zero


class TestStepsToZero(unittest.TestCase):
    def test_steps_to_zero(self):
        self.assertEqual(steps_to_zero(14), 6)
        self.assertEqual(steps_to_zero(8), 4)
        self.assertEqual(steps_to_zero(123), 12)


if __name__ == '__main__':
    unittest.main()
