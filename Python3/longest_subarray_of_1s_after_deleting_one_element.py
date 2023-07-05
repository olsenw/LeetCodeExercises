# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a binary array nums, delete one element from it.

    Return the size of the longest non-empty subarray containing only 1's in the
    resulting array. Return 0 if there is no such subarray.
    '''
    def longestSubarray(self, nums: List[int]) -> int:
        a = []
        c = 0
        for n in nums:
            if n == 1:
                c += 1
            else:
                a.append(c)
                a.append(0)
                c = 0
        a.append(c)
        if a[0] == len(nums):
            return a[0] - 1
        answer = 0
        for i in range(1, len(a) - 1):
            answer = max(answer, a[i-1] + a[i+1])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,0,1]
        o = 3
        self.assertEqual(s.longestSubarray(i), o)

    def test_two(self):
        s = Solution()
        i = [0,1,1,1,0,1,1,0,1]
        o = 5
        self.assertEqual(s.longestSubarray(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1,1]
        o = 2
        self.assertEqual(s.longestSubarray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)