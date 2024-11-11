# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums of non-negative integers and an integer k.

    An array is called special if the bitwise OR of all of its elements is at
    least k.

    Return the length of the shortest special non-empty subarray of nums, or
    return -1 if no special subarray exists.
    '''
    # based on leetcode editorial
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        answer = len(nums) + 1
        # sliding window start and end
        a,b = 0,0
        # array holding the count of each bit at index
        bits = [0] * 32
        def toNumber():
            a = 0
            for i in range(32):
                if bits[i]:
                    a |= 1 << i
            return a
        # grow sliding window
        while b < len(nums):
            # update bit count array
            for i in range(32):
                bits[i] += nums[b] & (1 << i) == (1 << i)
            # shrink sliding window
            while a <= b and toNumber() >= k:
                answer = min(answer, b - a + 1)
                # update bit count array
                for i in range(32):
                    bits[i] -= nums[a] & (1 << i) == (1 << i)
                a += 1
            b += 1
        return answer if answer < len(nums) + 1 else -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3], 2
        o = 1
        self.assertEqual(s.minimumSubarrayLength(*i), o)

    def test_two(self):
        s = Solution()
        i = [2,1,8], 10
        o = 3
        self.assertEqual(s.minimumSubarrayLength(*i), o)

    def test_three(self):
        s = Solution()
        i = [1,2], 0
        o = 1
        self.assertEqual(s.minimumSubarrayLength(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)