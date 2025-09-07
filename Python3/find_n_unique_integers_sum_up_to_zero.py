# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n, return any array containing n unique integers such that
    they add up to 0.
    '''
    def sumZero(self, n: int) -> List[int]:
        answer = []
        if n % 2 == 1:
            answer.append(0)
            n -= 1
        for i in range(1,n,2):
            answer.append(i)
            answer.append(-i)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        o = [0,1,-1,3,-3]
        self.assertEqual(s.sumZero(i), o)

    def test_two(self):
        s = Solution()
        i = 3
        o = [0,1,-1]
        self.assertEqual(s.sumZero(i), o)

    def test_three(self):
        s = Solution()
        i = 1
        o = [0]
        self.assertEqual(s.sumZero(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)