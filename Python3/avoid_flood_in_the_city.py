# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A country has an infinite number of lakes. Initially, all the lakes are
    empty, but when it rains over the nth lake, the nth lake becomes full of
    water. If it rains over a lake that is full of water, there will be a flood.
    The goal is to avoid floods in any lake.

    Given an integer array rains where:
    * rains[i] > 0 means there will be rains over the rains[i] lake.
    * rains[i] == 0 means there are no rains this day and it is possible to
      choose one lake and dry it.
    
    Return an array ans where:
    * ans.length == rains.length
    * ans[i] == -1 if rains[i] > 0.
    * ans[i] is the lake chosen to dry on the ith day if rains[i] == 0.

    If there are multiple valid answers return any of them. If it is impossible
    to avoid flood return an empty array.
    '''
    # does not account for dry vs flood correctly
    def avoidFlood_fails(self, rains: List[int]) -> List[int]:
        n = len(rains)
        answer = []
        dry = 0
        lakes = set()
        for i in range(n):
            if rains[i] == 0:
                dry += 1
            elif rains[i] not in lakes:
                lakes.add(rains[i])
            elif dry > 0:
                dry -= 1
                answer.append(rains[i])
            else:
                return []
        ans = []
        j = 0
        for i in range(n):
            if rains[i] == 0:
                if j < len(answer):
                    ans.append(answer[j])
                    j += 1
                else:
                    ans.append(1)
            else:
                ans.append(-1)
        return ans

    # brute force dry lake search
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        answer = [-1] * n
        lakes = dict()
        dry = []
        for i,j in enumerate(rains):
            if j == 0:
                dry.append(i)
                answer[i] = 1
            elif j not in lakes:
                lakes[j] = i
            else:
                for k in range(len(dry)):
                    if lakes[j] < dry[k]:
                        lakes[j] = i
                        break
                if lakes[j] == i:
                    answer[dry[k]] = j
                    del dry[k]
                else:
                    return []
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4]
        o = [-1,-1,-1,-1]
        self.assertEqual(s.avoidFlood(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,0,0,2,1]
        o = [-1,-1,2,1,-1,-1]
        self.assertEqual(s.avoidFlood(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,0,1,2]
        o = []
        self.assertEqual(s.avoidFlood(i), o)

    def test_four(self):
        s = Solution()
        i = [69,0,0,0,69]
        o = [-1,69,1,1,-1]
        self.assertEqual(s.avoidFlood(i), o)

    def test_five(self):
        s = Solution()
        i = [0,1,1]
        o = []
        self.assertEqual(s.avoidFlood(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)