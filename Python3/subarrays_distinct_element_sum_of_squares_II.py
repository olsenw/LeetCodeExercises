# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums.

    The distinct count of a subarray of nums is defined as:
    * Let nums[i..j] be a subarray of nums consisting of all the indices from i
      to j such that 0 <= i <= j < nums.length. Then the number of distinct
      values in nums[i..j] is called the distinct count of nums[i..j].
    
    Return the sum of the squares of distinct counts of all subarrays of nums.

    Since the answer may be very large, return it modulo 10^9 + 7.

    A subarray is a contiguous non-empty sequence of elements within an array.
    '''
    # based on Leetcode editorial
    # https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/editorial/?envType=daily-question&envId=2026-10-16
    # the power of summation math and a segment tree combined
    def sumCounts(self, nums: List[int]) -> int:
        # Binary index tree
        class BIT:
            def __init__(self, n:int):
                self.size = n
                self._tree1 = defaultdict(int)
                self._tree2 = defaultdict(int)
            def _lowbit(self, index:int) -> int:
                return index & -index
            def add(self, left:int, right:int, delta:int) -> None:
                self._add(left, delta)
                self._add(right+1, -delta)
            def query(self, left:int, right:int) -> int:
                return self._query(right) - self._query(left-1)
            def _add(self, index:int, delta:int) -> None:
                rawIndex = index
                index += 1
                while index <= self.size:
                    self._tree1[index] += delta
                    self._tree2[index] += rawIndex * delta
                    index += self._lowbit(index)
            def _query(self, index:int) -> int:
                index = min(index+1, self.size)
                rawIndex = index
                answer = 0
                while index > 0:
                    answer += rawIndex * self._tree1[index] - self._tree2[index]
                    index -= self._lowbit(index)
                return answer
        n = len(nums)
        answer = current = 0
        bit = BIT(n+10)
        seen = {}
        m = 10**9 + 7
        for i,a in enumerate(nums):
            j = seen.get(a, -1) + 1
            current = (current + bit.query(j,i) * 2 + i - j + 1) % m
            answer = (answer + current) % m
            bit.add(j, i, 1)
            seen[a] = i
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,1]
        o = 15
        self.assertEqual(s.sumCounts(i), o)

    def test_two(self):
        s = Solution()
        i = [2,2]
        o = 3
        self.assertEqual(s.sumCounts(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)