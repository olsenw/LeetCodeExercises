# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There is a ballgame with strange rules for keeping score. The game
    consists of several rounds where the scores of past rounds may
    affect the scores of future rounds.

    At the beginning of the game, start with an empty record. Given a
    list of strings ops, where ops[i] is the ith operation to apply to
    record according to the following rules:
    * An integer x - Record an new score of x.
    * "+" - Record a new score that is the sum of the previous two
      scores. It is guaranteed there will always be two previous scores.
    * "D" - Record a new score that is double the previous score. It is
      guaranteed there will always be a previous score.
    * "C" - Invalidate the previous score, removing it from the record.
      It is guaranteed there will always be a previous score.
    
    Return the sum of all the scores on record.
    '''
    def calPoints(self, ops: List[str]) -> int:
        s = []
        for o in ops:
            if o == "+":
                s.append(s[-1] + s[-2])
            elif o == "D":
                s.append(2 * s[-1])
            elif o == "C":
                s.pop()
            else:
                s.append(int(o))
        return sum(s)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["5","2","C","D","+"]
        o = 30
        self.assertEqual(s.calPoints(i), o)

    def test_two(self):
        s = Solution()
        i = ["5","-2","4","C","D","9","+","+"]
        o = 27
        self.assertEqual(s.calPoints(i), o)

    def test_three(self):
        s = Solution()
        i = ["1"]
        o = 1
        self.assertEqual(s.calPoints(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)