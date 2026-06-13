# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a non-negative floating point number rounded to two decimal places
    celsius, that denotes the temperature in Celsius.

    Convert Celsius into Kelvin and Fahrenheit and return it as an array
    ans = [kelvin, fahrenheit].

    Return the array ans. Answers within 10^-5 of the actual answer will be
    accepted.

    Note that:
    * Kelvin = Celsius + 273.15
    * Fahrenheit = Celsius * 1.80 + 32.00
    '''
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 36.50
        o = [309.65000,97.70000]
        self.assertEqual(s.convertTemperature(i), o)

    def test_two(self):
        s = Solution()
        i = 122.11
        o = [395.26000,251.79800]
        self.assertEqual(s.convertTemperature(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)