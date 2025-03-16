# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array ranks representing the ranks of some mechanics ranksi
    is the rank of the ith mechanic. A mechanic with a rank r can repair n cars
    in r + n^2 minutes.

    Also given an integer cars representing the total number of cars waiting in
    the garage to be repaired.

    Return the minium time taken to repair all the cars.

    Note: All the mechanics can repair the cars simultaneously.
    '''
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(m:int) -> bool:
            c = 0
            for r in ranks:
                c += math.floor(math.sqrt(m // r))
                if c >= cars:
                    return True
            return False
        i,j = 1, max(ranks) * cars**2
        while i < j:
            k = (j-i) // 2 + i
            if check(k):
                j = k
            else:
                i = k + 1
        return j

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,2,3,1]
        j = 10
        o = 16
        self.assertEqual(s.repairCars(i,j), o)

    def test_two(self):
        s = Solution()
        i = [5,1,8]
        j = 6
        o = 16
        self.assertEqual(s.repairCars(i,j), o)

    def test_three(self):
        s = Solution()
        i = [3]
        j = 52
        o = 8112
        self.assertEqual(s.repairCars(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)