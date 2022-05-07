# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of n integers nums, a 132 pattern is a subsequence of
    three integers nums[i], nums[j], nums[k] such that i < j < k and
    nums[i] < nums[k] < nums[j].

    Return true if there is a 132 pattern in nums, otherwise return
    false.
    '''
    # does not enforce order (132 is valid but so is 321)
    def find132pattern_fails(self, nums: List[int]) -> bool:
        small, large = 10 ** 9 + 1, -10 ** 9 - 1
        for n in nums:
            if small < n < large:
                return True
            small = min(small, n)
            large = max(large, n)
        return False

    # passes test cases
    def find132pattern_slow_monotonic(self, nums: List[int]) -> bool:
        s, l = 10 ** 9 + 1, -10 ** 9 - 1
        m = []
        for n in nums:
            # if m and m[-1][0] < n < m[-1][1]:
            #     return True
            for x,y in m:
                if x < n < y:
                    return True
            if n < s:
                s = n
                l = -10 ** 9 - 1
            else:
                l = max(l, n)
            while m and ((s < m[-1][0] and m[-1][1] <= l) or (s <= m[-1][0] and m[-1][1] < l)):
                m.pop()
            m.append((s,l))
        return False

    # based on leetcode solution 4: stack
    # https://leetcode.com/problems/132-pattern/solution/
    # O(n) time
    # O(n) space
    def find132pattern_stack_leetcode(self, nums: List[int]) -> bool:
        # not enough numbers
        if len(nums) < 3:
            return False
        # array to know the min at any given index
        mins = [10**9] * len(nums)
        mins[0] = nums[0]
        for i in range(1, len(nums)):
            mins[i] = min(mins[i-1], nums[i])
        # decreaseing monotonic stack for k value
        stack = []
        for j in range(len(nums) - 1, -1, -1):
            # no point to consider
            if nums[j] <= mins[j]:
                continue
            # empty stack
            while stack and stack[i] < mins[j]:
                stack.pop()
            # correct pattern found
            if stack and stack[-1] < nums[j]:
                return True
            # add to stack
            stack.append(nums[j])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4]
        o = False
        self.assertEqual(s.find132pattern(i), o)

    def test_two(self):
        s = Solution()
        i = [3,1,4,2]
        o = True
        self.assertEqual(s.find132pattern(i), o)

    def test_three(self):
        s = Solution()
        i = [-1,3,2,0]
        o = True
        self.assertEqual(s.find132pattern(i), o)

    def test_four(self):
        s = Solution()
        i = [1,0,1,-4,-3]
        o = False
        self.assertEqual(s.find132pattern(i), o)

    def test_five(self):
        s = Solution()
        i = [3,5,0,3,4]
        o = True
        self.assertEqual(s.find132pattern(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)