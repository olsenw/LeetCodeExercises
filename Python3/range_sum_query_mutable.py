# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from itertools import accumulate
'''
Given an integer array nums, handle multiple queries of the following
types:
1) Update the value of an element in nums.
2) Calculate the sum of the elements of nums between indices left and
   right inclusive where left is <= right.
'''
# time limit exceeded
class NumArray_linear:
    '''
    Initializes the object with the integer array nums.
    '''
    # O(n) time
    def __init__(self, nums: List[int]):
        self.prefix = list(accumulate(nums))

    '''
    Updates the value of nums[index] to be val
    '''
    # O(n) time
    def update(self, index: int, val: int) -> None:
        diff = val - self.prefix[index]
        if index > 0:
            diff += self.prefix[index - 1]
        for i in range(index, len(self.prefix)):
            self.prefix[i] += diff

    '''
    Returns the sum of the elements of nums between indices left and
    right inclusive (nums[left] + nums[left + 1] + ... + nums[right]).
    '''
    # O(1) time
    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.prefix[right] - self.prefix[left - 1]
        return self.prefix[right]

# time limit exceeded
# simpler code to version above and flips update and sum complexities
class NumArray_linear_alt:
    def __init__(self, nums: List[int]):
        self.nums = nums
    # O(1) time
    def update(self, index: int, val: int) -> None:
        self.nums[index] = val
    # O(n) time
    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])

# based on leetcode solution approach 3
# https://leetcode.com/problems/range-sum-query-mutable/solution/
class NumArray_iterative_segment_tree:
    # O(n) time, doing 2n computations one for each of the 2n nodes
    # O(n) space, 2n nodes
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n * 2)
        i, j = self.n, 0
        while i < 2 * self.n:
            self.tree[i] = nums[j]
            i += 1
            j += 1
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]
    # O(log n) time, visit every level in tree
    def update(self, index: int, val: int) -> None:
        index += self.n
        self.tree[index] = val
        while index > 0:
            left = index
            right = index
            if index % 2:
                left -= 1
            else:
                right += 1
            self.tree[index // 2] = self.tree[left] + self.tree[right]
            index //= 2
    # O(log n) time, visit every level in tree
    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        s = 0
        while left <= right:
            if left % 2:
                s += self.tree[left]
                left += 1
            if not right % 2:
                s += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return s

'''
There are other ways to solve this problem
(beyond an iterative segment tree)

Recursive Approach to Segment Tres (also lazy propagation)
https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/

Binary Indexed Tree (Fenwick tree)
https://leetcode.com/problems/range-sum-query-mutable/discuss/75753/Java-using-Binary-Indexed-Tree-with-clear-explanation
'''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = NumArray([1, 3, 5])
        self.assertEqual(s.sumRange(0,2), 9)
        s.update(1,2)
        self.assertEqual(s.sumRange(0,2), 8)

if __name__ == '__main__':
    unittest.main(verbosity=2)