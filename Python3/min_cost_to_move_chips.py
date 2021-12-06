# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Have n chips where the postion of ith chip is position[i]
    
    Move all chips to the same position
    
    Can move a chip in two ways:
    * position[i] + 2 or position[i] - 2 with cost = 0
    * position[i] + 1 or position[i] - 1 with cost = 1
    
    Return minimum cost needed to move all chips to the same position
    
    Constraints:
    1 <= position.length <= 100 (maximum of 100 chios)
    1 <= position[i] <= 10^9 (chips can be placed in one of 10^9 spots)
    '''
    def minCostToMoveChips(self, position: List[int]) -> int:
        evens = 0
        odds = 0
        for i in position:
            # bitwise and to check if final bit is set
            # if it is set it must be odd
            # Traditionally would just use modulus (%) operator
            if i & 1:
                odds += 1
            else:
                evens += 1
        return min(evens, odds)

class UnitTesting(unittest.TestCase):
    # actual test to run on Solution
    def test_one(self):
        s = Solution()
        self.assertEqual(s.minCostToMoveChips([1,2,3]), 1)

    def test_two(self):
        s = Solution()
        self.assertEqual(s.minCostToMoveChips([2,2,2,3,3]), 2)

    def test_three(self):
        s = Solution()
        self.assertEqual(s.minCostToMoveChips([1,1000000000]), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)