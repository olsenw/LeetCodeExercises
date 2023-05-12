# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed 2D integer array questions where
    questions[i] = [pointsi, brainpoweri].

    The array describes the questions of an exam, where the questions are taken
    in order. At each question a decision to solve or skip the question is made.
    Solving question i will earn pointsi points but will require that the next
    brainpoweri questions be skipped. If a questions is skipped the decsion is
    made on the next question.

    Return the maximum points that can be earned on the exam.
    '''
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        @cache
        def dp(i):
            if i >= n:
                return 0
            a,b = questions[i]
            return max(a + dp(i + b + 1), dp(i+1))
        return dp(0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[3,2],[4,3],[4,4],[2,5]]
        o = 5
        self.assertEqual(s.mostPoints(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,1],[2,2],[3,3],[4,4],[5,5]]
        o = 7
        self.assertEqual(s.mostPoints(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)