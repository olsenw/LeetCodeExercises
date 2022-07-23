# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

import bisect
from sortedcontainers import SortedList

class Solution:
    '''
    Given an integer array nums, return a new counts array. The counts
    array has the property where counts[i] is the number of smaller
    elements to the right of nums[i].
    '''
    def countSmaller_brute(self, nums: List[int]) -> List[int]:
        counts = []
        for i in range(len(nums)):
            counts.append(0)
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i]:
                    counts[-1] += 1
        return counts

    def countSmaller_binary_search(self, nums: List[int]) -> List[int]:
        counts = [0] * len(nums)
        # holds all processed numbers in sorted order
        sort = []
        # iterate through nums backward
        for i in range(len(nums) - 1, -1, -1):
            # find index where sorted element should be inserted
            # this doubles as the answer to how many smaller than it
            counts[i] = bisect.bisect_left(sort, nums[i])
            # insert the element at sorted index
            sort.insert(counts[i], nums[i])
        return counts

    # from discussion post by aryonbe
    # https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/2319704/Python-or-SortedList-or-O(nlogn)
    # uses the sorted containers library to do above in reverse
    def countSmaller_sortedcontainers(self, nums: List[int]) -> List[int]:
        res = []
        sorted_nums = SortedList(nums)
        for e in nums:
            idx = sorted_nums.index(e)
            res.append(idx)
            sorted_nums.remove(e)
        return res

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,2,6,1]
        o = [2,1,1,0]
        self.assertEqual(s.countSmaller(i), o)

    def test_two(self):
        s = Solution()
        i = [-1]
        o = [0]
        self.assertEqual(s.countSmaller(i), o)

    def test_three(self):
        s = Solution()
        i = [-1,-1]
        o = [0, 0]
        self.assertEqual(s.countSmaller(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)