# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from itertools import permutations

class Solution:
    '''
    Given a collection of numbers nums, that might contain duplicates,
    return all possible unique permutations in any order.
    '''
    def permuteUnique_itertools(self, nums: List[int]) -> List[List[int]]:
        return list(set(permutations(nums)))

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        a = []
        v = []
        for i, e in enumerate(nums):
            if e not in v:
                for p in self.permuteUnique(nums[:i]+nums[i+1:]):
                    a.append([e] + p)
                v.append(e)
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,2]
        o = [[1,1,2], [1,2,1], [2,1,1]]
        self.assertEqual(s.permuteUnique(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3]
        o = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        self.assertEqual(s.permuteUnique(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)