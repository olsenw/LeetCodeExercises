# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a sorted integer array nums and an integer n, add/patch elements to
    the array such that any number in the range [1,n] inclusive can be formed by
    the sum of some elements in the array.

    Return the minimum number of patches required.
    '''
    # Solution based on bhanu_bhakta
    # https://leetcode.com/problems/patching-array/solutions/5319434/easy-to-understand-greedy-approach-detailed-explanation/?envType=daily-question&envId=2024-06-16
    def minPatches(self, nums: List[int], n: int) -> int:
        # number of patches needed
        answer = 0
        # target sum to create with combination of values
        miss = 1 
        # index in array
        i = 0
        # check if all target values <= n can be made
        while miss <= n:
            # possible to use existing number
            if i < len(nums) and nums[i] <= miss:
                # add to range of formable numbers
                miss += nums[i]
                # increment array index
                i += 1
            # unable to use existing number
            else:
                # add the missing range to the array - extending viable range
                miss += miss
                # increment the number of patches
                answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3]
        j = 6
        o = 1
        self.assertEqual(s.minPatches(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,5,10]
        j = 20
        o = 2
        self.assertEqual(s.minPatches(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,2,2]
        j = 5
        o = 0
        self.assertEqual(s.minPatches(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)