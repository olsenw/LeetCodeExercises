# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a 0-indexed integer array tasks, where tasks[i] represents the
    difficulty level of a task. In each round, 2 to 3 tasks of he same
    difficulty can be completed.

    Return the minimum number of rounds required to complete all the tasks, or
    -1 if it is not possible to complete all the tasks.
    '''
    def minimumRounds(self, tasks: List[int]) -> int:
        answer = 0
        c = Counter(tasks)
        for k in c:
            if c[k] == 1:
                return -1
            answer += math.ceil(c[k] / 3)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,2,3,3,2,4,4,4,4,4]
        o = 4
        self.assertEqual(s.minimumRounds(i), o)

    def test_two(self):
        s = Solution()
        i = [2,3,3]
        o = -1
        self.assertEqual(s.minimumRounds(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)