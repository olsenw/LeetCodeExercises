# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Write an algorithm to determine if a number n is happy.

    A happy number is a number defined by the following process:
    * Starting with any positive integer, replace the number by the sum of the
      squares of its digits.
    * Repeat the process until the number equals 1 (where it will stay), or
      loops endlessly in a cycle which does not include 1.
    * Those numbers for which this process ends in 1 are happy.

    Return true if n is a happy number, and false if not.
    '''
    # brute...
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            temp = 0
            while n > 0:
                temp += (n % 10) ** 2
                n //= 10
            if temp == 1:
                return True
            n = temp
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 19
        o = True
        self.assertEqual(s.isHappy(i), o)

    def test_two(self):
        s = Solution()
        i = 2
        o = False
        self.assertEqual(s.isHappy(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)