# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed array nums and a non-negative integer k.

    In one operation, the following can be done:
    * Choose an index i that hasn't been chosen before from the range
      [0, nums.length - 1].
    * Replace nums[i] with any integer from range [nums[i] - k, nums[i] + k].

    The beauty of the array is the length of the longest subsequence consisting
    of equal elements.

    Return the maximum possible beauty of the array nums after applying the
    operation any number of times.

    Note that the operation can be applied to each index once.

    A subsequence of an array is a new array generated from the original array
    by deleting some elements (possible none) without changing the order of the
    remaining elements.
    '''
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x:x-k)
        heap = []
        answer = 0
        for n in nums:
            pass
            while heap and heap[0] < n - k:
                heapq.heappop(heap)
            heapq.heappush(heap, n + k)
            answer = max(answer, len(heap))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,6,1,2], 2
        o = 3
        self.assertEqual(s.maximumBeauty(*i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1,1], 10
        o = 4
        self.assertEqual(s.maximumBeauty(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)