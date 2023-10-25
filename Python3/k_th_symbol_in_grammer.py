# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Build a table of n rows (1-indexed). Start by writing 0 in the 1st row. Now
    in every subsequent row, look at the previous row and replace each
    occurrence of 0 with 01, and each occurrence of 1 with 10.

    Given two integers n and k, return the kth (1-indexed) symbol in the nth row
    of a table of n rows.
    '''
    def kthGrammar_brute(self, n: int, k: int) -> int:
        row = "0"
        for _ in range(n):
            row = "".join(("01" if i == '0' else "10") for i in row)
            pass
        return 1 if row[k-1] == "1" else 0

    # number becomes way too big... python handles it due to unlimited int
    # creates the correct pattern unsure how to get answer from it
    def kthGrammar_memory_error(self, n: int, k: int) -> int:
        a = 0
        b = 1
        o = 1
        for _ in range(n):
            c = a ^ o
            a <<= b
            a |= c
            o = (o << b) + o
            b <<= 1
        # return a & (1 << (2**n - k))
        # return (a >> (k - 1)) & 1
        return 0

    # bases on leetcode tree solution
    # https://leetcode.com/problems/k-th-symbol-in-grammar/editorial/?envType=daily-question&envId=2023-10-25
    def kthGrammar(self, n: int, k: int) -> int:
        def dfs(n,k,rootval):
            if n == 1:
                return rootval
            t = 2 ** (n - 1)
            if k > (t / 2):
                a = 1 if rootval == 0 else 0
                return dfs(n - 1, k - (t / 2), a)
            else:
                a = 0 if rootval == 0 else 1
                return dfs(n - 1, k, a)
        return dfs(n, k, 0)

    # really neat math solution from leetcode editorial
    def kthGrammar_leetcode_math(self, n: int, k: int) -> int:
        count = bin(k - 1).count('1')
        return 0 if count % 2 == 0 else 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        j = 1
        o = 0
        self.assertEqual(s.kthGrammar(i,j), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = 1
        o = 0
        self.assertEqual(s.kthGrammar(i,j), o)

    def test_three(self):
        s = Solution()
        i = 2
        j = 2
        o = 1
        self.assertEqual(s.kthGrammar(i,j), o)

    def test_four(self):
        s = Solution()
        i = 6
        j = 10
        o = 0
        self.assertEqual(s.kthGrammar(i,j), o)

    def test_five(self):
        s = Solution()
        i = 30
        j = 434991989
        o = 0
        self.assertEqual(s.kthGrammar(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)