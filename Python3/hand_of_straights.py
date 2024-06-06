# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Alice has some number of cards and she wants to rearrange the cards into
    groups so that each group is of size groupSize, and consists of groupSize
    consecutive cards.

    Given an integer array hand where hand[i] is the value written on the ith
    card and an integer groupSize, return true if she can rearrange the cards,
    or false otherwise.
    '''
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True
        hand.sort()
        d = defaultdict(list)
        answer = 0
        for h in hand:
            if len(d[h]):
                c = d[h].pop() + 1
                if c == groupSize:
                    answer -= 1
                else:
                    d[h+1].append(c)
            else:
                d[h+1].append(1)
                answer += 1
        return answer == 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,6,2,3,4,7,8]
        j = 3
        o = True
        self.assertEqual(s.isNStraightHand(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5]
        j = 6
        o = False
        self.assertEqual(s.isNStraightHand(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)