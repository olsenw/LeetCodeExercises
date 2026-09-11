# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n employees in a company, numbered from 0 to n-1. Each employee i
    has worked for hours[i] hours in the company.

    The company requires each employee to work for at least target hours.

    Given a 0-indexed array of non-negative integers hours of length n and a
    non-negative integer target.

    Return the integer denoting the number of employees who worked at least
    target hours.
    '''
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(h >= target for h in hours)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,1,2,3,4]
        j = 2
        o = 3
        self.assertEqual(s.numberOfEmployeesWhoMetTarget(i,j), o)

    def test_two(self):
        s = Solution()
        i = [5,1,4,2,2]
        j = 6
        o = 0
        self.assertEqual(s.numberOfEmployeesWhoMetTarget(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)