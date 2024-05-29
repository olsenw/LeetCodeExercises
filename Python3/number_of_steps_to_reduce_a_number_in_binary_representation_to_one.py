# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given the binary representation of an integer as a string s, return the
    number of steps to reduce it to 1 under the following rules:
    * If the current number is even, it must be divided by 2.
    * If the current number is odd, it must have 1 added to it.

    It is guaranteed that one can be reached for all test cases.
    '''
    def numSteps(self, s: str) -> int:
        answer = 0
        s = deque(s)
        while len(s) > 1:
            # add one to an odd number
            if s[-1] == '1':
                answer += 1
                for i in range(len(s) - 2, -1, -1):
                    if s[i] == '0':
                        s[i] = '1'
                        break
                    s[i] = '0'
                else:
                    s.appendleft('1')
            # do the division on an even number and right shift by one
            s.pop()
            answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "1101"
        o = 6
        self.assertEqual(s.numSteps(i), o)

    def test_two(self):
        s = Solution()
        i = "10"
        o = 1
        self.assertEqual(s.numSteps(i), o)

    def test_three(self):
        s = Solution()
        i = "1"
        o = 0
        self.assertEqual(s.numSteps(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)