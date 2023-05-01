# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of unique integers salary where salary[i] is the salary of
    the ith employee.

    Return the average salary of employees excluding the minium and maximum
    salary. Answer within 10^-5 of the actual answer will be accepted.
    '''
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4000,3000,1000,2000]
        o = 2500.00000
        self.assertEqual(s.average(i), o)

    def test_two(self):
        s = Solution()
        i = [1000,2000,3000]
        o = 2000.00000
        self.assertEqual(s.average(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)