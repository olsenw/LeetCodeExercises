# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers nums and an integer k, return the number of
    contiguous subarrays where the product of all the elements in the array is
    strictly less than k.
    '''
    # sum instead of product... read the problem better
    def numSubarrayProductLessThanK_wrong(self, nums: List[int], k: int) -> int:
        answer = 0
        for i in range(1,k+1):
            s = sum(nums[:i])
            if s < k:
                answer += 1
            for j in range(i, len(nums)):
                s += nums[j] - nums[j-i]
                if s < k:
                    answer += 1
        return answer

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # corner case were it is impossible
        if k <= 1:
            return 0
        # total subarrays
        answer = 0
        # running product
        product = 1
        # start with a window 0,0
        i = 0
        # expand the window to the right
        for j in range(len(nums)):
            product *= nums[j]
            # shrink the window from the left
            while product >= k:
                product //= nums[i]
                i += 1
            # increment the number of subarrays
            answer += j - i + 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [10,5,2,6]
        j = 100
        o = 8
        self.assertEqual(s.numSubarrayProductLessThanK(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3]
        j = 0
        o = 0
        self.assertEqual(s.numSubarrayProductLessThanK(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)