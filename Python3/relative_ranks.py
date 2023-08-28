# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array score of size n, where score[i] is the score of the
    ith athlete in a competition. All the scores are guaranteed to be unique.

    The athletes are placed based on their scores, where the 1st place athlete
    has the highest score, the 2nd place athlete has the 2nd hightest score, and
    so on. The placement of each athlete determines their rank:
    * The 1st place athlete's rank is "Gold Medal".
    * the 2nd place athlete's rank is "Silver Medal".
    * The 3rd place athlete's rank is "Bronze Medal".
    * For the 4th place to the nth place athlete, their rank is their placement
      number (ie, the xth place athlete's rank is "x").
    
    Return an array answer of size n where answer[i] is the rank of the ith
    athlete.
    '''
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        m = {j:i for i,j in enumerate(sorted(score, reverse=True), 1)}
        answer = []
        for s in score:
            if m[s] > 3:
                answer.append(str(m[s]))
            elif m[s] == 3:
                answer.append("Bronze Medal")
            elif m[s] == 2:
                answer.append("Silver Medal")
            else:
                answer.append("Gold Medal")
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,4,3,2,1]
        o = ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
        self.assertEqual(s.findRelativeRanks(i), o)

    def test_two(self):
        s = Solution()
        i = [10,3,8,9,4]
        o = ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
        self.assertEqual(s.findRelativeRanks(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)