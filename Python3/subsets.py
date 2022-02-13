# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array nums of unique elements, return all possible
    subsets (the power set).

    The solution set must not contain duplicate subsets. Return the 
    solution in any order
    '''
    # use itertools to generate the combinations of given length
    def subsets_itertools(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        subsets = []
        for l in range(0, len(nums) + 1):
            for s in combinations(nums, l):
                subsets.append(list(s))
        return subsets

    # in example the new element is added to all the perexisting subsets
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for n in nums:
            for s in subsets[:len(subsets)]:
                subsets.append(s + [n])
        return subsets

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        o = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        a = s.subsets_itertools(i)
        a.sort()
        o.sort()
        self.assertEqual(a, o)
        a = s.subsets(i)
        a.sort()
        self.assertEqual(a, o)

    def test_two(self):
        s = Solution()
        i = [0]
        o = [[],[0]]
        a = s.subsets_itertools(i)
        a.sort()
        o.sort()
        self.assertEqual(a, o)
        a = s.subsets(i)
        a.sort()
        self.assertEqual(a, o)

if __name__ == '__main__':
    unittest.main(verbosity=2)