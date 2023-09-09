# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n and an integer array rounds. There is a track that
    consists of n sectors labeled from 1 to n. A marathon will be held on this
    track, the marathon consists of m rounds. The ith round starts at sector
    rounds[i-1] and ends at sector rounds[i]. For example, round 1 starts at
    sector rounds[0] and ends at sector rounds[1].

    Return an array of the most visited sectors sorted in ascending order.

    Notice that the track is circulated in ascending order of sector numbers in
    the counter-clockwise direction.
    '''
    # simulation... brute force
    # passes because of constraints being small.
    def mostVisited_passes(self, n: int, rounds: List[int]) -> List[int]:
        visits = [0] * (n + 1)
        visits[rounds[0]] = 1
        curr = rounds[0] 
        for r in rounds[1:]:
            while curr != r:
                curr += 1
                if curr > n:
                    curr = 1
                visits[curr] += 1
        answer = []
        best = 0
        for i,j in enumerate(visits):
            if j > best:
                answer = [i]
                best = j
            elif j == best:
                answer.append(i)
        return answer

    # takes advantage that all sectors are visited once in a full rotation
    # only sectors visited in partial rotation need returned.
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        if rounds[0] <= rounds[-1]:
            return [i for i in range(rounds[0], rounds[-1] + 1)]
        else:
            return [i for i in range(1, rounds[-1] + 1)] + [i for i in range(rounds[0], n + 1)]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        j = [1,3,1,2]
        o = [1,2]
        self.assertEqual(s.mostVisited(i,j), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = [2,1,2,1,2,1,2,1,2]
        o = [2]
        self.assertEqual(s.mostVisited(i,j), o)

    def test_three(self):
        s = Solution()
        i = 7
        j = [1,3,5,7]
        o = [1,2,3,4,5,6,7]
        self.assertEqual(s.mostVisited(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)