# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
Given two integer arrays persons and times. In an election the ith vote was
cast for persons[i] at time times[i].

For each query at a time t, find the person that was leading the election at
time t. Votes cast at time t will count towards the query. In the case of a
tie, the most recent vote (among tied candidates) wins.

Implement the TopVotedCandidate class:
'''
class TopVotedCandidate_fails:
    '''
    Initializes the object with the persons and times arrays.
    '''
    def __init__(self, persons: List[int], times: List[int]):
        votes = [0] * len(persons)
        winner = 0
        self.d = {0:0}
        for p,t in zip(persons, times):
            votes[p] += 1
            if votes[winner] == votes[p]:
                self.d[t] = p
                winner = p
            else:
                self.d[t] = winner
        self.times = [0] + times + [10**9+1]
        self.d[10**9+1] = winner

    '''
    Returns the number of the person that was leading the election at time t
    according to the mentioned rules.
    '''
    def q(self, t: int) -> int:
        i = bisect.bisect_left(self.times, t)
        return self.d[self.times[i]]

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        vote = [0] * len(persons)
        winner = 0
        self.time = times
        self.votes = {}
        for p,t in zip(persons, times):
            vote[p] += 1
            if vote[winner] <= vote[p]:
                winner = p
            self.votes[t] = winner

    def q(self, t: int) -> int:
        i = bisect.bisect(self.time, t) - 1
        return self.votes[self.time[i]]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
        self.assertEqual(s.q(3),0)
        self.assertEqual(s.q(12),1)
        self.assertEqual(s.q(25),1)
        self.assertEqual(s.q(15),0)
        self.assertEqual(s.q(24),0)
        self.assertEqual(s.q(8),1)

if __name__ == '__main__':
    unittest.main(verbosity=2)