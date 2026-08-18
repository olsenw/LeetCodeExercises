# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and an integer k.

    An integer x is almost missing from nums if x appears in exactly one
    subarray of size k within nums.

    Return the largest almost missing integer from nums. If no such integer
    exists, return -1.

    A subarray is a contiguous sequence of elements within an array.
    '''
    # brute force checking
    # O(n^3) <- incorrect... but real answer is still high
    def largestInteger_brute(self, nums: List[int], k: int) -> int:
        # go through all possible answers
        for n in sorted(set(nums), reverse=True):
            c = 0
            for i in range(len(nums) - k + 1):
                if n in nums[i:i+k]:
                    c += 1
            if c == 1:
                return n
        return -1

    # based on hints (give answer as one of three cases)
    def largestInteger(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        t = sorted(set(nums), reverse=True)
        # Case K == 1 (largest element occurring exactly once)
        if k == 1:
            for i in t:
                if c[i] == 1:
                    return i
        # Case k == n (largest element in whole array, which is whole subarray)
        elif k == len(nums):
            return t[0]
        # Case 1 < k < n (first or last element depends on repetitions)
        else:
            first,last = nums[0],nums[-1]
            if c[first] == 1 and c[last] == 1:
                return max(first,last)
            elif c[first] == 1:
                return first
            elif c[last] == 1:
                return last
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,9,2,1,7]
        j = 3
        o = 7
        self.assertEqual(s.largestInteger(i,j), o)

    def test_two(self):
        s = Solution()
        i = [3,9,7,2,1,7]
        j = 4
        o = 3
        self.assertEqual(s.largestInteger(i,j), o)

    def test_three(self):
        s = Solution()
        i = [0,0]
        j = 1
        o = -1
        self.assertEqual(s.largestInteger(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)