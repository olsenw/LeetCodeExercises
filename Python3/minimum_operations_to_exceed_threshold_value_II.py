# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums, and an integer k.

    In one operation:
    * Take the two smallest integers x and y in nums.
    * Remove x and y from nums.
    * Add min(x,y) * 2 + max(x,y) anywhere in the array.

    Note that the operation can only be applied it nums contains at least two
    elements.

    Return the minimum number of operations needed so that all elements of the
    array are greater than or equal to k.
    '''
    def minOperations(self, nums: List[int], k: int) -> int:
        answer = 0
        heapq.heapify(nums)
        while len(nums) > 1:
            x,y = heapq.heappop(nums), heapq.heappop(nums)
            if min(x,y) >= k:
                break
            heapq.heappush(nums, 2 * min(x,y) + max(x,y))
            answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,11,10,1,3]
        j = 10
        o = 2
        self.assertEqual(s.minOperations(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,1,2,4,9]
        j = 20
        o = 4
        self.assertEqual(s.minOperations(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)