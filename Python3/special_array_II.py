# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    An array is considered special if every pair of its adjacent elements
    contains two numbers with different parity.

    Given an array of integer nums and a 2D integer matrix queries, where for
    queries[i] = [fromi, toi], check that the subarray nums[fromi..toi] is
    special or not.

    Return an array of booleans answer such that answer[i] is true if
    nums[fromi..toi] is special.
    '''
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        answer = []
        parity = []
        x,y = 0,0
        for i in range(len(nums) - 1):
            p = nums[i] % 2 != nums[i+1] % 2
            if p:
                if x == y:
                    x,y = i, i + 1
                else:
                    y = i + 1
            else:
                if x < y:
                    parity.append([x,y])
                x,y = i,i
        if x < y:
            parity.append([x,y])
        for a,b in queries:
            if a == b:
                answer.append(True)
            else:
                i = bisect.bisect_left(parity, a, key=lambda i:i[0])
                if i == len(parity) or a < parity[i][0]:
                    if i == 0:
                        answer.append(False)
                    else:
                        answer.append(parity[i-1][0] <= a < b <= parity[i-1][1])
                else:
                    answer.append(parity[i][0] <= a < b <= parity[i][1])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,4,1,2,6,6,7,8,9,9], [[0,4]]
        o = [False]
        self.assertEqual(s.isArraySpecial(*i), o)

    def test_two(self):
        s = Solution()
        i = [4,3,1,6], [[0,2],[2,3]]
        o = [False,True]
        self.assertEqual(s.isArraySpecial(*i), o)

    def test_three(self):
        s = Solution()
        i = [2,7,2], [[0,0],[1,2]]
        o = [True,True]
        self.assertEqual(s.isArraySpecial(*i), o)

    def test_four(self):
        s = Solution()
        i = [2,2,3,6,8,7,4,9], [[2,3]]
        o = [True]
        self.assertEqual(s.isArraySpecial(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)