# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers n and k.

    The cost of a binary string s is defined as the sum of all indices i
    (0-based) such that s[i] == '1'.

    A binary string is considered valid if:
    * It does not contain two consecutive '1' characters.
    * Its cost is less than or equal to k.

    Return a list of all valid binary strings of length n in any order.
    '''
    # does not calculate cost correctly
    def generateValidStrings_fails(self, n: int, k: int) -> list[str]:
        if n == 0:
            return [""]
        answer = []
        for s in self.generateValidStrings(n-1,k):
            answer.append('0' + s)
        for s in self.generateValidStrings(n-1,k-1):
            if len(s) == 0 or s[0] != '1':
                answer.append('1' + s)
        return answer
    
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        def generate(s:list[list[str,int]]) -> list[str]:
            m = len(s[0][0])
            if m == n:
                return [i[0] for i in s]
            answer = []
            for i,j in s:
                answer.append([i + '0', j])
                if i[-1] != '1' and j + m <= k:
                    answer.append([i + '1', j + m])
            return generate(answer)
        return generate([["0",0],["1",0]])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = 1
        o = ["000","010","100"]
        self.assertEqual(s.generateValidStrings(i,j), o)

    def test_two(self):
        s = Solution()
        i = 1
        j = 0
        o = ["0","1"]
        self.assertEqual(s.generateValidStrings(i,j), o)

    def test_three(self):
        s = Solution()
        i = 4
        j = 4
        o = ["0000","0001","0010","0100","0101","1000","1001","1010"]
        self.assertEqual(s.generateValidStrings(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)