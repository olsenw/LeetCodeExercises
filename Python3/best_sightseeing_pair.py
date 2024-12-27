# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array values where values[i] represents the value of the
    ith sightseeing spot. Two sightseeing spots i and j have a distance j - i
    between them.

    The score of a pair (i < j) of sightseeing spots is
    values[i] + values[j] + i - j: the sum of the values of the sightseeing
    spots minus the distance between them.

    Return the maximum score of a pair of sightseeing spots.
    '''
    def maxScoreSightseeingPair_brute(self, values: List[int]) -> int:
        answer = 0
        for j in range(1,len(values)):
            for i in range(j):
                answer = max(answer, values[i] + values[j] + i - j)
        return answer
    
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        answer = 0
        a,b = values[0],0
        for i in range(1,len(values)):
            answer = max(answer, values[i] + a + b - i)
            if values[i] > a + b - i:
                a,b = values[i], i
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [8,1,5,2,6]
        o = 11
        self.assertEqual(s.maxScoreSightseeingPair(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2]
        o = 2
        self.assertEqual(s.maxScoreSightseeingPair(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1,5,8,2,6]
        o = 12
        self.assertEqual(s.maxScoreSightseeingPair(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)