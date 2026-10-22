# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of length n, where nums is a permutation of the
    integers from 0 to n - 1.

    Only the two following operations may be preformed:
    * Reverse the entire array.
    * Rotate Left by One: Move the first element to the end of the array, and
      the rest of the elements to the left by one position.
    
    Return an integer denoting the minimum number of operations required to sort
    the array in increasing order. If it is not possible to sort the array using
    only the given operations, return -1.
    '''
    def minOperations_incomplete(self, nums: List[int]) -> int:
        n = len(nums)
        def valid(nums:List[int]) -> int:
            for i in range(len(nums)):
                if nums[i] == 0:
                    break
            for j in range(i+1,i+n):
                if nums[j] == nums[j-1] + 1:
                    continue
                else:
                    return -1
            return i
        cycle = nums + nums
        i = valid(cycle)
        reverse = nums[::-1] + nums[::-1]
        i = valid(reverse)
        return

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        def inc(nums:List[int]) -> List[int]:
            for i in range(len(nums)):
                if nums[i] == 0:
                    break
            inc = i
            for j in range(i+1,i+n):
                if nums[j] == nums[j-1] + 1:
                    continue
                else:
                    return -1
            return inc
        def dec(nums:List[int]) -> List[int]:
            for i in range(len(nums)):
                if nums[i] == n-1:
                    break
            dec = i
            for j in range(i+1,i+n):
                if nums[j] == nums[j-1] - 1:
                    continue
                else:
                    return -1
            return dec
        c = nums + nums
        ci,cd = inc(c),dec(c)
        r = nums[::-1] + nums[::-1]
        ri,rd = inc(r),dec(r)
        # ri,rd = inc(r),-1
        if all(i == -1 for i in [ci,cd,ri,rd]):
            return -1
        answer = n
        if ci >= 0:
            answer = min(answer, ci)
        if cd >= 0:
            answer = min(answer, 1 + cd)
        if ri >= 0:
            answer = min(answer, 1 + ri)
        if rd >= 0:
            answer = min(answer, 2 + rd)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,2,1]
        o = 2
        self.assertEqual(s.minOperations(i), o)

    def test_two(self):
        s = Solution()
        i = [1,0,2]
        o = 2
        self.assertEqual(s.minOperations(i), o)

    def test_three(self):
        s = Solution()
        i = [2,0,1,3]
        o = -1
        self.assertEqual(s.minOperations(i), o)

    def test_four(self):
        s = Solution()
        i = [1,2,0]
        o = 2
        self.assertEqual(s.minOperations(i), o)

    def test_four(self):
        s = Solution()
        i = [1,2,3,4,0]
        o = 3
        self.assertEqual(s.minOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)