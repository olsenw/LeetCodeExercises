# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums, return the number of triplets chosen from the
    array that can make triangles if used as the lengths of the sides of a
    triangle.
    '''
    def triangleNumber_brute(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        answer = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] != nums[k]:
                        answer += 1
        return answer

    # [1,1,3] will get answer 1 even though sides are too short
    def triangleNumber_wrong(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        answer = 0
        for i in range(n):
            for j in range(i+1,n):
                k = nums[i] + nums[j]
                a = bisect.bisect(nums, k, j+1)
                b = bisect.bisect_left(nums, k, j+1)
                answer += n - j - a + b - 1
        return answer

    # binary search
    # O(n^2 log n)
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        answer = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                k = nums[i] + nums[j]
                b = bisect.bisect(nums,k-1,j+1)
                if b == n or nums[b-1] < k:
                    answer += b - j - 1
        return answer

    # based on 466ms code sample
    # O(n log n)
    def triangleNumber_two_pointer(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0
        for i,j in enumerate(nums[2:], 2):
            lo, hi = 0, i-1
            while lo < hi:
                if nums[lo] + nums[hi] > j:
                    answer += hi - lo
                    hi -= 1
                else:
                    lo += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,2,3,4]
        o = 3
        self.assertEqual(s.triangleNumber(i), o)

    def test_two(self):
        s = Solution()
        i = [4,2,3,4]
        o = 4
        self.assertEqual(s.triangleNumber(i), o)

    def test_three(self):
        s = Solution()
        i = [1] * 1000
        o = 166167000
        self.assertEqual(s.triangleNumber(i), o)

    def test_four(self):
        s = Solution()
        i = [1,1,3,4]
        o = 0
        self.assertEqual(s.triangleNumber(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)