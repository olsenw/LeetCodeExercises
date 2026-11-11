# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given five integers cost1, cost2, costBoth, need1, and need2.

    There are three types of items available:
    * An item of type 1 costs cost1 and contributes 1 unit to the type 1
      requirement only.
    * An item of type 2 costs cost2 and contributes 2 unit to the type 2
      requirement only.
    * An item of type 3 costs costBoth and contributes 1 unit to both type 1 and
      type 2 requirements.

    Collect enough items so that the total contribution toward type 1 is at
    least nee1 and the total contribution toward type 2 is at least need2.

    Return an integer representing the minimum possible total cost of achieve
    these requirements.
    '''
    # search area too large for linear time
    def minimumCost_tle(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        answer = float('inf')
        if need1 < need2:
            need1,need2 = need2,need1
            cost1,cost2 = cost2,cost1
        for i in range(need1+1):
            a = ((need1-i) * cost1) + (max(need2-i,0) * cost2) + (i * costBoth)
            answer = min(answer,a)
        return answer

    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        a = cost1 * need1 + cost2 * need2
        b = costBoth * max(need1, need2)
        c = costBoth * min(need1,need2) + cost1 * (need1 - min(need1,need2)) + cost2 * (need2 - min(need1,need2))
        return min(a,b,c)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3,2,1,3,2
        o = 3
        self.assertEqual(s.minimumCost(*i), o)

    def test_two(self):
        s = Solution()
        i = 5,4,15,2,3
        o = 22
        self.assertEqual(s.minimumCost(*i), o)

    def test_three(self):
        s = Solution()
        i = 5,4,15,0,0
        o = 0
        self.assertEqual(s.minimumCost(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)