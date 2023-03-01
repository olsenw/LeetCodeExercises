# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers nums, sort the array in ascending order and
    return it.

    Solve the problem without using any built-in functions in O(n log n) time
    complexity and with the smallest space complexity possible.
    '''
    # breaking the rules by using sort
    def sortArray_invalid_sort(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums

    # probably also invalid
    # correct answer... just abuses python's built in heap
    def sortArray_invalid_queue(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        return [heapq.heappop(nums) for _ in range(len(nums))]

    # Counting Sort (Frequency sort)
    # O(n + k) time [n = number elements][k = range of values]
    def sortArray(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        index = 0
        for i in range(min(nums), max(nums) + 1):
            if i in c:
                while c[i] > 0:
                    c[i] -= 1
                    nums[index] = i
                    index += 1
        return nums

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,2,3,1]
        o = [1,2,3,5]
        self.assertEqual(s.sortArray(i), o)

    def test_two(self):
        s = Solution()
        i = [5,1,1,2,0,0]
        o = [0,0,1,1,2,5]
        self.assertEqual(s.sortArray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)