# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    There is a programming language with only four operations and one variable
    X:
    * ++X and X++ increments the value of the variable X by 1.
    * --X and X-- decrements the value of the variable X by 1.

    Initially, the value of X is 0.

    Given an array of string operations containing a list of operations, return
    the final value of X after performing all the operations.
    '''
    def finalValueAfterOperations_counter(self, operations: List[str]) -> int:
        c = Counter(operations)
        return c['X++'] + c['++X'] - c['X--'] - c['--X']

    def finalValueAfterOperations(self, operations: List[str]) -> int:
        s = 0
        for n in operations:
            if "--X" == n or "X--" == n:
                s -= 1
            else:
                s += 1
        return s

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["--X","X++","X++"]
        o = 1
        self.assertEqual(s.finalValueAfterOperations(i), o)

    def test_two(self):
        s = Solution()
        i = ["++X","++X","X++"]
        o = 3
        self.assertEqual(s.finalValueAfterOperations(i), o)

    def test_three(self):
        s = Solution()
        i = ["X++","++X","--X","X--"]
        o = 0
        self.assertEqual(s.finalValueAfterOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)