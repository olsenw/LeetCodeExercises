# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of distinct integers arr, find all pairs of elements
    with the minimum absolute difference of any two elements.

    Return a list of pairs in ascending order(with respect to pairs),
    each pair [a,b] follows
    * a, b are in arr
    * a < b
    * b - a equals minimum absolute difference of any two elements in arr
    '''
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        l = []
        # get largest possible int to set diff
        from sys import maxsize
        minDiff = maxsize
        for i in range(len(arr) - 1):
            diff = arr[i+1] - arr[i]
            if diff < minDiff:
                minDiff = diff
                l = [[arr[i], arr[i+1]]]
            elif diff == minDiff:
                l.append([arr[i], arr[i+1]])
        return l

class UnitTesting(unittest.TestCase):
    # actual test to run on Solution
    def test_one(self):
        s = Solution()
        i = [4,2,1,3]
        o = [[1,2],[2,3],[3,4]]
        self.assertEqual(s.minimumAbsDifference(i), o)

    def test_two(self):
        s = Solution()
        i = [3,8,-10,23,19,-4,-14,27]
        o = [[-14,-10],[19,23],[23,27]]
        self.assertEqual(s.minimumAbsDifference(i), o)

    def test_three(self):
        s = Solution()
        i = [1,3,6,10,15]
        o = [[1,3]]
        self.assertEqual(s.minimumAbsDifference(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)