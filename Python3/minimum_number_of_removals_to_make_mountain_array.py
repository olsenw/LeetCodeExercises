# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    An array arr is a mountain array if and only if:
    * arr.length >= 3
    * There exists some index i (0-indexed) with 0 < i < arr.length - 1 such
      that:
      * arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
      * arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
    
    Given an integer array nums, return the minimum number of elements to remove
    to make nums a mountain array.
    '''
    def minimumMountainRemovals_fails(self, nums: List[int]) -> int:
        n = len(nums)
        def less(i:int, j:int) -> int:
            if i == 0:
                return 0
            if nums[i] >= j:
                return 1 + less(i-1, j)
            return min(1 + less(i-1, j), less(i-1, nums[i]))
        def more(i:int, j:int) -> int:
            if i == n:
                return 0
            if nums[i] >= j:
                return 1 + more(i+1, j)
            return min(1 + more(i+1, j), more(i+1, nums[i]))
        answer = []
        for i in range(1,n-1):
            answer.append([less(i-1, nums[i]), more(i+1, nums[i])])
        a = min(a+b for a,b in answer)
        return a

    # based on Leetcode editorial
    # https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/?envType=daily-question&envId=2024-10-30
    # for each index calculate the longest possible increasing sequence and
    # decreasing sequence, can then calc answer using math
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        # longest increasing subsequence
        lis = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)
        # longest decreasing subsequence
        lds = [1] * n
        for i in range(n-1,-1,-1):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    lds[i] = max(lds[i], lds[j] + 1)
        # find minimum needed removals
        answer = 1000
        for i in range(n):
            if lis[i] > 1 and lds[i] > 1:
                answer = min(answer, n - (lis[i] + lds[i] - 1))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,1]
        o = 0
        self.assertEqual(s.minimumMountainRemovals(i), o)

    def test_two(self):
        s = Solution()
        i = [2,1,1,5,6,2,3,1]
        o = 3
        self.assertEqual(s.minimumMountainRemovals(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)