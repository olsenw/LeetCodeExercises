# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    The score of an array is defined as the product of its sum and its length.

    Given a positive integer array nums and an integer k, return the number of
    non-empty subarrays of nums whose score is strictly less than k.

    A subarray is a contiguous sequence of elements within an array.
    '''
    def countSubarrays_wrong(self, nums: List[int], k: int) -> int:
        answer = 0
        s = 0
        i = 0
        for j in range(len(nums)):
            s += nums[j]
            if s * (j-i+1) < k:
                answer += 1
            while i < j and s * (j-i+1) >= k:
                s -= nums[i]
                if s * (j-i+1) < k:
                    answer += 1
                i += 1
        return answer

    def countSubarrays(self, nums: List[int], k: int) -> int:
        def f(n:int):
            return (n * (n+1)) // 2
        nums.append(k)
        answer = 0
        s,i = 0,0
        for j in range(len(nums)):
            s += nums[j]
            pass
            while i < j and s * (j-i+1) >= k:
                answer += f(j-i)
                s -= nums[i]
                i += 1
        return answer

    def countSubarrays(self, nums: List[int], k: int) -> int:
        nums.append(k)
        n = len(nums)
        answer = 0
        s,i = 0,0
        for j in range(n):
            s += nums[j]
            pass
            while i < j and s * (j-i+1) >= k:
                s -= nums[i]
                i += 1
            if s * (j-i+1) < k:
                answer += j-i+1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,1,4,3,5]
        j = 10
        o = 6
        self.assertEqual(s.countSubarrays(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1]
        j = 5
        o = 5
        self.assertEqual(s.countSubarrays(i,j), o)

    def test_three(self):
        s = Solution()
        i = [9,5,3,8,4,7,2,7,4,5,4,9,1,4,8,10,8,10,4,7]
        j = 4
        o = 3
        self.assertEqual(s.countSubarrays(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)