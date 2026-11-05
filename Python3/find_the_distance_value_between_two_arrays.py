# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integer arrays arr1 and arr2, and the the integer d, return the
    distance value between the two arrays.

    The distance value is defined as the number of elements arr1[i] such that
    there is not any element arr2[j] where |arr1[i] - arr2[j]| <= d.
    '''
    # O(n^2)
    def findTheDistanceValue_valid(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        answer = len(arr1)
        for i in arr1:
            for j in arr2:
                if abs(i - j) <= d:
                    answer -= 1
                    break
            pass
        return answer

    # based on hints
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        answer = len(arr1)
        arr2.sort()
        for i in arr1:
            j = bisect.bisect(arr2, i)
            if j < len(arr2) and abs(i - arr2[j]) <= d:
                answer -= 1
            elif abs(i - arr2[j-1]) <= d:
                answer -= 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,5,8]
        j = [10,9,1,8]
        k = 2
        o = 2
        self.assertEqual(s.findTheDistanceValue(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [1,4,2,3]
        j = [-4,-3,6,10,20,30]
        k = 3
        o = 2
        self.assertEqual(s.findTheDistanceValue(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [2,1,100,3]
        j = [-5,-2,10,-3,7]
        k = 6
        o = 1
        self.assertEqual(s.findTheDistanceValue(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)