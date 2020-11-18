import unittest
from frequency_sort import frequency_sort


class TestFrequencySort(unittest.TestCase):
    def test_frequency_sort(self):
        self.assertEqual(frequency_sort("tree"), "eetr")
        self.assertEqual(frequency_sort("cccaaa"), "cccaaa")
        self.assertEqual(frequency_sort("Aabb"), "bbAa")


if __name__ == '__main__':
    unittest.main()
