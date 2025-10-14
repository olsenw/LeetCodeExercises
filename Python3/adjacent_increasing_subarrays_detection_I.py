# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    def hasIncreasingSubarrays_fails(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if k == 1:
            return True
        def test(a:int,b:int) -> bool:
            pass
            for i in range(a, b-k):
                # t = True
                # last = nums[i]
                # for j in range(i+1,i+k):
                #     if nums[j] <= nums[j-1]:
                #         t = False
                #         break
                # if t:
                #     return True
                if all(nums[j] > nums[j-1] for j in range(i+1, i+k)):
                    return True
            return False
        for i in range(n-k-k+1):
            if test(i,i+k) and test(i+k,n):
                return True
        return False
        return any(test(i,i+k+1) and test(i+k+1,n) for i in range(n))

    # solved problem of non adjacent increasing subarrays
    def hasIncreasingSubarrays_incorrect(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        for i in range(len(nums)-k-k+1):
            if all(nums[j] > nums[j-1] for j in range(i+1,i+k)):
                for j in range(i+k,len(nums)-k+1):
                    if all(nums[x] > nums[x-1] for x in range(j+1,j+k)):
                        return True
            pass
        return False

    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums) - k - k + 1):
            pass
            if all(nums[j] > nums[j-1] for j in range(i+1,i+k)) and all(nums[j] > nums[j-1] for j in range(i+k+1,i+k+k)):
                return True
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,5,7,8,9,2,3,4,3,1]
        j = 3
        o = True
        self.assertEqual(s.hasIncreasingSubarrays(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,4,4,4,5,6,7]
        j = 5
        o = False
        self.assertEqual(s.hasIncreasingSubarrays(i,j), o)

    def test_three(self):
        s = Solution()
        i = [-15,19]
        j = 1
        o = True
        self.assertEqual(s.hasIncreasingSubarrays(i,j), o)

    def test_four(self):
        s = Solution()
        i = [5,8,-2,-1]
        j = 2
        o = True
        self.assertEqual(s.hasIncreasingSubarrays(i,j), o)

    def test_five(self):
        s = Solution()
        i = [-3,-19,-8,-16]
        j = 2
        o = False
        self.assertEqual(s.hasIncreasingSubarrays(i,j), o)

    def test_six(self):
        s = Solution()
        i = [-15,3,16,0]
        j = 2
        o = False
        self.assertEqual(s.hasIncreasingSubarrays(i,j), o)

    def test_seven(self):
        s = Solution()
        i = [6,13,-17,-20,2]
        j = 2
        o = False
        self.assertEqual(s.hasIncreasingSubarrays(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)