# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers nums, sort the array in increasing order based on
    the frequency of the values. If multiple values have the same frequency,
    sort them in decreasing order.

    Return the sorted array.
    '''
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        answer = []
        for x,y in sorted((j,-i) for i,j in c.items()):
            answer.extend([-y] * x)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,2,2,2,3]
        o = [3,1,1,2,2,2]
        self.assertEqual(s.frequencySort(i), o)

    def test_two(self):
        s = Solution()
        i = [2,3,1,3,2]
        o = [1,3,3,2,2]
        self.assertEqual(s.frequencySort(i), o)

    def test_two(self):
        s = Solution()
        i = [-1,1,-6,4,5,-6,1,4,1]
        o = [5,-1,4,4,-6,-6,1,1,1]
        self.assertEqual(s.frequencySort(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)