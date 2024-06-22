# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers nums and an integer k. A continuous subarray is
    called nice if there are k odd numbers on it.

    Return the number of nice subarrays.
    '''
    def numberOfSubarrays_wrong(self, nums: List[int], k: int) -> int:
        answer = 0
        nums = [n % 2 for n in nums]
        c = 0
        i = 0
        for j in range(len(nums)):
            c += nums[j]
            if c == k:
                answer += 1
            while c > k:
                answer += 1
                c -= nums[i]
                i += 1
        return answer

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        answer = 0
        nums = [n % 2 for n in nums]
        d = deque()
        i = 0
        for j in range(len(nums)):
            if nums[j] == 1:
                d.append(j)
            if len(d) > k:
                i = d.popleft() + 1
            if len(d) == k:
                answer += d[0] - i + 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,2,1,1]
        j = 3
        o = 2
        self.assertEqual(s.numberOfSubarrays(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,4,6]
        j = 1
        o = 0
        self.assertEqual(s.numberOfSubarrays(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,1,1,1,2,2,2,1,2,2,1,2,2,2,1]
        j = 2
        o = 16
        self.assertEqual(s.numberOfSubarrays(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)