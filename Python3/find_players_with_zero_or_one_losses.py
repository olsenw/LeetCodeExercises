# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from sortedcontainers import SortedDict,SortedSet

class Solution:
    '''
    Given an integer array matches where matches[i] = [winneri, loseri]
    indicates that the player winneri defeated player loseri in a match.

    Return a list of size 2 where:
    * answer[0] is a list of all the players that have not lost any matches.
    * answer[1] is a list of all players that have lost exactly one match.

    The values in the two lists should be returned in increasing order.

    Notes:
    * Only consider players that have player at least one match.
    * The testcases are generated such that no two matches have the same
      outcome.
    '''
    # passes (very slow)
    def findWinners_slow(self, matches: List[List[int]]) -> List[List[int]]:
        participated = SortedDict()
        for w,l in matches:
            if w not in participated:
                participated[w] = 0
            if l not in participated:
                participated[l] = 0
            participated[l] += 1
        answer = [[],[]]
        for p in participated:
            if participated[p] < 2:
                answer[participated[p]].append(p)
        return answer

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        participant = set()
        # undefeated = SortedSet()
        undefeated = set()
        # single = SortedSet()
        single = set()
        for w,l in matches:
            # see if the winner has appeared before
            if w not in participant:
                undefeated.add(w)
                participant.add(w)
            # deal with the loser
            if l in participant:
                if l in undefeated:
                    undefeated.remove(l)
                    single.add(l)
                elif l in single:
                    single.remove(l)
                    participant.add(l)
            else:
                participant.add(l)
                single.add(l)
        # return [list(undefeated),list(single)]
        return [sorted(undefeated),sorted(single)]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
        o = [[1,2,10],[4,5,7,8]]
        self.assertEqual(s.findWinners(i), o)

    def test_two(self):
        s = Solution()
        i = [[2,3],[1,3],[5,4],[6,4]]
        o = [[1,2,5,6],[]]
        self.assertEqual(s.findWinners(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)