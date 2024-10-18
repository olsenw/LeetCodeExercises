# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from itertools import accumulate, chain, combinations
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums, find the maximum possible bitwise OR of a
    subset of nums and return the number of different non-empty subsets with the
    maximum bitwise OR.

    An array a is a subset of an array b if a can be obtained from b by deleting
    some (possibly zero) elements of b. Two subsets are considered different if
    the indices of the elements chosen are different.

    The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR
    a[a.length - 1] (0-indexed).
    '''
    # brute force based on hints
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        answer = 0
        target = 0
        for i in nums:
            target |= i
        for i in chain.from_iterable(combinations(nums, x) for x in range(1, len(nums)+1)):
            a = 0
            for j in i:
                a |= j
            if a == target:
                answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,1]
        o = 2
        self.assertEqual(s.countMaxOrSubsets(i), o)

    def test_two(self):
        s = Solution()
        i = [2,2,2]
        o = 7
        self.assertEqual(s.countMaxOrSubsets(i), o)

    def test_three(self):
        s = Solution()
        i = [3,2,1,5]
        o = 6
        self.assertEqual(s.countMaxOrSubsets(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)