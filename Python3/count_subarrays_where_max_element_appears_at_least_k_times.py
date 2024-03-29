# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer arrays nums and a positive integer k.

    Return the number of subarrays where the maximum element of nums appears at
    least k times in that subarray.

    A subarray is a contiguous sequence of elements within an array.
    '''
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m,n = max(nums), len(nums)
        answer = 0
        c = 0
        i = 0
        for j in range(n):
            if nums[j] == m:
                c += 1
            if c >= k:
                answer += n - j
            while i <= j and c >= k:
                if nums[i] == m:
                    c -= 1
                if c >= k:
                    answer += n - j
                i += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,2,3,3]
        j = 2
        o = 6
        self.assertEqual(s.countSubarrays(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,4,2,1]
        j = 3
        o = 0
        self.assertEqual(s.countSubarrays(i,j), o)

    def test_three(self):
        s = Solution()
        i = [4,3,2,1]
        j = 1
        o = 4
        self.assertEqual(s.countSubarrays(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)