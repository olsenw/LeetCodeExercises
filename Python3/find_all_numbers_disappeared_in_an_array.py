# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums of n integers where nums[i] is in the range [1,n],
    return an array of all the integers in the range [1,n] that do not appear in
    nums.
    '''
    def findDisappearedNumbers_fails(self, nums: list[int]) -> list[int]:
        nums.sort()
        # return [i+1 for i,j in enumerate(nums) if i+1 != j]
        answer = []
        for i,j in enumerate(nums):
            if i+1 != j:
                answer.append(i+1)
        return answer

    # #O(n) time and space
    def findDisappearedNumbers_passes(self, nums: list[int]) -> list[int]:
        answer = []
        n = set(nums)
        for i in range(1,len(nums)+1):
            if i not in n:
                answer.append(i)
        return answer

    # O(n) time and no addition space (excepting returned answer)
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n):
            x = nums[i]
            if x > 2 * n:
                x -= 2*n
            if nums[x-1] < 2*n:
                nums[x-1] += 2*n
            # nums[x-1] = max(nums[i] + 2*n, nums[i])
        return [i+1 for i in range(n) if nums[i] < 2*n]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,3,2,7,8,2,3,1]
        o = [5,6]
        self.assertEqual(s.findDisappearedNumbers(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1]
        o = [2]
        self.assertEqual(s.findDisappearedNumbers(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)