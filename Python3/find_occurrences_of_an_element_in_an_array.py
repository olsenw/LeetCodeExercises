# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums, an integer array queries, and an integer x.

    For each queries[i], find the index of the queries[i]th occurrence of x in
    the nums array. If there are fewer than queries[i] occurrences of x, the
    answer should be -1 for that query.

    Return an integer array answer containing the answers to all queries.
    '''
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        indices = [i for i,j in enumerate(nums) if j == x]
        return [indices[q-1] if q <= len(indices) else -1 for q in queries]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,1,7]
        j = [1,3,2,4]
        k = 1
        o = [0,-1,2,-1]
        self.assertEqual(s.occurrencesOfElement(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3]
        j = [10]
        k = 5
        o = [-1]
        self.assertEqual(s.occurrencesOfElement(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)