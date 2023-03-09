# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    An n-bit gray code sequence is a sequence of 2^n integers where:
    * Every integer is in the inclusive range [0, 2^n - 1]
    * The first integer is 0
    * An integer appears no more than once in the sequence
    * The binary representation of every pair of adjacent integers differs by
      exactly one bit
    * The binary representation of the first and last integers differs by
      exactly on bit.
    
    Given an integer n, return any valid n-bit gray code sequence.
    '''
    def grayCode(self, n: int) -> List[int]:
        answer = [0,1]
        for i in range(1, n):
            j = 1 << i
            for a in answer[::-1]:
                answer.append(j | a)
        return answer 

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        o = [0,1]
        self.assertEqual(s.grayCode(i), o)

    def test_two(self):
        s = Solution()
        i = 2
        o = [0,1,3,2]
        self.assertEqual(s.grayCode(i), o)

    def test_three(self):
        s = Solution()
        i = 3
        o = [0,1,3,2,6,7,5,4]
        self.assertEqual(s.grayCode(i), o)

    def test_four(self):
        s = Solution()
        i = 4
        o = [0,1,3,2,6,7,5,4,12,13,15,14,10,11,9,8]
        self.assertEqual(s.grayCode(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)