# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a circular integer array nums (ie the next element of
    nums[nums.length - 1] is nums[0]), return the next greater number for every
    element in nums.

    The next greater number of a number x is the first greater number to its
    traversing-order next in the array, which means the search could loop the
    circle to find the next greatest number. If it doesn't exist, return -1 for
    this number.
    '''
    def nextGreaterElements_brute(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = max(nums)
        nums = nums + nums
        answer = []
        for i in range(n):
            if nums[i] == m:
                answer.append(-1)
                continue
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    answer.append(nums[j])
                    break
        return answer

    # fails on decreasing sequences (queue not cleared correctly)
    def nextGreaterElements_fails(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = max(nums)
        nums = nums + nums
        answer = [-1] * n
        d = deque([])
        for i in range(n):
            if nums[i] == m:
                d.clear()
                continue
            while d and d[0] < nums[i]:
                d.popleft()
            if d and d[0] > nums[i]:
                answer[i] = d[0]
                continue
            for j in range(i + 1, len(nums)):
                d.append(nums[j])
                if nums[j] > nums[i]:
                    answer[i] = nums[j]
                    break
        return answer

    # based on Leetcode stack solution
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [-1] * n
        stack = []
        for i in range(2 * n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i % n]:
                stack.pop()
            if stack:
                answer[i % n] = nums[stack[-1]]
            else:
                answer[i % n] = -1
            stack.append(i % n)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,1]
        o = [2,-1,2]
        self.assertEqual(s.nextGreaterElements(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,3]
        o = [2,3,4,-1,4]
        self.assertEqual(s.nextGreaterElements(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1,1,5,5,5,1,3]
        o = [5,5,5,-1,-1,-1,3,5]
        self.assertEqual(s.nextGreaterElements(i), o)

    def test_four(self):
        s = Solution()
        i = [5,4,3,2,1]
        o = [-1,5,5,5,5]
        self.assertEqual(s.nextGreaterElements(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)