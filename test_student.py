import unittest
from proj1 import *
#proj1.py should contain your data class and function definitions
#these do not contribute positivly to your grade. 
#but your grade will be lowered if they are missing

class TestRegionFunctions(unittest.TestCase):

    def setUp(self):
        self.rc = rc1

    def test_holder(self):
        self.assertEqual(emissions_per_capita(rc4),0.0004)
        self.assertEqual(area(rect1),2514.22)
        self.assertEqual(emissions_per_square_km(rc1),0.48)
        self.assertEqual(densest(region_conditions),"Tokyo Metro")
        self.assertEqual(project_condition(rc1,1),RegionCondition(
            rc1.region,
            rc1.year + 1,
            int(37000000 * (1 + 0.0003)),
            1200.0 * (int(37000000 * (1 + 0.0003)) / 37000000)))


if __name__ == '__main__':
    unittest.main()
