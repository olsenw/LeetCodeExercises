# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and an integer k. nums may be partitioned into
    one or more subsequences such that each element in nums appears in exactly
    one of the subsequences.

    Return the minimum number of subsequences needed such that the difference
    between the maximum and minimum values in each subsequence is at most k.

    A subsequence is a sequence that can be derived from another sequence by
    deleting some or no elements without changing the order of the remaining
    elements.
    '''
    # based on hints
    def partitionArray(self, nums: List[int], k: int) -> int:
        answer = 0
        s = sorted(nums)
        i = 0
        for j in range(len(nums)):
            if s[j] > s[i] + k:
                answer += 1
                i = j
        return answer + 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,6,1,2,5]
        j = 2
        o = 2
        self.assertEqual(s.partitionArray(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3]
        j = 1
        o = 2
        self.assertEqual(s.partitionArray(i,j), o)

    def test_three(self):
        s = Solution()
        i = [2,2,4,5]
        j = 0
        o = 3
        self.assertEqual(s.partitionArray(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)