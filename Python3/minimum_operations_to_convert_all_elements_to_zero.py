# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums of size n, consisting of non-negative integers. Apply
    some (possibly zero) operations on the array so that all elements become 0.

    In one operation, select a subarray [i,j] (where 0 <= i <= j < n) and set
    all occurrences of the minimum non-negative integer in that subarray to 0.

    Return the minimum number of operations required to make all elements in the
    array 0.
    '''
    def minOperations_fails(self, nums: List[int]) -> int:
        answer = 0
        for i in sorted(set(nums)):
            last = 0
            for j in range(len(nums)):
                n = nums[j]
                if nums[j] == i:
                    if last != i:
                        answer += 1
                    nums[j] = 0
                last = n
        return answer

    def minOperations(self, nums: List[int]) -> int:
        answer = 0
        stack = []
        for n in nums:
            while stack and stack[-1] > n:
                stack.pop()
                answer += 1
            if n > 0 and not(stack and stack[-1] == n):
                stack.append(n)
        return answer + len(stack)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,2]
        o = 1
        self.assertEqual(s.minOperations(i), o)

    def test_two(self):
        s = Solution()
        i = [3,1,2,1]
        o = 3
        self.assertEqual(s.minOperations(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,1,2,1,2]
        o = 4
        self.assertEqual(s.minOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)