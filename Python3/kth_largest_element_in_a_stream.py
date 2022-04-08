# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

import heapq

'''
Design a class to find the kth largest element in a stream. Note that it
is the kth largest element in the sorted order, not the kth distinct
element.
'''

class Solution:
    # Initialize object with the integer k and the stream of integers
    # nums.
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums[:k] if len(nums) >= k else nums + [-10**4] * (k - len(nums))
        heapq.heapify(self.heap)
        for n in nums[k:]:
            heapq.heappushpop(self.heap, n)

    # Appends the integer val to the stream and returns the element 
    # representing the kth largest element in the stream
    def add(self, val: int) -> int:
        heapq.heappushpop(self.heap, val)
        return self.heap[0]

class Solution_alt:
    # Initialize object with the integer k and the stream of integers
    # nums.
    def __init__(self, k: int, nums: List[int]):
        self.heap = [-10**4] * k
        for n in nums:
            self.add(n)

    # Appends the integer val to the stream and returns the element 
    # representing the kth largest element in the stream
    def add(self, val: int) -> int:
        if val > self.heap[0]:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution(3, [4,5,8,2])
        self.assertEqual(s.add(3), 4)
        self.assertEqual(s.add(5), 5)
        self.assertEqual(s.add(10), 5)
        self.assertEqual(s.add(9), 8)
        self.assertEqual(s.add(4), 8)

        s = Solution_alt(3, [4,5,8,2])
        self.assertEqual(s.add(3), 4)
        self.assertEqual(s.add(5), 5)
        self.assertEqual(s.add(10), 5)
        self.assertEqual(s.add(9), 8)
        self.assertEqual(s.add(4), 8)

    def test_two(self):
        s = Solution(1, [])
        self.assertEqual(s.add(-3), -3)
        self.assertEqual(s.add(-2), -2)
        self.assertEqual(s.add(-4), -2)
        self.assertEqual(s.add(0), 0)
        self.assertEqual(s.add(4), 4)

        s = Solution_alt(1, [])
        self.assertEqual(s.add(-3), -3)
        self.assertEqual(s.add(-2), -2)
        self.assertEqual(s.add(-4), -2)
        self.assertEqual(s.add(0), 0)
        self.assertEqual(s.add(4), 4)

if __name__ == '__main__':
    unittest.main(verbosity=2)