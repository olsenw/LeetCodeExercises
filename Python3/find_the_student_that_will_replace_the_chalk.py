# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n students in a class numbered from 0 to n-1. The teacher will
    give each student a problem starting with the student number 0, then the
    student number 1, and so on until the teacher reaches the student number
    n-1. After that, the teacher will restart the process, starting with the
    student number 0 again.

    Given a 0-indexed integer array chalk and an integer k. There are initially
    k pieces of chalk. When the student number 1 is given a problem to solve,
    they will use chalk[i] pieces of chalk to solve that problem. However, if
    the current number of chalk pieces is strictly less than chalk[i], then the
    student number will be asked to replace the chalk.

    Return the index of the student that will replace the chalk pieces.
    '''
    def chalkReplacer_simulation(self, chalk: List[int], k: int) -> int:
        i = 0
        while k >= chalk[i]:
            k -= chalk[i]
            i += 1
            if i == len(chalk):
                i = 0
        return i

    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        i = 0
        while k >= chalk[i]:
            k -= chalk[i]
            i += 1
            if i == len(chalk):
                i = 0
        return i

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,1,5], 22
        o = 0
        self.assertEqual(s.chalkReplacer(*i), o)

    def test_two(self):
        s = Solution()
        i = [3,4,1,2], 25
        o = 1
        self.assertEqual(s.chalkReplacer(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)