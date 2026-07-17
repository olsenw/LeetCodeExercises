# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of length n and an integer array queries.

    Let gcdPairs denote an array obtained by calculating the GCD of all possible
    pairs (nums[i], nums[j]), where 0 <= i < j < n, and then sorting these
    values in ascending order.

    For each query queries[i], find the element at index queries[i] in gcdPairs.

    Return an integer array answer, where answer[i] is the value at
    gcdPairs[queries[i]] for each query.

    The term gcd(a,b) denotes the greatest common divisor of a and b.
    '''
    # O(n^2) time and space
    def gcdValues_brute(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        gcdPairs = []
        for i in range(n):
            for j in range(i+1,n):
                gcdPairs.append(math.gcd(nums[i],nums[j]))
        gcdPairs.sort()
        return [gcdPairs[i] for i in queries]

    # Based on Leetcode Editorial
    # https://leetcode.com/problems/sorted-gcd-pair-queries/editorial/?envType=daily-question&envId=2026-07-17
    # O(mlogm + qlogm) time O(m) space
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        # The largest possible GCD in nums
        m = max(nums)
        # number times each possible GCD occurs
        count = [0] * (m + 1)
        # get GCD of each self (ie gcd(a,a))
        for num in nums:
            count[num] += 1
        # for each GCD update all multiples
        for i in range(1, m+1):
            # increments by multiples
            for j in range(i * 2, m+1, i):
                count[i] += count[j]
        for i in range(1, m+1):
            count[i] = count[i] * (count[i] - 1) // 2
        # for each GCD decrement higher value multiples (get exact count for gcd i)
        for i in range(m, 0, -1):
            # increments by multiples
            for j in range(i*2, m+1, i):
                count[i] -= count[j]
        # prefix sum for binary search later
        for i in range(1, m+1):
            count[i] += count[i-1]
        # calculate answer
        answer = []
        for q in queries:
            q += 1
            i = bisect.bisect_left(count, q)
            answer.append(i)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,3,4]
        j = [0,2,2]
        o = [1,2,2]
        self.assertEqual(s.gcdValues(i,j), o)

    def test_two(self):
        s = Solution()
        i = [4,4,2,1]
        j = [5,3,1,0]
        o = [4,2,1,1]
        self.assertEqual(s.gcdValues(i,j), o)

    def test_three(self):
        s = Solution()
        i = [2,2]
        j = [0,0]
        o = [2,2]
        self.assertEqual(s.gcdValues(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)