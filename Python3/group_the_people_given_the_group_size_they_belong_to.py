# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n people that are split into some unknown number of groups. Each
    person is labeled with a unique ID from 0 to n-1.

    Given an integer array groupSizes, where groupSizes[i] is the size of the
    group that person i is in. For example if groupSizes[1] = 3, then person 1
    must be in a group of size 3.

    Return a list of groups such that each person i is in a group of size
    groupSizes[i].

    Each person should appear in exactly one group, and every person must be in
    a group. If there are multiple answers, return any of them. It is guaranteed
    that there will be at least one valid solution for the given input.
    '''
    # only works because of the guaranteed answer.
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        for i,j in enumerate(groupSizes):
            d[j].append(i)
        answer = []
        for i in d:
            while d[i]:
                answer.append([d[i].pop() for _ in range(i)])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,3,3,3,3,1,3]
        # o = [[5],[0,1,2],[3,4,6]]
        o = [[6,4,3],[2,1,0],[5]]
        self.assertEqual(s.groupThePeople(i), o)

    def test_two(self):
        s = Solution()
        i = [2,1,3,3,3,2]
        # o = [[1],[0,5],[2,3,4]]
        o = [[5,0],[1],[4,3,2]]
        self.assertEqual(s.groupThePeople(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)