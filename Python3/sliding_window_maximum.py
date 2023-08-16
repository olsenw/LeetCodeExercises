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
    Given an array of integers nums, there is a sliding window of size k which
    is moving from the left of the array to the right of the array. It is only
    possible to see the k numbers in the window. Each time the sliding window
    moves right by one position.

    Return the max sliding window.
    '''
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = [-n for n in nums[:k]]
        heapq.heapify(h)
        c = Counter(h)
        a = [-h[0]]
        for i in range(k, len(nums)):
            c[-nums[i-k]] -= 1
            c[-nums[i]] += 1
            heapq.heappush(h, -nums[i])
            while c[h[0]] == 0:
                heapq.heappop(h)
            a.append(-h[0])
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,-1,-3,5,3,6,7]
        j = 3
        o = [3,3,5,5,6,7]
        self.assertEqual(s.maxSlidingWindow(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1]
        j = 1
        o = [1]
        self.assertEqual(s.maxSlidingWindow(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)