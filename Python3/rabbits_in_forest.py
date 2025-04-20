# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a forest with an unknown number of rabbits. n rabbits are asked
    "How many rabbits have the same color as you?" and the answers are collected
    into an integer array answers where answers[i] is the answer of the ith
    rabbit.

    Given the array answers, return the minimum number of rabbits that could be
    in the forest.
    '''
    def numRabbits(self, answers: List[int]) -> int:
        answer = 0
        c = Counter(answers)
        for i in c:
            while c[i] > 0:
                answer += i + 1
                c[i] -= i + 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,2]
        o = 5
        self.assertEqual(s.numRabbits(i), o)

    def test_two(self):
        s = Solution()
        i = [10,10,10]
        o = 11
        self.assertEqual(s.numRabbits(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1,1,1]
        o = 4
        self.assertEqual(s.numRabbits(i), o)

    def test_three(self):
        s = Solution()
        i = [2,2,2,2]
        o = 6
        self.assertEqual(s.numRabbits(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)