import unittest
from fizzbuzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz(15), [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz"
        ])
        self.assertEqual(fizz_buzz(1), ["1"])


if __name__ == '__main__':
    unittest.main()
