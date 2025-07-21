# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two non-negative integers num1 and num2.

    In one operation, if num1 > num2, subtract num2 from num1, otherwise
    subtract num1 from num2.

    Return the number of operations required to make either num1 == 0 or
    num2 == 0.
    '''
    def countOperations(self, num1: int, num2: int) -> int:
        answer = 0
        while num1 > 0 and num2 > 0:
            answer += 1
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2,3
        o = 3
        self.assertEqual(s.countOperations(*i), o)

    def test_two(self):
        s = Solution()
        i = 10,10
        o = 1
        self.assertEqual(s.countOperations(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)