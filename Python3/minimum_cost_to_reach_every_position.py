# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array cost of size n. Currently Alice is at position n (at
    the end of the line) in a line of n + 1 people (numbered from 0 to n).

    Alice wishes to move forward in the line, but each person in front of them
    charges a specific amount to swap places. The cost to swap with person i is
    given by cost[i].

    Alice is allowed to swap places as follows:
    * If they are in front of Alice, Alice must pay them cost[i] to swap with
      them.
    * If they are behind Alice, they can swap with Alice for free.

    Return an array answer of size n, where answer[i] is the minimum total cost
    to reach each position i in the line.
    '''
    def minCosts(self, cost: List[int]) -> List[int]:
        answer = [cost[0]]
        for c in cost[1:]:
            if c < answer[-1]:
                answer.append(c)
            else:
                answer.append(answer[-1])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,3,4,1,3,2]
        o = [5,3,3,1,1,1]
        self.assertEqual(s.minCosts(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,4,6,7]
        o = [1,1,1,1,1]
        self.assertEqual(s.minCosts(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)