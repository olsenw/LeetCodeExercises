# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

# based on Leetcode editorial
# https://leetcode.com/problems/find-x-value-of-array-ii/editorial/?envType=daily-question&envId=2026-09-22
class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        self.k = k
        n = len(nums)
        size = 2 << n.bit_length()
        # tree[o] = pre + [multiply]
        self.tree = [[0] * (k+1) for _ in range(size)]
        self.build(nums, 1, 0, n-1)
    def makeLeaf(self, o: int, value: int) -> None:
        info = [0] * (self.k + 1)
        r = value % self.k
        info[r] = 1
        info[self.k] = r # multiply
        self.tree[o] = info
    def mergePrefix(self, left: List[int], right: List[int]) -> List[int]:
        prefix = [0] * (self.k + 1)
        multiplyLeft = left[self.k]
        multiplyRight = right[self.k]
        # remainder of the interval product
        prefix[self.k] = (multiplyLeft * multiplyRight) % self.k
        # case 1: Entirely within the left interval
        for x in range(self.k):
            prefix[x] = left[x]
        # case 2: Contains the entire left interval, follow by prefix of the right interval
        for x in range(self.k):
            prefix[(multiplyLeft * x) % self.k] += right[x]
        return prefix
    def maintain(self, o:int) -> None:
        self.tree[o] = self.mergePrefix(
            self.tree[o * 2],
            self.tree[o * 2 + 1]
        )
    def build(self, nums: List[int], o: int, l: int, r: int) -> None:
        if l == r:
            self.makeLeaf(o, nums[l])
            return
        m = (l+r) // 2
        self.build(nums, o*2, l, m)
        self.build(nums, o*2+1, m+1, r)
        self.maintain(o)
    def update(self, o: int, l: int, r: int, index: int, value: int) -> None:
        if l == r:
            self.makeLeaf(o, value)
            return
        m = (l + r) // 2
        if index <= m:
            self.update(o * 2, l, m, index, value)
        else:
            self.update(o * 2 + 1, m+1, r, index, value)
        self.maintain(o)
    def query(self, o: int, l: int, r: int, left: int, right: int) -> List[int]:
        if left <= l and r <= right:
            return self.tree[o]
        m = (l + r) // 2
        if right <= m:
            return self.query(o * 2, l, m, left, right)
        if left > m:
            return self.query(o * 2 + 1, m+1, r, left, right)
        queryLeft = self.query(o * 2, l, m, left, right)
        queryRight = self.query(o * 2 + 1, m+1, r, left, right)
        return self.mergePrefix(queryLeft, queryRight)

class Solution:
    '''
    Given an array of positive integers nums and a positive integer k. Also
    given a 2D array queries, where queries[i] = [indexi, valuei, starti, xi].

    It is possible to perform an operation once on nums, where any suffix can be
    removed from nums such that nums remains non-empty.

    The x-value of nums for a given x is defined as the number of ways to
    preform this operation so that the product of the remaining elements leaves
    a remainder of x modulo k.

    For each query in queries, determine the x-value of nums for xi after
    performing the following actions:
    * Update nums[indexi] to valuei. Only this step persists for the rest of the
      queries.
    * Remove the prefix nums[0..(starti - 1)] (where nums[0..(-1)] will be used
      to represent the empty prefix).
    
    Return an array result of size queries.length where result[i] is the answer
    for the ith query.

    A prefix of an array is a subarray that starts from the beginning of the
    array and extends to any point within it.

    A suffix of an array is a subarray that starts at any point within the array
    and extends to the end of the array.

    Note that the prefix and suffix to be chosen for the operation can be empty.

    Note that the x-value has a different definition in this version.
    '''
    # based on Leetcode editorial
    # https://leetcode.com/problems/find-x-value-of-array-ii/editorial/?envType=daily-question&envId=2026-09-22
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        segment = SegmentTree(nums, k)

        answer = []
        for index, value, start, x in queries:
            segment.update(1, 0, n-1, index, value)
            prefix = segment.query(1, 0, n-1, start, n-1)
            answer.append(prefix[x])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5]
        j = 3
        k = [[2,2,0,2],[3,3,3,0],[0,1,0,1]]
        o = [2,2,2]
        self.assertEqual(s.resultArray(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [1,2,4,8,16,32]
        j = 4
        k = [[0,2,0,2],[0,2,0,1]]
        o = [1,0]
        self.assertEqual(s.resultArray(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [1,1,2,1,1]
        j = 2
        k = [[2,1,0,1]]
        o = [5]
        self.assertEqual(s.resultArray(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = [9,10,7]
        j = 1
        k = [[0,8,1,0]]
        o = [2]
        self.assertEqual(s.resultArray(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)