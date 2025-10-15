# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums of n integers, find the maximum value of k for which
    there exist two adjacent subarrays of length k each, such that both
    subarrays are strictly increasing. Specifically, check if there are two
    subarrays of length k starting at indices a and b (a < b), where:
    * Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly
      increasing.
    * The subarrays must be adjacent, meaning b = a + k.

    Return the maximum possible value of k.

    A subarray is a contiguous non-empty sequence of elements within an array.
    '''
    # test takes too long
    def maxIncreasingSubarrays_tle(self, nums: List[int]) -> int:
        n = len(nums)
        def test(k:int) -> bool:
            for i in range(n - k - k + 1):
                if all(nums[j] > nums[j-1] for j in range(i+1,i+k)) and all(nums[j] > nums[j-1] for j in range(i+k+1,i+k+k)):
                    return True
            return False
        i,j = 1,len(nums)//2
        while i < j:
            k = i + (j - i) // 2 + (j - i) % 2
            if test(k):
                i = k
            else:
                j = k - 1
        return j

    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        def test(k:int) -> bool:
            # for i in range(n - k - k + 1):
            #     if all(nums[j] > nums[j-1] for j in range(i+1,i+k)) and all(nums[j] > nums[j-1] for j in range(i+k+1,i+k+k)):
            #         return True
            i = 1
            c = 1
            while i < n - k + 1:
                if nums[i] > nums[i-1]:
                    c += 1
                else:
                    c = 1
                i += 1
                if c < k:
                    continue
                j = i + 1
                c = 1
                while j < n:
                    if nums[j] > nums[j-1]:
                        c += 1
                    else:
                        i = j - k + 1
                        c = 1
                        break
                    j += 1
                    if c == k:
                        return True
            return False
        i,j = 1,len(nums)//2
        while i < j:
            k = i + (j - i) // 2 + (j - i) % 2
            if test(k):
                i = k
            else:
                j = k - 1
        return j

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,5,7,8,9,2,3,4,3,1]
        o = 3
        self.assertEqual(s.maxIncreasingSubarrays(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,4,4,4,5,6,7]
        o = 2
        self.assertEqual(s.maxIncreasingSubarrays(i), o)

    def test_three(self):
        s = Solution()
        i = [5,8,-2,-1]
        o = 2
        self.assertEqual(s.maxIncreasingSubarrays(i), o)

    def test_four(self):
        s = Solution()
        i = [-5,17,19,-9,-1,-4]
        o = 2
        self.assertEqual(s.maxIncreasingSubarrays(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)