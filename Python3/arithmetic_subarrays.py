# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A sequence of numbers is called arithmetic if it consists of at least two
    elements, and the difference between every two consecutive elements is the
    same. More formally, a sequence s is arithmetic if and only if
    s[i+1] - s[i] == s[1] - s[0] for all valid i.

    Given an array of n integers, nums, and two arrays of m integers each, l and
    r, representing the m range queries, where the ith query is the range
    [l[i], r[i]]. All the arrays are 0-indexed.

    Return a list of boolean elements answer, where answer[i] is true if the
    subarray nums[l[i]], nums[i[i] + 1], ..., nums[r[i]] can be rearranged to
    form an arithmetic sequence, and false otherwise.
    '''
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def valid(n):
            n = sorted(n)
            c = n[1] - n[0]
            for i in range(2, len(n)):
                if n[i] - n[i-1] != c:
                    return False
            return True
        return [valid(nums[i:j+1]) for i,j in zip(l,r)]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,6,5,9,3,7]
        j = [0,0,2]
        k = [2,3,5]
        o = [True,False,True]
        self.assertEqual(s.checkArithmeticSubarrays(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
        j = [0,1,6,4,8,7]
        k = [4,4,9,7,9,10]
        o = [False,True,False,False,True,True]
        self.assertEqual(s.checkArithmeticSubarrays(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)