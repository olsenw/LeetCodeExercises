# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two 0-indexed integer permutations A and B of length n.

    A prefix common array of A and B is an array C such that C[i] is equal to
    the count of numbers that are present at or before the index i in both A and
    B.

    Return the prefix common array of A and B.

    A sequence of n integers is called a permutation if it contains all integers
    from 1 to n exactly once.
    '''
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        s = set()
        answer = []
        a = 0
        for i,j in zip(A,B):
            if i in s:
                a += 1
            else:
                s.add(i)
            if j in s:
                a += 1
            else:
                s.add(j)
            answer.append(a)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,2,4]
        j = [3,1,2,4]
        o = [0,2,3,4]
        self.assertEqual(s.findThePrefixCommonArray(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,3,1]
        j = [3,1,2]
        o = [0,1,3]
        self.assertEqual(s.findThePrefixCommonArray(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)