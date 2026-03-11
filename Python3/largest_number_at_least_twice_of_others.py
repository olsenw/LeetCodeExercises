# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums where the largest integer is unique.

    Determine whether the largest element in the array is at least twice as much
    as every other number in the array. If it is, return the index of the
    largest element, or return -1 otherwise.
    '''
    # solves the wrong problem
    def dominantIndex_fails(self, nums: List[int]) -> int:
        n = len(nums)
        answer = {j:i for i,j in enumerate(nums)}
        nums.sort(reverse=True)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[j] * 2 > nums[i]:
                    break
            else:
                return answer[nums[i]]
        return -1

    def dominantIndex(self, nums: List[int]) -> int:
        answer = {j:i for i,j in enumerate(nums)}
        nums.sort(reverse=True)
        if nums[0] >= 2 * nums[1]:
            return answer[nums[0]]
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,6,1,0]
        o = 1
        self.assertEqual(s.dominantIndex(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4]
        o = -1
        self.assertEqual(s.dominantIndex(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)