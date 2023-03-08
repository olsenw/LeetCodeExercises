# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums of distinct integers, return all the possible
    permutations. The answer can be returned in any order.
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = [[n] for n in nums]
        for _ in range(len(nums) - 1):
            iteration = []
            for a in answer:
                for n in nums:
                    if n not in a:
                        iteration.append(a + [n])
            answer = iteration
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        o = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        self.assertEqual(sorted(s.permute(i)), o)

    def test_two(self):
        s = Solution()
        i = [0,1]
        o = [[0,1],[1,0]]
        self.assertEqual(sorted(s.permute(i)), o)

    def test_three(self):
        s = Solution()
        i = [1]
        o = [[1]]
        self.assertEqual(sorted(s.permute(i)), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)