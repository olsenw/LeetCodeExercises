# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    A gene string can be represented by an 8-character long string, with choices
    from 'A', 'C', 'G', and 'T'.

    Suppose that an investigation is underway to understand a mutation from a
    gene string start to a gene string end where one mutation is defined as one
    single character changed in the gene string.

    * For example "AACCGGTT" --> "AACCGGTA" is one mutation.

    There is a gene bank that records all the valid gene mutations. A gene must
    be in the bank to make it a valid gene string.

    Given the two gene strings start and end and the gene bank, return the
    minimum number of mutations needed to mutate from start to end. If there is
    no such mutation, return -1.

    Note that the starting point is assumed to be a valid, so it might not be
    included in the bank.
    '''
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        seen = set()
        mutate = deque([(start,0)])
        while mutate:
            m, c = mutate.popleft()
            if m == end:
                return c
            seen.add(m)
            for b in bank:
                if b in seen:
                    continue
                if sum(i != j for i,j in zip(m,b)) == 1:
                    mutate.append((b,c+1))
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "AACCGGTT"
        j = "AACCGGTA"
        k = ["AACCGGTA"]
        o = 1
        self.assertEqual(s.minMutation(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = "AACCGGTT"
        j = "AAACGGTA"
        k = ["AACCGGTA","AACCGCTA","AAACGGTA"]
        o = 2
        self.assertEqual(s.minMutation(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = "AAAAACCC"
        j = "AACCCCCC"
        k = ["AAAACCCC","AAACCCCC","AACCCCCC"]
        o = 3
        self.assertEqual(s.minMutation(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = "AACCGGTT"
        j = "AACCGCTA"
        k = ["AACCGGTA","AACCGCTA","AAACGGTA"]
        o = 2
        self.assertEqual(s.minMutation(i,j,k), o)

    def test_five(self):
        s = Solution()
        i = "AAAAAAAA"
        j = "AAAAACGG"
        k = ["AAAAAAGA","AAAAAGGA","AAAAACGA","AAAAACGG","AAAAAAGG","AAAAAAGC"]
        o = 3
        self.assertEqual(s.minMutation(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)