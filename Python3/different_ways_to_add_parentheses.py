# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string expression of numbers and operators, return all possible
    results from computing all the different possible ways to group numbers and
    operators. The answer may be returned in any order.

    The test cases are generated such that the output values fit in a 32-bit
    integer and the number of different results does not exceed 10^4.
    '''
    ops = {'+':lambda x,y: x+y, '-':lambda x,y: x-y, '*':lambda x,y: x*y}
    @cache
    def diffWaysToCompute(self, expression: str) -> List[int]:
        answer = []
        for x,y in enumerate(expression):
            if y in self.ops:
                for i in self.diffWaysToCompute(expression[:x]):
                    for j in self.diffWaysToCompute(expression[x+1:]):
                        answer.append(self.ops[y](i,j))
        return answer if len(answer) > 0 else [int(expression)]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "2-1-1"
        o = sorted([0,2])
        self.assertEqual(sorted(s.diffWaysToCompute(i)), o)

    def test_two(self):
        s = Solution()
        i = "2*3-4*5"
        o = sorted([-34,-14,-10,-10,10])
        self.assertEqual(sorted(s.diffWaysToCompute(i)), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)