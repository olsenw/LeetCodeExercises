# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums. Create a 2D array from nums, satisfying the
    following conditions:
    * The 2D array should contain only the elements of the array nums.
    * Each row in the 2D array contains distinct integers.
    * The number of rows in the 2D array should be minimal.

    Return the resulting array. If there are multiple answers, return any of
    them.

    Note that the 2D array can have a different number of elements on each row.
    '''
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        c = Counter()
        answer = [[]]
        for n in nums:
            if c[n] == len(answer):
                answer.append([])
            answer[c[n]].append(n)
            c[n] += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,4,1,2,3,1]
        o = [[1,3,4,2],[1,3],[1]]
        self.assertEqual(s.findMatrix(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4]
        o = [[1,2,3,4]]
        self.assertEqual(s.findMatrix(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)