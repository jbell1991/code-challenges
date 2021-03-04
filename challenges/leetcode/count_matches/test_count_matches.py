import unittest
from count_matches import count_matches


class TestCountMatches(unittest.TestCase):
    def test_count_matches(self):
        self.assertEqual(count_matches([["phone", "blue", "pixel"], 
            ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]], 
            ruleKey="color", ruleValue="silver"), 1)
        self.assertEqual(count_matches([["phone", "blue", "pixel"], ["computer", "silver", 
            "phone"], ["phone", "gold", "iphone"]], ruleKey="type", ruleValue="phone"), 2)
                                                                                            

if __name__ == '__main__':
    unittest.main()
