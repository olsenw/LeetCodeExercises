# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string moves of length n consisting only of characters 'L', 'R', and
    '_'. The string represents movement on a number line starting from the
    origin 0.

    In the ith move, it is possible to choose one of the following directions:
    * move to the left if moves[i] = 'L' or moves[i] = '_'
    * move to the right if moves[i] = 'R' or moves[i] = '_'
    '''
    # evaluates only final position
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        c = Counter(moves)
        return abs(c['R'] - c['L']) + c['_']

    # fails because we only care about final position
    def furthestDistanceFromOrigin_fails(self, moves: str) -> int:
        answer = 0
        a = 0
        b = 0
        for m in moves:
            if m == '_':
                b += 1
            elif m == 'R':
                a += 1
            elif m == 'L':
                a -= 1
            else:
                raise ValueError(f'move {m} is not "L", "R" or "_"!') 
            answer = max(answer, abs(a) + b)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "L_RL__R"
        #   4 3 2 1 0 1 2 3
        # S         *
        # L       *
        # _     - * -
        # R       - * -
        # L     - * -
        # _   - - * - -
        # _ - - - * - - -
        # R   - - - * - - -
        o = 3
        self.assertEqual(s.furthestDistanceFromOrigin(i), o)

    def test_two(self):
        s = Solution()
        i = "_R__LL_"
        o = 5
        self.assertEqual(s.furthestDistanceFromOrigin(i), o)

    def test_three(self):
        s = Solution()
        i = "_______"
        o = 7
        self.assertEqual(s.furthestDistanceFromOrigin(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)