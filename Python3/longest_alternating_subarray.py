# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums. A subarray s of length m s called
    alternating if:
    * m is greater than 1.
    * s1 = s0 + 1
    * The 0-indexed subarray s looks like [s0, s1, s0, s1, ..., s(m-1)%2].

    Return the maximum length of all alternating subarrays present in nums or -1
    if no such subarray exists.

    A subarray is a contiguous non-empty sequence of elements within an array.
    '''
    # solves the problem if it is a subsequence (not a subarray)
    def alternatingSubarray_fails(self, nums: List[int]) -> int:
        answer = -1
        s = set(nums)
        for i in s:
            for j in s:
                if i+1 != j:
                    continue
                a = 0
                t = i
                for k in range(len(nums)):
                    if nums[k] == t:
                        a += 1
                        t = i if t == j else j
                if a > 1:
                    answer = max(answer, a)
        return answer

    def alternatingSubarray_failsv(self, nums: List[int]) -> int:
        answer = -1
        n = len(nums)
        i = 0
        while i < n:
            t = nums[i] + 1
            j = i + 1
            while j < n and nums[j] == t:
                j += 1
                t = nums[i] + (t == nums[i])
            if j - i > 2:
                answer = max(answer, j - i)
            i = j
        return answer

    def alternatingSubarray(self, nums: List[int]) -> int:
        answer = -1
        n = len(nums)
        for i,a in enumerate(nums):
            j = i
            b = a
            t = a
            while j < n and b == t:
                j += 1
                b = nums[min(j,n-1)]
                t = a+1 if t == a else a
            if j - i > 1:
                answer = max(answer, j-i)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,3,4,3,4]
        o = 4
        self.assertEqual(s.alternatingSubarray(i), o)

    def test_two(self):
        s = Solution()
        i = [4,5,6]
        o = 2
        self.assertEqual(s.alternatingSubarray(i), o)

    def test_three(self):
        s = Solution()
        i = [21,9,5]
        o = -1
        self.assertEqual(s.alternatingSubarray(i), o)

    def test_four(self):
        s = Solution()
        i = [7,10,5,2,11,3,9,12,9,11]
        o = -1
        self.assertEqual(s.alternatingSubarray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)