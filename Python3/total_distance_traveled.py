# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A truck has two fuel tanks. Given two integers, mainTank representing the
    fuel present in the main tack in liters and additionalTank representing the
    fuel present in the additional tank in liters.

    The truck has a mileage of 10 km per liter. Whenever 5 liters of fuel get
    used up in the main tank, if the additional tank has at least 1 liter of
    fuel, 1 liters of fuel will be transferred from the additional tank to the
    main tank.

    Return the maximum distance which can be traveled.

    Note: Injection from the additional tank is not continuous. It happens
    suddenly and immediately for every 5 liters consumed.
    '''
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        answer = 0
        distance = 10
        fuelFill = 5
        transfer = 1
        while mainTank >= fuelFill:
            mainTank -= fuelFill
            answer += fuelFill * distance
            if additionalTank > 0:
                mainTank += transfer
                additionalTank -= transfer
        return answer + (mainTank * distance)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        j = 10
        o = 60
        self.assertEqual(s.distanceTraveled(i,j), o)

    def test_two(self):
        s = Solution()
        i = 1
        j = 2
        o = 10
        self.assertEqual(s.distanceTraveled(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)