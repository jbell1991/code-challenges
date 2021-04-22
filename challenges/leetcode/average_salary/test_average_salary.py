import unittest
from average_salary import average_salary


class TestAverageSalary(unittest.TestCase):
    def test_average_salary(self):
        self.assertEqual(average_salary([4000,3000,1000,2000]), 2500.00000)
        self.assertEqual(average_salary([1000,2000,3000]), 2000.00000)
        self.assertEqual(average_salary([6000,5000,4000,3000,2000,1000]), 3500.0000)
        self.assertEqual(average_salary([8000,9000,2000,3000,6000,1000]), 4750.0000)


if __name__ == '__main__':
    unittest.main()
